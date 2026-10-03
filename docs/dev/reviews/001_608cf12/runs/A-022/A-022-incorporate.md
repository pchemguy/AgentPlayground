# Selected feature incorporation action journal

Request: read A-022-prompt.txt only; incorporate accepted FEATURE-SPEC into SPEC and existing T-001 in TASKS. No implementation, hosted operations, token, source archive or new agents.

Orientation: eligible clean worktree /workspace/scratch/sdd008-A-022/repo, feature/001_57234b3-call-independence at 9c033dd11e79ed21e0bc2e3dcd1ce7463b5927c6. Campaign README establishes full baseline 57234b333e533d6bd606d3c5dda7275cf74ddacf and target phase/1-named-file-baseline at same SHA. Origin is local bare fixture; ls-remote confirms source/target publication. Applicable root AGENTS and pinned manage/integrate-feature/orient/conventions/report/verify instructions read. Current SPEC/TASKS, accepted FEATURE-SPEC, campaign record, PLAN/PROJECT, historical T-001 commit and actual tests inspected.

Existing six tests include successive calls but no opposite-BOM-policy retained-result regression. Historical T-001 evidence remains valid within prior scope, insufficient for the accepted explicit requirement. Phase/milestone unchecked; only T-001 checkbox preserved pending reassessment. Main target not eligible for phase integration. Full source-vs-phase diff initially contains accepted FEATURE-SPEC plus campaign README only; no unrelated work.

Selected edits: SPEC adds bidirectional successive-call independence and exact retained-result acceptance. TASKS updates T-001 evidence plan, adds Completion reassessment pending with authoritative sources/prior commit/required owner, preserves checkbox and historical evidence byte-for-byte. Intro reconciled with existing checked evidence. T-002..T-008 unchanged. FEATURE-SPEC/campaign records retained unchanged; no source archival authorized.

Verification commands: `git diff --check` exit 0; scoped diff inspected (SPEC +4 lines, TASKS +3/-2); `python -m unittest discover -s tests -v` exit 0, six tests passed. These are baseline regressions, not new accepted requirement completion. Structural Python assertions passed: selected paths only, unchanged historical line/T-002 onward/task checkboxes, links resolve, blank lines around headings.

Command: `git add -- docs/dev/SPEC.md docs/dev/TASKS.md`; exit 0.

```text
```

Command: `git commit -m 'Incorporate call-independence acceptance (T-001)' -m 'Update SPEC and T-001 acceptance from the accepted FEATURE-SPEC. Preserve the historical checkbox and six-test evidence with a pending reassessment note. Document structure, links, scoped diff and existing six-test discovery pass; the new retained-result regression is pending implementation.'`; exit 0.

```text
[feature/001_57234b3-call-independence 9416a16] Incorporate call-independence acceptance (T-001)
 2 files changed, 7 insertions(+), 2 deletions(-)
```

Command: `git rev-parse HEAD`; exit 0.

```text
9416a16fe5b2f0325e7c63d47647786577a3fe7b
```

Command: `git push origin HEAD:refs/heads/feature/001_57234b3-call-independence`; exit 0.

```text
To /workspace/scratch/sdd008-A-022/remote.git
   9c033dd..9416a16  HEAD -> feature/001_57234b3-call-independence
```

Command: `git ls-remote origin refs/heads/feature/001_57234b3-call-independence`; exit 0.

```text
9416a16fe5b2f0325e7c63d47647786577a3fe7b	refs/heads/feature/001_57234b3-call-independence
```

Command: `git fetch origin phase/1-named-file-baseline`; exit 0.

```text
From /workspace/scratch/sdd008-A-022/remote
 * branch            phase/1-named-file-baseline -> FETCH_HEAD
```

Command: `git rev-parse origin/phase/1-named-file-baseline`; exit 0.

```text
57234b333e533d6bd606d3c5dda7275cf74ddacf
```

Command: `git switch phase/1-named-file-baseline`; exit 0.

```text
Your branch is up to date with 'origin/phase/1-named-file-baseline'.
Switched to branch 'phase/1-named-file-baseline'
```

Command: `git rev-parse HEAD`; exit 0.

```text
57234b333e533d6bd606d3c5dda7275cf74ddacf
```

Command: `git status --porcelain=v1`; exit 0.

```text
?? tests/__pycache__/
?? textstats/__pycache__/
```

Post-test status exposed generated untracked tests/__pycache__ and textstats/__pycache__; merge had not started. Confirmed paths untracked and removed only these operation-owned Python caches. Subsequent checks use python -B to avoid recurrence.

Command: `git rev-parse HEAD`; exit 0.

```text
57234b333e533d6bd606d3c5dda7275cf74ddacf
```

Command: `git rev-parse feature/001_57234b3-call-independence`; exit 0.

```text
9416a16fe5b2f0325e7c63d47647786577a3fe7b
```

Command: `git status --porcelain=v1`; exit 0.

```text
```

Command: `git diff --name-only 57234b333e533d6bd606d3c5dda7275cf74ddacf 9416a16fe5b2f0325e7c63d47647786577a3fe7b`; exit 0.

```text
docs/dev/FEATURE-SPEC.md
docs/dev/SPEC.md
docs/dev/TASKS.md
docs/dev/features/001_57234b3/README.md
```

Command: `git merge --no-ff --no-commit 9416a16fe5b2f0325e7c63d47647786577a3fe7b`; exit 0.

```text
Automatic merge went well; stopped before committing as requested
```

Command: `git diff --cached --check`; exit 0.

```text
```

Command: `git diff --cached --stat`; exit 0.

```text
 docs/dev/FEATURE-SPEC.md                | 13 +++++++++++++
 docs/dev/SPEC.md                        |  4 ++++
 docs/dev/TASKS.md                       |  5 +++--
 docs/dev/features/001_57234b3/README.md |  3 +++
 4 files changed, 23 insertions(+), 2 deletions(-)
```

Command: `python -B -m unittest discover -s tests -v`; exit 0.

```text
test_package_level_counting_api (test_api.PublicApiTests.test_package_level_counting_api) ... ok
test_bom_policy (test_counting.CountingTests.test_bom_policy) ... ok
test_counting_boundaries (test_counting.CountingTests.test_counting_boundaries) ... ok
test_default_removes_one_leading_bom (test_counting.CountingTests.test_default_removes_one_leading_bom) ... ok
test_option_is_keyword_only (test_counting.CountingTests.test_option_is_keyword_only) ... ok
test_result_fields_are_nonnegative_integers_and_immutable (test_counting.CountingTests.test_result_fields_are_nonnegative_integers_and_immutable) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

Command: `git diff --name-only --diff-filter=U`; exit 0.

```text
```

Prospective merge verified: target 57234b333e533d6bd606d3c5dda7275cf74ddacf; working 9416a16fe5b2f0325e7c63d47647786577a3fe7b. No conflicts, full branch difference contains only selected SPEC/TASKS and previously accepted feature source/navigation. Six existing regression tests pass; new explicit acceptance still pending and TASKS note retained.

Command: `git write-tree`; exit 0.

```text
f804839edba563addb4c3ac5e55f95445b779e89
```

Command: `git rev-parse '9416a16fe5b2f0325e7c63d47647786577a3fe7b^{tree}'`; exit 0.

```text
f804839edba563addb4c3ac5e55f95445b779e89
```

Command: `git commit -m 'Merge call-independence document incorporation (T-001)' -m 'Incorporate the accepted SPEC and existing T-001 acceptance only; retain active FEATURE-SPEC and campaign navigation. Preserve historical task checkbox/evidence and flag completion reassessment pending.

Working: feature/001_57234b3-call-independence at 9416a16fe5b2f0325e7c63d47647786577a3fe7b.
Target: phase/1-named-file-baseline at 57234b333e533d6bd606d3c5dda7275cf74ddacf.
Baseline: 57234b333e533d6bd606d3c5dda7275cf74ddacf.

Working and prospective merged states passed document scope/link/evidence checks, git diff --check, and full unittest discovery (6 tests). No conflicts. Merge tree equals verified working tree. New retained-result regression and T-001 reassessment remain pending; no product or test implementation, task completion, phase completion or integration into main.'`; exit 0.

```text
[phase/1-named-file-baseline 88dd406] Merge call-independence document incorporation (T-001)
```

Command: `git rev-parse HEAD`; exit 0.

```text
88dd40678e31c2b4fbce5ed7ca84519940ce9b9d
```

Command: `git show -s --format=%P HEAD`; exit 0.

```text
57234b333e533d6bd606d3c5dda7275cf74ddacf 9416a16fe5b2f0325e7c63d47647786577a3fe7b
```

Command: `git status --porcelain=v1`; exit 0.

```text
```

Command: `git push origin HEAD:refs/heads/phase/1-named-file-baseline`; exit 0.

```text
To /workspace/scratch/sdd008-A-022/remote.git
   57234b3..88dd406  HEAD -> phase/1-named-file-baseline
```

Command: `git ls-remote origin refs/heads/phase/1-named-file-baseline refs/heads/feature/001_57234b3-call-independence refs/heads/main`; exit 0.

```text
9416a16fe5b2f0325e7c63d47647786577a3fe7b	refs/heads/feature/001_57234b3-call-independence
e750d1c6f07a9e6cda49a7cf0924d2c605c82c0d	refs/heads/main
88dd40678e31c2b4fbce5ed7ca84519940ce9b9d	refs/heads/phase/1-named-file-baseline
```

Complete final handoff saved as A-022-incorporate-final.md. Both remote refs confirmed; clean phase checkout. Stop at selected document incorporation and publication.
Final read-only check: ARCHITECTURE has invocation-owned results; DECOMPOSITION has new immutable values per call; layout owns public API tests. No conflict or unselected edit. Git diff of tests/textstats against starting phase checkpoint empty; final porcelain status empty.
