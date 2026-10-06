"""Emit the canonical link without a trailing slash.

Why this exists
---------------
The docs are served with trailing-slash stripping (Next.js
`trailingSlash: false`), so the address that actually loads is:

    https://www.corpusiq.io/docs/connectors        -> 200
    https://www.corpusiq.io/docs/connectors/       -> 308 -> the above

The sitemap lists the no-slash form, and a full crawl of both hosts confirms
every sitemap URL returns 2xx on that form.

MkDocs, however, derives the canonical tag from `site_url` plus the page URL,
and with `use_directory_urls: true` the page URL ends in `/`. So every page
declared:

    <link rel="canonical" href="https://www.corpusiq.io/docs/connectors/">

That names a redirect as the page's own address. It is the source of the
"Non-canonical page in sitemap" rows in the Ahrefs site audit, and it is the
thing to fix at the token rather than per page.

Note: the `canonical:` key in page frontmatter is INERT here. It is not a
MkDocs feature, and editing it changes nothing in the built output (verified
2026-10-06: a 1,425-file frontmatter edit produced an unchanged 2,414
trailing-slash canonicals in `site/`). The tag is generated during the build,
so it must be corrected during the build.

Scope
-----
Only the href of a link element carrying rel="canonical" is rewritten, and only
when the URL ends in a single slash. The root of the docs site
(`https://www.corpusiq.io/docs/`) becomes `https://www.corpusiq.io/docs`, which
serves 200. Bare schemes (`https://`) are never touched.
"""
import re

__all__ = ['on_post_page']

# Match a whole <link ...> tag that carries rel="canonical", then pull its href.
_LINK = re.compile(r'<link\b[^>]*\brel="canonical"[^>]*>', re.I)
_HREF = re.compile(r'(href=")([^"]*)(")')


def _fix_tag(tag: str) -> str:
    def repl(m):
        url = m.group(2)
        # never touch a bare scheme, and only strip ONE slash
        if url.endswith('/') and not url.endswith('://'):
            return m.group(1) + url[:-1] + m.group(3)
        return m.group(0)

    return _HREF.sub(repl, tag, count=1)


def on_post_page(output: str, page=None, config=None) -> str:
    """Strip the trailing slash from the canonical link, if present."""
    if not output or 'canonical' not in output:
        return output
    return _LINK.sub(lambda m: _fix_tag(m.group(0)), output)
