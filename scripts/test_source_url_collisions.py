#!/usr/bin/env python3
"""Tests for scripts/check_source_url_collisions.py.

The gate exists because MkDocs silently drops one of two files that claim the
same URL. These tests pin the rule itself, so a future refactor cannot make the
gate blind without failing here.

Fixtures mirror the real repository shape: docs/ is the build root and the
content directories (hermes, connectors, ...) live at the repository root with
a symlink from docs/. That matters, because the checker reports real paths and
the index/README exemption is keyed on the real directory.
"""
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_source_url_collisions as gate  # noqa: E402


class SourceUrlCollisionTests(unittest.TestCase):
    def _repo(self, layout, links=("hermes",)):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        (root / "docs").mkdir()
        for rel in layout:
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# page\n")
        for name in links:
            if (root / name).is_dir():
                os.symlink(os.path.join("..", name), root / "docs" / name)
        return root

    def _scan(self, root):
        repo = gate.REPO
        try:
            gate.REPO = str(root)
            return gate.scan(str(root / "docs"))
        finally:
            gate.REPO = repo

    def _real(self, collisions):
        return {url: paths for url, paths in collisions.items()
                if os.path.dirname(paths[0]) not in gate.EXEMPT_DIRS}

    def test_flat_page_and_folder_index_collide(self):
        root = self._repo(["docs/connectors.md", "docs/connectors/index.md"])
        collisions, _ = self._scan(root)
        self.assertEqual(len(collisions), 1, collisions)
        (paths,) = collisions.values()
        self.assertEqual(
            sorted(os.path.basename(p) for p in paths),
            ["connectors.md", "index.md"],
        )

    def test_flat_page_and_folder_readme_collide(self):
        root = self._repo(["docs/security.md", "docs/security/README.md"])
        collisions, _ = self._scan(root)
        self.assertEqual(len(collisions), 1, collisions)

    def test_distinct_pages_do_not_collide(self):
        root = self._repo(["docs/connectors.md",
                           "docs/connectors/google-ads-for-agencies.md"])
        collisions, _ = self._scan(root)
        self.assertEqual(collisions, {})

    def test_index_and_readme_pair_is_exempt(self):
        root = self._repo(["hermes/index.md", "hermes/README.md"])
        collisions, stale = self._scan(root)
        self.assertEqual(len(collisions), 1, collisions)
        self.assertEqual(self._real(collisions), {})
        # Other exempt directories are absent from this fixture, which the
        # checker reports; the point here is that hermes itself is satisfied.
        self.assertFalse([n for n in stale if n.startswith("hermes:")], stale)

    def test_exemptions_report_when_the_pair_is_gone(self):
        root = self._repo(["hermes/index.md"])
        _, stale = self._scan(root)
        self.assertTrue([n for n in stale if n.startswith("hermes:")], stale)

    def test_repository_tree_is_clean(self):
        """The real docs tree must pass - this is the deploy-blocking condition."""
        collisions, stale = gate.scan()
        self.assertEqual(self._real(collisions), {},
                         f"source URL collisions: {self._real(collisions)}")
        self.assertEqual(stale, [], f"stale exemptions: {stale}")


if __name__ == "__main__":
    unittest.main()
