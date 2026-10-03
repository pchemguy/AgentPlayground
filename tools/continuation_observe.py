"""Retain read-only observations for the October six-case continuation.

This observer reports actual Git state, owned tasks and optional product tests;
case acceptance is a separate evaluator judgment. It never changes product Git
state, imports product code or publishes a pass merely because tests are green.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tests.workflows.git_snapshot import capture, git
from tests.workflows.product_acceptance import run


def observe(repo, suites, oracles):
    """Capture actual state and preserve complete independently run results."""
    state = capture(repo)
    state['tracked_status'] = git(repo, 'status', '--porcelain', '--untracked-files=no').splitlines()
    state['main'] = git(repo, 'rev-parse', 'origin/main')
    state['log'] = git(repo, 'log', '--all', '-12', '--format=%H %P %s').splitlines()
    state['product_hashes'] = {str(p.relative_to(repo)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in sorted((repo / 'textstats').glob('*.py'))}
    state['task_check'] = command([sys.executable, '-m', 'tests.workflows.task_ownership', str(repo / 'docs')], ROOT)
    state['suites'] = [command([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], repo)] if suites else []
    state['oracles'] = {str(p.resolve().relative_to(ROOT)): run(repo, json.loads(p.read_text())) for p in oracles}
    state['limits'] = 'Read-only observation is not a consumer action or autonomous pass decision. Tests create ordinary bytecode; credentials/raw provider bodies are excluded.'
    return state


def command(argv, cwd):
    """Record a complete command/result without shell interpolation."""
    result = subprocess.run(argv, cwd=cwd, text=True, capture_output=True, timeout=120)
    return {'argv': argv, 'cwd': str(cwd), 'returncode': result.returncode,
            'stdout': result.stdout, 'stderr': result.stderr}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repo', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--suite', action='store_true')
    parser.add_argument('--oracle', type=Path, action='append', default=[])
    args = parser.parse_args()
    state = observe(args.repo, args.suite, args.oracle)
    args.output.write_text(json.dumps(state, indent=2) + '\n')
    failures = state['task_check']['returncode'] or any(r['returncode'] for r in state['suites']) or any(c['mismatches'] for cases in state['oracles'].values() for c in cases)
    print(json.dumps({'head': state['head'], 'branch': state['branch'], 'tracked_status':state['tracked_status'], 'suite_exit':[r['returncode'] for r in state['suites']], 'oracle_cases':sum(map(len,state['oracles'].values())), 'errors':bool(failures)}))
    raise SystemExit(bool(failures))
