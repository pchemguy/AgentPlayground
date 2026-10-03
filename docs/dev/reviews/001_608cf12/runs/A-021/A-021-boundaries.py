import subprocess,json,hashlib,re,sys
from pathlib import Path
sys.path.insert(0,'/workspace/scratch/AgentPlayground-evidence-008')
from tests.workflows.task_ownership import check_ownership,read_tasks
r=Path('/workspace/scratch/sdd008-A-021-feature/repo');o=Path('/workspace/scratch/acceptance-out-008');b=json.loads((o/'A-021-fixture.json').read_text())
def git(*a):return subprocess.check_output(['git',*a],cwd=r,text=True).strip()
mode=sys.argv[1];owners=check_ownership(r/'docs/dev')['owners'];assert set(owners)=={f'T-{i:03}' for i in range(1,12)}
for i in [1,2,3,4,5,6,9,10,11]:assert owners[f'T-{i:03}']['status']=='Checked'
for i in [7,8]:assert owners[f'T-{i:03}']['status']=='Unchecked'
assert git('rev-parse','origin/main')==b['main_before'];assert git('ls-remote','origin','refs/heads/main').split()[0]==b['main_before']
for path in git('ls-tree','-r','--name-only',b['working_before'],'textstats','tests','vendor').splitlines():assert (r/path).exists() and hashlib.sha256((r/path).read_bytes()).hexdigest()==hashlib.sha256(subprocess.check_output(['git','show',b['working_before']+':'+path],cwd=r)).hexdigest()
assert git('rev-parse','HEAD:docs/dev/SPEC.md')==git('rev-parse',b['working_before']+':docs/dev/SPEC.md');assert (r/'docs/dev/SPEC.md').read_bytes()==subprocess.check_output(['git','show',b['working_before']+':docs/dev/SPEC.md'],cwd=r)
prov=json.loads((r/'vendor/PROVENANCE.json').read_text())
for path,h in prov['hashes'].items():assert hashlib.sha256((r/'vendor/sdd-manager'/path).read_bytes()).hexdigest()==h
assert not (r/'gh.tkn').exists();assert git('remote','get-url','origin')==b['origin'];assert '002_8a53078' in (r/'docs/dev/features/002_8a53078/README.md').read_text()
if mode=='partial':
 assert git('rev-parse','HEAD')==b['working_before'];assert git('branch','--show-current')==b['working_branch'];assert git('ls-remote','origin','refs/heads/'+b['working_branch']).split()[0]==b['working_before'];assert git('ls-remote','origin','refs/heads/'+b['target_branch']).split()[0]==b['target_before']
 assert owners['T-009']['document'].endswith('/docs/dev/TASKS.md');assert all(owners[x]['document'].endswith('/docs/dev/FEATURE-TASKS.md') for x in ['T-010','T-011'])
 assert all((r/'docs/dev'/name).exists() for name in b['initial_active_sources']);assert not any((r/'docs/dev/features/002_8a53078'/name).exists() for name in b['initial_active_sources']);assert git('status','--porcelain','--untracked-files=no')
 result={'mode':mode,'head':git('rev-parse','HEAD'),'actual_dirty_transfer':True,'T009_owner':'TASKS.md','T010_T011_owners':'FEATURE-TASKS.md','needed_sources_retained':True,'no_commit_push_merge':True}
else:
 assert git('branch','--show-current')==b['target_branch'];assert not git('status','--porcelain');assert all(x['document'].endswith('/docs/dev/TASKS.md') for x in owners.values());assert not list((r/'docs/dev').glob('FEATURE*'));assert re.search(r'\[ \] Phase 2',(r/'docs/dev/TASKS.md').read_text());assert re.search(r'\[x\] Milestone 2.3',(r/'docs/dev/TASKS.md').read_text())
 head=git('rev-parse','HEAD');parents=git('rev-list','--parents','-n','1','HEAD').split()[1:];assert len(parents)==2 and parents[0]==b['target_before'];feature=git('rev-parse',b['working_branch']);assert parents[1]==feature
 for branch,tip in [(b['target_branch'],head),(b['working_branch'],feature)]:assert git('ls-remote','origin','refs/heads/'+branch).split()[0]==tip
 archive=r/'docs/dev/features/002_8a53078';assert all((archive/name).exists() for name in b['initial_active_sources']);assert 'histor' in (archive/'README.md').read_text().lower()
 oldfeature=subprocess.check_output(['git','show',b['feature_completed_tip']+':docs/dev/FEATURE-TASKS.md'],cwd=r,text=True);main=(r/'docs/dev/TASKS.md').read_text();history=(archive/'FEATURE-TASKS.md').read_text()
 for line in oldfeature.splitlines():
  if line.strip().startswith('Verified T-'):
   assert line.strip() in main
   if not line.strip().startswith('Verified T-009'):assert line.strip() in history
 assert 'T-009 was transferred at the interrupted checkpoint' in history and 'complete historical evidence are in main' in history
 assert {x['id'] for x in read_tasks(archive/'FEATURE-TASKS.md')}=={'T-010','T-011'}
 partial=json.loads((o/'A-021-partial-state/state.json').read_text());assert partial['head']==b['working_before'];assert partial['owned_hashes']['docs/dev/TASKS.md']
 result={'mode':mode,'head':head,'parents':parents,'feature_tip':feature,'exact_remote_refs_verified':True,'same_campaign_baseline_and_paths':True,'all_feature_task_history_preserved':True,'sole_current_task_owner':'TASKS.md','archives_historical_sources_preserved':True,'main_and_stdin_whole_phase_incomplete':True,'no_product_test_vendor_changes':True}
result.update(task_owners=owners,pinned_hashes_verified=len(prov['hashes']),live_hosted_or_credentials=False)
(o/('A-021-'+mode+'-boundaries.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='task_owners'},indent=2))
