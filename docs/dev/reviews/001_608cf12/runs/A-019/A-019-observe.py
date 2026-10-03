"""Retain actual merge state; never advance refs or infer consumer acceptance."""
from pathlib import Path
import subprocess,json,hashlib,sys
r=Path('/workspace/scratch/sdd008-A-019-boundary/repo');o=Path('/workspace/scratch/acceptance-out-008')/('A-019-'+sys.argv[1]);o.mkdir(exist_ok=False)
def git(*a):
 p=subprocess.run(['git',*a],cwd=r,capture_output=True);return {'returncode':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()}
state={k:git(*args) for k,args in {'head':['rev-parse','HEAD'],'branch':['branch','--show-current'],'merge_head':['rev-parse','--verify','MERGE_HEAD'],'refs':['show-ref'],'status':['status','--porcelain'],'stages':['ls-files','--stage'],'unmerged':['ls-files','--unmerged'],'remote_main':['ls-remote','origin','refs/heads/main'],'remote_phase':['ls-remote','origin','refs/heads/phase/1-named-file-baseline']}.items()}
for name,args in [('staged.patch',['diff','--cached','--binary']),('unstaged.patch',['diff','--binary'])]:
 p=subprocess.run(['git',*args],cwd=r,capture_output=True);(o/name).write_bytes(p.stdout)
(o/'README.md').write_bytes((r/'README.md').read_bytes())
state['README_sha256']=hashlib.sha256((r/'README.md').read_bytes()).hexdigest();state['index_sha256']=hashlib.sha256((r/'.git/index').read_bytes()).hexdigest()
stages={}
for line in state['stages']['stdout'].splitlines():
 meta,path=line.split('\t',1)
 if path=='README.md':
  mode,blob,stage=meta.split();data=subprocess.check_output(['git','cat-file','blob',blob],cwd=r);(o/f'README-stage-{stage}.md').write_bytes(data);stages[stage]={'mode':mode,'blob':blob,'sha256':hashlib.sha256(data).hexdigest()}
state['README_stages']=stages
for name in ['MERGE_HEAD','MERGE_MSG','MERGE_MODE']:
 p=r/'.git'/name
 if p.exists():(o/name).write_bytes(p.read_bytes())
ready=r/'.git/controlled-boundary-ready';state['readiness_present']=ready.exists();state['readiness_sha256']=hashlib.sha256(ready.read_bytes()).hexdigest() if ready.exists() else None
subprocess.run(['git','bundle','create',str(o/'refs.bundle'),'refs/heads/main','refs/heads/phase/1-named-file-baseline'],cwd=r,check=True,capture_output=True)
(o/'state.json').write_text(json.dumps(state,indent=2)+'\n');print(json.dumps({k:state[k] for k in ['head','branch','merge_head','status','unmerged','remote_main','remote_phase','README_sha256','README_stages','readiness_present']},indent=2))
