# Line-range counting design delta

Status: proposed and unimplemented. Active package: [002_8a53078](features/002_8a53078/README.md). Unchanged major blocks and dependency direction remain owned by [ARCHITECTURE](ARCHITECTURE.md); no architectural overlay or new physical layer is needed. This delta revises the affected logical responsibilities in [DECOMPOSITION](DECOMPOSITION.md), subject to later explicit incorporation.

## Affected components

The counting core additionally owns a private decoded-text range-counting operation. It applies the whole-input BOM policy once, recognizes only CR, LF and CRLF logical segments with their terminators, selects contiguous one-based inclusive positions, and computes a TextStats result from selected segments. Existing `count_text` and `count_file` public signatures, results and whole-input behavior remain intact. Private collaboration must share canonical BOM/counting rules instead of duplicating them in the CLI or removing a BOM again after selection. A BOM that originally begins a later line remains interior even when that line becomes the first selected line.

The file adapter reads and strictly decodes the complete input, owns and closes its handle, and delegates selected counting to the pure core through a private collaboration seam. Ordinary public file calls retain whole-input behavior. Reading only selected bytes or stopping decoding at END would violate existing complete-input failure semantics and is excluded.

The CLI owns endpoint syntax/validation, source selection and success/failure presentation. Validated endpoints travel with the decoded input to the core. Default and JSON presentation use the same immutable result. The planned stdin path acquires strict UTF-8 bytes until EOF without closing process stdin, then invokes the same selection owner. No new filesystem dependency enters the core; no output-format dependency enters selection.

## Verification and compatibility seams

Pure private-core checks use independent literal expected counts for range boundaries, logical empty lines, mixed terminators, Unicode separators and BOM ordering. Real temporary files protect strict decoding and handle lifecycle. Module subprocesses verify range syntax, output formats, channels, unchanged input and composition. Stdin checks become executable only after main task T-007 provides that source. Existing public import/API tests protect the unchanged facade.

The existing [layout](layout.md) already allocates these responsibilities to counting.py, files.py, cli.py and their unit/integration tests. No layout mutation is required during preparation. [FEATURE-SPEC](FEATURE-SPEC.md) owns exact behavior; [FEATURE-PLAN](FEATURE-PLAN.md) owns delivery gates.
