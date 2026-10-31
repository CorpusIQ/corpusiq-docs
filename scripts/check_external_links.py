#!/usr/bin/env python3
"""Probe external links in published docs for dead (404/410) targets.

Motivation (2026-10-31): the docs tree shipped a link to
https://github.com/memcore-cloud for months. That account does not exist
(404), and nothing in the pipeline ever touched external URLs, so the dead
link survived every validate_* gate. This script closes that class: it walks
the published Markdown, dedupes external URLs, probes them, and reports the
ones that are definitively gone.

Usage:
  python3 scripts/check_external_links.py                  # hermes/ tree, report only
  python3 scripts/check_external_links.py --paths hermes/README.md hermes/setup
  python3 scripts/check_external_links.py --github-only    # only github.com/... links
  python3 scripts/check_external_links.py --strict         # exit 1 if any DEAD

Classification:
  OK       2xx/3xx
  DEAD     404/410 (a real, actionable defect)
  BLOCKED  401/403/429/451/999 (auth-walled or bot-walled: not proof of death)
  ERROR    timeout / DNS / TLS (retry later, not proof of death)

Only DEAD fails --strict. BLOCKED and ERROR are reported but never block, so
third-party bot walls (Cloudflare, LinkedIn, X) cannot wedge a deploy.
Results are cached (.link-check-cache.json in the repo root) so repeated runs
stay cheap; pass --refresh to re-probe everything.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CACHE_PATH = REPO / ".link-check-cache.json"
CACHE_TTL = 7 * 24 * 3600
# BLOCKED/ERROR mean "we could not tell". Cache them briefly so a rate-limit
# window is not frozen in for a week and later mistaken for a clean result.
CACHE_TTL_INCONCLUSIVE = 30 * 60

URL_RE = re.compile(r"https?://[^\s)\"'<>\]]+")
TRAILING = ".,;:!?`*|"

# Hosts that either block automated clients outright or require auth; probing
# them produces noise, not signal.
SKIP_HOSTS = {
    "x.com", "twitter.com", "linkedin.com", "www.linkedin.com", "reddit.com",
    "www.reddit.com", "medium.com", "facebook.com", "instagram.com",
    "news.ycombinator.com", "discord.gg", "discord.com", "t.me",
    "open.spotify.com", "apps.apple.com", "chromewebstore.google.com",
    "mcp.honcho.dev",  # MCP endpoint: 401 by design
}
UA = "CorpusIQ-Docs-LinkCheck/1.0 (+https://docs.corpusiq.io)"


def normalise(url: str) -> str:
    url = url.rstrip(TRAILING)
    # Drop pure anchors / mailto leftovers already excluded by URL_RE.
    return url


def iter_urls(paths: list[Path], github_only: bool):
    """Map url -> {"file": ..., "fenced": every occurrence sits in a code block}."""
    seen: dict[str, dict] = {}
    for p in paths:
        files = [p] if p.is_file() else sorted(p.rglob("*.md"))
        for f in files:
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            fenced = False
            for line in text.splitlines():
                if line.strip().startswith("```"):
                    fenced = not fenced
                    continue
                for raw in URL_RE.findall(line):
                    u = normalise(raw)
                    # Template placeholders (${REPO}, {{repo}}) are shell/Jinja, not links.
                    if "${" in u or "{{" in u:
                        continue
                    host = u.split("/", 3)[2].lower() if u.count("/") >= 2 else ""
                    if github_only and host not in ("github.com", "www.github.com"):
                        continue
                    if host in SKIP_HOSTS:
                        continue
                    entry = seen.get(u)
                    if entry is None:
                        seen[u] = {"file": str(f.relative_to(REPO)), "fenced": fenced}
                    elif not fenced:
                        # one prose occurrence is enough to make it clickable
                        entry["fenced"] = False
    return seen


def probe(url: str) -> tuple[str, int | str]:
    req = urllib.request.Request(url, method="GET", headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    })
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
            return "OK", r.status
    except urllib.error.HTTPError as e:
        code = e.code
        if code in (404, 410):
            # A GitHub subpath 404 is not proof the repo is gone: CLI shorthands
            # like `hermes skills install https://github.com/o/r/SKILL.md` and
            # bare directory paths (`/o/r/subdir` instead of `/o/r/tree/main/subdir`)
            # 404 in a browser while working in the tool. Check the repo root
            # before calling it dead.
            root = github_repo_root(url)
            if root and root != url:
                verdict, detail = probe(root)
                if verdict == "OK":
                    return "PATH", f"{code} at path, repo root {detail}"
                if verdict == "DEAD":
                    return "DEAD", f"repo root {detail}"
                return verdict, detail
            return "DEAD", code
        if code in (401, 403, 429, 451, 999):
            return "BLOCKED", code
        if 300 <= code < 400:
            return "OK", code
        return "ERROR", code
    except (urllib.error.URLError, TimeoutError, ssl.SSLError, OSError) as e:
        return "ERROR", str(e)[:80]


ROUTE_SEGMENTS = {
    "blob", "tree", "releases", "issues", "pull", "pulls", "compare", "actions",
    "wiki", "discussions", "stargazers", "forks", "tags", "branches", "raw",
    "commits", "graphs", "network", "security", "sponsors", "projects", "settings",
}


def github_repo_root(url: str) -> str | None:
    """Return https://github.com/owner/repo for a github URL, else None."""
    parts = url.split("/")
    if len(parts) < 5:
        return None
    if parts[2].lower() not in ("github.com", "www.github.com"):
        return None
    owner, repo = parts[3], parts[4].replace(".git", "")
    if not owner or not repo or "${" in owner or "${" in repo:
        return None
    if owner in ROUTE_SEGMENTS:
        return None
    return f"https://github.com/{owner}/{repo}"


def has_github_subpath(url: str) -> bool:
    parts = url.split("/")
    if len(parts) <= 5:
        return False
    return parts[5] not in ROUTE_SEGMENTS


def load_cache(refresh: bool) -> dict:
    if refresh or not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text())
    except (OSError, json.JSONDecodeError):
        return {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paths", nargs="*", default=None)
    ap.add_argument("--github-only", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args()

    paths = [Path(x) if Path(x).is_absolute() else REPO / x for x in
             (args.paths or ["hermes"])]
    paths = [p for p in paths if p.exists()]
    if not paths:
        print("no input paths", file=sys.stderr)
        return 2

    urls = iter_urls(paths, args.github_only)
    if args.limit:
        urls = dict(list(urls.items())[: args.limit])

    cache = load_cache(args.refresh)
    prior = {} if args.refresh else load_cache(False)  # raw, for merge-back
    now = time.time()
    to_probe = []
    for u in urls:
        c = cache.get(u)
        if c:
            ttl = CACHE_TTL_INCONCLUSIVE if c.get("verdict") in ("BLOCKED", "ERROR") else CACHE_TTL
            if now - c.get("ts", 0) < ttl:
                continue
        to_probe.append(u)

    print(f"links: {len(urls)} unique | cached: {len(urls) - len(to_probe)} | probing: {len(to_probe)}")

    results: dict[str, dict] = {}
    if to_probe:
        def work(u: str):
            time.sleep(random.uniform(0, 0.25))
            verdict, detail = probe(u)
            return u, verdict, detail

        done = 0
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            for u, verdict, detail in ex.map(work, to_probe):
                results[u] = {"verdict": verdict, "detail": detail, "ts": now}
                done += 1
                if done % 25 == 0:
                    print(f"  ... {done}/{len(to_probe)}", flush=True)
                # Flush progress so a long sweep that gets killed (or a cycle
                # that runs out of wall clock) resumes instead of restarting.
                if done % 200 == 0:
                    partial = {k: v for k, v in cache.items() if v.get("verdict") != "UNKNOWN"}
                    partial.update(results)
                    try:
                        CACHE_PATH.write_text(json.dumps(partial, indent=1, sort_keys=True))
                    except OSError:
                        pass

    merged: dict[str, dict] = {}
    for u in urls:
        merged[u] = results.get(u) or cache.get(u) or {"verdict": "UNKNOWN", "detail": "unprobed", "ts": 0}

    # Merge into the prior cache instead of replacing it: a scoped run over a
    # few paths must not throw away the results of a full-tree sweep.
    store = dict(prior)
    store.update(merged)
    CACHE_PATH.write_text(json.dumps(store, indent=1, sort_keys=True))

    dead_all = {u: m for u, m in merged.items() if m["verdict"] == "DEAD"}
    # A dead URL that only ever appears inside a code fence is a command in a
    # guide, not a link a reader clicks. Those pages carry an upstream-status
    # note instead; they are reported separately and never fail --strict.
    dead = {u: m for u, m in dead_all.items() if not urls[u]["fenced"]}
    dead_fenced = {u: m for u, m in dead_all.items() if urls[u]["fenced"]}
    pathish = [u for u, m in merged.items() if m["verdict"] == "PATH"]
    blocked = [u for u, m in merged.items() if m["verdict"] == "BLOCKED"]
    errors = [u for u, m in merged.items() if m["verdict"] == "ERROR"]

    print(f"\nOK: {sum(1 for m in merged.values() if m['verdict'] == 'OK')}"
          f" | DEAD (clickable): {len(dead)} | DEAD (in code): {len(dead_fenced)}"
          f" | PATH: {len(pathish)} | BLOCKED: {len(blocked)} | ERROR: {len(errors)}")

    if dead:
        print("\nDEAD links (clickable, repo root 404/410):")
        for u, m in sorted(dead.items()):
            print(f"  {u}  [{m['detail']}]  <- {urls[u]['file']}")
    if dead_fenced:
        print("\nDEAD inside code blocks (commands in guides, annotated on the page):")
        for u, m in sorted(dead_fenced.items())[:15]:
            print(f"  {u}  <- {urls[u]['file']}")
        if len(dead_fenced) > 15:
            print(f"  ... {len(dead_fenced) - 15} more")
    if pathish:
        print("\nPATH: 404 on the subpath but the repo exists (usually a CLI shorthand")
        print("or a browser path that needs /tree/main/; review, does not fail --strict):")
        for u in sorted(pathish)[:15]:
            print(f"  {u}  <- {urls[u]['file']}")
        if len(pathish) > 15:
            print(f"  ... {len(pathish) - 15} more")
    if errors:
        print("\nUnverified (retry later):")
        for u in sorted(errors)[:15]:
            print(f"  {u}  [{merged[u]['detail']}]")
        if len(errors) > 15:
            print(f"  ... {len(errors) - 15} more")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(merged, indent=1, sort_keys=True))
        print(f"\nwrote {args.json_out}")

    if dead and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
