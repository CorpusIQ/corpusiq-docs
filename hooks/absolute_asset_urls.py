"""Rewrite the theme's relative asset URLs to absolute /docs/-rooted paths.

Why this exists
---------------
The site is served under https://www.corpusiq.io/docs/, but the hosting layer
runs with trailing-slash stripping (Next.js `trailingSlash: false`). A
directory-index request such as `/docs` (no trailing slash) still serves the
page, but the browser treats `docs` as a file and resolves every page-relative
asset reference (`assets/...`, `javascripts/...`, `stylesheets/...`) against the
domain root. That turns `assets/javascripts/bundle.<hash>.min.js` into
`https://www.corpusiq.io/assets/javascripts/bundle.<hash>.min.js`, which 404s
because the docs assets live under `/docs/assets/...`. The Material theme emits
these references relative by design, so the fix belongs here, at build time.

Making the references absolute under `/docs/` resolves them correctly no matter
whether the page is reached with or without the trailing slash, and no matter
the page's directory depth.

Scope
-----
Only the asset directories are rewritten: `assets/` (Material bundle, theme CSS,
images, search worker), `javascripts/` and `stylesheets/` (extra_javascript /
extra_css). Content and navigation links never begin with those directory names,
so they are left untouched. Absolute URLs (`https://...`, already-`/docs/...`)
do not match the pattern and are left as-is, so the hook is idempotent.

CSS-internal font URLs (`../fonts/...` inside the bundled stylesheet) are not in
the page HTML; they resolve relative to the stylesheet's own URL, which this hook
makes absolute, so fonts follow automatically.
"""

import re

# src="..." / href="..." whose value is a page-relative reference (zero or more
# ../ hops) into one of the asset directories. The directory name is captured so
# the replacement can keep the remainder of the path (hash, query string) intact.
_ASSET_REF = re.compile(r'(?P<attr>src|href)="(?:\.\./)*(?P<dir>assets/|javascripts/|stylesheets/)')

_SITE_SUBPATH = "/docs/"


def on_post_page(output: str, page=None, config=None) -> str:
    return _ASSET_REF.sub(
        lambda m: f'{m.group("attr")}="{_SITE_SUBPATH}{m.group("dir")}',
        output,
    )
