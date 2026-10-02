# Select sufficient checks

Read the accepted contract and requested work boundary before selecting commands. Inspect the actual diff or relevant implementation, declared tooling, and tests. A task's expected edit scope helps locate effects; it does not excuse ignoring dependent behavior affected by its changes.

## Scope and evidence

| Boundary | Evidence to establish |
| --- | --- |
| Task | Its acceptance conditions and directly affected behavior, including necessary regressions. |
| Selected change | Changed contracts, affected consumers, compatibility, and integration paths. |
| Milestone or phase | Applicable PLAN exit conditions, constituent results, and cross-component behavior. |
| Project | Requested acceptance, integration, build, packaging, or other project-level checks. |

For feature work, use the owning FEATURE-TASKS and relevant feature contracts alongside applicable main requirements. A feature's scoped parent checkbox does not establish the whole-project milestone or phase exit conditions.

## Select checks

1. Identify observable acceptance conditions and the evidence each needs. Reuse meaningful tests, inspections, examples, or measurements; do not create artificial tests merely to populate a checklist.
2. Select direct checks for affected behavior, dependent checks for relevant consumers, integration checks for collaborating components, and exit checks for the requested boundary. Include failure paths and operational risks where the contract calls for them.
3. Follow mandatory project commands, suites, supported environments, and boundary checks. Run the declared full suite when project policy or the requested scope requires it; report why checks are omitted or unavailable. An apparently small change does not waive governing requirements.
4. Use existing test routing when helpful, but inspect whether it still reflects the changed components and contracts. Report missing or stale mapping entries rather than treating the map as proof of coverage.
5. Identify coverage gaps and unsuitable checks. Return needed test design or changes through the implementation workflow to **sdd-tdd**; verification does not silently add tests or redefine acceptance.

Select checks proportionate to the requested claim. For example, compilation does not establish runtime behavior, a unit check may not establish packaging, and a timing run does not establish correctness. Documentation may need inspected contracts, executable examples, link checks, or documentation generation instead of unrelated runtime tests. Performance or security claims require evidence appropriate to the particular claim.
