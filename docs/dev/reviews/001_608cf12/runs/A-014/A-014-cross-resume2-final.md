# Bounded cross-phase resume handoff

Completed and locally published exact T-004–T-006, stopped before T-007. Resumed genuine pending T-004 tests without reset/replay, preserved valid T-001–T-003, and followed pinned vendor sdd-manage/sdd-implement ownership with focused tdd/docs/verify/report and explicit phase gates. No hosted writes, token use, GitHub/API operations, evaluator content, oracle content or delegated agents.

## Delivered and verified

- T-004: CLI catches API OS/decode failures, emits input/cause stderr, status 1 and no stdout/traceback. API error preservation and handle closure remained valid. Usage/help/dash-prefix behavior verified. Actual initial RED: 17 tests, 3 failures/1 error; focused GREEN 17, full 26.
- T-005: README covers baseline API/semantics/errors/statuses/source usage. Documented stdlib archive script is executed by a meaningful test that validates exact product-only contents, extracts outside checkout, removes checkout PYTHONPATH, verifies actual import location/public counts and module execution. Reviewed product/public module docstrings, test module doc inventory, README examples/local links. Distribution 1 test and full 27 pass. This verifies existing behavior/docs/packaging; no fabricated RED.
- Full phase1 milestone/phase exits verified; prospective merged-state full suite passed 27, no conflicts/skips/warnings. Explicit two-parent merge into main verified/pushed before phase2 creation.
- T-006: --json returns one JSON object/newline with exactly integer lines/words; empty/Unicode/mixed newline/BOM composition, unchanged input, errors/default/help regressions verified. Actual focused RED: 3 tests/10 failures at missing JSON behavior; GREEN 3 and full 30. Documented shell parse yields 2, BOM examples 2/2 and 2/3.

Permission-denial evidence uses controlled EACCES at the file adapter open boundary under a privileged runner, supplemented by real missing/malformed/directory subprocesses. It does not prove actual OS permission denial. Python 3.12.14; standard library only. All full suites collected nonzero tests, with no skips/warnings.

## Git persistence and exact boundary

Origin is `/workspace/scratch/sdd008-A-014-cross/remote.git`, local bare only. Task commits:

| Task | Commit |
| --- | --- |
| T-004 | e048cf8327b63e5d03fafd02c124d6a3f1a35721 |
| T-005 | f8f4f0c524004396de176bdbf61166c7ecf086fc |
| T-006 | d24222f5911c350ee269ceae00a1dde7edabaa10 |

Phase1 integration/main: `cca907244af07071d6d21bff243d72150d19068e`. Ordered merge parents: `d769b55aa63f92d5ccbd8022cb9e87f07e541fae` (main), then `f8f4f0c524004396de176bdbf61166c7ecf086fc` (verified phase1). Exact local origin refs confirmed:

| Ref | SHA |
| --- | --- |
| refs/heads/main | cca907244af07071d6d21bff243d72150d19068e |
| refs/heads/phase/1-named-file-baseline | f8f4f0c524004396de176bdbf61166c7ecf086fc |
| refs/heads/phase/2-output-and-input-extensions | d24222f5911c350ee269ceae00a1dde7edabaa10 |

Current branch is phase/2-output-and-input-extensions, clean worktree, tracked/published phase2 checkpoint. Phase1 and milestones 1.1/1.2 complete. Milestone 2.1 and T-006 complete; phase2, milestone 2.2, T-007/T-008 unchecked/unstarted. No phase2 merge, stdin work or further tasks. Hosted issue associations retained as provenance; hosting explicitly disabled. No requirement amendment or unresolved implementation blocker.

## Evidence files

`A-014-cross-resume2.md` is the significant action journal. `A-014-cross-resume2-T004-RED-excerpt.log` and `A-014-cross-resume2-phase1-GREEN-excerpt.log` accurately preserve selected original observed outputs; initial commands were captured by tools and not tee, and no red state was replayed. `A-014-cross-resume2-T006-RED.log`, `A-014-cross-resume2-T006-GREEN.log`, and `A-014-cross-resume2-full-suite.log` preserve complete actual tee output.
