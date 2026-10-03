from pathlib import Path
import subprocess,json,hashlib
r=Path('/workspace/scratch/AgentPlayground-sdd-008');o=Path('/workspace/scratch/acceptance-out-008')
def git(*a):return subprocess.check_output(['git',*a],cwd=r,text=True).strip()
b=json.loads((o/'A-011-baseline.json').read_text())
for k,args in [('head',('rev-parse','HEAD')),('branch',('branch','--show-current')),('refs',('show-ref',)),('tree',('ls-tree','-r','HEAD')),('tracked_status',('status','--porcelain','--untracked-files=no'))]:assert git(*args)==b[k],k
assert set(git('ls-files','--others','--exclude-standard').splitlines())==set(b['bytecode_hashes'])
for p,h in b['bytecode_hashes'].items():assert hashlib.sha256((r/p).read_bytes()).hexdigest()==h
before=json.loads((o/'A-010-host-independent.json').read_text())['rows'];after=json.loads((o/'A-011-host-independent.json').read_text())['rows'];assert {x['task']:x for x in before}=={x['task']:x for x in after}
final=(o/'A-011-final.md').read_text();assert '--json' in final and 'T-006' in final and 'T-007' in final and 'T-008' in final
result={'head':b['head'],'branch':b['branch'],'Git_refs_tree_index_and_worktree_unchanged':True,'no_new_untracked_repo_file':True,'bytecode_hashes_preserved':len(b['bytecode_hashes']),'hosted_selected_metadata_unchanged':True,'assessment_only':True,'limits':'Metadata GET checks and retained factual inspection journal support the no-mutation assessment; complete native tool-message transcript is unavailable.'}
(o/'A-011-independent.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
