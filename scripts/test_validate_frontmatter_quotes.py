#!/usr/bin/env python3
"""Adversarial regression tests for the frontmatter quote / date gate.

WHY (2026-11-05)
----------------
PR #182 refreshed four stale hermes pages and, on two of them, rewrote
`last_updated` as:

    last_updated: 2026-11-04"

PyYAML accepts that. A plain scalar absorbs the stray trailing quote, so the
frontmatter parses as the string '2026-11-04"' - no YAML error, no duplicate
key, no truncated value, and the pre-existing validator passed. The string is
then copied verbatim into the rendered page, so two live pages served:

    "datePublished": "2026-11-04"",
    "dateModified": "2026-11-04"",

which is unparseable JSON. Search engines drop the whole node silently, so the
page loses the structured data an AI answer engine reads to date the answer.
Nothing in the pre-merge gate noticed; the defect was found by reading the
served HTML.

Three external MCP pages carried the sibling defect: a description whose
opening quote was dropped, leaving an unquoted scalar that ends with `"`.

Run: python -m unittest scripts/test_validate_frontmatter_quotes.py
"""

from __future__ import annotations

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts import validate_frontmatter as vf  # noqa: E402


class FrontmatterQuoteGateTests(unittest.TestCase):
    def issues(self, body: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "page.md")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(body)
            return vf.check_file(path)

    def assert_flagged(self, body: str, needle: str) -> None:
        found = self.issues(body)
        self.assertTrue(found, "expected a problem, got none")
        self.assertTrue(
            any(needle in issue for issue in found),
            f"expected {needle!r} in {found!r}",
        )

    # --- the exact regressions that shipped ------------------------------

    def test_stray_trailing_quote_on_last_updated(self) -> None:
        self.assert_flagged(
            '---\ntitle: "Page"\nlast_updated: 2026-11-04"\n---\n\n# Page\n',
            "double quote",
        )

    def test_unquoted_description_ending_in_quote(self) -> None:
        self.assert_flagged(
            '---\ntitle: "Prov"\n'
            "description: Hosted MCP server for returns across 32,000+ funds.\"\n"
            "---\n\n# Prov\n",
            "double quote",
        )

    def test_prose_date_is_rejected(self) -> None:
        self.assert_flagged(
            '---\ntitle: "Page"\nlast_updated: June 22, 2026\n---\n\n# Page\n',
            "bare ISO date",
        )

    def test_opening_quote_never_closed(self) -> None:
        # Caught one layer earlier than the quote rule: PyYAML itself fails.
        self.assert_flagged(
            '---\ntitle: "Page"\ndescription: "A value that never closes\n'
            "---\n\n# Page\n",
            "invalid YAML",
        )

    # --- must stay clean (false-positive control) ------------------------

    def test_correctly_quoted_date_is_clean(self) -> None:
        self.assertEqual(
            self.issues('---\ntitle: "Page"\nlast_updated: "2026-11-04"\n---\n\n# Page\n'),
            [],
        )

    def test_bare_iso_date_is_clean(self) -> None:
        self.assertEqual(
            self.issues("---\ntitle: Page\nlast_updated: 2026-11-04\n---\n\n# Page\n"),
            [],
        )

    def test_quoted_value_ending_in_single_quote_is_clean(self) -> None:
        # English prose closing a quotation inside a double-quoted scalar.
        self.assertEqual(
            self.issues(
                '---\ntitle: "Page"\n'
                "description: \"A CFO once said: 'Nobody looks at them.'\"\n"
                "---\n\n# Page\n"
            ),
            [],
        )

    def test_escaped_inner_quotes_are_clean(self) -> None:
        self.assertEqual(
            self.issues(
                '---\ntitle: "Page"\n'
                'description: "He asked \\"what changed?\\" and left."\n'
                "---\n\n# Page\n"
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()
