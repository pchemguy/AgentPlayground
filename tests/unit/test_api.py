"""Exercise the package facade and immutable public result as a caller."""

import contextlib
import io
import unittest

from textstats import TextStats, count_text


class PublicApiTests(unittest.TestCase):
    """Protect public imports, independent invocation results and silence."""

    def test_public_result_has_integer_counts(self):
        result = TextStats(lines=2, words=3)
        self.assertEqual((result.lines, result.words), (2, 3))
        self.assertIs(type(result.lines), int)
        self.assertIs(type(result.words), int)

    def test_result_is_immutable(self):
        result = count_text("alpha beta")
        for field in ("lines", "words"):
            with self.subTest(field=field):
                with self.assertRaises(AttributeError):
                    setattr(result, field, 9)
                with self.assertRaises(AttributeError):
                    delattr(result, field)
        self.assertEqual((result.lines, result.words), (1, 2))

    def test_public_calls_return_independent_values_without_output(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            first = count_text("alpha\nbeta")
            second = count_text("", strip_bom=False)
        self.assertIsInstance(first, TextStats)
        self.assertIsInstance(second, TextStats)
        self.assertIsNot(first, second)
        self.assertEqual((first.lines, first.words), (2, 2))
        self.assertEqual((second.lines, second.words), (0, 0))
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")
