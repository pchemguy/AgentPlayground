import subprocess,json,re,hashlib,sys
from pathlib import Path
sys.path.insert(0,'/workspace/scratch/AgentPlayground-evidence-008')
from tests.workflows.task_ownership import check_ownership
r=Path('/workspace/scratch/AgentPlayground-sdd-008');o=Path('/workspace/scratch/acceptance-out-008')
def git(*a):return subprocess.check_output(['git',*a],cwd=r,text=True).strip()
b=json.loads((o/'A-009-baseline.json').read_text());head=git('rev-parse','HEAD')
assert git('branch','--show-current')==b['branch'] and head!=b['head']
assert not git('status','--porcelain','--untracked-files=no')
assert git('diff','--name-only',b['head'],head).splitlines()==['docs/dev/SPEC.md']
assert git('rev-parse','HEAD^')==b['head'] and len(git('rev-list','--parents','-n','1','HEAD').split())==2
for branch,expected in [(b['branch'],head),('main','29c27580db73cf128c42ddb9535e6d8f5c38ed39'),('phase/2-output-and-input-extensions','8a53078d0f734165075691dae0dbfa224a63446f')]:
 assert git('rev-parse',branch)==expected
 assert git('ls-remote','origin','refs/heads/'+branch).split()[0]==expected
current={}
for line in git('ls-tree','-r','HEAD').splitlines():
 meta,p=line.split('\t',1);current[p]=meta.split()[2]
assert set(current)==set(b['tracked_blobs'])
assert all(current[p]==h for p,h in b['tracked_blobs'].items() if p!='docs/dev/SPEC.md')
for p,h in b['bytecode_hashes'].items():assert hashlib.sha256((r/p).read_bytes()).hexdigest()==h
spec=(r/'docs/dev/SPEC.md').read_text();links=[]
for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',spec):
 target=target.split('#',1)[0]
 if target and ':' not in target:
  assert (r/'docs/dev'/target).exists();links.append(target)
prov=json.loads((r/'vendor/PROVENANCE.json').read_text())
for p,h in prov['hashes'].items():assert hashlib.sha256((r/'vendor/sdd-manager'/p).read_bytes()).hexdigest()==h
owners=check_ownership(r/'docs/dev')
result={'head':head,'baseline':b['head'],'branch':b['branch'],'only_SPEC_changed':True,'all_other_tracked_blobs_and_paths_preserved':True,'single_parent_checkpoint':True,'main_and_phase2_unchanged':True,'exact_remote_refs_verified':True,'tracked_clean':True,'bytecode_hashes_preserved':len(b['bytecode_hashes']),'pinned_hashes_verified':len(prov['hashes']),'valid_SPEC_links':links,'task_owners':owners,'feature_sources_retained':True,'implementation_and_task_status_unchanged':True}
(o/'A-009-independent.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='task_owners'},indent=2))
