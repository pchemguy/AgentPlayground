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
