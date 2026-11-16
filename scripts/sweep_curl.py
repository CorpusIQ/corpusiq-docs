#!/usr/bin/env python3
"""curl-based skills.sh sweep runner (standing window + probe lanes).

Why: Python urllib against https://skills.sh/api/search averaged ~60s/query
(Nov 11 2026 evening fire) where curl averages ~1s, and skills.sh enforces
30 requests/minute, so pacing is mandatory. This runner shells out to curl,
paces at 2.7s, caps retries at 3, and reuses sweep_fast.one_pass for the
one-pass ripgrep cross-ref (same semantics as the standing window).

Usage:
  python3 scripts/sweep_curl.py standing            -> /tmp/sweep_standing.json
  python3 scripts/sweep_curl.py probe <lanes.json>  -> /tmp/sweep_probe.json
"""
import json
import os
import subprocess
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sweep_fast import one_pass, QUERIES, SKIP_SOURCES, DOCS_SKILLS, DOCS_ROOT  # noqa: E402

PACE = 2.7
RETRIES = 3


def fetch(q, limit):
    url = 'https://skills.sh/api/search?q=%s&limit=%d' % (urllib.parse.quote(q), limit)
    for attempt in range(RETRIES):
        r = subprocess.run(['curl', '-sS', '-m', '25', '-A', 'Mozilla/5.0 (Hermes sweep)', url],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip().startswith('{'):
            try:
                return json.loads(r.stdout)
            except Exception:
                pass
        time.sleep(5 * (attempt + 1))
    return None


def collect(queries, label):
    skills = {}
    failed = []
    for i, item in enumerate(queries):
        q, limit = (item if isinstance(item, (list, tuple)) else (item, 50))
        data = fetch(q, limit)
        if data is None:
            failed.append(q)
            print('FAIL %s' % q, flush=True)
        else:
            for s in data.get('skills', []) or []:
                src = (s.get('source') or '').strip()
                name = (s.get('name') or '').strip()
                if src in SKIP_SOURCES or not name:
                    continue
                key = '%s|%s' % (src, name)
                prev = skills.get(key)
                inst = int(s.get('installs', 0) or 0)
                if prev is None or inst > prev['installs']:
                    skills[key] = {'source': src, 'name': name, 'installs': inst}
        if (i + 1) % 25 == 0:
            print('%d/%d queries, %d rows' % (i + 1, len(queries), len(skills)), flush=True)
        time.sleep(PACE)
    names = sorted({s['name'] for s in skills.values()})
    sources = sorted({s['source'] for s in skills.values()})
    marker = 'hermes-agent'
    name_hits = one_pass(names, DOCS_SKILLS, marker=marker)
    src_hits = one_pass(sources, DOCS_SKILLS)
    remaining = [s for s in sources if s.lower() not in src_hits]
    src_hits_root = one_pass(remaining, DOCS_ROOT)
    new_list, partial_list = [], []
    for s in skills.values():
        if s['name'].lower() in name_hits:
            continue
        if s['source'].lower() in src_hits:
            partial_list.append(s)
            continue
        if s['source'].lower() in src_hits_root:
            continue
        new_list.append(s)
    new_list.sort(key=lambda x: -x['installs'])
    partial_list.sort(key=lambda x: -x['installs'])
    out = {'label': label, 'skills': list(skills.values()), 'new': new_list,
           'partial': partial_list, 'failed': failed}
    path = '/tmp/sweep_%s.json' % label
    json.dump(out, open(path, 'w'))
    uncovered = sorted({s['source'] for s in new_list})
    print('LABEL %s | UNIQUE %d | NAMES %d | SOURCES %d | NEW %d | PARTIAL %d | UNCOVERED_SOURCES %d | FAILED %d'
          % (label, len(skills), len(names), len(sources), len(new_list), len(partial_list),
             len(uncovered), len(failed)), flush=True)
    print('--- NEW >=100 ---')
    for s in new_list:
        if s['installs'] >= 100:
            print('%7d  %s  %s' % (s['installs'], s['source'], s['name']), flush=True)
    print('--- source totals (uncovered) ---')
    tot = {}
    for s in new_list:
        tot[s['source']] = tot.get(s['source'], 0) + s['installs']
    for src, v in sorted(tot.items(), key=lambda kv: -kv[1])[:60]:
        print('%8d  %s' % (v, src), flush=True)
    print('JSON %s' % path, flush=True)
    return out


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'standing'
    if mode == 'standing':
        collect(QUERIES, 'standing')
    else:
        lanes = json.load(open(sys.argv[2]))
        collect([(q, 96) for q in lanes], 'probe')
