#!/usr/bin/env python3
"""Page-metadata gate: blocks the classes of corruption that reached production.

Two defect classes each shipped to live pages because nothing checked them:

1. DUPLICATE FOOTER LINES. A footer appender ran twice on the same page, so the
   closing italic line rendered twice. Recovered across 150+ pages (docs/ and
   hermes/) on 2026-10-24.
2. DANGLING TITLES. ``docs_perfection.compact()`` cut titles at 60 characters
   and left the last word a connective ("...Native Web Workspace for"), which
   became the <title> tag: the SERP headline read as broken text.

Warnings (reported, not fatal -- the render hook caps description length):

3. Descriptions longer than 160 characters (``scripts/hooks/
   truncate_meta_description.py`` trims them at a clean boundary at build time).
4. Descriptions that do not end on terminal punctuation (a style question, not
   corruption -- only a dangling connective is a defect).

Usage:
    python3 scripts/validate_page_metadata.py [--warn] [--fix] [repo-root]

--fix repairs dangling titles by rebuilding them from the page H1 (only when
the current title is a strict prefix of the H1, so an intentional short title
is never overwritten). Exit 1 on any fatal finding (fail closed).
"""
import os
import re
import sys

DANGLING = {
    'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'from', 'in', 'into',
    'is', 'it', 'its', 'of', 'on', 'or', 'the', 'to', 'via', 'vs', 'with',
    'your', 'that', 'this', 'those', 'without', 'plus',
}
SKIP_DIRS = {'.git', 'site', 'node_modules', '.cache', '__pycache__'}
MAX_DESC = 160
MAX_TITLE = 60


def pages(root):
    for dp, dirs, fns in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in fns:
            if f.endswith('.md'):
                yield os.path.join(dp, f)


def frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    return m.group(1) if m else None


def value(fm, key):
    m = re.search(r'(?m)^%s:\s*(.*)$' % key, fm)
    if not m:
        return None
    v = m.group(1).strip()
    if re.fullmatch(r'>-?|\|', v):
        return None  # YAML block scalar: the value is on the following lines
    return v.strip('"')


def h1_of(text):
    m = re.search(r'(?m)^#\s+(.+)$', text)
    return m.group(1).strip() if m else None


def dangling(title):
    s = title.strip()
    if not s:
        return True
    if s.endswith('...') or s[-1] in '&|,;:/-+':
        return True
    last = re.split(r'\s+', s)[-1].strip('.,:;').lower()
    return last in DANGLING or not last


def retitle(title, h1):
    """Longest prefix of the H1 that fits MAX_TITLE and does not end dangling."""
    if not h1 or not h1.lower().startswith(title.strip().lower()):
        return None
    words = h1.split()
    best = None
    for i in range(1, len(words) + 1):
        cand = ' '.join(words[:i]).rstrip(' ,;:.-')
        if len(cand) > MAX_TITLE:
            break
        if not dangling(cand) and len(cand) >= 25:
            best = cand
    return best


def main(argv):
    warn = '--warn' in argv
    do_fix = '--fix' in argv
    args = [a for a in argv[1:] if not a.startswith('-')]
    root = os.path.abspath(args[0]) if args else os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))

    dup_footer, bad_title, long_desc, open_desc, fixed = [], [], 0, 0, []
    for p in pages(root):
        rel = os.path.relpath(p, root)
        try:
            text = open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue

        lines = [l.strip() for l in text.split('\n') if l.strip()]
        for i in range(1, len(lines)):
            ln = lines[i]
            if (ln == lines[i - 1] and ln.startswith('*') and ln.endswith('*')
                    and len(ln) >= 40 and 'This Hermes repo' not in ln):
                dup_footer.append(rel)
                break

        fm = frontmatter(text)
        if not fm:
            continue
        title = value(fm, 'title')
        if title and dangling(title):
            new = retitle(title, h1_of(text)) if do_fix else None
            if new:
                t2 = re.sub(r'(?m)^title:.*$', 'title: "%s"' % new.replace('"', "'"),
                            text, count=1)
                open(p, 'w', encoding='utf-8').write(t2)
                fixed.append((rel, title, new))
            else:
                bad_title.append((rel, title))
        elif title and len(title) > MAX_TITLE:
            bad_title.append((rel, 'LEN %d: %s' % (len(title), title)))

        desc = value(fm, 'description')
        if desc:
            if dangling(desc):
                bad_title.append((rel, 'DESC DANGLING: ...%s' % desc[-40:]))
            elif len(desc) > MAX_DESC:
                long_desc += 1
            elif not re.search(r'[.!?"\')\]]\s*$', desc):
                open_desc += 1

    total = len(dup_footer) + len(bad_title)
    print('page-metadata gate: %s' % os.path.relpath(root))
    print('  duplicate footer lines   : %d' % len(dup_footer))
    print('  dangling/invalid titles  : %d' % len(bad_title))
    print('  titles repaired from H1  : %d' % len(fixed))
    print('  (warn) descriptions >160 : %d' % long_desc)
    print('  (warn) no terminal punct : %d' % open_desc)
    for rel in dup_footer[:20]:
        print('   [dup-footer] %s' % rel)
    for rel, t in bad_title[:20]:
        print('   [title] %s | %s' % (rel, t))
    for rel, old, new in fixed[:20]:
        print('   [fixed] %s | %s -> %s' % (rel, old, new))
    if total:
        print('RESULT: %s (%d findings)' % ('warn' if warn else 'FAIL', total))
        return 0 if warn else 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
