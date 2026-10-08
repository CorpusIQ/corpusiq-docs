#!/usr/bin/env python3
"""Normalize a built MkDocs site tree to the no-slash convention + hard-verify.

Merge-path hardening for .github/workflows/vercel-deploy.yml (Oct 8, 2026):
raw MkDocs output is slashed by default (sitemap <loc> entries, canonical
tags, internal hrefs). Both local deploy paths (deploy_docs.py and
deploy_vercel_prod.py) normalize + verify before deploying; this script gives
the CI merge path the same gate so a merge can never publish slashed
artifacts to production.

Usage:
    python scripts/normalize_site_no_slash.py [site_dir]     # default: site

Exit 0 = normalized + verified clean; exit 1 = verification failed (the
caller, i.e. the deploy workflow, must abort).
Mirrors the proven functions in scripts/deploy_vercel_prod.py (Aug 30, 2026).
"""
import glob
import gzip
import os
import re
import sys

SITE = sys.argv[1] if len(sys.argv) > 1 else 'site'


def normalize_no_slash():
    for name, opener in (('sitemap.xml', open), ('sitemap.xml.gz', gzip.open)):
        sm = os.path.join(SITE, name)
        if not os.path.exists(sm):
            continue
        with opener(sm, 'rt', encoding='utf-8') as f:
            xml = f.read()
        new_xml = re.sub(
            r'<loc>(.*?)</loc>', lambda m: '<loc>{}</loc>'.format(m.group(1).rstrip('/')), xml)
        with opener(sm, 'wt', encoding='utf-8') as f:
            f.write(new_xml)
        print('   {} normalized (no-slash)'.format(name))
    link_count = 0
    for html in glob.glob(os.path.join(SITE, '**', '*.html'), recursive=True):
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
    errors = []
    for name, opener in (('sitemap.xml', open), ('sitemap.xml.gz', gzip.open)):
        p = os.path.join(SITE, name)
        if not os.path.exists(p):
            continue
        with opener(p, 'rt', encoding='utf-8') as f:
            xml = f.read()
        n = len(re.findall(r'<loc>([^<]*/)</loc>', xml))
        if n:
            errors.append('{}: {} slashed <loc> entries'.format(name, n))
    for feed in ('llms.txt', 'llms-full.txt'):
        p = os.path.join(SITE, feed)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding='utf-8').read()
        n = len(re.findall(r'https://www\.corpusiq\.io/docs/[^)\s"\']*/[)\s"\']', txt))
        if n:
            errors.append('{}: {} slashed docs URLs'.format(feed, n))
    for html in glob.glob(os.path.join(SITE, '**', '*.html'), recursive=True):
        text = open(html, encoding='utf-8').read()
        rel = os.path.relpath(html, SITE)
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
    if not os.path.isdir(SITE):
        print('ERROR: site dir not found: {}'.format(SITE))
        sys.exit(1)
    print('Normalizing {} to no-slash convention...'.format(SITE))
    normalize_no_slash()
    if not verify_no_slash():
        sys.exit(1)


if __name__ == '__main__':
    main()
