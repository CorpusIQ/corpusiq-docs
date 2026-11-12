"""MkDocs hook: cap meta descriptions at 160 characters, at a clean boundary.

Ahrefs Site Audit flags "Meta description too long" for descriptions over 160
characters. The base theme emits ``page.meta.description`` verbatim, and many
frontmatter descriptions run long. This hook trims an over-length description
in ``page.meta`` before the page renders, so the rendered
``<meta name="description">`` -- and the ``og:description`` /
``twitter:description`` built from the same value in ``overrides/main.html`` --
all stay within the limit.

Cut order (first boundary that keeps at least ``_MIN_KEEP`` characters wins):

1. the end of the last complete sentence inside the cap,
2. the first complete sentence that ends just past the cap, up to
   ``_OVERRUN_MAX``,
3. a word boundary, after popping any trailing function word.

Rule 3 exists because the old implementation cut at ``_TARGET`` and left
dangling fragments in live snippets ("...and get real-time, source-cited",
"...Compare Glean, Guru, and"). A description that ends on "and" reads as
broken text in the SERP, so the last word must never be a connective.

Rule 2 exists because rule 3 can NEVER return a complete sentence: ``_tidy``
strips the trailing period, so the word-boundary cut always lands mid-thought.
Live evidence 2026-11-12: 1,603 pages shipped a ``<meta name="description">``
that stopped mid-sentence ("...and get answers tied to the sheet and tab",
"...territory") because rule 1 was skipped whenever the only sentence end
inside the cap landed before ``_MIN_KEEP``. A description that runs to its own
full stop at 181 characters is a complete thought; the same text cut to 155
characters is broken. The overrun is bounded so a 280-character single-sentence
description still gets the word-boundary treatment.

Running in ``on_page_markdown`` (before the template renders) is what makes the
single edit to ``page.meta`` flow through to every consumer of the description.
"""

import re

# Ahrefs flags descriptions longer than this many characters.
_MAX_LEN = 160
# Never produce a snippet shorter than this -- a 40-character fragment is worse
# than a slightly over-length one, so fall through to the next rule instead.
_MIN_KEEP = 90
# Hard ceiling for rule 2. A complete sentence that closes shortly after the cap
# beats a fragment cut at the cap; a single 280-character sentence must still be
# cut, so the overrun stays bounded.
_OVERRUN_MAX = 200

# Words that must never be the last word of a rendered description.
_DANGLING = {
    'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'from', 'in', 'into', 'is',
    'it', 'its', 'of', 'on', 'or', 'the', 'to', 'via', 'vs', 'with', 'your',
    'that', 'this', 'these', 'those', 'without', 'plus',
}

_SENTENCE_END = re.compile(r'[.!?](?=\s|$)')


def _tidy(s):
    return re.sub(r'\s+', ' ', s).strip().rstrip(' ,;:.-')


def _trim(desc):
    head = desc[:_MAX_LEN]

    # 1. last complete sentence inside the cap
    ends = [m.end() for m in _SENTENCE_END.finditer(head)]
    if ends and ends[-1] >= _MIN_KEEP:
        return desc[:ends[-1]].strip()

    # 2. word boundary, with trailing connectives popped. A clause cut is
    # deliberately NOT used: cutting at a comma and forcing a period yields
    # fragments like "and get real-time." A word boundary that drops the
    # trailing connective at least ends on a complete phrase.
    cut = _tidy(desc[:_MAX_LEN].rsplit(' ', 1)[0])
    words = cut.split(' ')
    while words and words[-1].lower().strip('.,;:') in _DANGLING:
        words.pop()
    cut = ' '.join(words).rstrip(' ,;:.-')

    # 3. First complete sentence that closes just past the cap. Reaching here
    # means no sentence ended inside the cap at a usable length, and the
    # word-boundary cut cannot end a sentence at all -- _tidy strips the
    # trailing period. Ship the complete thought and accept the small overrun.
    for m in _SENTENCE_END.finditer(desc, _MAX_LEN):
        if m.end() <= _OVERRUN_MAX:
            return desc[:m.end()].strip()
        break

    return cut or _tidy(desc[:_MAX_LEN])


def on_page_markdown(markdown, page, config, files):
    if page is None:
        return markdown
    desc = page.meta.get('description')
    if not isinstance(desc, str) or len(desc) <= _MAX_LEN:
        return markdown
    page.meta['description'] = _trim(desc)
    return markdown
