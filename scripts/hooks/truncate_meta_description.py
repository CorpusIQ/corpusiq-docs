"""MkDocs hook: cap meta descriptions at 160 characters.

Ahrefs Site Audit flags "Meta description too long" for descriptions over
160 characters. The base theme emits ``page.meta.description`` verbatim, and
many frontmatter descriptions run long. This hook truncates an over-length
description at a word boundary in ``page.meta`` before the page renders, so the
rendered ``<meta name="description">`` -- and the ``og:description`` /
``twitter:description`` built from the same value in ``overrides/main.html`` --
all stay within the limit. Descriptions already within the limit are untouched.

Running in ``on_page_markdown`` (before the template renders) is what makes the
single edit to ``page.meta`` flow through to every consumer of the description.
"""

# Ahrefs flags descriptions longer than this many characters.
_MAX_LEN = 160
# Truncate to a bit under the cap so trimming back to a word boundary can never
# push the result over _MAX_LEN.
_TARGET = 157


def on_page_markdown(markdown, page, config, files):
    if page is None:
        return markdown
    desc = page.meta.get("description")
    if not isinstance(desc, str) or len(desc) <= _MAX_LEN:
        return markdown

    # Trim to the last word boundary within _TARGET chars, then strip any
    # trailing punctuation left dangling by the cut.
    cut = desc[:_TARGET].rsplit(" ", 1)[0].rstrip(" ,;:.—–-")
    # Fallback for a description with no space in the first _TARGET chars.
    if not cut:
        cut = desc[:_TARGET]
    page.meta["description"] = cut
    return markdown
