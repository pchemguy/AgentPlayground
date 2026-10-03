# Phase 1 merge publication handoff

Phase 1 (T-001–T-005) publication is complete. This continuation preserved and published the already existing explicit two-parent merge; it made no new commits or merges.

- Repository: `/workspace/scratch/sdd008-A-018-merge/repo`.
- Working phase branch: `phase/1-named-file-baseline`, retained at `841a3311a8d526597b9637cb2bfc957c6ac0eba8`, also the remote phase tip.
- Integration target: `main`, now published at `7f845c755464890e72a5e0cbd1fd6a8d41addac4`.
- Merge target parent: `d769b55aa63f92d5ccbd8022cb9e87f07e541fae`.
- Merge working parent: `841a3311a8d526597b9637cb2bfc957c6ac0eba8`.
- Task commits retained: T-001 `3b201a3`; T-002 `9042c20`; T-003 `8836c49`; T-004 `b9fabb0`; T-005 `964e72b`. Layout maintenance `0b97f4b` and isolated hosting policy `841a331` are preserved.

## Verification

`python -m unittest discover -s tests -v` exited 0 on Python 3.12.14, collected and passed 26 named tests with no skips/warnings. The journal contains the complete named test output. Coverage includes immutable public values, SPEC counting/BOM/newline boundaries, real UTF-8 named files and owned-handle cleanup, module subprocess channels/statuses, malformed inputs/usage/help/dash filenames, documented archive recipe, isolated extracted-source imports and CLI deployment. Privileged-runner permission denial is simulated narrowly at API/CLI boundaries as already documented; real missing/directory/malformed-byte fixtures supplement it.

Main and the Phase 1 tip have identical trees (`git --no-optional-locks diff --exit-code main phase/1-named-file-baseline`, exit 0). Merge diff whitespace check passed. Fresh origin fetch found no divergence (`0 8` before publication). Existing committed phase exit and README evidence was reused where unchanged, without presenting it as a new test-first cycle. No Phase 2 acceptance is claimed.

## Actual push and refs

`git push origin main:main` exited 0:

```text
To /workspace/scratch/sdd008-A-018-merge/remote.git
   d769b55..7f845c7  main -> main
```

`git ls-remote --heads origin main phase/1-named-file-baseline` exited 0:

```text
7f845c755464890e72a5e0cbd1fd6a8d41addac4 refs/heads/main
841a3311a8d526597b9637cb2bfc957c6ac0eba8 refs/heads/phase/1-named-file-baseline
```

Local main and origin/main resolve to the merge SHA. Phase 1 ancestry in origin/main check exited 0. Post-publication main/origin comparison is `0 0`. Final status is `## main...origin/main` with no dirty paths after removal of exactly the test-generated untracked bytecode files.

## Exact stopping point

Stopped on clean `main` immediately after verified Phase 1 publication. T-006–T-008 remain unchecked/unstarted; no Phase 2 local or remote-tracking branch is present. Hosted tracking remains disabled; no GitHub/API/token operation, server-policy inspection/edit, force push, reset, unrelated task or new agent. There is no unresolved Phase 1 publication blocker. Any Phase 2 work requires a separate instruction.

Detailed significant command/action/results journal: `/workspace/scratch/acceptance-out-008/A-018-merge-recovery.md`.
