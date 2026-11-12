#!/usr/bin/env python3
"""Regression tests for the SEO validator's description parser.

WHY (2026-11-12)
----------------
`scripts/validate_seo.py` reported "7 pages with short description (2c)" for
pages whose frontmatter uses a YAML folded block scalar:

    description: >-
      Use CorpusIQ inside ChatGPT - available on the ChatGPT app store. Ask
      natural-language questions across your connected business tools.

The system interpreter CI runs has no PyYAML, so the parser fell through to a
plain-scalar regex that read the indicator line only and returned the 2-char
string '>-'. Every folded description looked like a 2-character description.

The live pages were fine (the rendered `meta[name=description]` was 126 and 181
characters), so the warning was noise - and noise in a pre-deploy gate is how a
real finding gets ignored. The parser now understands block scalars.

Run: python -m unittest scripts/test_validate_seo_description.py
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_seo import parse_description  # noqa: E402


FOLDED = """title: "ChatGPT Integration - CorpusIQ Docs"
description: >-
  Use CorpusIQ inside ChatGPT - available on the ChatGPT app store. Ask
  natural-language questions across your connected business tools and get
  cited answers without leaving the chat.
canonical: "https://www.corpusiq.io/docs/chatgpt-integration/"
last_updated: "2026-11-07"
"""

LITERAL = """title: "Two lines"
description: |
  First line of the description.
  Second line of the description.
tags: ["a"]
"""

PLAIN = """title: "Plain"
description: A short plain scalar description that is written on one line.
"""

QUOTED = """title: "Quoted"
description: "A quoted description, which keeps its own punctuation."
"""

EMPTY_FOLDED = """title: "Empty"
description: >-
tags: ["a"]
"""


class ParseDescriptionTests(unittest.TestCase):
    def test_folded_block_scalar_is_joined_into_one_line(self):
        desc = parse_description(FOLDED)
        self.assertIsNotNone(desc)
        self.assertGreater(len(desc), 70)
        self.assertTrue(desc.startswith("Use CorpusIQ inside ChatGPT"))
        self.assertTrue(desc.endswith("leaving the chat."))
        self.assertNotIn("\n", desc)
        self.assertNotEqual(desc.strip(), ">-")

    def test_literal_block_scalar_keeps_line_breaks(self):
        desc = parse_description(LITERAL)
        # A literal scalar keeps its line breaks; YAML clip mode leaves a
        # trailing newline, which the caller strips when measuring length.
        self.assertEqual(
            desc.rstrip("\n"),
            "First line of the description.\nSecond line of the description.",
        )

    def test_plain_scalar_still_parses(self):
        self.assertTrue(parse_description(PLAIN).startswith("A short plain scalar"))

    def test_quoted_scalar_still_parses(self):
        self.assertEqual(
            parse_description(QUOTED),
            "A quoted description, which keeps its own punctuation.",
        )

    def test_folded_scalar_with_no_body_is_short_not_crashing(self):
        self.assertEqual(parse_description(EMPTY_FOLDED), "")

    def test_missing_description_returns_none(self):
        self.assertIsNone(parse_description("title: \"No description\"\n"))

    def test_dict_frontmatter_unchanged(self):
        self.assertEqual(parse_description({"description": "from dict"}), "from dict")


class BlockScalarStopsAtNextKeyTests(unittest.TestCase):
    def test_body_stops_before_a_top_level_key(self):
        fm = (
            'description: >-\n'
            '  One folded line and a second wrapped line that reaches the\n'
            '  minimum length the validator wants to see on a page.\n'
            'canonical: "https://www.corpusiq.io/docs/x/"\n'
        )
        desc = parse_description(fm)
        self.assertNotIn("canonical", desc)
        self.assertNotIn("https://", desc)


if __name__ == "__main__":
    unittest.main(verbosity=2)
