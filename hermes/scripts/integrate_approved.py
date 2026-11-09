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
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import promote_submission as p  # noqa: E402

TOKEN_PATH = Path(os.path.expanduser("~/.hermes/profiles/corpusiq/secrets/github.token"))
DEAD_DB = p.DATA_DIR / "dead_approved_repos.json"

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


def _token():
    try:
        return TOKEN_PATH.read_text().strip()
    except OSError:
        return ""


def probe(name):
    """Return (state, data) for a repo via the GitHub API.

    A repo that was renamed answers 301 with the canonical repo, so a bare 404
    test misses moves. A repo that was deleted or made private answers 404. Both
    used to slip through: the directory lists such repos as
    "owner/name (repo no longer public)" with no URL, the old presence test
    looked for the URL string only, and the nightly run therefore re-published
    four dead repos as live entries (2026-11-08 build failure).
    """
    url = "https://api.github.com/repos/" + name
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "corpusiq-ecosystem-discovery",
    })
    tok = _token()
    if tok:
        req.add_header("Authorization", "Bearer " + tok)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return "dead", None
        if exc.code in (403, 429):
            return "ratelimited", None
        return "error", None
    except Exception:
        return "error", None
    full = (data.get("full_name") or "").lower()
    return ("live" if full == name.lower() else "renamed"), data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="max entries to write")
    ap.add_argument("--skip-liveness", action="store_true",
                    help="trust approved_repos.json without a GitHub check (offline use only)")
    args = ap.parse_args()

    approved = p.load(p.DATA_DIR / "approved_repos.json")
    idx = p.PUBLISHED_INDEX.read_text() if p.PUBLISHED_INDEX.exists() else ""

    # Presence is decided on the entry heading, not the URL string: entries for
    # repos that went dark are written without a link, so a URL-only test sees
    # them as absent and publishes a duplicate.
    present = {m.lower() for m in re.findall(r"^###\s+(\S+/\S+)\s*$", idx, re.M)}

    def listed(row):
        name = (row.get("name") or "").strip().lower()
        url = (row.get("url") or "").rstrip("/")
        if name and name in present:
            return True
        return bool(url) and (url in idx or (url + "/") in idx)

    todo = [r for r in approved if r.get("url") and not listed(r)]
    todo.sort(key=lambda r: -(r.get("stars") or 0))
    if args.limit:
        todo = todo[:args.limit]

    print(f"approved: {len(approved)} | missing from the published page: {len(todo)}")
    if not todo:
        print("NOTHING_TO_INTEGRATE")
        return 0

    dead = []
    added = 0
    for row in todo:
        if not args.skip_liveness:
            state, data = probe(row["name"])
            if state == "dead":
                dead.append(row["name"])
                print(f"  SKIP dead   {row['name']:44s} (GitHub 404 - not published)")
                continue
            if state in ("ratelimited", "error"):
                print(f"  SKIP {state:8s} {row['name']:44s} (could not verify - not published blind)")
                continue
            if data:
                canonical = data.get("full_name") or row["name"]
                if state == "renamed":
                    if canonical.lower() in present:
                        print(f"  SKIP renamed {row['name']:43s} -> {canonical} (already listed)")
                        continue
                    print(f"  MOVE renamed {row['name']:43s} -> {canonical}")
                    row = dict(row,
                               name=canonical,
                               url=data.get("html_url") or ("https://github.com/" + canonical))
                row = dict(row, stars=data.get("stargazers_count", row.get("stars")))

        row = normalise(row)
        print(f"  {'WOULD ADD' if args.dry_run else 'ADD'} "
              f"{row['name']:44s} {row.get('stars', 0):>8,}* [{row['category']}]")
        if args.dry_run:
            continue
        wrote_idx = p.insert_into_published_index(row)
        if wrote_idx:
            added += 1
        else:
            print(f"    WARN: nothing written for {row['name']} - check category heading")

    if dead and not args.dry_run:
        DEAD_DB.write_text(json.dumps(
            {"checked_at": p.az_today(), "dead": sorted(set(dead))}, indent=2) + "\n")
        print(f"  dead repos recorded in {DEAD_DB.name}: {len(set(dead))}")

    print(f"{'DRY_RUN_OK' if args.dry_run else 'INTEGRATE_OK'} (written: {added})")
    if not args.dry_run and added:
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
