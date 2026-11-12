"""Unit tests for the llms.txt index-summary truncation.

The index line is the first thing an LLM crawler reads, so a summary that
stops mid-word ("...read-only, from the account y") or on a dangling
connective is a corrupt record, not a short one.
"""
import sys
import pathlib
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from generate_llms_txt import index_description  # noqa: E402

DANGLING = {'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'from', 'in',
            'into', 'is', 'it', 'its', 'of', 'on', 'or', 'the', 'to', 'via',
            'vs', 'with', 'your', 'that', 'this', 'those', 'without', 'plus'}


def last_word(s):
    return s.split()[-1].strip('.,;:').lower()


class IndexDescriptionTest(unittest.TestCase):
    def test_short_description_is_untouched(self):
        d = 'Bring SEO and competitive search data into the conversation.'
        self.assertEqual(index_description(d), d)

    def test_prefers_sentence_inside_the_limit(self):
        first = ('Connect your HubSpot account to ChatGPT through CorpusIQ MCP and ask '
                 'pipeline questions in plain English.')
        d = first + ' And this second thought runs on and on and on past the cap.'
        self.assertEqual(index_description(d), first)

    def test_complete_sentence_just_past_the_limit_wins(self):
        d = ('For developers: how CorpusIQ exposes 40+ business connectors through Model '
             'Context Protocol, how tools are named and scoped, and how the architecture '
             'keeps answers auditable.')
        out = index_description(d)
        self.assertEqual(out, d)
        self.assertLessEqual(len(out), 200)

    def test_punctuated_but_unbounded_text_is_cut_at_a_word_boundary(self):
        d = ('One very long sentence with no full stop that keeps going past the limit '
             'and past the overrun ceiling and therefore has to be cut somewhere that '
             'does not split a word in half or leave a connective hanging at the end and the')
        out = index_description(d)
        self.assertLessEqual(len(out), 160)
        self.assertTrue(d.startswith(out))
        self.assertNotIn(last_word(out), DANGLING)

    def test_no_mid_word_cut(self):
        d = ('Connect Google Docs to Claude through CorpusIQ MCP. Ask what a brief, '
             'contract or meeting note says and get the passage, read-only, from the '
             'account you already use everywhere else in the business today.')
        out = index_description(d)
        self.assertTrue(d.startswith(out))
        # the cut lands on a whole word from the source, never a prefix of one
        words = d.replace(',', ' ').split()
        self.assertIn(out.split()[-1].strip('.,'), [w.strip('.,') for w in words])

    def test_empty_description(self):
        self.assertEqual(index_description(''), '')
        self.assertEqual(index_description(None), '')


if __name__ == '__main__':
    unittest.main()
