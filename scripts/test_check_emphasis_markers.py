#!/usr/bin/env python3
"""Tests for scripts/check_emphasis_markers.py (class found live 2026-11-08)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_emphasis_markers as cem  # noqa: E402


class TestCheckText(unittest.TestCase):
    def test_balanced_bold_passes(self):
        ok, problems = cem.check_text("A **bold** claim and another **one**.\n")
        self.assertTrue(ok, problems)

    def test_unbalanced_bold_fails(self):
        ok, problems = cem.check_text("A **bold claim that never closes.\n")
        self.assertFalse(ok)
        self.assertTrue(any("bold" in p for p in problems), problems)

    def test_live_defect_shape_fails(self):
        """The exact DutyKit sentence that shipped broken."""
        text = (
            "The registry carries two active records under two owner names "
            "(`io.github.r08150816s-star/dutykit` **0.1.0** published "
            "`2026-11-07T16:05:01Z` and `io.github.renschrder-stack/dutykit` "
            "**0.1.1`), which reads as a rename in progress rather than two servers.\n"
        )
        ok, problems = cem.check_text(text)
        self.assertFalse(ok)
        self.assertTrue(any("backtick" in p for p in problems), problems)

    def test_repaired_sentence_passes(self):
        text = (
            "The registry carries two active records under two owner names "
            "(`io.github.r08150816s-star/dutykit` **0.1.0** published "
            "`2026-11-07T16:05:01Z` and `io.github.renschrder-stack/dutykit` "
            "**0.1.1**), which reads as a rename in progress rather than two servers.\n"
        )
        ok, problems = cem.check_text(text)
        self.assertTrue(ok, problems)

    def test_fenced_json_with_quotes_passes(self):
        text = '```json\n{"a": "b", "c": [1, 2]}\n```\n'
        ok, problems = cem.check_text(text)
        self.assertTrue(ok, problems)

    def test_fenced_block_dropped_from_counts(self):
        text = "```bash\necho `unbalanced\n```\nClean **text**.\n"
        ok, problems = cem.check_text(text)
        self.assertTrue(ok, problems)

    def test_balanced_inline_code_passes(self):
        ok, problems = cem.check_text("Run `python3 x.py` then `git status`.\n")
        self.assertTrue(ok, problems)

    def test_stray_backtick_fails(self):
        ok, problems = cem.check_text("A stray ` tick in prose.\n")
        self.assertFalse(ok)
        self.assertTrue(any("backtick" in p for p in problems), problems)

    def test_hint_lines_point_at_the_defect(self):
        text = "good line\nbad **open line\nanother line\n"
        self.assertEqual(cem.odd_lines(text, "**"), [2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
