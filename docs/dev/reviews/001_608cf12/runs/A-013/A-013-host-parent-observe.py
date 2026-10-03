import subprocess,json,hashlib
from pathlib import Path
r=Path('/workspace/scratch/AgentPlayground-sdd-008');o=Path('/workspace/scratch/acceptance-out-008')
def get(path):
 x=subprocess.run(['python','tools/github_api.py','GET','/repos/pchemguy/AgentPlayground/'+path,'--token-file','gh.tkn'],cwd=r,capture_output=True,text=True,check=True);d=json.loads(x.stdout);assert d['status']==200;return d['body']
ms=get('milestones?state=all&per_page=100');labels=get('labels?per_page=100')
rows=[{'number':x['number'],'title':x['title'],'state':x['state'],'description_sha256':hashlib.sha256((x.get('description') or '').encode()).hexdigest()} for x in ms]
phase=[{'name':x['name'],'description_sha256':hashlib.sha256((x.get('description') or '').encode()).hexdigest(),'description_claims_incomplete':'incomplete' in (x.get('description') or '').lower(),'description_claims_planned':'planned' in (x.get('description') or '').lower()} for x in labels if x['name'].startswith('sdd-phase-2-')]
result={'milestones':rows,'phase_labels':phase,'read_only':True,'raw_bodies_excluded':True};(o/'A-013-host-parents-independent.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
