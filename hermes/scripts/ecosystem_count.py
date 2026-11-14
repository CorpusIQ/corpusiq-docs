#!/usr/bin/env python3
"""Recount catalogue entries per section of hermes/ecosystem/index.md.

A catalogued "repo" here = a distinct github.com/<owner>/<repo> target that
appears either as an ``### owner/repo`` heading or inside a section table row.
That is the unit the page's nav table and stats table claim to count, so
counting it directly is the only way to keep the declared numbers true.

Sections after the 18 catalog sections (Ecosystem Stats, Cross-Reference Index,
Operational Playbooks, Level-Up Blueprints, Contributing, FAQ, Related Pages,
New Additions) are infrastructure, not catalogue, and are excluded.
"""
import json
import re
import sys

PATH = "ecosystem/index.md"
CATALOG_END = "## \U0001f4ca Ecosystem Stats"  # "## Ecosystem Stats"
LINK_RE = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")


def slug(m):
    owner, repo = m.group(1).lower(), m.group(2).lower()
    if repo.endswith(".git"):
        repo = repo[:-4]
    return (owner, repo)


def main():
    text = open(PATH).read()
    end = text.find(CATALOG_END)
    if end == -1:
        print("ERROR: stats section marker not found", file=sys.stderr)
        return 1
    body = text[:end]

    sections = []  # [name, set_of_repos]
    cur = None
    self_slug = ("corpusiq", "corpusiq-docs")
    for line in body.split("\n"):
        h2 = re.match(r"^## (.+)$", line)
        if h2:
            name = re.sub(r"^[^\w]+", "", h2.group(1)).strip()
            cur = [name, set()]
            sections.append(cur)
            continue
        if cur is None:
            continue
        for m in LINK_RE.finditer(line):
            s = slug(m)
            if s == self_slug:
                continue
            cur[1].add(s)

    total = 0
    out = []
    for name, repos in sections:
        total += len(repos)
        out.append({"section": name, "repos": len(repos)})
    print(json.dumps({"sections": out, "catalog_total": total}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
