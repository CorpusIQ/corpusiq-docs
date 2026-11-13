#!/usr/bin/env python3
"""Auto-sanitize a single markdown file for the pre-commit ops docs gate.

Mirrors the proven `validate-guides.py --fix` transform (em/en dash -> hyphen,
`title` clamp <=60 chars, `description` clamp <=155 chars, both on a whole-word
boundary) but operates on an arbitrary file path, so the pre-commit hook can
run it against ANY staged markdown instead of only external MCP guides.

Scoping rules (deliberate, so the gate is NOT weakened):
- Dash normalization is global: the gate's `no_dashes` rule scans the whole
  file, and Ben's content standard forbids em/en dashes everywhere, so this is
  a lossless formatting fix applied to every line.
- `title` / `description` clamping runs ONLY inside a well-formed YAML
  frontmatter block (the file must start with `---`), mirroring how the gate
  itself detects frontmatter. Body lines that merely start with `title:` are
  never touched.
- A file with no frontmatter is left for the gate to hard-fail (we never
  invent a title), and a missing/unreadable file is left for the gate's
  `readable` rule.

Idempotent: running twice yields 'clean' the second time. Prints 'changed' or
'clean' on stdout; exits 0 on success, 1 on an unreadable path.
"""

import re
import sys

EM_DASH = '\u2014'
EN_DASH = '\u2013'
MAX_TITLE = 60
MAX_DESC = 155

# Mirrors validate_page_metadata.DANGLING (the authoritative source). A title
# that ends on one of these reads as broken in the SERP, so the clamp must not
# leave one dangling. Kept as a local copy to avoid an import-time coupling
# between two pre-commit scripts.
DANGLING = {
    'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'from', 'in', 'into',
    'is', 'it', 'its', 'of', 'on', 'or', 'the', 'to', 'via', 'vs', 'with',
    'your', 'that', 'this', 'those', 'without', 'plus',
    'across', 'over', 'between', 'through', 'within', 'under', 'above',
    'below', 'behind', 'against', 'among', 'around', 'before', 'after',
    'during', 'until', 'per', 'than', 'whether', 'nor', 'because', 'although',
    'unless', 'toward', 'towards', 'onto', 'upon', 'near', 'beyond', 'despite',
    'except', 'inside', 'outside', 'throughout', 'alongside', 'regarding',
    'including', 'any',
}


def sanitize_len(value, maxlen):
    """Dash-normalize, clamp to a whole-word boundary <= maxlen, then drop any
    trailing dangling connective so the result also passes
    validate_page_metadata.dangling().

    A value that already fits is returned untouched. Routing it through
    trim_dangling() anyway was silently deleting the sentence-final period from
    every description the hook touched ("...make them useful." became
    "...make them useful"), which is exactly the no-terminal-punctuation class
    the SEO repairs were fixing (2026-11-12).
    """
    value = value.replace(EM_DASH, '-').replace(EN_DASH, '-')
    if len(value) <= maxlen:
        return value
    head = value[:maxlen]
    if ' ' in head:
        head = head.rsplit(' ', 1)[0]
    head = head.rstrip()
    return trim_dangling(head)


def trim_dangling(value):
    """Drop trailing function words / bare numbers so a clamped title never ends
    on a dangling connective (see DANGLING)."""
    words = value.split()
    while words:
        last = words[-1].strip('.,:;').lower()
        if last in DANGLING:
            words.pop()
            continue
        if re.fullmatch(r'\d+', last):
            words.pop()
            continue
        break
    return ' '.join(words).rstrip(' ,;:.-')


def sanitize_text(txt):
    txt = txt.replace(EM_DASH, '-').replace(EN_DASH, '-')
    if not txt.startswith('---\n'):
        return txt
    lines = txt.split('\n')
    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            close = i
            break
    if close is None:
        return txt
    for i in range(1, close):
        stripped = lines[i].strip()
        for key, maxlen in (('title', MAX_TITLE),):
            if stripped.startswith(key + ':'):
                val = stripped.split(':', 1)[1].strip()
                # `description` is deliberately NOT clamped here. The hook used
                # to cut it to MAX_DESC on a word boundary, which ships a
                # fragment as the live <meta name="description"> (2026-11-12:
                # "...Per-Person vs Shared Access" + a truncated compare line
                # cost a 33-page repair, PR #310). The render-time hook
                # scripts/hooks/truncate_meta_description.py already caps the
                # served value, and the ops gate reports an over-length
                # description as a WARN (meta_len), never a failure, so cutting
                # it in source deletes content that nothing puts back.
                # A folded/literal block scalar carries its value on the
                # indented lines below; rewriting this line to a quoted string
                # destroyed them. 2026-11-12: `description: >-` became
                # `description: ">"` and the value leaked into the page body.
                # The block is left alone (the render hook caps the value).
                if val in ('>', '>-', '>+', '|', '|-', '|+'):
                    break
                if len(val) >= 2 and val[0] in '\'"' and val[-1] in '\'"':
                    val = val[1:-1]
                new_val = sanitize_len(val, maxlen)
                if new_val != val:
                    indent = lines[i][:len(lines[i]) - len(lines[i].lstrip())]
                    lines[i] = '%s%s: "%s"' % (indent, key, new_val)
                break
    return '\n'.join(lines)


def main():
    if len(sys.argv) != 2:
        print('usage: sanitize_gate_docs.py <file>', file=sys.stderr)
        return 1
    path = sys.argv[1]
    try:
        with open(path, encoding='utf-8') as fh:
            txt = fh.read()
    except OSError as exc:
        print('error reading %s: %s' % (path, exc), file=sys.stderr)
        return 1
    new = sanitize_text(txt)
    if new != txt:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new)
        print('changed')
    else:
        print('clean')
    return 0


if __name__ == '__main__':
    sys.exit(main())
