#!/usr/bin/env python3
"""Unit tests for scripts/repair_changelog_faq.py.

Regression guards for the 2026-11-10 defect class: a generated changelog page
whose FAQ contradicted its own Release Date, whose "what changed" answer ended
mid-sentence with a literal "...", and whose sanitized em dashes rendered as
"word  -  word". Run: python -m unittest scripts/test_repair_changelog_faq.py
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import repair_changelog_faq as rcf  # noqa: E402

PAGE = """---
title: "Hermes Agent v9.9.9 Patch Release"
---

# Hermes Agent v9.9.9

**Release Date:** November 9, 2026

> Patch release. Rolls up the window since the last tag. Full curated notes ship later.

## Frequently Asked Questions

### What changed in Hermes Agent v9.9.9?

Patch release. Rolls up the window since the last tag. Full curated notes for...

### When was Hermes Agent v9.9.9 released?

November 10, 2026
"""


class TestCompleteAnswer(unittest.TestCase):
    def test_never_ends_mid_clause(self):
        out = rcf.complete_answer("First sentence here. Second sentence continues the story of the release.")
        self.assertFalse(out.endswith("..."))
        self.assertTrue(out.endswith("."))
        self.assertIn("First sentence here.", out)

    def test_adds_sentences_within_budget(self):
        # "A." is 2 chars; adding " B." needs 5 - budget 4 forces the stop.
        self.assertEqual(rcf.complete_answer("A. B. C. D.", budget=4), "A.")
        self.assertEqual(rcf.complete_answer("A. B. C. D.", budget=5), "A. B.")

    def test_strips_existing_ellipsis(self):
        self.assertFalse(rcf.complete_answer("Done here. Tail...").endswith("..."))


class TestNormalizeDashes(unittest.TestCase):
    def test_collapses_double_space_dash(self):
        self.assertEqual(rcf.normalize_dashes("onward  -  highlights"), "onward - highlights")

    def test_leaves_code_fences_alone(self):
        src = "```\na  -  b\n```\nprose  -  here"
        self.assertEqual(rcf.normalize_dashes(src), "```\na  -  b\n```\nprose - here")


class TestRepairPage(unittest.TestCase):
    def _write(self, text):
        fd, path = tempfile.mkstemp(suffix=".md")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        self.addCleanup(os.remove, path)
        return path

    def test_aligns_faq_date_to_page_release_date(self):
        path = self._write(PAGE)
        rcf.repair_page(path)
        with open(path, encoding="utf-8") as fh:
            out = fh.read()
        self.assertIn("### When was Hermes Agent v9.9.9 released?\n\nNovember 9, 2026", out)
        self.assertNotIn("November 10, 2026", out)

    def test_detruncates_faq_answer(self):
        path = self._write(PAGE)
        rcf.repair_page(path)
        with open(path, encoding="utf-8") as fh:
            out = fh.read()
        self.assertNotIn("Full curated notes for...", out)
        self.assertIn("Full curated notes ship later.", out)

    def test_idempotent(self):
        path = self._write(PAGE)
        rcf.repair_page(path)
        with open(path, encoding="utf-8") as fh:
            first = fh.read()
        changes = rcf.repair_page(path)
        with open(path, encoding="utf-8") as fh:
            self.assertEqual(first, fh.read())
        self.assertEqual(changes, [])


if __name__ == "__main__":
    unittest.main()
