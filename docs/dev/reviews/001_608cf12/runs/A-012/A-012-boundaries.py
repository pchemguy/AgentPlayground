from pathlib import Path
import subprocess,json,re,hashlib,sys
sys.path.insert(0,'/workspace/scratch/AgentPlayground-evidence-008')
from tests.workflows.task_ownership import check_ownership
r=Path('/workspace/scratch/AgentPlayground-sdd-008');o=Path('/workspace/scratch/acceptance-out-008')
def git(*a):return subprocess.check_output(['git',*a],cwd=r,text=True).strip()
b=json.loads((o/'A-012-baseline.json').read_text());head=git('rev-parse','HEAD');assert git('branch','--show-current')==b['branch']
parents=git('rev-list','--parents','-n','1','HEAD').split()[1:];assert len(parents)==2 and parents[0]==b['head']
branches=git('for-each-ref','--format=%(refname:short) %(objectname)','refs/heads/revision').splitlines();matches=[line.split() for line in branches if line.split()[1]==parents[1]];assert len(matches)==1
amendment,tip=matches[0];identity=re.fullmatch(r'revision/(\d{3}_d0eeeff)-.+',amendment);assert identity
record=r/'docs/dev/reviews'/identity[1]/'REVISION-REPORT.md';assert record.exists() and b['head'] in record.read_text()
assert git('rev-parse','main')==b['main'];assert not git('status','--porcelain','--untracked-files=no')
for branch,expected in [('main',b['main']),(b['branch'],head),(amendment,tip)]:assert git('ls-remote','origin','refs/heads/'+branch).split()[0]==expected
changed=git('diff','--name-only',b['head'],'HEAD').splitlines()
for path in ['textstats/counting.py','textstats/files.py','textstats/__init__.py','textstats/__main__.py']:
 assert git('rev-parse','HEAD:'+path)==b['tracked_blobs'][path]
for path in b['tracked_blobs']:
 if path.startswith('docs/dev/features/002_8a53078/') and Path(path).name!='README.md':assert git('rev-parse','HEAD:'+path)==b['tracked_blobs'][path]
assert not list((r/'docs/dev').glob('FEATURE*'))
newdocs=[p for p in git('diff','--diff-filter=A','--name-only',b['head'],'HEAD').splitlines() if p.startswith('docs/')];assert newdocs==[str(record.relative_to(r))]
owners=check_ownership(r/'docs/dev')['owners'];assert set(owners)==set(f'T-{i:03}' for i in range(1,12)) - {'T-006'}
for task in ['T-001','T-002','T-003','T-004','T-005','T-009','T-010','T-011']:assert owners[task]['status']=='Checked'
for task in ['T-007','T-008']:assert owners[task]['status']=='Unchecked'
assert re.search(r'\[ \] Phase 2',(r/'docs/dev/TASKS.md').read_text())
prov=json.loads((r/'vendor/PROVENANCE.json').read_text())
for p,h in prov['hashes'].items():assert hashlib.sha256((r/'vendor/sdd-manager'/p).read_bytes()).hexdigest()==h
for p,h in b['bytecode_hashes'].items():assert hashlib.sha256((r/p).read_bytes()).hexdigest()==h
before=json.loads((o/'A-011-host-independent.json').read_text())['rows'];after=json.loads((o/'A-012-host-independent.json').read_text())['rows'];by={x['task']:x for x in after};assert len(by)==11
for old in before:
 new=by[old['task']];assert new['number']==old['number'] and new['foreign_body_sha256']==old['foreign_body_sha256'];assert new['state']==old['state']
 if old['task'] in {'T-007','T-008'}:assert new['comments_count']==0
result={'head':head,'parents':parents,'amendment_branch':amendment,'amendment_tip':tip,'revision_record':str(record.relative_to(r)),'exact_remote_refs_verified':True,'main_unchanged':b['main'],'tracked_clean':True,'changed_paths':changed,'no_feature_overlay_or_incorporation':True,'historical_feature_sources_preserved':True,'public_API_and_core_file_modules_unchanged':True,'task_owners':owners,'Phase2_and_stdin_incomplete':True,'pinned_hashes_verified':len(prov['hashes']),'bytecode_hashes_preserved':len(b['bytecode_hashes']),'hosted_IDs_foreign_bodies_states_preserved':True,'limits':'Behavior is separately checked by full suite, retained independent text/range oracles, JSON rejection and real literal filename/help checks. No complete native transcript.'}
(o/'A-012-boundaries.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='task_owners'},indent=2))
