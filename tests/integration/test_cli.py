"""Verify the public module CLI through real named-file subprocesses."""

import json
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
        for arguments in ([], ["a", "b"], ["--unknown"], ["--json"]):
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


class JsonCliTests(unittest.TestCase):
    """Verify JSON serialization and its composition with existing CLI policy."""

    run_cli = NamedFileCliTests.run_cli
    assert_failure = CliFailureTests.assert_failure

    def assert_json_success(self, result, lines, words):
        """Require one object, exact keys, true integers and success channels."""
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertTrue(result.stdout.endswith("\n"))
        self.assertEqual(result.stdout.count("\n"), 1)
        value = json.loads(result.stdout)
        self.assertEqual(value, {"lines": lines, "words": words})
        self.assertEqual(set(value), {"lines", "words"})
        self.assertIs(type(value["lines"]), int)
        self.assertIs(type(value["words"]), int)

    def test_json_named_file_boundaries(self):
        cases = [
            ("", 0, 0),
            (" \t", 1, 0),
            ("alpha beta", 1, 2),
            ("alpha\r\nbeta\rgamma\n", 3, 3),
            ("café\u00a0猫\u2028dog\n", 1, 3),
            ("alpha\n\n", 2, 1),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "file with spaces.txt"
            for text, lines, words in cases:
                with self.subTest(text=text):
                    data = text.encode("utf-8")
                    path.write_bytes(data)
                    self.assert_json_success(self.run_cli(path, "--json"), lines, words)
                    self.assertEqual(path.read_bytes(), data)

    def test_json_bom_policy_and_option_order(self):
        cases = [
            ("\ufeff alpha\r\nbeta\n", (), 2, 2),
            ("\ufeff alpha\r\nbeta\n", ("--keep-bom",), 2, 3),
            ("\ufeff", (), 0, 0),
            ("\ufeff", ("--keep-bom",), 1, 1),
            ("alpha \ufeff beta", (), 1, 3),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bom.txt"
            for text, options, lines, words in cases:
                with self.subTest(text=text, options=options):
                    path.write_bytes(text.encode("utf-8"))
                    self.assert_json_success(self.run_cli(path, "--json", *options), lines, words)
                    if options:
                        self.assert_json_success(self.run_cli(path, *options, "--json"), lines, words)

    def test_json_read_and_decode_failure_channels(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.txt"
            bad = Path(directory) / "bad.txt"
            bad.write_bytes(b"alpha\n\xff")
            for path in (missing, bad, Path(directory)):
                with self.subTest(path=path):
                    self.assert_failure(self.run_cli(path, "--json"), 1, path.name)
            self.assertEqual(bad.read_bytes(), b"alpha\n\xff")

    def test_json_dash_prefixed_named_file(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "-sample.txt").write_bytes(b"alpha beta\n")
            self.assert_json_success(self.run_cli("-sample.txt", "--json", "--", cwd=directory), 1, 2)

    def test_json_permission_denial_translation(self):
        from unittest.mock import patch
        import contextlib
        import io
        from textstats.cli import main
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch("textstats.cli.count_file", side_effect=PermissionError("Permission denied")):
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                status = main(["--json", "denied.txt"])
        self.assertEqual(status, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("denied.txt", stderr.getvalue())
        self.assertIn("Permission denied", stderr.getvalue())


class LineRangeCliTests(NamedFileCliTests):
    """Verify inclusive selected counting, parser failures and complete decoding."""

    def test_literal_selected_cases_in_both_formats_and_bom_modes(self):
        cases = [
            ("alpha beta\nbeta\nlast two", "2:3", False, (2, 3)),
            ("alpha beta\nbeta\nlast two", "1:1", False, (1, 2)),
            ("alpha beta\nbeta\nlast two", "2:99", False, (2, 3)),
            ("alpha beta\nbeta\nlast two", "4:99", False, (0, 0)),
            ("", "1:3", False, (0, 0)),
            ("a\n\n", "2:9", False, (1, 0)),
            ("a\r\nb c\rd\n", "2:3", False, (2, 3)),
            ("a\u2028b\nc", "1:1", False, (1, 2)),
            ("\ufeff", "1:1", False, (0, 0)),
            ("\ufeff", "1:1", True, (1, 1)),
            ("\ufeff a\nb", "2:2", False, (1, 1)),
            ("\ufeff a\nb", "2:2", True, (1, 1)),
            ("a\n\ufeff b", "2:2", False, (1, 2)),
            ("\ufeff\ufeff", "1:1", False, (1, 1)),
            ("a\nb", "01:02", False, (2, 2)),
            ("a\nb", "2:2", False, (1, 1)),
            ("a\r\r", "2:9", False, (1, 0)),
            ("a\r\n\r\n", "2:9", False, (1, 0)),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "selected.txt"
            for text, span, keep, expected in cases:
                data = text.encode("utf-8")
                path.write_bytes(data)
                for use_json in [False, True]:
                    options = ["--lines=" + span]
                    if keep: options += ["--keep-bom"]
                    if use_json: options.insert(0, "--json")
                    with self.subTest(text=text, span=span, keep=keep, json=use_json):
                        result = self.run_cli(path, *options)
                        self.assertEqual((result.returncode, result.stderr), (0, ""))
                        if use_json:
                            parsed = json.loads(result.stdout)
                            self.assertEqual(parsed, dict(zip(["lines", "words"], expected)))
                            self.assertEqual({type(v) for v in parsed.values()}, {int})
                            self.assertTrue(result.stdout.endswith("\n"))
                        else:
                            self.assertEqual(result.stdout, "lines=%d words=%d\n" % expected)
                        self.assertEqual(path.read_bytes(), data)
            path.write_bytes(b"a\nb")
            self.assert_success(self.run_cli(path, "--lines", "1:"+"9"*5000), "lines=2 words=2\n")
            result = self.run_cli(path, "--keep-bom", "--lines", "2:2", "--json")
            self.assertEqual(json.loads(result.stdout), {"lines": 1, "words": 1})
            self.assertEqual((result.returncode, result.stderr), (0, ""))

    def test_invalid_ranges_precede_missing_input(self):
        ranges = ["0:1", "2:1", "-1:2", "1:", ":2", "1:2:3", "1.0:2",
                  "+1:2", " 1:2", "1:2 ", "١:٢", "１:２"]
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.txt"
            for span in ranges:
                with self.subTest(span=span):
                    result = self.run_cli(missing, "--lines="+span)
                    self.assertEqual((result.returncode, result.stdout), (2, ""))
                    self.assertTrue(result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
            for options in [("--lines",), ("--lines", "1:2", "--lines=1:1")]:
                result = self.run_cli(missing, *options)
                self.assertEqual((result.returncode, result.stdout), (2, ""))
                self.assertTrue(result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_decode_failure_outside_selection_and_named_dash_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.txt"
            for data in [b"valid\n\xff", b"\xff\nvalid"]:
                path.write_bytes(data)
                for options in [("--lines=1:1",), ("--json", "--lines=2:2")]:
                    result = self.run_cli(path, *options)
                    self.assertEqual((result.returncode, result.stdout), (1, ""))
                    self.assertIn(str(path), result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
                    self.assertEqual(path.read_bytes(), data)
            for name in ["-", "-range.txt"]:
                (Path(directory) / name).write_bytes(b"a\nb c")
                self.assert_success(self.run_cli(name, "--lines=2:2", "--", cwd=directory),
                                    "lines=1 words=2\n")
            help_result = self.run_cli(path, "--help")
            self.assertEqual((help_result.returncode, help_result.stderr), (0, ""))
            self.assertIn("inclusive", help_result.stdout)
            self.assertIn("one-based", help_result.stdout)
