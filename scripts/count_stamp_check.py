#!/usr/bin/env python3
"""Block a deploy when a page's own count stamps disagree with each other.

Why
---
The Skills Marketplace page carried two totals for the same fact at the same
time: the header said "1,157+ curated skill repos across 22 categories" and the
footer on the same page said "Total: 1,151+ curated skill repos across 22
categories". The JSON-LD block repeated the stale 1,151+. A reader scrolling to
the bottom was told a different number than the reader at the top, and every
sweep bumps one stamp while the others are forgotten (Oct 24 2026: the evening
sweep moved 1,152+ to 1,157+ and left three mentions behind).

The class is the same one reconcile_ecosystem_counts.py fixes for the ecosystem
directory: hand-maintained derived numbers drift. That script derives the value
from the directory and rewrites it; this one cannot derive an external skills.sh
total from the repo, so it enforces the weaker but still load-bearing invariant:
inside one page, every stamp for the same claim must be identical.

Historical stamps are not drift. A batch page records a transition
("1,151+ to 1,152+"), so ranges are excluded from the comparison.

Usage:
    python3 scripts/count_stamp_check.py [repo_root] [--list]

Exit 0 when every page is internally consistent, 1 when any page disagrees.
"""
import re
import sys
from pathlib import Path

# claim -> the phrase that follows the number, used to scope the stamp.
# Add a claim here when a new hand-maintained total appears on a page.
CLAIMS = [
    r"curated skill repos?(?:itory|itories)?",
    r"curated skills",
]

# A transition log, not a published total ("1,151+ to 1,152+").
RANGE_RE = re.compile(r"([\d,]+)\+\s+to\s+([\d,]+)\+")

SCAN_DIRS = [
    "hermes/skills/marketplace",
    "hermes/skills",
]


def stamps(text, phrase):
    """Every non-range '<n>+ <phrase>' stamp as (line_no, raw_number)."""
    pattern = re.compile(r"([\d,]+)\+\s+" + phrase + r"\b")
    ranges = set()
    for m in RANGE_RE.finditer(text):
        ranges.add(m.start(1))
    out = []
    for m in pattern.finditer(text):
        if m.start(1) in ranges:
            continue
        line_no = text.count("\n", 0, m.start()) + 1
        out.append((line_no, m.group(1), int(m.group(1).replace(",", ""))))
    return out


def check_file(path: Path, show=False):
    text = path.read_text(encoding="utf-8", errors="replace")
    problems = []
    for phrase in CLAIMS:
        found = stamps(text, phrase)
        if len({n for _, _, n in found}) > 1:
            detail = ", ".join(f"line {ln}: {raw}+" for ln, raw, _ in found)
            problems.append((phrase, detail))
        elif show and found:
            print(f"    {path}: {found[0][1]}+ {phrase} ({len(found)} stamps, agree)")
    return problems


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = Path(args[0] if args else ".").resolve()
    show = "--list" in sys.argv

    files = []
    seen = set()
    for d in SCAN_DIRS:
        base = root / d
        if base.is_dir():
            for p in sorted(base.rglob("*.md")):
                if p in seen:
                    continue
                seen.add(p)
                files.append(p)

    failures = 0
    checked = 0
    for path in files:
        rel = path.relative_to(root)
        if "/site/" in str(rel) or str(rel).startswith("site/"):
            continue
        checked += 1
        problems = check_file(path, show=show)
        for phrase, detail in problems:
            failures += 1
            print(f"FAIL {rel}: stamps disagree for '{phrase}' -> {detail}")

    if failures:
        print(f"\n{failures} page(s) with disagreeing count stamps across {checked} file(s)")
        print("Fix: make every stamp on the page carry the current total (the header one).")
        return 1

    print(f"OK: count stamps agree across {checked} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
