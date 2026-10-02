# Coordinate review and revision campaigns

Use **sdd-conventions**' **Review campaigns** reference for campaign identity/storage and **sdd-report**'s **Campaign artifacts** reference for formats. Scope the work before choosing focused reviewers; a campaign does not require a separate review or revision skill.

This is the formal campaign path for the [revision core workflow](workflows.md#core-development-workflows). A directly accepted focused amendment can enter revision planning without fabricating a preceding review. At a paused implementation checkpoint, [lightweight steering](workflows.md#steering-as-lightweight-revision) uses the human-defined objective and existing documents rather than requiring campaign artifacts. Both paths retain their own scope and stop rules.

## Review

1. Establish the request, authoritative instructions, exact reviewed source, concerns, criteria, evidence mode, and stopping boundary. A read-only review does not authorize source repairs or external effects. Writing requested review artifacts and their established commit/push checkpoints is distinct from changing the reviewed source.
2. For a comprehensive/systematic review, create a review plan defining units, dependency order, criteria, representative positive/negative scenarios, tooling, evidence limits, and report checkpoints. For a focused review, the prompt may supply the plan; record its scope and criteria in the review report without requiring another file.
3. Route each concern to its owning focused skill and relevant conventions. Review both sides of consequential handoffs, not merely file presence. Distinguish inspected source, consumer assessment, actual local execution, and authorized external verification. Record unavailable checks and unknowns without fabricating evidence.
4. Maintain the review report as each unit is assessed. Allocate stable finding IDs, located baseline evidence, consequence, confidence, bounded correction, and objective recheck. Preserve no-finding coverage and deferred units. Commit and push the updated report after each planned review unit before dependent work.
5. Consolidate coverage, canonical findings, counts, priorities, dependencies, and actual readiness. Return the report and proposed revision queue. Stop before revision unless the request already authorizes it; do not ask again when accepted revisions and their execution are already covered.

## Plan accepted revisions

For a directly accepted prompt-defined revision, record its objective, affected owners, and stable action IDs in the revision plan; omit nonexistent review stages and links rather than inventing findings or a review report. Resolve missing requirement/design decisions before dependent work.

- Record which findings are accepted, deferred, rejected, or require a decision, with reasons and retained IDs. A recommendation need not be treated as a confirmed defect.
- Build an ordered revision plan with affected owners, intended outcomes, dependencies, permitted effects, and verification/recheck criteria. Link actions to findings; one action may address several findings and a finding may require several actions.
- Identify accepted changes to governing PROJECT/design/SPEC/PLAN/layout and TASKS/FEATURE-TASKS. Incorporate relevant decisions through the owning workflows so implementation has current authoritative inputs. The revision plan remains a retained campaign record, not a replacement SPEC or PLAN.
- Preserve selected document scope and task ownership. **sdd-integrate-feature** incorporates accepted feature deltas; **sdd-tasks** creates/reviews task lists; **sdd-implement** owns task execution/completion. Human-commanded checkpoint amendments remain **sdd-steer**-owned. Do not turn an ordinary review into steering or create feature overlays by implication.

## Revise, verify, and finish

1. Establish/reuse the scoped working branch and target under [branch management](branch-management.md), using [Git workflows](git-workflows.md) for integration. A request to implement the accepted revision plan authorizes routine work within that boundary, including its default verified explicit merge/publication.
2. Coordinate accepted governing-document updates and bounded source/test/document changes with their owners. Use task-list execution where executable tasks govern the work; use authorized focused maintenance where no task is assigned. Never invent a task ID from a finding ID.
3. After each revision action, update the revision report with actual changed artifacts, relevant acceptance/recheck evidence, finding disposition, limitations, and Git state. Commit and push source and evidence together before dependent revisions. Unresolved failures retain their actual state; do not mark a finding verified from a planned check or commit alone.
4. Recheck composition and relevant regressions after coupled changes. Keep original review evidence intact; append current verification or link it from canonical dispositions without rewriting the baseline observation as if it never occurred.
5. Verify the completed authorized boundary, explicitly merge, verify the merged result, and publish the target. Record working/target branches, revision commits, merge, publication, and remaining findings. Keep all campaign artifacts in their original directory; no completion-time move or transaction journal is required.

For a blocked campaign, preserve valid work and report the exact active action, affected source/evidence, branch/merge state, and needed decision or facility. A later authorized continuation resumes that campaign and scope rather than repeating completed review units or starting unrelated implementation.
