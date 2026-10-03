import sys,json,subprocess,hashlib,re
from pathlib import Path
sys.path.insert(0,'/workspace/scratch/AgentPlayground-evidence-008')
from tests.workflows.task_ownership import check_ownership
r=Path('/workspace/scratch/AgentPlayground-sdd-008');o=Path('/workspace/scratch/acceptance-out-008')
def git(*a):return subprocess.check_output(['git',*a],cwd=r,text=True).strip()
b=json.loads((o/'A-010-baseline.json').read_text());head=git('rev-parse','HEAD')
assert git('branch','--show-current')=='phase/2-output-and-input-extensions'
parents=git('rev-list','--parents','-n','1',head).split()[1:];assert len(parents)==2 and parents[0]==b['phase2']
feature=git('rev-parse','feature/002_8a53078-line-ranges');assert parents[1]==feature
assert git('rev-parse','main')==b['main'];assert not git('status','--porcelain','--untracked-files=no')
for branch,expected in [('main',b['main']),('phase/2-output-and-input-extensions',head),('feature/002_8a53078-line-ranges',feature)]:assert git('ls-remote','origin','refs/heads/'+branch).split()[0]==expected
owners=check_ownership(r/'docs/dev')['owners'];assert len(owners)==11
for task,row in owners.items():
 assert Path(row['document']).name=='TASKS.md'
 assert row['status']==('Unchecked' if task in {'T-007','T-008'} else 'Checked')
tasks=(r/'docs/dev/TASKS.md').read_text();assert re.search(r'\[ \] Phase 2',tasks)
archive=r/'docs/dev/features/002_8a53078'
names=['FEATURE_DECOMPOSITION.md','FEATURE-SPEC.md','FEATURE-PLAN.md','FEATURE-TASKS.md']
for name in names:assert (archive/name).exists() and not (r/'docs/dev'/name).exists()
links=0
for p in (r/'docs/dev').rglob('*.md'):
 for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',p.read_text()):
  target=target.split('#',1)[0]
  if target and ':' not in target:
   assert (p.parent/target).exists(),(str(p),target);links+=1
prov=json.loads((r/'vendor/PROVENANCE.json').read_text())
for p,h in prov['hashes'].items():assert hashlib.sha256((r/'vendor/sdd-manager'/p).read_bytes()).hexdigest()==h
for p,h in b['bytecode_hashes'].items():assert hashlib.sha256((r/p).read_bytes()).hexdigest()==h
baseline=json.loads((o/'A-010-host-baseline.json').read_text())['rows'];host=json.loads((o/'A-010-host-independent.json').read_text())['rows'];by={x['task']:x for x in host};assert len(by)==11
for t in ['T-009','T-010','T-011']:
 x=by[t];assert x['state']=='closed' and x['state_reason']=='completed' and len(x['comment_ids'])==1
for old in baseline:
 new=by[old['task']];assert new['number']==old['number'] and new['foreign_body_sha256']==old['foreign_body_sha256'];assert set(old['labels'])<=set(new['labels'])
 if old['task'] in {'T-007','T-008'}:assert new['state']=='open' and new['comments_count']==0
 elif old['task'] in {'T-001','T-002','T-003','T-004','T-005','T-006'}:assert new['state']=='closed' and new['comments_count']==old['comments_count']
data={'head':head,'parents':parents,'feature_tip':feature,'main_unchanged':b['main'],'exact_remote_refs':True,'tracked_clean':True,'task_owners':owners,'Phase2_unchecked_stdin_unstarted':True,'archived_sources':names,'local_links_checked':links,'pinned_hashes_verified':len(prov['hashes']),'bytecode_hashes_preserved':len(b['bytecode_hashes']),'hosted_task_IDs_preserved':True,'foreign_hosted_body_hashes_preserved':True,'unique_feature_closures':True}
(o/'A-010-boundaries.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({k:v for k,v in data.items() if k!='task_owners'},indent=2))
