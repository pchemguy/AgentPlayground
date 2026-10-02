"""Retain evaluator observations and publish one consumer-case evidence checkpoint."""
from pathlib import Path
import sys,subprocess,json,datetime,shutil,re
EVAL=Path('/workspace/scratch/AgentPlayground-evidence-008'); CAM=EVAL/'docs/dev/reviews/001_608cf12'
data=json.loads(Path(sys.argv[1]).read_text());id=data['id'];run=CAM/'runs'/id;run.mkdir(parents=True,exist_ok=True)
for source in data.get('artifacts',[]):
 p=Path(source)
 assert p.exists(), f'Required artifact missing: {p}'
 if p.exists():
  if p.is_dir():shutil.copytree(p,run/p.name,dirs_exist_ok=True)
  else:shutil.copy2(p,run/p.name)
(run/'assessment.json').write_text(json.dumps(data,indent=2)+'\n')
if 'repo' in data:
 subprocess.run(['python','-m','tests.workflows.git_snapshot','capture',data['repo'],str(run/'git-snapshot.json')],cwd=EVAL,check=True,capture_output=True,text=True)
registry=CAM/'acceptance/cases.json';cases=json.loads(registry.read_text())
for c in cases:
 if c['id']==id:c.update(status=data['status'],run_path='runs/'+id,assessment=data['assessment'],assessed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),evidence=[str(p.relative_to(CAM)) for p in run.iterdir() if p.is_file()]);c['prompt_path']=next((x for x in c['evidence'] if 'prompt' in x),None)
registry.write_text(json.dumps(cases,indent=2)+'\n')
report='# TextStats runtime acceptance report\n\n## State and evidence\n\nPinned source: 529e98d4d3cd7002e3a49e34394552a44bf0a8d0. Explicit skill-source loading through fresh agents; automatic installed-client discovery is not claimed. Prompts, available consumer journals/final handoffs and independent actual checks are retained; no native complete tool transcript is fabricated.\n\n| Case | Status | Assessment | Records |\n| --- | --- | --- | --- |\n'
for c in cases:report+=f"| {c['id']} | {c['status']} | {(c['assessment'] or 'Not executed').replace('|','/').replace(chr(10),' ')} | "+(f"[Run]({c['run_path']}/assessment.json)" if c['run_path'] else 'None')+' |\n'
report+='\n## Counts and limits\n\n'+', '.join(f'{status}: {sum(c["status"]==status for c in cases)}' for status in ['Passed','Failed','Blocked','Suspended','Running','Pending'])+'.\n\nFixture-only checks are not agent-driven passes. Injected failures are distinguished from real GitHub failures. Native client installation/discovery and complete raw tool-message export remain outside the available runtime.\n'
(CAM/'ACCEPTANCE-REPORT.md').write_text(report)
for p in run.rglob('*'):
 if p.is_file():assert not re.search(rb'(?:github_pat_[A-Za-z0-9_]{30,}|ghp_[A-Za-z0-9]{30,})',p.read_bytes()),p
subprocess.run(['git','diff','--check'],cwd=EVAL,check=True)
subprocess.run(['git','add',str(CAM)],cwd=EVAL,check=True)
subprocess.run(['git','commit','-m',f'Record {id} consumer acceptance assessment'],cwd=EVAL,check=True)
subprocess.run(['git','push','origin','evaluation/008-runtime-acceptance'],cwd=EVAL,check=True)
local=subprocess.check_output(['git','rev-parse','HEAD'],cwd=EVAL,text=True).strip();remote=subprocess.check_output(['git','ls-remote','origin','refs/heads/evaluation/008-runtime-acceptance'],cwd=EVAL,text=True).split()[0];assert local==remote
print(id,local,'remote equality verified')
