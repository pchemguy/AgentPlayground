"""Check the public file API with real UTF-8 fixtures and owned handles."""

import builtins
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from textstats import TextStats, count_file


class FileCountingTests(unittest.TestCase):
    """Verify decoding, BOM delegation and success-path resource ownership."""

    def test_real_files_match_fixed_expected_counts(self):
        cases = [
            (b"", 0, 0),
            ("alpha\r\nbeta\rgamma\n".encode("utf-8"), 3, 3),
            ("café\u00a0猫\u2028dog\n".encode("utf-8"), 1, 3),
            (b" \t\n\n", 2, 0),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            for data, lines, words in cases:
                path.write_bytes(data)
                for public_path in (path, str(path)):
                    with self.subTest(data=data, path_type=type(public_path)):
                        result = count_file(public_path)
                        self.assertIsInstance(result, TextStats)
                        self.assertEqual((result.lines, result.words), (lines, words))
                        self.assertEqual(path.read_bytes(), data)

    def test_bom_modes_are_applied_to_decoded_file(self):
        cases = [
            ("\ufeff", True, 0, 0), ("\ufeff", False, 1, 1),
            ("\ufeff alpha\r\nbeta\n", True, 2, 2),
            ("\ufeff alpha\r\nbeta\n", False, 2, 3),
            ("\ufeff\ufeff", True, 1, 1),
            ("alpha \ufeff beta", True, 1, 3),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bom.txt"
            for text, strip_bom, lines, words in cases:
                path.write_bytes(text.encode("utf-8"))
                with self.subTest(text=text, strip_bom=strip_bom):
                    result = count_file(path, strip_bom=strip_bom)
                    self.assertEqual((result.lines, result.words), (lines, words))

    def test_success_closes_real_owned_handle_without_output(self):
        handles = []

        def observe_open(*args, **kwargs):
            handle = builtins.open(*args, **kwargs)
            handles.append(handle)
            return handle

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_bytes(b"alpha beta\n")
            stdout, stderr = io.StringIO(), io.StringIO()
            with patch("textstats.files.open", side_effect=observe_open, create=True):
                with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                    result = count_file(path)
            self.assertEqual((result.lines, result.words), (1, 2))
            self.assertTrue(handles, "The file adapter must acquire its own handle")
            self.assertTrue(all(handle.closed for handle in handles))
            self.assertEqual(stdout.getvalue(), "")
            self.assertEqual(stderr.getvalue(), "")


class FileFailureTests(unittest.TestCase):
    """Protect original exceptions and owned-handle cleanup on read failure."""

    def test_missing_file_preserves_oserror_without_output(self):
        with tempfile.TemporaryDirectory() as directory:
            stdout, stderr = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                with self.assertRaises(FileNotFoundError):
                    count_file(Path(directory) / "missing.txt")
            self.assertEqual((stdout.getvalue(), stderr.getvalue()), ("", ""))

    def test_decode_failure_closes_real_handle_and_preserves_bytes(self):
        handles = []
        def observe_open(*args, **kwargs):
            handle = builtins.open(*args, **kwargs)
            handles.append(handle)
            return handle
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.txt"
            path.write_bytes(b"valid prefix\n\xff")
            with patch("textstats.files.open", side_effect=observe_open, create=True):
                with self.assertRaises(UnicodeDecodeError):
                    count_file(path)
            self.assertTrue(handles)
            self.assertTrue(all(handle.closed for handle in handles))
            self.assertEqual(path.read_bytes(), b"valid prefix\n\xff")

    def test_read_denial_closes_acquired_handle_and_preserves_exception(self):
        class DeniedReader(io.StringIO):
            def read(self, *args, **kwargs):
                raise PermissionError("controlled read denial")
        handle = DeniedReader("partial data")
        with patch("textstats.files.open", return_value=handle, create=True):
            with self.assertRaises(PermissionError):
                count_file("denied.txt")
        self.assertTrue(handle.closed)
