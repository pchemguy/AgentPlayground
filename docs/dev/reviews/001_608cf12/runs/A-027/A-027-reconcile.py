from pathlib import Path
import json,re,subprocess,hashlib,os
O=Path('/workspace/scratch/acceptance-out-008');E=Path('/workspace/scratch/AgentPlayground-evidence-008');C=E/'docs/dev/reviews/001_608cf12';live=Path('/workspace/scratch/AgentPlayground-sdd-008');case=Path('/workspace/scratch/sdd008-A-021-feature/repo');env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',GIT_OPTIONAL_LOCKS='0')
def git(repo,*args):return subprocess.check_output(['git',*args],cwd=repo,env=env,text=True).strip()
x=json.loads((O/'A-027-fresh-checks.json').read_text());checks={'current_exact_branch_remote':{},'boundary_objects':[]}
for rp,v in x['repositories'].items():
 checks['current_exact_branch_remote'][rp]=f"{v['head']['stdout']}\trefs/heads/{v['branch']['stdout']}" in v['remote_refs']['stdout'];assert checks['current_exact_branch_remote'][rp]
for n,f in [(6,'A-006-resume4-independent.json'),(10,'A-010-independent.json'),(12,'A-012-independent.json'),(13,'A-013-independent.json'),(18,'A-018-merge-recovered-independent.json'),(19,'A-019-independent.json'),(21,'A-021-independent.json')]:
 d=C/'runs'/f'A-{n:03}';j=json.loads((d/f).read_text());a=json.loads((d/'assessment.json').read_text());r=Path(a['repo']);oid=j['head'];actual=git(r,'show','-s','--format=%P',oid).split();assert actual==j['parents'];assert len(actual)==2;remote=x['repositories'][str(r)]['remote_refs']['stdout'];containing=[]
 for line in remote.splitlines():
  tip,ref=line.split();p=subprocess.run(['git','merge-base','--is-ancestor',oid,tip],cwd=r,env=env,capture_output=True)
  if p.returncode==0:containing.append(ref)
 assert containing;checks['boundary_objects'].append({'case':n,'head':oid,'exact_ordered_parents':actual,'current_remote_containment':containing})
old=git(case,'show','64cee9bc48346d710c74f5ae4a0cc5c3359557f9:docs/dev/FEATURE-TASKS.md');main=(case/'docs/dev/TASKS.md').read_text()
def block(s,tid):return re.search(r'^        - \[[x ]\] '+tid+r' .*?(?=^        - \[|^    - \[|^\S|\Z)',s,re.M|re.S).group().rstrip()
assert all(block(old,f'T-{n:03}')==block(main,f'T-{n:03}') for n in [9,10,11]);changed=git(case,'diff','--name-only','64cee9bc48346d710c74f5ae4a0cc5c3359557f9','b74570a206a696c863daa3d09f6a393743d0e69c').splitlines();assert all(p.endswith('.md') and (p.startswith('docs/dev/') or p=='README.md') for p in changed)
partial=C/'runs/A-021/A-021-partial-state/owned/docs/dev';pm=(partial/'TASKS.md').read_text();pf=(partial/'FEATURE-TASKS.md').read_text();assert block(old,'T-009')==block(pm,'T-009');assert not re.search(r'^        - \[[x ]\] T-009',pf,re.M);assert all(block(old,f'T-{n:03}')==block(pf,f'T-{n:03}') for n in [10,11]);assert all((partial/n).exists() for n in ['FEATURE-TASKS.md','FEATURE-SPEC.md','FEATURE-PLAN.md','FEATURE_DECOMPOSITION.md'])
links=[]
for p in (case/'docs/dev').rglob('*.md'):
 for label,target in re.findall(r'\[([^\]\n]+)\]\(([^)]+)\)',p.read_text()):
  target=target.split('#')[0]
  if not target or ':' in target:continue
  assert (p.parent/target).exists(),(p,target);links.append([str(p.relative_to(case)),target])
checks['A021']={'partial_export_T009_exact_once':True,'partial_remaining_sources_and_T010_T011_exact':True,'final_all_three_blocks_exact':True,'incorporation_paths':changed,'all_local_document_links_checked':len(links),'no_source_test_vendor_changes':True,'archives_remain_historical':True}
oldhost=json.loads((C/'runs/A-013/A-013-host-independent-final.json').read_text())['rows'];newhost=json.loads((O/'A-027-hosted.json').read_text())['rows'];assert oldhost==newhost;checks['hosted_selected_metadata_unchanged_since_A013']=True
checks['source_check']=json.loads((O/'A-027-source-check.json').read_text());checks['retained_case_counts']={}
reg=json.loads((C/'acceptance/cases.json').read_text());checks['registry_type']=type(reg).__name__
checks['recovery_bundles_all_valid']=all(b['exit']==0 for b in x['bundles']);assert checks['recovery_bundles_all_valid']
(O/'A-027-reconciliation.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps({k:v for k,v in checks.items() if k not in ['source_check','boundary_objects','current_exact_branch_remote']},indent=2))
