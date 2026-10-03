import os,subprocess,tempfile,json
from pathlib import Path
r=Path('/workspace/scratch/AgentPlayground-sdd-008');out=Path('/workspace/scratch/acceptance-out-008/A-012-literal-help.json')
results=[]
help=subprocess.run(['python','-m','textstats','--help'],cwd=r,text=True,capture_output=True);assert help.returncode==0 and not help.stderr and '--json' not in help.stdout;assert '--lines' in help.stdout and '--keep-bom' in help.stdout
results.append({'case':'help','status':help.returncode,'stdout':help.stdout,'stderr':help.stderr})
with tempfile.TemporaryDirectory(prefix='textstats-literal-') as temp:
 p=Path(temp)/'--json';raw=b'alpha beta\nlast\n';p.write_bytes(raw)
 env=dict(os.environ,PYTHONPATH=str(r),PYTHONDONTWRITEBYTECODE='1')
 for flags,expected in [(['--','--json'],'lines=2 words=3\n'),(['--lines','2:2','--','--json'],'lines=1 words=1\n')]:
  result=subprocess.run(['python','-m','textstats',*flags],cwd=temp,env=env,text=True,capture_output=True);assert result.returncode==0 and result.stdout==expected and not result.stderr;assert p.read_bytes()==raw
  results.append({'case':'literal-filename','flags':flags,'status':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'input_unchanged':True})
out.write_text(json.dumps({'results':results,'limits':'Real temporary literal filename; explicit PYTHONPATH resolves current checkout. Distribution isolation is separately verified by consumer suite.'},indent=2)+'\n');print('Help and two real literal --json filename cases passed.')
