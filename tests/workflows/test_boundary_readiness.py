"""Check controlled boundary adapter states with real Git references."""
import subprocess
import tempfile
from pathlib import Path
import unittest

ADAPTER = Path(__file__).with_name('boundary_readiness.py').resolve()


class ReadinessStates(unittest.TestCase):
    """Ensure ordinary checks and failed/restored merge readiness stay distinct."""

    def test_states(self):
        with tempfile.TemporaryDirectory() as folder:
            repo = Path(folder)
            def git(*args):
                return subprocess.check_output(['git',*args],cwd=repo,text=True,stderr=subprocess.DEVNULL).strip()
            git('init','-b','main')
            git('config','user.name','Fixture')
            git('config','user.email','fixture@example.invalid')
            git('commit','--allow-empty','-m','Fixture baseline')
            def check():
                return subprocess.run(['python',str(ADAPTER)],cwd=repo,capture_output=True,text=True)
            self.assertEqual(check().returncode,0)
            head = git('rev-parse','HEAD')
            (repo/'.git/MERGE_HEAD').write_text(head+'\n')
            failure = check()
            self.assertEqual(failure.returncode,1)
            self.assertIn('retain uncommitted merge',failure.stderr)
            (repo/'.git/controlled-boundary-ready').write_text('ready\n')
            self.assertEqual(check().returncode,0)
            self.assertEqual((repo/'.git/MERGE_HEAD').read_text(),head+'\n')


if __name__ == '__main__':
    unittest.main()
