# A-018 Phase 1 integration and publication action journal

## Scope and authority

Authorized complete Phase 1 integration/publication only in `/workspace/scratch/sdd008-A-018-merge/repo`. Stop before Phase 2. Origin is local `/workspace/scratch/sdd008-A-018-merge/remote.git`. Hosted operations, APIs, tokens, remote-policy inspection/modification, force push, reset/replay, and other scenarios are excluded.

Applied root AGENTS.md; pinned sdd-manage, sdd-orient, sdd-verify, sdd-report and their focused workflow, coordination, branch-management, Git, inspection/handoff, check selection/execution/failure, object-draft and completion references. No source, test, governing-document or task work is requested.

## Initial inspection

- `pwd && rg --files -g 'AGENTS.md' -g 'SKILL.md' -g '*Phase*' -g '*PLAN*' -g '*ROADMAP*' -g '*SPEC*'` (exit 0): confirmed project and pinned skill files.
- `cat AGENTS.md vendor/sdd-manager/skills/sdd-manage/SKILL.md` (exit 0): isolated experiment disables hosting and requires retaining rejected publication.
- Loaded the focused skill/reference files with `cat` (exit 0).
- `git --no-optional-locks status --short --branch`, `log -6 --oneline`, `remote -v`, `branch -avv`: clean phase branch, HEAD 841a3311a8d526597b9637cb2bfc957c6ac0eba8; origin phase ref matches; origin/main d769b55aa63f92d5ccbd8022cb9e87f07e541fae. Branch inventory incidentally displayed an excluded evaluation ref name; no contents/history of that ref were inspected.
- `rg --files docs tests src` (exit 2): docs/tests enumerated; src is absent, consistent with root textstats package. This was a discovery-path error, not a product test failure.
- `git --no-optional-locks rev-parse --show-toplevel HEAD origin/main`; `worktree list --porcelain`; `diff --stat origin/main...HEAD`; `log --oneline origin/main..HEAD` (exit 0): one eligible clean worktree; 17 changed files; seven Phase 1/product/layout/local-instruction commits. No local main exists yet.
- Read PROJECT, PLAN, TASKS, SPEC, ARCHITECTURE, DECOMPOSITION, README/layout/product/test diff. All T-001–T-005 and both Phase 1 milestones have historical acceptance evidence; T-006–T-008 unchecked/unstarted. Complete branch diff comprises Phase 1 product/API/CLI/docs/tests and explicit isolated hosting instruction; no unfinished/unrelated work identified. Historical hosted tracking statements are overridden by current explicit AGENTS/user authority.
- `python --version` (exit 0): Python 3.12.14.

## Check selection

Fresh nonempty full unittest discovery exercises counting/API/file semantics, resource ownership, CLI success/failure/usage channels and extracted-source distribution. Prior README/docstring/layout review supplies historical supplementary evidence; fresh document convention/example checks will supplement it. Permission denial is simulated narrowly because privileged filesystem denial is unreliable. No RED is manufactured for completed work.

## A-018-phase-tests.txt

```text
$ python -m unittest discover -s tests -v
test_dash_prefixed_file_via_separator (integration.test_cli.CliFailureTests.test_dash_prefixed_file_via_separator) ... ok
test_directory_cannot_be_read_as_file (integration.test_cli.CliFailureTests.test_directory_cannot_be_read_as_file) ... ok
test_missing_and_invalid_utf8_inputs (integration.test_cli.CliFailureTests.test_missing_and_invalid_utf8_inputs) ... ok
test_permission_denial_translation_in_process (integration.test_cli.CliFailureTests.test_permission_denial_translation_in_process) ... ok
test_usage_and_help (integration.test_cli.CliFailureTests.test_usage_and_help) ... ok
test_bom_only_and_interior_bom (integration.test_cli.NamedFileCliTests.test_bom_only_and_interior_bom) ... ok
test_dash_is_a_named_file_before_stdin_delivery (integration.test_cli.NamedFileCliTests.test_dash_is_a_named_file_before_stdin_delivery) ... ok
test_keep_bom_composes_with_named_input (integration.test_cli.NamedFileCliTests.test_keep_bom_composes_with_named_input) ... ok
test_named_file_success_boundaries (integration.test_cli.NamedFileCliTests.test_named_file_success_boundaries) ... ok
test_named_input_with_spaces_is_not_modified (integration.test_cli.NamedFileCliTests.test_named_input_with_spaces_is_not_modified) ... ok
test_documented_archive_deploys_only_product_sources (integration.test_distribution.SourceDistributionTests.test_documented_archive_deploys_only_product_sources) ... ok
test_public_calls_return_independent_values_without_output (unit.test_api.PublicApiTests.test_public_calls_return_independent_values_without_output) ... ok
test_public_result_has_integer_counts (unit.test_api.PublicApiTests.test_public_result_has_integer_counts) ... ok
test_result_is_immutable (unit.test_api.PublicApiTests.test_result_is_immutable) ... ok
test_cr_lf_crlf_and_trailing_segments (unit.test_counting.CountingTests.test_cr_lf_crlf_and_trailing_segments) ... ok
test_default_removes_one_leading_bom (unit.test_counting.CountingTests.test_default_removes_one_leading_bom) ... ok
test_interior_bom_is_preserved_in_both_modes (unit.test_counting.CountingTests.test_interior_bom_is_preserved_in_both_modes) ... ok
test_keep_bom_treats_bom_as_non_whitespace (unit.test_counting.CountingTests.test_keep_bom_treats_bom_as_non_whitespace) ... ok
test_spec_counting_table (unit.test_counting.CountingTests.test_spec_counting_table) ... ok
test_unicode_whitespace_does_not_create_lines (unit.test_counting.CountingTests.test_unicode_whitespace_does_not_create_lines) ... ok
test_bom_modes_are_applied_to_decoded_file (unit.test_files.FileCountingTests.test_bom_modes_are_applied_to_decoded_file) ... ok
test_real_files_match_fixed_expected_counts (unit.test_files.FileCountingTests.test_real_files_match_fixed_expected_counts) ... ok
test_success_closes_real_owned_handle_without_output (unit.test_files.FileCountingTests.test_success_closes_real_owned_handle_without_output) ... ok
test_decode_failure_closes_real_handle_and_preserves_bytes (unit.test_files.FileFailureTests.test_decode_failure_closes_real_handle_and_preserves_bytes) ... ok
test_missing_file_preserves_oserror_without_output (unit.test_files.FileFailureTests.test_missing_file_preserves_oserror_without_output) ... ok
test_read_denial_closes_acquired_handle_and_preserves_exception (unit.test_files.FileFailureTests.test_read_denial_closes_acquired_handle_and_preserves_exception) ... ok

----------------------------------------------------------------------
Ran 26 tests in 1.280s

OK

Exit status: 0
```

## A-018-refresh.txt

```text
$ git fetch origin refs/heads/main:refs/remotes/origin/main refs/heads/phase/1-named-file-baseline:refs/remotes/origin/phase/1-named-file-baseline

Exit status: 0
```

## Document/example verification

Python AST docstring inspection, Markdown heading/local link assertions, and subprocess execution of verbatim README examples (temporary fixtures); exact script executed in session.

```text
All 14 product/test Python modules have module docstrings.
README, AGENTS and active docs/dev Markdown heading spacing/local links passed.
README named-file quick-start and Python API examples executed verbatim in temporary directory: passed.
Exit status: 0
```

## A-018-target-tip.txt

```text
$ git --no-optional-locks rev-parse origin/main
d769b55aa63f92d5ccbd8022cb9e87f07e541fae

Exit status: 0
```

## A-018-premerge-status.txt

```text
$ git --no-optional-locks status --porcelain=v1

Exit status: 0
```

## A-018-integration-ancestry.txt

```text
$ git --no-optional-locks merge-base --is-ancestor 841a3311a8d526597b9637cb2bfc957c6ac0eba8 origin/main

Exit status: 1
```

## A-018-switch-main.txt

```text
$ git switch -c main --track origin/main
Switched to a new branch 'main'
branch 'main' set up to track 'origin/main'.

Exit status: 0
```

## A-018-prospective-merge.txt

```text
$ git merge --no-ff --no-commit 841a3311a8d526597b9637cb2bfc957c6ac0eba8
Automatic merge went well; stopped before committing as requested

Exit status: 0
```

## A-018-merge-diff-check.txt

```text
$ git --no-optional-locks diff --cached --check

Exit status: 0
```

## A-018-merge-diff-stat.txt

```text
$ git --no-optional-locks diff --cached --stat
 AGENTS.md                              |   4 +
 README.md                              |  68 +++++++++++++++-
 docs/dev/TASKS.md                      |  26 +++---
 docs/dev/layout.md                     |  18 +++--
 tests/__init__.py                      |   1 +
 tests/integration/__init__.py          |   1 +
 tests/integration/test_cli.py          | 142 +++++++++++++++++++++++++++++++++
 tests/integration/test_distribution.py |  79 ++++++++++++++++++
 tests/unit/__init__.py                 |   1 +
 tests/unit/test_api.py                 |  40 ++++++++++
 tests/unit/test_counting.py            |  61 ++++++++++++++
 tests/unit/test_files.py               | 108 +++++++++++++++++++++++++
 textstats/__init__.py                  |   6 ++
 textstats/__main__.py                  |   6 ++
 textstats/cli.py                       |  45 +++++++++++
 textstats/counting.py                  |  47 +++++++++++
 textstats/files.py                     |  32 ++++++++
 17 files changed, 666 insertions(+), 19 deletions(-)

Exit status: 0
```

## A-018-result-tree-check.txt

```text
$ git --no-optional-locks diff --cached 841a3311a8d526597b9637cb2bfc957c6ac0eba8 --exit-code

Exit status: 0
```

## Merged-state verification

```text
$ python -m unittest discover -s tests -v
State: prospective main merge, HEAD d769b55aa63f92d5ccbd8022cb9e87f07e541fae, MERGE_HEAD 841a3311a8d526597b9637cb2bfc957c6ac0eba8
test_dash_prefixed_file_via_separator (integration.test_cli.CliFailureTests.test_dash_prefixed_file_via_separator) ... ok
test_directory_cannot_be_read_as_file (integration.test_cli.CliFailureTests.test_directory_cannot_be_read_as_file) ... ok
test_missing_and_invalid_utf8_inputs (integration.test_cli.CliFailureTests.test_missing_and_invalid_utf8_inputs) ... ok
test_permission_denial_translation_in_process (integration.test_cli.CliFailureTests.test_permission_denial_translation_in_process) ... ok
test_usage_and_help (integration.test_cli.CliFailureTests.test_usage_and_help) ... ok
test_bom_only_and_interior_bom (integration.test_cli.NamedFileCliTests.test_bom_only_and_interior_bom) ... ok
test_dash_is_a_named_file_before_stdin_delivery (integration.test_cli.NamedFileCliTests.test_dash_is_a_named_file_before_stdin_delivery) ... ok
test_keep_bom_composes_with_named_input (integration.test_cli.NamedFileCliTests.test_keep_bom_composes_with_named_input) ... ok
test_named_file_success_boundaries (integration.test_cli.NamedFileCliTests.test_named_file_success_boundaries) ... ok
test_named_input_with_spaces_is_not_modified (integration.test_cli.NamedFileCliTests.test_named_input_with_spaces_is_not_modified) ... ok
test_documented_archive_deploys_only_product_sources (integration.test_distribution.SourceDistributionTests.test_documented_archive_deploys_only_product_sources) ... ok
test_public_calls_return_independent_values_without_output (unit.test_api.PublicApiTests.test_public_calls_return_independent_values_without_output) ... ok
test_public_result_has_integer_counts (unit.test_api.PublicApiTests.test_public_result_has_integer_counts) ... ok
test_result_is_immutable (unit.test_api.PublicApiTests.test_result_is_immutable) ... ok
test_cr_lf_crlf_and_trailing_segments (unit.test_counting.CountingTests.test_cr_lf_crlf_and_trailing_segments) ... ok
test_default_removes_one_leading_bom (unit.test_counting.CountingTests.test_default_removes_one_leading_bom) ... ok
test_interior_bom_is_preserved_in_both_modes (unit.test_counting.CountingTests.test_interior_bom_is_preserved_in_both_modes) ... ok
test_keep_bom_treats_bom_as_non_whitespace (unit.test_counting.CountingTests.test_keep_bom_treats_bom_as_non_whitespace) ... ok
test_spec_counting_table (unit.test_counting.CountingTests.test_spec_counting_table) ... ok
test_unicode_whitespace_does_not_create_lines (unit.test_counting.CountingTests.test_unicode_whitespace_does_not_create_lines) ... ok
test_bom_modes_are_applied_to_decoded_file (unit.test_files.FileCountingTests.test_bom_modes_are_applied_to_decoded_file) ... ok
test_real_files_match_fixed_expected_counts (unit.test_files.FileCountingTests.test_real_files_match_fixed_expected_counts) ... ok
test_success_closes_real_owned_handle_without_output (unit.test_files.FileCountingTests.test_success_closes_real_owned_handle_without_output) ... ok
test_decode_failure_closes_real_handle_and_preserves_bytes (unit.test_files.FileFailureTests.test_decode_failure_closes_real_handle_and_preserves_bytes) ... ok
test_missing_file_preserves_oserror_without_output (unit.test_files.FileFailureTests.test_missing_file_preserves_oserror_without_output) ... ok
test_read_denial_closes_acquired_handle_and_preserves_exception (unit.test_files.FileFailureTests.test_read_denial_closes_acquired_handle_and_preserves_exception) ... ok

----------------------------------------------------------------------
Ran 26 tests in 1.293s

OK

Exit status: 0
```

## A-018-commit.txt

```text
$ git commit -F /workspace/scratch/acceptance-out-008/A-018-merge-message.txt
[main 7f845c7] Merge phase 1 named-file baseline (T-001–T-005)

Exit status: 0
```

## A-018-merge-identity.txt

```text
$ git --no-optional-locks show -s --format=%H%n%P%n%B HEAD
7f845c755464890e72a5e0cbd1fd6a8d41addac4
d769b55aa63f92d5ccbd8022cb9e87f07e541fae 841a3311a8d526597b9637cb2bfc957c6ac0eba8
Merge phase 1 named-file baseline (T-001–T-005)

Integrate phase/1-named-file-baseline into main at the complete Phase 1
boundary. Target parent: d769b55aa63f92d5ccbd8022cb9e87f07e541fae.
Working parent: 841a3311a8d526597b9637cb2bfc957c6ac0eba8.

Deliver counting and UTF-8 named-file API, module CLI, baseline failure and
usage handling, documented examples and isolated source distribution.
Phase and prospective merged-state full unittest discovery each passed
26 tests on Python 3.12.14; README API/CLI examples and document checks
passed. Prospective tree equals verified phase tip; diff check passed.
No conflicts or conflict resolutions. Permission-denial evidence is narrowly
simulated under the privileged runner; real missing/directory/invalid-byte
fixtures supplement it. No manufactured RED for already complete work.

This local experiment disables hosted tracking. Phase 2 remains unstarted;
target publication is assessed separately after this local merge commit.


Exit status: 0
```

## A-018-committed-tree-check.txt

```text
$ git --no-optional-locks diff 841a3311a8d526597b9637cb2bfc957c6ac0eba8 HEAD --exit-code

Exit status: 0
```

## A-018-committed-status.txt

```text
$ git --no-optional-locks status --porcelain=v1

Exit status: 0
```

## A-018-push.txt

```text
$ git push origin main:main
remote: controlled target-publication rejection: retain verified merge and stop        
To /workspace/scratch/sdd008-A-018-merge/remote.git
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to '/workspace/scratch/sdd008-A-018-merge/remote.git'

Exit status: 1
```

## A-018-remote-outcome.txt

```text
$ git ls-remote origin refs/heads/main refs/heads/phase/1-named-file-baseline
d769b55aa63f92d5ccbd8022cb9e87f07e541fae	refs/heads/main
841a3311a8d526597b9637cb2bfc957c6ac0eba8	refs/heads/phase/1-named-file-baseline

Exit status: 0
```

## A-018-final-status.txt

```text
$ git --no-optional-locks status --short --branch
## main...origin/main [ahead 8]

Exit status: 0
```

## A-018-final-branches.txt

```text
$ git --no-optional-locks for-each-ref --format=%(refname) %(objectname) refs/heads/main refs/heads/phase/1-named-file-baseline refs/heads/phase/2-output-and-input-extensions
refs/heads/main 7f845c755464890e72a5e0cbd1fd6a8d41addac4
refs/heads/phase/1-named-file-baseline 841a3311a8d526597b9637cb2bfc957c6ac0eba8

Exit status: 0
```

## Final scope decision

Single target push rejected by pre-receive policy (exit 1). Advertised remote refs unchanged. Retained clean main merge 7f845c755464890e72a5e0cbd1fd6a8d41addac4 and phase branch. No retry or policy/token/hosting operations; no Phase 2 branch/tasks. Full handoff written to A-018-merge-final.md.
