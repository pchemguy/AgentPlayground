"""Run retained literal CLI cases using real named files or raw-byte stdin.

Independent oracle files supply expected counts, statuses and output channels.
No production module is imported. Results, including failures, are persisted.
"""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile


def check_case(repo, case, directory):
    """Execute one independently authored input and report all mismatches."""
    raw = bytes.fromhex(case['input_hex']) if 'input_hex' in case else case.get('input', '').encode('utf-8')
    source = case.get('source', 'file')
    argv = ['python', '-m', 'textstats', *case.get('flags', [])]
    if source == 'stdin':
        argv.append('-')
        stdin = raw
    elif source == 'missing':
        argv.append(str(directory / 'missing.txt'))
        stdin = None
    elif source == 'argv':
        argv.extend(case.get('args', []))
        stdin = None
    else:
        path = directory / (case['name'] + '.txt')
        path.write_bytes(raw)
        argv.append(str(path))
        stdin = None
    result = subprocess.run(argv, cwd=repo, input=stdin, capture_output=True, timeout=30)
    stdout = result.stdout.decode('utf-8', errors='replace')
    stderr = result.stderr.decode('utf-8', errors='replace')
    actual = dict(name=case['name'], argv=argv, returncode=result.returncode,
                  stdout=stdout, stderr=stderr, mismatches=[])
    if result.returncode != case.get('returncode', 0):
        actual['mismatches'].append('exit')
    if 'json' in case:
        try:
            parsed = json.loads(stdout)
            if parsed != case['json'] or not isinstance(parsed, dict) or any(type(v) is not int for v in parsed.values()) or not stdout.endswith('\n'):
                actual['mismatches'].append('json')
        except (ValueError, TypeError):
            actual['mismatches'].append('json')
    elif stdout != case.get('stdout', ''):
        actual['mismatches'].append('stdout')
    if case.get('stderr_nonempty'):
        if not stderr.strip() or 'Traceback' in stderr:
            actual['mismatches'].append('diagnostic')
    elif stderr != case.get('stderr', ''):
        actual['mismatches'].append('stderr')
    return actual


def run(repo, cases):
    """Keep assessor-owned fixtures outside the product tree."""
    with tempfile.TemporaryDirectory(prefix='textstats-assessor-') as path:
        return [check_case(repo, case, Path(path)) for case in cases]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repo', type=Path)
    parser.add_argument('oracle', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    result = run(args.repo, json.loads(args.oracle.read_text()))
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    raise SystemExit(any(case['mismatches'] for case in result))
