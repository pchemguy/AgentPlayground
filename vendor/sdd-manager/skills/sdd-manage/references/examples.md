# Workflow examples

These examples illustrate routing and boundaries; repository instructions and the actual request determine the concrete work.

| Request and context | Coordinated result |
| --- | --- |
| “Prepare the project through TASKS.” An eligible Git worktree exists. | Orient; prepare the necessary design, SPEC, PLAN, layout, and tasks; check and persist the documents; stop before implementation. |
| “Review this SPEC.” The files are outside Git. | Perform read-only behavioral review and return findings. Do not initialize Git or rewrite files. |
| “Implement milestone 2.2.” TASKS contains its accepted requirements. | Orient; pass the boundary to **sdd-implement**; it pushes outstanding commits first, executes/persists tasks on the owning phase branch, and pauses if the phase remains incomplete. A fully verified phase explicitly merges and publishes before stopping. |
| “Resume milestone 2.2.” The last checked task is ahead of its last task commit. | Pass pending changes and evidence to **sdd-implement**. It verifies and commits the completed result without repeating implementation, then continues only within the selected boundary. |
| “Continue.” The tree is clean but task commits are unpushed. | Orient; **sdd-implement** pushes those commits before selecting tasks, testing, or editing. A push blocker prevents further implementation. |
| “Assess removing encrypted streams.” Implementation is paused at a checkpoint. | Route impact assessment to **sdd-steer**; return the proposed scope without mutation. |
| “Implement that removal.” The amendment objective is established. | **sdd-steer** amends existing documents, code, tests, and guides; verifies, commits, pushes, explicitly merges into the paused implementation branch, verifies/pushes the target, and reports. Create no feature documents and do not resume the main task list. |
| “Integrate FEATURE-SPEC into SPEC only.” FEATURE-TASKS is still active. | Incorporate accepted behavior into SPEC; retain sources still required by active work; leave the task lists unchanged and report affected links outside scope. |
| “Incorporate feature tasks into TASKS only.” FEATURE-TASKS owns their active entries. | Explain that ownership transfer requires both lists in scope; defer the transfer rather than duplicating IDs or editing an unselected source. Independent reconciliation of existing TASKS entries may proceed. |
| “Verify this phase.” Some required checks are blocked. | **sdd-verify** returns observed evidence and blocked acceptance conditions. Do not repair code, mark tasks complete, or close issues. |
| “Align README.” **sdd-docs** finds a conflict with SPEC. | Report the conflict and proposed governing-document amendment to the user; continue independent authorized README work. Do not invoke **sdd-specify** automatically. |
| “Create task issues on GitHub.” No suitable token is available. | Try the available authenticated API client for the requested scope. If credential recovery is needed, find a suitable ignored token or ensure `*.tkn` exclusion and request/save `gh.tkn` with the GitHub backend profile. Local work needs no token. |
| Resume active hosted tracking after an outage left several completed tasks open. | Reconcile verified completed tasks in the maintained tracking scope, including older pending issues; do not inspect only the latest task or add a recovery journal. |
| Active hosted tracking returns 403 during issue closure. | Receive sanitized operation context; check suitable ignored repository tokens and escalate when necessary; recheck access before retrying. Report pending hosted closure separately from verified local completion. |

## Branch and artifact examples

| Request/context | Result |
| --- | --- |
| Main phase 2 contains an accepted milestone request, but other phase work remains. | Use phase/2-<slug>, verify/commit/push selected work, and pause without main merge or phase 3 creation. |
| Phase 2 and all exits are complete; phase 3 execution is authorized. | Explicitly integrate/publish phase 2, then branch phase 3 from updated main; absent authorization, stop. |
| Commanded steering at paused phase 2. | Allocate matching review identity/revision branch, retain a minimal revision report, amend and integrate into phase 2, and return control. |
| Feature SPEC alone is incorporated while FEATURE-TASKS remains active. | Retain necessary active sources and task owner; do not archive the whole package. |
| A complete feature is incorporated with tasks transferred. | Retain eligible sources in its features directory, repair links, mark historical snapshots, then verify/integrate the feature boundary. |
| A legacy working branch already owns the interrupted scope. | Preserve the suitable identity/name and target; do not rename from the new convention alone. |

## Credential recovery examples

| Context | Result |
| --- | --- |
| Authorized push succeeds with the current shell session. | Verify remote containment; no token discovery or credential prompt is needed. |
| Push returns access 403 and gh.tkn is suitable. | sdd-manage verifies ignored/untracked status, refreshes supported shell authentication, retries the established destination, and confirms publication. |
| Shell lacks credentials and no token file exists. | Preserve/create root .gitignore with `*.tkn`, verify exclusion, request a target-repository fine-grained token with the GitHub profile, save gh.tkn beside .gitignore, authenticate, and retry. |
| A token creates an issue but cannot close it. | Treat actual endpoint denial as failed access; check Issues write suitability and request a suitable replacement when needed. Creation alone does not prove closure permission. |
| Several token files have ambiguous provider/repository ownership. | Resolve suitability before selection; preserve unrelated files and do not print values. |
| A token file is already tracked or an ignore negation exposes it. | Block tracked-secret remediation for an explicit decision; fix effective ignore coverage for an untracked file before reuse/save. Preserve unrelated work. |
| Git push succeeds but a connector's API operation is denied. | Recover the API client through its supported credential mechanism or report that mechanism unavailable; shell authentication is not connector authorization. |

## Blocked steering continuation

When a commanded amendment is blocked by an unavailable check, report its branch, paused target, pending changes, and concrete missing facility. A later “Continue that amendment” resumes the same scoped steering workflow after the facility is supplied; it verifies, explicitly merges and publishes, then stops without selecting the next task.

## Branch and operational boundaries

| Context | Result |
| --- | --- |
| Feature preparation through implementation is requested. | Reuse one feature branch; incorporate selected accepted documents before final verification, explicit merge, and target publication. |
| Only one feature task is requested, but the branch includes unrelated unfinished work. | Resolve the scope/branch conflict; do not merge the entire feature by implication. |
| Document incorporation stopped after SPEC changed but before TASKS reconciliation. | Inspect checkpoint and accepted sources; finish only selected owners, preserve history and reassessment notes, then verify/persist the document boundary. |
| A merge is committed but target push was rejected. | Preserve the merge and reconcile destination/divergence/access; finish publication without creating a second merge. |
| Hosted requests encounter rate-limit 403 or 429. | Defer according to backend timing and report pending effects; do not replace a suitable token to evade limits. |
| A hosted write times out. | Backend re-reads exact identities and effects before retrying; incomplete lookup leaves outcome unknown. |

## Review and revision campaigns

| Request | Result |
| --- | --- |
| “Review the credential protocol.” | Start from the prompt; record scope/criteria, located findings, and limits in the campaign review report. Stop before repairs. |
| “Plan and run a comprehensive plugin review.” | Create a review plan; update, commit, and push the report after each planned unit; consolidate findings and revision handoff. |
| “Implement the accepted revision plan.” | Incorporate relevant accepted decisions into governing documents, perform bounded revisions with evidence checkpoints, then verify, explicitly merge, and publish. Retain the campaign plans/reports. |
