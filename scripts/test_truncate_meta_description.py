"""Regression tests for the 160-character meta-description hook.

Why this exists
---------------
The base theme emits ``page.meta.description`` verbatim, so this hook decides
what every live ``<meta name="description">``, ``og:description`` and
``twitter:description`` says. Its word-boundary branch could never produce a
complete sentence -- ``_tidy`` strips the trailing period -- and rule 1 was
skipped whenever the only sentence end inside the cap landed before
``_MIN_KEEP``.

Measured on production 2026-11-12, before the fix:

  /connect-google-sheets-to-claude  ...get answers tied to the sheet and tab
  /hubspot-business-intelligence    ...pipeline intelligence, and natural-language business
  /claude-for-hubspot               ...multi-quarter forecasting, territory

1,603 pages carried that defect. These tests pin the three boundaries the hook
must respect: a clean sentence inside the cap still wins, a complete sentence
just past the cap beats a fragment, and a single long sentence is still cut.
"""
import importlib.util
import os
import unittest

_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     'scripts', 'hooks', 'truncate_meta_description.py')
_spec = importlib.util.spec_from_file_location('truncate_meta_description', _PATH)
tmd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tmd)


def _trim(desc):
    """Call the hook's trim with the same guard on_page_markdown applies."""
    if len(desc) <= tmd._MAX_LEN:
        return desc
    return tmd._trim(desc)


def _complete(s):
    return s.endswith('.') or s.endswith('!') or s.endswith('?')


class RuleOrderTest(unittest.TestCase):
    def test_sentence_inside_cap_wins(self):
        # Rule 1: a long enough sentence ends inside the cap.
        desc = ('Ask revenue, order and pipeline questions in plain English and get '
                'answers your finance team can check. Every answer cites the source '
                'row it came from, so a number is never a guess.')
        out = _trim(desc)
        self.assertLessEqual(len(out), tmd._MAX_LEN)
        self.assertTrue(_complete(out), out)
        self.assertTrue(desc.startswith(out))

    def test_complete_sentence_just_past_cap_beats_fragment(self):
        # Live regression, docs/chatgpt-integration.md. The only sentence end
        # inside the cap is at 73 characters, below _MIN_KEEP, so rule 1 was
        # skipped and the old word-boundary cut shipped 155 broken characters.
        desc = ("Use CorpusIQ inside ChatGPT - available on the ChatGPT app store. Ask "
                "natural-language questions across your connected business tools and get "
                "cited answers without leaving the chat.")
        out = _trim(desc)
        self.assertTrue(_complete(out), out)
        self.assertEqual(out, desc)

    def test_fragment_replaced_on_live_hubspot_page(self):
        # Live regression, docs/hubspot-business-intelligence.md.
        desc = ("Connect HubSpot to any AI assistant in seconds with CorpusIQ's MCP "
                "platform. Real-time CRM analytics, pipeline intelligence, and "
                "natural-language business answers from the live CRM.")
        out = _trim(desc)
        self.assertTrue(_complete(out), out)
        self.assertGreater(len(out), tmd._MAX_LEN)

    def test_overrun_is_bounded(self):
        # A single 280-character sentence has no usable sentence end: the hook
        # must still cut it rather than ship the whole value.
        desc = ('Connect every system you already run and ask one question that ' * 4).strip()
        self.assertGreater(len(desc), tmd._OVERRUN_MAX)
        out = _trim(desc)
        self.assertLessEqual(len(out), tmd._MAX_LEN)
        self.assertFalse(out.endswith(' '), out)


class CleanBoundaryTest(unittest.TestCase):
    def test_short_description_untouched(self):
        desc = 'Ask your revenue question in plain English and get a cited answer.'
        self.assertLessEqual(len(desc), tmd._MAX_LEN)
        self.assertEqual(_trim(desc), desc)

    def test_never_ends_on_a_connective(self):
        # No sentence end within the overrun ceiling, so the word-boundary cut
        # applies and must still drop the trailing "and".
        desc = ('Track inventory across warehouses and marketplaces and reconcile '
                'every restock decision against the supplier lead time you were '
                'given and the freight window that followed and')
        out = _trim(desc)
        last = out.split(' ')[-1].lower().strip('.,;:')
        self.assertNotIn(last, tmd._DANGLING, out)

    def test_no_trailing_punctuation_debris(self):
        desc = ('CorpusIQ connects your business systems, and the answers come '
                'back cited, so the numbers can be checked by the person who '
                'owns them, and the audit trail')
        out = _trim(desc)
        self.assertFalse(out.endswith((' ', ',', ';', ':', '-')), out)


class HookWiringTest(unittest.TestCase):
    def test_registered_in_mkdocs(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(root, 'mkdocs.yml'), encoding='utf-8') as fh:
            config = fh.read()
        self.assertIn('scripts/hooks/truncate_meta_description.py', config)

    def test_on_page_markdown_ignores_short_and_missing(self):
        class Page:
            def __init__(self, meta):
                self.meta = meta

        long = ('Use CorpusIQ inside ChatGPT - available on the ChatGPT app store. Ask '
                'natural-language questions across your connected business tools and get '
                'cited answers without leaving the chat.')
        page = Page({'description': long})
        tmd.on_page_markdown('body', page, {}, [])
        self.assertTrue(_complete(page.meta['description']))

        short = Page({'description': 'Short and clean.'})
        tmd.on_page_markdown('body', short, {}, [])
        self.assertEqual(short.meta['description'], 'Short and clean.')

        missing = Page({})
        tmd.on_page_markdown('body', missing, {}, [])
        self.assertEqual(missing.meta, {})


if __name__ == '__main__':
    unittest.main()
