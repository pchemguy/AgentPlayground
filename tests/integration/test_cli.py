"""Verify binary stdin and named files through the public module CLI."""

import os
import io
from types import SimpleNamespace
from unittest.mock import patch
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

    def test_literal_dash_file_uses_explicit_relative_path(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "-").write_bytes(b"named input\n")
            self.assert_success(self.run_cli("./-", cwd=directory), "lines=1 words=2\n")


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


class RemovedJsonCliTests(unittest.TestCase):
    """Reject the removed option before acquisition and preserve literal paths."""

    run_cli = NamedFileCliTests.run_cli
    assert_success = NamedFileCliTests.assert_success
    assert_failure = CliFailureTests.assert_failure

    def test_removed_option_precedes_source_acquisition(self):
        with tempfile.TemporaryDirectory() as directory:
            existing = Path(directory) / "bom.txt"
            existing.write_bytes("\ufeff a\nb".encode("utf-8"))
            missing = Path(directory) / "missing.txt"
            for path in [existing, missing, Path(directory)]:
                for options in [("--json",), ("--keep-bom", "--json"),
                                ("--lines=1:1", "--json"),
                                ("--json", "--lines", "2:2", "--keep-bom")]:
                    with self.subTest(path=path, options=options):
                        result = self.run_cli(path, *options)
                        self.assert_failure(result, 2)
                        self.assertIn("unrecognized arguments: --json", result.stderr)
            self.assertEqual(existing.read_bytes(), "\ufeff a\nb".encode("utf-8"))

    def test_help_omits_removed_option(self):
        result = self.run_cli("unused", "--help")
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertNotIn("--json", result.stdout)
        self.assertIn("--lines", result.stdout)
        self.assertIn("--keep-bom", result.stdout)

    def test_removed_option_name_is_a_literal_file_after_separator(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "--json").write_bytes(b"a\nb c")
            self.assert_success(self.run_cli("--json", "--", cwd=directory),
                                "lines=2 words=3\n")
            self.assert_success(self.run_cli("--json", "--lines=2:2", "--", cwd=directory),
                                "lines=1 words=2\n")


class LineRangeCliTests(NamedFileCliTests):
    """Verify inclusive selected counting, parser failures and complete decoding."""

    def test_literal_selected_cases_in_plain_output_and_bom_modes(self):
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
                options = ["--lines=" + span]
                if keep:
                    options += ["--keep-bom"]
                with self.subTest(text=text, span=span, keep=keep):
                    self.assert_success(self.run_cli(path, *options),
                                        "lines=%d words=%d\n" % expected)
                    self.assertEqual(path.read_bytes(), data)
            path.write_bytes(b"a\nb")
            self.assert_success(self.run_cli(path, "--lines", "1:"+"9"*5000), "lines=2 words=2\n")
            for options in [("--keep-bom", "--lines", "2:2"),
                            ("--lines", "2:2", "--keep-bom")]:
                self.assert_success(self.run_cli(path, *options), "lines=1 words=1\n")

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
                for options in [("--lines=1:1",), ("--lines=2:2",)]:
                    result = self.run_cli(path, *options)
                    self.assertEqual((result.returncode, result.stdout), (1, ""))
                    self.assertIn(str(path), result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
                    self.assertEqual(path.read_bytes(), data)
            for name in ["-", "-range.txt"]:
                (Path(directory) / name).write_bytes(b"a\nb c")
                self.assert_success(self.run_cli("./-" if name == "-" else name, "--lines=2:2", "--", cwd=directory),
                                    "lines=1 words=2\n")
            help_result = self.run_cli(path, "--help")
            self.assertEqual((help_result.returncode, help_result.stderr), (0, ""))
            self.assertIn("inclusive", help_result.stdout)
            self.assertIn("one-based", help_result.stdout)


class StdinCliTests(unittest.TestCase):
    """Protect source-independent counts, strict binary input and ownership."""

    def run_binary(self, data, *options, environment=None):
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        if environment:
            env.update(environment)
        return subprocess.run([sys.executable, "-m", "textstats", *options, "-"],
            cwd=PROJECT_ROOT, input=data, capture_output=True, env=env, timeout=10)

    def test_binary_whole_input_and_bom_modes(self):
        cases = [
            (b"", (), b"lines=0 words=0\n"),
            (b"alpha beta", (), b"lines=1 words=2\n"),
            (b"a\r\nb c\rd\n", (), b"lines=3 words=4\n"),
            ("café\u00a0猫\u2028dog\n".encode(), (), b"lines=1 words=3\n"),
            ("\ufeff".encode(), (), b"lines=0 words=0\n"),
            ("\ufeff".encode(), ("--keep-bom",), b"lines=1 words=1\n"),
            ("\ufeff a\nb".encode(), (), b"lines=2 words=2\n"),
            ("\ufeff a\nb".encode(), ("--keep-bom",), b"lines=2 words=3\n"),
        ]
        for data, options, output in cases:
            with self.subTest(data=data, options=options):
                result = self.run_binary(data, *options)
                self.assertEqual((result.returncode, result.stdout, result.stderr), (0, output, b""))

    def test_selected_binary_input_matches_literal_contract(self):
        cases = [
            ("alpha beta\nbeta\nlast two", "1:1", (1, 2)),
            ("alpha beta\nbeta\nlast two", "2:3", (2, 3)),
            ("alpha beta\nbeta\nlast two", "2:99", (2, 3)),
            ("alpha beta\nbeta\nlast two", "4:99", (0, 0)),
            ("", "1:3", (0, 0)), ("a\n\n", "2:9", (1, 0)),
            ("a\r\nb c\rd\n", "2:3", (2, 3)),
            ("a\u2028b\nc", "1:1", (1, 2)),
            ("a\n\ufeff b", "2:2", (1, 2)),
            ("\ufeff a\nb", "2:2", (1, 1)),
            ("\ufeff\ufeff", "1:1", (1, 1)),
        ]
        for text, span, counts in cases:
            for options in [("--lines", span), ("--keep-bom", "--lines=" + span),
                            ("--lines", span, "--keep-bom")]:
                with self.subTest(text=text, options=options):
                    result = self.run_binary(text.encode(), *options)
                    self.assertEqual((result.returncode, result.stdout, result.stderr),
                        (0, ("lines=%d words=%d\n" % counts).encode(), b""))
        for options, output in [((), b"lines=0 words=0\n"),
                                (("--keep-bom",), b"lines=1 words=1\n")]:
            result = self.run_binary("\ufeff".encode(), "--lines", "1:1", *options)
            self.assertEqual((result.returncode, result.stdout, result.stderr), (0, output, b""))

    def test_utf8_is_independent_of_process_text_encoding(self):
        env = {"LC_ALL": "C", "PYTHONUTF8": "0", "PYTHONCOERCECLOCALE": "0",
               "PYTHONIOENCODING": "ascii:strict"}
        result = self.run_binary("café 猫\n".encode(), environment=env)
        self.assertEqual((result.returncode, result.stdout, result.stderr),
                         (0, b"lines=1 words=2\n", b""))

    def test_full_decode_errors_before_and_after_selection(self):
        for data in [b"\xff\nvalid", b"valid\n\xff", b"valid\n\xc3"]:
            for options in [(), ("--lines", "1:1"), ("--lines", "99:100", "--keep-bom")]:
                with self.subTest(data=data, options=options):
                    result = self.run_binary(data, *options)
                    self.assertEqual((result.returncode, result.stdout), (1, b""))
                    self.assertIn(b"stdin", result.stderr)
                    self.assertIn(b"utf-8", result.stderr)
                    self.assertNotIn(b"Traceback", result.stderr)

    def test_caller_stream_survives_success_and_decode_failure(self):
        from textstats.cli import main
        for data, status, output in [(b"a\nb c", 0, "lines=1 words=1\n"),
                                     (b"a\n\xff", 1, "")]:
            stream = io.BytesIO(data)
            stdout, stderr = io.StringIO(), io.StringIO()
            with patch("sys.stdin", SimpleNamespace(buffer=stream)), \
                 patch("sys.stdout", stdout), patch("sys.stderr", stderr):
                self.assertEqual(main(["--lines", "1:1", "-"]), status)
            self.assertFalse(stream.closed)
            self.assertEqual(stream.tell(), len(data))
            self.assertEqual(stdout.getvalue(), output)
            if status:
                self.assertIn("stdin", stderr.getvalue())
            else:
                self.assertEqual(stderr.getvalue(), "")
            stream.seek(0)
            self.assertEqual(stream.read(), data)
            stream.close()

    def test_short_reads_reach_eof_and_late_read_failure_is_not_partial_success(self):
        from textstats.cli import main

        class ChunkedStream(io.BytesIO):
            """Return short binary chunks and optionally fail after good input."""

            def __init__(self, fail=False):
                super().__init__(b"a\nb c")
                self.fail = fail
                self.eof_seen = False

            def read(self, size=-1):
                if self.tell() >= 2 and self.fail:
                    raise OSError("controlled stdin read failure")
                chunk = super().read(2)
                self.eof_seen |= not chunk
                return chunk

        for fail in [False, True]:
            stream = ChunkedStream(fail)
            stdout, stderr = io.StringIO(), io.StringIO()
            with patch("sys.stdin", SimpleNamespace(buffer=stream)), \
                 patch("sys.stdout", stdout), patch("sys.stderr", stderr):
                status = main(["--lines", "1:1", "-"])
            self.assertFalse(stream.closed)
            self.assertEqual(status, 1 if fail else 0)
            self.assertEqual(stdout.getvalue(), "" if fail else "lines=1 words=1\n")
            if fail:
                self.assertIn("stdin", stderr.getvalue())
                self.assertIn("controlled stdin read failure", stderr.getvalue())
                self.assertNotIn("Traceback", stderr.getvalue())
            else:
                self.assertTrue(stream.eof_seen)
                self.assertEqual(stream.tell(), 5)
                self.assertEqual(stderr.getvalue(), "")
            stream.close()

    def test_usage_precedes_stdin_acquisition(self):
        from textstats.cli import main

        class ForbiddenStream:
            """Fail if usage processing attempts input acquisition."""

            def read(self, size=-1):
                raise AssertionError("stdin acquired before validation")

        for options in [["--lines", "0:1", "-"], ["--lines", "1:1", "--lines", "2:2", "-"],
                        ["--json", "-"], ["--help"]]:
            stdout, stderr = io.StringIO(), io.StringIO()
            with patch("sys.stdin", SimpleNamespace(buffer=ForbiddenStream())), \
                 patch("sys.stdout", stdout), patch("sys.stderr", stderr):
                with self.assertRaises(SystemExit) as raised:
                    main(options)
            self.assertEqual(raised.exception.code, 0 if options == ["--help"] else 2)
