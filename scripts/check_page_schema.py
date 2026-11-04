#!/usr/bin/env python3
"""Fail the build when the docs site loses its per-page schema or honest dates.

WHY (2026-11-03): the AI Discoverability audit found 335 docs/editorial pages
with no Article markup and a sitemap where every URL carried the build date.
Both are fixed by scripts/hooks/page_schema.py + rewrite_sitemap_lastmod.py, and
both fail silently if a hook is dropped from mkdocs.yml or a step is skipped
from the deploy path — nothing else notices. This is the check that notices.

Gates (all on built output in site/):
  1. at least 99% of rendered pages carry a TechArticle/Article node;
  2. every such node has headline, url, image, datePublished, dateModified;
  3. no page claims datePublished after dateModified;
  4. the sitemap's lastmod is not one single date (the build-date regression).

USAGE
    python3 scripts/check_page_schema.py
"""
import glob
import json
import os
import re
import sys
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(REPO, "site")

REQUIRED = ("headline", "url", "image", "datePublished", "dateModified")


def main() -> int:
    pages = glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True)
    if len(pages) < 100:
        print(f"check_page_schema: FAIL no build output ({len(pages)} pages) - run mkdocs build")
        return 1

    with_schema = 0
    failures = []
    for path in pages:
        html = open(path, encoding="utf-8", errors="ignore").read()
        nodes = []
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            if "TechArticle" not in block and '"Article"' not in block:
                continue
            try:
                nodes.append(json.loads(block))
            except Exception:
                failures.append(f"{os.path.relpath(path, SITE)}: unparseable JSON-LD")
        if not nodes:
            continue
        with_schema += 1
        node = nodes[0]
        rel = os.path.relpath(path, SITE)
        for field in REQUIRED:
            if not node.get(field):
                failures.append(f"{rel}: Article missing {field}")
        if node.get("datePublished", "") > node.get("dateModified", ""):
            failures.append(f"{rel}: datePublished {node['datePublished']} > dateModified {node['dateModified']}")

    ratio = with_schema / len(pages)
    if ratio < 0.99:
        failures.append(f"only {with_schema}/{len(pages)} pages carry Article schema ({ratio:.1%})")

    # Gate 5 (2026-11-04): BreadcrumbList on every page that carries an Article
    # node, and its last item must be the page itself. Without this the trail
    # silently disappears if the hook is dropped, which is exactly what the
    # operator's breadcrumb rule requires us never to ship.
    with_crumbs = 0
    for path in pages:
        html = open(path, encoding="utf-8", errors="ignore").read()
        if "BreadcrumbList" not in html:
            continue
        blocks = [b for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
                  if "BreadcrumbList" in b]
        try:
            node = json.loads(blocks[0])
        except Exception:
            failures.append(f"{os.path.relpath(path, SITE)}: unparseable BreadcrumbList JSON-LD")
            continue
        items = node.get("itemListElement") or []
        if len(items) < 2:
            failures.append(f"{os.path.relpath(path, SITE)}: BreadcrumbList has {len(items)} items")
        with_crumbs += 1
        if "ciq-crumbs" not in html:
            failures.append(f"{os.path.relpath(path, SITE)}: BreadcrumbList without a visible trail")
    crumb_ratio = with_crumbs / max(with_schema, 1)
    if crumb_ratio < 0.99:
        failures.append(f"only {with_crumbs}/{with_schema} Article pages carry BreadcrumbList ({crumb_ratio:.1%})")

    sitemap = os.path.join(SITE, "sitemap.xml")
    if os.path.exists(sitemap):
        dates = Counter(re.findall(r"<lastmod>([^<]+)</lastmod>", open(sitemap, encoding="utf-8").read()))
        if len(dates) < 2:
            failures.append(f"sitemap lastmod has a single date ({dates.most_common(1)}) - rebuild/rewrite step skipped")
    else:
        dates = Counter()
        failures.append("no site/sitemap.xml")

    if failures:
        print(f"check_page_schema: FAIL ({len(failures)} problems)")
        for f in failures[:25]:
            print("  -", f)
        return 1
    print(f"check_page_schema: ok ({with_schema}/{len(pages)} pages with Article schema, "
          f"sitemap lastmod spread {len(dates)} dates)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
