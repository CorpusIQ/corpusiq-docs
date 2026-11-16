#!/usr/bin/env python3
"""Build a draft pack for one skills.sh publisher source.

Fills the gap left by the Mac Mini `build_packs.py` (not in this repo). One
call per candidate produces everything a drafter needs:

  - exact-source install rows (q=<owner/repo>&limit=96, strict source equality)
  - GitHub repo meta + FULL tree (never a sampled dir list)
  - README head (full text to scratch)
  - per-skill SKILL.md frontmatter description for every in-tree skill
  - skills.sh security verdicts (Gen Agent Trust Hub / Socket / Snyk) sampled
    across the listings, fetched with `curl -L` (without -L every cell parses
    empty, Nov 14 2026 pitfall)

Usage:
  python3 scripts/build_skill_pack.py <owner/repo> [--slug SLUG] [--out DIR] [--top N]
"""
import argparse
import json
import os
import re
import subprocess
import time
import urllib.parse

TOKEN_FILE = os.path.expanduser('~/.hermes/profiles/corpusiq/secrets/github.token')
PACE = 2.7


def sh(args, timeout=40):
    r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    return r.stdout if r.returncode == 0 else None


def curl(url, auth_github=False, follow=True):
    args = ['curl', '-sS', '-m', '30']
    if follow:
        args.append('-L')
    args += ['-A', 'Mozilla/5.0 (Hermes sweep)']
    if auth_github:
        args += ['-H', 'Authorization: token %s' % open(TOKEN_FILE).read().strip()]
    args.append(url)
    return sh(args)


def api_rows(source, limit=96):
    url = 'https://skills.sh/api/search?q=%s&limit=%d' % (urllib.parse.quote(source), limit)
    out = curl(url)
    try:
        data = json.loads(out)
    except Exception:
        return []
    rows = []
    for s in data.get('skills', []) or []:
        if (s.get('source') or '') == source:
            rows.append({'name': s.get('name'), 'skillId': s.get('skillId'),
                         'installs': int(s.get('installs', 0) or 0)})
    # de-dupe by name, keep max
    best = {}
    for r in rows:
        if r['name'] not in best or r['installs'] > best[r['name']]['installs']:
            best[r['name']] = r
    return sorted(best.values(), key=lambda r: -r['installs'])


VERDICT_RE = re.compile(r'truncate">(Gen Agent Trust Hub|Socket|Snyk)</span><span[^>]*>([^<]+)</span>')


def verdicts(source, names):
    out = {}
    for n in names:
        html = curl('https://skills.sh/%s/%s' % (source, urllib.parse.quote(n)))
        cells = VERDICT_RE.findall(html or '')
        if cells:
            out[n] = {k: v.strip() for k, v in cells}
        else:
            out[n] = {'Gen Agent Trust Hub': 'not parsed', 'Socket': 'not parsed', 'Snyk': 'not parsed'}
        time.sleep(2.6)
    return out


def gh_meta(source):
    out = curl('https://api.github.com/repos/%s' % source, auth_github=True)
    try:
        d = json.loads(out)
    except Exception:
        return {}
    return {'stars': d.get('stargazers_count'), 'description': d.get('description'),
            'license': (d.get('license') or {}).get('spdx_id'),
            'pushed_at': d.get('pushed_at'), 'branch': d.get('default_branch'),
            'html_url': d.get('html_url'), 'archived': d.get('archived'),
            'topics': d.get('topics')}


def gh_tree(source, branch):
    out = curl('https://api.github.com/repos/%s/git/trees/%s?recursive=1' % (source, branch),
               auth_github=True)
    try:
        d = json.loads(out)
    except Exception:
        return []
    return [x['path'] for x in d.get('tree', []) if x.get('type') == 'blob']


def skill_desc(source, branch, path):
    raw = 'https://raw.githubusercontent.com/%s/%s/%s' % (source, branch, path)
    txt = curl(raw)
    if not txt:
        return None
    lines = txt.splitlines()
    if not lines or lines[0].strip() != '---':
        return None
    desc = []
    collecting = False
    for line in lines[1:]:
        if line.strip() == '---':
            break
        if re.match(r'^\s*description:\s*', line):
            collecting = True
            desc.append(re.sub(r'^\s*description:\s*', '', line).strip().strip('"\''))
        elif collecting:
            if re.match(r'^\s+\S', line):
                desc.append(line.strip())
            else:
                break
    if not desc:
        return None
    return re.sub(r'\s+', ' ', ' '.join(desc)).strip().strip('"\'')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('source')
    ap.add_argument('--slug')
    ap.add_argument('--out', default='/tmp/packs')
    ap.add_argument('--top', type=int, default=20, help='verdicts to sample')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    slug = a.slug or re.sub(r'[^a-z0-9]+', '-', a.source.split('/')[-1].lower()).strip('-')
    rows = api_rows(a.source)
    total = sum(r['installs'] for r in rows)
    meta = gh_meta(a.source)
    time.sleep(0.5)
    tree = gh_tree(a.source, meta.get('branch') or 'main') if meta.get('branch') or meta else []
    readme = None
    for cand in ('README.md', 'readme.md', 'README.MD'):
        readme = curl('https://raw.githubusercontent.com/%s/%s/%s'
                      % (a.source, meta.get('branch') or 'main', cand))
        if readme and len(readme) > 50:
            break
        readme = None
    tree_skills = [p for p in tree if p.endswith('SKILL.md')]
    want = set(r['name'].lower() for r in rows[:a.top])
    descs = {}
    for p in tree_skills:
        parts = p.split('/')
        if not any(x.lower() in want for x in parts):
            continue
        descs[p] = skill_desc(a.source, meta.get('branch') or 'main', p)
    sampled = [r['name'] for r in rows[:a.top]]
    ver = verdicts(a.source, sampled) if sampled else {}
    pack = []
    pack.append('# Pack: %s' % a.source)
    pack.append('')
    pack.append('- SOURCE: %s' % a.source)
    pack.append('- SLUG: %s-setup' % slug)
    pack.append('- COMBINED INSTALLS (exact): %s' % format(total, ','))
    pack.append('- COMBINED K FORM: %.1fK' % (total / 1000.0))
    pack.append('- indexed listings: %d' % len(rows))
    pack.append('- REPO META: stars=%s license=%s pushed=%s branch=%s archived=%s'
                % (meta.get('stars'), meta.get('license'), meta.get('pushed_at'),
                   meta.get('branch'), meta.get('archived')))
    pack.append('- DESCRIPTION: %s' % (meta.get('description') or ''))
    pack.append('- URL: https://skills.sh/%s' % a.source)
    pack.append('')
    pack.append('## EXACT ROWS')
    pack.append('| skill | installs |')
    pack.append('|---|---|')
    for r in rows:
        pack.append('| %s | %s |' % (r['name'], format(r['installs'], ',')))
    pack.append('')
    pack.append('## TREE (full, %d files)' % len(tree))
    for p in tree:
        pack.append(p)
    pack.append('')
    pack.append('## SKILL DESCRIPTIONS')
    for p, d in descs.items():
        pack.append('- %s -> %s' % (p, d or '(no frontmatter description)'))
    pack.append('')
    pack.append('## SECURITY VERDICTS (skills.sh, sampled %d of %d)' % (len(ver), len(rows)))
    pack.append('| Skill | Gen Agent Trust Hub | Socket | Snyk |')
    pack.append('|---|---|---|---|')
    for n, v in ver.items():
        pack.append('| %s | %s | %s | %s |' % (n, v.get('Gen Agent Trust Hub'),
                                               v.get('Socket'), v.get('Snyk')))
    pack.append('')
    pack.append('## README')
    pack.append(readme or '(README not fetched)')
    path = os.path.join(a.out, slug + '.pack.md')
    open(path, 'w').write('\n'.join(pack) + '\n')
    print('PACK %s  total=%s rows=%d tree=%d verdicts=%d' % (path, format(total, ','),
                                                             len(rows), len(tree), len(ver)))
    json.dump({'source': a.source, 'slug': slug, 'total': total, 'rows': rows,
               'meta': meta, 'tree': tree, 'verdicts': ver,
               'descs': descs}, open(os.path.join(a.out, slug + '.pack.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
