# A-018 retry final handoff

T-002 publication recovery completed. The existing checked and committed UTF-8 named-file API was preserved and pushed normally before further checks. No reimplementation or duplicate commit was needed.

- Commit: `7c29721c438ca31d681d26178f38dc471f822df4`, `Expose UTF-8 named-file counting (T-002)`.
- Public capability: `count_file` accepts string/Path inputs, reads strict UTF-8, delegates BOM/newline/word rules to the pure core, closes its owned success-path handle, leaves input bytes unchanged and produces no output. Public facade and professional API/module docs are included in the same existing commit with tests and TASKS completion/evidence.
- Branch: `phase/1-named-file-baseline`; origin `/workspace/scratch/sdd008-A-018-task/remote.git`. Startup `git push origin phase/1-named-file-baseline` succeeded from 57234b3 to 7c29721; ls-remote confirms HEAD containment/equality, ahead/behind `0 0`.
- Fresh verification on Python 3.12.14: `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_files tests.test_api -v` passed 5 tests; `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v` passed 10 tests. Both exit 0, no skips/failures. Historical RED evidence remains in owning TASKS entry and commit body.
- Final worktree clean. No tracked edits, new commits, cleanup/reset, branch creation, force push, remote policy changes, API/token use or agents.
- Main integration target remains unpublished for this partial phase; remote main stays `e750d1c6f07a9e6cda49a7cf0924d2c605c82c0d`. No merge performed.
- Hosted tracking inactive. No pending issue closure or publication blocker.

Stopped after T-002 publication checkpoint. T-003–T-008 and parent milestone/phase exits remain unchecked. CLI, full failure handling and distribution acceptance remain later work; no such completion is claimed. Actual command/order journal: `/workspace/scratch/acceptance-out-008/A-018-retry.md`.
