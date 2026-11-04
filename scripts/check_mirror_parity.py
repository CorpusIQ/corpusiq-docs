#!/usr/bin/env python3
"""check_mirror_parity.py - keep the root Markdown mirror honest.

WHY (2026-11-03): this repository carries a pre-migration mirror of the docs
tree at the repo root (``api/``, ``connectors/``, ``hermes/``, ...) alongside
the published tree under ``docs/``. MkDocs builds ``docs/`` only, so the root
copies are never rendered - but they are public in the repository, where
GitHub search, crawlers and AI assistants read them.

Of 2,984 root/docs file-name pairs, 2,968 are byte-identical apart from the
``last_updated`` stamp: the mirror is maintained, not a leftover. Nothing
enforced that parity, so drift was invisible. It had already happened:

  * ``api/authentication.md`` still claimed "API keys do not expire
    automatically" while the published page documents a 60-minute bearer
    token expiry - two different answers from one company.
  * five ``api/*.md`` files pointed at ``https://api.corpusiq.io``, a host
    that returns DEPLOYMENT_NOT_FOUND. The published pages name the live host.
  * cause: PR #141 (38708851b9) edited ``docs/api/authentication.md`` alone,
    while the previous change (8ce1ed147a) had updated both copies.

The seven root section READMEs are deliberately NOT mirrors: a folder README
for someone browsing the repo is a different document from the site landing
page of the same name. They are allowlisted, not silently ignored.

Usage:
    python3 scripts/check_mirror_parity.py          # exit 1 on drift
    python3 scripts/check_mirror_parity.py --list   # also print matched pairs
"""

from __future__ import annotations

import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories never part of the mirror.
SKIP_DIRS = {
    ".git", "site", "node_modules", "__pycache__", ".vercel",
    "published-content", "docs", "scripts", ".github",
}

# Root section READMEs are their own documents, not mirror copies.
ALLOWLIST = {
    "README.md",
    "architecture/README.md",
    "governance/README.md",
    "onboarding/README.md",
    "reporting/README.md",
    "search/README.md",
    "security/README.md",
}


def strip_stamp(text: str) -> str:
    """Drop the last_updated frontmatter line and trailing blank noise.

    The stamp is deliberately excluded: each copy carries its own date, and
    scripts/sync_last_updated.py owns those values.
    """
    out = []
    for line in text.splitlines():
        if line.strip().startswith("last_updated:"):
            continue
        out.append(line.rstrip())
    while out and not out[-1]:
        out.pop()
    return "\n".join(out)


def main() -> int:
    show_list = "--list" in sys.argv
    checked = 0
    drift = []

    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            root_path = os.path.join(dirpath, name)
            rel = os.path.relpath(root_path, REPO).replace(os.sep, "/")
            if rel in ALLOWLIST:
                continue
            twin = os.path.join(REPO, "docs", rel)
            if not os.path.exists(twin):
                continue
            checked += 1
            try:
                a = open(root_path, encoding="utf-8", errors="replace").read()
                b = open(twin, encoding="utf-8", errors="replace").read()
            except OSError as exc:
                drift.append(f"{rel}: unreadable ({exc})")
                continue
            if strip_stamp(a) != strip_stamp(b):
                la, lb = len(strip_stamp(a).splitlines()), len(strip_stamp(b).splitlines())
                drift.append(f"{rel}: root copy differs from docs/ twin ({la} vs {lb} lines)")

    print(f"mirror pairs checked: {checked}")
    if show_list:
        print("allowlisted as intentionally different: " + ", ".join(sorted(ALLOWLIST)))

    if drift:
        print(f"FAIL: {len(drift)} root copy(ies) diverged from docs/")
        for line in drift:
            print(f"  {line}")
        print()
        print("Fix: copy the docs/ twin over the root copy (the published tree wins),")
        print("or add the path to ALLOWLIST in this script if it is a different document.")
        return 1

    print("OK: every root mirror copy matches its docs/ twin")
    return 0


if __name__ == "__main__":
    sys.exit(main())
