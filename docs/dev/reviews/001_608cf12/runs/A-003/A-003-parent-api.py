"""Create verified absent projection parents and log sanitized operations."""
import json,subprocess,time
from pathlib import Path
out=Path('/workspace/scratch/acceptance-out-008')
root=Path('/workspace/scratch/AgentPlayground-sdd-008')
data=json.loads((out/'A-003-projection.json').read_text())
for kind,items in [('labels',data['phases']),('milestones',data['milestones'])]:
 for item in items:
  payload=({'name':item['name'],'description':item['description'],'color':'5319e7'} if kind=='labels' else {'title':item['title'],'description':item['description']})
  body=out/('A-003-'+kind+'-'+item['id']+'.json'); body.write_text(json.dumps(payload))
  endpoint='/repos/pchemguy/AgentPlayground/'+kind
  cmd=['python','tools/github_api.py','POST',endpoint,'--token-file','gh.tkn','--body-file',str(body)]
  result=subprocess.run(cmd,cwd=root,capture_output=True,text=True)
  response=json.loads(result.stdout)
  with (out/'A-003.md').open('a') as log:
   log.write('\n```text\n'+' '.join(cmd)+'\n```\n\nPayload: '+json.dumps(payload)+'\n\nResponse: '+json.dumps(response)+'\n')
  if result.returncode or response['status'] not in (200,201): raise SystemExit('Parent operation failed; stop and inspect journal.')
  item['host']=response['body']
  (out/'A-003-projection.json').write_text(json.dumps(data,indent=2))
  print(kind,item['id'],response['status'],response['body'].get('number',response['body'].get('name')),flush=True)
  time.sleep(1)
