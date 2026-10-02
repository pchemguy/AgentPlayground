# Git branch management

Use this coordinator procedure for mutating branch setup, reuse, continuation, and authorized phase transitions. Apply **sdd-conventions**' **Workflow identity** rules; use [Git workflows](git-workflows.md) for explicit integration/publication. Local Git operations require no hosting backend. Execution/steering owners retain their commits and pushes; sdd-orient observes state without branch mutations.

## Establish context and identity

1. Use current orientation to identify eligible worktree, actual branch/HEAD, applicable instructions, pending-change ownership, authorized workflow/range, and accepted sources. Read-only review or selection creates no branch. Implementation pushes outstanding commits on the current established branch before task work or new branch setup; never create a branch to evade a push blocker.
2. Establish working branch, target, starting checkpoint, relevant HEADs and remote destinations. Main development identifies its actual main integration branch explicitly; revision/feature targets may be that branch or the active phase. Steering targets the paused implementation branch. A prefix or default-branch name proves neither target nor ownership.
3. Allocate or recover the convention's campaign identity for revision/steering/feature, or the owning PLAN/TASKS phase number for main implementation. Inspect both campaign collections and relevant remote state for allocation/collisions. Record the full baseline, actual working/target identities, scope, and active source links in the existing campaign/task/change record before dependent work. Preparation-only can reserve identity without authorizing implementation.
4. For revision/steering, ensure the review directory/record matches the branch identity; a steering report can begin with objective/context and gain verification results later. For feature preparation, reserve its features directory with a concise README identifying full baseline, branch/target, scope, and active sources. Main documents remain in docs/dev. Do not fabricate optional review stages or a second registry.

## Create or reuse

- Reuse only when context, history, target and pending work fit the same scope. Preserve suitable legacy/in-flight names or explicit project/user overrides and their recorded association; no automatic migration.
- For new work, choose the workflow convention's branch name and validate it with `git check-ref-format --branch`. Inspect local/remote name collisions and worktree occupancy. An unrelated occupied name needs a distinct slug suffix without changing campaign identity; remote uncertainty is not proof the name is free.
- Create from the established target checkpoint before scoped edits. Use a separate worktree where unrelated dirty work or target availability requires it; preserve original staging/work and never implicitly stash/reset/clean. Do not check out one branch in two worktrees.
- An unborn/detached/conflicted state, missing usable checkpoint/target/remote, unresolved ownership or inability to establish identity blocks setup. Report the concrete decision/facility rather than guessing a different destination.
- Publish branch checkpoints through the active owner's ordinary Git push and verify remote containment; do not create the same remote ref through a duplicate API operation. This manager needs no sdd-forge branch capability or PR workflow.

## Main phase lifecycle

Select main-project work on the owning `phase/<number>-<slug>` branch. A bounded task or milestone request within an incomplete phase ends with verified commits/pushes and a paused phase branch, not a merge into main. Record completed range, remaining phase work, applicable evidence and current target context.

When all phase work and exit evidence are complete, use the Git protocol for one explicit merge into the established main integration branch, verify the merged state, publish, and confirm containment. A checkbox or completed subset is insufficient. Failed exits or publication retain branch/merge state; do not create the next phase.

Only when the request authorizes further work, create the next phase branch from the updated verified/published main checkpoint and re-establish its scope. Split an authorized cross-phase range into sequential phase segments; each phase must meet its exit before the next branch starts. Do not execute extra tasks or perform an unrequested continuation to fill a phase. An explicit instruction to integrate a partial phase is a recorded override with its scope/evidence consequences, not the default.

Feature/revision integration into a phase updates that phase's accepted inputs and evidence; it does not complete the phase. Steering returns control after its amendment merge. Standalone revision/feature boundaries retain their own accepted scope and integration gates.

## Continuation

Recover identities and actual file paths from retained records and Git; names alone do not prove state. Distinguish incomplete phase work, pending archive/reconciliation, uncommitted merge, completed merge awaiting push, and an already integrated campaign. Resume the same authorized operation rather than allocate another identity or repeat an existing merge. Report ambiguous ownership/target and preserve valid work. Retain branches unless deletion is explicitly requested or covered by project policy.
