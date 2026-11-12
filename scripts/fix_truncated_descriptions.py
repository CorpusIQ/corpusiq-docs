#!/usr/bin/env python3
"""fix_truncated_descriptions.py - repair frontmatter descriptions cut mid-sentence.

Why this exists
---------------
A bulk writer (2026-11-01) and the hermes freshness lane (2026-11-12) shortened
`description:` values in place by deleting the tail. The result ships as the
`<meta name="description">` / `og:description` of a live page, ending on a
fragment: "... Deterministic at the host", "Sourced from SEC proxy filings, not",
"faithful design-to-code, not".

Detection (see validate_page_metadata.py for the failing gate)
--------------------------------------------------------------
A description with no terminal punctuation is broken when either
  * its trailing 40/30/22 characters appear in the page body followed by more
    words that run to a sentence end (the description is a cut quote), or
  * its last word can never end a sentence ("not", "these", "and", ...).

Repair (grounded, additive only)
--------------------------------
The full sentence already exists in the page body: the writer derived the
description from page copy and deleted part of it. This script finds the body
sentence that ENDS with the truncated description, and replaces the description
with that sentence - trimmed at a clean boundary (last complete sentence, then
word boundary with trailing connectives popped) when the sentence exceeds 160
characters. It refuses any repair that would not be an extension of the current
description, so no text is invented.

Usage
-----
    /usr/bin/python3 scripts/fix_truncated_descriptions.py            # dry run
    /usr/bin/python3 scripts/fix_truncated_descriptions.py --apply
    /usr/bin/python3 scripts/fix_truncated_descriptions.py --apply --paths hermes/mcp/runbook-v1.md
"""
from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import validate_page_metadata as vpm  # noqa: E402

TERM = re.compile(r'[.!?"\')\]]\s*$')
SENT_SPLIT = re.compile(r'(?<=[.!?])\s+')

# Words that can never close a sentence. 'not' is deliberately included here
# (not in vpm.DANGLING) because the gate must stay safe for titles that end
# "...are not." while a description ending bare "not" is always a cut.
CUT_WORDS = {
    'not', 'these', 'both', 'either', 'nor', 'and', 'or', 'the', 'of', 'to',
    'for', 'with', 'a', 'an', 'at', 'in', 'on', 'by', 'from', 'as', 'that',
    'which', 'is', 'are', 'was', 'were', 'be', 'been', 'vs', 'via', 'plus',
    'between', 'across', 'through', 'into', 'than', 'including', 'such',
}

MIN_KEEP = 90
MAX_DESC = 160
DANGLING = {'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'from', 'in',
            'into', 'is', 'it', 'its', 'of', 'on', 'or', 'the', 'to', 'via',
            'vs', 'with', 'your', 'that', 'this', 'these', 'those', 'not'}


def plain(text: str) -> str:
    """Body text as one normalized, comparable string (markdown stripped)."""
    m = re.match(r'^---\n.*?\n---\n(.*)$', text, re.S)
    body = m.group(1) if m else text
    body = re.sub(r'[*_`#>\[\]()]', ' ', body)
    return re.sub(r'\s+', ' ', body).strip()


def norm(s: str) -> str:
    return re.sub(r'\s+', ' ', s).strip().lower()


def trim(desc: str) -> str:
    """Cut an over-length description at a clean boundary."""
    head = desc[:MAX_DESC]
    ends = [m.end() for m in re.finditer(r'[.!?](?=\s|$)', head)]
    if ends and ends[-1] >= MIN_KEEP:
        return desc[:ends[-1]].strip()
    cut = desc[:MAX_DESC].rsplit(' ', 1)[0].strip().rstrip(' ,;:.-')
    words = cut.split(' ')
    while words and words[-1].lower().strip('.,;:') in DANGLING:
        words.pop()
    return ' '.join(words).rstrip(' ,;:.-')


def find_full_sentence(desc: str, body_plain: str) -> str | None:
    """Body sentence that ends with `desc`, or None when no clean match."""
    dn = norm(desc)
    for n in (40, 30, 22):
        if len(dn) < n:
            continue
        tail = dn[-n:]
        i = body_plain.lower().find(tail)
        if i < 0:
            continue
        after = body_plain[i + len(tail):]
        if not re.match(r'\s+[A-Za-z0-9]', after):
            continue
        # End of the sentence that contains the tail.
        m = re.search(r'[.!?](?=\s|$)', after)
        if not m:
            continue
        # Sentence start: the previous terminator before the tail, else body start.
        prev = None
        for pm in re.finditer(r'[.!?](?=\s)', body_plain[:i]):
            prev = pm.end()
        start = prev or 0
        sentence = body_plain[start:i + len(tail) + m.end()].strip()
        if not norm(sentence).endswith(dn):
            continue  # the tail did not sit at the sentence end
        if not norm(sentence).startswith(dn[:min(len(dn), 22)]):
            # Description drifted from the sentence (rewritten copy); take the
            # longest common run instead of guessing.
            return None
        return sentence
    return None


def repair(path: str) -> tuple[str, str] | None:
    text = open(path, encoding='utf-8', errors='replace').read()
    fm = vpm.frontmatter(text)
    if not fm:
        return None
    desc = vpm.value(fm, 'description')
    if not desc or len(desc) > MAX_DESC or TERM.search(desc.strip()):
        return None

    body = plain(text)
    new = find_full_sentence(desc, body)
    if new is None:
        # Fall back to appending the cut word's sentence remainder: the body
        # fragment that begins exactly where the description stops.
        dn = norm(desc)
        for n in (40, 30, 22):
            if len(dn) < n:
                continue
            i = body.lower().find(dn[-n:])
            if i >= 0:
                rest = body[i + n:]
                m = re.match(r'\s+([A-Za-z0-9][^.!?]{0,120})[.!?]', rest)
                if m:
                    candidate = desc + m.group(0)
                    if len(candidate) > MAX_DESC:
                        candidate = trim(candidate)
                        if not candidate.endswith(('.', '!', '?', '"', ')')):
                            candidate = candidate.rstrip(' ,;:') + '.'
                    return candidate, 'append'
        return None

    candidate = new if len(new) <= MAX_DESC else trim(new)
    if not candidate.endswith(('.', '!', '?', '"', ')')):
        candidate = candidate.rstrip(' ,;:') + '.'
    if norm(candidate) == norm(desc):
        return None
    if not norm(candidate).startswith(norm(desc)[:40]):
        return None
    return candidate, 'sentence'


def main(argv: list[str]) -> int:
    apply = '--apply' in argv
    paths = None
    if '--paths' in argv:
        i = argv.index('--paths')
        paths = [a for a in argv[i + 1:] if not a.startswith('-')]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    targets = []
    if paths:
        for p in paths:
            targets.append(p if os.path.isabs(p) else os.path.join(root, p))
    else:
        targets = list(vpm.pages(root))

    changed = 0
    skipped_block = 0
    for p in targets:
        if not os.path.exists(p):
            print('MISSING %s' % p)
            continue
        try:
            raw = open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        # Block-scalar descriptions (`description: >-` / `description: |`) span
        # indented continuation lines. Rewriting only the key line orphaned that
        # text and produced invalid YAML (`description: ">"`), which silently
        # dropped the meta description and blocked the docs deploy behind the
        # frontmatter gate. Those pages are complete sentences already: leave
        # them alone.
        if re.search(r'(?m)^description:\s*[>|]', raw):
            skipped_block += 1
            print('SKIP block-scalar %s' % os.path.relpath(p, root))
            continue
        try:
            res = repair(p)
        except OSError:
            continue
        if not res:
            continue
        new, how = res
        rel = os.path.relpath(p, root)
        text = open(p, encoding='utf-8', errors='replace').read()
        old_line = re.search(r'(?m)^description:.*$', text).group(0)
        new_line = 'description: "%s"' % new.replace('"', "'")
        print('%s [%s]\n  - %s\n  + %s' % (rel, how, old_line, new_line))
        if apply:
            text = re.sub(r'(?m)^description:.*$', lambda _m: new_line, text, count=1)
            open(p, 'w', encoding='utf-8').write(text)
        changed += 1

    print('%s: %d description(s) %s' % ('APPLIED' if apply else 'DRY RUN',
                                        changed,
                                        'repaired' if apply else 'repairable'))
    if skipped_block:
        print('skipped %d block-scalar description(s) (folded/literal YAML)' % skipped_block)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
