#!/usr/bin/env python3
"""Integrate auto-approved repos into the published directory.

Why this exists
---------------
`discover.py` auto-approves repos into `data/approved_repos.json` and prints
"N new repos ready for ecosystem integration" - it never writes the directory
page. The nightly run therefore had to hand-edit files, and the hand edit kept
missing `ecosystem/index.md`, which is the page mkdocs actually publishes. Root
cause of the Oct 14 hyperconsciousness promotion never appearing on the live
site.

This script closes that gap for every future run: it finds approved repos that
are missing from the directory and writes them to ecosystem/index.md,
star-sorted, using the same block builder as `promote_submission.py`. The old
`ecosystem.md` twin was deleted Nov 3 2026, so there is one surface left.

Usage:
    python3 integrate_approved.py --dry-run     # report what would be written
    python3 integrate_approved.py               # write the published page
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import promote_submission as p  # noqa: E402

# discover.py emits lowercase query-bucket names; the directory maps display names.
CATEGORY_ALIASES = {
    "core": "Core Framework",
    "official": "Core Framework",
    "forks": "Forks & Derivatives",
    "mcp": "MCP & Integrations",
    "integrations": "MCP & Integrations",
    "messaging": "MCP & Integrations",
    "apis": "MCP & Integrations",
    "skills": "Skills & Plugins",
    "ui": "UI & Dashboards",
    "deployment": "Deployment",
    "production": "Deployment",
    "memory": "Memory & Knowledge",
    "research": "Memory & Knowledge",
    "benchmarks": "Memory & Knowledge",
    "content": "Content & Media",
    "security": "Security & Governance",
}


def normalise(row):
    """Return a copy of the row with a directory-display category."""
    out = dict(row)
    cat = (row.get("category") or "").strip()
    out["category"] = CATEGORY_ALIASES.get(cat.lower(), cat or "Core Framework")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="max entries to write")
    args = ap.parse_args()

    approved = p.load(p.DATA_DIR / "approved_repos.json")
    idx = p.PUBLISHED_INDEX.read_text() if p.PUBLISHED_INDEX.exists() else ""

    todo = [r for r in approved
            if r.get("url") and r["url"] not in idx]
    todo.sort(key=lambda r: -(r.get("stars") or 0))
    if args.limit:
        todo = todo[:args.limit]

    print(f"approved: {len(approved)} | missing from the published page: {len(todo)}")
    if not todo:
        print("NOTHING_TO_INTEGRATE")
        return 0

    for row in todo:
        row = normalise(row)
        print(f"  {'WOULD ADD' if args.dry_run else 'ADD'} "
              f"{row['name']:44s} {row.get('stars', 0):>8,}* [{row['category']}]")
        if args.dry_run:
            continue
        wrote_idx = p.insert_into_published_index(row)
        if not wrote_idx:
            print(f"    WARN: nothing written for {row['name']} - check category heading")

    print("DRY_RUN_OK" if args.dry_run else "INTEGRATE_OK")
    if not args.dry_run:
        regenerate_llms_txt()
    return 0


def regenerate_llms_txt():
    """Rebuild llms.txt after a write.

    Every insert bumps the "N+ repos" counters, and llms.txt embeds that
    description verbatim. CI regenerates llms.txt and then requires a clean
    `git diff`, so an un-regenerated file fails the docs build and the whole
    directory stops deploying (first hit 2026-10-27).
    """
    import subprocess
    # generate_llms_txt.py lives at the REPO root (one level above hermes/),
    # while REPO_ROOT here is the hermes/ directory.
    for root in (p.REPO_ROOT.parent, p.REPO_ROOT):
        script = root / "scripts" / "generate_llms_txt.py"
        if script.exists():
            break
    else:
        print("  WARN: generate_llms_txt.py not found - llms.txt may be stale")
        return
    res = subprocess.run([sys.executable, str(script)], cwd=str(script.parent.parent),
                         capture_output=True, text=True)
    for line in (res.stdout or "").strip().splitlines()[-2:]:
        print("  llms: " + line)
    if res.returncode != 0:
        print("  WARN: llms.txt regeneration failed: " + (res.stderr or "")[-300:])


if __name__ == "__main__":
    sys.exit(main())
