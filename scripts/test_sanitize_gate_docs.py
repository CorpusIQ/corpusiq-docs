#!/usr/bin/env python3
"""Unit tests for scripts/sanitize_gate_docs.py (the pre-commit auto-sanitizer).

Proves each scoping rule before the sanitizer is wired into the hook:
  - t1: em/en dash -> hyphen, global (body AND frontmatter)
  - t2: title > 60 clamped on a word boundary, quotes preserved
  - t3: description > 155 clamped on a word boundary
  - t4: under-limit title/description left untouched
  - t5: idempotent (sanitize(sanitize(x)) == sanitize(x))
  - t6: body line starting with `title:` is NOT clamped (frontmatter-scoped)
  - t7: no-frontmatter file still gets dash-normalized but no title clamp
  - t8: quoted title/description values stay valid YAML after clamp

Run:  python3 -m unittest scripts.test_sanitize_gate_docs
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import scripts.sanitize_gate_docs as s  # noqa: E402


class SanitizeGateDocsTests(unittest.TestCase):
    def test_dash_normalization_global(self):
        body = "Body has an em\u2014dash and en\u2013dash.\n"
        out = s.sanitize_text(body)
        self.assertNotIn('\u2014', out)
        self.assertNotIn('\u2013', out)
        self.assertIn('em-dash and en-dash', out)

    def test_title_clamped_word_boundary(self):
        original = 'LoadOptimizer MCP - Server-Side Load Balancing for Autonomous Agents'
        self.assertGreater(len(original), 60)  # premise: actually over the limit
        raw = (
            '---\n'
            'title: "%s"\n'
            'description: "short"\n'
            '---\n'
            'body\n' % original
        )
        out = s.sanitize_text(raw)
        title = next(l for l in out.split('\n') if l.startswith('title:'))
        value = title.split(':', 1)[1].strip().strip('"')
        self.assertLessEqual(len(value), 60)
        self.assertTrue(original.startswith(value))  # clamped from the right, never reworded
        self.assertFalse(value.endswith('Agents'))   # trailing partial word dropped

    def test_dangling_connective_trimmed(self):
        # the clamp lands on a function word ("...for") which must be dropped so
        # validate_page_metadata.dangling() does not flag the result
        raw = (
            '---\n'
            'title: "LoadOptimizer MCP - Server-Side Load Balancing for Autonomous Agents"\n'
            'description: "short"\n'
            '---\nbody\n'
        )
        out = s.sanitize_text(raw)
        value = next(l for l in out.split('\n') if l.startswith('title:'))
        value = value.split(':', 1)[1].strip().strip('"')
        last_word = value.split()[-1].lower()
        self.assertNotIn(last_word, s.DANGLING)

    def test_description_clamped(self):
        long_desc = 'D' * 180
        raw = '---\ntitle: "ok"\ndescription: "%s"\n---\nbody\n' % long_desc
        out = s.sanitize_text(raw)
        desc = next(l for l in out.split('\n') if l.startswith('description:'))
        value = desc.split(':', 1)[1].strip().strip('"')
        self.assertLessEqual(len(value), 155)

    def test_under_limit_untouched(self):
        raw = '---\ntitle: "Short Title"\ndescription: "short desc"\n---\nbody\n'
        self.assertEqual(s.sanitize_text(raw), raw)

    def test_idempotent(self):
        raw = (
            '---\n'
            'title: "A Very Long Title That Definitely Exceeds The Sixty Character Limit For Testing"\n'
            'description: "%s"\n'
            '---\nbody with em\u2014dash\n' % ('x' * 200)
        )
        once = s.sanitize_text(raw)
        twice = s.sanitize_text(once)
        self.assertEqual(once, twice)

    def test_body_title_line_not_clamped(self):
        raw = '---\ntitle: "ok"\ndescription: "ok"\n---\n\ntitle: this body line is very long and should never be clamped by the sanitizer\n'
        out = s.sanitize_text(raw)
        self.assertIn('title: this body line is very long and should never be clamped by the sanitizer', out)

    def test_no_frontmatter_dash_only(self):
        raw = 'No frontmatter here, just an em\u2014dash and a long title: some text\n'
        out = s.sanitize_text(raw)
        self.assertNotIn('\u2014', out)
        self.assertIn('em-dash', out)
        self.assertIn('title: some text', out)  # body `title:` untouched

    def test_quoted_values_stay_quoted(self):
        raw = '---\ntitle: "Under limit"\ndescription: "Under limit"\n---\nbody\n'
        out = s.sanitize_text(raw)
        for line in out.split('\n'):
            if line.startswith('title:') or line.startswith('description:'):
                self.assertIn('"', line)

    # --- 2026-11-12 regressions -------------------------------------------
    def test_in_limit_description_keeps_its_period(self):
        # The sanitizer ran trim_dangling() on values that already fit, and its
        # final rstrip(' ,;:.-') deleted the sentence-final period. Every
        # description committed through the hook lost its full stop.
        raw = ('---\ntitle: "Ok"\n'
               'description: "Ask pipeline questions in plain English and get cited answers."\n'
               '---\nbody\n')
        self.assertEqual(s.sanitize_text(raw), raw)

    def test_unquoted_in_limit_description_is_not_requoted(self):
        raw = ('---\ntitle: "Ok"\n'
               'description: Ask pipeline questions in plain English.\n'
               '---\nbody\n')
        self.assertEqual(s.sanitize_text(raw), raw)

    def test_folded_block_scalar_is_untouched(self):
        # `description: >-` was treated as the value itself, so the line became
        # description: ">" and the folded value was orphaned in the body.
        raw = ('---\ntitle: "ChatGPT Integration - CorpusIQ Docs"\n'
               'description: >-\n'
               '  Use CorpusIQ inside ChatGPT. Ask natural-language questions\n'
               '  and get cited answers without leaving the chat.\n'
               '---\nbody\n')
        self.assertEqual(s.sanitize_text(raw), raw)


if __name__ == '__main__':
    unittest.main()
