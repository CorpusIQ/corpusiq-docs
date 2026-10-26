#!/usr/bin/env python3
"""Fail if any tracked content file carries unresolved merge-conflict markers.

Why this exists (2026-10-26)
----------------------------
Two agent lanes share one clone on this host. A lane ran `git pull --rebase`,
hit a conflict with another lane's unpushed commit, aborted, and the following
`git reset --hard` destroyed the commit. Minutes later an automated
"chore: docs perfection autofix" routine committed the half-resolved working
tree, so four published pages (`ecosystem.md`, `ecosystem/index.md`,
`contributors.md`, `contributors/index.md`) carried `<<<<<<<` / `=======` /
`>>>>>>>` blocks. Nothing on the deploy path would have stopped them: mkdocs
renders the markers as body text, so the live site would have shown the
conflict garbage to readers.

The markers are unambiguous and cheap to detect, so this is a hard gate.

Detection
---------
A file is reported only when it contains an opening marker line
(`^<<<<<<< `) together with either a separator line (`^=======$`) or a
closing marker line (`^>>>>>>> `). Requiring the pair avoids flagging a
setext heading underline (`=======`) used on its own, which is legal
Markdown.

Usage:
    python3 scripts/validate_no_conflict_markers.py [repo_root]
Exit codes: 0 clean, 1 markers found (or scan error).
"""
import os
import re
import subprocess
import sys

SKIP_DIRS = {".git", "__pycache__", "node_modules", "site", ".venv", "venv"}
SUFFIXES = (".md", ".mdx", ".json", ".py", ".yml", ".yaml", ".txt", ".mjs", ".js")

OPEN_RE = re.compile(r"^<<<<<<< ")
MID_RE = re.compile(r"^=======\s*$")
CLOSE_RE = re.compile(r"^>>>>>>> ")


def tracked_files(root):
    """Prefer git's index (authoritative, skips build output), fall back to a walk."""
    try:
        out = subprocess.run(
            ["git", "-C", root, "ls-files"],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
        if out:
            return [p for p in out if p.endswith(SUFFIXES)]
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(SUFFIXES):
                found.append(os.path.relpath(os.path.join(dirpath, name), root))
    return found


def scan(path):
    """Return list of (line_number, text) for marker lines in one file."""
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.read().splitlines()
    except OSError as exc:
        return [(-1, f"unreadable: {exc}")]
    has_open = any(OPEN_RE.match(line) for line in lines)
    has_mid = any(MID_RE.match(line) for line in lines)
    has_close = any(CLOSE_RE.match(line) for line in lines)
    if not (has_open and (has_mid or has_close)):
        return []
    hits = []
    for i, line in enumerate(lines, 1):
        if OPEN_RE.match(line) or MID_RE.match(line) or CLOSE_RE.match(line):
            hits.append((i, line.strip()[:80]))
    return hits


def main(argv):
    root = argv[1] if len(argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = tracked_files(root)
    bad = 0
    for rel in files:
        hits = scan(os.path.join(root, rel))
        if hits:
            bad += 1
            print(f"CONFLICT MARKERS: {rel}")
            for num, text in hits[:6]:
                print(f"   line {num}: {text}")
    if bad:
        print(f"\nFAIL: {bad} file(s) with unresolved merge-conflict markers. "
              f"Resolve or restore before publishing.")
        return 1
    print(f"OK: no conflict markers across {len(files)} tracked content file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
