#!/usr/bin/env python3
"""check_sweep_index_links.py - keep the skills sweep index honest.

WHY (2026-11-06): the skills sweep lane publishes a batch page per fire under
``hermes/skills/marketplace/new-*/index.md`` and appends one entry to the
"Recent Sweeps" list in ``hermes/skills/marketplace/index.md``. The append step
silently stopped: the November 5 evening and November 6 morning batch pages
were both live in the sitemap and reachable from nowhere in the site - no
internal link from the marketplace index, the catalog index or any guide page.
A reader browsing the marketplace simply could not reach the newest sweeps, and
nothing noticed because every URL still returned 200.

Two checks, both about the same failure mode (an index that drifts from the
tree it indexes):

1. ORPHANS - a batch page fired within RECENT_DAYS of the newest fire must be
   linked from the marketplace index. The fire date comes from the SLUG
   (``new-nov6-2026-morning-skills``), never from ``last_updated``: a freshness
   sweep rewrote the stamp on the July and August pages to 2026-11-01, which
   would make four three-month-old fires look brand new. The window is measured
   against the newest fire in the tree rather than today, so the gate stays
   deterministic inside CI and in a stale checkout. Older fires age out.
2. DANGLING - every ``/hermes/skills/marketplace/new-*`` link in the index must
   resolve to a real batch page. A stale link is the same defect from the other
   side: the index promises a page the site no longer serves.

Usage:
    python3 scripts/check_sweep_index_links.py            # exit 1 on failure
    python3 scripts/check_sweep_index_links.py --root DIR # check another tree
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys

RECENT_DAYS = 21
MARKET_DIR = os.path.join("hermes", "skills", "marketplace")
INDEX_REL = os.path.join(MARKET_DIR, "index.md")
LINK_RE = re.compile(r"/hermes/skills/marketplace/(new-[a-z0-9-]+)")
SLUG_RE = re.compile(r"^new-([a-z]+)(\d{1,2})?(?:-(\d{1,2}))?-(\d{4})")
STAMP_RE = re.compile(r"^last_updated:\s*\"?(\d{4}-\d{2}-\d{2})", re.MULTILINE)

MONTHS = {
    "jan": 1, "january": 1,
    "feb": 2, "february": 2,
    "mar": 3, "march": 3,
    "apr": 4, "april": 4,
    "may": 5,
    "jun": 6, "june": 6,
    "jul": 7, "july": 7,
    "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10,
    "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}


def read(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as handle:
        return handle.read()


def page_date(slug: str, path: str) -> dt.date | None:
    """Fire date from the slug; ``last_updated`` only when the slug is odd."""
    match = SLUG_RE.match(slug)
    if match:
        month = MONTHS.get(match.group(1))
        if month:
            day = int(match.group(2) or 1)
            year = int(match.group(4))
            try:
                return dt.date(year, month, day)
            except ValueError:
                pass
    stamp = STAMP_RE.search(read(path))
    if stamp:
        try:
            return dt.date.fromisoformat(stamp.group(1))
        except ValueError:
            return None
    return None


def batch_pages(root: str) -> dict[str, dt.date]:
    """slug -> fire date for every batch page that can be dated."""
    pages: dict[str, dt.date] = {}
    market = os.path.join(root, MARKET_DIR)
    if not os.path.isdir(market):
        return pages
    for name in sorted(os.listdir(market)):
        if not name.startswith("new-"):
            continue
        page = os.path.join(market, name, "index.md")
        if not os.path.isfile(page):
            continue
        dated = page_date(name, page)
        if dated:
            pages[name] = dated
    return pages


def check(root: str, recent_days: int = RECENT_DAYS) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []

    index_path = os.path.join(root, INDEX_REL)
    if not os.path.isfile(index_path):
        return [f"missing marketplace index: {INDEX_REL}"], notes

    index_text = read(index_path)
    linked = set(LINK_RE.findall(index_text))
    pages = batch_pages(root)

    if not pages:
        notes.append("no dated batch pages found - nothing to check")
        return errors, notes

    newest = max(pages.values())
    cutoff = newest - dt.timedelta(days=recent_days)

    for slug, fired in sorted(pages.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
        if fired < cutoff:
            continue
        if slug not in linked:
            errors.append(
                f"orphan batch page: {slug} (fired {fired}) is not linked from "
                f"{INDEX_REL} - add an entry pointing at "
                f"/hermes/skills/marketplace/{slug}"
            )

    for slug in sorted(linked):
        if slug not in pages:
            errors.append(
                f"dangling sweep link: {INDEX_REL} links /hermes/skills/marketplace/{slug} "
                f"but no batch page carries that slug"
            )

    notes.append(
        f"checked {len(pages)} batch pages, {len(linked)} index links, "
        f"newest fire {newest}, window {recent_days}d"
    )
    return errors, notes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=None, help="repository root (default: parent of scripts/)")
    parser.add_argument("--recent-days", type=int, default=RECENT_DAYS)
    args = parser.parse_args(argv)

    root = args.root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    errors, notes = check(root, args.recent_days)

    for note in notes:
        print(f"check_sweep_index_links: {note}")
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    print("check_sweep_index_links: OK - every recent sweep page is indexed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
