"""Verify the selected incorporation and preserved historical identities."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
root=Path.cwd(); out=Path('/workspace/scratch/acceptance-out-008'); dev=root/'docs/dev'; pkg=dev/'features/002_8a53078'
protected=json.loads((out/'A-021-resume-preserved-sha256.json').read_text())
assert all(hashlib.sha256((root/p).read_bytes()).hexdigest()==h for p,h in protected.items())
main=(dev/'TASKS.md').read_text(); old=subprocess.check_output(['git','show','64cee9bc48346d710c74f5ae4a0cc5c3359557f9:docs/dev/TASKS.md'],text=True)
source=subprocess.check_output(['git','show','64cee9bc48346d710c74f5ae4a0cc5c3359557f9:docs/dev/FEATURE-TASKS.md'],text=True)
def block(text,tid):
    m=re.search(r'^        - \[[x ]\] '+tid+r' .*?(?=^        - \[|^    - \[|^\S|\Z)',text,re.M|re.S)
    assert m,tid
    return m.group().rstrip()
for number in range(1,7):
    tid=f'T-{number:03}'; assert block(main,tid)==block(old,tid),tid
for number in range(9,12):
    tid=f'T-{number:03}'; assert block(main,tid)==block(source,tid),tid
ids=re.findall(r'^        - \[[x ]\] (T-\d+)',main,re.M)
assert sorted(ids)==[f'T-{n:03}' for n in range(1,12)]
assert '- [ ] Phase 2 — Output and input extensions' in main
assert '- [ ] Milestone 2.2 — UTF-8 stdin' in main
for tid in ['T-007','T-008']: assert f'- [ ] {tid}' in main
assert '- [x] Milestone 2.3 — Line-range counting' in main
names=['FEATURE-SPEC.md','FEATURE_DECOMPOSITION.md','FEATURE-PLAN.md','FEATURE-TASKS.md']
for name in names: assert not (dev/name).exists() and (pkg/name).is_file()
assert 'historical, non-executable task snapshot' in (pkg/'FEATURE-TASKS.md').read_text()
assert 'independently executable feature rows are retired' in (pkg/'FEATURE-TASKS.md').read_text()
assert 'FEATURE-TASKS.md)' not in main
paths=[dev/n for n in ['PROJECT.md','DECOMPOSITION.md','PLAN.md','TASKS.md','SPEC.md','ARCHITECTURE.md','layout.md']]+[pkg/'README.md']+[pkg/n for n in names]+[root/'README.md']
links=[]; headings=[]
for p in paths:
    s=p.read_text()
    for label,target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',s):
        if re.match(r'^[a-z]+:',target) or target.startswith('#'): continue
        assert (p.parent/target.split('#')[0]).exists(),(p,target)
        links.append((str(p.relative_to(root)),target))
    lines=s.splitlines(); fence=False
    for i,line in enumerate(lines):
        if line.startswith('```'): fence=not fence; continue
        if not fence and re.match(r'^#{1,6} ',line):
            assert i==0 or not lines[i-1].strip(),(p,i,'before')
            assert i+1==len(lines) or not lines[i+1].strip(),(p,i,'after')
            headings.append((str(p.relative_to(root)),i+1))
subprocess.run(['git','diff','--check'],check=True)
facts={'boundary':sys.argv[1], 'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'protected_files_unchanged':len(protected),'selected_documents_checked':len(paths),'local_links_checked':len(links),'heading_spacing_checked':len(headings),'unique_current_task_ids':ids,'preserved_exact_blocks':['T-001','T-002','T-003','T-004','T-005','T-006','T-009','T-010','T-011'],'archives':names,'remaining_incomplete':['T-007','T-008','milestone 2.2','Phase 2'],'findings':[]}
(out/f'A-021-resume-{sys.argv[1]}-checks.json').write_text(json.dumps(facts,indent=2)+'\n')
print(json.dumps(facts,indent=2))
