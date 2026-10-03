# Acceptance campaign findings

## TST-001 — Preparation prompt omitted retained test-directory requirement

- Type: campaign input omission; priorityP3; scope is harness/consumer preparation, not a confirmed pinned-plugin source defect.
- Baseline: accepted source revision plan prescribes product tests in tests/unit and tests/integration. Retained A-001 raw request omitted those paths; consumer layout consequently chose flat tests, and A-004 followed its governing layout.
- Effect: committed tests exist and behavior checks remain valid, but the campaign's stated retained organization is not yet met. Do not falsely attribute compliance or blame a consumer that never received this requirement.
- Correction authorized by existing plan: A-005 request explicitly supplies the original requirement and authorizes focused layout/test-package alignment while preserving historical evidence. Production contracts and pinned source identity remain unchanged.
- State: Resolved in A-005 pending actual directory/layout/recheck/publication evidence. Objective recheck: unit/integration discoverable packages, links/commands/current layout agree, nonempty moved suite and CLI checks run, scoped changes published.

Resolution: layout maintenance `0b97f4b` preserved moved core/API test contents byte-for-byte; discoverable unit/integration packages are present. A-005 independent full suite ran17 tests and eight literal CLI cases passed. T-002/T-003 published, main unmerged. Pinned plugin unchanged.

## TST-002 — Future stdin compatibility expanded into a feature-completion dependency

- Type: campaign input ambiguity and document-consistency correction; scope is A-008 preparation, not an established pinned-plugin defect.
- Input: the retained preparation request requires planned stdin compatibility while forbidding main-task resumption. It did not explicitly say that named-file line-range completion must precede stdin delivery.
- Observed: initial preparation `37ff9bc` made T-011 and the feature exit depend on separately unstarted T-007, preventing the accepted feature-before-stdin sequence. The original five documents, prompt and actual outputs are retained.
- Correction: evaluator supplied an explicit scope clarification: deliver the complete named-file text/JSON feature now; preserve source-independent selection as the interface constraint for later main T-007/T-008. No main owner, product contract or pinned package changed. A residual T-010 pause condition was identified during review and sent back for correction.
- Assessment limit: this pass includes a recorded coordinator clarification and consistency review; it does not claim an unassisted initial preparation. Final independent checks and case assessment record the coherent published package, preservation of all existing tracked blobs and unchecked unique task owners.

Resolution: final preparation `62b5408e80adc2ac12464e5f9163b3afd47a58ba` published with exact remote equality. T-011 depends only on T-010; T-010 residual pause removed. Independent checks confirm five added active documents, all previous tracked blobs intact, 26 local links, 11 unique current task IDs with T-009–T-011 unchecked and all97 pinned hashes unchanged. Current package remains explicitly unimplemented.
