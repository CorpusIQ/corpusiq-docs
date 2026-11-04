"""MkDocs hook: per-page TechArticle schema and honest sitemap dates.

Why this exists (2026-11-03). The Ahrefs AI Discoverability audit reports
"Article page missing Article schema: 335 of 503" and "Changed pages not
submitted to IndexNow: 1,793". Both come from this build:

* Every one of the 3,147 docs pages shipped only Organization / WebSite /
  WebPage. ``scripts/inject_structured_data.py`` was written to add Article but
  is wired into no deploy path, so it never ran, and its hardcoded
  ``date_published="2026-08-06"`` would have been a false claim anyway.
* The sitemap stamps every URL with the build date, so it tells a crawler the
  whole site changed today, every day. That is a false freshness signal, it
  inflates the IndexNow delta, and it wastes crawl budget.

What this hook does, at build time:

1. ``on_config`` reads one ``git log`` for the whole repo and keeps, per source
   file, the newest and oldest commit date. One subprocess for the whole build;
   no per-page ``git`` calls.
2. ``on_page_markdown`` stashes the page's own dates and, for a section index
   that lists children, the child list. Nothing is added to the markdown.
3. ``on_post_page`` injects a ``TechArticle`` JSON-LD node (``@type`` also lists
   ``Article``, because TechArticle is its subtype and audit tooling checks the
   parent name), plus ``CollectionPage`` + ``ItemList`` on section index pages.
4. ``on_post_build`` writes ``site/.page_dates.json``; the deploy path runs
   ``scripts/rewrite_sitemap_lastmod.py`` with it, because the sitemap is
   written after this hook runs.

Dates are the page's own git history, never the build date. Files outside git
fall back to their mtime. Opt a page out with frontmatter ``schema: none``.
"""

from __future__ import annotations

import datetime
import json
import os
import re
import subprocess
from urllib.parse import quote

# src_uri -> (added, modified), newest/oldest commit date of the source file.
_DATES: dict[str, tuple[str, str]] = {}
_PAGE_INFO: dict[str, dict] = {}
_TODAY = ""

_SITE = "https://www.corpusiq.io"
_ORG_ID = f"{_SITE}#organization"
_WEBSITE_ID = f"{_SITE}#website"
_REPO = "/home/hermes/corpusiq-docs"


def _git_dates(repo: str) -> dict[str, tuple[str, str]]:
    """Oldest and newest commit date per tracked file, in one git call.

    ``git log`` prints newest-first, so the first date seen for a file is its
    modification date and the last one is the date it was added.
    """
    try:
        out = subprocess.run(
            ["git", "-C", repo, "log", "--format=%ad", "--date=short", "--name-only"],
            capture_output=True, text=True, timeout=180,
        )
    except Exception:
        return {}
    if out.returncode != 0:
        return {}
    dates: dict[str, list[str]] = {}
    current = ""
    for line in out.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", line):
            current = line
            continue
        if current:
            entry = dates.setdefault(line, [current, current])
            entry[1] = current
    return {k: (v[1], v[0]) for k, v in dates.items()}


def _resolve(src_uri: str, dates: dict) -> tuple[str, str]:
    """Dates for a page source, trying the symlinked and in-docs paths."""
    for candidate in (src_uri, f"docs/{src_uri}"):
        if candidate in dates:
            return dates[candidate]
    # Untracked: fall back to the file's own mtime, never to the build date.
    for base in (os.path.join(_REPO, "docs"), _REPO):
        path = os.path.join(base, src_uri)
        if os.path.exists(path):
            stamp = datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat()
            return stamp, stamp
    return _TODAY, _TODAY


def on_config(config):
    global _TODAY
    _TODAY = datetime.date.today().isoformat()
    repo = os.path.dirname(os.path.abspath(getattr(config, "config_file_path", "") or _REPO))
    _DATES.clear()
    _DATES.update(_git_dates(repo or _REPO))
    _PAGE_INFO.clear()
    print(f"page_schema: {len(_DATES)} dated source files")
    return config


def _page_url(config, page) -> str:
    site = (config.site_url or "https://www.corpusiq.io/docs/").rstrip("/")
    url = page.url or ""
    if url.endswith("index.html"):
        url = url[: -len("index.html")]
    return f"{site}/{url}".rstrip("/") if url else site


def _children(page, files) -> list:
    """Direct child pages of a section landing page, as {name, url}.

    Two shapes exist in this corpus: a section ``index.md`` and a flat landing
    page ``section.md`` whose children live in the sibling ``section/``
    directory (docs/connectors.md is one). A child is ``name.md`` or
    ``name/index.md`` one level down; anything deeper owns its own section.
    """
    src = page.file.src_uri
    if src.endswith("index.md"):
        prefix = src[: -len("index.md")]
    elif src.endswith(".md") and any(f.src_uri.startswith(src[:-3] + "/") for f in files):
        prefix = src[:-3] + "/"
    else:
        return []
    out = []
    for f in files:
        if not f.src_uri.startswith(prefix) or f.src_uri == src:
            continue
        rest = f.src_uri[len(prefix):]
        stem = rest[:-3]
        if stem.endswith("/index"):
            stem = stem[: -len("/index")]
        if not stem or "/" in stem:      # deeper pages own their own section
            continue
        title = ""
        child_page = getattr(f, "page", None)
        if child_page is not None:
            title = (child_page.title or "").strip()
        if not title:
            title = stem.replace("-", " ").replace("_", " ").strip().title()
        out.append({"name": title, "url": stem + "/"})
    return out


def _norm_date(value) -> str:
    """Normalize a frontmatter date into YYYY-MM-DD, or '' when unusable."""
    if not value:
        return ""
    text = str(getattr(value, "isoformat", lambda: value)()).strip().strip('"').strip("'")
    m = re.match(r"(\d{4}-\d{2}-\d{2})", text)
    return m.group(1) if m else ""


def on_page_markdown(markdown, page, config, files):
    if (page.meta or {}).get("schema") == "none":
        return markdown
    src = page.file.src_uri
    added, modified = _resolve(src, _DATES)
    description = ""
    meta = page.meta or {}
    for key in ("description", "summary", "excerpt"):
        if isinstance(meta.get(key), str) and meta[key].strip():
            description = meta[key].strip()
            break
    # The corpus maintains `last_updated` and syncs it to git truth; it is the
    # page's own freshness claim and beats a git date that a bulk regeneration
    # commit rewrites for thousands of files at once.
    claimed = _norm_date(meta.get("last_updated"))
    if claimed:
        modified = claimed
        if added > modified:
            added = modified
    _PAGE_INFO[_page_url(config, page)] = {
        "src": src,
        "headline": page.title or "",
        "description": description,
        "added": added,
        "modified": modified,
        "section": (src.split("/")[0].replace("-", " ").title() if "/" in src else ""),
        "children": _children(page, files),
    }
    return markdown


def _article_node(info: dict, url: str) -> dict:
    image = f"{_SITE}/og?title={quote(info['headline'][:90])}&category=Docs"
    node = {
        "@context": "https://schema.org",
        # TechArticle is the honest type for documentation; Article is listed
        # alongside it because audit tooling checks the parent name.
        "@type": ["Article", "TechArticle"],
        "headline": info["headline"],
        "url": url,
        "image": image,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "datePublished": info["added"],
        "dateModified": info["modified"],
        "author": {"@id": _ORG_ID},
        "publisher": {"@id": _ORG_ID},
        "isPartOf": {"@id": _WEBSITE_ID},
        "inLanguage": "en-US",
    }
    if info["description"]:
        node["description"] = info["description"]
    if info["section"]:
        node["articleSection"] = info["section"]
    return node


def _item_list_node(info: dict, url: str) -> dict | None:
    children = info["children"]
    if len(children) < 2:
        return None
    base = url if url.endswith("/") else url + "/"
    return {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "url": url,
        "name": info["headline"],
        "mainEntity": {
            "@type": "ItemList",
            "numberOfItems": len(children),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": c["name"], "url": base + c["url"]}
                for i, c in enumerate(children)
            ],
        },
    }


def _trail(page, info: dict, url: str) -> list[tuple[str, str]]:
    """Ancestor trail for one page, top down, ending with the page itself.

    MkDocs gives Section objects with a title and a docs-relative url. When a
    section has no url (pure grouping node) it is skipped rather than invented.
    Falls back to the source path segments so the trail is never empty.
    """
    out: list[tuple[str, str]] = []
    try:
        for anc in page.ancestors:
            u = getattr(anc, "url", None)
            t = (getattr(anc, "title", None) or "").strip()
            if u:
                full = f"{_SITE}/docs/{u}".rstrip("/")
                if full == url.rstrip("/"):
                    continue
                out.append((t or u.strip("/").split("/")[-1], full))
    except Exception:
        out = []
    if not out:
        parts = info["src"].split("/")[:-1]
        acc = ""
        for part in parts:
            acc = f"{acc}/{part}" if acc else part
            full = f"{_SITE}/docs/{acc}"
            if full.rstrip("/") == url.rstrip("/"):
                continue
            out.append((_pretty(part), full))
    out.append((info["headline"] or url.rsplit("/", 1)[-1], url))
    root = (f"{_SITE}/docs", "Docs")
    if out and out[0][1].rstrip("/") != root[0]:
        out.insert(0, (root[1], root[0]))
    return out


_ACRONYMS = {"mcp": "MCP", "api": "API", "sdk": "SDK", "cli": "CLI", "ai": "AI",
             "llm": "LLM", "ui": "UI", "css": "CSS", "seo": "SEO", "aeo": "AEO",
             "geo": "GEO", "http": "HTTP", "json": "JSON", "sql": "SQL", "crm": "CRM"}


def _pretty(part: str) -> str:
    words = part.replace("-", " ").replace("_", " ").split()
    return " ".join(_ACRONYMS.get(w.lower(), w[:1].upper() + w[1:]) for w in words)


def _breadcrumb_node(trail: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": u}
            for i, (name, u) in enumerate(trail)
        ],
    }


_BREADCRUMB_CSS = (
    "<style>.ciq-crumbs{font-size:.78rem;line-height:1.4;margin:0 0 .6rem;opacity:.75}"
    ".ciq-crumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:.35rem;margin:0;padding:0}"
    ".ciq-crumbs li:not(:last-child)::after{content:'\\203A';margin-left:.35rem;opacity:.6}"
    "</style>"
)


def _breadcrumb_html(trail: list[tuple[str, str]]) -> str:
    """Visible trail, so the BreadcrumbList above matches what a reader sees."""
    parts = []
    for i, (name, u) in enumerate(trail):
        label = name.replace("<", "&lt;").replace(">", "&gt;")
        if i == len(trail) - 1:
            parts.append(f'<li aria-current="page">{label}</li>')
        else:
            parts.append(f'<li><a href="{u}">{label}</a></li>')
    return (
        _BREADCRUMB_CSS
        + '<nav class="ciq-crumbs" aria-label="Breadcrumb"><ol>'
        + "".join(parts)
        + "</ol></nav>"
    )


def on_post_page(output, page, config):
    url = _page_url(config, page)
    info = _PAGE_INFO.get(url)
    if not info or url.endswith(".html"):
        return output
    trail = _trail(page, info, url)
    blocks = [json.dumps(_article_node(info, url), ensure_ascii=False)]
    if len(trail) > 1:
        blocks.append(json.dumps(_breadcrumb_node(trail), ensure_ascii=False))
    listing = _item_list_node(info, url)
    if listing:
        blocks.append(json.dumps(listing, ensure_ascii=False))
    scripts = "".join(f'\n<script type="application/ld+json">{b}</script>' for b in blocks)
    output = output.replace("</head>", f"{scripts}\n</head>", 1)
    if len(trail) > 1:
        marker = re.search(r'(<article[^>]*class="[^"]*md-content__inner[^"]*"[^>]*>)', output)
        if marker:
            output = output[: marker.end()] + _breadcrumb_html(trail) + output[marker.end():]
    return output


def on_post_build(config):
    dates = {u.rstrip("/"): v["modified"] for u, v in _PAGE_INFO.items()}
    out = os.path.join(config.site_dir, ".page_dates.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(dates, fh)
    print(f"page_schema: {len(_PAGE_INFO)} pages, "
          f"{sum(1 for v in _PAGE_INFO.values() if v['children'])} with ItemList, "
          f"dates map -> {out}")
