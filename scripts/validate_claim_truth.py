#!/usr/bin/env python3
"""Claim-truth gate: block public pages that assert something we cannot show.

Two classes are covered.

1. Directory-listing claims (Oct 25, 2026): docs/index.md, the highest-traffic
   page in the repository, told readers "CorpusIQ is listed in Anthropic's MCP
   connector directory for one-click install in Claude". It is not listed. The
   claim was verified false three ways - api.anthropic.com/api/directory/servers
   paged to 1,000 servers returns zero CorpusIQ entries, claude.com/connectors
   contains no mention, and docs/changelog.md already printed the opposite.

2. Platform-support claims (Oct 27, 2026): hermes/compare/corpusiq-vs-microsoft-copilot
   said CorpusIQ "reads Microsoft Copilot" and that readers should "connect
   Microsoft Copilot once". Microsoft Copilot has no MCP connector, so there is
   nothing to connect to, and the corpusiq.io FAQ already says the opposite.
   The page argued one thing and the site another, on the same domain.

The frontend gates block this class on corpusiq.io; the docs had no equivalent,
so both claims shipped from the docs side. The gate scans every Markdown page in
the tree (not just docs/) because the second miss lived under hermes/.

The gate is deliberately NARROW. It only fails on affirmative claims we can
disprove, and it understands the negated form so honest copy ("not yet listed in
Anthropic's Connector Directory", "does not plug into Microsoft Copilot") keeps
passing.

Usage:
    python3 scripts/validate_claim_truth.py            # gate the tree
    python3 scripts/validate_claim_truth.py --selftest # prove the matcher bites

Exit codes: 0 = clean, 1 = forbidden claim found (or selftest failure).
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Top-level folders that are code, build output, or fixtures rather than
# reader-facing pages. Anything else at the root is walked, so a new content
# folder is covered without editing this list.
SKIP_DIRS = {
    ".git", ".github", ".claude-plugin", ".next", ".vercel", "__pycache__",
    "node_modules", "scripts", "site", "assets", "javascripts",
}
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
    # Platform-support claims: Microsoft Copilot has no MCP connector, so
    # CorpusIQ cannot read it, connect to it, or plug into it.
    re.compile(
        r"\b(?:corpusiq\s+)?(?:connects?|reads?|integrates?\s+with|plugs?\s+into)"
        r"\s+(?:to\s+|from\s+)?(?:microsoft\s+|ms\s+)?copilot\b",
        re.I,
    ),
    re.compile(r"\bconnect\s+(?:microsoft\s+)?copilot\s+once\b", re.I),
    re.compile(
        r"\bcopilot\b[^.]{0,40}\b(?:uses?|connects?\s+to|reads?)\s+(?:corpusiq|our)\b",
        re.I,
    ),
    # "... Copilot ... CorpusIQ reads from it ..." in either order on one line
    re.compile(r"\bcopilot\b.*\breads?\s+from\s+it\b", re.I),
    re.compile(r"\breads?\s+from\s+it\b.*\bcopilot\b", re.I),
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
    for base, dirs, files in os.walk(REPO, followlinks=False):
        if base == REPO:
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
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
        # Copilot: the Oct 27 regression, verbatim from the shipped page.
        "| Data access | Its own data | Reads Microsoft Copilot AND 40+ other tools in one prompt |",
        "CorpusIQ connects Microsoft Copilot to those systems and exposes all of them to ChatGPT, Claude, and Perplexity.",
        "Yes. Connect Microsoft Copilot once, then ask ChatGPT business questions with live, cited answers.",
        "No. Microsoft Copilot stays your system of record for its job. CorpusIQ reads from it with read-only OAuth.",
    ]
    good = [
        "CorpusIQ is not yet listed in Anthropic's Connector Directory, so setup requires pasting the endpoint.",
        "Add the public MCP endpoint through Claude's custom connector flow.",
        "CorpusIQ is live in the ChatGPT app store.",
        "Every connector below is included in the base plan.",
        # Honest Copilot copy must keep passing.
        "No. It does not plug into Microsoft Copilot, which has no MCP connector.",
        "The two do different jobs, and CorpusIQ does not connect to Copilot: Copilot has no MCP connector.",
        "For the Microsoft piece, CorpusIQ works inside Microsoft Teams, where you add your own AI key.",
        "Supported agents: **Hermes**, Claude Code, GitHub Copilot CLI, Cursor, Gemini CLI.",
        "npx skills add github/awesome-copilot@gh-cli",
        "| AI surface | Power BI Copilot inside the report builder | Any AI you already use, via MCP |",
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
        print("BLOCKED - the text above asserts a listing or a platform connection we cannot show.")
        print("CorpusIQ is not in Anthropic's Connector Directory, and Microsoft Copilot has no MCP")
        print("connector. Rewrite to the supported path, or drop the claim.")
        return 1
    print("PASS: no unsupported listing or platform-support claims")
    return 0


if __name__ == "__main__":
    sys.exit(main())
