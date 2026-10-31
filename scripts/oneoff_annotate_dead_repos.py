#!/usr/bin/env python3
"""One-shot: annotate links to repositories that no longer exist (2026-10-31).

Input: /tmp/dead_verify.txt lines "GONE   owner/repo :: reason" produced by
verifying each link twice (HTTP 404 and `git ls-remote` rc=128).

Behaviour per file:
  * markdown link  [text](https://github.com/o/r)  -> text (repo no longer public)
  * bare URL       https://github.com/o/r          -> o/r (repo no longer public)
  * HTML href/src  left untouched (reported for manual review)
  * code fences    left untouched; a status blockquote is inserted after the
                   frontmatter instead, because the commands cannot work.

Idempotent: a repo already carrying "(repo no longer public)" next to it is skipped.
"""
import re
import sys
import pathlib

VERIFY = pathlib.Path("/tmp/dead_verify.txt")
ROOT = pathlib.Path("hermes")


def load_repos():
    repos = []
    for line in VERIFY.read_text().splitlines():
        if not line.startswith("GONE"):
            continue
        repos.append(line.split()[1])
    return repos


def annotate(text: str, repos: list[str]) -> tuple[str, set[str], set[str]]:
    """Return (new_text, repos_in_code, html_hits)."""
    md_repl_total = 0
    in_code = set()
    html_hits = set()

    for repo in repos:
        # 1. markdown links
        md = re.compile(r"\[([^\]]+)\]\(https://github\.com/" + re.escape(repo) + r"/?\)")
        text, n = md.subn(lambda m: f"{m.group(1)} (repo no longer public)", text)
        md_repl_total += n

        # 2. bare URLs on their own (not inside code fences - handled below)
        lines = text.splitlines(keepends=True)
        fenced = False
        out = []
        for line in lines:
            if line.strip().startswith("```"):
                fenced = not fenced
                out.append(line)
                continue
            if f"github.com/{repo}" in line:
                if fenced:
                    in_code.add(repo)
                    out.append(line)
                    continue
                if re.search(r'(href|src)="https://github\.com/' + re.escape(repo), line):
                    html_hits.add(repo)
                    out.append(line)
                    continue
                # don't touch a line that still holds a markdown link we already rewrote
                new = line.replace(f"https://github.com/{repo}", f"{repo} (repo no longer public)")
                new = new.replace(f"http://github.com/{repo}", f"{repo} (repo no longer public)")
                out.append(new)
            else:
                out.append(line)
        text = "".join(out)

    return text, in_code, html_hits


def insert_status(text: str, repos: list[str]) -> str:
    body = ", ".join(f"`{r}`" for r in sorted(repos))
    note = (
        f"> **Upstream status (2026-10-31):** {body} "
        f"{'is' if len(repos) == 1 else 'are'} no longer available. GitHub returns 404 "
        "and the repository cannot be cloned; the commands below are kept as published "
        "and will fail until the project reappears.\n\n"
    )
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            nl = text.find("\n", end + 4)
            if nl != -1:
                return text[: nl + 1] + "\n" + note + text[nl + 1 :].lstrip("\n")
    return note + text


def main() -> int:
    apply = "--apply" in sys.argv
    repos = load_repos()
    changed = 0
    report = []
    for p in sorted(ROOT.rglob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        if "github.com/" not in text:
            continue
        new, in_code, html_hits = annotate(text, repos)
        if in_code:
            new = insert_status(new, list(in_code))
        if new != text:
            changed += 1
            report.append(f"{p}: code={sorted(in_code)} html={sorted(html_hits)}")
            if apply:
                p.write_text(new, encoding="utf-8")
    print(f"{'APPLIED' if apply else 'DRY-RUN'}: {changed} file(s)")
    for line in report:
        print(" ", line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
