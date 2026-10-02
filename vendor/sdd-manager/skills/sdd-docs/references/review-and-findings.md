# Documentation review and findings

## Establish coverage

For a change-scoped review, inspect affected modules, consequential API changes, and README or guide sections that describe them. Report wider gaps without silently expanding the work boundary. For a project-wide audit, inventory every project-owned code module and the project's standalone documentation; include scripts, entry points, and tests unless project policy excludes them. Account for generated or externally maintained code separately and report the applicable editing policy.

Assess module coverage, documentation style, API contracts, README alignment, examples, navigation, duplication, stale guidance, and documentation placement as relevant. Missing documentation and misleading documentation are distinct findings. A module's docstring existing is not proof that its content is adequate.

## Governing-document amendments

If resolution would require changing SPEC, PLAN, design, layout, or another authoritative requirement, report the finding to the user using these fields:

| Field | Content |
| --- | --- |
| Location | Affected document section and relevant code, test, or usage. |
| Issue | Inconsistency, missing guidance, or unsupported claim and the inspected evidence. |
| Impact | Consequences for users, maintainers, implementation, or verification. |
| Proposed amendment | Concise recommendation and any decision still needed. |

Defer the amendment to the user. Do not edit the governing document or automatically invoke its owning skill. Keep dependent documentation work unresolved and identified; continue independent work within the accepted scope. Do not assume that observed implementation is correct merely because it differs from a requirement.

## Review result

Return module and document coverage, style selected and its governing source or fallback, fixes made, remaining findings, checks actually performed, and limitations. Identify whether each example or command was inspected or executed. For a project-wide audit, report modules with missing or inadequate documentation and excluded modules with reasons. Maintain evidence sufficient for the implementation workflow to review the result without requiring a separate documentation journal.
