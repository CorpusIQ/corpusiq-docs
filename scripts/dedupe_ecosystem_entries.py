#!/usr/bin/env python3
"""Remove duplicate entries from the ecosystem directory.

Why
---
The directory is assembled by several sweeps. Each sweep appends the repos it
found; none of them checks whether the repo is already listed. By 2026-10-28 six
repos appeared twice (three inside a single category, three in two categories),
which inflated the visible entry count and pushed a hand-bump of the Quick
Navigation numbers to 33/63/5 against a 31/62/4 census -- two answers to one
question on one page.

Rule: first occurrence wins. A repo is listed once, in the category that first
claimed it; every later copy is removed with its block (heading through the
trailing "---" separator). Deterministic, so the result does not depend on
which sweep ran last.

Usage:
    python3 scripts/dedupe_ecosystem_entries.py [repo_root] [--check]
"""
import os
import re
import sys

INDEX = "hermes/ecosystem/index.md"
HEAD = re.compile(r"^###\s+(.+?)\s*$")
RULE = re.compile(r"^---\s*$")


def blocks(lines):
    """Yield (heading, start, end_exclusive) for each '### name' entry block."""
    starts = [(i, HEAD.match(l).group(1)) for i, l in enumerate(lines) if HEAD.match(l)]
    for k, (start, name) in enumerate(starts):
        limit = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        # stop early at the next '## ' section heading
        end = limit
        for j in range(start + 1, limit):
            if lines[j].startswith("## "):
                end = j
                break
        # swallow the trailing separator and one blank line after it
        j = end - 1
        while j > start and not lines[j].strip():
            j -= 1
        if j > start and RULE.match(lines[j]):
            end = min(end, j + 1)
            if end < len(lines) and not lines[end].strip():
                end += 1
        yield name, start, end, limit


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    root = args[0] if args else os.path.expanduser("~/workspace/corpusiq-docs")
    path = os.path.join(root, INDEX)
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")

    seen = {}
    drop = []
    for name, start, end, limit in blocks(lines):
        if name in seen:
            drop.append((name, start, end, seen[name]))
        else:
            seen[name] = start

    if not drop:
        print("OK: every entry appears exactly once")
        return 0

    label = "WOULD REMOVE" if check else "removed"
    for name, start, end, first in drop:
        print(f"  {label}: duplicate '{name}' at line {start + 1} "
              f"(first listed at line {first + 1}), {end - start} lines")
    if check:
        return 1

    for name, start, end, _first in sorted(drop, key=lambda d: -d[1]):
        del lines[start:end]
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"deduped {len(drop)} duplicate entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
