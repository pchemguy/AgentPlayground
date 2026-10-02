# Acceptance campaign findings

## TST-001 — Preparation prompt omitted retained test-directory requirement

- Type: campaign input omission; priorityP3; scope is harness/consumer preparation, not a confirmed pinned-plugin source defect.
- Baseline: accepted source revision plan prescribes product tests in tests/unit and tests/integration. Retained A-001 raw request omitted those paths; consumer layout consequently chose flat tests, and A-004 followed its governing layout.
- Effect: committed tests exist and behavior checks remain valid, but the campaign's stated retained organization is not yet met. Do not falsely attribute compliance or blame a consumer that never received this requirement.
- Correction authorized by existing plan: A-005 request explicitly supplies the original requirement and authorizes focused layout/test-package alignment while preserving historical evidence. Production contracts and pinned source identity remain unchanged.
- State: Resolved in A-005 pending actual directory/layout/recheck/publication evidence. Objective recheck: unit/integration discoverable packages, links/commands/current layout agree, nonempty moved suite and CLI checks run, scoped changes published.

Resolution: layout maintenance `0b97f4b` preserved moved core/API test contents byte-for-byte; discoverable unit/integration packages are present. A-005 independent full suite ran17 tests and eight literal CLI cases passed. T-002/T-003 published, main unmerged. Pinned plugin unchanged.
