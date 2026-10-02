---
name: sdd-manage
description: Coordinate SDD workflows for initial development, feature preparation, bounded or resumed task implementation, human-directed checkpoint amendments, accepted feature integration, focused review or maintenance, and hosted task synchronization. Use for multi-stage project requests, shared prerequisites, branch management and phase transitions, workflow transitions, stopping boundaries, recovering shell authentication, or supplying hosting credentials to sdd-forge.
---

# Coordinate specification-driven development

Translate the user's objective into a scoped workflow and coordinate the responsible skills. Use the request and established session decisions as authorization; continue routine steps within that scope without repeated confirmation. Discussion, assessment, or review alone does not authorize edits. Start at the requested stage when its inputs are established, and stop at the requested boundary.

| Coordination concern | Load |
| --- | --- |
| Select a practical workflow and its entry, outputs, and stopping point | [available workflows](references/workflows.md) |
| Establish prerequisites, pass scope, resolve blockers, and persist results | [coordination protocol](references/coordination.md) |
| Resolve identities, create/reuse workflow branches, or manage phase transitions | [branch management](references/branch-management.md) |
| Integrate verified boundaries or continue a blocked merge | [Git workflows](references/git-workflows.md) |
| Discover, save, or supply a repository token; recover shell/API authentication | [hosting credentials](references/credentials.md) |
| Plan or coordinate focused/systematic review and accepted revisions | [review and revision](references/review-and-revision.md) |
| Check representative requests and expected boundaries | [workflow examples](references/examples.md) |

1. **Establish the request.** Identify the project, objective, requested operation, authoritative inputs, and stopping boundary. Distinguish initial preparation, feature deltas, task-list implementation, checkpoint steering, integration, and focused review. Ask only for missing decisions that materially prevent the requested work.
2. **Orient at startup.** Invoke **sdd-orient** for a current scoped handoff: project and Git roots, governing instructions, documents, environment, branch and HEAD, dirty-path ownership, and interrupted task state. Read-only discussion can proceed outside Git; repository mutations require an eligible worktree. Re-orient when material state or scope changes.
3. **Coordinate the responsible skills.** Follow the selected workflow. Supply the objective, allowed paths and effects, authoritative decisions, task IDs where applicable, Git baseline, pending-change ownership, and exit conditions. Load their instructions rather than reproducing their procedures. Preserve valid existing work; dirty state alone does not justify reset.
4. **Respect ownership and decisions.** Leave executable range selection, main execution, completion, commits, and pushes to **sdd-implement**, and checkpoint amendments to **sdd-steer**. Leave accepted feature reconciliation to **sdd-integrate-feature**. Return governing-document amendments identified by **sdd-docs** to the user; do not automatically route them into authoring. Coordinate hosting only when requested or already active for the selected work.
5. **Finish and stop.** Coordinate explicit integration/publication only when the workflow's integration gate is met: main development requires full phase completion; a partial task/milestone range pushes and pauses on its phase branch. Collect evidence and unresolved differences. For authorized repository changes outside implementation or steering, coordinate scoped verification, commit composition through **sdd-report**, commit, and push as specified by the request and project policy. Report blockers accurately. Never resume implementation after steering without a separate human instruction.

Use **sdd-report** for presentation, keeping planned, implemented, verified, committed, pushed, and hosted states distinct. Return the accomplished objective, affected artifacts or task IDs, evidence and limitations, commit/push and hosting outcomes when applicable, remaining decisions, and the exact stopping point. Do not require a transaction journal, recovery directory, extra issue map, or a new skill for interruption recovery. This coordinator requires the focused skills selected by the workflow; if one is unavailable, report the blocked capability rather than claiming it ran.
