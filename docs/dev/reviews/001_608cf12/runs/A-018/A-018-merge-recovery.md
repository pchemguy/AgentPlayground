# A-018 merge publication recovery journal

Authorized continuation: existing Phase 1 integration/publication only in `/workspace/scratch/sdd008-A-018-merge/repo`, origin `/workspace/scratch/sdd008-A-018-merge/remote.git`. Hosting disabled; no API/token access, force/reset, server-policy access, new agents, or Phase 2 operations.

## Initial inspection (recorded after the commands; factual summaries, not a native transcript)

- `pwd; rg --files -g AGENTS.md -g '*journal*' -g '*handoff*' -g '*A-018*' -g '*PLAN*' -g '*SPEC*'` exited 0. Located root instructions, governing SPEC/PLAN and pinned orientation reference.
- `cat AGENTS.md; cat vendor/sdd-manager/skills/sdd-manage/SKILL.md; git status --short --branch; git log -8 --oneline; git remote -v` exited 0. Clean main was ahead 8; HEAD was existing two-parent Phase 1 merge `7f845c755464890e72a5e0cbd1fd6a8d41addac4`. Origin is the authorized local bare path. Initial status command was plain git; subsequent inspection uses optional writes suppressed.
- Read pinned sdd-orient and its inspection/handoff reference; sdd-manage workflows, coordination, branch-management and git-workflows; sdd-report and completion-reports; sdd-verify plus check-selection, execution-and-evidence and failure-assessment. These explicitly require continuing a committed merge awaiting publication without making a second merge and stopping before the next phase.
- Read PROJECT, TASKS, PLAN, SPEC, ARCHITECTURE, layout, README, and source-distribution acceptance test. T-001–T-005 and Phase 1 exits have prior committed evidence. T-006–T-008 remain unchecked and outside scope. TASKS historical GitHub associations are provenance; scoped AGENTS hosting prohibition governs.
- `git --no-optional-locks show --format=fuller --stat HEAD; git --no-optional-locks branch -avv; git --no-optional-locks status --porcelain=v1; git --no-optional-locks ls-files -u` exited 0. Existing merge parents: `d769b55aa63f92d5ccbd8022cb9e87f07e541fae` and `841a3311a8d526597b9637cb2bfc957c6ac0eba8`. No dirty paths or unresolved entries. Phase branch is retained at second parent. Broad branch listing incidentally displayed an evaluation ref name; its content was not read or used, and subsequent ref inspection is explicitly restricted to main and Phase 1.

## Orientation and scope decision

Project and Git root are the requested repository. Mutation baseline is eligible: clean main, established origin, no unresolved merge, explicit publication authorization. Last task commit is T-005 `964e72b`; later `841a331` isolates hosting policy and `7f845c7` is the existing integration boundary. No pending task or product edit. Continue publication of the existing merge, assess merged-state regressions, retain Phase 1 branch, and stop on main. No new commit or merge is needed unless actual divergence warrants it.

## Captured subsequent commands and outputs

### `git fetch origin refs/heads/main:refs/remotes/origin/main refs/heads/phase/1-named-file-baseline:refs/remotes/origin/phase/1-named-file-baseline`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
(no output)
```

### `git --no-optional-locks rev-parse --show-toplevel`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
/workspace/scratch/sdd008-A-018-merge/repo
```

### `git --no-optional-locks rev-list --parents -n 1 HEAD`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
7f845c755464890e72a5e0cbd1fd6a8d41addac4 d769b55aa63f92d5ccbd8022cb9e87f07e541fae 841a3311a8d526597b9637cb2bfc957c6ac0eba8
```

### `git --no-optional-locks rev-list --left-right --count origin/main...main`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
0	8
```

### `git --no-optional-locks merge-base --is-ancestor origin/main main`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
(no output)
```

### `git --no-optional-locks diff --exit-code main phase/1-named-file-baseline`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
(no output)
```

### `git --no-optional-locks diff --check 'HEAD^1' HEAD`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
(no output)
```

### `python --version`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
Python 3.12.14
```

### `python -m unittest discover -s tests -v`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
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
Ran 26 tests in 1.388s

OK
```

### `git push origin main:main`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
To /workspace/scratch/sdd008-A-018-merge/remote.git
   d769b55..7f845c7  main -> main
```

### `git ls-remote --heads origin main phase/1-named-file-baseline`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
7f845c755464890e72a5e0cbd1fd6a8d41addac4	refs/heads/main
841a3311a8d526597b9637cb2bfc957c6ac0eba8	refs/heads/phase/1-named-file-baseline
```

### `git --no-optional-locks rev-parse main origin/main phase/1-named-file-baseline origin/phase/1-named-file-baseline`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
7f845c755464890e72a5e0cbd1fd6a8d41addac4
7f845c755464890e72a5e0cbd1fd6a8d41addac4
841a3311a8d526597b9637cb2bfc957c6ac0eba8
841a3311a8d526597b9637cb2bfc957c6ac0eba8
```

### `git --no-optional-locks merge-base --is-ancestor phase/1-named-file-baseline origin/main`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
(no output)
```

### `git --no-optional-locks rev-list --left-right --count origin/main...main`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
0	0
```

### `git --no-optional-locks status --porcelain=v1 --untracked-files=all`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
?? tests/integration/__pycache__/__init__.cpython-312.pyc
?? tests/integration/__pycache__/test_cli.cpython-312.pyc
?? tests/integration/__pycache__/test_distribution.cpython-312.pyc
?? tests/unit/__pycache__/__init__.cpython-312.pyc
?? tests/unit/__pycache__/test_api.cpython-312.pyc
?? tests/unit/__pycache__/test_counting.cpython-312.pyc
?? tests/unit/__pycache__/test_files.cpython-312.pyc
?? textstats/__pycache__/__init__.cpython-312.pyc
?? textstats/__pycache__/cli.cpython-312.pyc
?? textstats/__pycache__/counting.cpython-312.pyc
?? textstats/__pycache__/files.cpython-312.pyc
```

### `git --no-optional-locks symbolic-ref --short HEAD`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
main
```

### `git --no-optional-locks for-each-ref '--format=%(refname) %(objectname)' 'refs/heads/phase/2*' 'refs/remotes/origin/phase/2*'`

Working directory: `/workspace/scratch/sdd008-A-018-merge/repo`. Exit: 0.

```text
(no output)
```

## Generated verification artifacts

Full discovery generated the 11 untracked `.pyc` files shown in the status output above. Initial status was clean. Removed exactly those owned generated files with `Path.unlink()`; no reset/clean or unrelated removal.

### `git --no-optional-locks status --short --branch`

Exit: 0.

```text
## main...origin/main
```

## Result and stopping boundary

Existing verified two-parent merge `7f845c755464890e72a5e0cbd1fd6a8d41addac4` was successfully published to origin main. Main and origin/main are equal; Phase 1 local/remote branch remains `841a3311a8d526597b9637cb2bfc957c6ac0eba8` and is an ancestor of published main. No new merge/commit, product/doc edit, Phase 2 ref/task, hosted action, credential access, server-policy access, force/reset, or additional agent. The remote recovery announcement required no policy inspection. Full current merged-state unittest discovery passed 26 tests on Python 3.12.14 with no skips/warnings. Narrow simulated permission denial remains the documented privileged-runner limitation. Stopped on clean main after verified Phase 1 publication.
