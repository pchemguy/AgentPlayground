import os,sys,json,subprocess,hashlib,re
from pathlib import Path
O=Path('/workspace/scratch/acceptance-out-008'); E=Path('/workspace/scratch/AgentPlayground-evidence-008');S=Path('/workspace/scratch/6420baa7afea');R=Path('/workspace/scratch/AgentPlayground-sdd-008');C=E/'docs/dev/reviews/001_608cf12';env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',GIT_OPTIONAL_LOCKS='0');sys.path.insert(0,str(E))
def run(cmd,cwd,out):
 p=subprocess.run(cmd,cwd=cwd,env=env,text=True,capture_output=True);(O/('A-027-'+out)).write_text(p.stdout+p.stderr);return {'command':cmd,'exit':p.returncode,'output':'A-027-'+out}
def git(r,*args):
 p=subprocess.run(['git',*args],cwd=r,env=env,text=True,capture_output=True);return {'exit':p.returncode,'stdout':p.stdout.strip(),'stderr':p.stderr.strip()}
checks={};checks['python']=run(['python','--version'],R,'python.txt');checks['live_suite']=run(['python','-m','unittest','discover','-s','tests','-v'],R,'live-suite.txt');checks['evidence_suite']=run(['python','-m','unittest','discover','-s','tests','-v'],E,'evidence-suite.txt')
for name in ['named-success','named-errors','ranges-contract-text','json-removal','stdin-contract-text','stdin-final']:
 checks[name]=run(['python','-m','tests.workflows.product_acceptance',str(R),str(C/'acceptance/oracle'/f'{name}.json'),str(O/f'A-027-{name}.json')],E,f'{name}.txt')
from tests.workflows.task_ownership import check_ownership
checks['ownership_live']=check_ownership(R/'docs/dev');checks['ownership_A021']=check_ownership(Path('/workspace/scratch/sdd008-A-021-feature/repo/docs/dev'))
pin=json.loads((R/'vendor/PROVENANCE.json').read_text());comparison=[]
for name,h in pin['hashes'].items():
 live=hashlib.sha256((R/'vendor/sdd-manager'/name).read_bytes()).hexdigest();g=git(S,'show',pin['source_commit']+':'+name)
 p=subprocess.run(['git','show',pin['source_commit']+':'+name],cwd=S,capture_output=True);comparison.append({'path':name,'expected':h,'live':live,'source':hashlib.sha256(p.stdout).hexdigest(),'source_exit':p.returncode})
checks['pin']={'commit':pin['source_commit'],'files':len(comparison),'mismatches':[x for x in comparison if x['expected']!=x['live'] or x['expected']!=x['source'] or x['source_exit']]}
(O/'A-027-pin-comparison.json').write_text(json.dumps(comparison,indent=2))
repos=[S,E,R];rows=[]
for n in range(1,27):
 d=C/'runs'/f'A-{n:03}';a=json.loads((d/'assessment.json').read_text());r=Path(a['repo']);
 if r not in repos:repos.append(r)
 evidence=[]
 for f in sorted(d.rglob('*')):
  if f.is_file():evidence.append({'path':str(f.relative_to(E)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
 journals=[x for x in evidence if x['path'].endswith('.md') and 'final' not in x['path']];inputs=[x for x in evidence if 'prompt' in x['path']];observations=[x for x in evidence if any(k in x['path'] for k in ['independent','boundaries','commands','RED','red','GREEN','green','snapshot'])]
 rows.append({'id':a['id'],'claimed_status':a['status'],'repo':a['repo'],'retained_assessment':a['assessment'],'evidence_files':len(evidence),'journals':[x['path'] for x in journals],'inputs':[x['path'] for x in inputs],'observations':[x['path'] for x in observations],'manifest':evidence})
checks['repositories']={str(r):{'exists':r.exists(),'branch':git(r,'branch','--show-current'),'head':git(r,'rev-parse','HEAD'),'status':git(r,'status','--porcelain=v1','--untracked-files=no'),'refs':git(r,'show-ref','--heads'),'remote_refs':git(r,'ls-remote','--heads','origin')} for r in repos if r.exists()}
checks['bundles']=[]
for n in [15,18,19,20,21]:
 for f in (C/'runs'/f'A-{n:03}').rglob('*.bundle'):
  p=git(E,'bundle','verify',str(f));checks['bundles'].append({'path':str(f.relative_to(E)),**p})
(O/'A-027-evidence-inventory.json').write_text(json.dumps(rows,indent=2));(O/'A-027-fresh-checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps({k:v for k,v in checks.items() if k not in ['repositories','bundles','ownership_live','ownership_A021']},indent=2));print('repos',len(checks['repositories']),'bundles',len(checks['bundles']))
