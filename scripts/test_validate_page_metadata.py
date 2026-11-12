"""Regression tests for the duplicated-brand <title> repair.

The site template renders page.meta.title verbatim, so a frontmatter title that
already carries the brand suffix and has it appended again reaches the SERP as
"... - CorpusIQ Docs - CorpusIQ Docs". That defect was live on 121 pages and on
the domain's highest-impression catalog page (7,483 impressions, 0.04% CTR)
before the check landed.
"""
import importlib.util
import os
import unittest

_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     'validate_page_metadata.py')
_spec = importlib.util.spec_from_file_location('validate_page_metadata', _PATH)
vpm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vpm)


class BrandDupeTest(unittest.TestCase):
    def test_flags_repeated_brand(self):
        for title in (
            'Supabase - CorpusIQ Docs - CorpusIQ',
            'Contributing to CorpusIQ Docs - CorpusIQ Docs',
            'PostgreSQL - CorpusIQ Docs - CorpusIQ',
            'New Skills - CorpusIQ Docs - CorpusIQ Docs',
        ):
            self.assertTrue(vpm.brand_dupe(title), title)

    def test_accepts_single_brand(self):
        for title in (
            'CorpusIQ MCP Troubleshooting - CorpusIQ Docs',
            'Docker Hermes Agent Setup - CorpusIQ Docs',
            'CorpusIQ vs Viktor Pricing: Flat Plans vs Credit Metering',
            'Delete Hermes Agent Sessions and Prune state.db',
        ):
            self.assertFalse(vpm.brand_dupe(title), title)


class UnbrandTest(unittest.TestCase):
    def test_collapses_to_one_suffix(self):
        cases = {
            'Supabase - CorpusIQ Docs - CorpusIQ': 'Supabase - CorpusIQ Docs',
            'PostgreSQL - CorpusIQ Docs - CorpusIQ': 'PostgreSQL - CorpusIQ Docs',
            'New Skills - CorpusIQ Docs - CorpusIQ Docs': 'New Skills - CorpusIQ Docs',
        }
        for src, want in cases.items():
            self.assertEqual(vpm.unbrand(src), want)

    def test_does_not_double_a_branded_base(self):
        src = 'Contributing to CorpusIQ Docs - CorpusIQ Docs'
        self.assertEqual(vpm.unbrand(src), 'Contributing to CorpusIQ Docs')

    def test_drops_suffix_when_base_is_long(self):
        src = ('A very long base title that goes on and on past sixty chars '
               'for sure - CorpusIQ Docs - CorpusIQ Docs')
        out = vpm.unbrand(src)
        self.assertEqual(out, 'A very long base title that goes on and on past '
                              'sixty chars for sure')
        self.assertFalse(vpm.brand_dupe(out))

    def test_repair_is_idempotent(self):
        for title in ('Supabase - CorpusIQ Docs - CorpusIQ',
                      'Contributing to CorpusIQ Docs - CorpusIQ Docs'):
            once = vpm.unbrand(title)
            self.assertEqual(vpm.unbrand(once), once)
            self.assertFalse(vpm.brand_dupe(once))


class DescCutTest(unittest.TestCase):
    """2026-11-12: descriptions shortened in place by deleting the tail.

    Both cases below shipped live. The first ends on a noun, so the dangling
    vocabulary could never see it; the second ends on 'not'.
    """

    def page(self, desc, body):
        return '---\ntitle: "T"\ndescription: "%s"\n---\n\n# T\n\n%s\n' % (desc, body)

    def test_cut_quote_of_body_copy_is_flagged(self):
        desc = ('runbook.v1 is an application-layer contract for MCP that makes '
                'execution required, versioned, and auditable. Deterministic at the host')
        body = ('Design principles - Deterministic at the host boundary, free '
                'reasoning between checkpoints. Acquisition is a host function.')
        self.assertIsNotNone(vpm.desc_cut(desc, self.page(desc, body)))

    def test_cut_on_function_word_is_flagged(self):
        desc = ('Deterministic compensation data for 3,000 US public companies '
                'as callable MCP tools. Sourced from SEC proxy filings, not')
        self.assertIsNotNone(vpm.desc_cut(desc, self.page(desc, '# Other\n\nText.')))

    def test_complete_description_with_period_passes(self):
        desc = 'Daily sweeps catalog new MCP servers, their capabilities, and integration potential.'
        body = ('Daily sweeps catalog new MCP servers, their capabilities, and '
                'integration potential. Recent sweeps document them.')
        self.assertIsNone(vpm.desc_cut(desc, self.page(desc, body)))

    def test_unpunctuated_description_before_a_new_sentence_passes(self):
        desc = ('MCP Apps is the first official MCP extension. Tools render '
                'inside Claude and ChatGPT')
        body = 'MCP Apps is the first official MCP extension, live since January 26, 2026.'
        self.assertIsNone(vpm.desc_cut(desc, self.page(desc, body)))


if __name__ == '__main__':
    unittest.main()
