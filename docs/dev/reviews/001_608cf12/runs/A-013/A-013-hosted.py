"""Reconcile authorized existing hosted identities through the protected adapter."""
import json
import subprocess
from pathlib import Path

ROOT = Path('/workspace/scratch/AgentPlayground-sdd-008')
OUT = Path('/workspace/scratch/acceptance-out-008')
PREFIX = '/repos/pchemguy/AgentPlayground/'
LOG = OUT / 'A-013-hosted-actions.jsonl'

def request(method, endpoint, payload=None):
    args = ['python', 'tools/github_api.py', method, PREFIX + endpoint, '--token-file', 'gh.tkn']
    if payload is not None:
        args += ['--body-file', '-']
    result = subprocess.run(args, cwd=ROOT, input=None if payload is None else json.dumps(payload),
                            text=True, capture_output=True, timeout=40)
    response = json.loads(result.stdout)
    status = response['status']
    with LOG.open('a') as log:
        log.write(json.dumps({'method': method, 'endpoint': endpoint, 'status': status}) + '\n')
    if status is None or not 200 <= status < 300:
        raise RuntimeError(f'{method} {endpoint}: status {status}; no raw response retained')
    return response['body']

def complete(number, task, commit, evidence):
    issue = request('GET', f'issues/{number}')
    marker = f'sdd-forge:task-id={task}'
    assert issue['title'].startswith(f'[{task}]') and marker in issue['body']
    comments = request('GET', f'issues/{number}/comments?per_page=100')
    note = f'{task} verified on phase/2-output-and-input-extensions at {commit}.\n\n{evidence}'
    if not any(commit in comment['body'] for comment in comments):
        request('POST', f'issues/{number}/comments', {'body': note})
    body = issue['body'].replace('T-007/T-008 remain planned; no stdin execution is claimed.',
                               f'{task} implemented and verified; task commit {commit}. Integration/publication is tracked separately.')
    patch = {}
    if body != issue['body']:
        patch['body'] = body
    if issue['state'] != 'closed' or issue.get('state_reason') != 'completed':
        patch.update(state='closed', state_reason='completed')
    if patch:
        request('PATCH', f'issues/{number}', patch)
    final = request('GET', f'issues/{number}')
    assert final['state'] == 'closed'
    (OUT / f'A-013-issue-{number}-safe.json').write_text(json.dumps({
        key: final.get(key) for key in ['number', 'title', 'body', 'state', 'state_reason', 'html_url', 'milestone', 'labels']}, indent=2))
    print(f'{task} existing issue #{number}: verified closed; evidence commit {commit}')

if __name__ == '__main__':
    complete(7, 'T-007', '917f3d9889a67bede8850d9f8cc8a98bef08516e',
             'Actual test-first RED: 7 tests, 54 behavioral failures before production changes. Final CLI GREEN: 28 tests; full discovery: 46 tests, no skips. Binary UTF-8 subprocesses cover locale/BOM/ranges/full decoding; controlled short reads through EOF, late read failure and caller stream lifetime pass. Named-file/API/distribution regressions pass. T-008 phase exit verification remains pending.')
