"""Regression tests for the duplicated-brand <title> repair.

The site template renders page.meta.title verbatim, so a frontmatter title that
already carries the brand suffix and has it appended again reaches the SERP as
"... - CorpusIQ Docs - CorpusIQ Docs". That defect was live on 121 pages and on
the domain's highest-impression catalog page (7,483 impressions, 0.04% CTR)
before the check landed.
"""
import importlib.util
import os
import unittest

_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     'validate_page_metadata.py')
_spec = importlib.util.spec_from_file_location('validate_page_metadata', _PATH)
vpm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vpm)


class BrandDupeTest(unittest.TestCase):
    def test_flags_repeated_brand(self):
        for title in (
            'Supabase - CorpusIQ Docs - CorpusIQ',
            'Contributing to CorpusIQ Docs - CorpusIQ Docs',
            'PostgreSQL - CorpusIQ Docs - CorpusIQ',
            'New Skills - CorpusIQ Docs - CorpusIQ Docs',
        ):
            self.assertTrue(vpm.brand_dupe(title), title)

    def test_accepts_single_brand(self):
        for title in (
            'CorpusIQ MCP Troubleshooting - CorpusIQ Docs',
            'Docker Hermes Agent Setup - CorpusIQ Docs',
            'CorpusIQ vs Viktor Pricing: Flat Plans vs Credit Metering',
            'Delete Hermes Agent Sessions and Prune state.db',
        ):
            self.assertFalse(vpm.brand_dupe(title), title)


class UnbrandTest(unittest.TestCase):
    def test_collapses_to_one_suffix(self):
        cases = {
            'Supabase - CorpusIQ Docs - CorpusIQ': 'Supabase - CorpusIQ Docs',
            'PostgreSQL - CorpusIQ Docs - CorpusIQ': 'PostgreSQL - CorpusIQ Docs',
            'New Skills - CorpusIQ Docs - CorpusIQ Docs': 'New Skills - CorpusIQ Docs',
        }
        for src, want in cases.items():
            self.assertEqual(vpm.unbrand(src), want)

    def test_does_not_double_a_branded_base(self):
        src = 'Contributing to CorpusIQ Docs - CorpusIQ Docs'
        self.assertEqual(vpm.unbrand(src), 'Contributing to CorpusIQ Docs')

    def test_drops_suffix_when_base_is_long(self):
        src = ('A very long base title that goes on and on past sixty chars '
               'for sure - CorpusIQ Docs - CorpusIQ Docs')
        out = vpm.unbrand(src)
        self.assertEqual(out, 'A very long base title that goes on and on past '
                              'sixty chars for sure')
        self.assertFalse(vpm.brand_dupe(out))

    def test_repair_is_idempotent(self):
        for title in ('Supabase - CorpusIQ Docs - CorpusIQ',
                      'Contributing to CorpusIQ Docs - CorpusIQ Docs'):
            once = vpm.unbrand(title)
            self.assertEqual(vpm.unbrand(once), once)
            self.assertFalse(vpm.brand_dupe(once))


if __name__ == '__main__':
    unittest.main()
