# Available workflows

Select by the user's objective, not by which documents happen to be missing. A scoped request may enter any stage whose required inputs are established. A combined request may authorize preparation and implementation together; retain its explicit implementation boundary. Do not require fresh approval for a transition already covered by that request.

## Core development workflows

Choose among three core workflows by the intended change. They describe purpose and overall path; focused skills and the operation catalog below supply reusable stages. A workflow name grants no authorization or branch destination. Apply **sdd-conventions**' **Workflow identity** and [branch management](branch-management.md) for actual names and target context.

| Workflow | Purpose | Typical path |
| --- | --- | --- |
| Main / greenfield | Build the complete intended system from its initial definition. | Exploration → architecture/decomposition → SPEC → PLAN/layout → TASKS → bounded implementation and verification. |
| Revision | Correct, simplify, or improve previously defined or implemented work. | Review plan when needed → review → review report → revision plan → revision → revision report. |
| Feature | Add a scoped capability to an existing system. | Necessary feature design/specification/plan documents → FEATURE-TASKS → implementation → accepted document incorporation and verification. |

- **Entry:** Greenfield follows the main path from exploration; an existing project may enter at an established stage. Main names the development purpose, not Git's main or default branch. Reuse accepted inputs rather than replaying stages.
- **Revision scope:** Use [review and revision](review-and-revision.md) for formal campaigns. A focused prompt may define review scope or an accepted revision directly; do not invent a preceding review or mandatory artifact stage when it adds no needed evidence.
- **Feature preparation:** Define the scoped feature package before dependent implementation, using only the design, specification, and planning deltas it needs. FEATURE-TASKS governs active task-list feature work. Reuse sufficient existing design/layout; not every correction needs a feature package.
- **Shared execution:** Implement only the authorized bounded scope. Apply relevant verification and commit/push checkpoints under [Git workflows](git-workflows.md). Main development uses phase branches: partial ranges pause after pushes, complete phases explicitly integrate, and an authorized next phase starts from updated main. Revision/feature and steering use their applicable integration gates. Preparation, assessment, and review stop before implementation unless it is authorized. A narrow task request does not authorize unrelated incorporation or a whole-project campaign.

### Steering as lightweight revision

**sdd-steer** is the focused human-directed revision path at a paused task-list checkpoint, especially for reducing implemented functionality. The human supplies the amendment objective and commands execution. Steering directly updates affected existing documents, code, tests, and documentation; it creates no feature-document layer and requires no feature-document integration step or obligatory formal review/revision campaign.

Steering still verifies, commits/pushes, explicitly integrates into the paused implementation branch, verifies/publishes that target, and reports. It returns control without handing off to or resuming sdd-implement; the human separately resumes the task list. A broader revision may use the formal campaign instead. Steering is a revision variant, not a fourth core workflow.

## Operation catalog

These entries select stages or supporting operations within a core workflow; they can also be requested independently within their stated boundaries.

| Operation | Entry and coordination | Outputs and stop |
| --- | --- | --- |
| Prepare initial development | Use **sdd-design** for the brief, architecture, and decomposition; **sdd-specify** for behavior and acceptance; **sdd-plan** for delivery strategy and layout; **sdd-tasks** for TASKS. Resolve consequential decisions as they arise. | Selected preparation artifacts and open decisions. A preparation-only request stops before implementation. |
| Prepare a feature | Inspect existing contracts and implementation. Use design deltas where needed, then **sdd-specify**, **sdd-plan**, and **sdd-tasks** for the necessary FEATURE-SPEC, FEATURE-PLAN, and FEATURE-TASKS. Reuse established design and layout where sufficient. | Bounded feature requirements, delivery strategy, and executable tasks. Stop at preparation unless implementation is included in the request. |
| Implement a bounded range | Pass the owning TASKS or FEATURE-TASKS, requested IDs/count/milestone/phase, dependencies, and boundary to **sdd-implement**. It resolves the executable range and coordinates **sdd-tdd**, **sdd-docs**, **sdd-verify**, **sdd-report**, and active **sdd-forge** tracking. | Evidence-backed completed tasks, commits, pushes, and applicable issue closure. For main development, pause on an incomplete phase branch or explicitly integrate the verified full phase. For other workflows, integrate only the coherent authorized boundary. Verify/push applicable targets, then stop; retain branch state on a blocker. |
| Resume interrupted implementation | Pass orientation's identified pending task and evidence to **sdd-implement**. It pushes outstanding commits before task selection, tests, or edits, even on a clean tree; it finishes pending work before advancing. Use the established boundary; clarify it if unavailable. | Continuation of the bounded implementation workflow. No separate recovery protocol or automatic reset. |
| Steer at a checkpoint | Use **sdd-steer** for the human-defined focused amendment during partial implementation. An assessment request returns impact only; a command to implement authorizes direct changes to affected existing development documents, code, tests, and documentation. | Assessment, or a verified amendment branch explicitly merged into the paused implementation branch, merged-state verified and target pushed. Create no feature overlay and invoke no feature-document integration step. Stop; the human separately resumes implementation. |
| Integrate accepted feature documents | Pass the accepted sources and explicit target set to **sdd-integrate-feature**. TASKS and FEATURE-TASKS are independently selectable; transferring task ownership requires both lists in scope. Document-only integration does not imply task reconciliation. | Selected main documents incorporated, task relationships reconciled only within scope, source disposition, and external impacts. Stop without executing tasks. |
| Run a review/revision campaign | Use [review and revision](review-and-revision.md) for planned systematic review or prompt-driven focused review, stable findings, accepted revision planning, and authorized execution. Route concerns to focused owners. | Retained campaign plans/reports. Review stops before source changes unless revisions are authorized; implemented revisions finish with verified explicit merge/publication. |
| Review or maintain a selected scope | Route design review to **sdd-design**, behavior review to **sdd-specify**, strategy/layout review to **sdd-plan**, task-list review to **sdd-tasks**, selection-only requests to **sdd-implement**, test strategy or test maintenance to **sdd-tdd**, documentation to **sdd-docs**, and acceptance checks to **sdd-verify**. Use **sdd-conventions** for relevant criteria. | Findings, evidence, or explicitly requested maintenance. Review and verification do not authorize repairs or completion updates. Stop at the selected scope. |
| Synchronize hosted tracking | Use **sdd-forge** for the requested projection, association lookup, or issue reconciliation. Use available client authentication first and coordinate credential recovery through the credential protocol when needed; leave provider access checks and object mapping to its backend. | Repository and task-to-issue associations, changed hosted objects, differences, and access blockers. Stop after the hosted operation. |

## Delivery strategy handoff

Preparation carries the accepted design/contracts into an early meaningful end-to-end MVP and small testable capability increments through **sdd-plan**, then derives their bounded executable work through **sdd-tasks**. Retain complete intended design and SPEC, justified prerequisite exceptions, preserved useful behavior, and relevant exit evidence. A scoped feature uses the earliest meaningful changed path rather than rebuilding the whole project.

Pass the selected range, owning capability/milestone outcomes, dependencies, verification obligations, and applicable human decision gates into implementation. At consequential checkpoints, return the demonstrated functionality and relevant usability/risk evidence for the human's continue/amend/simplify/stop decision. This does not authorize automatic steering, broaden the selected range, or require approval for routine work already authorized.

## Feature sequencing

- **Preparation:** Establish or reuse the convention's feature branch/package identity under [branch management](branch-management.md). Create its features-directory README linking the active root FEATURE sources; preserve another active package in the same worktree. Keep feature deltas distinguishable from the complete main documents. Creating a feature task list does not require immediate incorporation into TASKS.
- **Implementation:** An accepted FEATURE-TASKS can drive implementation while its authoritative feature documents remain active. Identify those sources explicitly in the handoff.
- **Document integration:** Incorporate accepted targets included in the request on the feature branch before final verification and Git merge. A complete feature implementation includes incorporation needed for a coherent final project; a preparation-only or narrow task request does not authorize unrelated incorporation. Do not infer acceptance from passing tests.
- **Archive:** After accepted final incorporation and task/evidence disposition, **sdd-integrate-feature** retains eligible sources under the package directory, repairs selected links, and marks historical snapshots. Partial/narrow integration retains needed active documents; verify archive ownership before final merge.
- **Git integration:** Merge the verified completed boundary into its established target by default with an explicit merge commit, verify the merged state, and publish the target. Preparation-only persists its documents on the feature branch and stops before implementation or full-feature merge.
- **Consistency:** If the selected work requires an unresolved contract or dependency decision, report it before the dependent mutation. Continue independent authorized work when sound.

## Cross-cutting operations

- **Reporting:** Use **sdd-report** throughout, or independently for an issue, commit message, PR description, or progress report. Drafting PR text does not create or merge a PR.
- **Hosted tracking:** Local workflows remain usable without hosting. When tracking is active, coordinate task associations before commit composition and verified closure through **sdd-forge**; issue state never supplies completion evidence.
- **Authentication:** Attempt authorized pushes using existing shell authentication. Route access/credential failures to the coordinator's repository-token recovery protocol; preserve distinct Git and API access and the active backend's permission profile.
- **Persistence:** Implementation and steering own their commits and pushes. Coordinate persistence of other authorized repository edits through the shared protocol; hosted-only changes have no local commit by implication.
