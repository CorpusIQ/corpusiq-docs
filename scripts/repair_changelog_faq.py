#!/usr/bin/env python3
"""Repair the auto-generated FAQ block on Hermes changelog pages.

Two defect classes were found in the published pages on 2026-11-10
(monitor cycle T-NOV10-DOCSMON-0300MST):

1. DATE CONTRADICTION. Every page states its own
   `**Release Date:** <Month D, YYYY>` (taken verbatim from the upstream
   GitHub release body), but the AEO FAQ answer to "When was Hermes Agent
   <v> released?" was built from `published_at[:10]` - a UTC calendar date.
   Any release published in the Arizona evening (01:xx UTC the next day)
   therefore answered with a DIFFERENT day than the page itself stated.
   Seven pages disagreed: v0.4.0, v0.20.3, v0.20.5, v0.21.7, v0.22.0,
   v0.22.5, v0.23.1 (v0.20.5 was off by two days). An AI answer engine
   quoting the FAQ block and a reader reading the header got two dates.

2. MID-SENTENCE TRUNCATION. The answer to "What changed in Hermes Agent
   <v>?" was `summary_line()` cut at 210 characters with a literal "...".
   Twenty-two pages ended their answer mid-clause ("Full curated notes
   for..."), which reads as a stub and is a poor citation snippet. The
   full summary is already on the same page as the release blockquote,
   so the repair re-derives a COMPLETE first sentence (or two) from that
   blockquote instead of truncating.

3. DASH ARTIFACT (same pass, cosmetic). `sanitize_dashes()` replaced a
   spaced em dash with " - ", producing double spaces around the hyphen
   ("onward  -  highlights") where the upstream body had "onward - highlights".

The script is idempotent and safe to re-run: it only rewrites an answer
when the current text is wrong, and it never touches fenced code blocks
for the dash normalization. `--check` reports drift and exits 1 instead
of writing, so it can be wired into CI as a gate.

Usage:
    python scripts/repair_changelog_faq.py            # repair in place
    python scripts/repair_changelog_faq.py --check     # report only
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHANGELOG = os.path.join(ROOT, "hermes", "changelog")

RELEASE_DATE_RE = re.compile(r"^\*\*Release Date:\*\*\s*([A-Z][a-z]+ \d{1,2}, \d{4})", re.M)
FAQ_DATE_RE = re.compile(r"(### When was Hermes Agent [^\n]*released\?\s*\n\n)([^\n]+)")
FAQ_CHANGE_RE = re.compile(r"(### What changed in Hermes Agent [^\n]*\?\s*\n\n)(> ?)?([^\n]+)")
SUMMARY_BQ_RE = re.compile(r"^> (.+)$", re.M)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
DASH_ARTIFACT_RE = re.compile(r" {2,}- {2,}")
FENCE_RE = re.compile(r"^```")


def summary_text(page: str) -> str:
    """The release summary blockquote the page already carries."""
    for line in page.split("\n"):
        s = line.strip()
        if s.startswith("> ") and not s.startswith("> **Release Date"):
            return s[2:].strip()
    return ""


def complete_answer(text: str, budget: int = 300) -> str:
    """Trim to whole sentences; never end on an ellipsis.

    Keeps at least one sentence (whole, however long) and adds further
    sentences while they fit inside `budget`.
    """
    text = text.strip()
    if text.endswith("..."):
        text = text[:-3].rstrip()
    sentences = [s.strip() for s in SENTENCE_SPLIT_RE.split(text) if s.strip()]
    if not sentences:
        return text
    out = sentences[0]
    for s in sentences[1:]:
        if len(out) + 1 + len(s) > budget:
            break
        out = out + " " + s
    if not out.endswith((".", "!", "?")):
        out = out.rstrip(" ,;:") + "."
    return out


def normalize_dashes(text: str) -> str:
    """Collapse the '  -  ' double-space dash artifact outside fenced code."""
    out_lines, in_fence = [], False
    for line in text.split("\n"):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        out_lines.append(line if in_fence else DASH_ARTIFACT_RE.sub(" - ", line))
    return "\n".join(out_lines)


def release_dates() -> dict[str, str]:
    """version -> the date the page itself states (upstream release body)."""
    dates = {}
    for path in sorted(glob.glob(os.path.join(CHANGELOG, "v*", "index.md"))):
        version = os.path.basename(os.path.dirname(path))
        with open(path, encoding="utf-8") as fh:
            m = RELEASE_DATE_RE.search(fh.read())
        if m:
            dates[version] = m.group(1)
    return dates


INDEX_ROW_RE = re.compile(
    r"^\| \[(v[^\]]+)\]\(/hermes/changelog/\1\) \| ([A-Z][a-z]+ \d{1,2}, \d{4}) \| ([^|]+) \| (.+?) \|$",
    re.M,
)
INDEX_FAQ_RE = re.compile(r"(v\d+\.\d+\.\d+, published )([A-Z][a-z]+ \d{1,2}, \d{4})")
FRONT_DOOR_RE = re.compile(
    r"(\*\*Current release:\*\* Hermes Agent (v[\d.]+) \(released )([A-Z][a-z]+ \d{1,2}, \d{4})(\))"
)


def repair_index(dates: dict[str, str]) -> list[str]:
    """Align the changelog index table, its FAQ answer and the JSON-LD copy."""
    path = os.path.join(CHANGELOG, "index.md")
    with open(path, encoding="utf-8") as fh:
        txt = fh.read()
    original = txt
    changes: list[str] = []

    def _row(m: re.Match) -> str:
        version, stated, kind, summary = m.group(1), m.group(2), m.group(3), m.group(4)
        want = dates.get(version, stated)
        if summary.lstrip().startswith("> "):
            summary = summary.lstrip()[2:].lstrip()  # blockquote marker leaked into a table cell
            changes.append("%s summary cell de-quoted" % version)
        if want != stated:
            changes.append("%s row date %r -> %r" % (version, stated, want))
        return "| [%s](/hermes/changelog/%s) | %s | %s | %s |" % (version, version, want, kind.strip(), summary)

    txt = INDEX_ROW_RE.sub(_row, txt)

    # The index FAQ answers "which release is current and when" - each answer
    # is aligned to ITS OWN page's stated date, not the UTC day of the publish call.

    def _faq(m: re.Match) -> str:
        version, stated = m.group(1).split(",")[0], m.group(2)
        want = dates.get(version, stated)
        if want != stated:
            changes.append("index FAQ date %r -> %r" % (stated, want))
        return m.group(1) + want

    txt = INDEX_FAQ_RE.sub(_faq, txt)

    dedashed = normalize_dashes(txt)
    if dedashed != txt:
        changes.append("dash artifact x%d" % len(DASH_ARTIFACT_RE.findall(txt)))
        txt = dedashed

    if txt != original:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(txt)
    return changes


def repair_front_door(dates: dict[str, str]) -> list[str]:
    """Hub 'Current release' line states the release date - keep it true."""
    changes: list[str] = []
    for rel_path in ("hermes/index.md", "hermes/ecosystem/index.md"):
        path = os.path.join(ROOT, rel_path)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            txt = fh.read()
        original = txt

        def _fix(m: re.Match) -> str:
            version, stated = m.group(2), m.group(3)
            want = dates.get(version, stated)
            if want != stated:
                changes.append("%s current-release date %r -> %r" % (rel_path, stated, want))
            return m.group(1) + want + m.group(4)

        txt = FRONT_DOOR_RE.sub(_fix, txt)
        if txt != original:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(txt)
    return changes


def repair_page(path: str) -> list[str]:
    """Return a list of human-readable changes applied (empty when clean)."""
    with open(path, encoding="utf-8") as fh:
        page = fh.read()
    original = page
    changes: list[str] = []

    m_rel = RELEASE_DATE_RE.search(page)
    release_date = m_rel.group(1) if m_rel else ""

    if release_date:
        m_faq = FAQ_DATE_RE.search(page)
        if m_faq and m_faq.group(2).strip() != release_date:
            changes.append(
                "date %r -> %r" % (m_faq.group(2).strip(), release_date)
            )
            page = FAQ_DATE_RE.sub(lambda m: m.group(1) + release_date, page, count=1)

    m_change = FAQ_CHANGE_RE.search(page)
    if m_change:
        prefix, quote_mark, answer = m_change.group(1), m_change.group(2) or "", m_change.group(3)
        source = summary_text(page) or answer
        if answer.rstrip().endswith("...") or len(answer) > 260:
            fixed = complete_answer(source)
            if fixed and fixed.rstrip() != answer.rstrip():
                changes.append("answer de-truncated (%d -> %d chars)" % (len(answer), len(fixed)))
                page = page[: m_change.start(3)] + fixed + page[m_change.end(3):]

    dedashed = normalize_dashes(page)
    if dedashed != page:
        n = len(DASH_ARTIFACT_RE.findall(page))
        changes.append("dash artifact x%d" % n)
        page = dedashed

    if page != original:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(page)
    return changes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report drift, write nothing")
    args = ap.parse_args()

    paths = sorted(glob.glob(os.path.join(CHANGELOG, "v*", "index.md")))
    if not paths:
        print("ERROR: no changelog pages found under %s" % CHANGELOG)
        return 2

    dirty = 0
    for path in paths:
        rel = os.path.relpath(path, ROOT)
        if args.check:
            with open(path, encoding="utf-8") as fh:
                page = fh.read()
            problems = []
            m_rel = RELEASE_DATE_RE.search(page)
            m_faq = FAQ_DATE_RE.search(page)
            if m_rel and m_faq and m_faq.group(2).strip() != m_rel.group(1):
                problems.append("FAQ date %r != Release Date %r" % (m_faq.group(2).strip(), m_rel.group(1)))
            m_change = FAQ_CHANGE_RE.search(page)
            if m_change and m_change.group(3).rstrip().endswith("..."):
                problems.append("'What changed' answer truncated with '...'")
            if DASH_ARTIFACT_RE.search(page):
                problems.append("dash artifact x%d" % len(DASH_ARTIFACT_RE.findall(page)))
            if problems:
                dirty += 1
                print("DRIFT %s: %s" % (rel, "; ".join(problems)))
        else:
            changes = repair_page(path)
            if changes:
                dirty += 1
                print("FIXED %s: %s" % (rel, "; ".join(changes)))

    # Index + front door carry the same release date, so they drift with it.
    dates = release_dates()
    if args.check:
        index_txt = open(os.path.join(CHANGELOG, "index.md"), encoding="utf-8").read()
        index_problems = []
        for m in INDEX_ROW_RE.finditer(index_txt):
            version, stated = m.group(1), m.group(2)
            if version in dates and dates[version] != stated:
                index_problems.append("%s row %r != %r" % (version, stated, dates[version]))
            if m.group(4).lstrip().startswith("> "):
                index_problems.append("%s summary cell carries a leaked blockquote marker" % version)
        if DASH_ARTIFACT_RE.search(index_txt):
            index_problems.append("dash artifact x%d" % len(DASH_ARTIFACT_RE.findall(index_txt)))
        for m in INDEX_FAQ_RE.finditer(index_txt):
            version, stated = m.group(1).split(",")[0], m.group(2)
            if version in dates and dates[version] != stated:
                index_problems.append("FAQ %s %r != %r" % (version, stated, dates[version]))
        if index_problems:
            dirty += 1
            print("DRIFT hermes/changelog/index.md: %s" % "; ".join(index_problems))
        for rel_path in ("hermes/index.md", "hermes/ecosystem/index.md"):
            p = os.path.join(ROOT, rel_path)
            if not os.path.exists(p):
                continue
            for m in FRONT_DOOR_RE.finditer(open(p, encoding="utf-8").read()):
                version, stated = m.group(2), m.group(3)
                if version in dates and dates[version] != stated:
                    dirty += 1
                    print("DRIFT %s: current-release %r != %r" % (rel_path, stated, dates[version]))
    else:
        for label, fn in (("hermes/changelog/index.md", lambda: repair_index(dates)),
                          ("hub/ecosystem", lambda: repair_front_door(dates))):
            changes = fn()
            if changes:
                dirty += 1
                print("FIXED %s: %s" % (label, "; ".join(changes)))

    verb = "surfaces with drift" if args.check else "surfaces repaired"
    print("%d/%d %s" % (dirty, len(paths) + 3, verb))
    if args.check and dirty:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
