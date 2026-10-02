"""Verify CLI assessor sensitivity with standalone synthetic subprocesses."""
import tempfile
from pathlib import Path
import unittest
from tests.workflows.product_acceptance import run


class AcceptanceSensitivity(unittest.TestCase):
    """Reject distinct wrong evidence without importing product code."""

    def check(self, source, case):
        """Run an actual synthetic module in a disposable source directory."""
        with tempfile.TemporaryDirectory() as folder:
            repo = Path(folder)
            (repo / 'textstats.py').write_text(source)
            return run(repo, [dict(name='fixture', input='alpha', **case)])[0]

    def test_correct_literal(self):
        self.assertEqual(self.check("print('lines=1 words=1')\n", {'stdout':'lines=1 words=1\n'})['mismatches'], [])

    def test_bad_stdout(self):
        self.assertIn('stdout', self.check("print('lines=2 words=1')\n", {'stdout':'lines=1 words=1\n'})['mismatches'])

    def test_json_bool_is_not_count(self):
        self.assertIn('json', self.check("print('{\"lines\":true,\"words\":1}')\n", {'json':{'lines':1,'words':1}})['mismatches'])

    def test_bad_exit_and_channels(self):
        result = self.check("print('incorrect success')\n", {'returncode':1,'stderr_nonempty':True})
        self.assertEqual(set(result['mismatches']), {'exit','stdout','diagnostic'})


if __name__ == '__main__':
    unittest.main()
