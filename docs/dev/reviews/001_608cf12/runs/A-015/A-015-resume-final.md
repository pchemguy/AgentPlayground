T-001 is complete, committed, and pushed after resuming the interrupted checkpoint.

The retained implementation provides immutable `TextStats` and package-level `count_text`, including exact leading-BOM handling, CR/LF/CRLF line semantics, Unicode whitespace words, and professional docstrings. Existing source, tests, staged completion status, and historical RED/GREEN evidence were preserved. Only a concise resumed verification note was added to the owning T-001 entry.

Verification on Python 3.12.14:

- `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_counting tests.test_api -v`: exit 0, 7 tests passed, no skips.
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v`: exit 0, 7 tests passed, no skips.
- `git --no-optional-locks diff --cached --check`: exit 0 before commit; source/API docstrings reviewed against SPEC.

Persistence: commit `35df4a01c0681ab7b649c288e4ba52f37acd00ad` (`Implement public counting core (T-001)`) contains exactly the six task-owned paths: `docs/dev/TASKS.md`, `tests/__init__.py`, `tests/test_api.py`, `tests/test_counting.py`, `textstats/__init__.py`, and `textstats/counting.py`. Ordinary commit and push succeeded. `git ls-remote origin` confirmed `refs/heads/phase/1-named-file-baseline` equals this commit. Origin is the isolated local bare repository `/workspace/scratch/sdd008-A-015/remote.git`; hosted task projection is inactive.

Stopping state: paused on `phase/1-named-file-baseline` after T-001. Phase 1 and milestone 1.1 remain unchecked; T-002 through T-008 remain unchecked and were not started. No merge occurred. Local and remote main remain `e750d1c6f07a9e6cda49a7cf0924d2c605c82c0d`. There are no remaining staged or unstaged tracked differences. The five pre-existing untracked bytecode files in `tests/__pycache__/` and `textstats/__pycache__/` were preserved and excluded from the commit. The released controlled hook remains intact as `.git/hooks/pre-commit.controlled-disabled`; no hook bypass, reset, blanket staging, or cleanup was used. No blocker remains for this checkpoint. Named-file IO, CLI, distribution, JSON, and stdin acceptance belong to future tasks and were not claimed.

The action journal and this full handoff are saved at `/workspace/scratch/acceptance-out-008/A-015-resume.md` and `/workspace/scratch/acceptance-out-008/A-015-resume-final.md`.
