#!/usr/bin/env python3
"""cap_meta_descriptions.py - keep every meta description inside the 160-char SERP limit.

WHY (2026-11-19, DEF-2026-11-19-05): roughly a tenth of the published pages carried a
frontmatter `description` over 160 characters, so search engines truncate the snippet
wherever they like. The source is per-page frontmatter, not a template, so the fix is a
bulk pass plus a gate that keeps new pages honest.

Rules it enforces (identical to scripts/validate_page_metadata.py, which owns them):
  * the measured value is the DECODED string - HTML entities count as one character,
    the way a search engine reads them. Measuring the raw attribute is what produced
    the false "over 160" defects on pages whose only sin was an apostrophe.
  * a shortened description must read as a finished sentence: it ends in . ! or ?,
    and never on a dangling connective ('with', 'and', 'your', 'a' ...), otherwise
    the page-metadata gate reads it as cut prose.

Usage:
    python3 scripts/cap_meta_descriptions.py            # report only
    python3 scripts/cap_meta_descriptions.py --apply
    python3 scripts/cap_meta_descriptions.py --check    # CI gate: exit 1 if any page is over
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from html import unescape

LIMIT = 160
TARGET = 158
SKIP_DIRS = {".git", "node_modules", "site", ".vercel", "cache", "__pycache__"}
LINE_RE = re.compile(r"^(description:[ \t]*)(.*)$", re.M)
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)

# Words that can never end a sentence (mirror of validate_page_metadata.DANGLING + CUT_WORDS).
DANGLING = {
    "a", "an", "and", "as", "at", "but", "by", "for", "from", "in", "into",
    "is", "it", "its", "of", "on", "or", "the", "to", "via", "vs", "with",
    "your", "that", "this", "those", "without", "plus", "across", "over",
    "between", "through", "within", "under", "above", "below", "behind",
    "against", "among", "around", "before", "after", "during", "until", "per",
    "than", "whether", "nor", "because", "although", "unless", "toward",
    "towards", "onto", "upon", "near", "beyond", "despite", "except", "inside",
    "outside", "throughout", "alongside", "regarding", "including", "any",
    "these", "both", "either", "not", "was", "were", "be", "been", "which",
    "are", "such",
}


def unquote(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v.strip()



FUNC_TAIL = ("for", "of", "to", "in", "with", "at", "by", "within", "across",
             "over", "up", "from", "and", "or", "on", "as", "than")


def dangles(s: str) -> bool:
    """Mirror of validate_page_metadata.dangling() for a description."""
    toks = [t for t in re.split(r"\s+", s.strip()) if t]
    if not toks:
        return True
    last = toks[-1].strip('.,:;').lower()
    if last in DANGLING:
        return True
    if len(toks) >= 2 and re.fullmatch(r"\d+", last) and toks[-2].lower().strip('.,:;') in FUNC_TAIL:
        return True
    return False


def finish(s: str) -> str:
    """Shorten what is still dangling, then guarantee a terminal full stop."""
    toks = s.split()
    guard = 0
    while toks and dangles(" ".join(toks)) and guard < 6:
        toks.pop()
        guard += 1
    out = " ".join(toks).rstrip(" ,;:-")
    if not out:
        return s
    return out if out[-1] in ".!?" else out + "."


def trim(s: str) -> str:
    """Fit s in the SERP limit as a finished sentence."""
    s = " ".join(s.split())
    if len(s) <= LIMIT:
        return finish(s) if dangles(s) else s
    window = s[:TARGET]
    # 1. the last whole sentence that still fits and is worth keeping
    best = -1
    for i, ch in enumerate(window):
        if ch in ".!?" and i + 1 < len(window) and window[i + 1] == " " and i + 1 >= 90:
            best = i + 1
    if best > 0:
        return finish(window[:best].strip())
    # 2. word boundary, drop trailing dangling words, finish the sentence
    cut = window
    if " " in cut:
        cut = cut[:cut.rfind(" ")]
    cut = cut.rstrip(" ,;:-")
    words = cut.split()
    while words and words[-1].lower().strip(",;:-") in DANGLING:
        words.pop()
    cut = " ".join(words).rstrip(" ,;:-")
    if cut.endswith("-"):
        cut = cut[:-1].rstrip(" ,;:-")
    return finish(cut)


def measure(path: str):
    """Return (text, start, end, prefix, value) for the frontmatter description line, or None."""
    try:
        text = open(path, encoding="utf-8").read()
    except Exception:
        return None
    fm = FM_RE.match(text)
    if not fm:
        return None
    m = LINE_RE.search(fm.group(1))
    if not m:
        return None
    value = unescape(unquote(m.group(2)))
    return text, fm.start(1) + m.start(), fm.start(1) + m.end(), m.group(1), value


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--root", default=".")
    a = ap.parse_args()

    over, fixed, failed, seen = [], 0, [], set()
    for dirpath, dirnames, names in os.walk(a.root, followlinks=True):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for n in names:
            if not n.endswith(".md"):
                continue
            p = os.path.join(dirpath, n)
            real = os.path.realpath(p)
            if real in seen:
                continue
            seen.add(real)
            got = measure(p)
            if not got:
                continue
            text, s, e, prefix, value = got
            needs_fix = len(value) > LIMIT or (
                value[-1] in ".!?" and len(value) > 100 and dangles(value))
            if not needs_fix:
                continue
            over.append((p, len(value)))
            if a.check or not a.apply:
                continue
            new = trim(value)
            if len(new) > LIMIT or new[-1] not in ".!?":
                failed.append((p, len(new), new[-40:]))
                continue
            line = '%s"%s"' % (prefix, new.replace('"', "'"))
            text = text[:s] + line + text[e:]
            open(p, "w", encoding="utf-8").write(text)
            again = measure(p)
            if again and len(again[4]) > LIMIT:
                failed.append((p, len(again[4]), "still over after write"))
            else:
                fixed += 1

    if a.check:
        if over:
            print("FAIL: %d page(s) carry a meta description over %d characters, e.g.:" % (len(over), LIMIT))
            for p, n in over[:10]:
                print("  %s (%d)" % (p, n))
            print("Fix: python3 scripts/cap_meta_descriptions.py --apply")
            return 1
        print("OK: every meta description is within %d characters" % LIMIT)
        return 0

    print("%d page(s) over %d characters" % (len(over), LIMIT))
    if a.apply:
        print("rewrote %d description(s)" % fixed)
        for p, n, why in failed[:10]:
            print("  UNRESOLVED %s (%s) %s" % (p, n, why))
        if failed:
            return 1
    else:
        for p, n in over[:10]:
            print("  %s (%d)" % (p, n))
        print("dry run - pass --apply to write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
