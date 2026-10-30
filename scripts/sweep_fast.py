#!/usr/bin/env python3
"""Fast skills.sh sweep — one-pass rg cross-ref (subsumption + leftmost-mask fix).

Bug fixed Oct 2 2026: `rg -o` with many `-e` alternatives reports the LEFTMOST
alternative. A short pattern present in the set (e.g. `hermes`) masks longer
literals that start with it (`hermes-agent`), so those names falsely read NEW.
Fix: after the bulk pass, re-run a targeted pass for every collected name that
is a substring of another collected name, and union the hits.

Bug fixed Oct 7 2026: the same leftmost-alternative masking also hits longer
names that CONTAIN a shorter collected name anywhere (`github-pr-workflow` is
masked by a collected `github`; `hermes-agent-skill-authoring` by shorter names
inside it), so covered names falsely read PARTIAL. The targeted pass now
re-probes every name in EITHER containment direction versus the collected set
(scope ~85 names, ~6s). Single-pattern probes are the ground-truth semantics.

v3, Oct 9 2026: adds a five-query GENERIC PASS ('agent skills', 'claude skills',
'design engineering skill', 'ui design skill', 'frontend skill'). The Hermes-focused
15-query window structurally misses the general publisher space (validated by the
Oct 9 evening extended-query probe: 454 rows / 185 sources served, 87 tree-uncovered
at the time, ~1.06M combined installs queued). The generic pass is the mechanism
that drains that queue across fires.

Run on the Mac Mini with: export PATH=$HOME/bin:$PATH
"""
import json, subprocess, urllib.parse, urllib.request
import os

DOCS_SKILLS = os.path.expanduser('~/corpusiq-docs/hermes/skills/')
DOCS_ROOT = os.path.expanduser('~/corpusiq-docs/')

QUERIES = [
    ('nousresearch/hermes-agent', 96), ('aradotso/hermes-skills', 96),
    ('hermes', 50), ('hermes agent', 50), ('hermes skill', 50),
    ('hermes automation', 50), ('hermes agent new', 50),
    ('garrytan/gbrain', 50), ('plastic-labs/honcho', 50),
    ('aradotso/devtools-skills', 50), ('sickn33/antigravity-awesome-skills', 50),
    ('kcchien/clawpilot', 50), ('rethinking-studio/clawpilot-skills', 50),
    ('varnan-tech/opendirectory', 96), ('cosmicstack-labs/mercury-agent-skills', 50),
    # v3 (Oct 9 2026): generic pass - the general publisher space (see docstring).
    ('agent skills', 96), ('claude skills', 96),
    ('design engineering skill', 96), ('ui design skill', 96), ('frontend skill', 96),
]
SKIP_SOURCES = {'facebook/hermes'}


EXCLUDE_GLOBS = ['!**/marketplace/new-*/**']


def bulk_pass(patterns, path):
    """One rg run over many patterns.

    v4, Oct 21 2026: per-fire report pages are excluded. They list newly seen
    skill names without a guide, so counting them as coverage made a previously
    reported NEW name permanently un-convertible (Oct 21: 0 NEW vs 106 NEW
    under the corrected test). rg needs the doubled-star glob.
    """
    if not patterns:
        return set()
    args = ['rg', '--no-filename', '-o', '-i', '-F']
    for g in EXCLUDE_GLOBS:
        args += ['--glob', g]
    for p in patterns:
        if p:
            args += ['-e', p]
    args += [path]
    r = subprocess.run(args, capture_output=True, text=True, timeout=900)
    return {line.strip().lower() for line in r.stdout.splitlines() if line.strip()}


def one_pass(patterns, path, marker=None):
    """Bulk pass + masking-repair pass (both containment directions)."""
    hits = bulk_pass(patterns, path)
    lows = {p.lower() for p in patterns if p}
    masked = [p for p in patterns if p and any(p.lower() != q and (p.lower() in q or q in p.lower()) for q in lows)]
    for p in masked:
        r = subprocess.run(['rg', '--no-filename', '-o', '-i', '-F', '--glob', EXCLUDE_GLOBS[0], '-e', p, path],
                           capture_output=True, text=True, timeout=120)
        if {l.strip().lower() for l in r.stdout.splitlines() if l.strip()}:
            hits.add(p.lower())
    if marker is not None and marker.lower() not in hits:
        raise AssertionError('rg construction broken (%s missing)' % marker)
    return hits


def main():
    skills = {}
    failed = 0
    for q, limit in QUERIES:
        url = 'https://skills.sh/api/search?q=' + urllib.parse.quote(q) + '&limit=%d' % limit
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Hermes sweep)'})
        data = None
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=20) as resp:
                    data = json.loads(resp.read().decode())
                break
            except Exception as e:
                import time as _t
                wait = 8 * (2 ** attempt)
                print('QUERY RETRY %d %s: %s (sleep %ds)' % (attempt + 1, q, e, wait))
                _t.sleep(wait)
        if data is None:
            failed += 1
            print('QUERY FAIL %s' % q)
            continue
        for s in data.get('skills', []):
            src = (s.get('source') or '').strip()
            name = (s.get('name') or '').strip()
            if src in SKIP_SOURCES or not name:
                continue
            skills.setdefault('%s|%s' % (src, name),
                {'source': src, 'name': name,
                 'installs': int(s.get('installs', 0) or 0)})
    names = sorted({s['name'] for s in skills.values()})
    sources = sorted({s['source'] for s in skills.values()})

    name_hits = one_pass(names, DOCS_SKILLS, marker='hermes-agent')
    src_hits_skills = one_pass(sources, DOCS_SKILLS)
    remaining = [s for s in sources if s.lower() not in src_hits_skills]
    src_hits_root = one_pass(remaining, DOCS_ROOT)

    new_list, partial_list = [], []
    for s in skills.values():
        if s['name'].lower() in name_hits:
            continue
        if s['source'].lower() in src_hits_skills:
            partial_list.append(s); continue
        if s['source'].lower() in src_hits_root:
            continue
        new_list.append(s)
    new_list.sort(key=lambda x: -x['installs'])
    partial_list.sort(key=lambda x: -x['installs'])
    print('UNIQUE: %d | NEW: %d | PARTIAL: %d | FAILED_QUERIES: %d' % (
        len(skills), len(new_list), len(partial_list), failed))
    print('--- NEW >=100 ---')
    for s in new_list:
        if s['installs'] >= 100:
            print('%6d  %s  %s' % (s['installs'], s['source'], s['name']))
    print('--- PARTIAL >=100 ---')
    for s in partial_list:
        if s['installs'] >= 100:
            print('%6d  %s  %s' % (s['installs'], s['source'], s['name']))
    json.dump({'skills': list(skills.values()), 'new': new_list, 'partial': partial_list},
              open('/tmp/sweep_fast.json', 'w'))


if __name__ == '__main__':
    main()
