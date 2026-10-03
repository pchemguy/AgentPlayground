"""Read authorized task metadata, retaining hashes instead of provider bodies."""
import subprocess,json,re,hashlib,sys
from pathlib import Path
r=Path('/workspace/scratch/AgentPlayground-sdd-008')
def get(endpoint):
 p=subprocess.run(['python','tools/github_api.py','GET','/repos/pchemguy/AgentPlayground/'+endpoint,'--token-file','gh.tkn'],cwd=r,text=True,capture_output=True,check=True)
 x=json.loads(p.stdout);assert x['status']==200;return x['body']
issues=get('issues?state=all&per_page=100');rows=[]
for i in issues:
 if 'pull_request' in i:continue
 body=i.get('body') or '';marker=re.search(r'<!-- sdd-forge:task-id=(T-\d+) -->',body)
 if not marker:continue
 foreign=re.sub(r'<!-- sdd-forge:task-id=T-\d+ -->.*?<!-- /sdd-forge:task-id=T-\d+ -->','',body,flags=re.S)
 row={'task':marker[1],'number':i['number'],'state':i['state'],'state_reason':i.get('state_reason'),'milestone':(i.get('milestone') or {}).get('number'),'labels':[v['name'] for v in i['labels']],'comments_count':i['comments'],'foreign_body_sha256':hashlib.sha256(foreign.encode()).hexdigest()}
 if marker[1] in {'T-009','T-010','T-011'}:
  cs=get(f'issues/{i["number"]}/comments?per_page=100');row['comment_ids']=[c['id'] for c in cs];row['comment_commits']=[sorted(set(re.findall(r'\b[0-9a-f]{40}\b',c.get('body') or ''))) for c in cs]
 rows.append(row)
Path(sys.argv[1]).write_text(json.dumps({'rows':rows,'limits':'GET observations only; provider bodies and credentials excluded.'},indent=2)+'\n');print('Protected hosted metadata retained:',len(rows),'task issues.')
