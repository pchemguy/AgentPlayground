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


class SelectedCountingTests(unittest.TestCase):
    """Verify private source-independent selection with literal expectations."""

    def test_selected_logical_segments_and_original_bom_policy(self):
        from textstats import counting
        cases = [
            ("alpha beta\nbeta\nlast two", (2, 3), True, (2, 3)),
            ("alpha beta\nbeta\nlast two", (1, 1), True, (1, 2)),
            ("alpha beta\nbeta\nlast two", (2, 99), True, (2, 3)),
            ("alpha beta\nbeta\nlast two", (4, 99), True, (0, 0)),
            ("", (1, 3), True, (0, 0)),
            ("a\n\n", (2, 9), True, (1, 0)),
            ("a\r\nb c\rd\n", (2, 3), True, (2, 3)),
            ("a\u2028b\nc", (1, 1), True, (1, 2)),
            ("\ufeff", (1, 1), True, (0, 0)),
            ("\ufeff", (1, 1), False, (1, 1)),
            ("\ufeff a\nb", (2, 2), True, (1, 1)),
            ("\ufeff a\nb", (2, 2), False, (1, 1)),
            ("a\n\ufeff b", (2, 2), True, (1, 2)),
            ("\ufeff\ufeff", (1, 1), True, (1, 1)),
            ("a\r\r", (2, 9), True, (1, 0)),
            ("a\r\n\r\n", (2, 9), True, (1, 0)),
            ("a\nb", (2, 2), True, (1, 1)),
        ]
        for text, span, strip, expected in cases:
            with self.subTest(text=text, span=span, strip=strip):
                result = counting._count_selected(text, span, strip_bom=strip)
                self.assertEqual((result.lines, result.words), expected)
        for text in ["", "a\r\nb\n", "\ufeff\ufeff a", "a\n\ufeff b"]:
            for strip in [False, True]:
                self.assertEqual(counting._count_selected(text, (1, 999), strip_bom=strip),
                                 counting.count_text(text, strip_bom=strip))
