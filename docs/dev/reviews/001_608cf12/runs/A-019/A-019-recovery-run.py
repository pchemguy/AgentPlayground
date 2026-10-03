import hashlib, json, os, pathlib, re, shutil, subprocess, tempfile
ROOT = pathlib.Path('/workspace/scratch/sdd008-A-019-boundary/repo')
OUT = pathlib.Path('/workspace/scratch/acceptance-out-008')
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', GIT_OPTIONAL_LOCKS='0')
LOG = OUT / 'A-019-recovery-commands.log'
def run(args, cwd=ROOT, expected=0):
    p = subprocess.run(args, cwd=cwd, env=ENV, capture_output=True, text=True)
    with LOG.open('a') as f:
        f.write(json.dumps({'args':args,'cwd':str(cwd),'environment_overrides':{'PYTHONDONTWRITEBYTECODE':'1','GIT_OPTIONAL_LOCKS':'0'},'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr})+'\n')
    print(json.dumps({'args':args,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr}))
    assert p.returncode == expected
    return p.stdout
def snapshot():
    return {'index':run(['git','ls-files','--stage']), 'tree':run(['git','write-tree']).strip(),
            'vendor':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'vendor/sdd-manager').rglob('*') if p.is_file()}}
def checks():
    run(['python','--version'])
    suite=run(['python','-m','unittest','discover','-s','tests','-v'])
    # unittest reports its collection count to stderr, captured above.
    readme=(ROOT/'README.md').read_text()
    shell=re.findall(r'```sh\n(.*?)```',readme,re.S)
    python=re.findall(r'```python\n(.*?)```',readme,re.S)
    with tempfile.TemporaryDirectory(prefix='A-019-recovery-') as d:
        source=pathlib.Path(d)
        shutil.copytree(ROOT/'textstats',source/'textstats')
        shutil.copy(ROOT/'README.md',source/'README.md')
        assert run(['bash','-e','-c',shell[0]],source)=='lines=1 words=2\n'
        for block in python: assert run(['python','-c',block],source)==''
        run(['bash','-e','-c',shell[1]],source)
    for target in re.findall(r'\]\(([^)]+)\)',readme):
        if '://' not in target: assert (ROOT/target.split('#')[0]).exists(),target
    for p in list((ROOT/'textstats').glob('*.py'))+list((ROOT/'tests').rglob('*.py')):
        import ast
        assert ast.get_docstring(ast.parse(p.read_text())),p
    assert 'Target-owned note: this isolated boundary preserves both accepted TextStats usage and this integration note.' in readme
    run(['git','diff','--cached','--check'])
    assert run(['git','ls-files','-u'])==''
    assert run(['git','diff'])==''
    run(['python','tools/controlled_boundary.py'])
if __name__=='__main__':
    run(['git','status','--porcelain=v2','--branch'])
    run(['git','remote','-v'])
    run(['git','rev-parse','HEAD','ORIG_HEAD','MERGE_HEAD','main','origin/main','phase/1-named-file-baseline','origin/phase/1-named-file-baseline'])
    run(['git','log','-8','--format=%H %s','phase/1-named-file-baseline'])
    run(['git','diff','--cached','--stat'])
    baseline=snapshot()
    (OUT/'A-019-recovery-baseline.json').write_text(json.dumps(baseline,indent=2)+'\n')
    checks()
    assert snapshot()==baseline
    print('Prospective checks passed; original index tree and pinned vendor hashes preserved.')
