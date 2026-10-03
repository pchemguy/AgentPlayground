# Plain-output checkpoint amendment

Campaign: `003_d0eeeff`; focused human-commanded steering revision.
Full baseline: `d0eeeffc0432a45a603ef17cca457e9f04544876`.
Working branch: `revision/003_d0eeeff-remove-json`; paused target:
`phase/2-output-and-input-extensions`; remote: `origin`.

Objective: remove CLI JSON support and align current governing owners, code,
tests, README and maintained hosted scope. Retain exact plain output, public
whole-input APIs, strict complete UTF-8 decoding, BOM ownership, ranges,
errors/resources and planned source-independent stdin. Authoritative input:
human command and A-011 assessment, current SPEC/PLAN/TASKS.
Stable affected IDs: retired T-006/Milestone 2.1; retained T-010/T-011/Milestone
2.3; planned T-007/T-008 and incomplete Phase 2/Milestone 2.2.

State: amendment verified; commit/push/integration publication remain pending. No main task execution or phase completion.
Historical feature sources and existing verification evidence remain retained.

## Retired identity and historical evidence

T-006 and Milestone 2.1 are removed from the current executable hierarchy and phase exits. Their stable IDs are reserved permanently; no new completion is claimed. Existing hosted issue #6 and milestone #3 retain historical associations and state, with current retirement described explicitly. The following original checkpoint evidence remains historical and does not describe current supported behavior.

    - [x] Milestone 2.1 — JSON output
        - [x] T-006 — Add and verify JSON output
            Scope: CLI formatter/parser, CLI tests, README/docstrings and milestone 2.1 evidence. Depends on: T-005 and verified/published phase 1 integration.
            Outcome: `--json` emits the SPEC object/newline and composes with BOM policy, retaining default text and failure behavior. Evidence: stdlib parsed JSON keys/value types and fixed counts, default-output/channel regressions, documented demonstration and full discovery. Record the milestone decision evidence; pause on the phase branch if only 2.1 is requested.
            Checkpoint: milestone 2.1 / T-006 only on `phase/2-output-and-input-extensions`, from actual verified/published main `29c27580db73cf128c42ddb9535e6d8f5c38ed39`; target `main`, remote `origin`. Hosted association: [T-006 issue #6](https://github.com/pchemguy/AgentPlayground/issues/6). Phase 2 remains incomplete; T-007/T-008 are unstarted and excluded, with no phase merge at this boundary.
            Verified T-006 / milestone 2.1 (Python 3.12.14): `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.integration.test_cli.JsonCliTests -v` observed RED with 5 tests, 15 failures and one argparse SystemExit scenario error because `--json` was unsupported. After the parser/formatter change, `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.integration.test_cli -v` passed all 15 CLI tests; `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v` passed all 31 tests without skips/warnings. Real named-file subprocesses and stdlib parsing verify one object/newline, exactly lines/words integer keys, fixed empty/whitespace/Unicode/mixed/trailing-newline counts, BOM modes/option order, unchanged files, dash-prefixed paths, default text regressions and read/decode/usage channels. Permission denial is simulated narrowly at the CLI adapter under this privileged runner; real missing/directory/malformed-byte fixtures supplement it. Affected module/API docstrings, README links and heading spacing reviewed. README quick-start/JSON examples executed in a temporary directory: text `lines=1 words=2`, JSON (1,2), BOM stripped (2,2), BOM kept (2,3), all status 0 with empty stderr. This demonstration meets PLAN 2.1 and informs the next human continuation/amendment/stop decision; no further decision or usability feedback is inferred. Pause on the published phase branch before milestone 2.2; stdin still treats `-` as a filename.

## Amendment verification

- Test-first removal: `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.integration.test_cli.RemovedJsonCliTests -v` observed 3 tests/13 behavioral failures before production deletion, then the same 3 tests passed. Existing literal `--json` filename behavior passed characterization.
- Focused core/API/file/CLI/distribution checks passed 39 tests; mandatory `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v` passed 39 tests after the final scope correction, with no skips or warnings.
- Real module usage rejects removed JSON before acquiring valid/missing/directory inputs, with BOM/range combinations; help omits JSON and literal `-- --json` works. Retained literal range/BOM/EOF/Unicode/blank/mixed-newline cases, 5000-digit endpoint, malformed-range precedence, invalid UTF-8 before/after selection, unchanged files, API silence and owned-handle cleanup pass.
- Extracted distribution contains exactly five modules plus README, excludes infrastructure/credentials/bytecode, removes PYTHONPATH and asserts the deployed import path. Independent named-file/plain-output/API/selection/decode checks and four documented outputs pass. Checkout README quick-start, selected shell commands and API block execute successfully.
- Current governing documents/README/help/docstrings and dependencies inspected; JSON support is removed, historical evidence remains labeled. Markdown local links/heading spacing and `git diff --check` pass. Core/file/facade/entrypoint and pinned vendor bytes remain unchanged.

T-010/T-011 and Milestone 2.3 retained acceptance is freshly verified. T-009 and Phase 1 regressions pass; historical evidence is retained. T-007/T-008, Milestone 2.2 and Phase 2 remain incomplete. Permission denial remains narrowly simulated under the privileged runner and supplemented by real missing/directory/invalid-byte fixtures. No actual stdin implementation, acceptance or phase/main integration is claimed.
