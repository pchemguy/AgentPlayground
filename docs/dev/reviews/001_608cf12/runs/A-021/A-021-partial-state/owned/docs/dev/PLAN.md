# TextStats delivery plan

Deliver the [SPEC](SPEC.md) through an early usable named-file slice and small adapter increments. [ARCHITECTURE](ARCHITECTURE.md) and [DECOMPOSITION](DECOMPOSITION.md) permit the pure counting rules to remain stable. This is delivery strategy, not completed progress.

## Phase 1 — Named-file baseline

### Milestone 1.1 — Usable named-file API and CLI

Deliver the public count value/functions, UTF-8 named-file reading, BOM option, universal newline and word semantics, and the default module CLI success path. Core and file adapter precede CLI integration; no infrastructure-only milestone delays the useful outcome. Baseline failure polish and source packaging evidence remain for 1.2, while JSON and stdin remain in phase 2.

Exit: demonstrate importable calls and `python -m textstats` on actual named files with exact expected counts/output; check empty input, BOM modes, Unicode whitespace, mixed terminators, and trailing terminators. Gather a concise API/CLI example to let the human judge usability and choose continue, amend, simplify, or stop at a requested checkpoint. This exit proves the usable success slice, not the entire baseline acceptance.

### Milestone 1.2 — Reliable baseline and distribution

Finish API error preservation and CLI read/decode/usage failures, professional docstrings and user documentation, and source distribution/module entry-point checks. Depends on 1.1. Distribution uses a self-contained source archive and Python module execution, avoiding third-party build tools; wheel and console-script publication are outside scope.

Exit: useful stderr and statuses 1/2, no partial stdout or tracebacks, closed owned handles, help/status 0, dash-prefixed paths through `--`, successful extracted-source imports and module launch, accurate examples, and full nonempty unittest discovery. Phase 1 exits only after both milestones and these checks pass; explicitly merge the complete verified phase into main and verify/push the merged state. Retain partial ranges on the phase branch.

## Phase 2 — Output and input extensions

### Milestone 2.1 — JSON output

Add `--json` while preserving default output and all baseline failures. Depends on completed phase 1. Exit: stdlib JSON parsing confirms exactly the keys `lines` and `words` with integer values; BOM option composes, default regressions and error channels pass, and examples show practical shell use. The demonstration informs the human's next bounded continuation decision.

### Milestone 2.2 — UTF-8 stdin

Add `-` as stdin with strict UTF-8 and process-owned stream lifetime. Depends on 2.1 and the named-file range capability in 2.3 so both formats, BOM modes and whole-input/selected counting compose with both sources. Exit: piped text, empty input, BOM modes, mixed newlines, malformed bytes, stdin read failures, JSON and range composition, locale-independent strict decoding, failures outside selected endpoints, and retained named-file behavior are verified. Full nonempty discovery, documentation and extracted-source whole-input/selected stdin module checks complete the phase only after milestone 2.3 also meets its named-file exits. Integrate by an explicit two-parent merge only at the full phase exit and verify/push main.

### Milestone 2.3 — Line-range counting

Deliver optional `--lines START:END` on named files in both text and JSON formats, preserving BOM policy, complete-input strict UTF-8 decoding, baseline failures and unchanged public Python APIs. Pure selection depends on T-001/T-002; named-file CLI delivery depends on T-006 and the selection core. This milestone can finish at the paused JSON checkpoint before 2.2: numeric labels do not require stdin first.

First establish pure decoded-text selection and file-adapter collaboration, then demonstrate the earliest useful changed path on real named files: singleton, inclusive middle/end, EOF-truncated and empty selection with exact outputs, plus malformed-range diagnostics. Record the demonstration and limitations for the human continuation/amendment/stop decision without inferring feedback.

Exit: SPEC named-file selection acceptance in both formats and BOM modes, syntax and usage precedence, complete-input decode/read failures and owned-handle cleanup, baseline/public API regressions, meaningful full unittest discovery, accurate documentation and extracted-source selected examples. The decoded-text selection seam must remain compatible with future stdin; actual stdin integration is owned by milestone 2.2/T-007/T-008 and does not gate this named-file milestone. Phase 2 remains incomplete until both milestones' exits are met.

The feature campaign targets the paused phase branch. Coherent incorporation, source/task evidence disposition and verified explicit two-parent feature integration update that phase's accepted inputs; they do not complete Phase 2 or merge it into main. Retain active feature sources while remaining owners depend on them.

## Verification and decision policy

Use Python >=3.11 and `python -m unittest discover -s tests -v` once tests exist, with independent expected values and subprocess evidence. Focused checks accompany each bounded task; milestone exits combine relevant acceptance and regressions. Record actual commands, results, and remaining limitations when implementation occurs. Permission-denied behavior needs evidence that remains meaningful under privileged runners; simulated OS denial can supplement real filesystem fixtures.

Main is the integration target and origin the remote. Future implementation uses `phase/1-named-file-baseline` then `phase/2-output-and-input-extensions`, starting phase 2 from published verified main. Complete phases integrate; partial ranges push and pause. Consequential checkpoint decisions remain human decisions, without redundant approval for already authorized routine steps. This preparation authorizes no execution of those phases. No unresolved material planning decisions remain.
