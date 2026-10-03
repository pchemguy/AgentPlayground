"""Create an isolated consumer clone and bare origin from an exact checkpoint.

No network, credential copying, hosted writes, or consumer actions occur here.
The destination must be absent. Each fork retains origin/main independently of
its working branch, so checks must not assume a local main reference exists.
"""
import argparse
from pathlib import Path
import subprocess


def git(root, *args):
    """Run fixture Git commands and reject any failed setup step."""
    return subprocess.run(['git', *args], cwd=root, check=True, text=True,
                          capture_output=True).stdout.strip()


def setup(source, destination, working, tip, main):
    """Reproduce branch histories without carrying source working files."""
    destination.mkdir(parents=True, exist_ok=False)
    remote = destination / 'remote.git'
    git(None, 'clone', '--bare', str(source), str(remote))
    git(remote, 'update-ref', 'refs/heads/main', main)
    git(remote, 'update-ref', 'refs/heads/' + working, tip)
    git(remote, 'symbolic-ref', 'HEAD', 'refs/heads/' + working)
    repo = destination / 'repo'
    git(None, 'clone', str(remote), str(repo))
    git(repo, 'config', 'user.name', 'Fixture')
    git(repo, 'config', 'user.email', 'fixture@example.invalid')
    return repo


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('destination', type=Path)
    parser.add_argument('working')
    parser.add_argument('tip')
    parser.add_argument('main')
    args = parser.parse_args()
    print(setup(args.source, args.destination, args.working, args.tip, args.main))
