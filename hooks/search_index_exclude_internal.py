"""Keep the internal agent catalogs out of the public search index.

Why this exists
---------------
`/docs/search/search_index.json` had grown to 37.5 MB uncompressed (9.4 MB
brotli on the wire). Material renders a search form on every page and the
bundle fetches the index as soon as a form exists:

    var zi = document.forms.namedItem("search") ? ks() : tt

so every visitor paid that 9.4 MB before first paint. That single request was
the whole of the 9.83 MB measured page weight and the reason Lighthouse sat at
performance 86 with FCP 3.0 s.

The index held 42,268 entries for 247 pages because two subtrees are machine
facing catalogs with a heading per row:

    hermes/mcp       17,969 entries   10.96 MB
    hermes/skills    16,541 entries   12.27 MB

Together 82 percent of the entries and 85 percent of the indexed text, for
content that is navigated from its own index pages and is not what a visitor
searches the product docs for. The Material search plugin honours
`search.exclude: true` in frontmatter but has no subtree option, and putting
that key into thousands of generated catalog pages would put it back on the
next regeneration. Excluding by source path here is the durable form.

Reversible: delete this hook from `hooks:` in mkdocs.yml and the catalogs
return to the index on the next build.

Measured 2026-11-19 on the real build: 42,268 entries -> 7,758, 37.5 MB ->
5.8 MB uncompressed, 9.4 MB -> about 1.3 MB on the wire. Every product page
(connectors, best-practices, agents) keeps its entries.
"""

# Source-path prefixes whose pages are kept out of the search index. These
# trees stay published and stay reachable through navigation and the sitemap;
# only their search entries are dropped.
EXCLUDED_PREFIXES = (
    "hermes/mcp/",
    "hermes/skills/",
)
EXCLUDED_EXACT = (
    "hermes/mcp",
    "hermes/skills",
)


def on_page_markdown(markdown, *, page, config, files):
    """Mark excluded pages before the search plugin reads page meta."""
    src = page.file.src_uri
    if src in EXCLUDED_EXACT or src.startswith(EXCLUDED_PREFIXES):
        meta = page.meta if isinstance(page.meta, dict) else {}
        search = meta.get("search")
        if not isinstance(search, dict):
            search = {}
            meta["search"] = search
        search["exclude"] = True
        page.meta = meta
    return markdown
