#!/usr/bin/env python3
"""Reconcile every published ecosystem count stamp against the directory itself.

Why
---
The "N+ repos" claim is hand-bumped in several files and the number had drifted
three ways at once: the served directory said 199+, the pages that link to it
said 196+, and the shadowed twin said 197+, while the page actually carries ~395
repo entries across 19 categories (the stamp also said 14 categories).

Derived data is generated, not maintained. This script counts the entries in
hermes/ecosystem/index.md (the page users see) and rewrites every stamp from
that count, so the numbers cannot disagree. Idempotent: a second run is a no-op.

Usage:
    python3 scripts/reconcile_ecosystem_counts.py [repo_root] [--check]

--check prints the drift and exits 1 when anything would change.
"""
import json
import os
import re
import sys

SURFACES = [
    "hermes/ecosystem/index.md",
    "hermes/ecosystem.md",
    "hermes/README.md",
    "hermes/index.md",
    "hermes/agent-marketplace.md",
]

# Sections that are navigation or prose, not directories of entries.
NON_CATEGORY = {
    "quick-navigation", "ecosystem-stats", "cross-reference-index",
    "operational-playbooks", "level-up-blueprints", "contributing",
    "faq", "related-pages",
}


def canon(anchor):
    """One anchor spelling for both sides: collapse dashes, drop edge dashes.

    A heading like "🏛 Core & Official" slugs to "-core--official" while the
    hand-written nav link reads "#core-official". Comparing raw strings silently
    matches nothing, which reads as "no drift" instead of "no comparison".
    """
    return re.sub(r"-+", "-", anchor).strip("-")

REPO_HEADING = re.compile(r"^###\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\s*$")
# Second entry form: table rows that link a repo (Platform-Specific, Domain
# Applications and the Cross-Reference index all use it). Counting only the
# heading form understated those sections as zero.
REPO_TABLE_ROW = re.compile(r"^\|\s*\[([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\]\(https?://github\.com/")


def heading_anchor(text):
    """GitHub/MkDocs slug for a heading, matching the style already in use."""
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return s.replace(" ", "-")


def census(index_text):
    lines = index_text.split("\n")
    sections = []
    for i, line in enumerate(lines):
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            sections.append((i, m.group(1).strip()))
    counts = {}
    distinct = set()
    for idx, (start, title) in enumerate(sections):
        anchor = canon(heading_anchor(title))
        end = sections[idx + 1][0] if idx + 1 < len(sections) else len(lines)
        if anchor in NON_CATEGORY or anchor.startswith("new-additions"):
            continue
        found = set()
        for line in lines[start + 1:end]:
            m = REPO_HEADING.match(line) or REPO_TABLE_ROW.match(line)
            if m:
                found.add(m.group(1))
        counts[anchor] = len(found)
        distinct |= found
    return counts, len(distinct), sum(counts.values())


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    root = args[0] if args else os.path.expanduser("~/workspace/corpusiq-docs")

    index_path = os.path.join(root, "hermes/ecosystem/index.md")
    index_text = open(index_path, encoding="utf-8").read()
    counts, distinct, headings = census(index_text)

    approved_path = os.path.join(root, "hermes/data/approved_repos.json")
    approved = len(json.load(open(approved_path))) if os.path.exists(approved_path) else None

    print(f"directory entries: {headings} headings / {distinct} distinct  categories: {len(counts)}"
          f"  approved ledger: {approved}")
    for anchor, n in counts.items():
        print(f"  {anchor:42s} {n}")

    total = distinct
    cat_count = len(counts)
    changes = []

    def fix(path, pattern, replacement_count, label, flags=0, count_guard=None):
        """Replace group-1 numbers with replacement_count; record whether changed."""
        p = os.path.join(root, path)
        if not os.path.exists(p):
            return
        text = open(p, encoding="utf-8").read()

        def sub(m):
            return m.group(0).replace(m.group(1), str(replacement_count), 1)

        new, n = re.subn(pattern, sub, text, flags=flags)
        if n and new != text:
            changes.append((path, label, n))
            if not check:
                open(p, "w", encoding="utf-8").write(new)

    # --- the directory's own stamps -------------------------------------
    fix("hermes/ecosystem/index.md", r"(\d+)\+ repos, docs", total, "description repos")
    fix("hermes/ecosystem/index.md", r"(\d+)\+ repositories", total, "body repositories")
    fix("hermes/ecosystem/index.md", r"\*\*Repos indexed:\*\* (\d+)\+", total, "repos indexed stamp")
    fix("hermes/ecosystem/index.md", r"(\d+)\+ repos indexed", total, "self entry repos indexed")
    fix("hermes/ecosystem.md", r"(\d+)\+ repos, docs", total, "twin description repos")
    fix("hermes/ecosystem.md", r"(\d+)\+ repositories", total, "twin repositories")
    fix("hermes/ecosystem.md", r"(\d+)\+ repos\b", total, "twin repos")

    # --- the surfaces that link to it -----------------------------------
    fix("hermes/README.md", r"Ecosystem-(\d+)\+_repos", total, "README badge")
    fix("hermes/README.md", r"\*\*(\d+)\+ repos\*\*", total, "README bullet")
    fix("hermes/README.md", r"(\d+)\+ repos indexed", total, "README footer")
    fix("hermes/index.md", r"(\d+)\+ repos\b", total, "hermes index quick link")
    fix("hermes/agent-marketplace.md", r"(\d+)\+ repos indexed", total, "marketplace footer")

    # --- category count --------------------------------------------------
    fix("hermes/ecosystem.md", r"repositories\*\* across (\d+) categories", cat_count, "twin categories")
    fix("hermes/ecosystem.md", r"(\d+) categories", cat_count, "twin categories 2")
    fix("hermes/index.md", r"across (\d+) categories", cat_count, "index categories")
    fix("hermes/README.md", r"indexed across (\d+) categories", cat_count, "README categories")
    fix("hermes/agent-marketplace.md", r"across (\d+) categories", cat_count, "marketplace categories")

    # --- approved-entry count (from the ledger, not a guess) -------------
    if approved is not None:
        fix("hermes/README.md", r"\((\d+) auto-approved", approved, "README auto-approved")
        fix("hermes/ecosystem.md", r"(\d+) auto-approved", approved, "twin auto-approved")

    # --- contributors page: maintainer row must track the live ledger -----
    # contributors.json keeps a LIFETIME approval counter (it never decrements
    # when a dead repo is pruned), so the hand-maintained table drifted to 192
    # while the ledger held 190. Derive the cell from the ledger instead.
    if approved is not None:
        cp = os.path.join(root, "hermes/contributors/index.md")
        if os.path.exists(cp):
            ctext = open(cp, encoding="utf-8").read()
            # | [@CorpusIQ](...) | 2628 | 192 | Maintainer |  -> submissions kept, approved from ledger
            cnew, cn = re.subn(r"^(\| \[@CorpusIQ\]\([^)]*\) \| )(\d+)( \| )(\d+)( \| )",
                               lambda m: f"{m.group(1)}{m.group(2)}{m.group(3)}{approved}{m.group(5)}",
                               ctext, flags=re.M)
            # repos-indexed metric row
            cnew2, cn2 = re.subn(r"^(\| \*\*Repos indexed\*\* \| )\d+( \|)$",
                                 lambda m: f"{m.group(1)}{total}{m.group(2)}", cnew, flags=re.M)
            if cnew2 != ctext:
                changes.append(("hermes/contributors/index.md", "maintainer approved + repos indexed", cn + cn2))
                if not check:
                    open(cp, "w", encoding="utf-8").write(cnew2)

    # --- quick navigation per-category counts ---------------------------
    p = os.path.join(root, "hermes/ecosystem/index.md")
    text = open(p, encoding="utf-8").read()
    nav_changes = 0

    # Preserve the visible label: only the count column changes.
    def nav_sub(m):
        nonlocal nav_changes
        label, anchor, n, arrow = m.group(1), canon(m.group(2)), int(m.group(3)), m.group(4)
        if anchor in counts and counts[anchor] != n:
            nav_changes += 1
            return f"| {label} | {counts[anchor]} | {arrow} |"
        return m.group(0)

    new_text, rows = re.subn(r"^\| (\[[^\]]+\]\(#([^)]+)\)) \| (\d+) \| (\[↓\]\(#[^)]+\)) \|$",
                             nav_sub, text, flags=re.M)
    if nav_changes:
        changes.append(("hermes/ecosystem/index.md", "quick nav counts", nav_changes))
        if not check:
            open(p, "w", encoding="utf-8").write(new_text)

    if not changes:
        print("OK: every count stamp already matches the directory")
        return 0
    for path, label, n in changes:
        print(f"  {'WOULD FIX' if check else 'fixed'}: {path}: {label} ({n})")
    return 1 if check else 0


if __name__ == "__main__":
    sys.exit(main())
