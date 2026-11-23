#!/usr/bin/env python3
"""archive_sweep_log.py - keep every sweep-log page under the 2 MB crawl limit.

WHY (2026-11-23): split_sweep_log.py moved history off the catalog index into
changelog.md, and changelog.md then grew to 1.63 MB of Markdown, which renders
to a 2.36 MB page - over the 2 MB limit Google will fetch. The log is history:
the newest passes stay on changelog.md and older passes move into half-month
archive pages, each small enough to be crawled whole.

Idempotent. Sections are ordered by their date heading, not by file position,
so an appending writer cannot break it. Run from the repo root:
    python3 scripts/archive_sweep_log.py            # dry run
    python3 scripts/archive_sweep_log.py --apply
    python3 scripts/archive_sweep_log.py --check    # CI gate, exit 1 if over
"""
import argparse
import os
import re
import sys

REL = os.path.join("hermes", "mcp", "servers", "external", "changelog.md")
DIR = os.path.dirname(REL)
KEEP = 40
MD_LIMIT = 950 * 1024

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}

HEAD_RE = re.compile(r"^## \U0001F195 (.+?)$", re.M)
DATE_RE = re.compile(r"([A-Z][a-z]+) (\d{1,2}), (\d{4})")


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)


def parse(text):
    """(head, sections) where head is frontmatter+intro, sections are (key, date, body)."""
    starts = [m.start() for m in HEAD_RE.finditer(text)]
    if not starts:
        return text, []
    head = text[:starts[0]]
    out = []
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else len(text)
        body = text[s:e]
        title = HEAD_RE.search(body).group(1).strip()
        m = DATE_RE.search(title)
        key = (int(m.group(3)), MONTHS.get(m.group(1), 13), int(m.group(2))) if m else (0, 13, 0)
        out.append((key, title, body))
    return head, out


FOOTER_MARK = "\n## Archive"


def strip_footer(body):
    """Drop a previously written archive footer so rewriting is idempotent.

    The footer sits after the last sweep section, so parse() folds it into that
    section's body. Without this, every run appended another copy of it and the
    live page carried three of them (2026-11-23).
    """
    i = body.find(FOOTER_MARK)
    return body[:i] if i > 0 else body


def bucket(key):
    """'2026-11a' = days 1-15, '2026-11b' = days 16-31."""
    y, m, d = key
    half = "a" if d <= 15 else "b"
    return "{:04d}-{:02d}{}".format(y, m, half)


def bucket_range(b):
    y, m, half = int(b[:4]), int(b[5:7]), b[7]
    name = [k for k, v in MONTHS.items() if v == m][0]
    return "{} {}, {}".format(name, "1-15" if half == "a" else "16-31", y)


def front(b, stamp, prev_b, next_b):
    name = bucket_range(b)
    return (
        '---\n'
        'title: "Catalog Sweep Log Archive - ' + name + '"\n'
        'description: "External MCP server catalog sweep log, '
        + name + ' archive: directory movement, measured candidates, hold decisions"\n'
        'canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/changelog-' + b + '/"\n'
        'robots: "noindex,follow"\n'
        'last_updated: "' + stamp + '"\n'
        'tags: ["mcp server", "model context protocol", "sweep log"]\n'
        '---\n\n'
        '# External MCP Server Catalog - Sweep Log, ' + name + '\n\n'
        'Archive for ' + name + '. Discovery passes appear newest first. '
        'The [current sweep log](/hermes/mcp/servers/external/changelog) carries the most recent passes.\n\n'
        'Archive: ' + " | ".join(
            "[{}](/hermes/mcp/servers/external/changelog-{})".format(bucket_range(x), x)
            for x in (prev_b, next_b) if x) + '\n\n'
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    path = REL
    text = read(path)
    if a.check:
        size = len(text.encode("utf-8"))
        if size > MD_LIMIT:
            print("FAIL: {} is {:.0f} KB (renders well past 2 MB). "
                  "Run: python3 scripts/archive_sweep_log.py --apply".format(
                      REL, size / 1024.0))
            return 1
        print("OK: {} is {:.0f} KB under the {:.0f} KB cap".format(
            REL, size / 1024.0, MD_LIMIT / 1024.0))
        return 0
    head, sections = parse(text)
    sections.sort(key=lambda s: s[0], reverse=True)
    keep, move = sections[:KEEP], sections[KEEP:]
    groups = {}
    for key, title, body in move:
        groups.setdefault(bucket(key), []).append((key, title, body))
    stamp = "2026-11-23"
    m = re.search(r'last_updated:\s*"(\d{4}-\d{2}-\d{2})"', head)
    if m:
        stamp = m.group(1)
    # Existing archive pages are always regenerated so frontmatter rules
    # (title length, canonical form) are repaired even when nothing moves.
    on_disk = sorted(
        p.split("changelog-")[-1][:-3]
        for p in __import__("glob").glob(os.path.join(DIR, "changelog-20*.md")))
    allb = sorted(set(groups) | set(on_disk))
    print("keeping {} sections; archiving {} into {} page(s)".format(
        len(keep), len(move), len(allb)))
    new_head = head.split("\n## ")[0]
    if not a.apply:
        for b in allb:
            print("  {} -> {} new section(s)".format(b, len(groups.get(b, []))))
        print("dry run - pass --apply to write")
        return 0
    for i, b in enumerate(allb):
        p = os.path.join(DIR, "changelog-" + b + ".md")
        existing = []
        if os.path.exists(p):
            ex_head, existing = parse(read(p))
            m2 = re.search(r'last_updated:\s*"(\d{4}-\d{2}-\d{2})"', ex_head)
            if m2:
                stamp = max(stamp, m2.group(1))
        seen = {x[1] for x in existing}
        merged = existing + [x for x in groups.get(b, []) if x[1] not in seen]
        merged.sort(key=lambda s: s[0], reverse=True)
        prev_b = allb[i - 1] if i > 0 else ""
        next_b = allb[i + 1] if i + 1 < len(allb) else ""
        body = front(b, stamp, prev_b, next_b) + "".join(strip_footer(x[2]).rstrip() + "\n\n" for x in merged)
        for rel in (os.path.join(DIR, "changelog-" + b + ".md"),
                    os.path.join("docs", DIR, "changelog-" + b + ".md")):
            write(rel, body)
        print("  wrote changelog-{}.md ({} sections)".format(b, len(merged)))
    log = new_head.rstrip() + "\n\n" + "".join(strip_footer(x[2]).rstrip() + "\n\n" for x in keep)
    log += "## Archive\n\nOlder passes by half-month: " + " | ".join(
        "[{}](/hermes/mcp/servers/external/changelog-{})".format(bucket_range(b), b)
        for b in allb) + "\n"
    for rel in (REL, os.path.join("docs", REL)):
        write(rel, log)
    print("wrote {} ({:.0f} KB) plus docs/ twin".format(REL, len(log) / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
