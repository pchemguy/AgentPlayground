# TextStats executable tasks

Derived from [PROJECT](PROJECT.md), [ARCHITECTURE](ARCHITECTURE.md), [DECOMPOSITION](DECOMPOSITION.md), [SPEC](SPEC.md), [PLAN](PLAN.md), and [layout](layout.md). These are planned tasks; none has been implemented or verified. IDs are project-wide and stable. No hosted projection is active.

Preparation baseline: `61f9670736c58b841519f9484239ee05eff58e63`; working/integration branch `main`, remote `origin`. Preparation stops here. Future bounded implementation selects from this list through sdd-implement; the first selectable task is T-001. Phase branch names and full-phase integration gates are in PLAN. Never infer completion from this list alone.

## Phase 1 — Named-file baseline

- [ ] Phase 1 — Named-file baseline
    - [ ] Milestone 1.1 — Usable named-file API and CLI
        - [ ] T-001 — Implement the public counting core
            Scope: `textstats/counting.py`, public facade, discoverable test package, counting/API tests and professional docstrings. Depends on: none.
            Outcome: immutable public result and `count_text` with SPEC counting/BOM semantics; independent expected values cover empty, whitespace, Unicode, CR/LF/CRLF and trailing terminators. Evidence: focused unittest checks and package-level import, including BOM-only/preserved interior BOM cases. No IO or CLI behavior belongs here.
        - [ ] T-002 — Expose UTF-8 named-file counting
            Scope: file adapter, public exports and file/API tests with relevant docstrings. Depends on: T-001.
            Outcome: `count_file` reads real UTF-8 files and delegates BOM policy while owning/closing its handle. Evidence: temporary-file public API calls with fixed expected counts and success-path handle lifecycle; keep pure counting tests independent. Failure completion belongs to T-004.
        - [ ] T-003 — Deliver the usable named-file module CLI
            Scope: CLI adapter, module entry point, CLI subprocess tests and a concise README example. Depends on: T-002.
            Outcome: one named input, default output, `--keep-bom`, exit 0 and silent stderr. Evidence: actual `python -m textstats` subprocesses, exact stdout/status assertions and milestone 1.1 API/CLI demonstration with empty/BOM/mixed-newline fixtures. Record the bounded milestone exit and any human feedback; do not claim phase completion.
    - [ ] Milestone 1.2 — Reliable baseline and distribution
        - [ ] T-004 — Complete baseline failure and usage handling
            Scope: file/CLI adapters, focused file and CLI tests and error docstrings. Depends on: T-003.
            Outcome: preserve API OSError/UnicodeDecodeError, close owned handles on failure, useful CLI diagnostics/status 1 with no success output; usage status 2, help status 0, dash-prefixed filenames through `--`. Evidence: missing/unreadable/malformed UTF-8 files, invalid invocations and channel checks. Use meaningful permission-denial evidence under privileged runners and document its limits.
        - [ ] T-005 — Verify baseline documentation and source distribution
            Scope: README, all public/module docstrings, distribution tests and baseline exit evidence attached to this task. Depends on: T-004.
            Outcome: documented API, BOM, input/output/statuses and source usage; stdlib archive/extraction checks establish imports and module execution outside the checkout. Evidence: meaningful extracted-package tests, documented example checks, `python -m unittest discover -s tests -v` with nonzero tests, and all PLAN 1.2/phase 1 exits. Exclude infrastructure and secrets from distribution. Phase integration occurs only after all phase exits pass, with explicit merge and merged-state verification/push per policy.

## Phase 2 — Output and input extensions

- [ ] Phase 2 — Output and input extensions
    - [ ] Milestone 2.1 — JSON output
        - [ ] T-006 — Add and verify JSON output
            Scope: CLI formatter/parser, CLI tests, README/docstrings and milestone 2.1 evidence. Depends on: T-005 and verified/published phase 1 integration.
            Outcome: `--json` emits the SPEC object/newline and composes with BOM policy, retaining default text and failure behavior. Evidence: stdlib parsed JSON keys/value types and fixed counts, default-output/channel regressions, documented demonstration and full discovery. Record the milestone decision evidence; pause on the phase branch if only 2.1 is requested.
    - [ ] Milestone 2.2 — UTF-8 stdin
        - [ ] T-007 — Support stdin through the dash input
            Scope: CLI source acquisition, CLI tests and relevant docstrings. Depends on: T-006.
            Outcome: `-` reads strict UTF-8 stdin until EOF without closing it; both output formats/BOM modes work and read/decode failures identify stdin. Evidence: binary subprocess input covering empty/BOM/mixed terminators/invalid bytes, locale independence, appropriate stream-lifetime/read-failure checks and named-file regressions. Counting remains owned by the core.
        - [ ] T-008 — Verify complete stdin delivery and phase exits
            Scope: README, distribution/CLI integration checks and phase 2 exit evidence attached to this task. Depends on: T-007.
            Outcome: accurate pipe/API/JSON examples and complete intended acceptance with packaged module invocation. Evidence: both formats and sources compose; named-file errors/defaults remain correct; extracted-source stdin smoke, documentation checks and full nonempty unittest discovery meet PLAN 2.2/phase 2 exits. Explicitly integrate only the complete verified phase, verify merged-state regressions and push main; then stop at the authorized boundary.
