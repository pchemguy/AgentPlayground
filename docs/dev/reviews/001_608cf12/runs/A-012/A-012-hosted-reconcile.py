"""Reconcile authorized managed scope while preserving identities and human material."""
from pathlib import Path
import json,re,time,urllib.request
root=Path('/workspace/scratch/AgentPlayground-sdd-008')
repo='https://api.github.com/repos/pchemguy/AgentPlayground'
token=(root/'gh.tkn').read_text().strip()
def request(path, data=None, method=None):
    payload=None if data is None else json.dumps(data).encode()
    req=urllib.request.Request(repo+path,data=payload,method=method,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','Content-Type':'application/json','X-GitHub-Api-Version':'2022-11-28'})
    with urllib.request.urlopen(req,timeout=30) as response: return json.load(response)
issues=request('/issues?state=all&per_page=100'); milestones=request('/milestones?state=all&per_page=100')
before=json.loads(Path('/workspace/scratch/acceptance-out-008/A-012-hosted-before.json').read_text())
old={i['number']:i for i in before['issues']}; tasks=(root/'docs/dev/TASKS.md').read_text(); plan=(root/'docs/dev/PLAN.md').read_text(); actions=[]
for tid in ['T-006','T-007','T-008','T-010','T-011']:
    matches=[i for i in issues if 'pull_request' not in i and re.match(r'\['+tid+r'\]',i['title']) and i.get('body','').count('sdd-forge:task-id='+tid)==2]
    assert len(matches)==1,('ambiguous',tid)
    i=matches[0]; assert i['body']==old[i['number']]['body'],('concurrent body edit',tid)
    pattern=r'## Task brief <!-- sdd-forge:task-id='+tid+r' -->.*?<!-- /sdd-forge:task-id='+tid+r' -->'
    if tid=='T-006':
        title='Retired JSON output scope'
        original=re.search(pattern,i['body'],re.S).group().split('-->\n',1)[1].rsplit('<!--',1)[0]
        content='Retired by human-commanded campaign 003_d0eeeff. No active JSON requirement, executable task or phase exit remains. Stable T-006/Milestone 2.1 identities are reserved; historical verified delivery and issue state are preserved. No new completion or reopening is claimed. Current output is exact plain lines=<N> words=<N>; --json is an unknown option.\n\n### Historical task brief (superseded)\n\n'+original
    else:
        entry=re.search(r'        - \[[ x]\] '+tid+r' — (.*?)(?=\n        - |\n    - |\Z)',tasks,re.S).group(1)
        title=entry.splitlines()[0]
        content=entry.split('            Verified ',1)[0].strip()+'\n\nSources: docs/dev/TASKS.md; docs/dev/SPEC.md; docs/dev/PLAN.md on phase/2-output-and-input-extensions. T-007/T-008 remain planned; no stdin execution is claimed.'
    managed='## Task brief <!-- sdd-forge:task-id='+tid+' -->\n\n'+content+'\n<!-- /sdd-forge:task-id='+tid+' -->'
    body=re.sub(pattern,lambda _:managed,i['body'],count=1,flags=re.S)
    result=request('/issues/'+str(i['number']),{'title':'['+tid+'] '+title,'body':body},'PATCH')
    assert result['state']==i['state'] and result['milestone']['number']==i['milestone']['number']
    actions.append({'task':tid,'number':i['number'],'url':result['html_url'],'state':result['state'],'action':'managed title/body aligned; state/parent/labels preserved'})
    time.sleep(1)
for mid,num in [('1.1',1),('2.1',3),('2.2',4),('2.3',5)]:
    existing=next(m for m in milestones if m['number']==num)
    assert re.match(r'sdd-'+re.escape(mid)+r'-',existing['title'])
    original=next(m for m in before['milestones'] if m['number']==num)
    assert existing['description']==original['description'],('concurrent milestone edit',mid)
    if mid=='2.1':
        title='sdd-2.1-Retired-JSON-output-scope'
        description='Retired by campaign 003_d0eeeff; excluded from current TASKS/phase exits. Stable identity, issue #6 history and prior state retained, without claiming new completion.\n\nHistorical superseded outcome: '+existing['description']
    else:
        section=re.search(r'### Milestone '+re.escape(mid)+r' — ([^\n]+)\n\n(.*?)(?=\n### |\n## |\Z)',plan,re.S)
        title='sdd-'+mid+'-'+section.group(1).replace(' ','-')
        description=section.group(2).strip()
    result=request('/milestones/'+str(num),{'title':title,'description':description},'PATCH')
    assert result['state']==existing['state']
    actions.append({'milestone':mid,'number':num,'state':result['state'],'action':'managed description/title aligned; identity/state preserved'})
    time.sleep(1)
label='sdd-phase-2-Output-and-input-extensions'
result=request('/labels/'+label,{'description':'Plain-output named-file ranges and planned strict UTF-8 stdin; Phase 2 remains incomplete.'},'PATCH')
actions.append({'label':result['name'],'action':'scope description aligned; identity/color preserved'})
Path('/workspace/scratch/acceptance-out-008/A-012-hosted-actions.json').write_text(json.dumps(actions,indent=2))
print(json.dumps(actions,indent=2))
