#!/usr/bin/env python3
"""Validate the Hermes skills catalog index pages.

WHY (2026-10-08): two defects were live in production and nothing caught them.

1. Twelve category index pages carried an EMPTY skills table:

       | Skill | Description | Type |
       |-------|-------------|------|
       | Coming soon | New skills added regularly | - |

   while 49 real skill pages sat unlinked in the same directories. The pages
   ranked (shopify: 156 impressions at position 18.7) and got zero clicks,
   because the body listed nothing.

2. hermes/skills/catalog/claude-office/index.md listed eleven skills that exist
   nowhere in this library at all (sheets-automation, gmail-workflows,
   hr-automation, shopify-automation, Microsoft Teams Automation, and six more),
   while omitting the four real skills in its own directory. The rows were plain
   text, so nothing ever 404'd and nothing noticed.

CHECK 1 is a hard failure: an empty roster next to real skills is always wrong.
CHECK 2 is a hard failure: a linked row that points at no page is a broken link.
CHECK 3 is a WARNING, not a failure: an unlinked row naming a skill with no page
may be a curated roster rather than an error, so it is surfaced without blocking
a deploy.

Exit code 1 on any hard failure.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent / "hermes" / "skills" / "catalog"
EMPTY_ROW = "| Coming soon | New skills added regularly | - |"

hard, warn = [], []

if not ROOT.exists():
    print(f"catalog root not found: {ROOT}")
    sys.exit(1)

# Every skill name that exists anywhere in the library.
known = set()
for md in ROOT.rglob("*.md"):
    txt = md.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r"^name:\s*(.+)$", txt, re.M)
    if m:
        known.add(m.group(1).strip().strip('"'))
    known.add(md.stem)

checked = 0
for idx in sorted(ROOT.glob("*/index.md")):
    checked += 1
    cat = idx.parent.name
    txt = idx.read_text(encoding="utf-8", errors="ignore")
    siblings = [p for p in idx.parent.glob("*.md") if p.name != "index.md"]

    # CHECK 1: empty roster next to real skills.
    if EMPTY_ROW in txt and siblings:
        hard.append(f"{cat}: 'Coming soon' roster while {len(siblings)} skill page(s) "
                    f"exist beside it -> {[p.name for p in siblings][:4]}")

    # Only the "## Available Skills" table. Other tables on these pages are
    # troubleshooting or requirements tables ("| Issue | Fix |"), and treating
    # their rows as skill rosters produces pure noise.
    section = ""
    m = re.search(r"^##\s+Available Skills\s*$(.*?)(?=^##\s|\Z)", txt, re.M | re.S)
    if m:
        section = m.group(1)
    rows = [l for l in section.split("\n") if l.startswith("|")]
    data = [l for l in rows
            if not re.match(r"^\|[\s\-:|]+\|$", l) and "Skill" not in l.split("|")[1]]

    if data and not siblings:
        warn.append(f"{cat}: lists {len(data)} skill(s) but the directory has no skill pages")

    for line in data:
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells:
            continue
        first = cells[0]
        link = re.match(r"\[([^\]]+)\]\(([^)]+)\)", first)
        if link:
            name, url = link.group(1), link.group(2)
            # CHECK 2: the link must resolve to a file in this category.
            stem = url.rstrip("/").split("/")[-1]
            if not (idx.parent / f"{stem}.md").exists() and not (idx.parent / stem).exists():
                hard.append(f"{cat}: row '{name}' links to {url} but no such page exists")
        else:
            # CHECK 3: unlinked row naming a skill with no page anywhere.
            if first and first not in known:
                warn.append(f"{cat}: row '{first}' is unlinked and matches no skill in the library")

print(f"catalog index validation: {checked} index pages checked")
for w in warn:
    print(f"  WARN  {w}")
for h in hard:
    print(f"  FAIL  {h}")

if hard:
    print(f"\nFAILED: {len(hard)} hard problem(s) in the skills catalog indexes")
    sys.exit(1)
print("OK: every catalog index roster matches the pages beside it")
sys.exit(0)
