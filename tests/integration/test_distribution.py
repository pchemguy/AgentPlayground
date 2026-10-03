"""Verify the documented source archive and deployment outside the checkout.

The test environment deliberately removes PYTHONPATH and checks the imported
package location so the installed source cannot silently use checkout modules.
"""

import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[2]


class SourceDistributionTests(unittest.TestCase):
    """Exercise archive contents, independent imports, CLI and README examples."""

    def test_documented_archive_deploys_only_product_sources(self):
        readme = (PROJECT_ROOT / "README.md").read_text()
        scripts = re.findall(r"```python\n(.*?)```", readme, re.S)
        recipe = next(script for script in scripts if 'tarfile.open' in script)
        environment = os.environ.copy()
        environment.pop("PYTHONPATH", None)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, deployed = root / "source", root / "deployed"
            source.mkdir()
            deployed.mkdir()
            shutil.copytree(PROJECT_ROOT / "textstats", source / "textstats")
            shutil.copy(PROJECT_ROOT / "README.md", source / "README.md")
            # Deliberate excluded inputs detect over-broad archive recipes.
            (source / "gh.tkn").write_text("synthetic-not-a-credential")
            (source / "vendor").mkdir()
            (source / "vendor" / "unrelated.txt").write_text("infrastructure")
            recipe_result = subprocess.run([sys.executable, "-c", recipe], cwd=source,
                env=environment, capture_output=True, text=True, timeout=10)
            self.assertEqual(recipe_result.returncode, 0, recipe_result.stderr)
            with tarfile.open(source / "TextStats.tar.gz") as archive:
                self.assertEqual(set(archive.getnames()), {
                    "README.md", "textstats/__init__.py", "textstats/__main__.py",
                    "textstats/cli.py", "textstats/counting.py", "textstats/files.py"})
                archive.extractall(deployed, filter="data")
            fixture = deployed / "sample.txt"
            fixture.write_bytes(b"alpha beta\n")
            api_script = scripts[0] + "\nimport textstats\nfrom pathlib import Path\nassert Path(textstats.__file__).resolve().parent == Path.cwd() / 'textstats'\n"
            api = subprocess.run([sys.executable, "-c", api_script], cwd=deployed,
                env=environment, capture_output=True, text=True, timeout=10)
            self.assertEqual((api.returncode, api.stdout, api.stderr), (0, "", ""))
            cases = [
                (b"", [], 0, "lines=0 words=0\n"),
                ("\ufeff alpha\r\nbeta\n".encode(), [], 0, "lines=2 words=2\n"),
                ("\ufeff alpha\r\nbeta\n".encode(), ["--keep-bom"], 0, "lines=2 words=3\n"),
                ("café\u00a0猫\r\nthird\rfourth\n".encode(), [], 0, "lines=3 words=4\n"),
                (b"valid\n\xff", [], 1, ""),
            ]
            for data, options, status, output in cases:
                fixture.write_bytes(data)
                with self.subTest(data=data, options=options):
                    result = subprocess.run([sys.executable, "-m", "textstats", *options, "sample.txt"],
                        cwd=deployed, env=environment, capture_output=True, text=True, timeout=10)
                    self.assertEqual(result.returncode, status, result.stderr)
                    self.assertEqual(result.stdout, output)
                    if status == 0:
                        self.assertEqual(result.stderr, "")
                    else:
                        self.assertIn("sample.txt", result.stderr)
                        self.assertNotIn("Traceback", result.stderr)
                    self.assertEqual(fixture.read_bytes(), data)
            selected_cases = [
                ("alpha beta\nbeta\nlast two", "1:1", False, (1, 2)),
                ("alpha beta\nbeta\nlast two", "2:3", False, (2, 3)),
                ("alpha beta\nbeta\nlast two", "2:99", False, (2, 3)),
                ("alpha beta\nbeta\nlast two", "4:99", False, (0, 0)),
                ("", "1:3", False, (0, 0)),
                ("a\r\nb c\rd\n", "2:3", False, (2, 3)),
                ("a\n\n", "2:9", False, (1, 0)),
                ("\ufeff", "1:1", False, (0, 0)),
                ("\ufeff", "1:1", True, (1, 1)),
                ("a\n\ufeff b", "2:2", False, (1, 2)),
                ("\ufeff a\nb", "2:2", True, (1, 1)),
            ]
            for text, span, keep, expected in selected_cases:
                data = text.encode("utf-8")
                fixture.write_bytes(data)
                options = ["--lines", span]
                if keep:
                    options += ["--keep-bom"]
                with self.subTest(deployed_range=span, text=text, keep=keep):
                    result = subprocess.run([sys.executable, "-m", "textstats", *options, "sample.txt"],
                        cwd=deployed, env=environment, capture_output=True, text=True, timeout=10)
                    self.assertEqual((result.returncode, result.stderr), (0, ""))
                    self.assertEqual(result.stdout, "lines=%d words=%d\n" % expected)
                    self.assertEqual(fixture.read_bytes(), data)
            fixture.write_bytes(b"valid\n\xff")
            for options in [["--lines=1:1"], ["--lines=1:1", "--keep-bom"]]:
                failure = subprocess.run([sys.executable, "-m", "textstats", *options, "sample.txt"],
                    cwd=deployed, env=environment, capture_output=True, text=True, timeout=10)
                self.assertEqual((failure.returncode, failure.stdout), (1, ""))
                self.assertIn("sample.txt", failure.stderr)
                self.assertNotIn("Traceback", failure.stderr)
            # Execute the documented selected named-file shell block verbatim.
            selected_script = re.search(r"## Selected named-file lines.*?```sh\n(.*?)```", readme, re.S).group(1)
            documented = subprocess.run(selected_script, shell=True, cwd=deployed,
                env=environment, capture_output=True, text=True, timeout=10)
            self.assertEqual((documented.returncode, documented.stderr), (0, ""))
            self.assertEqual(documented.stdout, 'lines=1 words=2\nlines=2 words=3\nlines=2 words=3\nlines=0 words=0\n')
            help_result = subprocess.run([sys.executable, "-m", "textstats", "--help"],
                cwd=deployed, env=environment, capture_output=True, text=True, timeout=10)
            self.assertEqual(help_result.returncode, 0)
            self.assertTrue(help_result.stdout)
            self.assertNotIn("--json", help_result.stdout)
            removed = subprocess.run([sys.executable, "-m", "textstats", "--json", "sample.txt"],
                cwd=deployed, env=environment, capture_output=True, text=True, timeout=10)
            self.assertEqual((removed.returncode, removed.stdout), (2, ""))
            self.assertIn("unrecognized arguments: --json", removed.stderr)
            self.assertNotIn("Traceback", removed.stderr)
            self.assertEqual(help_result.stderr, "")
