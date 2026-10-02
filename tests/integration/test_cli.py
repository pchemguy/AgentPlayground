"""Verify the public module CLI through real named-file subprocesses."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[2]


class NamedFileCliTests(unittest.TestCase):
    """Protect exact success output, BOM modes and unchanged named inputs."""

    def run_cli(self, path, *options, cwd=PROJECT_ROOT):
        """Launch the actual module while keeping verification bytecode-free."""
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment["PYTHONPATH"] = str(PROJECT_ROOT)
        return subprocess.run(
            [sys.executable, "-m", "textstats", *options, str(path)],
            cwd=cwd, env=environment, capture_output=True, text=True,
            encoding="utf-8", timeout=10, check=False,
        )

    def assert_success(self, result, expected_stdout):
        """Check all observable success channels with literal output."""
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, expected_stdout)
        self.assertEqual(result.stderr, "")

    def test_named_file_success_boundaries(self):
        cases = [
            ("", "lines=0 words=0\n"),
            ("alpha beta", "lines=1 words=2\n"),
            ("alpha\r\nbeta\rgamma\n", "lines=3 words=3\n"),
            ("café\u00a0猫\u2028dog\n", "lines=1 words=3\n"),
            ("alpha\n\n", "lines=2 words=1\n"),
            (" \t", "lines=1 words=0\n"),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            for text, output in cases:
                with self.subTest(text=text):
                    path.write_bytes(text.encode("utf-8"))
                    self.assert_success(self.run_cli(path), output)

    def test_keep_bom_composes_with_named_input(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bom.txt"
            path.write_bytes("\ufeff alpha\r\nbeta\n".encode("utf-8"))
            self.assert_success(self.run_cli(path), "lines=2 words=2\n")
            self.assert_success(self.run_cli(path, "--keep-bom"), "lines=2 words=3\n")

    def test_bom_only_and_interior_bom(self):
        cases = [
            ("\ufeff", (), "lines=0 words=0\n"),
            ("\ufeff", ("--keep-bom",), "lines=1 words=1\n"),
            ("alpha \ufeff beta", (), "lines=1 words=3\n"),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bom.txt"
            for text, options, output in cases:
                with self.subTest(text=text, options=options):
                    path.write_bytes(text.encode("utf-8"))
                    self.assert_success(self.run_cli(path, *options), output)

    def test_named_input_with_spaces_is_not_modified(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "file with spaces.txt"
            data = b"alpha beta\n"
            path.write_bytes(data)
            self.assert_success(self.run_cli(path), "lines=1 words=2\n")
            self.assertEqual(path.read_bytes(), data)

    def test_dash_is_a_named_file_before_stdin_delivery(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "-").write_bytes(b"named input\n")
            self.assert_success(self.run_cli("-", cwd=directory), "lines=1 words=2\n")


class CliFailureTests(unittest.TestCase):
    """Protect process failure/usage channels and useful diagnostics."""

    run_cli = NamedFileCliTests.run_cli
    assert_success = NamedFileCliTests.assert_success

    def assert_failure(self, result, status, name=None):
        self.assertEqual(result.returncode, status, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertTrue(result.stderr.strip())
        self.assertNotIn("Traceback", result.stderr)
        if name is not None:
            self.assertIn(name, result.stderr)

    def test_missing_and_invalid_utf8_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.txt"
            bad = Path(directory) / "invalid.txt"
            bad.write_bytes(b"valid\n\xff")
            for path in (missing, bad):
                with self.subTest(path=path.name):
                    self.assert_failure(self.run_cli(path), 1, path.name)
            self.assertEqual(bad.read_bytes(), b"valid\n\xff")

    def test_directory_cannot_be_read_as_file(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assert_failure(self.run_cli(directory), 1, directory)

    def test_usage_and_help(self):
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        for arguments in ([], ["a", "b"], ["--unknown"], ["--json", "a"]):
            with self.subTest(arguments=arguments):
                result = subprocess.run([sys.executable, "-m", "textstats", *arguments],
                    cwd=PROJECT_ROOT, env=environment, capture_output=True, text=True, timeout=10)
                self.assert_failure(result, 2)
        result = subprocess.run([sys.executable, "-m", "textstats", "--help"],
            cwd=PROJECT_ROOT, env=environment, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0)
        self.assertIn("INPUT", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_dash_prefixed_file_via_separator(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "-sample.txt").write_bytes(b"alpha beta\n")
            self.assert_success(self.run_cli("-sample.txt", "--", cwd=directory), "lines=1 words=2\n")

    def test_permission_denial_translation_in_process(self):
        from unittest.mock import patch
        import contextlib
        import io
        from textstats.cli import main
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch("textstats.cli.count_file", side_effect=PermissionError("Permission denied")):
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                status = main(["denied.txt"])
        self.assertEqual(status, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("denied.txt", stderr.getvalue())
        self.assertIn("Permission denied", stderr.getvalue())
