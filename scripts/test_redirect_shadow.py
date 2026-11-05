"""Guard the redirect map against shadowing or stranding a real docs page.

Two failure modes are possible in ``vercel.json`` and both are silent until a
reader clicks a link:

1. SHADOWING -- a redirect source matches a page that actually exists. Vercel
   is evaluated before the filesystem, so the real page becomes unreachable at
   its own URL and every inbound link 301s elsewhere.
2. STRANDING -- a redirect destination points at a page that does not exist, so
   the reader lands on a 404.

Both happened together on 2026-11-04: a bulk connector redirect block (added in
8ce1ed147a) mapped ``/docs/connect-klaviyo-to-chatgpt`` to
``/docs/connectors/connect-klaviyo-to-chatgpt``. ``docs/connect-klaviyo-to-chatgpt.md``
exists, so the redirect shadowed it, and no
``connectors/connect-klaviyo-to-chatgpt.md`` exists, so the destination 404'd.
The page was live on the www proxy but dead on docs.corpusiq.io.

Route mapping this test encodes (verified against production):
``/docs/<rest>`` is backed by ``<rest>.md`` or ``docs/<rest>.md``.
"""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

# Intentionally-shadowed pages, with the reason spelled out. Add an entry here
# only when the redirect is the deliberate choice and the page is retired.
ALLOWED_SHADOWS = {
    # "docs/example.md": "/docs/example -> /docs/connectors/example (page retired 2026-01-01)",
}


def _page_md(rest):
    """Return the backing markdown path for a /docs/<rest> route, or None."""
    rest = rest.strip("/")
    for candidate in (ROOT / f"{rest}.md", ROOT / "docs" / f"{rest}.md"):
        if candidate.is_file():
            return candidate
    return None


def _route_of(redirect):
    source = redirect.get("source", "")
    return source.split("#")[0].split("?")[0].rstrip("/")


class RedirectMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((ROOT / "vercel.json").read_text())
        cls.redirects = cls.config.get("redirects", [])

    def test_config_is_parseable_and_has_redirects(self):
        self.assertGreater(len(self.redirects), 0, "vercel.json carries no redirects")

    def test_no_redirect_shadows_a_real_docs_page(self):
        offenders = []
        for redirect in self.redirects:
            route = _route_of(redirect)
            if not route.startswith("/docs/"):
                continue
            rest = route[len("/docs/"):]
            backing = _page_md(rest)
            if backing is None:
                continue
            key = str(backing.relative_to(ROOT))
            if key in ALLOWED_SHADOWS:
                continue
            offenders.append(
                f"{route} -> {redirect.get('destination')} "
                f"(page {key} exists, so the redirect hides it)"
            )
        self.assertEqual(
            offenders,
            [],
            "Redirect(s) shadow a real docs page; remove the redirect or "
            "retire the page deliberately:\n  " + "\n  ".join(offenders),
        )

    def test_no_redirect_strands_readers_on_a_missing_page(self):
        offenders = []
        for redirect in self.redirects:
            destination = redirect.get("destination", "")
            if not destination.startswith("/docs/"):
                continue
            rest = destination.split("#")[0].split("?")[0].rstrip("/")
            rest = rest[len("/docs/"):]
            if _page_md(rest) is None:
                offenders.append(
                    f"{redirect.get('source')} -> {destination} (no page backs this)"
                )
        self.assertEqual(
            offenders,
            [],
            "Redirect destination(s) point at pages that do not exist:\n  "
            + "\n  ".join(offenders),
        )


if __name__ == "__main__":
    unittest.main()
