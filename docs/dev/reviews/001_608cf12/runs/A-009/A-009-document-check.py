"""Check the SPEC-only incorporation boundary and document navigation."""
from pathlib import Path
import re
import subprocess

root = Path('/workspace/scratch/AgentPlayground-sdd-008')
spec_path = root / 'docs/dev/SPEC.md'
spec = spec_path.read_text()
source = (root / 'docs/dev/FEATURE-SPEC.md').read_text()
lines = spec.splitlines()
for index, line in enumerate(lines):
    if line.startswith('#'):
        assert index == 0 or not lines[index - 1].strip(), f'Heading before line {index + 1}'
        assert index + 1 < len(lines) and not lines[index + 1].strip(), f'Heading after line {index + 1}'
print('PASS: Markdown heading spacing')
links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', spec)
for link in links:
    assert (spec_path.parent / link.split('#')[0]).is_file(), link
print(f'PASS: {len(links)} local SPEC links resolve')
feature_rows = [line for line in source.splitlines() if line.startswith('|')]
assert len(feature_rows) == 15
for row in feature_rows:
    assert row in spec, row
print('PASS: all 13 accepted selected-counting cases and table headings incorporated verbatim')
baseline = subprocess.check_output(['git', '--no-optional-locks', 'show', 'HEAD:docs/dev/SPEC.md'], cwd=root, text=True)
for paragraph in baseline.split('\n\n'):
    if paragraph.startswith(('When `strip_bom`', 'Recognize CRLF', '`count_file` closes', 'Stdin bytes')) or paragraph.startswith('| Input after BOM'):
        assert paragraph in spec
print('PASS: existing BOM/newline/API-error/resource/stdin contracts and whole-input table preserved')
for expected in (
    '[--lines START:END]', '--lines=START:END', 'ASCII decimal digits',
    'START <= END', 'no arbitrary upper endpoint limit', 'before acquiring input',
    'exactly once before', 'retaining their original contents and terminators',
    'An interior U+FEFF is never removed', 'Selection adds no metadata',
    'do not gate named-file range delivery',
):
    assert expected in spec, expected
assert 'No line-selection behavior is included.' not in spec
assert 'Status: proposed' not in spec
print('PASS: accepted range syntax/order/output/error/compatibility clauses and superseded exclusion review')
changed = subprocess.check_output(['git', '--no-optional-locks', 'diff', '--name-only', 'HEAD'], cwd=root, text=True).splitlines()
assert changed == ['docs/dev/SPEC.md'], changed
print('PASS: tracked edit scope is docs/dev/SPEC.md only; active feature sources and task owners retained')
print('Document checks establish incorporation consistency, not range/stdin implementation acceptance.')
