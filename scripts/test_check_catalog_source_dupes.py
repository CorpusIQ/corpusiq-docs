#!/usr/bin/env python3
"""Regression tests for check_catalog_source_dupes.py."""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_catalog_source_dupes as gate  # noqa: E402

CATALOG = os.path.join("hermes", "skills", "catalog")


def write(root: str, rel: str, text: str) -> None:
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def guide(slug: str, owner_repo: str, host: str = "skills.sh") -> str:
    return (
        "---\n"
        f"title: \"{slug}\"\n"
        "last_updated: \"2026-11-09\"\n"
        "---\n\n"
        f"# {slug}\n\n"
        f"**Source:** [{owner_repo}](https://www.{host}/{owner_repo}) via skills.sh\n"
    )


def alias_map(root: str, mapping: dict, retired_ok: dict | None = None) -> None:
    write(
        root,
        os.path.join("scripts", "catalog_source_aliases.json"),
        json.dumps({"aliases": mapping, "retired_ok": retired_ok or {}}),
    )


class RetiredPublisherGateTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def run_gate(self) -> int:
        return gate.main(["--root", self.root])

    def test_current_identity_passes(self) -> None:
        alias_map(self.root, {"old/repo": "new/repo"})
        write(self.root, os.path.join(CATALOG, "a-setup.md"), guide("a", "new/repo"))
        self.assertEqual(self.run_gate(), 0)

    def test_retired_identity_fails(self) -> None:
        alias_map(self.root, {"old/repo": "new/repo"})
        write(self.root, os.path.join(CATALOG, "a-setup.md"), guide("a", "old/repo"))
        self.assertEqual(self.run_gate(), 1)

    def test_retired_identity_fails_even_alone(self) -> None:
        # The duplicate is the symptom; a stale owner name on a live page is the
        # same defect one step earlier, so it fails before the twin exists.
        alias_map(self.root, {"old/repo": "new/repo"})
        write(self.root, os.path.join(CATALOG, "only-setup.md"), guide("only", "old/repo"))
        self.assertEqual(self.run_gate(), 1)

    def test_retired_identity_without_alias_passes(self) -> None:
        # The gate cannot invent identity offline: an unrecorded rename is
        # invisible until the alias row is added, which is why the map is part
        # of the fix rather than an optional extra.
        alias_map(self.root, {})
        write(self.root, os.path.join(CATALOG, "a-setup.md"), guide("a", "old/repo"))
        self.assertEqual(self.run_gate(), 0)

    def test_recorded_exception_is_allowed(self) -> None:
        alias_map(
            self.root,
            {"old/repo": "new/repo"},
            {"old/repo": "kept for a redirect surface with no live twin"},
        )
        write(self.root, os.path.join(CATALOG, "a-setup.md"), guide("a", "old/repo"))
        self.assertEqual(self.run_gate(), 0)

    def test_many_guides_for_one_current_monorepo_pass(self) -> None:
        # Deliberate: nousresearch/hermes-agent carries one page per skill.
        # Grouping by repository would delete real pages, so the gate does not.
        alias_map(self.root, {"old/repo": "new/repo"})
        for idx in range(5):
            write(
                self.root,
                os.path.join(CATALOG, f"skill-{idx}-setup.md"),
                guide(f"skill-{idx}", "new/repo"),
            )
        self.assertEqual(self.run_gate(), 0)

    def test_github_source_line_is_read(self) -> None:
        alias_map(self.root, {"old/repo": "new/repo"})
        write(
            self.root,
            os.path.join(CATALOG, "a-setup.md"),
            guide("a", "old/repo", host="github.com"),
        )
        self.assertEqual(self.run_gate(), 1)

    def test_skills_sh_urls_in_the_body_are_not_the_identity(self) -> None:
        alias_map(self.root, {"old/repo": "new/repo"})
        body = (
            "---\ntitle: \"b\"\n---\n\n# b\n\n"
            "**Source:** [new/repo](https://www.skills.sh/new/repo)\n\n"
            "```bash\nnpx skills add https://www.skills.sh/old/repo\n```\n"
        )
        write(self.root, os.path.join(CATALOG, "b-setup.md"), body)
        self.assertEqual(self.run_gate(), 0)

    def test_guide_without_a_source_line_is_skipped(self) -> None:
        alias_map(self.root, {"old/repo": "new/repo"})
        write(
            self.root,
            os.path.join(CATALOG, "hand-setup.md"),
            "---\ntitle: \"x\"\n---\n\n# x\n\nNo source row here.\n",
        )
        self.assertEqual(self.run_gate(), 0)

    def test_index_pages_are_not_scanned(self) -> None:
        alias_map(self.root, {"old/repo": "new/repo"})
        write(
            self.root,
            os.path.join(CATALOG, "index.md"),
            "**Source:** [x](https://www.skills.sh/old/repo)\n",
        )
        self.assertEqual(self.run_gate(), 0)


if __name__ == "__main__":
    unittest.main()
