# Feature incorporation

Treat each accepted feature document as a scoped delta and each main document as the complete intended description of its own concern. Identify which main nodes the selected delta changes and which unchanged nodes it references. Project instructions and accepted decisions govern; observed code or an unchecked task does not settle a design or behavioral conflict.

## Select and incorporate

1. Confirm the selected main target or targets and the corresponding accepted feature source. A feature may have no overlay for some levels. Permit a single document, such as SPEC alone, when its change can be expressed coherently there. Record affected but unselected dependents; do not expand the edit scope silently.
2. For PROJECT, integrate changes to purpose, users, scope, outcomes, or constraints into the brief. For ARCHITECTURE and DECOMPOSITION, integrate accepted block and component boundaries, dependencies, interfaces, and relevant rationale into the owning root and focused children. Preserve the difference between architectural structure and final behavioral contracts.
3. For SPEC, integrate final supported and unsupported behavior, errors, invariants, and objective acceptance into the owning root and children. For PLAN, integrate delivery strategy, phase and milestone definitions, dependencies, and exit checks. For layout, integrate changed physical ownership only where the accepted change requires it. Keep each concern in its main owner rather than copying it across documents.
4. When transferring tasks from FEATURE-TASKS into TASKS, require both lists in the selected edit scope. Move each owning entry into the complete hierarchy once, retiring its independently checked source entry in the same change while preserving project-wide IDs, dependencies, verified status, and durable evidence. If FEATURE-TASKS is outside scope, defer the transfer and report the required scope extension; TASKS-only reconciliation of existing main entries may still proceed. Reconcile parent placement and exit conditions against the accepted PLAN. A feature parent checkbox does not establish completion of its whole-project parent. Task-list creation and review belong to **sdd-tasks**; executable range selection, implementation, and completion updates belong to **sdd-implement**.
5. Read every changed main root and child as a coherent description of the intended end state. Remove superseded claims and editing-history language. Keep genuine backward compatibility or transition requirements as present obligations. Check parent-child links, affected cross-document contracts, and task references within the selected scope.

When a selected target depends on a still-unaccepted decision in another concern, stop that target and report the specific decision and owner. Continue independent selected targets only where their meaning remains sound. In particular, do not incorporate a task list against an unreconciled conflicting PLAN or SPEC.

## Task-list reconciliation

When TASKS or FEATURE-TASKS is selected, reconcile the accepted changes in its owning list; this need not incorporate the feature list into TASKS.

For an accepted feature delta, compare the intended final SPEC, design, PLAN, and layout with existing work, TASKS, and any active feature documents and FEATURE-TASKS. Revise affected tasks and dependency edges, remove obsolete uncompleted work, add necessary corrective work, and identify previously checked items whose acceptance has changed. Keep unaffected completed work and stable IDs. Revise an active feature list within its scope; revise main TASKS when the accepted end state changes its complete hierarchy. Do not leave a chronological amendment section or a list of discarded approaches in the main TASKS; Git retains that history. Preserve evidence for an implemented capability that was later removed in Git, while the current checklist describes only work required for the accepted end state.

When changed acceptance makes a checked task or parent claim stale:

- Record **Completion reassessment pending** beneath the affected owning entry, or in its existing linked evidence location, only when that location is in the edit scope. Identify the stable task or parent ID, changed acceptance and authoritative source, prior evidence whose scope no longer suffices, and required reassessment.
- Preserve the checkbox and previous evidence. The pending note makes the checked claim disputed; it is not current completion evidence. **sdd-implement** owns acceptance reassessment and checkbox correction. Direct checkpoint amendments retain **sdd-steer** ownership.
- Keep the note with the owning entry during task transfer. Preserve prior evidence as historical, and flag affected checked parent claims without inferring whole-project completion from feature results.
- If the owning list or evidence location is outside scope, report the deferred reassessment and needed edit scope without adding a note there or changing its status. Do not invoke implementation or change hosted state from the finding.

If the feature is withdrawn, preserve Git history and resolve the disposition of completed work before removing its task list. Task execution and completion verification belong to **sdd-implement**; reconciliation preserves evidence and the durable pending-reassessment notes for its review.

## Scope and cleanup

Feature source documents remain active while other levels are integrated or work still depends on them. A selected SPEC-only incorporation does not archive the whole package, remove FEATURE-TASKS, or transfer unselected tasks. Preserve active sources and report deferred link/owner changes outside scope.

For a completed accepted feature, apply **sdd-conventions**' **Workflow identity** archive location. After selected final incorporation and task/evidence disposition, retain eligible sources in `docs/dev/features/<campaign>/` with their basenames rather than deleting them. Archive on the feature branch before final verification and Git integration; this skill owns document disposition, while sdd-manage owns the Git merge.

### Archive eligibility and procedure

1. Recover the package identity/full baseline and actual active sources from its navigation record and Git. Confirm completion and accepted incorporation scope; if completion verification or a necessary owner is unresolved, retain the active source and report the blocker.
2. Ensure accepted content is represented in the main owners, transferred tasks have one executable owner in TASKS, remaining work has a current authorized owner, and historical evidence remains findable. No active work may rely on a moved file as its sole authoritative source. FEATURE-TASKS remains active until its work/evidence disposition permits archival; document-only integration does not change it by implication.
3. Move only eligible selected sources, preserving basenames and any substantial child documents. Inspect for archive collisions rather than overwrite another record. Update in-scope links and evidence references; retain a source still required by unselected active links until those edits are authorized.
4. Update the package README with historical/archive status, source dispositions, current main owners/task references, and incorporation evidence. Mark archived task lists as historical snapshots, not executable owners. Archived checkboxes do not supply current task selection or completion; main owning entries preserve stable IDs and verified/historical evidence.
5. Recheck moved paths, relative links, cross-document consistency, unique task ownership, remaining active sources, and completion/publication reporting. Commit/push the coherent document checkpoint on the feature branch; coordinate final Git integration only when the authorized feature boundary is ready.

For a withdrawn feature, preserve historical evidence and resolve completed/remaining work disposition explicitly before archive/removal; withdrawal is not completed implementation. Report hosted identity/parentage impacts to sdd-forge when tracking is active, without mutating hosted objects here.

## Continue interrupted incorporation

- **Context:** Recover the selected target set, accepted feature sources, working/target branches, and starting checkpoint from the request, Git, and existing change evidence. An active feature campaign retains its working branch; a standalone integration uses a scoped branch under **sdd-manage**'s Git protocol. Ambiguous scope or dirty-path ownership blocks overlapping changes.
- **Partial state:** Compare actual selected roots, children, task lists, and links with the checkpoint and accepted delta. Identify completed amendments, unfinished reconciliation, partially moved archive paths, duplicate task IDs, conflicting executable owners, and stale acceptance. A changed SPEC or clean worktree is not proof that incorporation finished.
- **Resume:** Preserve valid incorporated content and historical evidence. Finish only selected owners, applying the ordinary unique-ownership, source-retention, and pending-reassessment rules. If task transfer is partially applied, inspect both entries and Git evidence before reconciling; require both lists in scope. Stop on unresolved identity or contract conflicts instead of creating a second executable task or deleting a guessed source entry.
- **Unselected owners:** A SPEC-only request leaves TASKS and FEATURE-TASKS untouched and reports their deferred consequences. Do not expand the request to repair all documents merely because the previous operation was interrupted.
- **Finish:** Check selected document consistency, links, task identity/ownership, and retained sources. Report coherent changes and unresolved dependencies to **sdd-manage** for commit/push and default explicit Git integration of the authorized boundary. Within a larger feature campaign, persist this document checkpoint on its branch and leave final merge to that campaign's boundary. Partial or conflicting incorporation is not a successful merge prerequisite.

Branch isolation protects the target from unpublished partial edits; it does not make individual working-branch edits transactional. No automatic rollback, reset, separate journal, or implementation invocation is required.
