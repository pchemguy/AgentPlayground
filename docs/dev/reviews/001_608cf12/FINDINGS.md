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

## TST-003 — Retired JSON scope remained in the executable checklist

- Type: consumer application consistency defect caught during A-012 review; not an established pinned-plugin source defect. PriorityP3.
- Expected: current TASKS/PLAN describe required accepted work; obsolete JSON-only work is removed without reusing its stable IDs, and genuine historical delivery remains in Git/revision evidence/provider history. Direct steering owns reassessment.
- Observed: the first amended draft made T-006 and Milestone2.1 unchecked executable entries and invented an “unchecked means retired” interpretation. PLAN included former-scope history. This leaves an ordinary current checklist with obsolete unchecked work and ambiguous selection/phase completion.
- Evidence: A-012-initial-retired-scope.json retains exact pre-review TASKS/PLAN and observed Git identity. Exact coordinator correction retained in A-012-retired-scope-review.txt.
- Correction: existing amendment scope requires removal of obsolete executable rows, preserving T-006/2.1 identity and historical evidence in the minimal revision record/Git/hosted associations. No new tasks, false completion or pinned-package modification is authorized.
- State: correction and objective final recheck pending. Assessment must disclose review assistance and original draft; do not claim unassisted first-pass compliance.

Resolution: amendment `6561e287e59c8b4e86c7a3cdeaaa48a60df82154` and target merge `1d11ae343bfb3a1dcd6c12431ad401ecba77bfa6` are published with exact remote equality. Independent checks establish ten unique current task owners excluding retired T-006, preserved original checked T-006 history in the minimal revision report, no former-scope PLAN paragraph, unchanged public core/file/API modules, 39 passing tests and 62 literal CLI cases plus help/literal-filename checks. T-007/T-008 and phase2 remain incomplete. Review assistance remains disclosed.

## TST-004 — Provider body retention and inspection

- Type: campaign record handling defect, not a pinned-plugin source defect; priorityP3.
- Observed: three A-013 consumer metadata artifacts retained provider body/description fields; root inspection mistakenly displayed task bodies. No token exposure was observed.
- Correction: recursively replace body/description fields with SHA256 before publication, retain affected filenames/method/incident in A-013-record-sanitization.json, and use purpose-built metadata-only read observers thereafter. Product and provider state are unchanged by record sanitization. The display cannot be undone; it is explicitly disclosed rather than described as compliant raw-body handling.
- State: corrected before A-013 record publication; assessment discloses the record-handling intervention.
