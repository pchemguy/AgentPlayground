# A-017 final handoff

T-001 is complete, freshly verified, committed and pushed on `phase/1-named-file-baseline`. Stopped before T-002 and phase integration.

The interrupted task-owned change removed lone-CR normalization. Restored that normalization to match SPEC and the previously committed core, retained the independent regression test and recorded current acceptance alongside historical evidence in `docs/dev/TASKS.md`. The core now matches the original task commit; the new durable commit contains the added regression test and resumed evidence. Public counting/API docstrings remain accurate.

## Verification

Python 3.12.14 in `/workspace/scratch/sdd008-A-017/repo`:

- Before repair, `python -m unittest tests.test_regression -v` ran 1 test and failed the lone-CR expectation (1 line instead of 2).
- Before repair, `python -m unittest discover -s tests -v` ran 7 tests with 3 failures: two mixed-newline subtests and the lone-CR regression.
- After repair, the lone-CR regression passed 1 test; `python -m unittest tests.test_counting tests.test_api tests.test_regression -v` passed 7; full discovery passed 7. No skips or warnings.
- Direct public-import examples verified fixed lone-CR, BOM-only and mixed-terminator expectations and silent stdout/stderr.
- Diff whitespace checks passed. Documentation review found no contract amendment needed.

The independent tests cover empty/whitespace, Unicode whitespace, CR/LF/CRLF and trailing terminators, non-CR/LF Unicode separators, BOM defaults/preservation/interior retention, public imports, keyword-only option and immutable integer results. File IO, CLI, distribution and later phase conditions remain outside this task and were not claimed verified.

## Durable state and boundary

Commit: `8a204f97e930b61c95c646f5e897cf1fed742dd9` — `Retain lone-CR regression coverage and reverify counting (T-001)`.

Push to isolated local `origin` succeeded; remote phase tip exactly matches that commit. At startup the phase tip already matched `57234b333e533d6bd606d3c5dda7275cf74ddacf`, so no outstanding commits needed an initial push. Origin main remains unchanged at `e750d1c6f07a9e6cda49a7cf0924d2c605c82c0d`. Local `main` does not exist; target inspection commands for it failed, then `origin/main` and remote main were confirmed. This does not block the authorized partial-phase task checkpoint; no branch creation or merge was performed.

T-001 checked; T-002 through T-008 and milestone/phase parents remain unchecked. Tracked working tree and index are clean; pre-existing/generated Python bytecode caches remain untracked and were excluded from the commit. Hosted tracking is inactive, so no issue synchronization or closure was attempted. No unresolved T-001 acceptance failure remains.

The next eligible work is T-002, requiring a separate continuation request. The phase is incomplete; no phase integration, additional task or steering was started. Full action journal: `/workspace/scratch/acceptance-out-008/A-017.md`.
