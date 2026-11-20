#!/usr/bin/env python3
"""split_sweep_log.py - keep the External MCP Server Catalog page under the crawl limit.

WHY (2026-11-19): ``hermes/mcp/servers/external/index.md`` had grown to 2.18 MB of
Markdown because every sweep appends a "## 🆕 <date> - <slot> Sweep" section to it.
The rendered page measured 3.66 MB and then 3.84 MB, over the 2 MB crawl limit, so
Google can stop indexing the catalog (defect DEF-2026-11-16-01). The sweep log is
history, not the catalog: it belongs on its own page, and the index should carry only
the newest few passes plus a link.

What this does, idempotently:
  * every ``## 🆕 ...`` sweep section beyond the newest ``--keep`` (default 3) is moved
    off ``index.md`` and prepended to ``changelog.md`` (newest first, no duplication)
  * ``changelog.md`` is created with frontmatter if it does not exist
  * the docs/ twin and the legacy root mirror are written together, so the
    check_mirror_parity gate stays green

Run it from the docs repo root:
    python3 scripts/split_sweep_log.py            # dry run
    python3 scripts/split_sweep_log.py --apply
"""
from __future__ import annotations

import argparse
import os
import re
import sys

REL = os.path.join("hermes", "mcp", "servers", "external", "index.md")
CHANGELOG_REL = os.path.join("hermes", "mcp", "servers", "external", "changelog.md")
SWEEP_RE = re.compile(r"^## 🆕 ", re.M)

CHANGELOG_FRONTMATTER = """---
title: "External MCP Server Catalog - Sweep Log"
description: "Every discovery pass behind the CorpusIQ external MCP server catalog: what moved in the directory, what was measured, and what was held"
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/changelog/"
robots: "index,follow"
last_updated: "{stamp}"
tags: ["mcp server", "model context protocol", "sweep log"]
---

# External MCP Server Catalog - Sweep Log

Every discovery pass behind the [external MCP server catalog](/hermes/mcp/servers/external/), newest first. Each entry records what the mcpservers.org and mcp.so surfaces returned, which candidates were measured, and what was held and why.

"""


def sweep_sections(text: str) -> list[tuple[int, str]]:
    """(start_offset, section_text) for each '## 🆕 ' sweep section, in file order."""
    starts = [m.start() for m in SWEEP_RE.finditer(text)]
    out = []
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else len(text)
        out.append((s, text[s:e]))
    return out


def split(text: str, keep: int):
    sections = sweep_sections(text)
    if len(sections) <= keep:
        return None
    move_from = sections[keep][0]
    # The movable run ends where the catalog body resumes: the first heading after
    # the LAST sweep section that is NOT itself a sweep section. Non-sweep headings
    # inside the historical log (e.g. "## Directory Status Re-Verified") stay with
    # the log, not with the index.
    last_start = sections[-1][0]
    tail = text[last_start:]
    move_end = len(text)
    for m in re.finditer(r"^## ", tail, re.M):
        head = tail[m.start():m.start() + 40]
        if not head.startswith("## 🆕 "):
            move_end = last_start + m.start()
            break
    moved = text[move_from:move_end]
    new_index = text[:move_from] + text[move_end:]
    return move_end, new_index, moved


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--keep", type=int, default=3)
    ap.add_argument("--repo", default=".")
    a = ap.parse_args()

    index_path = os.path.join(a.repo, REL)
    text = read(index_path)
    res = split(text, a.keep)
    if res is None:
        print("index already within %d sweep sections (%.1f KB) - nothing to move"
              % (a.keep, len(text) / 1024))
        return 0
    _, new_index, moved = res
    print("index  %.1f KB -> %.1f KB" % (len(text) / 1024, len(new_index) / 1024))
    print("moving %.1f KB of sweep log (%d sections)"
          % (len(moved) / 1024, len(sweep_sections(moved))))
    if not a.apply:
        print("dry run - pass --apply to write")
        return 0

    log_path = os.path.join(a.repo, CHANGELOG_REL)
    if os.path.exists(log_path):
        log = read(log_path)
        marker = "\n## 🆕 "
        i = log.find(marker)
        head, body = (log[:i + 1], log[i + 1:]) if i > 0 else (log, "")
        new_log = head + moved + body
    else:
        stamp = re.search(r'last_updated:\s*"(\d{4}-\d{2}-\d{2})"', text)
        fm = CHANGELOG_FRONTMATTER.format(stamp=stamp.group(1) if stamp else "2026-11-19")
        new_log = fm + moved

    for rel, content in ((CHANGELOG_REL, new_log), (REL, new_index)):
        write(os.path.join(a.repo, rel), content)
        write(os.path.join(a.repo, "docs", rel), content)
    print("wrote %s and %s (plus docs/ twins)" % (REL, CHANGELOG_REL))
    return 0


if __name__ == "__main__":
    sys.exit(main())
