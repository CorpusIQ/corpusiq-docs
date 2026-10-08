"""Unit tests for the CI no-slash normalize + verify gate.

Exercises scripts/normalize_site_no_slash.py on synthetic site trees:
slashed artifacts must be normalized to pass; missing or duplicate canonical
tags must hard-fail (exit 1) so a broken build can never deploy.
"""

import gzip
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "normalize_site_no_slash.py"

SLASHED_SITEMAP = (
    '<?xml version="1.0"?>\n<urlset>\n'
    "  <url><loc>https://www.corpusiq.io/docs/</loc></url>\n"
    "  <url><loc>https://www.corpusiq.io/docs/CONTRIBUTING/</loc></url>\n"
    "</urlset>\n"
)
GOOD_HTML = (
    '<html><head><link rel="canonical" '
    'href="https://www.corpusiq.io/docs/foo/"></head>'
    '<body><a href="/docs/foo/">x</a> <a href="/assets/x.css">css</a></body></html>'
)
NO_CANON = '<html><head></head><body><a href="/docs/foo/">x</a></body></html>'
TWO_CANON = (
    '<html><head><link rel="canonical" href="https://www.corpusiq.io/docs/a/">'
    '<link rel="canonical" href="https://www.corpusiq.io/docs/b/"></head></html>'
)


class NormalizeSiteTests(unittest.TestCase):
    def _run(self, sitemap, html):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory) / "site"
            site.mkdir()
            (site / "sitemap.xml").write_text(sitemap)
            with gzip.open(site / "sitemap.xml.gz", "wt", encoding="utf-8") as f:
                f.write(sitemap)
            (site / "index.html").write_text(html)
            (site / "llms.txt").write_text(
                "clean: https://www.corpusiq.io/docs/index.md\n"
            )
            return subprocess.run(
                [sys.executable, str(SCRIPT), str(site)],
                capture_output=True,
                text=True,
            )

    def test_slashed_input_is_normalized_and_passes(self):
        # Input is slashed; exit 0 is only possible if normalization fixed the
        # sitemap + canonical, since verify hard-fails on any slashed artifact.
        proc = self._run(SLASHED_SITEMAP, GOOD_HTML)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("Verify gate passed", proc.stdout)

    def test_missing_canonical_fails(self):
        proc = self._run(SLASHED_SITEMAP, NO_CANON)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("canonical", proc.stdout)

    def test_duplicate_canonical_fails(self):
        proc = self._run(SLASHED_SITEMAP, TWO_CANON)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("canonical", proc.stdout)


if __name__ == "__main__":
    unittest.main()
