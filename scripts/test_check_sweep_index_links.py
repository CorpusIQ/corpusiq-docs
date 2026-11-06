#!/usr/bin/env python3
"""Regression tests for check_sweep_index_links.py."""

from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_sweep_index_links as gate  # noqa: E402

MARKET = os.path.join("hermes", "skills", "marketplace")


def write(root: str, rel: str, text: str) -> None:
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def page(date: str) -> str:
    return f'---\ntitle: "x"\nlast_updated: "{date}"\n---\n\n# x\n'


class SweepIndexGateTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_recent_page_must_be_linked(self) -> None:
        write(self.root, f"{MARKET}/new-nov5-2026/index.md", page("2026-11-05"))
        write(self.root, f"{MARKET}/new-nov6-2026-morning-skills/index.md", page("2026-11-06"))
        write(
            self.root,
            f"{MARKET}/index.md",
            "## Recent Sweeps\n- [a](/hermes/skills/marketplace/new-nov5-2026)\n",
        )

        errors, _ = gate.check(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("new-nov6-2026-morning-skills", errors[0])
        self.assertIn("orphan", errors[0])

    def test_recent_page_linked_passes(self) -> None:
        write(self.root, f"{MARKET}/new-nov6-2026-morning-skills/index.md", page("2026-11-06"))
        write(self.root, f"{MARKET}/index.md", "- [a](/hermes/skills/marketplace/new-nov6-2026-morning-skills)\n")

        errors, _ = gate.check(self.root)
        self.assertEqual(errors, [])

    def test_old_page_may_age_out(self) -> None:
        write(self.root, f"{MARKET}/new-july18-2026/index.md", page("2026-07-18"))
        write(self.root, f"{MARKET}/new-nov6-2026-morning-skills/index.md", page("2026-11-06"))
        write(self.root, f"{MARKET}/index.md", "- [a](/hermes/skills/marketplace/new-nov6-2026-morning-skills)\n")

        errors, _ = gate.check(self.root)
        self.assertEqual(errors, [])

    def test_stamp_bump_on_old_page_is_ignored(self) -> None:
        """The 2026-11-01 freshness sweep restamped July/August pages."""
        write(self.root, f"{MARKET}/new-aug10-2026/index.md", page("2026-11-01"))
        write(self.root, f"{MARKET}/new-nov6-2026-morning-skills/index.md", page("2026-11-06"))
        write(self.root, f"{MARKET}/index.md", "- [a](/hermes/skills/marketplace/new-nov6-2026-morning-skills)\n")

        errors, _ = gate.check(self.root)
        self.assertEqual(errors, [])

    def test_month_only_slug_dates_to_first_of_month(self) -> None:
        write(self.root, f"{MARKET}/new-june-2026/index.md", page("2026-11-01"))
        write(self.root, f"{MARKET}/new-nov6-2026-morning-skills/index.md", page("2026-11-06"))
        write(self.root, f"{MARKET}/index.md", "- [a](/hermes/skills/marketplace/new-nov6-2026-morning-skills)\n")

        errors, _ = gate.check(self.root)
        self.assertEqual(errors, [])

    def test_dangling_link_fails(self) -> None:
        write(self.root, f"{MARKET}/new-nov6-2026-morning-skills/index.md", page("2026-11-06"))
        write(
            self.root,
            f"{MARKET}/index.md",
            "- [a](/hermes/skills/marketplace/new-nov6-2026-morning-skills)\n"
            "- [b](/hermes/skills/marketplace/new-nov7-2026-skills)\n",
        )

        errors, _ = gate.check(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("dangling", errors[0])

    def test_missing_index_fails(self) -> None:
        write(self.root, f"{MARKET}/new-nov6-2026-morning-skills/index.md", page("2026-11-06"))

        errors, _ = gate.check(self.root)
        self.assertTrue(any("missing marketplace index" in error for error in errors))

    def test_undated_page_is_ignored(self) -> None:
        write(self.root, f"{MARKET}/new-nov6-2026-morning-skills/index.md", "# no frontmatter\n")
        write(self.root, f"{MARKET}/index.md", "- [a](/hermes/skills/marketplace/new-nov6-2026-morning-skills)\n")

        errors, _ = gate.check(self.root)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
