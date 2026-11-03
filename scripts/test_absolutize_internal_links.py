#!/usr/bin/env python3
import io
from pathlib import Path
import sys
import tempfile
import unittest
from contextlib import redirect_stderr

# Importable from the repo root as well as from scripts/, because CI runs this as
# `python -m unittest scripts/test_absolutize_internal_links.py`.
sys.path.insert(0, str(Path(__file__).resolve().parent))

import absolutize_internal_links as ail


class AbsolutizeInternalLinksTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.site = Path(self.tempdir.name)

    def tearDown(self):
        self.tempdir.cleanup()

    def _write(self, rel_path: str, content: str):
        path = self.site / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _mkdir(self, rel_path: str):
        (self.site / rel_path).mkdir(parents=True, exist_ok=True)

    def _write_fixture(self):
        self._mkdir("mcp-for-hr")
        self._mkdir("security/how-it-works")
        self._mkdir("security/sibling")
        self._write("security/images/diagram.png", "img")
        self._mkdir("hermes/setup/session-cleanup")
        self._mkdir("hermes/agents/vetting-an-mcp-server")
        self._write("hermes/agents/scripts/app.js", "console.log('ok')")

        self._write(
            "security/index.html",
            """
<html><body>
  <a href="../mcp-for-hr">mcp</a>
  <a href="./how-it-works?from=nav">query</a>
  <a href="sibling#details">fragment</a>
  <a href="https://example.com/page">external</a>
  <a href="/docs/already-absolute">absolute</a>
  <img src="./images/diagram.png#v1" alt="diagram">
</body></html>
""".strip(),
        )

        self._write(
            "hermes/agents/index.html",
            """
<html><body>
  <a href="../setup/session-cleanup">cleanup</a>
  <a href="vetting-an-mcp-server">sibling</a>
  <script src="./scripts/app.js?cache=1"></script>
</body></html>
""".strip(),
        )

    def test_rewrites_depth1_and_depth2_links_and_preserves_allowed_values(self):
        self._write_fixture()

        summary = ail.absolutize_internal_links(self.site, check=False)
        self.assertEqual(summary.files_touched, 2)
        self.assertEqual(summary.references_rewritten, 7)
        self.assertEqual(summary.distinct_targets, 7)

        security_html = (self.site / "security" / "index.html").read_text(encoding="utf-8")
        agents_html = (self.site / "hermes" / "agents" / "index.html").read_text(encoding="utf-8")

        self.assertIn('href="/docs/mcp-for-hr"', security_html)
        self.assertIn('href="/docs/security/how-it-works?from=nav"', security_html)
        self.assertIn('href="/docs/security/sibling#details"', security_html)
        self.assertIn('src="/docs/security/images/diagram.png#v1"', security_html)

        self.assertIn('href="/docs/hermes/setup/session-cleanup"', agents_html)
        self.assertIn('href="/docs/hermes/agents/vetting-an-mcp-server"', agents_html)
        self.assertIn('src="/docs/hermes/agents/scripts/app.js?cache=1"', agents_html)

        self.assertIn('href="https://example.com/page"', security_html)
        self.assertIn('href="/docs/already-absolute"', security_html)

    def test_idempotent_second_run_reports_zero(self):
        self._write_fixture()

        first = ail.absolutize_internal_links(self.site, check=False)
        second = ail.absolutize_internal_links(self.site, check=False)

        self.assertGreater(first.files_touched, 0)
        self.assertGreater(first.references_rewritten, 0)
        self.assertEqual(second.files_touched, 0)
        self.assertEqual(second.references_rewritten, 0)
        self.assertEqual(second.distinct_targets, 0)

    def test_check_mode_exit_codes(self):
        self._write_fixture()

        first_check = ail.main([str(self.site), "--check"])
        self.assertEqual(first_check, 1)

        apply_run = ail.main([str(self.site)])
        self.assertEqual(apply_run, 0)

        second_check = ail.main([str(self.site), "--check"])
        self.assertEqual(second_check, 0)

    def test_hard_fail_when_resolved_target_is_missing(self):
        self._mkdir("security")
        self._write(
            "security/index.html",
            '<html><body><a href="../does-not-exist">broken</a></body></html>',
        )

        err = io.StringIO()
        with redirect_stderr(err):
            with self.assertRaises(SystemExit) as raised:
                ail.main([str(self.site)])

        self.assertEqual(raised.exception.code, 1)
        text = err.getvalue()
        self.assertIn("security/index.html", text)
        self.assertIn("../does-not-exist", text)

    def test_repairs_authored_site_root_links_only_when_the_page_exists(self):
        self._mkdir("security")
        self._mkdir("hermes/data")
        self._write(
            "hermes/data/index.html",
            """
<html><body>
  <a href="/hermes">hub</a>
  <a href="/api/overview?x=1">api</a>
  <a href="/pricing">frontend route</a>
  <a href="/docs/already-absolute">already</a>
</body></html>
""".strip(),
        )
        self._mkdir("hermes/data")  # target of /hermes
        self._mkdir("api/overview")

        summary = ail.absolutize_internal_links(self.site, check=False)
        html = (self.site / "hermes" / "data" / "index.html").read_text(encoding="utf-8")

        self.assertIn('href="/docs/hermes"', html)
        self.assertIn('href="/docs/api/overview?x=1"', html)
        # A frontend route that this build does not contain must be left alone,
        # and it is counted so a run can report it without failing.
        self.assertIn('href="/pricing"', html)
        self.assertIn('href="/docs/already-absolute"', html)
        self.assertEqual(summary.root_unresolved, 1)


if __name__ == "__main__":
    unittest.main()

