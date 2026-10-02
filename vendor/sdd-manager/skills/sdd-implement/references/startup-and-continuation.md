# Startup and continuation

## Push before task work

Use the current **sdd-orient** handoff to establish the eligible Git worktree, current branch, HEAD, governing instructions, and pending-change ownership. Resolve the established remote destination from repository policy and branch configuration. This prerequisite inspection enables the first execution action: push outstanding commits before any task selection, check execution, or edit.

Check the current branch against the established remote branch and push all unpushed commits, independently of worktree cleanliness. Verify that the remote contains those commits; when no new remote changes occurred, its branch tip should match local HEAD. If no commits are outstanding, continue without creating a push solely for ceremony. Do not force-push, guess a destination, initialize Git, or reset pending work. Report missing destination, access failure, detached or unusable branch state, or divergence that prevents the required push; stop further implementation until resolved.

Attempt the required push with existing shell authentication; do not discover/request tokens first. On a 403 or explicit credential failure, pass sanitized destination, transport, operation, and cause to **sdd-manage**'s **Hosting credentials** protocol for recovery and retry. Confirm remote containment before proceeding; unresolved access remains a push blocker.

## Interpret the startup task state

| Observed state | Action |
| --- | --- |
| Checked task or parent has a pending completion reassessment | After startup pushing, assess its current acceptance within the authorized range; correct unsupported status, preserve historical evidence, and retain the note until reassessment is resolved. Report out-of-range work as a scope conflict. |
| Last checked task is ahead of the last completed task commit | Confirm task ownership and existing completion evidence, finish its commit and push, and coordinate its issue closure. Do not reimplement completed work. |
| Current task is unchecked with task-owned pending changes | Inspect existing work and resume the remaining implementation and verification. |
| Clean tree and checklist agrees with committed task boundary | Select eligible work within the requested range; do not treat cleanliness as proof that required issue closure has occurred. |
| Missing or contradictory completion evidence | Obtain the missing checks or repair incomplete work within scope before treating the task as complete. |
| Ambiguous task identity, ownership, or conflicting changes | Preserve changes and report the ambiguity before mutating the affected work. |

Use the last task commit as the historical completed boundary; later maintenance, reconciliation, or steering-amendment commits do not establish another completed task. A pending reassessment disputes current acceptance without erasing that history. Preserve stable IDs in the owning TASKS or FEATURE-TASKS. If no task has been committed, use the established preimplementation baseline.

Continuation finishes the interrupted task before new task selection. If it falls outside the newly requested range or the user directs a conflicting action, report the scope conflict rather than silently expanding or discarding work. When hosted tracking is active, check pending references and closures for verified completed tasks within the established maintained tracking scope through **sdd-forge** as part of normal completion processing, including older tasks completed while hosting was unavailable. Do not limit reconciliation to the resumed or latest task, infer completion from hosted state, or block independent local work solely because hosting remains unavailable.

## Select the authorized range

Use [range selection](range-selection.md) to resolve task, next-N-task, milestone, or phase requests into precise IDs, prerequisite evidence, and exit conditions. For feature work, select from the active FEATURE-TASKS and inspect relevant TASKS prerequisites; for main work, use TASKS. Report ambiguous active scope and unmet out-of-range prerequisites rather than selecting silently.

Keep the selected range and checkpoint visible throughout execution. A user may change the range or pause work; preserve completed commits and current pending work, report the new boundary, and follow the latest instruction. A separate steering request does not authorize automatic continuation afterward.

## Working branch and integration continuation

After startup pushing, establish or reuse the selected range's working branch and target under **sdd-manage**'s **Branch management** reference. Record its starting checkpoint in existing task/change evidence. Preserve unfinished task ownership before branch setup; do not create a new branch to evade pending work or push blockers. On continuation, distinguish unfinished tasks, completed tasks awaiting commit/push, an uncommitted merge awaiting conflict repair or verification, and a verified merge awaiting target publication. Finish the authorized state rather than repeating tasks or merging again. Ambiguous branch/target identities or out-of-range work block the affected continuation.
