from pathlib import Path
import subprocess,json,hashlib
r=Path('/workspace/scratch/AgentPlayground-sdd-008');out=Path('/workspace/scratch/acceptance-out-008/A-027-host-parents.json')
def get(endpoint):
 p=subprocess.run(['python','tools/github_api.py','GET','/repos/pchemguy/AgentPlayground/'+endpoint,'--token-file','gh.tkn'],cwd=r,text=True,capture_output=True,check=True);x=json.loads(p.stdout);assert x['status']==200;return x['body']
ms=get('milestones?state=all&per_page=100'); ls=get('labels?per_page=100'); rows=[{'id':v['id'],'number':v['number'],'title':v['title'],'state':v['state'],'description_sha256':hashlib.sha256((v.get('description') or '').encode()).hexdigest()} for v in ms];labels=[{'name':v['name'],'description_sha256':hashlib.sha256((v.get('description') or '').encode()).hexdigest()} for v in ls if v['name'].startswith('sdd-phase-')]
out.write_text(json.dumps({'milestones':rows,'phase_labels':labels,'read_only':True,'raw_bodies_excluded':True},indent=2));print('Selected',len(rows),'milestones and',len(labels),'phase labels.')
