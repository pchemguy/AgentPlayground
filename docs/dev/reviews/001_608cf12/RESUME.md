# Resume checkpoint for campaign 001_608cf12

## Stop boundary

Suspended by the user on 2026-10-02. All consumer agents stopped; no hosted writes are in flight or uncertain. Do not start further work until a resume instruction. State:6 Passed,2 Suspended,19 Pending,0 Running/Failed/Blocked. See [ACCEPTANCE-REPORT.md](ACCEPTANCE-REPORT.md) and [case registry](acceptance/cases.json).

The source revision is campaign008_98a5562 in pchemguy/Skill-SDD-Manager, branch `revision/008_98a5562-runtime-acceptance`, target `feature/architecture-revision`. Its REVISION-REPORT.md is the authoritative revision checkpoint. Source boundary integration has not occurred.

## Live positive workflow

- Consumer path: `/workspace/scratch/AgentPlayground-sdd-008`; repository pchemguy/AgentPlayground, main at published `d769b55aa63f92d5ccbd8022cb9e87f07e541fae`; clean.
- Pinned portable package: `vendor/sdd-manager`, source `529e98d4d3cd7002e3a49e34394552a44bf0a8d0`; provenance/hashes in `vendor/PROVENANCE.json`. Explicit source loading; no installed-client discovery claim.
- Governing documents prepared; T-001–T-008 all unchecked. No product implementation on main. A-001/A-002 independently passed.
- A-003 first projection incomplete: phase1/2 labels exist; milestone1.1/1.2/2.1/2.2 map to native milestone1/2/3/4. T-001 connector create failed403, Resource not accessible by integration; no task issues confirmed, no uncertain effects. Drafts and exact parent IDs in [projection](runs/A-003/A-003-projection.json); [consumer handoff](runs/A-003/A-003-final.md).
- Resume A-003 with all-state reread, existing parent reuse and appropriate protected-client issue-access handling. Do not replay `A-003-parent-api.py`, a first-creation driver. Complete first projection/readback, then second idempotence/foreign-field preservation trial and assessment/publication before A-004.
- Main Git credential helper and ignored/untracked mode0600 `gh.tkn` existed locally at suspension. Tokens intentionally absent from tracked evidence. Recover credentials through manager if unavailable. Connector authentication and supplied PAT permissions are distinct; PAT Contents and metadata writes succeeded, PAT Issues write is untested.

## Isolated pending and completed task scenarios

| Case | Exact state | Continuation |
| --- | --- | --- |
| A-015 | `/workspace/scratch/sdd008-A-015/repo`, phase1 branch HEAD e750d1c; six owned files staged, T-001 checked,7 tests observed, controlled pre-commit rejection; hook intact; no commit/push | Fresh consumer resumes existing checked/verified task after deliberate controlled-hook release. Preserve files/evidence and identity; commit/push before any next work. Case stays Suspended until recovery independently assessed. |
| A-020 | `/workspace/scratch/sdd008-A-020/repo`, phase1 branch57234b3; owned T-001 commit published to isolated bare origin. Unrelated staged blob, untracked content and tracked unstaged README preserved | Case Passed; no T-002 or phase merge. Do not promote this scenario's code into live main. |

Both checkpoint bundles are self-contained and verified. [A-015 snapshot](runs/A-015/A-015-independent.json) retains six exact pending file contents, staged binary patch and commit hook. [A-020 snapshot](runs/A-020/A-020-independent.json) retains unrelated content/index intent and owned commit paths. Bytecode artifacts were transient and left in A-015's worktree; exclude from owned commit without deleting unrelated work.

## Restoration if local paths disappear

1. Clone published source revision, live consumer main and this evaluation branch separately. Recheck instructions/refs and keep oracle/evaluation contents out of fresh consumer contexts.
2. Verify `runs/A-015/A-015-checkpoint.bundle` and `runs/A-020/A-020-checkpoint.bundle` using `git bundle verify`. Each contains complete phase-branch history; clone each into a new isolated directory and create a separate local bare origin. Never redirect an isolated failure case to live GitHub.
3. A-015: restore each `owned_pending_files` entry from its independent JSON, stage exactly those six paths, restore the recorded pre-commit hook with executable permissions. Reproduce baseline e750d1c and verify task/index state; retain rejection evidence. Release only the deliberately controlled hook as part of the resumed recovery test.
4. A-020: restore the published owned commit from its bundle; restore `unrelated-staged.txt` content and stage it, leave `unrelated-unstaged.txt` untracked, restore README working content without staging. Compare with recorded state before relying on reconstruction. Record restoration as an intervention, not original execution.
5. Synthetic credential/verification fixtures can be recreated with `python -m tests.workflows.scenario_setup SOURCE BASELINE NEW_DEST --case A-025` or A-026 (original baseline61f9670), A-015/A-020 (original baselinee750d1c). NEW_DEST must not exist. A-024 controlled adapter is retained in its run; use a new ignored synthetic token and documented no-network session mechanism. Never reconstruct live credentials from records.

## Remaining sequence and evidence rules

Execute A-004–A-013 only after completed A-003. Remaining isolated cases A-014, A-016–A-019, A-021–A-023 and A-015 continuation still need actual consumer execution. A-027 final assessment is Pending. Resume follows the accepted source plan; do not fabricate unsupported client/injection passes or repair newly discovered plugin defects without accepted scope.

Commit/push each case assessment before dependent work. `tools/record_case.py` now requires all declared artifacts to exist and supports Suspended separately from Running. Case records retain action journals/full final handoffs and available tool results; no complete native transcript export is claimed. Fixture recreation script was consolidated after initial runs; maintain that provenance. Python3.12.14 was actually used;3.11 was not run. Final source integration remains explicit two-parent merge at completed authorized revision boundary.
