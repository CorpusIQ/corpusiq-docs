#!/usr/bin/env python3
"""Find two Markdown source files that claim the same output URL.

Why this exists
---------------
MkDocs does not fail when `X.md` and `X/index.md` both exist. It publishes one
of them and drops the other silently. On 2026-11-03 thirteen docs pages were in
that state; twelve of them still listed the dead file as the source, and 9 of 13
dead copies held sections the live page did not (skill-vetter-setup.md had 16
headings against 9 on the published page). Editing the dead copy published
nothing, which is a trap for any agent or human following the file name.

The invariant enforced here is the URL, not the filename: two source files must
not resolve to one page. That catches `X.md` + `X/index.md`, `X.md` + `X/README.md`,
and `index.md` + `README.md` in the same directory, because all three publish to
one URL.

Exemptions
----------
A folder README is a real GitHub surface: it renders when someone browses the
repository, while index.md is the page served by the site. Both have a reader, so
the three directories that carry both are listed in EXEMPT rather than deleted.
The exemption is checked for staleness: an exempt path that no longer pairs is
reported, so the list cannot rot into a blanket permission.

Usage
-----
    python3 scripts/check_source_url_collisions.py          # report, exit 1 on collision
    python3 scripts/check_source_url_collisions.py --json   # machine readable

The MkDocs hook `hooks/duplicate_source_pair_gate.py` runs the same check at
build time, so a collision fails the deploy that produces the site.
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(REPO, "docs")

SKIP_DIRS = {".git", "site", "node_modules", "__pycache__", "assets",
             "javascripts", "stylesheets", ".vercel", ".husky"}

# index.md + README.md in one directory: GitHub renders the README, the site
# renders index.md. Both are maintained on purpose, so both stay. Add a
# repository-relative directory here only when its README has a reader that
# index.md cannot serve.
EXEMPT_DIRS = {
    "docs",
    "hermes",
    "hermes/prompts",
}


def _url_for(docs_root: str, path: str) -> str:
    """Output URL path MkDocs derives from a source file (no leading slash)."""
    rel = os.path.relpath(path, docs_root).replace(os.sep, "/")
    parts = rel.split("/")
    stem = parts[-1][:-3]
    if stem in ("index", "README"):
        return "/".join(parts[:-1])
    return "/".join(parts[:-1] + [stem])


def scan(docs_root: str = DOCS_DIR) -> tuple[dict[str, list[str]], list[str]]:
    """Return ({url: [sources]}, [stale exemptions]) for the built tree.

    Walks with symlinks followed (docs/ links to the real content directories),
    guarding against a cycle by tracking resolved directories.
    """
    seen_real: set[str] = set()
    sources: list[str] = []

    def walk(directory: str) -> None:
        real = os.path.realpath(directory)
        if real in seen_real:
            return
        seen_real.add(real)
        try:
            entries = sorted(os.scandir(directory), key=lambda e: e.name)
        except OSError:
            return
        for entry in entries:
            if entry.name.startswith(".") or entry.name in SKIP_DIRS:
                continue
            try:
                is_dir = entry.is_dir(follow_symlinks=True)
            except OSError:
                continue
            if is_dir:
                walk(os.path.join(directory, entry.name))
            elif entry.name.endswith(".md"):
                sources.append(os.path.join(directory, entry.name))

    walk(docs_root)

    by_url: dict[str, list[str]] = defaultdict(list)
    for path in sources:
        # Report the real repository path: docs/ subdirectories are symlinks to
        # their sibling directories, so docs/hermes/index.md IS hermes/index.md.
        by_url[_url_for(docs_root, path)].append(
            os.path.relpath(os.path.realpath(path), REPO).replace(os.sep, "/")
        )

    collisions = {url: paths for url, paths in by_url.items() if len(paths) > 1}

    # An exemption only means anything while the pair still exists.
    paired_dirs = {os.path.dirname(paths[0]) for paths in collisions.values()}
    stale = [f"{d}: exempted but no index.md/README.md pair"
             for d in sorted(EXEMPT_DIRS) if d not in paired_dirs]

    return collisions, stale


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    as_json = "--json" in argv

    collisions, stale = scan()
    real = {url: paths for url, paths in collisions.items()
            if os.path.dirname(paths[0]) not in EXEMPT_DIRS}

    if as_json:
        print(json.dumps({"collisions": real, "exempt": sorted(EXEMPT_DIRS),
                          "stale_exemptions": stale}, indent=2))
    else:
        if real:
            print(f"SOURCE URL COLLISIONS: {len(real)}")
            for url, paths in sorted(real.items()):
                print(f"  /{url}".rstrip("/"))
                for p in paths:
                    print(f"    {p}")
            print("Fix: merge the useful sections into the published file, then")
            print("delete the shadowed one. Only one source may claim a URL.")
        else:
            print("OK: every source file resolves to its own URL")
        if stale:
            for note in stale:
                print(f"STALE EXEMPTION: {note}")

    return 1 if real else 0


if __name__ == "__main__":
    sys.exit(main())
