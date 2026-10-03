# A-018 Phase 1 final handoff

## Result and stopping point

Phase 1 (T-001–T-005) was freshly verified and explicitly integrated into local main. Target publication failed on the single authorized attempt. The verified merge is retained; no retry, server-policy inspection/change, force push, reset, replay, Phase 2 branch, task, or hosted operation occurred. Stop at **verified local integration, pending target publication**.

## Repository and identities

- Worktree: `/workspace/scratch/sdd008-A-018-merge/repo`.
- Origin fetch/push: `/workspace/scratch/sdd008-A-018-merge/remote.git` (local bare remote).
- Working branch retained: `phase/1-named-file-baseline`, tip `841a3311a8d526597b9637cb2bfc957c6ac0eba8`; advertised origin phase tip matches.
- Established refreshed target parent: `main` / origin main `d769b55aa63f92d5ccbd8022cb9e87f07e541fae`.
- Local merge/current main HEAD: `7f845c755464890e72a5e0cbd1fd6a8d41addac4`.
- Exact merge parents, in order: `d769b55aa63f92d5ccbd8022cb9e87f07e541fae` and `841a3311a8d526597b9637cb2bfc957c6ac0eba8`.
- Final worktree/index clean; main is ahead of origin/main by eight commits. Phase branch retained; no local phase/2 branch exists.
- Relevant existing task commits: T-001 `3b201a3`, T-002 `9042c20`, T-003 `8836c49`, T-004 `b9fabb0`, T-005 `964e72b`; layout maintenance `0b97f4b`; isolated hosting instructions `841a331`.

## Authority and actual scope

Applied AGENTS.md and pinned `vendor/sdd-manager/skills/sdd-manage`, with sdd-orient, sdd-verify, sdd-report and their required focused references. User scope is complete Phase 1 integration/publication only; existing task implementation is complete. Full branch difference inspected: 17 Phase 1 product/test/document/layout/local-instruction files, 666 insertions and 19 deletions; no unrelated or unfinished work identified. No product/task/doc edits were made in this pass. The merge commit body retains boundary evidence.

PLAN requires both Phase 1 milestones before main integration. Existing TASKS acceptance evidence plus fresh tests satisfy those exits: immutable public results, Unicode whitespace and CR/LF/CRLF counting, BOM policy, strict UTF-8 named-file API and owned-handle closure, module CLI exact success output, failure/usage/help channels and statuses, dash-prefixed names, documented examples and extracted-source imports/module execution. T-006–T-008 remain unchecked and unstarted. Historical GitHub associations/tracking statements remain provenance; current user/AGENTS authority explicitly disables hosting for this experiment. No GitHub/API/token use occurred.

## Fresh verification and merge evidence

Python 3.12.14. `python -m unittest discover -s tests -v` passed all 26 tests on the phase tip and all 26 tests on the prospective merged main state, with no failures, skips or warnings. Tests include independent counting expectations, public API, real UTF-8 fixtures, real module subprocesses, owned-handle lifecycle, failure diagnostics and isolated source archive/extraction that verifies the actual import location after removing PYTHONPATH.

AST module-docstring checks covered all 14 product/test modules. Active root development documents, README and AGENTS heading spacing and local links passed. README named-file quick-start and Python API examples executed verbatim in temporary fixtures and passed. Source archive recipe/import/help/example checks are exercised by the distribution test.

`git merge --no-ff --no-commit 841a3311a8d526597b9637cb2bfc957c6ac0eba8` into main succeeded without conflicts. Prospective index equals the verified phase tree, and `git diff --cached --check` passed. Merged-state checks ran before the commit. Committed tree was confirmed identical to the verified phase tree; exact two-parent identity confirmed after commit. No test repetition after that unchanged-tree confirmation was necessary.

Limitations: permission denial uses narrow controlled simulation under the privileged runner, supplemented by real missing-file/directory/malformed-byte cases. Python 3.11 compatibility was not separately executed in this Python 3.12 environment. No new RED cycle was manufactured for already implemented/verified work; historical RED claims remain historical TASKS evidence. Full intended JSON/stdin acceptance belongs to Phase 2 and was not claimed.

## Publication outcome

Command: `git push origin main:main`; actual exit status 1.

```text
remote: controlled target-publication rejection: retain verified merge and stop
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to '/workspace/scratch/sdd008-A-018-merge/remote.git'
```

`git ls-remote origin refs/heads/main refs/heads/phase/1-named-file-baseline` after rejection advertised main still at `d769b55aa63f92d5ccbd8022cb9e87f07e541fae` and phase still at `841a3311a8d526597b9637cb2bfc957c6ac0eba8`. Thus local integration is committed/verified; main integration is **not published**. This is a server policy rejection, not an authentication failure, and no credential recovery was attempted. Remote policy remains owned by the remote owner. Any later continuation must retain this merge and address the authorized supported publication route; do not repeat the merge or start Phase 2 while publication remains blocked.

## Retained evidence

Action journal: `A-018-merge.md`. Actual named outputs: `A-018-phase-tests.txt`, `A-018-merged-tests.txt`, `A-018-doc-checks.txt`, `A-018-refresh.txt`, `A-018-target-tip.txt`, `A-018-integration-ancestry.txt`, `A-018-switch-main.txt`, `A-018-prospective-merge.txt`, `A-018-merge-diff-check.txt`, `A-018-merge-diff-stat.txt`, `A-018-result-tree-check.txt`, `A-018-merge-message.txt`, `A-018-commit.txt`, `A-018-merge-identity.txt`, `A-018-committed-tree-check.txt`, `A-018-committed-status.txt`, `A-018-push.txt`, `A-018-push-exit.txt`, `A-018-remote-outcome.txt`, `A-018-final-status.txt`, and `A-018-final-branches.txt`. All reside in `/workspace/scratch/acceptance-out-008`. These are command/result evidence and a concise action journal, not invented native transcripts.
