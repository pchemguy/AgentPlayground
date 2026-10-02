"""Capture scoped product work for interruption recovery without Git mutation."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import tarfile

repo = Path(sys.argv[1])
destination = Path(sys.argv[2])
destination.mkdir(parents=True,exist_ok=True)

def git(*args, binary=False):
    """Return read-only Git observations; fail on missing state."""
    output = subprocess.check_output(['git', *args], cwd=repo)
    return output if binary else output.decode().strip()

paths = set(git('diff', '--name-only').splitlines()) | set(git('diff', '--cached', '--name-only').splitlines()) | set(git('ls-files','--others','--exclude-standard').splitlines())
owned = sorted(p for p in paths if '__pycache__' not in p and (p in {'README.md','AGENTS.md','.gitignore'} or p.startswith(('textstats/','tests/','docs/dev/'))))
assert not any(p.endswith('.tkn') for p in owned)
records = []
secret = re.compile(rb'(?:github_pat_[A-Za-z0-9_]{30,}|ghp_[A-Za-z0-9]{30,})')
for name in owned:
    path = repo/name
    content = path.read_bytes() if path.is_file() else b''
    assert not secret.search(content), 'Sensitive content blocked from recovery export'
    records.append({'path':name,'exists':path.exists(),'sha256':hashlib.sha256(content).hexdigest() if path.exists() else None,'index':git('ls-files','--stage','--',name)})
for title,args in [('unstaged.diff',['diff','--binary']),('staged.diff',['diff','--cached','--binary'])]:
    data = git(*args,'--',*owned,binary=True) if owned else b''
    assert not secret.search(data)
    (destination/title).write_bytes(data)
with tarfile.open(destination/'pending-files.tar.gz','w:gz') as archive:
    for name in owned:
        if (repo/name).is_file():archive.add(repo/name,arcname=name,recursive=False)
subprocess.run(['git','bundle','create',str(destination/'checkpoint.bundle'),'HEAD'],cwd=repo,check=True,capture_output=True)
subprocess.run(['git','bundle','verify',str(destination/'checkpoint.bundle')],cwd=repo,check=True,capture_output=True)
(destination/'state.json').write_text(json.dumps({'repo':str(repo),'branch':git('branch','--show-current'),'head':git('rev-parse','HEAD'),'parents':git('show','--format=%P','--no-patch','HEAD').split(),'status':git('status','--porcelain').splitlines(),'owned_pending':records,'merge_pending':(repo/'.git/MERGE_HEAD').exists(),'scope':'Bytecode and unrelated paths omitted from content export; credentials excluded. No staging/reset/commit/checkout occurs.'},indent=2)+'\n')
print(json.dumps({'destination':str(destination),'head':git('rev-parse','HEAD'),'owned_pending':owned}))
