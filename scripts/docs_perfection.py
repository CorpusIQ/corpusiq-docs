#!/usr/bin/env python3
"""docs_perfection.py - CorpusIQ docs repo perfection audit + safe auto-fixes.

Audits the BUILT site (site/) when present for the classes the fleet keeps
drifting on, and auto-fixes the safe ones in SOURCE:
  - em/en dashes (house rule: none anywhere public)  [auto-fix]
  - titles over 60 chars                             [auto-fix, conservative]
  - H1 count != 1, missing meta description/canonical, images missing,
    unresolved internal links                      [report]

Usage:
  python3 scripts/docs_perfection.py            # audit (site/ if present) + report
  python3 scripts/docs_perfection.py --fix      # auto-fix dashes + titles in source
  python3 scripts/docs_perfection.py --source   # dash-only scan when no build

Exit codes: 0 = clean (or fixed), 1 = remaining issues need attention.
"""
import os, re, sys, glob, json

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)
SITE = os.path.join(REPO, 'site')
FIX = '--fix' in sys.argv
SOURCE_ONLY = '--source' in sys.argv

DASH = re.compile('[\u2014\u2013]')

def _tidy(s):
    s = re.sub(r'\s{2,}', ' ', s)
    s = re.sub(r'\s+--\s+', ' - ', s)
    s = re.sub(r'\s*[\u2014\u2013]\s*', ' - ', s)
    return s.strip(' -')

STOP = {'can', 'you', 'your', 'in', 'for', 'and', 'the', 'a', 'an', 'to', 'with', 'of',
        'vs', 'on', 'or', 'at', 'by', 'is', 'are', 'it', 'its', 'from', 'that', 'this'}

def compact(t, limit=60):
    s = _tidy(t)
    for pat in (r'\s+for Hermes Growth Agents$', r'\s+for Hermes Agents$', r'\s+for Hermes Agent$',
                r'\s+for Hermes$', r'\s+for OpenClaw$'):
        s = re.sub(pat, '', s, flags=re.I)
    s = re.sub(r' - Full Setup Guide\b', ' - Setup Guide', s, flags=re.I)
    s = re.sub(r'\s+for Hermes(?=\s*\()', '', s, flags=re.I)
    s = re.sub(r'\((?:Ask|Ask Your)[^)]*[Pp]lain [Ee]nglish[^)]*\)', '(Plain English Q&A)', s)
    s = re.sub(r'\((?:Real|Ask)[^)]{18,}\)\s*$', '(Plain English)', s)
    s = _tidy(s)
    if len(s) > limit:
        s2 = re.sub(r'\s+for\s+[A-Z][^.]{2,28}$', '', s)
        if len(s2) >= 25:
            s = s2

    def wbtrim(x, lim):
        if len(x) <= lim:
            return x
        cut = x[:lim + 1]
        cut = cut[:cut.rfind(' ')] if ' ' in cut else cut[:lim]
        words = cut.split()
        while words and words[-1].lower().strip('.,;:') in STOP:
            words.pop()
        return ' '.join(words).rstrip('.,;:')

    if len(s) > limit:
        sep = ' - ' if ' - ' in s else (': ' if ': ' in s else None)
        if sep:
            head, _, tail = s.partition(sep)
            tail = re.sub(r'\s+Setup Guide$', '', tail)
            tail = re.sub(r'\s+Setup$', '', tail)
            tail = re.sub(r'\s+Suite Setup$', ' Suite', tail)
            tail2 = wbtrim(tail, max(limit - len(head) - len(sep), 12))
            s = head + sep + tail2 if tail2 else head
        else:
            s = wbtrim(s, limit)
    return _tidy(s)

def dash_fix_sources():
    changed = []
    for root, dirs, files in os.walk('.'):
        if any(x in root for x in ('/.git', '/site', '/node_modules', '/.cache')):
            continue
        for f in files:
            if not f.endswith(('.md', '.html')):
                continue
            fp = os.path.join(root, f)
            try:
                t = open(fp, encoding='utf-8', errors='replace').read()
            except Exception:
                continue
            if DASH.search(t):
                n = len(DASH.findall(t))
                t2 = re.sub(r'\s*[\u2014\u2013]\s*', ' - ', t)
                t2 = re.sub(r'  +', ' ', t2)
                open(fp, 'w', encoding='utf-8').write(t2)
                changed.append((fp, n))
    return changed

def resolve_source(rel):
    base = rel[:-len('index.html')].rstrip('/') if rel.endswith('index.html') else rel[:-len('.html')]
    for c in (f'{base}.md', f'docs/{base}.md', f'{base}/index.md', f'docs/{base}/index.md'):
        if os.path.exists(c):
            return c
    return None

def audit_site():
    issues = {'title_long': [], 'h1': [], 'desc': [], 'canon': [], 'img': [], 'unresolved': []}
    if not os.path.isdir(SITE):
        return issues
    existing = set()
    for root, _, files in os.walk(SITE):
        for f in files:
            p = os.path.relpath(os.path.join(root, f), SITE).replace(os.sep, '/')
            existing.add(p)
            if f == 'index.html':
                d = os.path.dirname(p)
                if d:
                    existing.add(d)

    def target_exists(rp):
        rp = rp.strip('/')
        return bool(rp and (rp in existing or (rp + '/index.html') in existing or (rp + '.html') in existing))

    import posixpath
    for h in glob.glob(os.path.join(SITE, '**', '*.html'), recursive=True):
        rel = os.path.relpath(h, SITE).replace(os.sep, '/')
        if rel == '404.html' or '/hermes/templates/' in ('/' + rel) or 'tokens-saved-widget' in rel:
            continue
        t = open(h, encoding='utf-8', errors='replace').read()
        m = re.search(r'<title>(.*?)</title>', t, re.S | re.I)
        if m and len(m.group(1)) > 60:
            issues['title_long'].append((rel, m.group(1)))
        n1 = len(re.findall(r'<h1[^>]*>', t, re.I))
        if n1 != 1:
            issues['h1'].append((rel, n1))
        if not re.search(r'<meta name="description" content="[^"]+"', t, re.I):
            issues['desc'].append(rel)
        if 'rel="canonical"' not in t:
            issues['canon'].append(rel)
        for sm in re.finditer(r'<img[^>]+src="([^"]+)"', t):
            src = sm.group(1)
            if src.startswith(('http', 'data:', '/')):
                continue
            base = '/' + os.path.dirname(rel) if os.path.dirname(rel) else '/'
            rp = posixpath.normpath(base + '/' + src).lstrip('/')
            if rp not in existing:
                issues['img'].append((rel, src))
        pdir = os.path.dirname(rel)
        for hm in re.finditer(r'href="([^"]+)"', t):
            hr = hm.group(1)
            if hr.startswith(('http', 'mailto', 'tel', 'javascript', 'data:', '#', '?')) or '{{' in hr:
                continue
            pp = hr.split('#')[0].split('?')[0]
            low = pp.lower()
            if not pp or low.endswith(('.css', '.js', '.png', '.svg', '.ico', '.jpg', '.jpeg', '.webp',
                                       '.gif', '.woff', '.woff2', '.ttf', '.mp4', '.webm', '.pdf', '.gz', '.zip')) \
                    or 'assets/' in low:
                continue
            if pp.startswith('/docs/'):
                R = posixpath.normpath(pp[len('/docs'):])  # www-form /docs/<path> -> <path>
            elif pp.startswith('/'):
                # Root-relative non-/docs links are the deliberate www-form family
                # (docs pages pointing at marketing-site paths, e.g. /enterprise,
                # /connect/..., /compare). They resolve on www.corpusiq.io; they
                # are not docs-internal targets, so they are not audited here.
                continue
            else:
                base = '/' + pdir if pdir else '/'
                R = posixpath.normpath(base.rstrip('/') + '/' + pp)
            if R == '/' or '..' in R.split('/'):
                continue
            if not target_exists(R.strip('/')):
                issues['unresolved'].append((rel, hr))
    return issues

def title_fix():
    issues = audit_site()
    fixed, leftovers = [], []
    for rel, old in issues['title_long']:
        src = resolve_source(rel)
        if not src:
            leftovers.append((rel, old))
            continue
        # guard: only touch sources whose CURRENT title still matches the
        # stale built title (avoid clobbering newer source edits by the fleet)
        cur = None
        t = open(src, encoding='utf-8').read()
        mc = re.search(r'(?m)^(?:title|name): ?"?([^"\n]*)"?$', t)
        if mc:
            cur = mc.group(1).strip()
        else:
            mh = re.search(r'(?m)^# (.+)$', t)
            if mh:
                cur = mh.group(1).strip()
        if cur != old.strip():
            continue
        new = compact(old)
        t = open(src, encoding='utf-8').read()
        n = 0
        for k in ('title', 'name'):
            if re.search(r'(?m)^%s: ?' % k, t):
                val = '"%s"' % new if ':' in new else new
                t = re.sub(r'(?m)^%s: ?.*$' % k, '%s: %s' % (k, val), t, count=1)
                n += 1
        if n:
            open(src, 'w', encoding='utf-8').write(t)
            fixed.append((rel, old, new))
        if len(new) > 60:
            leftovers.append((rel, new))
    return fixed, leftovers

def main():
    rc = 0
    if FIX:
        dc = dash_fix_sources()
        print(f'dashes fixed: {len(dc)} files')
        fixed, leftovers = title_fix()
        print(f'titles fixed: {len(fixed)} files')
        for rel, old, new in fixed[:15]:
            print(f'   {len(old)} -> {len(new)}  {rel}')
        if leftovers:
            print('titles still over 60 (need manual):')
            for rel, v in leftovers:
                print(f'   {rel} | {v}')
            rc = 1
    issues = audit_site()
    print()
    print('AUDIT (site/):')
    print(f"  titles>60: {len(issues['title_long'])}  h1!=1: {len(issues['h1'])}  "
          f"desc missing: {len(issues['desc'])}  canonical missing: {len(issues['canon'])}  "
          f"img missing: {len(issues['img'])}  unresolved links: {len(issues['unresolved'])}")
    for k in ('title_long', 'h1', 'desc', 'canon', 'img', 'unresolved'):
        for item in issues[k][:25]:
            print(f'   [{k}] {item}')
    if any(issues.values()):
        rc = 1
    sys.exit(rc)

if __name__ == '__main__':
    main()
