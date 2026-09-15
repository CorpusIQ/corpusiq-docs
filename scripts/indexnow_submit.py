#!/usr/bin/env python3
"""IndexNow submission for corpusiq-docs.

Values pinned per the frontend runbook (docs/runbooks/indexnow-key.md in
CorpusIQ/corpusiq-frontend): the key is public by design, its proof file is
served at https://www.corpusiq.io/<key>.txt, and docs URLs live under the
same www host via the /docs/:path* rewrite.

Modes:
  python3 scripts/indexnow_submit.py --all      # submit the full sitemap (bootstrap)
  python3 scripts/indexnow_submit.py            # submit pages changed since the
                                                # last marker (.indexnow-last)

Never fails the caller: prints the response and exits 0 on every status
(a ping failure must not fail the deploy that triggered it).
"""
import json, os, re, subprocess, sys, urllib.request, urllib.error

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

KEY = '619b0a15ffaf16fc05f32fc94740ae7c'
HOST = 'www.corpusiq.io'
KEY_LOCATION = f'https://{HOST}/{KEY}.txt'
ENDPOINT = 'https://api.indexnow.org/indexnow'
MARKER = os.path.join(REPO, '.indexnow-last')
SITEMAP = os.path.join(REPO, 'site', 'sitemap.xml')


def submit(urls):
    urls = [u for u in dict.fromkeys(urls)]  # dedupe, keep order
    if not urls:
        print('indexnow: nothing to submit')
        return
    total = 0
    for i in range(0, len(urls), 10000):
        chunk = urls[i:i + 10000]
        payload = json.dumps({
            'host': HOST,
            'key': KEY,
            'keyLocation': KEY_LOCATION,
            'urlList': chunk,
        }).encode('utf-8')
        req = urllib.request.Request(
            ENDPOINT, data=payload,
            headers={'Content-Type': 'application/json; charset=utf-8',
                     'User-Agent': 'CorpusIQ-docs-indexnow/1.0'})
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                code = r.status
                body = r.read().decode('utf-8', 'replace')[:200]
        except urllib.error.HTTPError as e:
            code = e.code
            body = (e.read().decode('utf-8', 'replace')[:200] if e.fp else '')
        except Exception as e:
            code = -1
            body = f'{type(e).__name__}: {e}'
        note = {200: 'accepted', 202: 'accepted', 400: 'malformed payload',
                403: 'key not verified', 422: 'url/host mismatch', 429: 'rate limited'}.get(code, '')
        print(f'indexnow: {len(chunk)} urls -> HTTP {code} {note} {body[:120]}')
        total += len(chunk)
    print(f'indexnow: submitted {total} url(s)')


def url_for_md(path):
    p = path
    if p.startswith('docs/'):
        p = p[5:]  # real files inside docs_dir map to docs root
    if not p.endswith('.md'):
        return None
    p = p[:-3]
    if p.endswith('/index'):
        p = p[:-6]
    if p.endswith('/README') or p == 'README':
        p = p[:-7] if p.endswith('/README') else ''
    cand = p.strip('/')
    if not cand:
        return None
    # job files / non-page content
    if cand.startswith(('.', '_')) or '/_' in ('/' + cand):
        return None
    if not (os.path.exists(os.path.join('site', cand, 'index.html'))
            or os.path.exists(os.path.join('site', cand + '.html'))):
        return None
    return f'https://{HOST}/docs/{cand}'


def main():
    if '--all' in sys.argv or not os.path.exists(MARKER):
        if not os.path.exists(SITEMAP):
            print('indexnow: no site/sitemap.xml (run a build first), skipping bootstrap')
            return
        xml = open(SITEMAP, encoding='utf-8').read()
        urls = re.findall(r'<loc>([^<]+)</loc>', xml)
        urls = [u for u in urls if '/docs/' in u]
        print(f'indexnow: bootstrap mode, {len(urls)} sitemap urls')
        submit(urls)
    else:
        last = open(MARKER).read().strip()
        try:
            out = subprocess.run(['git', 'diff', '--name-only', f'{last}..HEAD'],
                                 capture_output=True, text=True, timeout=60).stdout
        except Exception as e:
            print(f'indexnow: diff failed ({e}), skipping')
            return
        urls = []
        for line in out.splitlines():
            u = url_for_md(line.strip())
            if u:
                urls.append(u)
        print(f'indexnow: {len(urls)} changed page(s) since {last[:10]}')
        submit(urls)
    # advance marker
    try:
        head = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True,
                              text=True, timeout=30).stdout.strip()
        if head:
            open(MARKER, 'w').write(head + '\n')
    except Exception:
        pass


if __name__ == '__main__':
    main()
