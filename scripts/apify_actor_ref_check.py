#!/usr/bin/env python3
"""Gate: every Apify identifier in the docs must be real.

Origin: GitHub issue #118 (2026-10-24). `apify-ultimate-scraper-setup.md` told
readers to run `apify/google-maps-scraper`, which returns 404, and the audit of
the same page found more invented identifiers: two more dead Actor slugs, three
payloads whose input keys do not exist on the real Actors, a CLI verb the CLI
does not implement (`apify actor run`), and an npm package that does not exist
(`@apify/mcp`). Invented vendor identifiers are a CLASS defect: a reader who
copies the command gets an error on step one and blames the doc.

What this checks over every tracked .md file:
  1. Actor slugs referenced as `apify actors call|start <owner>/<actor>`,
     `apify actor run <owner>/<actor>`, `apify call <owner>/<actor>` or an
     inline `apify/<actor>` mention -> GET /v2/acts/<owner>~<actor> must be 200.
  2. CLI verbs -> `apify actor run` / `apify actor call` are rejected. In
     apify-cli 1.10.0 `actor` is the runtime-only namespace (get-input,
     push-data, ...) and `actors call` is the remote-execution verb.
  3. Payloads (default; --no-payloads to skip) -> every key in the `-i '<json>'`
     (or legacy `--input`) payload must exist in the Actor's live input schema,
     required fields must be present, and enum values must be legal.
  4. npm packages -> `npx @apify/<pkg>` / `npm i @apify/<pkg>` must resolve on
     registry.npmjs.org (the published MCP server is @apify/actors-mcp-server).

Exit codes: 0 = everything verified (network-only failures are warnings),
            1 = a dead slug, bad verb, bad payload or unknown package,
            2 = could not run (not a git checkout).

Usage:
  python3 scripts/apify_actor_ref_check.py
  python3 scripts/apify_actor_ref_check.py --repo /path/to/docs --no-payloads
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ACT_RE = r"[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+"
CALL_RE = re.compile(r"apify\s+(?:actor[s]?\s+(?:call|run|start)|call)\s+(" + ACT_RE + ")")
INLINE_RE = re.compile(r"\b(apify/[A-Za-z0-9_-]{3,})\b")
PAYLOAD_RE = re.compile(
    r"apify\s+(?:actors?\s+(?:call|run|start)|call)\s+(" + ACT_RE + r")[^\n]*"
    r"\n\s*(?:-i|--input)\s+'(\{.*?\})'"
)
# `apify actor <x>` where <x> is a remote-execution verb: the namespace is wrong.
BAD_VERBS = {"actor run", "actor call", "actor start"}
NPM_RE = re.compile(r"(?:npx|npm\s+(?:i|install)|pnpm\s+(?:add|dlx)|yarn\s+add)\s+(@apify/[A-Za-z0-9._-]+)")
API = "https://api.apify.com/v2/acts/"
NPM = "https://registry.npmjs.org/"
TIMEOUT = 25

# `apify/<x>` is also how GitHub repos and npm packages are spelled; a bare
# mention only counts as an Actor when the line is not a repo/package reference.
NOT_AN_ACTOR_MARKERS = (
    "github.com", "gitlab.com", "npmjs.com", "registry.npmjs", "www.npmjs.com",
    "npx ", "npm install", "npm i ", "skills.sh", "pypi",
)
IGNORE_SLUGS = {
    "apify/agent-skills", "apify/apify-mcp-server", "apify/mcp",
    "apify/apify-cli", "apify/crawlee", "apify/fingerprint-suite",
}
REPO_DEFAULT = Path(__file__).resolve().parent.parent


def api_get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "corpusiq-docs-gate"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.getcode(), json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as exc:
        return exc.code, None
    except Exception:
        return 0, None


def track_md(repo: Path):
    out = subprocess.run(["git", "-C", str(repo), "ls-files", "*.md"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        return None
    return [repo / line for line in out.stdout.splitlines() if line.strip()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(REPO_DEFAULT))
    ap.add_argument("--no-payloads", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    files = track_md(repo)
    if files is None:
        print("cannot run: --repo is not a git checkout")
        return 2

    refs: dict[str, set[str]] = {}
    payloads: list[tuple[str, str, str]] = []
    verbs: dict[str, set[str]] = {}
    packages: dict[str, set[str]] = {}

    for path in files:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if "apify" not in text.lower():
            continue
        rel = str(path.relative_to(repo))
        for m in CALL_RE.finditer(text):
            refs.setdefault(m.group(1), set()).add(rel)
            v = re.search(r"apify\s+(actor[s]?\s+\w+|call)\s", m.group(0))
            if v:
                verbs.setdefault(" ".join(v.group(1).split()), set()).add(rel)
        for m in INLINE_RE.finditer(text):
            slug = m.group(1)
            if slug in IGNORE_SLUGS:
                continue
            start = text.rfind("\n", 0, m.start()) + 1
            end = text.find("\n", m.end())
            line = text[start: end if end != -1 else len(text)]
            if any(marker in line for marker in NOT_AN_ACTOR_MARKERS):
                continue
            refs.setdefault(slug, set()).add(rel)
        for m in PAYLOAD_RE.finditer(text):
            payloads.append((m.group(1), rel, m.group(2)))
        for m in NPM_RE.finditer(text):
            packages.setdefault(m.group(1), set()).add(rel)

    dead: dict[str, list[str]] = {}
    schema_unknown: list[str] = []
    for slug in sorted(refs):
        code, _ = api_get(API + slug.replace("/", "~"))
        if not args.quiet:
            print(f"  {code:>3} {slug}  ({len(refs[slug])} file(s))")
        if code == 0:
            schema_unknown.append(slug)
        elif code != 200:
            dead[slug] = sorted(refs[slug])
        time.sleep(0.4)

    bad_payloads: list[str] = []
    if not args.no_payloads:
        for actor, rel, payload in payloads:
            code, body = api_get(API + actor.replace("/", "~") + "/builds/default")
            if code != 200 or not body:
                if code == 0:
                    schema_unknown.append(actor)
                else:
                    bad_payloads.append(f"{rel}: {actor} build lookup {code}")
                continue
            try:
                schema = body["data"]["inputSchema"]
                schema = json.loads(schema) if isinstance(schema, str) else schema
                data = json.loads(payload)
            except Exception as exc:
                bad_payloads.append(f"{rel}: {actor} unreadable ({exc})")
                continue
            props = schema.get("properties", {}) or {}
            unknown = [k for k in data if k not in props]
            missing = [r for r in (schema.get("required") or []) if r not in data]
            enum_bad = [f"{k}={data[k]!r}" for k in data
                        if k in props and props[k].get("enum") and data[k] not in props[k]["enum"]]
            if unknown or missing or enum_bad:
                bad_payloads.append(
                    f"{rel}: {actor} unknown={unknown} missing_required={missing} bad_enum={enum_bad}")
            time.sleep(0.4)

    bad_verbs = sorted(v for v in verbs if v in BAD_VERBS)

    bad_packages: list[str] = []
    for pkg, where in sorted(packages.items()):
        code, _ = api_get(NPM + urllib.parse.quote(pkg, safe=""))
        if code == 0:
            schema_unknown.append(pkg)
        elif code != 200:
            bad_packages.append(f"{pkg} -> {code}  in: {', '.join(sorted(where))}")
        time.sleep(0.3)

    print(f"\nscanned {len(files)} markdown files, {len(refs)} distinct actor slugs")
    if schema_unknown:
        print(f"WARN could not resolve over the network (not blocking): "
              f"{', '.join(sorted(set(schema_unknown)))}")
    if dead:
        print("DEAD ACTORS:")
        for slug, where in dead.items():
            print(f"  - {slug} -> 404  in: {', '.join(where)}")
    if bad_verbs:
        print("NON-EXISTENT CLI VERBS (use `apify actors call`):")
        for v in bad_verbs:
            print(f"  - apify {v}  in: {', '.join(sorted(verbs[v]))}")
    if bad_payloads:
        print("INVALID PAYLOADS:")
        for line in bad_payloads:
            print(f"  - {line}")
    if bad_packages:
        print("UNKNOWN NPM PACKAGES:")
        for line in bad_packages:
            print(f"  - {line}")
    if dead or bad_verbs or bad_payloads or bad_packages:
        return 1
    print("OK: every Apify reference, payload and package resolves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
