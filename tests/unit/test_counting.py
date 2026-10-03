"""Verify pure counting against hand-checked SPEC examples and boundaries."""

import unittest

from textstats.counting import count_text


class CountingTests(unittest.TestCase):
    """Protect newline, whitespace and single-leading-BOM semantics."""

    def assert_counts(self, text, lines, words, **options):
        """Compare public counts with independent literal expectations."""
        result = count_text(text, **options)
        self.assertEqual(result.lines, lines)
        self.assertEqual(result.words, words)
        self.assertIs(type(result.lines), int)
        self.assertIs(type(result.words), int)

    def test_spec_counting_table(self):
        cases = [
            ("", 0, 0), ("alpha beta", 1, 2), ("alpha\n", 1, 1),
            ("\n", 1, 0), ("alpha\r\nbeta\rgamma\n", 3, 3),
            ("alpha\n\n", 2, 1), (" \t", 1, 0),
            ("alpha\u2028beta", 1, 2),
        ]
        for text, lines, words in cases:
            with self.subTest(text=text):
                self.assert_counts(text, lines, words)

    def test_cr_lf_crlf_and_trailing_segments(self):
        cases = [
            ("\r", 1, 0), ("\r\n", 1, 0), ("a\rb", 2, 2),
            ("a\r\nb", 2, 2), ("\r\n\r\n", 2, 0),
            ("a\r\nb\rc\nd", 4, 4), ("a\n\r", 2, 1),
            ("\r\n\r\nend", 3, 1),
        ]
        for text, lines, words in cases:
            with self.subTest(text=text):
                self.assert_counts(text, lines, words)

    def test_unicode_whitespace_does_not_create_lines(self):
        self.assert_counts("café\u00a0猫\u2003dog\u2029fin", 1, 4)
        self.assert_counts("a\vb\fc\x85d\u2028e", 1, 5)
        self.assert_counts("\u2028\u2029\u00a0", 1, 0)

    def test_default_removes_one_leading_bom(self):
        self.assert_counts("\ufeff", 0, 0)
        self.assert_counts("\ufeffalpha beta\n", 1, 2)
        self.assert_counts("\ufeff\ufeff", 1, 1)
        self.assert_counts("\ufeff\n", 1, 0)

    def test_keep_bom_treats_bom_as_non_whitespace(self):
        self.assert_counts("\ufeff", 1, 1, strip_bom=False)
        self.assert_counts("\ufeff alpha\n", 1, 2, strip_bom=False)
        self.assert_counts("", 0, 0, strip_bom=False)

    def test_interior_bom_is_preserved_in_both_modes(self):
        for strip_bom in (True, False):
            with self.subTest(strip_bom=strip_bom):
                self.assert_counts("alpha \ufeff beta", 1, 3, strip_bom=strip_bom)
                self.assert_counts(" \ufeff", 1, 1, strip_bom=strip_bom)
