# Line-range counting delivery delta

Status: named-file milestone implementation verified; accepted delivery strategy is incorporated into main [PLAN](PLAN.md). Retained active for remaining feature task/evidence dependencies. Package: [002_8a53078](features/002_8a53078/README.md). Derived from [FEATURE-SPEC](FEATURE-SPEC.md), [FEATURE_DECOMPOSITION](FEATURE_DECOMPOSITION.md) and unchanged main [PLAN](PLAN.md)/[layout](layout.md). Main PLAN owns milestone 2.3 within existing Phase 2 — Output and input extensions.

## Milestone 2.3 — Line-range counting

Preserve the usable published named-file/JSON checkpoint. First establish pure selected counting with the accepted BOM/newline boundaries and adapter reuse, then deliver the earliest useful changed path: `--lines START:END` on actual named files with both existing formats and usage/failure semantics. No infrastructure-only phase, new package, public API or source-layout allocation is needed.

Named-file delivery depends on completed main T-006; pure selection builds on T-001/T-002. Demonstrate a singleton, an inclusive middle/end range, an EOF-truncated range and an empty selection with exact outputs, plus malformed-range diagnostics. This provides practical feedback for the human to continue, amend, simplify or stop at an authorized checkpoint; historical T-010/T-011 evidence records that demonstration; no human feedback is inferred.

Finish the feature against the currently implemented named-file capability: verify both formats and BOM modes, complete-input decode/read failures, regression preservation, accurate user/module documentation and extracted-source named-file use. Planned stdin compatibility is an interface constraint on source-independent core selection; actual stdin implementation/composition/lifetime/locale verification stays with separately owned main T-007/T-008 and does not gate this feature exit. Those tasks remain unstarted. Later incorporation must reconcile their phase-exit implications without duplicating or marking main tasks complete from feature evidence.

Exit: all named-file FEATURE-SPEC acceptance and unchanged baseline regressions pass, meaningful full unittest discovery and selected named-file source-distribution examples succeed, documentation matches supported options, and the demonstration/limitations are reported. Milestone 2.3 completion measures this feature only; Phase 2 cannot exit while 2.2/T-007/T-008 remain incomplete.

## Sequencing and integration gates

The feature targets the paused `phase/2-output-and-input-extensions` checkpoint. The complete feature delivery is named-file line-range counting with text/JSON output. T-007/T-008 are not prerequisites to feature completion; preserve the source-independent selection interface for their later stdin delivery. No main task resumption or unrelated future capability is required.

Selected incorporation reconciles PROJECT, DECOMPOSITION, SPEC, PLAN and both task owners on the existing feature branch; unchanged ARCHITECTURE/layout are reused. The bounded interruption transfers only T-009, retaining T-010/T-011 ownership in FEATURE-TASKS. Keep active feature sources until incorporation/task/evidence disposition qualifies them for archival. Full feature integration requires coherent implementation, applicable incorporation, verified explicit two-parent merge into the phase target and target publication. It does not complete or merge Phase 2 into main, nor authorize continuation of main tasks.

The physical map is reused: pure selection in `textstats/counting.py`, private named-file collaboration in `textstats/files.py`, CLI argument/source collaboration in `textstats/cli.py`, tests under existing unit/integration owners, user instructions in README. No new physical ownership decision blocks task derivation. Principal risk is accidental BOM reapplication or permissive Unicode splitting for line positions; core-level independent cases protect these contracts. No unresolved routine design or delivery choice remains.
