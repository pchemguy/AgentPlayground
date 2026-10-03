from pathlib import Path
import subprocess,json,re,hashlib,sys,ast
sys.path.insert(0,'/workspace/scratch/AgentPlayground-evidence-008')
from tests.workflows.task_ownership import check_ownership
r=Path('/workspace/scratch/AgentPlayground-sdd-008');o=Path('/workspace/scratch/acceptance-out-008')
def git(*a):return subprocess.check_output(['git',*a],cwd=r,text=True).strip()
b=json.loads((o/'A-012-baseline.json').read_text());head=git('rev-parse','HEAD');assert git('branch','--show-current')=='main'
parents=git('rev-list','--parents','-n','1','HEAD').split()[1:];assert len(parents)==2 and parents[0]==b['main'];phase=git('rev-parse','phase/2-output-and-input-extensions');assert parents[1]==phase
assert not git('status','--porcelain','--untracked-files=no')
for branch,expected in [('main',head),('phase/2-output-and-input-extensions',phase)]:assert git('ls-remote','origin','refs/heads/'+branch).split()[0]==expected
start='1d11ae343bfb3a1dcd6c12431ad401ecba77bfa6';assert subprocess.run(['git','merge-base','--is-ancestor',start,phase],cwd=r).returncode==0
changed=git('diff','--name-only',start,'HEAD').splitlines()
for path in ['textstats/files.py','textstats/__init__.py','textstats/__main__.py']:
 assert git('rev-parse','HEAD:'+path)==b['tracked_blobs'][path]
for path in b['tracked_blobs']:
 if path.startswith('docs/dev/features/002_8a53078/') and Path(path).name!='README.md':assert git('rev-parse','HEAD:'+path)==b['tracked_blobs'][path]
class WithoutDocs(ast.NodeTransformer):
 def generic_visit(self,node):
  node=super().generic_visit(node)
  if isinstance(node,(ast.Module,ast.ClassDef,ast.FunctionDef,ast.AsyncFunctionDef)) and node.body and isinstance(node.body[0],ast.Expr) and isinstance(node.body[0].value,ast.Constant) and isinstance(node.body[0].value.value,str):node.body=node.body[1:]
  return node
def functional(source):return ast.dump(WithoutDocs().visit(ast.parse(source)),include_attributes=False)
oldcore=subprocess.check_output(['git','show',start+':textstats/counting.py'],cwd=r,text=True)
assert functional(oldcore)==functional((r/'textstats/counting.py').read_text())
assert not list((r/'docs/dev').glob('FEATURE*'))
owners=check_ownership(r/'docs/dev')['owners'];assert set(owners)==set(f'T-{i:03}' for i in range(1,12)) - {'T-006'};assert all(x['status']=='Checked' for x in owners.values())
tasks=(r/'docs/dev/TASKS.md').read_text();assert re.search(r'\[x\] Phase 2',tasks);assert not re.search(r'\[ \] (?:Phase|Milestone)',tasks);assert not re.search(r'Phase 3',tasks)
prov=json.loads((r/'vendor/PROVENANCE.json').read_text())
for p,h in prov['hashes'].items():assert hashlib.sha256((r/'vendor/sdd-manager'/p).read_bytes()).hexdigest()==h
for p,h in b['bytecode_hashes'].items():assert hashlib.sha256((r/p).read_bytes()).hexdigest()==h
before=json.loads((o/'A-012-host-independent.json').read_text())['rows'];after=json.loads((o/'A-013-host-independent-final.json').read_text())['rows'];by={x['task']:x for x in after};assert len(by)==11
for old in before:
 new=by[old['task']];assert new['number']==old['number'] and new['foreign_body_sha256']==old['foreign_body_sha256']
 if old['task'] in {'T-007','T-008'}:assert new['state']=='closed' and new['state_reason']=='completed' and new['comments_count']==2 and len(new['comment_ids'])==2 and any(new['comment_commits'][0]) and head in new['comment_commits'][1]
 else:
  assert all(new[k]==v for k,v in old.items())
result={'head':head,'parents':parents,'phase_tip':phase,'exact_remote_refs_verified':True,'tracked_clean':True,'changed_paths':changed,'historical_feature_sources_preserved':True,'public_API_file_modules_and_core_behavior_unchanged':True,'task_owners':owners,'Phase2_complete_no_Phase3':True,'pinned_hashes_verified':len(prov['hashes']),'bytecode_hashes_preserved':len(b['bytecode_hashes']),'hosted_IDs_foreign_bodies_history_preserved':True,'limits':'Behavior is separately checked by full suite and independent retained named-file/stdin/plain/range/JSON-rejection oracles. No complete native transcript.'}
(o/'A-013-boundaries.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='task_owners'},indent=2))
