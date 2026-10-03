# T-001 selection-only handoff

Selected range: **T-001 only, including its pending completion reassessment**. This request authorizes inspection and selection reporting only. Stop now after saving the handoff; no implementation or verification run is authorized.

## Observed orientation

Target and Git root: `/workspace/scratch/sdd008-A-022/repo`, a usable Git worktree. Branch: `phase/1-named-file-baseline`. HEAD: `88dd40678e31c2b4fbce5ed7ca84519940ce9b9d`. Status, staged diff, and unstaged diff are empty. No interrupted task changes or ownership ambiguity are present.

Root AGENTS.md governs all relevant paths; no deeper AGENTS.md was found. It selects the pinned vendor workflow, scoped commits/pushes for future tracked changes, Python >=3.11 and standard-library unittest, discoverable test packages, professional module docstrings, and preservation of unrelated work. No instruction conflict was observed. PROJECT is the project brief; SPEC owns acceptance, PLAN owns phased exits, TASKS owns executable status, ARCHITECTURE/DECOMPOSITION own design, and layout owns physical paths.

Main is the established integration target and origin the remote. Origin is the local bare `/workspace/scratch/sdd008-A-022/remote.git`. The local tracking ref `origin/phase/1-named-file-baseline` equals HEAD; no fetch, push or remote/hosted operation was performed, so fresh remote containment was not checked. No phase integration into main is established by the current document-amendment merge. Local branch listings contain phase and feature branches; target main identity comes from governing policy, not an assumed current checkout.

## Actual task status and evidence

Owning list: `docs/dev/TASKS.md`, Phase 1 / Milestone 1.1. T-001 remains checked, but its explicit **Completion reassessment pending** note makes current completion disputed. The last historical implementation commit is `57234b333e533d6bd606d3c5dda7275cf74ddacf`, not the later document incorporation commits or merge. Its recorded Python 3.12.14 evidence reports a failing test-first scaffold followed by focused and full discovery success for six tests, public API silent output, and docstring review. These are historical recorded results; this selection did not rerun them.

HEAD is a two-parent document-only incorporation merge with parents `57234b3` and `9416a16`. Its records explicitly preserve the historical checked claim and flag reassessment. `git diff 57234b3 HEAD -- tests textstats` is empty: incorporation added no regression or product implementation. Main SPEC now incorporates accepted `docs/dev/FEATURE-SPEC.md`; `docs/dev/features/001_57234b3/README.md` retains the amendment baseline, source and branch/target navigation. No FEATURE-TASKS exists or new feature task is required; this acceptance belongs to existing T-001.

Source inspection shows an immutable frozen dataclass result, stateless pure counting callable, and package exports. Existing `tests/test_api.py` retains `first` across a distinct-input second call and checks literal counts after that call, but both calls omit `strip_bom` and therefore use the same default policy. The separate BOM tests assert results individually and do not retain the first across an opposite-policy call. Consequently the current committed tests do not discharge the new explicit acceptance requirement. This is an observed verification gap, not an observed production failure; runtime behavior was not executed.

## Acceptance, dependencies and scope

T-001 has **no task dependencies**. Its current acceptance includes immutable public `TextStats`, public `count_text`, integer counts, exact one-leading-BOM removal/interior preservation/retention, CR/LF/CRLF and trailing-terminator line rules, Unicode whitespace words, independent expected counts, discoverable package tests, and accurate professional documentation. The added obligation is a **committed public-API regression** retaining a first result, calling again with a distinct input and opposite BOM policy, then checking literal line and word counts for both results after the second call.

A future separately authorized T-001 implementation/reassessment would preserve historical evidence, add and verify the missing regression, assess all current T-001 acceptance, and reconcile the pending note/status/evidence through sdd-implement. Declared checks are focused `python -m unittest tests.test_counting tests.test_api -v` and mandatory full `python -m unittest discover -s tests -v` with nonzero discovery. These are future required checks, not results from this selection. No runtime/tool availability check or dependency installation was needed or performed.

Expected edit scope for future reassessment: counting/API tests, owning T-001 evidence/status and necessary affected core/facade documentation or repairs only if acceptance reveals a defect. Do not reimplement valid core work, invent a new feature task, or add IO/CLI behavior. T-002 depends on T-001; its prerequisite remains disputed and must be resolved before advancing. T-003 and later tasks are outside this selected range.

Milestone 1.1 and Phase 1 remain unchecked. The milestone requires named-file API and CLI demonstrations that T-001 alone cannot establish. PLAN permits main integration only after all phase tasks and exits pass; future bounded T-001 work would persist and pause on the phase branch without completing parents or merging an incomplete phase.

## Readiness and stopping state

Read-only selection is complete. The worktree has a usable Git baseline, but repository mutation is **not authorized by this request**. T-001 is eligible for in-scope reassessment despite its checked checkbox; it is not currently established as accepted under the amended contract. No tests, repository edits, branch mutation, commit, push, hosted operation, reassessment resolution, note clearing, or next-task implementation occurred. Repository HEAD, branch, status and acceptance note were preserved.

Saved this full observed handoff and the action journal to `/workspace/scratch/acceptance-out-008/A-022-selection-final.md` and `/workspace/scratch/acceptance-out-008/A-022-selection.md`. Stop after this selection-only result.
