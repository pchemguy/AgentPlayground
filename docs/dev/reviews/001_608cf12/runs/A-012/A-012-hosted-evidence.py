"""Publish deduplicated amendment evidence and save safe hosted metadata."""
from pathlib import Path
import json,re,time,urllib.request,subprocess
root=Path('/workspace/scratch/AgentPlayground-sdd-008'); token=(root/'gh.tkn').read_text().strip(); repo='https://api.github.com/repos/pchemguy/AgentPlayground'
def request(path,data=None,method=None):
    req=urllib.request.Request(repo+path,data=None if data is None else json.dumps(data).encode(),method=method,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','Content-Type':'application/json','X-GitHub-Api-Version':'2022-11-28'})
    with urllib.request.urlopen(req,timeout=30) as response: return json.load(response)
merge=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(); amendment='6561e287e59c8b4e86c7a3cdeaaa48a60df82154'; records=[]
for number,tid in [(6,'T-006'),(10,'T-010'),(11,'T-011')]:
    issue=request('/issues/'+str(number)); assert issue['title'].startswith('['+tid+']') and ('sdd-forge:task-id='+tid) in issue['body']
    assert issue['state']=='closed'
    comments=request('/issues/'+str(number)+'/comments?per_page=100'); marker='<!-- sdd-steer:003_d0eeeff:amendment-evidence -->'
    body=marker+'\n\n'+tid+': human-commanded JSON removal amendment '+amendment+' published and explicitly merged into paused phase/2-output-and-input-extensions at '+merge+'.\n\n'
    if tid=='T-006': body+='JSON-only current scope is retired; its stable identity and historical delivery evidence are retained. This is removal evidence, not new task completion. Existing closed state is preserved.\n\n'
    else: body+='Retained named-file plain-output/range/BOM/strict-complete-decode acceptance is freshly verified; task and Milestone 2.3 remain complete. Existing completion history is preserved.\n\n'
    body+='Removal test-first checks observed 3 tests/13 behavioral failures then 3 passed. Focused and full amendment suites passed 39 tests; merged-state full suite passed 39 with no skips. Checkout/extracted README examples and source-package API/import/archive checks passed. Permission denial is narrowly simulated under the privileged runner. T-007/T-008, Milestone 2.2 and Phase 2 remain incomplete; main unchanged. Revision report: https://github.com/pchemguy/AgentPlayground/blob/'+merge+'/docs/dev/reviews/003_d0eeeff/REVISION-REPORT.md'
    existing=[c for c in comments if marker in c.get('body','')]
    assert len(existing)<=1
    if not existing: comment=request('/issues/'+str(number)+'/comments',{'body':body},'POST')
    else: comment=existing[0]
    records.append({'task':tid,'issue':number,'state':issue['state'],'comment_id':comment['id'],'url':comment['html_url'],'evidence':'amendment and merge verified/published; no state change'})
    time.sleep(1)
issues=request('/issues?state=all&per_page=100'); milestones=request('/milestones?state=all&per_page=100'); labels=request('/labels?per_page=100')
safe={'publication':records,'issues':[{'number':i['number'],'title':i['title'],'state':i['state'],'state_reason':i.get('state_reason'),'url':i['html_url'],'managed_ids':re.findall(r'(?<!/)sdd-forge:task-id=(T-\d+)',i.get('body','')),'milestone':i['milestone']['number'] if i['milestone'] else None,'labels':[l['name'] for l in i['labels']]} for i in issues if 'pull_request' not in i], 'milestones':[{'number':m['number'],'title':m['title'],'state':m['state']} for m in milestones], 'labels':[{'name':l['name'],'description':l['description']} for l in labels if l['name'].startswith('sdd-phase-')]}
Path('/workspace/scratch/acceptance-out-008/A-012-hosted-after.json').write_text(json.dumps(safe,indent=2)); print(json.dumps(records,indent=2))
