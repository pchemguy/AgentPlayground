"""Export actual isolated incorporation state; never make project edits."""
import subprocess,json,hashlib,sys,shutil
from pathlib import Path
r=Path('/workspace/scratch/sdd008-A-021-feature/repo');out=Path('/workspace/scratch/acceptance-out-008');d=out/('A-021-'+sys.argv[1]);d.mkdir(exist_ok=False)
def git(*a):return subprocess.check_output(['git',*a],cwd=r,text=True).strip()
state={name:git(*args) for name,args in {'head':['rev-parse','HEAD'],'branch':['branch','--show-current'],'refs':['show-ref'],'stages':['ls-files','--stage'],'status':['status','--porcelain'],'remote_refs':['ls-remote','origin','refs/heads/main','refs/heads/phase/2-output-and-input-extensions','refs/heads/feature/002_8a53078-line-ranges']}.items()}
for name,args in [('staged.patch',['diff','--cached','--binary']),('unstaged.patch',['diff','--binary'])]:(d/name).write_bytes(subprocess.check_output(['git',*args],cwd=r))
paths=set(git('diff','--name-only').splitlines())|set(git('diff','--cached','--name-only').splitlines());state['changed_paths']=sorted(paths);state['owned_hashes']={}
for path in sorted(paths):
 p=r/path
 if p.is_file():
  target=d/'owned'/path;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target);state['owned_hashes'][path]=hashlib.sha256(p.read_bytes()).hexdigest()
state['active_sources']=[p.name for p in sorted((r/'docs/dev').glob('FEATURE*'))];state['archive_paths']=[str(p.relative_to(r)) for p in sorted((r/'docs/dev/features/002_8a53078').rglob('*')) if p.is_file()];state['index_sha256']=hashlib.sha256((r/'.git/index').read_bytes()).hexdigest()
subprocess.run(['git','bundle','create',str(d/'refs.bundle'),'--branches'],cwd=r,check=True,capture_output=True)
(d/'state.json').write_text(json.dumps(state,indent=2)+'\n');print(json.dumps({k:state[k] for k in ['head','branch','status','changed_paths','active_sources','archive_paths']},indent=2))
