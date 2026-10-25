#!/usr/bin/env python3
"""Claim-truth gate: block public pages that assert a directory listing we do not have.

Why this exists (Oct 25, 2026): docs/index.md, the highest-traffic page in the
repository, told readers "CorpusIQ is listed in Anthropic's MCP connector
directory for one-click install in Claude". It is not listed. The claim was
verified false three ways - api.anthropic.com/api/directory/servers paged to
1,000 servers returns zero CorpusIQ entries, claude.com/connectors contains no
mention, and docs/changelog.md already printed the opposite. The frontend gates
block this class on corpusiq.io; the docs had no equivalent, so the claim
shipped from the docs side.

The gate is deliberately NARROW. It only fails on affirmative listing claims we
can disprove, and it understands the negated form so honest copy ("not yet
listed in Anthropic's Connector Directory") keeps passing.

Usage:
    python3 scripts/validate_claim_truth.py            # gate the tree
    python3 scripts/validate_claim_truth.py --selftest # prove the matcher bites

Exit codes: 0 = clean, 1 = forbidden claim found (or selftest failure).
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAN_DIRS = ["docs"]
SCAN_FILES = ["llms.txt", "llms-full.txt"]

# Affirmative listing claims. Each pattern must be a phrase that is only
# truthful if the listing actually exists.
FORBIDDEN = [
    # "listed in Anthropic's MCP connector directory" and friends
    re.compile(r"\blisted\s+in\s+(?:the\s+)?anthropic'?s?\b", re.I),
    re.compile(r"\banthropic'?s?\s+(?:mcp\s+)?connector\s+directory\b", re.I),
    # linking the directory as evidence of presence
    re.compile(r"claude\.com/connectors", re.I),
    # install-path claims that only a directory listing would provide
    re.compile(r"one-?click\s+install\s+in\s+claude\b", re.I),
]

# A line carrying one of these negations is honest copy, not a claim.
NEGATIONS = re.compile(
    r"\b(not|isn'?t|aren'?t|never|yet|no longer|neither|missing|absent)\b", re.I
)


def scan_text(text):
    """Return [(lineno, line)] for forbidden affirmative claims."""
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if not any(p.search(line) for p in FORBIDDEN):
            continue
        if NEGATIONS.search(line):
            continue
        hits.append((i, line.strip()[:220]))
    return hits


def iter_targets():
    seen = set()
    for d in SCAN_DIRS:
        root = os.path.join(REPO, d)
        for base, _dirs, files in os.walk(root, followlinks=True):
            for f in files:
                if not f.endswith(".md"):
                    continue
                p = os.path.join(base, f)
                real = os.path.realpath(p)
                if real in seen:
                    continue
                seen.add(real)
                yield p
    for f in SCAN_FILES:
        p = os.path.join(REPO, f)
        if os.path.exists(p):
            yield p


def selftest():
    bad = [
        "CorpusIQ is listed in Anthropic's MCP connector directory for one-click install in Claude.",
        "See [Anthropic's MCP connector directory](https://claude.com/connectors) for the listing.",
        "Setup is one-click install in Claude.",
    ]
    good = [
        "CorpusIQ is not yet listed in Anthropic's Connector Directory, so setup requires pasting the endpoint.",
        "Add the public MCP endpoint through Claude's custom connector flow.",
        "CorpusIQ is live in the ChatGPT app store.",
        "Every connector below is included in the base plan.",
    ]
    ok = True
    for t in bad:
        if not scan_text(t):
            print(f"SELFTEST FAIL (missed): {t}")
            ok = False
    for t in good:
        if scan_text(t):
            print(f"SELFTEST FAIL (false positive): {t}")
            ok = False
    print("SELFTEST OK" if ok else "SELFTEST FAILED")
    return 0 if ok else 1


def main():
    if "--selftest" in sys.argv:
        return selftest()

    checked = 0
    total_hits = 0
    for path in iter_targets():
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        checked += 1
        for lineno, line in scan_text(text):
            total_hits += 1
            rel = os.path.relpath(path, REPO)
            print(f"FORBIDDEN CLAIM {rel}:{lineno}")
            print(f"    {line}")

    print(f"claim-truth gate: {checked} file(s) scanned, {total_hits} forbidden claim(s)")
    if total_hits:
        print("BLOCKED - CorpusIQ is not in Anthropic's Connector Directory.")
        print("Rewrite the sentence to the custom-connector path, or drop the claim.")
        return 1
    print("PASS: no unsupported directory-listing claims")
    return 0


if __name__ == "__main__":
    sys.exit(main())
