from pathlib import Path
import subprocess,json,re,hashlib,sys
sys.path.insert(0,'/workspace/scratch/AgentPlayground-evidence-008')
from tests.workflows.task_ownership import check_ownership
r=Path('/workspace/scratch/sdd008-A-019-boundary/repo');o=Path('/workspace/scratch/acceptance-out-008')
def git(*a):return subprocess.check_output(['git',*a],cwd=r,text=True).strip()
b=json.loads((o/'A-019-fixture.json').read_text());conf=json.loads((o/'A-019-conflicted/state.json').read_text());failed=json.loads((o/'A-019-failed-check/state.json').read_text())
assert conf['unmerged']['stdout'] and conf['merge_head']['returncode']==0
assert conf['head']['stdout'].strip()==b['target_before'] and conf['remote_main']['stdout'].split()[0]==b['target_before']
assert not failed['unmerged']['stdout'] and failed['merge_head']['returncode']==0;assert failed['head']['stdout'].strip()==b['target_before'];assert failed['remote_main']['stdout'].split()[0]==b['target_before']
head=git('rev-parse','HEAD');parents=git('rev-list','--parents','-n','1','HEAD').split()[1:];assert parents==[b['target_before'],b['working_before']]
assert git('branch','--show-current')=='main';assert subprocess.run(['git','rev-parse','--verify','MERGE_HEAD'],cwd=r,capture_output=True).returncode!=0
assert not git('status','--porcelain');assert git('ls-files','--stage')==failed['stages']['stdout'].strip();assert hashlib.sha256((r/'README.md').read_bytes()).hexdigest()==failed['README_sha256']
assert 'Target-owned note:' in (r/'README.md').read_text();assert '# TextStats' in (r/'README.md').read_text()
assert git('rev-parse','phase/1-named-file-baseline')==b['working_before']
for branch,tip in [('main',head),('phase/1-named-file-baseline',b['working_before'])]:assert git('ls-remote','origin','refs/heads/'+branch).split()[0]==tip
assert git('remote','get-url','origin')==b['remote'];assert not (r/'gh.tkn').exists();assert (r/'.git/controlled-boundary-ready').read_text()=='ready\n'
assert git('rev-parse','HEAD:tools/controlled_boundary.py')==git('rev-parse',b['working_before']+':tools/controlled_boundary.py');assert git('rev-parse','HEAD:AGENTS.md')==git('rev-parse',b['working_before']+':AGENTS.md')
for p in git('ls-tree','-r','--name-only',b['working_before'],'textstats','tests','docs','vendor').splitlines():assert git('rev-parse','HEAD:'+p)==git('rev-parse',b['working_before']+':'+p)
owners=check_ownership(r/'docs/dev')['owners'];assert set(owners)=={f'T-{i:03}' for i in range(1,9)};assert all(owners[f'T-{i:03}']['status']=='Checked' for i in range(1,6));assert all(owners[f'T-{i:03}']['status']=='Unchecked' for i in range(6,9));assert re.search(r'\[x\] Phase 1',(r/'docs/dev/TASKS.md').read_text());assert re.search(r'\[ \] Phase 2',(r/'docs/dev/TASKS.md').read_text())
prov=json.loads((r/'vendor/PROVENANCE.json').read_text())
for p,h in prov['hashes'].items():assert hashlib.sha256((r/'vendor/sdd-manager'/p).read_bytes()).hexdigest()==h
result={'head':head,'parents':parents,'working_branch_preserved':b['working_before'],'exact_remote_refs_verified':True,'conflicted_and_failed_check_target_uncommitted_unpublished':True,'resolved_staged_tree_and_README_preserved_exactly':True,'tracked_clean_no_Phase2_work':True,'task_owners':owners,'pinned_hashes_verified':len(prov['hashes']),'fixture_policy_check_preserved':True,'live_hosted_or_credentials':False,'limits':'Controlled local origin and external prerequisite, not a real hosted outage; actual consumer attempts and subsequent checks separately retained.'}
(o/'A-019-boundaries.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='task_owners'},indent=2))
