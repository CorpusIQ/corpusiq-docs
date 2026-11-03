#!/usr/bin/env python3
"""Deploy corpusiq-docs site/ to Vercel production (docs.corpusiq.io).

Prebuilt mode: site/ is the final static output (MkDocs builds locally).
vercel.json is copied into site/ so the production redirects and
outputDirectory settings travel with the deployment.

Aug 30, 2026 — NO-SLASH HARD GATE (regression: this script shadowed the
normalized deploy_docs.py build with a RAW slashed mkdocs output; 1735/1735
sitemap locs slashed + slashed canonicals shipped to prod for ~10h, caught
by docs_live_health.py 23:00). This script is the SECOND deploy path and
must apply the SAME no-slash normalize + verify gate as deploy_docs.py
(3b/3c) BEFORE deploying. Raw mkdocs output is slashed by default.
"""
import gzip
import glob
import json
import os
import re
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRETS = '/home/hermes/.hermes/profiles/corpusiq/secrets/vercel.json'
TEAM_ID = 'team_btwsQPaxGRECjJjdKQOMcMUQ'


def main_only_gate():
    """Refuse to publish anything that is not origin/main.

    2026-11-03: two production deploys came from feature branches
    (`deploy/canon` at 14:23 UTC and `mcp/midday-sweep-nov3` at 17:10 UTC)
    because this script deploys whatever HEAD the calling clone sits on.
    A branch deploy serves unreviewed pages on docs.corpusiq.io and can
    silently revert pages that main already fixed. Production is main only;
    a branch gets a preview, never --prod.
    """
    def git(*args):
        r = subprocess.run(['git'] + list(args), cwd=REPO, capture_output=True, text=True)
        return r.returncode, (r.stdout or '').strip(), (r.stderr or '').strip()

    rc, branch, _ = git('rev-parse', '--abbrev-ref', 'HEAD')
    if rc != 0:
        print('REFUSING TO DEPLOY: cannot read the branch name in {}'.format(REPO))
        return False
    git('fetch', 'origin', 'main')
    rc, head, _ = git('rev-parse', 'HEAD')
    rc2, main_sha, _ = git('rev-parse', 'origin/main')
    if rc != 0 or rc2 != 0:
        print('REFUSING TO DEPLOY: cannot compare HEAD with origin/main')
        return False
    if branch != 'main' or head != main_sha:
        print('REFUSING TO DEPLOY: HEAD is {} ({}) but production is origin/main ({})'.format(
            branch, head[:8], main_sha[:8]))
        print('Merge the work first, then deploy from main. Branch builds get a preview, not --prod.')
        return False
    print('   Main-only gate passed (HEAD {} is origin/main)'.format(head[:8]))
    return True



def normalize_no_slash():
    """Mirror of deploy_docs.py 3b: strip trailing slashes from sitemap
    xml+gz, internal hrefs, and canonical tags. Returns counts for logging."""
    site = os.path.join(REPO, 'site')
    sitemap_count = 0
    # sitemap.xml + sitemap.xml.gz
    for name, opener in (('sitemap.xml', open), ('sitemap.xml.gz', gzip.open)):
        sm = os.path.join(site, name)
        if not os.path.exists(sm):
            continue
        with opener(sm, 'rt', encoding='utf-8') as f:
            xml = f.read()
        new_xml = re.sub(
            r'<loc>(.*?)</loc>', lambda m: '<loc>{}</loc>'.format(m.group(1).rstrip('/')), xml)
        with opener(sm, 'wt', encoding='utf-8') as f:
            f.write(new_xml)
        print('   {} normalized (no-slash)'.format(name))
    # internal hrefs + canonical tags across all HTML
    link_count = 0
    for html in glob.glob(os.path.join(site, '**', '*.html'), recursive=True):
        with open(html, encoding='utf-8') as f:
            text = f.read()

        def fix_href(m):
            nonlocal link_count
            href = m.group(1)
            if (href.startswith('http') or href.startswith('mailto:')
                    or href.startswith('tel:') or href.startswith('javascript:')
                    or href.startswith('#') or href.startswith('/assets')
                    or 'assets/' in href or '.css' in href or '.js' in href
                    or '.png' in href or '.svg' in href or '.ico' in href
                    or '.xml' in href or '.txt' in href or '.json' in href):
                return m.group(0)
            if href.endswith('/') and len(href) > 1:
                link_count += 1
                return 'href="{}"'.format(href[:-1])
            return m.group(0)

        new = re.sub(r'href="([^"]+)"', fix_href, text)
        new = re.sub(r'(https://www\.corpusiq\.io/docs/[^"\s]+?)/"', r'\1"', new)
        new = re.sub(r'(<link rel="canonical" href="[^"]+)/">', r'\1">', new)
        if new != text:
            with open(html, 'w', encoding='utf-8') as f:
                f.write(new)
    print('   Links normalized ({})'.format(link_count))


def verify_no_slash():
    """Mirror of deploy_docs.py 3c: hard-fail on any slashed invariant."""
    site = os.path.join(REPO, 'site')
    errors = []
    for name, opener in (('sitemap.xml', open), ('sitemap.xml.gz', gzip.open)):
        p = os.path.join(site, name)
        if not os.path.exists(p):
            continue
        with opener(p, 'rt', encoding='utf-8') as f:
            xml = f.read()
        n = len(re.findall(r'<loc>([^<]*/)</loc>', xml))
        if n:
            errors.append('{}: {} slashed <loc> entries'.format(name, n))
    for feed in ('llms.txt', 'llms-full.txt'):
        p = os.path.join(site, feed)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding='utf-8').read()
        n = len(re.findall(r'https://www\.corpusiq\.io/docs/[^)\s"\']*/[)\s"\']', txt))
        if n:
            errors.append('{}: {} slashed docs URLs'.format(feed, n))
    for html in glob.glob(os.path.join(site, '**', '*.html'), recursive=True):
        text = open(html, encoding='utf-8').read()
        rel = os.path.relpath(html, REPO)
        if (rel.endswith('404.html') or 'templates/' in rel
                or rel.endswith('tokens-saved-widget.html')):
            continue
        canons = re.findall(r'<link rel="canonical" href="([^"]+)"', text)
        if len(canons) != 1:
            errors.append('{}: {} canonical tags'.format(rel, len(canons)))
        elif canons[0].endswith('/'):
            errors.append('{}: slashed canonical {}'.format(rel, canons[0]))
    if errors:
        print('VERIFY GATE FAILED - deploy aborted (no-slash invariant violated):')
        for e in errors[:25]:
            print('  -', e)
        print('  ({} total violations)'.format(len(errors)))
        return False
    print('   Verify gate passed (canonical, sitemap, feeds all no-slash)')
    return True


def main():
    with open(SECRETS) as f:
        creds = json.load(f)
    tok = creds.get('token', '')
    if not tok:
        print('ERROR: no token')
        sys.exit(1)
    if not main_only_gate():
        sys.exit(2)
    if not os.path.isdir(os.path.join(REPO, 'site')):
        print('ERROR: site/ is missing. Build first (mkdocs build), then deploy.')
        sys.exit(1)
    shutil.copy(os.path.join(REPO, 'vercel.json'), os.path.join(REPO, 'site', 'vercel.json'))
    print('Rewriting sitemap lastmod from each page\'s own date...')
    step = subprocess.run([sys.executable, os.path.join(REPO, 'scripts', 'rewrite_sitemap_lastmod.py'), '--write'],
                          capture_output=True, text=True)
    print((step.stdout or '').strip())
    if step.returncode != 0:
        print((step.stderr or '').strip())
        sys.exit(step.returncode)
    print('Checking per-page Article schema and sitemap dates...')
    gate = subprocess.run([sys.executable, os.path.join(REPO, 'scripts', 'check_page_schema.py')],
                          capture_output=True, text=True)
    print((gate.stdout or '').strip())
    if gate.returncode != 0:
        print((gate.stderr or '').strip())
        sys.exit(gate.returncode)
    print('Normalizing site/ to no-slash convention...')
    normalize_no_slash()
    if not verify_no_slash():
        sys.exit(1)
    print('Absolutizing internal docs links for no-slash-safe nav...')
    absolutize_cmd = [
        sys.executable,
        os.path.join(REPO, 'scripts', 'absolutize_internal_links.py'),
        os.path.join(REPO, 'site'),
    ]
    abs_run = subprocess.run(absolutize_cmd, capture_output=True, text=True)
    if abs_run.stdout:
        print(abs_run.stdout.strip())
    if abs_run.returncode != 0:
        if abs_run.stderr:
            print(abs_run.stderr.strip())
        sys.exit(abs_run.returncode)
    for step in ('apply_canonical_overrides.py', 'prune_non_canonical_sitemap_entries.py'):
        cmd = [sys.executable, os.path.join(REPO, 'scripts', step), os.path.join(REPO, 'site')]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.stdout:
            print(proc.stdout.strip())
        if proc.returncode != 0:
            print(proc.stderr.strip())
            sys.exit(proc.returncode)
    print('Stabilizing hashed asset names for cache-safe CSS and JavaScript references...')
    stabilize_cmd = [
        sys.executable,
        os.path.join(REPO, 'scripts', 'stabilize_hashed_assets.py'),
        os.path.join(REPO, 'site'),
    ]
    stab = subprocess.run(stabilize_cmd, capture_output=True, text=True)
    if stab.stdout:
        print(stab.stdout.strip())
    if stab.returncode != 0:
        if stab.stderr:
            print(stab.stderr.strip())
        sys.exit(stab.returncode)
    env = dict(os.environ)
    env['VERCEL_PROJECT_ID'] = creds.get('docs_project_id', '')
    env['VERCEL_ORG_ID'] = TEAM_ID
    cmd = ['npx', '--yes', 'vercel@latest', 'deploy', 'site',
           '--yes', '--prod', '--token', tok, '--scope', TEAM_ID]
    print('Running: npx vercel deploy site --prod (vercel.json inside site/)')
    proc = subprocess.run(cmd, cwd=REPO, env=env, capture_output=True, text=True, timeout=600)
    print(proc.stdout[-3000:])
    print(proc.stderr[-1500:])
    sys.exit(proc.returncode)


if __name__ == '__main__':
    main()
