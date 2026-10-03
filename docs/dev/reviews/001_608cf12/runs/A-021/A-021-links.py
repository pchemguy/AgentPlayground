from pathlib import Path
import re,json
r=Path('/workspace/scratch/sdd008-A-021-feature/repo');o=Path('/workspace/scratch/acceptance-out-008');rows=[];errors=[]
for p in sorted((r/'docs/dev').rglob('*.md')):
 for label,target in re.findall(r'\[([^]\n]+)\]\(([^)]+)\)',p.read_text()):
  local=target.split('#',1)[0]
  if not local or ':' in local or local.startswith('/'):continue
  valid=(p.parent/local).resolve().exists();rows.append({'document':str(p.relative_to(r)),'target':target,'exists':valid})
  if not valid:errors.append(rows[-1])
(o/'A-021-links.json').write_text(json.dumps({'checked':len(rows),'errors':errors,'links':rows},indent=2)+'\n');print(json.dumps({'links_checked':len(rows),'errors':errors}));assert not errors
