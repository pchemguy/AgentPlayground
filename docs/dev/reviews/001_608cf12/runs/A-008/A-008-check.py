from pathlib import Path
import subprocess, json, hashlib, re, sys
sys.path.insert(0,'/workspace/scratch/AgentPlayground-evidence-008')
from tests.workflows.task_ownership import check_ownership
r=Path('/workspace/scratch/AgentPlayground-sdd-008'); out=Path('/workspace/scratch/acceptance-out-008')
def git(*args): return subprocess.check_output(['git',*args],cwd=r,text=True).strip()
b=json.loads((out/'A-008-baseline-tree.json').read_text())
branch=git('branch','--show-current'); assert branch=='feature/002_8a53078-line-ranges'
head=git('rev-parse','HEAD'); assert head!=b['head']
assert git('rev-parse','main')==b['main']
assert git('rev-parse','phase/2-output-and-input-extensions')==b['head']
assert git('ls-remote','origin','refs/heads/'+branch).split()[0]==head
assert git('ls-remote','origin','refs/heads/main').split()[0]==b['main']
assert git('ls-remote','origin','refs/heads/phase/2-output-and-input-extensions').split()[0]==b['head']
assert not git('status','--porcelain','--untracked-files=no')
tree={}
for line in git('ls-tree','-r','HEAD').splitlines():
 meta,path=line.split('\t',1);tree[path]=meta.split()[2]
assert all(tree.get(p)==h for p,h in b['tracked_blobs'].items())
expected={'docs/dev/FEATURE_DECOMPOSITION.md','docs/dev/FEATURE-SPEC.md','docs/dev/FEATURE-PLAN.md','docs/dev/FEATURE-TASKS.md','docs/dev/features/002_8a53078/README.md'}
assert set(tree)-set(b['tracked_blobs'])==expected
links=[]
for p in expected:
 s=(r/p).read_text();assert s.startswith('# ')
 for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',s):
  target=target.split('#',1)[0]
  if target and ':' not in target:
   assert ((r/p).parent/target).exists(),(p,target);links.append([p,target])
owner=check_ownership(r/'docs/dev')
prov=json.loads((r/'vendor/PROVENANCE.json').read_text())
for p,h in prov['hashes'].items():
 assert hashlib.sha256((r/'vendor/sdd-manager'/p).read_bytes()).hexdigest()==h,p
spec=(r/'docs/dev/FEATURE-SPEC.md').read_text();plan=(r/'docs/dev/FEATURE-PLAN.md').read_text();tasks=(r/'docs/dev/FEATURE-TASKS.md').read_text()
assert re.findall(r'^\s*- \[ \] (T-\d+)\b',tasks,re.M)==['T-009','T-010','T-011']
assert not re.search(r'^\s*- \[[xX]\]',tasks,re.M)
assert '--lines START:END' in spec and 'START <= END' in spec
assert '37ff9bc' in git('log','--oneline',b['head']+'..HEAD')
data={'head':head,'branch':branch,'main_unchanged':b['main'],'phase2_unchanged':b['head'],'remote_equality':True,'tracked_clean':True,'all_existing_tracked_blobs_unchanged':True,'added_documents':sorted(expected),'active_links_checked':len(links),'task_ownership':owner,'pinned_hashes_verified':len(prov['hashes']),'all_feature_tasks_unchecked':True,'product_unimplemented':True,'semantic_review':'Named-file range contract covers positive inclusive bounds, beyond-EOF subset, whole-input UTF-8 and BOM ordering, text/JSON and invalid syntax. Main architecture/layout reused; active decomposition/spec/plan/tasks retained; future stdin compatibility separately owned and does not gate named-file delivery. No incorporation, archive, implementation or boundary.'}
(out/'A-008-independent.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k not in ['task_ownership','semantic_review']},indent=2))
