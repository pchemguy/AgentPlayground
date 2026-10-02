"""Expose a controlled prospective-merge prerequisite to a consuming agent.

Only an uncommitted Git merge consults the fixture owner's readiness file.
Ordinary working-state verification stays unaffected. The file is experiment
state, not a credential, product behavior, or proof of task completion.
"""
from pathlib import Path
import subprocess
import sys


def main():
    """Report a real failed check until the experiment owner restores readiness."""
    merge = subprocess.run(['git','rev-parse','--verify','MERGE_HEAD'],capture_output=True)
    if merge.returncode:
        print('No prospective merge: controlled prerequisite not applicable')
        return 0
    path = Path(subprocess.check_output(['git','rev-parse','--git-path','controlled-boundary-ready'],text=True).strip())
    if not path.exists() or path.read_text().strip() != 'ready':
        print('Controlled prospective merged-state prerequisite unavailable; retain uncommitted merge',file=sys.stderr)
        return 1
    print('Controlled prospective merged-state prerequisite restored')
    return 0


if __name__ == '__main__':
    sys.exit(main())
