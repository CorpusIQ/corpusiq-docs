#!/usr/bin/env python3
"""sync_last_updated.py - keep frontmatter `last_updated` truthful.

The docs site renders "Last updated: <frontmatter last_updated>" under the H1
(docs/javascripts/last-updated.js) and emits it as schema.org dateModified
(docs/overrides/main.html). If the frontmatter date is not maintained, every
freshness signal the site publishes is a lie - pages edited today keep showing
a date from weeks ago.

This script derives the date from git (the last commit that actually changed
the page) and bumps the frontmatter to match.

Rules
-----
* default  : only bump forward (frontmatter < git date). Reads as "stale stamp".
* --strict : set every stamp to the git date exactly (can rewind).
* --add-missing : add `last_updated:` to frontmatter blocks that lack it.
* stamp-only commits (subject starts with MARKER) are ignored when computing
  the git date, so the sync never feeds on its own commits and never oscillates.
* files with no frontmatter, or no git history, are left alone.

Usage
-----
    python3 scripts/sync_last_updated.py                     # dry-run, whole repo
    python3 scripts/sync_last_updated.py --paths hermes/     # dry-run, one section
    python3 scripts/sync_last_updated.py --paths hermes/ --apply
    python3 scripts/sync_last_updated.py --apply --add-missing --strict
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import datetime as dt
from typing import Iterable

MARKER = "chore(stamps):"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "site", "node_modules", "__pycache__", ".vercel", "published-content"}
FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
LU_RE = re.compile(r"^(last_updated:\s*)([\"']?)(\d{4}-\d{2}-\d{2})([\"']?)\s*$", re.M)


def git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    return out.stdout if out.returncode == 0 else ""


def is_stamp_only(sha: str, path: str) -> bool:
    """True when this commit's change to `path` touched only last_updated lines.

    The subject marker alone is too coarse: a mixed commit such as
    "docs(freshness): refresh 2 stale pages + sync last_updated stamps" carries
    the stamp sync for hundreds of pages it did not otherwise edit. Counting
    that as content makes every one of them look freshly updated, so the date
    has to be judged per file from the diff.
    """
    diff = git("show", "--unified=0", "--format=", sha, "--", path)
    if not diff.strip():
        return False
    changed = [
        ln for ln in diff.splitlines()
        if (ln.startswith("+") or ln.startswith("-")) and not ln.startswith(("+++", "---"))
    ]
    return bool(changed) and all(
        ln[1:].lstrip().startswith("last_updated:") for ln in changed
    )


def last_content_date(path: str) -> str | None:
    """Last commit date (YYYY-MM-DD) that changed `path`, ignoring stamp commits."""
    log = git("log", "--format=%H\t%cs\t%s", "--follow", "--", path)
    for line in log.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        sha, date = parts[0], parts[1]
        subject = parts[2] if len(parts) > 2 else ""
        if subject.startswith(MARKER):
            continue
        if is_stamp_only(sha, path):
            continue
        return date
    return None


def iter_pages(paths: Iterable[str]) -> list[str]:
    found: list[str] = []
    for prefix in paths:
        target = os.path.join(REPO, prefix.rstrip("/"))
        if os.path.isfile(target):
            found.append(os.path.relpath(target, REPO))
            continue
        for dirpath, dirnames, filenames in os.walk(target):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for name in filenames:
                if name.endswith(".md"):
                    found.append(os.path.relpath(os.path.join(dirpath, name), REPO))
    return sorted(set(found))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paths", nargs="*", default=["."], help="repo-relative file or dir prefixes")
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry-run)")
    ap.add_argument("--strict", action="store_true", help="set stamps to git date exactly (allows rewind)")
    ap.add_argument("--add-missing", action="store_true", help="add last_updated to frontmatter that lacks it")
    ap.add_argument("--limit", type=int, default=0, help="max files to change (0 = no limit)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    pages = iter_pages(args.paths)
    bumped: list[tuple[str, str, str]] = []
    added: list[tuple[str, str]] = []
    unchanged = 0
    skipped = {"no_frontmatter": 0, "no_git": 0, "future_or_equal": 0, "unsupported": 0}

    for rel in pages:
        full = os.path.join(REPO, rel)
        try:
            text = open(full, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            skipped["unsupported"] += 1
            continue
        m = FM_RE.match(text)
        if not m:
            skipped["no_frontmatter"] += 1
            continue
        gdate = last_content_date(rel)
        if not gdate:
            skipped["no_git"] += 1
            continue

        fm = m.group(1)

        # 0. Duplicate keys. LU_RE cannot parse a non-ISO value such as
        #    "June 22, 2026", so an older run treated the field as missing and
        #    APPENDED a second last_updated instead of replacing the first.
        #    YAML quietly keeps the last one, so the page shipped two claims
        #    about its own freshness and the original date was lost. Collapse
        #    to a single truthful line before anything else looks at the block.
        dup_lines = [ln for ln in fm.split("\n") if ln.startswith("last_updated:")]
        if len(dup_lines) > 1:
            kept_lines, seen = [], False
            for ln in fm.split("\n"):
                if ln.startswith("last_updated:"):
                    if not seen:
                        kept_lines.append(f'last_updated: "{gdate}"')
                        seen = True
                    continue
                kept_lines.append(ln)
            new_fm = "\n".join(kept_lines)
            old = " | ".join(v.split(":", 1)[1].strip() for v in dup_lines)
            bumped.append((rel, f"duplicate:{old}", gdate))
            if args.apply and not (args.limit and len(bumped) + len(added) > args.limit):
                new_text = text[: m.start(1)] + new_fm + text[m.end(1) :]
                with open(full, "w", encoding="utf-8") as fh:
                    fh.write(new_text)
            continue

        lu = LU_RE.search(fm)
        if lu:
            current = lu.group(3)
            if args.strict:
                if current == gdate:
                    unchanged += 1
                    continue
                new_fm = LU_RE.sub(
                    lambda mm: f"{mm.group(1)}{mm.group(2)}{gdate}{mm.group(4)}", fm, count=1
                )
                bumped.append((rel, current, gdate))
            else:
                if current >= gdate:
                    skipped["future_or_equal"] += 1
                    continue
                new_fm = LU_RE.sub(
                    lambda mm: f"{mm.group(1)}{mm.group(2)}{gdate}{mm.group(4)}", fm, count=1
                )
                bumped.append((rel, current, gdate))
        else:
            if not args.add_missing:
                skipped["unsupported"] += 1
                continue
            quote = '"'
            new_fm = fm + f"\nlast_updated: {quote}{gdate}{quote}"
            added.append((rel, gdate))

        if args.apply and not (args.limit and len(bumped) + len(added) > args.limit):
            new_text = text[: m.start(1)] + new_fm + text[m.end(1) :]
            with open(full, "w", encoding="utf-8") as fh:
                fh.write(new_text)

    total_changes = len(bumped) + len(added)
    if args.limit and total_changes > args.limit:
        print(f"NOTE: --limit {args.limit} reached; {total_changes - args.limit} further changes not written")

    if not args.quiet:
        mode = "APPLY" if args.apply else "DRY-RUN"
        print(f"[{mode}] pages scanned={len(pages)} bumped={len(bumped)} added={len(added)} unchanged={unchanged}")
        for rel, old, new in bumped[:40]:
            print(f"  bump {old} -> {new}  {rel}")
        if len(bumped) > 40:
            print(f"  ... {len(bumped) - 40} more bumps")
        for rel, new in added[:40]:
            print(f"  add  {new}  {rel}")
        if len(added) > 40:
            print(f"  ... {len(added) - 40} more adds")
        print("  skipped: " + ", ".join(f"{k}={v}" for k, v in skipped.items()))
        if bumped:
            dates = [b[2] for b in bumped]
            print(f"  newest git date in bumps: {max(dates)}  today: {dt.date.today().isoformat()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
