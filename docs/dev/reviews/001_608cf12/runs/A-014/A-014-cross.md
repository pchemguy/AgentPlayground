# A-014-cross — controlled suspension journal

Status: SUSPENDED during T-004 RED, before any production fix, task completion, new commit or merge. Latest user instruction requests controlled process suspension and supersedes continuation of the originally authorized T-004..T-006 range.

## Request, sources and actual baseline

Read exact A-014-cross-prompt.txt. Scope: `/workspace/scratch/sdd008-A-014-cross/repo`, T-004 through T-006 inclusive; task/phase Git persistence and integration when verified; stop before T-007. Governing AGENTS.md explicitly disables hosted tracking and credential use for the isolated local bare-origin experiment. No GitHub/API/token operations performed; historical issue text remained provenance.

Consumed actual pinned manage/implement/orient skills and branch/Git/startup/range/task/checkpoint references, focused TDD/docs/verify/report skills and test-first/good-tests/documentation/verification/report references, plus current PROJECT, ARCHITECTURE, DECOMPOSITION, SPEC, PLAN, layout, TASKS and relevant file/CLI source/tests. No parent/evaluation/oracle content or other scenario code read; no workers spawned. A broad Git ref listing incidentally showed an evaluation ref identity; no content was inspected.

Actual clean startup HEAD was `83eab02a70e7757e11f04f46a64849f69ba64df0`, Isolate cross-phase consumer from live hosting, on `phase/1-named-file-baseline`. This differs from the initial handoff shorthand and was reported using actual Git evidence. Latest completed task remains T-003 at 8836c49; isolation maintenance does not complete another task.

Origin: `/workspace/scratch/sdd008-A-014-cross/remote.git`. `git ls-remote --heads origin main phase/1-named-file-baseline phase/2-output-and-input-extensions` confirmed phase1 remote exactly 83eab02, main d769b55, no phase2 ref. No outstanding commits required pushing before selection. No local main branch currently exists; origin/main is available. One attempted read-only `git diff main...HEAD --stat` failed because local main is absent; subsequent target identity used actual origin/main/remote state. No Git state was modified by that inspection.

Selected requested range from actual TASKS dependencies: T-004 then T-005 on phase1; only after verified complete phase1, explicit two-parent main merge and main publication may T-006 start on a phase2 branch from main. T-007 excluded. This was selection only; no phase transition or merge started.

## Actual execution order and checks before suspension

1. Inspected existing file adapter and CLI. Existing API context-managed read already propagates standard errors and closes handles; CLI currently exposes read/decode exceptions as tracebacks. TASKS T-004/T-005/T-006 remain unchecked.
2. Added owned pending file unit tests to tests/unit/test_files.py for missing-file subtype/silence; malformed real UTF-8 with real captured handle closure/unchanged bytes; open PermissionError identity; simulated device read failure on a real handle with exception identity and closure. These characterize already present API behavior; no fabricated API RED or production edits.
3. Added pending baseline CLI tests in tests/integration/test_cli.py for missing/malformed/directory inputs, status/output/diagnostic channels without traceback, invalid invocations, help, dash-prefixed file via --, permission denial. Initially attempted real chmod(0) denial under an unprivileged child and temporarily inherited existing success tests; no product behavior modified.
4. First RED command: `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.unit.test_files tests.integration.test_cli -v`, exit 1, 22 collected tests (including five duplicate inherited success checks), 3 intended failure subcases plus 1 environment error. Intended failures: CLI missing/directory traces and invalid-UTF8 diagnostic omitting filename. Environment error: subprocess preexec privilege drop failed. Raw log: A-014-cross-T004-red.log.
5. Investigated actual error with rg against raw log and permission/uid inspection: effective UID 0; /workspace/scratch mode 700; child preexec raised SubprocessError. Controlled child-only privilege probe attempted setgroups/setgid/setuid and reported PermissionError EPERM for setgroups and EINVAL for setgid/setuid. No parent identity or permissions changed. This environment cannot supply an unprivileged child; root chmod-only readability would not prove denial. Do not claim real filesystem permission-denial verification.
6. Repaired test fixture only: factored CLI helper mixin to prevent duplicated collection; replaced unavailable privilege-drop check with deterministic standard EACCES at `textstats.files.open` while running actual cli.main/count_file and preserving real fixture bytes. This boundary check supplements real missing/malformed/directory subprocesses. It meaningfully verifies denial propagation/translation but does not prove OS permission enforcement under root; record that limitation on future completion.
7. Second RED command before any production change: same focused command, exit 1, 17 tests collected, failures=3 and errors=1. Three intended subcase failures still show missing/malformed/directory diagnostic defects; the error is now intended unhandled PermissionError from actual cli.main, not an environment/setup error. Raw log: A-014-cross-T004-red-repaired-fixture.log. All file API tests pass as characterization; usage/help/dash path and existing CLI success tests pass already. No GREEN or full-suite acceptance run occurred.
8. Received latest user controlled suspension instruction immediately after the completed RED command. Stopped all implementation/advancement. Read-only final status/remote/check-output inspection performed solely to record coherent handoff.

## Exact suspended state

- Branch/HEAD: phase/1-named-file-baseline, `83eab02a70e7757e11f04f46a64849f69ba64df0`.
- Owned unstaged pending paths only: tests/integration/test_cli.py; tests/unit/test_files.py. Diff: two files, 138 insertions, 4 deletions. No staged entries, untracked files, conflicts or merge state observed.
- Production files, README, TASKS, PLAN and SPEC unchanged. No task checkbox or parent completion claimed.
- No task commit/push made; startup checkpoint already published. Final `git rev-list --left-right --count HEAD...origin/phase/1-named-file-baseline`: 0/0. Final ls-remote: phase1 83eab02, main `d769b55aa63f92d5ccbd8022cb9e87f07e541fae`.
- T-004 incomplete; T-005/T-006 not started. No phase merge/publication, new phase branch, hosted write or credential access.
- No reset, stash, clean or pending-work deletion. Raw RED logs retained. No native transcript invented.

## Resume handoff — not executed

After a separate resume instruction, preserve these tests and implement the T-004 CLI boundary: catch OSError/UnicodeDecodeError, emit a useful input-and-cause diagnostic to stderr, return 1, no success stdout/traceback. Existing API behavior needs no destructive reconstruction. Re-run current focused tests and required full discovery, update accurate error documentation and evidence, complete T-004 only when acceptance holds, scoped commit/push.

Then continue authorized T-005 documentation/distribution/phase exit checks and per-task commit/push. Before T-006, refresh actual main from local origin, inspect complete phase diff, merge verified phase1 into main with two parents, verify merged state and push/confirm main. Only then create phase2 from verified published main and implement/verify/push T-006 JSON output. Stop before T-007. No further operation is authorized while suspension remains active.

Full final suspension handoff: A-014-cross-final.md.
