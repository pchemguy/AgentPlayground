"""Exercise independent checkers against valid and deliberately bad evidence."""

import copy
import sys
import tempfile
import unittest
from pathlib import Path

from tests.workflows.cli_expectations import run_expectation
from tests.workflows.git_snapshot import check_boundary
from tests.workflows.task_ownership import check_ownership
from tools.github_api import BASE, NoRedirect, build_request


class BoundaryTests(unittest.TestCase):
    """Verify merge ancestry, branch, scope and publication rejection paths."""

    def setUp(self):
        """Create independent literal evidence, never imported from product code."""
        self.snapshot = {"branch": "phase/1", "head": "c", "parents": ["a", "b"],
                         "status": [], "changed_paths": ["src/tool.py"],
                         "remote_heads": {"refs/heads/phase/1": "c"}}

    def check(self, snapshot):
        """Apply the fixed fixture contract to an arbitrary snapshot."""
        check_boundary(snapshot, "phase/1", "a", "b", ["src"], require_remote=True)

    def test_valid_snapshot(self):
        """Accept the exact literal boundary fixture."""
        self.check(self.snapshot)

    def test_bad_snapshots(self):
        """Reject one-parent merges, wrong parents, dirty state and escaped scope."""
        changes = {"parents": [["a"], ["b", "a"], ["a", "b", "d"]],
                   "branch": ["main"], "status": [["?? stray"]],
                   "changed_paths": [["src-other/tool.py"], ["vendor/plugin.py"]],
                   "remote_heads": [{"refs/heads/phase/1": "old"}]}
        for key, values in changes.items():
            for value in values:
                with self.subTest(key=key, value=value):
                    bad = copy.deepcopy(self.snapshot)
                    bad[key] = value
                    with self.assertRaises(AssertionError):
                        self.check(bad)


class OwnershipTests(unittest.TestCase):
    """Verify active owner uniqueness and archive/terminal-row exclusion."""

    def test_duplicate_and_archive(self):
        """Reject duplicate IDs in active feature work but ignore archived rows."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            table = "| ID | Status |\n| --- | --- |\n| T-001 | Pending |\n"
            (root / "TASKS.md").write_text(table)
            archive = root / "archive"
            archive.mkdir()
            (archive / "FEATURE-TASKS.md").write_text(table)
            self.assertEqual(set(check_ownership(root)["owners"]), {"T-001"})
            active = root / "feature"
            active.mkdir()
            (active / "FEATURE-TASKS.md").write_text(table)
            with self.assertRaisesRegex(AssertionError, "duplicate executable ID"):
                check_ownership(root)
            (active / "FEATURE-TASKS.md").write_text(table.replace("Pending", "Done"))
            self.assertEqual(set(check_ownership(root)["owners"]), {"T-001"})

    def test_duplicate_in_same_document(self):
        """Reject duplicate executable rows even in one document."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "TASKS.md").write_text("| ID | Status |\n| --- | --- |\n"
                                           "| X | Pending |\n| X | Active |\n")
            with self.assertRaises(AssertionError):
                check_ownership(root)

    def test_missing_or_ambiguous_tables(self):
        """Reject absent task documents and tables with no status field."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(AssertionError):
                check_ownership(root)
            (root / "TASKS.md").write_text("| ID | Name |\n| --- | --- |\n| X | Work |\n")
            with self.assertRaises(ValueError):
                check_ownership(root)


class LiteralCliTests(unittest.TestCase):
    """Run a synthetic process and independently compare its literal behavior."""

    def test_literal_success_and_failure(self):
        """Detect deliberately incorrect output and exit expectations."""
        expected = {"argv": [sys.executable, "-c", "print('literal')"],
                    "returncode": 0, "stdout": "literal\n", "stderr": ""}
        self.assertEqual(run_expectation(expected, ".")["mismatches"], [])
        bad = dict(expected, stdout="wrong\n", returncode=9)
        self.assertEqual(run_expectation(bad, ".")["mismatches"], ["returncode", "stdout"])


class ApiTests(unittest.TestCase):
    """Test protected API construction using synthetic credentials only."""

    def test_scoped_request(self):
        """Construct literal repository-scoped JSON with no token in its URL."""
        request = build_request("POST", "/repos/pchemguy/AgentPlayground/milestones",
                                "synthetic-test-token", {"title": "test"})
        self.assertEqual(request.full_url, BASE + "/repos/pchemguy/AgentPlayground/milestones")
        self.assertEqual(request.get_header("Authorization"), "Bearer synthetic-test-token")
        self.assertEqual(request.data, b'{"title": "test"}')
        self.assertNotIn("synthetic-test-token", request.full_url)
        self.assertIsNone(NoRedirect().redirect_request(None, None, 302, "", {}, "https://example.com"))

    def test_escape_rejected(self):
        """Reject other repositories and encoded or literal traversal attempts."""
        for endpoint in ["https://api.github.com/repos/pchemguy/AgentPlayground/issues",
                         "/repos/other/repo/issues", "/repos/pchemguy/AgentPlayground/../issues",
                         "/repos/pchemguy/AgentPlayground/%2e%2e/issues"]:
            with self.subTest(endpoint=endpoint), self.assertRaises(ValueError):
                build_request("GET", endpoint, "synthetic")


if __name__ == "__main__":
    unittest.main()
