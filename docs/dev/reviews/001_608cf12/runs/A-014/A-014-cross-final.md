# A-014-cross — SUSPENDED

Controlled suspension completed during T-004's test-first RED stage. The requested T-004..T-006 boundary is incomplete; no task/phase completion is claimed.

## Current state

- Repository: `/workspace/scratch/sdd008-A-014-cross/repo`.
- Branch: `phase/1-named-file-baseline`.
- HEAD and local bare-origin phase tip: `83eab02a70e7757e11f04f46a64849f69ba64df0`; local/upstream divergence 0/0.
- Main remote remains `d769b55aa63f92d5ccbd8022cb9e87f07e541fae`; local main branch not yet created.
- Pending owned unstaged work: `tests/unit/test_files.py` and `tests/integration/test_cli.py`; two files, 138 insertions/4 deletions. No staged/untracked paths or merge state.
- No production, README or task-status edits. No commit, push, merge, phase transition or hosted operation performed during this request. No credentials read or used.

## Observed progress and failures

T-004 tests added for API standard exception preservation, silent failures and real-handle closure; CLI error/usage channels, help, dash-prefixed files and permission-denial translation. Existing API/usage/help/success behavior passes characterization.

The first focused command collected 22 tests and failed with 3 intended CLI failure subcases plus 1 environment error in child privilege dropping. Fixture review removed five duplicate inherited success checks and replaced unavailable unprivileged-child denial with deterministic EACCES at the real file-open boundary.

The latest command, `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.unit.test_files tests.integration.test_cli -v`, collected 17 tests and exited 1: 3 intended read/decode diagnostic failure subcases and 1 intended unhandled PermissionError at cli.main. Missing/directory failures expose tracebacks; malformed UTF-8 omits the input path. Production has not yet been changed. No GREEN/full-suite acceptance evidence exists for T-004.

Environment limitation: this root runner cannot set child groups/UID/GID. Controlled probe observed EPERM/EINVAL. Deterministic denied-open tests supplement real missing/malformed/directory fixtures; no real OS permission-enforcement claim is made.

## Next action after explicit resume

Preserve current tests. Add CLI read/decode exception translation into useful named stderr diagnostics/status 1 with no success stdout/traceback. Run focused and full tests, review error docs, and only then mark/commit/push T-004. T-005 and T-006 remain unstarted.

The original remaining order is T-004 → T-005 → verify complete phase1 → explicit two-parent merge into main → merged-state verification and main publication → phase2 branch from published main → T-006 → stop before T-007. No part of that continuation was started after suspension.

Hosted tracking remains disabled by governing AGENTS.md; historical live issue references are provenance only. All raw logs and exact action chronology are preserved in A-014-cross.md, A-014-cross-T004-red.log and A-014-cross-T004-red-repaired-fixture.log. Pending work was preserved without reset/stash.
