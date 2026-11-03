#!/usr/bin/env python3
"""Drop sitemap entries that do not canonicalise to themselves.

Why: a sitemap is a list of URLs a crawler should index. Six docs pages on
www.corpusiq.io canonicalise to a marketing page instead (the docs mirrors of
/connectors, /alternatives/* and similar), and every one of them is advertised in
sitemap.xml. Ahrefs scores that as an Error ("Non-canonical page in sitemap") on
2026-11-02 and it is the only Error class besides one oversized page that survives
the asset and link fixes.

The rule is general rather than a list of six paths: for every <loc> in the built
site's sitemap, read the page it points at (site/<path>/index.html or site/<path>.html),
parse its rel=canonical, and drop the entry when that canonical is not the same URL.
If a page has no canonical tag at all the entry is kept and reported, because
"missing canonical" is a different fault that must not be silently hidden.

A second pass drops repeated <loc> entries, keeping the first occurrence. The
canonical rule cannot see those: a page built from two source files that claim the
same output path (``X.md`` and ``X/index.md``) is emitted twice under one URL and
each copy canonicalises to itself, so both survive. Until every source pair is
resolved this pass is what keeps the file a list of unique URLs. It is defence in
depth, not a substitute: the pair itself still has a dead source file, which the
build gate ``hooks/duplicate_source_pair_gate.py`` reports.

Usage:
    python scripts/prune_non_canonical_sitemap_entries.py [site_dir] [--check]
Exit 0 = sitemap written (or clean in --check), 1 = change needed in --check,
       or the sitemap could not be read.
"""
from __future__ import annotations

import argparse
import gzip
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

CANON = re.compile(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', re.I)
LOC_BLOCK = re.compile(r"\s*<url>\s*<loc>([^<]+)</loc>.*?</url>", re.S)


def page_file(site: Path, url: str) -> Path | None:
    path = urlsplit(url).path.strip("/")
    # Sitemap URLs carry the public /docs prefix; the built tree does not.
    if path == "docs":
        path = ""
    elif path.startswith("docs/"):
        path = path[len("docs/"):]
    if not path:
        return site / "index.html"
    for candidate in (site / path / "index.html", site / f"{path}.html"):
        if candidate.is_file():
            return candidate
    return None


def canonical_of(html: str) -> str | None:
    match = CANON.search(html)
    return match.group(1).strip() if match else None


def normalise(url: str) -> str:
    url = url.replace("https://corpusiq.io/", "https://www.corpusiq.io/")
    return url.rstrip("/")


def prune(site: Path, *, check: bool) -> tuple[int, list[tuple[str, str]], int, list[str]]:
    sitemap = site / "sitemap.xml"
    if not sitemap.is_file():
        raise FileNotFoundError(f"no sitemap at {sitemap}")
    text = sitemap.read_text(encoding="utf-8")

    dropped: list[tuple[str, str]] = []
    duplicate_locs: list[str] = []
    missing = 0

    def keep(block: str) -> str:
        nonlocal missing
        url = block.strip().split("<loc>", 1)[1].split("</loc>", 1)[0].strip()
        target = page_file(site, url)
        if target is None:
            missing += 1
            return block
        canonical = canonical_of(target.read_text(encoding="utf-8"))
        if canonical is None:
            missing += 1
            return block
        if normalise(canonical) != normalise(url):
            dropped.append((url, canonical))
            return ""
        return block

    new_text = re.sub(r"\s*<url>.*?</url>", lambda m: keep(m.group(0)), text, flags=re.S)
    # collapse the blank gap a removed block leaves behind
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)

    # Second pass: one entry per URL. Two source files that claim the same output
    # path are emitted twice, and each copy canonicalises to itself, so the rule
    # above keeps both. Keep the first, drop the repeat.
    seen: set[str] = set()

    def dedupe(match: re.Match[str]) -> str:
        block = match.group(0)
        loc = normalise(block.split("<loc>", 1)[1].split("</loc>", 1)[0].strip())
        if loc in seen:
            duplicate_locs.append(loc)
            return ""
        seen.add(loc)
        return block

    new_text = re.sub(r"\s*<url>.*?</url>", dedupe, new_text, flags=re.S)
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)

    changed = new_text != text
    if changed and not check:
        sitemap.write_text(new_text, encoding="utf-8")
        gz = site / "sitemap.xml.gz"
        if gz.exists():
            with gzip.open(gz, "wt", encoding="utf-8") as fh:
                fh.write(new_text)

    return len(dropped), dropped, missing, duplicate_locs


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("site_dir", nargs="?", default="site")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    site = Path(args.site_dir)

    try:
        count, dropped, missing, duplicate_locs = prune(site, check=args.check)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    verb = "to drop" if args.check else "dropped"
    print(f"Sitemap entries {verb}: {count}")
    for url, canonical in dropped[:20]:
        print(f"  {url} -> {canonical}")
    repeat_verb = "to drop" if args.check else "dropped"
    print(f"Duplicate <loc> entries {repeat_verb}: {len(duplicate_locs)}")
    for loc in duplicate_locs[:20]:
        print(f"  {loc}")
    if missing:
        print(f"Kept {missing} entry/entries whose page or canonical could not be read")
    if args.check and (count or duplicate_locs):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
