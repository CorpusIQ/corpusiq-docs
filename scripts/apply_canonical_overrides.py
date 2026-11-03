#!/usr/bin/env python3
"""Apply scripts/canonical_overrides.json to a built site tree.

Why: six docs pages are deliberate duplicates of a marketing page and are
canonicalised onto it (see the rationale in canonical_overrides.json and
data/research/viktor-seo-decision-2026-09-14.md). deploy_docs.py applied that map
inline; the CI production path and deploy_vercel_prod.py did not, so a CI deploy
silently reverted those six canonicals to self-referencing. One implementation,
called by every deploy path, closes that divergence and lets the sitemap prune run
against the canonicals that actually ship.

Usage:
    python scripts/apply_canonical_overrides.py [site_dir]
Exit 0 = applied (or nothing to do), 1 = a keyed page is missing from the build.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CANON = re.compile(r'<link rel="canonical" href="[^"]*">')


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    site = Path(args[0] if args else "site")
    repo = Path(__file__).resolve().parents[1]
    map_path = repo / "scripts" / "canonical_overrides.json"

    try:
        overrides = json.loads(map_path.read_text(encoding="utf-8")).get("overrides", {})
    except FileNotFoundError:
        print(f":: no override map at {map_path}, nothing to apply")
        return 0

    applied, missing = 0, []
    for rel, target in overrides.items():
        page = site / rel
        if not page.is_file():
            missing.append(rel)
            continue
        text = page.read_text(encoding="utf-8")
        new = CANON.sub(f'<link rel="canonical" href="{target}">', text, count=1)
        if new != text:
            page.write_text(new, encoding="utf-8")
            applied += 1

    print(f"Canonical overrides applied: {applied}/{len(overrides)}")
    if missing:
        # A keyed page disappearing means the override silently stopped working.
        for rel in missing:
            print(f"  MISSING: {rel}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
