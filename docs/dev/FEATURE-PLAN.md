# Line-range counting delivery delta

Status: planned and unimplemented. Package: [002_8a53078](features/002_8a53078/README.md). Derived from [FEATURE-SPEC](FEATURE-SPEC.md), [FEATURE_DECOMPOSITION](FEATURE_DECOMPOSITION.md) and unchanged main [PLAN](PLAN.md)/[layout](layout.md). This proposes additional milestone 2.3 within existing Phase 2 — Output and input extensions; main owners are not amended in this preparation.

## Milestone 2.3 — Line-range counting

Preserve the usable published named-file/JSON checkpoint. First establish pure selected counting with the accepted BOM/newline boundaries and adapter reuse, then deliver the earliest useful changed path: `--lines START:END` on actual named files with both existing formats and usage/failure semantics. No infrastructure-only phase, new package, public API or source-layout allocation is needed.

Named-file delivery depends on completed main T-006; pure selection builds on T-001/T-002. Demonstrate a singleton, an inclusive middle/end range, an EOF-truncated range and an empty selection with exact outputs, plus malformed-range diagnostics. This provides practical feedback for the human to continue, amend, simplify or stop at an authorized checkpoint; preparation alone does not authorize that demonstration or implementation.

Finish composition with planned strict UTF-8 stdin after separately implemented main T-007. Verify both formats and BOM modes on both sources, locale independence, complete-input decode/read failures, process-owned stdin lifetime, regression preservation, accurate user/module documentation and extracted-source use. Main T-008 remains independently owned and unstarted; its phase-exit/distribution work overlaps the feature's final checks and needs explicit reconciliation during later incorporation. Do not duplicate or mark main tasks complete from feature evidence.

Exit: all FEATURE-SPEC acceptance and unchanged baseline regressions pass, meaningful full unittest discovery and selected source-distribution examples succeed, documentation matches supported options, and the demonstration/limitations are reported. Milestone 2.3 completion measures this feature only; Phase 2 cannot exit while 2.2/T-007/T-008 remain incomplete.

## Sequencing and integration gates

The feature targets the paused `phase/2-output-and-input-extensions` checkpoint. T-007 is a hard prerequisite to complete stdin-specific feature verification, not permission to resume it on this branch. If implementation is later authorized before stdin exists, pause after the named-file capability and leave the stdin-dependent exit unchecked. No unrelated future capability is required.

Preparation persists active FEATURE documents on the feature branch and stops. Later explicit scope must decide incorporation into PROJECT, DECOMPOSITION, SPEC, PLAN and both task owners; existing ARCHITECTURE/layout can be reused if unchanged. Keep active feature sources until incorporation/task/evidence disposition qualifies them for archival. Full feature integration requires coherent implementation, applicable incorporation, verified explicit two-parent merge into the phase target and target publication. It does not complete or merge Phase 2 into main, nor authorize continuation of main tasks.

The physical map is reused: pure selection in `textstats/counting.py`, private named-file collaboration in `textstats/files.py`, CLI argument/source collaboration in `textstats/cli.py`, tests under existing unit/integration owners, user instructions in README. No new physical ownership decision blocks task derivation. Principal risk is accidental BOM reapplication or permissive Unicode splitting for line positions; core-level independent cases protect these contracts. No unresolved routine design or delivery choice remains.
