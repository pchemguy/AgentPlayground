# GitHub TASKS projection

For the requested TASKS or active FEATURE-TASKS projection, create one GitHub issue per task, one GitHub milestone per SDD milestone, and one phase label per SDD phase. Assign each task issue its parent milestone and phase label when creating it. Do not duplicate an issue already projected from the other list. After a task is implemented, verified, committed, and reconciled in its owning task list, close its issue as completed under [issue lifecycle](github-issue-lifecycle.md).

Project the Phase → Milestone → Task hierarchy into one GitHub repository. Re-read TASKS, any active FEATURE-TASKS, and relevant PLAN or FEATURE-PLAN outcomes and exit conditions before writing. Take IDs and names from the task's owning list; use the applicable plan for supporting descriptions, not to rename hosted objects. For reused parents, ensure names match TASKS; stop for conflicting IDs, names, or parentage across the lists. Follow an established project naming convention only when it preserves unambiguous stable identity and the hierarchy.

| SDD item | GitHub object | Name or title | Brief description or body |
| --- | --- | --- | --- |
| Phase `2` — Archive streams | Label | `sdd-phase-2-Archive-streams` | Brief phase name and purpose. |
| Milestone `2.2` — ZIP support | GitHub milestone | `sdd-2.2-ZIP-support` | Milestone outcome and exit conditions. |
| Task `T-012` — Implement ZIP stream support | GitHub issue | `[T-012] Implement ZIP stream support` | Task brief and exact identity marker. |

Derive names from the owning task list using the hierarchy convention's normalization rule. Match managed objects by stable ID before reconciling a changed name; do not create a duplicate because a title changed. Give the phase label a brief description rather than copying the whole PLAN. The GitHub milestone reflects the milestone's outcome and exit condition; it is not a nested child of the phase. Assign each task issue the phase label and its GitHub milestone. Do not strip unrelated labels when reconciling.

When **sdd-report** is available, supply the exact task identity marker and request its issue draft (`title`, `body`) using the owning task list and applicable documents. Use its title and body format; verify that the title and marker identify the same task. When **sdd-report** is unavailable, compose a baseline draft with the `[<task-id>] <task title>` title and a body covering task outcome, reason or relevant context, expected scope, dependencies, acceptance and prescribed checks, and document links where present. Include code context, measurements, or task-kind instructions when the actual task calls for them; example prose from other projects is not a source of requirements. Do not fill absent facts with invented content. Separate each Markdown heading from adjacent content with a blank line, including in generated issue bodies; a heading at the start of a file or template needs no leading blank line. Include a clearly delimited identity marker, for example:

```markdown
## Task brief <!-- sdd-forge:task-id=T-012 -->

**Outcome:** ...
**Context:** ...
**Scope and dependencies:** ...
**Acceptance and verification:** ...
**Sources:** ...
<!-- /sdd-forge:task-id=T-012 -->
```

Use the exact ID for lookup. Before creation, search open and closed issues and exclude pull requests; validate any candidate's marker and title against the owning task list and the other active list for duplicate IDs. Reuse a unique match and report a conflict for multiple or contradictory matches. Create or reconcile the phase label and GitHub milestone, then the task issue with both associations. Apply the GitHub operational-failure protocol after failed or interrupted writes: re-read affected identities before retrying, preserve unknown outcomes, and create nothing when lookup is incomplete or ambiguous. Do not close or reopen an issue merely because a task list changed; use the issue lifecycle procedure.

Report created, matched, updated, and conflicted objects with IDs and URLs. Return the task-to-issue associations as the handoff; a separate checked-in mapping artifact is not required for this projection.
