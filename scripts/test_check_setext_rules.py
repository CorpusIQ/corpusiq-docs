#!/usr/bin/env python3
"""Regression tests for check_setext_rules.py.

Each case encodes a rendering outcome, not a string match: the gate exists
because a `---` line under prose becomes an H2 in the rendered page, which is
what production showed on 2026-11-07.
"""

from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_setext_rules as gate  # noqa: E402


def write(root: str, rel: str, text: str) -> str:
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


class SetextRuleGateTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_credit_line_above_rule_is_flagged(self) -> None:
        path = write(self.root, "a.md", "# T\n\n*Powered by CorpusIQ*\n---\n\nbody\n")
        self.assertEqual(gate.offenders(path), [4])

    def test_blank_line_above_rule_is_clean(self) -> None:
        path = write(self.root, "b.md", "# T\n\n*Powered by CorpusIQ*\n\n---\n\nbody\n")
        self.assertEqual(gate.offenders(path), [])

    def test_prose_above_rule_is_flagged(self) -> None:
        path = write(self.root, "c.md", "# T\n\nSome closing sentence.\n---\n")
        self.assertEqual(gate.offenders(path), [4])

    def test_frontmatter_close_is_not_flagged(self) -> None:
        text = '---\ntitle: "x"\nlast_updated: "2026-11-07"\nrobots: "index,follow"\n---\n\n# T\n'
        path = write(self.root, "d.md", text)
        self.assertEqual(gate.offenders(path), [])

    def test_rule_inside_fence_is_not_flagged(self) -> None:
        text = "# T\n\n```yaml\ntitle: x\n---\n```\n\nbody\n"
        path = write(self.root, "e.md", text)
        self.assertEqual(gate.offenders(path), [])

    def test_rule_under_atx_heading_is_not_flagged(self) -> None:
        path = write(self.root, "f.md", "# T\n\n## Powered by CorpusIQ\n---\n")
        self.assertEqual(gate.offenders(path), [])

    def test_run_after_closing_fence_is_not_flagged(self) -> None:
        text = "# T\n\n```bash\nls\n```\n---\n\nbody\n"
        path = write(self.root, "g.md", text)
        self.assertEqual(gate.offenders(path), [])

    def test_fix_inserts_one_blank_line_and_is_idempotent(self) -> None:
        path = write(self.root, "h.md", "# T\n\nline one\nline two\n---\n\nbody\n")
        self.assertEqual(gate.offenders(path), [5])
        self.assertTrue(gate.fix(path, 5))
        self.assertEqual(gate.offenders(path), [])
        with open(path, encoding="utf-8") as handle:
            body = handle.read()
        self.assertIn("line two\n\n---\n", body)
        self.assertEqual(gate.offenders(path), [])

    def test_directory_walk_ignores_build_dirs(self) -> None:
        write(self.root, "site/x.md", "prose\n---\n")
        write(self.root, "node_modules/y.md", "prose\n---\n")
        write(self.root, "real/z.md", "prose\n---\n")
        seen = [os.path.relpath(p, self.root) for p in gate._iter_markdown([self.root])]
        self.assertEqual(seen, [os.path.join("real", "z.md")])


if __name__ == "__main__":
    unittest.main()
