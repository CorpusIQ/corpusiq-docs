#!/usr/bin/env python3
"""Tests for scripts/check_progress_counts.py.

The gate exists because PROGRESS.md's file-count block was refreshed mid-cycle
and then a later merge invalidated it (#239 on 2026-11-07: stated 3,633 and
1,519 while main held 3,636 and 1,522). The failure modes worth pinning are
therefore narrow and specific: a parsed claim that disagrees must fail, a claim
that cannot be parsed must not fail, and the path predicates must count what
the page's own words say they count. Getting a predicate wrong would make the
gate lie in the other direction, failing a correct file.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_progress_counts as gate  # noqa: E402

# The shape of the block as PROGRESS.md writes it, in miniature.
GOOD = """
## File count (updated November 7, 2026)

- **Total Markdown files:** 3,636
- **Skills catalog:** 958 setup guides (measured: *setup*.md under hermes/skills)
- **MCP servers:** 1,522 total .md under hermes/mcp/ (measured 2026-11-07)
- **SEO pages:** 182 top-level docs pages targeting high-intent business keywords, plus 62 connector reference pages
"""

# 3,636 + 958 + 1,522 + 182 + 62 worth of paths, generated below.
def tree(total=3636, mcp=1522, setup=958, docs=182, connectors=62):
    files = []
    files += ["docs/page-%d.md" % i for i in range(docs)]
    files += ["connectors/connect-%d.md" % i for i in range(connectors)]
    files += ["hermes/skills/pkg-%d/skill-%d-setup.md" % (i, i) for i in range(setup)]
    files += ["hermes/mcp/servers/s-%d/index.md" % i for i in range(mcp)]
    rest = total - len(files)
    files += ["misc/file-%d.md" % i for i in range(rest)]
    return files


class TestPredicates(unittest.TestCase):
    def test_counts_what_the_page_says(self):
        files = tree()
        self.assertEqual(len(files), 3636)
        self.assertEqual(sum(1 for f in files if gate._md(f)), 3636)
        self.assertEqual(sum(1 for f in files if gate._under_mcp(f)), 1522)
        self.assertEqual(sum(1 for f in files if gate._setup_guide(f)), 958)
        self.assertEqual(sum(1 for f in files if gate._top_level_docs_page(f)), 182)
        self.assertEqual(sum(1 for f in files if gate._connector_reference(f)), 62)

    def test_non_markdown_and_nested_paths_are_excluded(self):
        self.assertFalse(gate._md("docs/page.html"))
        self.assertFalse(gate._setup_guide("hermes/skills/pkg/skill.md"))     # no 'setup'
        self.assertFalse(gate._setup_guide("docs/setup.md"))                  # not under hermes/skills
        self.assertFalse(gate._top_level_docs_page("docs/api/page.md"))       # nested, not top-level
        self.assertFalse(gate._connector_reference("docs/connectors/x.md"))   # different tree
        # hermes/mcp itself is not a page, the file under it is
        self.assertFalse(gate._under_mcp("hermes/mcp/"))
        self.assertTrue(gate._under_mcp("hermes/mcp/index.md"))


class TestEvaluate(unittest.TestCase):
    def test_clean_file_passes(self):
        failures, unparsed, checked = gate.evaluate(GOOD, tree())
        self.assertEqual(failures, [])
        self.assertEqual(unparsed, [])
        self.assertEqual(checked, 5)

    def test_the_nov7_drift_fails_on_both_numbers(self):
        drifted = GOOD.replace("3,636", "3,633").replace("1,522", "1,519")
        failures, _, checked = gate.evaluate(drifted, tree())
        self.assertEqual(len(failures), 2)
        labels = sorted(label for label, _, _ in failures)
        self.assertEqual(labels, ["MCP servers under hermes/mcp",
                                  "Total Markdown files"])
        for _, stated, actual in failures:
            # The message must name both numbers, never just "failed".
            self.assertNotEqual(stated, actual)

    def test_one_extra_file_fails(self):
        failures, _, _ = gate.evaluate(GOOD, tree(total=3637))
        self.assertEqual(len(failures), 1)
        self.assertEqual(failures[0][0], "Total Markdown files")

    def test_unparseable_claim_is_skipped_not_failed(self):
        reworded = GOOD.replace("Total Markdown files:", "Markdown files in total:")
        failures, unparsed, checked = gate.evaluate(reworded, tree())
        self.assertEqual(failures, [])
        self.assertEqual(unparsed, ["Total Markdown files"])
        self.assertEqual(checked, 4)

    def test_empty_text_skips_everything(self):
        failures, unparsed, checked = gate.evaluate("", tree())
        self.assertEqual(failures, [])
        self.assertEqual(checked, 0)
        self.assertEqual(len(unparsed), 5)

    def test_connector_count_is_scoped_to_its_own_clause(self):
        # 'plus N connector reference pages' must not pick up the docs number.
        text = GOOD.replace("plus 62 connector reference pages", "plus 63 connector reference pages")
        failures, _, _ = gate.evaluate(text, tree())
        self.assertEqual([f[0] for f in failures], ["Connector reference pages"])


if __name__ == "__main__":
    unittest.main()
