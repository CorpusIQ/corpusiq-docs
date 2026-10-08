#!/usr/bin/env python3
"""Generate the Hermes skills catalog rosters from the directory contents.

WHY (2026-10-08): the rosters had drifted badly. Twelve category index pages
carried an empty "Coming soon" table while 49 real skill pages sat unlinked
beside them, and one page listed eleven skills that exist nowhere in the
library. Those were repaired by hand, which means they can drift again.

The roster is DERIVED data: it is a list of the .md files in its own directory.
Derived data should be generated, not maintained. This regenerates the
"## Available Skills" table for every category index from the files beside it,
so the directory is the single source of truth, exactly as the connector pages
take their skill lists from data/build/skills.json rather than hand-coding them.

Idempotent: writes only when the generated table differs, so it produces no
commit noise. Reports every change it makes.

Pairs with scripts/validate_catalog_indexes.py, which stays as the independent
safety net: this script writes the rosters, the validator checks the result
against the same directories. Generation plus an independent check, so a bug in
either one is still caught.

USAGE
    python3 scripts/generate_catalog_indexes.py            # report only (dry)
    python3 scripts/generate_catalog_indexes.py --fix      # write changes
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "hermes" / "skills" / "catalog"
HEADING = "## Available Skills"
NEXT_HEADING = re.compile(r"^##\s", re.M)
TABLE_HEADER = ["| Skill | Installs | Description |", "|-------|----------|-------------|"]


def frontmatter(path: Path) -> dict:
    txt = path.read_text(encoding="utf-8", errors="ignore")
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    fm: dict[str, str] = {}
    if m:
        for line in m.group(1).split("\n"):
            mm = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if mm:
                fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm


def installs(desc: str) -> str:
    m = re.search(r"([\d.]+)\s*([KMkm])?\s*installs", desc or "")
    if not m:
        return ""
    num, suffix = float(m.group(1)), (m.group(2) or "").upper()
    if suffix == "K":
        return f"{num:,.1f}K".replace(".0K", "K")
    if suffix == "M":
        return f"{num:,.1f}M".replace(".0M", "M")
    return f"{int(num):,}"


def clean(desc: str) -> str:
    """Description as it should read inside a table cell.

    Strips the install count (it has its own column) and any trailing install
    command, which belongs on the skill page rather than in a roster row.

    Deliberately does NOT collapse internal whitespace: this repo writes its
    dashes as '  --  ' with double spaces, so collapsing runs would silently
    rewrite the house style. Only the ends are trimmed.

    The install-command cut uses a plain string search rather than a regex
    because this box's `re` shim has broken backtracking on \\S, which left a
    stray fragment ("resciencelab/opc-skills@seo-geo.") behind.
    """
    d = re.sub(r"\s*[\d.]+\s*[KMkm]?\s*installs\.?", "", desc or "")
    for marker in ("npx skills add", "npx skills"):
        i = d.find(marker)
        if i != -1:
            d = d[:i]
            break
    d = d.strip()
    return d if d.endswith(".") else d + "."


def sort_key(row: tuple[str, str, str, str]) -> float:
    raw = row[1].replace(",", "")
    try:
        if raw.endswith("K"):
            return -float(raw[:-1]) * 1000
        if raw.endswith("M"):
            return -float(raw[:-1]) * 1_000_000
        return -float(raw)
    except ValueError:
        return 1  # entries without a count sort last, alphabetically


def build_table(cat: str, skills: list[Path]) -> str:
    """Roster table with absolute links, matching the house style used by the
    Related sections on these same pages ([/hermes/skills/catalog](/hermes/skills/catalog))."""
    rows = []
    for s in skills:
        fm = frontmatter(s)
        rows.append((fm.get("name") or s.stem, installs(fm.get("description", "")),
                     clean(fm.get("description", "")), s.stem))
    rows.sort(key=sort_key)
    out = list(TABLE_HEADER)
    for name, inst, desc, stem in rows:
        out.append(f"| [{name}](/hermes/skills/catalog/{cat}/{stem}/) | {inst} | {desc} |")
    return "\n".join(out)


def main() -> int:
    write = "--fix" in sys.argv
    changed = checked = 0

    for idx in sorted(ROOT.glob("*/index.md")):
        txt = idx.read_text(encoding="utf-8")
        if HEADING not in txt:
            continue
        skills = sorted(p for p in idx.parent.glob("*.md") if p.name != "index.md")
        if not skills:
            continue
        checked += 1

        start = txt.index(HEADING) + len(HEADING)
        m = NEXT_HEADING.search(txt, start)
        end = m.start() if m else len(txt)
        body = txt[start:end]

        # Replace only the table block. Any italic note in this section is
        # dropped: notes like "*Roster refreshed in the Sep 29 sweep.*" were
        # disclosure for hand-maintained rosters, and the roster is generated
        # now. Keeping them also made this script non-idempotent, because a note
        # that sat after the table was re-emitted on every run and multiplied.
        lines = body.split("\n")
        table_lines = [l for l in lines if l.startswith("|")]
        head_lines = [l for l in lines if not l.startswith("|")]
        head = "\n".join(head_lines).rstrip()
        head = re.sub(r"\n*\s*\*[^*\n]{10,}\*\s*$", "", head).rstrip()

        new_body = f"{head}\n\n{build_table(idx.parent.name, skills)}\n\n"
        new_txt = txt[:start] + new_body + txt[end:]

        if new_txt != txt:
            changed += 1
            print(f"  {'WROTE' if write else 'WOULD WRITE'} {idx.parent.name:<18} "
                  f"{len(table_lines)} row(s) -> {len(skills)} row(s)")
            if write:
                idx.write_text(new_txt, encoding="utf-8")

    print(f"\n{checked} catalog index page(s) with skills; {changed} out of date")
    if changed and not write:
        print("(dry run; re-run with --fix to write, which the deploy pipeline does)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
