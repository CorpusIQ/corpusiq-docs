#!/usr/bin/env python3
import io
from pathlib import Path
import sys
import tempfile
import unittest
from contextlib import redirect_stderr

# Importable from the repo root as well as from scripts/, because CI runs this as
# `python -m unittest scripts/test_stabilize_hashed_assets.py`.
sys.path.insert(0, str(Path(__file__).resolve().parent))

import stabilize_hashed_assets as sha


class StabilizeHashedAssetsTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.site = Path(self.tempdir.name)
        (self.site / "assets" / "stylesheets").mkdir(parents=True)
        (self.site / "assets" / "javascripts").mkdir(parents=True)
        (self.site / "stylesheets").mkdir(parents=True)
        (self.site / "javascripts").mkdir(parents=True)
        (self.site / "images").mkdir(parents=True)
        (self.site / "nested").mkdir(parents=True)

    def tearDown(self):
        self.tempdir.cleanup()

    def _write_fixture(self):
        (self.site / "assets" / "stylesheets" / "main.abcdef12.min.css").write_text(
            "body { color: black; }",
            encoding="utf-8",
        )
        (self.site / "assets" / "javascripts" / "bundle.1234abcd.min.js").write_text(
            "console.log('ok')",
            encoding="utf-8",
        )

        (self.site / "stylesheets" / "extra-v2.css").write_bytes(b"EXTRA-CSS")
        (self.site / "javascripts" / "hermes-nav.js").write_bytes(b"HERMES-NAV")
        (self.site / "images" / "x.png").write_bytes(b"PNGDATA")

        (self.site / "index.html").write_text(
            """
<!doctype html>
<html>
  <head>
    <link rel=\"stylesheet\" href=\"/docs/assets/stylesheets/main.abcdef12.min.css?old=1\"> 
    <link rel=\"stylesheet\" href=\"https://cdn.example.com/main.abcdef12.min.css?old=1\"> 
    <link rel=\"stylesheet\" href=\"/docs/stylesheets/extra-v2.css\"> 
  </head>
  <body>
    <script src=\"/docs/assets/javascripts/bundle.1234abcd.min.js?cache=old\"></script>
    <script src=\"/docs/javascripts/hermes-nav.js?v=2\"></script>
    <img src=\"/images/x.png\" alt=\"x\"> 
  </body>
</html>
""".strip(),
            encoding="utf-8",
        )

        (self.site / "nested" / "page.html").write_text(
            """
<html>
  <head>
    <link rel=\"stylesheet\" href=\"../assets/stylesheets/main.abcdef12.min.css\"> 
  </head>
  <body>
    <script src=\"../assets/javascripts/bundle.1234abcd.min.js\"></script>
  </body>
</html>
""".strip(),
            encoding="utf-8",
        )

    def test_rewrites_hashed_href_and_src_and_preserves_unhashed_assets(self):
        self._write_fixture()

        before_extra = (self.site / "stylesheets" / "extra-v2.css").read_bytes()
        before_hermes = (self.site / "javascripts" / "hermes-nav.js").read_bytes()
        before_image = (self.site / "images" / "x.png").read_bytes()

        summary = sha.stabilize_hashed_assets(self.site, check=False)
        self.assertEqual(summary.stable_copies_written, 2)
        self.assertEqual(summary.references_rewritten, 4)
        self.assertEqual(summary.files_touched, 2)

        main_metric = summary.metrics["assets/stylesheets/main.abcdef12.min.css"]
        bundle_metric = summary.metrics["assets/javascripts/bundle.1234abcd.min.js"]
        self.assertEqual(main_metric.copies_written, 1)
        self.assertEqual(bundle_metric.copies_written, 1)
        self.assertEqual(main_metric.references_rewritten, 2)
        self.assertEqual(bundle_metric.references_rewritten, 2)

        self.assertEqual(
            (self.site / "assets" / "stylesheets" / "main.min.css").read_text(encoding="utf-8"),
            "body { color: black; }",
        )
        self.assertEqual(
            (self.site / "assets" / "javascripts" / "bundle.min.js").read_text(encoding="utf-8"),
            "console.log('ok')",
        )

        index_html = (self.site / "index.html").read_text(encoding="utf-8")
        nested_html = (self.site / "nested" / "page.html").read_text(encoding="utf-8")

        self.assertIn("/docs/assets/stylesheets/main.min.css?v=abcdef12", index_html)
        self.assertIn("/docs/assets/javascripts/bundle.min.js?v=1234abcd", index_html)
        self.assertIn("../assets/stylesheets/main.min.css?v=abcdef12", nested_html)
        self.assertIn("../assets/javascripts/bundle.min.js?v=1234abcd", nested_html)

        self.assertIn("https://cdn.example.com/main.abcdef12.min.css?old=1", index_html)

        self.assertEqual((self.site / "stylesheets" / "extra-v2.css").read_bytes(), before_extra)
        self.assertEqual((self.site / "javascripts" / "hermes-nav.js").read_bytes(), before_hermes)
        self.assertEqual((self.site / "images" / "x.png").read_bytes(), before_image)

    def test_idempotent_second_run_reports_zero(self):
        self._write_fixture()

        first = sha.stabilize_hashed_assets(self.site, check=False)
        second = sha.stabilize_hashed_assets(self.site, check=False)

        self.assertGreater(first.stable_copies_written, 0)
        self.assertGreater(first.references_rewritten, 0)
        self.assertEqual(second.stable_copies_written, 0)
        self.assertEqual(second.references_rewritten, 0)
        self.assertEqual(second.files_touched, 0)

    def test_check_mode_exit_code(self):
        self._write_fixture()

        first_check = sha.main([str(self.site), "--check"])
        self.assertEqual(first_check, 1)

        apply_run = sha.main([str(self.site)])
        self.assertEqual(apply_run, 0)

        second_check = sha.main([str(self.site), "--check"])
        self.assertEqual(second_check, 0)

    def test_hard_fail_when_html_references_missing_hashed_asset(self):
        (self.site / "index.html").write_text(
            '<html><head><link rel="stylesheet" href="/docs/assets/stylesheets/main.deadbeef.min.css"></head></html>',
            encoding="utf-8",
        )

        err = io.StringIO()
        with redirect_stderr(err):
            with self.assertRaises(SystemExit) as raised:
                sha.main([str(self.site)])

        self.assertEqual(raised.exception.code, 1)
        error_text = err.getvalue()
        self.assertIn("index.html", error_text)
        self.assertIn("main.deadbeef.min.css", error_text)


if __name__ == "__main__":
    unittest.main()

