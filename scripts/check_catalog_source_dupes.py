#!/usr/bin/env python3
"""Fail when a skills-catalog guide cites a retired publisher identity.

Why this exists
---------------
A repository rename creates a second guide for one project, and nothing in the
tree notices. On 2026-11-03 the catalog published ``openmontage-setup.md`` for
``calesthio/openmontage``. The publisher renamed the GitHub organisation to
``openmontageinc``, and the 2026-11-09 sweep saw ``openmontageinc/openmontage``
as a fresh cluster and published ``openmontage-video-skills-setup.md``. Two
pages, one repository, two self-canonical URLs, ``index,follow`` on both, and
the older page carrying an owner name, a star count and an install figure that
had all moved on.

``check_source_url_collisions.py`` did not catch it: that gate compares OUTPUT
URLs, and these pages publish to two different ones. Nothing compared the
SOURCE identity, and an offline parser cannot tell that ``calesthio/openmontage``
and ``openmontageinc/openmontage`` are the same project - the GitHub API that
would answer that is not available inside CI.

So identity is recorded, not guessed. ``scripts/catalog_source_aliases.json``
holds the rename map:

    {"aliases": {"retired-owner/repo": "current-owner/repo"}}

This gate then enforces one rule: **no catalog guide may cite a retired
identity.** After a rename, the sweep must repoint the existing guide, not
publish a second one. The retired row stays in the map so the same rename can
never quietly reintroduce a duplicate page.

Scope, deliberately narrow
--------------------------
This is NOT "one page per repository". A monorepo legitimately gets one guide
per skill: ``nousresearch/hermes-agent`` carries fifteen catalog pages, one per
published skill, and all fifteen cite the same source on purpose. Collapsing
those would delete real pages, so the gate never groups by repository. It only
fires on the identity that is known to be retired.

Usage
-----
    python3 scripts/check_catalog_source_dupes.py [--root DIR]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CATALOG_GLOB = "hermes/skills/catalog/**/*.md"
ALIAS_FILE = "scripts/catalog_source_aliases.json"

# The published line is "**Source:** [owner/repo](https://www.skills.sh/owner/repo)".
# Anchor on the URL, not the link text: the text is prose and gets rewritten,
# the URL is the machine identity.
SOURCE_RE = re.compile(
    r"\*\*Source:\*\*[^\n]*?(?:https?://(?:www\.)?skills\.sh"
    r"|https?://(?:www\.)?github\.com)/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)",
    re.IGNORECASE,
)


def load_config(root: Path) -> tuple[dict[str, str], dict[str, str]]:
    path = root / ALIAS_FILE
    if not path.exists():
        return {}, {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # a broken map must fail loudly, not skip the gate
        raise SystemExit(f"{ALIAS_FILE}: not valid JSON ({exc})")
    aliases = {
        str(k).strip().strip("/").lower(): str(v).strip().strip("/").lower()
        for k, v in (data.get("aliases") or {}).items()
    }
    retired_ok = {
        str(k).strip().strip("/").lower(): str(v)
        for k, v in (data.get("retired_ok") or {}).items()
    }
    return aliases, retired_ok


def source_of(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    # The header block carries the Source line. The body repeats skills.sh URLs
    # inside install commands and related links; anchoring on the bold label
    # keeps those out of the identity.
    for line in text.splitlines()[:80]:
        if line.lstrip().lower().startswith("**source:**"):
            match = SOURCE_RE.search(line)
            if match:
                return match.group(1).strip().strip("/").lower()
            return None
    return None


def main(argv: list[str]) -> int:
    root = Path(".")
    if "--root" in argv:
        root = Path(argv[argv.index("--root") + 1])
    aliases, retired_ok = load_config(root)

    scanned = 0
    failures: list[tuple[str, str, str]] = []
    for path in sorted(root.glob(CATALOG_GLOB)):
        if path.name == "index.md":
            continue
        source = source_of(path)
        scanned += 1
        if not source:
            continue
        target = aliases.get(source)
        if not target:
            continue
        rel = path.relative_to(root).as_posix()
        if source in retired_ok:
            continue
        failures.append((rel, source, target))

    if not failures:
        print(
            f"OK: {scanned} catalog guides scanned, none cite a retired "
            f"publisher identity ({len(aliases)} alias rows)"
        )
        return 0

    print(f"FAIL: {len(failures)} guide(s) cite a publisher identity that has moved")
    for rel, source, target in failures:
        print(f"\n  {rel}")
        print(f"    retired: {source}")
        print(f"    current: {target}")
    print(
        "\nFix: leave one guide for the project. Either repoint the existing page "
        "at the current publisher (Source line, install command and the facts "
        "that moved) or delete the superseded page and add a 301 in vercel.json "
        "from its slug to the survivor, then repoint the catalog and marketplace "
        "index entries. Keep the retired row in "
        f"{ALIAS_FILE} so the sweep cannot republish a second page. If a page "
        "must stay on the retired name for a stated reason, record it under "
        "retired_ok there."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
