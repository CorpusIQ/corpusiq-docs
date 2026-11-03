#!/usr/bin/env python3
"""Rewrite sitemap lastmod from each page's own source date.

WHY (2026-11-03): the sitemap plugin stamps every URL with the build date, so
every nightly build claims all 3,157 pages changed. Ahrefs reads that as
"Changed pages not submitted to IndexNow: 1,793", and search engines spend crawl
budget re-fetching pages that did not change.

The dates come from ``site/.page_dates.json``, written by
``scripts/hooks/page_schema.py`` during the build (per-file git history, mtime
fallback). This runs AFTER ``mkdocs build`` because the sitemap is written after
the hooks that produce that map.

USAGE
    python3 scripts/rewrite_sitemap_lastmod.py            # report only
    python3 scripts/rewrite_sitemap_lastmod.py --write    # rewrite sitemap.xml
"""
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(REPO, "site")
DATES = os.path.join(SITE, ".page_dates.json")
SITEMAP = os.path.join(SITE, "sitemap.xml")


def main() -> int:
    write = "--write" in sys.argv
    if not os.path.exists(DATES):
        print("rewrite_sitemap_lastmod: no .page_dates.json (build with the page_schema hook first)")
        return 2
    if not os.path.exists(SITEMAP):
        print("rewrite_sitemap_lastmod: no site/sitemap.xml")
        return 2
    dates = {k.rstrip("/"): v for k, v in json.load(open(DATES, encoding="utf-8")).items()}
    xml = open(SITEMAP, encoding="utf-8").read()
    before = re.findall(r"<lastmod>([^<]+)</lastmod>", xml)
    changed = [0]

    def repl(m):
        loc, old = m.group(1), m.group(2)
        new = dates.get(loc.rstrip("/"))
        if new and new != old:
            changed[0] += 1
            return m.group(0).replace(f"<lastmod>{old}</lastmod>", f"<lastmod>{new}</lastmod>")
        return m.group(0)

    out = re.sub(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]*)</lastmod>", repl, xml)
    after = re.findall(r"<lastmod>([^<]+)</lastmod>", out)
    print(f"rewrite_sitemap_lastmod: {len(dates)} dated urls, "
          f"{len(after)} lastmod entries, {changed[0]} rewritten, "
          f"{len(set(before))} -> {len(set(after))} distinct dates")
    if write and changed[0]:
        with open(SITEMAP, "w", encoding="utf-8") as fh:
            fh.write(out)
        print("rewrite_sitemap_lastmod: sitemap.xml written")
    elif not write:
        print("rewrite_sitemap_lastmod: dry run, pass --write to apply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
