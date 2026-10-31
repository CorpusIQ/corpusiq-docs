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

URL_RE = re.compile(r"https?://[^\s)\"'<>\]]+")
TRAILING = ".,;:!?"

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
    seen: dict[str, str] = {}
    for p in paths:
        files = [p] if p.is_file() else sorted(p.rglob("*.md"))
        for f in files:
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for raw in URL_RE.findall(text):
                u = normalise(raw)
                host = u.split("/", 3)[2].lower() if u.count("/") >= 2 else ""
                if github_only and host not in ("github.com", "www.github.com"):
                    continue
                if host in SKIP_HOSTS:
                    continue
                if u not in seen:
                    seen[u] = str(f.relative_to(REPO))
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
            return "DEAD", code
        if code in (401, 403, 429, 451, 999):
            return "BLOCKED", code
        if 300 <= code < 400:
            return "OK", code
        return "ERROR", code
    except (urllib.error.URLError, TimeoutError, ssl.SSLError, OSError) as e:
        return "ERROR", str(e)[:80]


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
    now = time.time()
    to_probe = []
    for u in urls:
        c = cache.get(u)
        if c and now - c.get("ts", 0) < CACHE_TTL:
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
                    print(f"  ... {done}/{len(to_probe)}")

    merged: dict[str, dict] = {}
    for u in urls:
        merged[u] = results.get(u) or cache.get(u) or {"verdict": "UNKNOWN", "detail": "unprobed", "ts": 0}

    CACHE_PATH.write_text(json.dumps(merged, indent=1, sort_keys=True))

    dead = {u: m for u, m in merged.items() if m["verdict"] == "DEAD"}
    blocked = [u for u, m in merged.items() if m["verdict"] == "BLOCKED"]
    errors = [u for u, m in merged.items() if m["verdict"] == "ERROR"]

    print(f"\nOK: {sum(1 for m in merged.values() if m['verdict'] == 'OK')}"
          f" | DEAD: {len(dead)} | BLOCKED: {len(blocked)} | ERROR: {len(errors)}")

    if dead:
        print("\nDEAD links (404/410):")
        for u, m in sorted(dead.items()):
            print(f"  {u}  [{m['detail']}]  <- {urls[u]}")
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
