# Coordination protocol

## Establish scope and prerequisites

- **Request:** Capture the objective, inspection or mutation mode, target paths or documents, owning task list, selected boundary, and allowed external effects. Reuse session authorization and decisions.
- **Orientation:** Start with **sdd-orient**. Use its observed repository, applicable instructions, baseline, pending changes, tooling, and task evidence. Do not mistake an unchecked task or latest maintenance commit for a proven execution boundary.
- **Git:** Require an eligible worktree for repository mutations. Outside Git, continue discussion or inspection and report the mutation blocker; do not initialize a repository implicitly.
- **Pending work:** Establish ownership of dirty paths. Preserve unrelated staged and unstaged changes. Do not reset because the tree is dirty. Pass interrupted task implementation to **sdd-implement**, document incorporation to **sdd-integrate-feature**, and commanded amendment continuation to **sdd-steer**; if it lies outside the requested new scope, resolve that conflict before overlapping mutations.
- **Inputs:** Confirm the authoritative requirements, design, strategy, and layout needed by the selected stage. File presence alone does not establish acceptance or consistency.
- **Facilities:** Check availability of the selected skills and necessary tools. Report concrete missing capabilities. Use ordinary filesystem, Git, and available provider tools; require no particular client, hidden hooks, or implicit installation mechanism.

For branch workflows, use [branch management](branch-management.md) for setup and [Git workflows](git-workflows.md) for final integration. Preserve implementation's push-first prerequisite; a direct focused invocation uses the same protocol.

## Coordinate execution

1. Give each responsible skill the objective, scope, authoritative inputs, decisions, relevant task IDs, branch/HEAD, dirty-path ownership, permitted effects, required evidence, and stopping point. Keep credentials out of ordinary handoff text.
2. Let the skill perform its owned procedure. Collect its changed paths, observed evidence, findings, and remaining differences before the next dependent stage.
3. Refresh the material baseline when HEAD, instructions, project, target scope, or relevant pending changes change. Do not repeatedly run orientation or checks when the current evidence remains applicable.
4. Resolve missing human decisions and out-of-scope requirements without guessing or silently expanding work. Continue independent authorized work where possible. State the blocked operation and decision needed.
5. For verification failures, return repairs to the active **sdd-implement** or **sdd-steer** workflow. A standalone verification request returns findings; it does not start implementation. Documentation findings requiring governing-document changes are returned to the user before any authoring is coordinated.
6. Stop at the requested boundary. A checkpoint is not permission to select another milestone, start steering, incorporate unselected feature documents, or create hosted objects. Complete explicit integration/publication when its workflow gate is met; incomplete main phases push and pause even when the requested task subset is complete. A human-commanded steering amendment always returns control without resuming implementation.

## Persist repository changes

Use this procedure for document preparation, accepted integration, and standalone maintenance. Do not duplicate the commit workflows owned by **sdd-implement** or **sdd-steer**.

- **Policy:** Honor the user's commit and push instructions and repository policy, including standing session instructions. When no persistence policy is established, commit and push authorized finished changes to an established destination. Do not invent a remote branch or force-push.
- **Verification:** Inspect the actual diff and run checks appropriate to its effects: document consistency and links for authoring, relevant tests for test changes, or **sdd-verify** for acceptance campaigns. Verify heading spacing and project conventions. Do not manufacture task completion for document-only work.
- **Staging:** Stage only owned changes; inspect the staged diff and exclude unrelated pre-existing staged paths from the commit. Preserve their index state. A normal commit includes all staged content; use a path-scoped commit only for wholly owned file contents, or isolate selected changes in a temporary index. Stop if ownership cannot be separated safely. Avoid broad staging or destructive cleanup.
- **Commit:** Use **sdd-report** to compose an evidence-backed message. Include stable task IDs and verified issue references when the change belongs to those tasks; preparation without assigned tasks does not invent IDs. Inspect commit contents and remaining staged and unstaged diffs; after a temporary-index commit, reconcile stale committed owned index entries while preserving unrelated staged content.
- **Push:** Assume existing shell authentication is usable; push the finished commits to the established destination and check that the remote contains them. For an access 403 or explicit credential failure, coordinate [shell recovery](credentials.md) and retry the affected push before reporting it as unresolved. Report a committed-but-unpushed result if access, destination, or divergence blocks persistence; retain local work. Resolve divergence without discarding changes or force-pushing.
- **State:** Distinguish committed, pushed, and hosted status. A successful local commit does not establish remote persistence or issue closure.

## Return results

Use **sdd-report** for the result format. Include the fulfilled objective and affected artifacts or task IDs, observed verification and gaps, commits and push status when applicable, hosted changes or pending reconciliation, unresolved decisions, and the boundary reached. Keep planned work distinct from implemented functionality. No extra workflow-state artifact is required: current documents, task evidence, Git, and applicable session decisions supply continuation context.
