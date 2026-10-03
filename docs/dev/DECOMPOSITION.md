# TextStats logical decomposition

This refines [ARCHITECTURE](ARCHITECTURE.md). [SPEC](SPEC.md) owns normative public contracts; the interfaces below show collaboration.

| Component | Responsibility and interface | Dependencies and verification seam |
| --- | --- | --- |
| Counting core | Immutable `TextStats` value; `count_text(text, *, strip_bom=True)`; canonical BOM/newline/word rules and private `_count_selected(text, line_range, *, strip_bom=True)` decoded-input selection. Does not read files or print. | Standard library only; direct string inputs and expected counts. |
| File adapter | `count_file(path, *, strip_bom=True)` acquires, strictly decodes the complete file, delegates, and closes its owned handle; private `_count_file_selected` passes optional validated endpoints to the core. Does not translate failures into process statuses. | Counting core; temporary files, invalid bytes, missing paths, and an independent unreadable-file check. |
| Public facade | Exports `TextStats`, `count_text`, `count_file`; keeps callers independent of internal module locations. Does not duplicate computation. | Core and file adapter; package-level import and documented calls. |
| CLI adapter | Parses one input, BOM/output options and one positive inclusive ASCII-decimal range before input acquisition; obtains a result, formats stdout and translates read/decode failures. Owns stdin acquisition in milestone 2.2 and delegates fully decoded stdin to the same pure selection owner. | File adapter and core; subprocess checks with separate stdout/stderr/status assertions. |
| Module entry point | Delegates process invocation to the CLI and propagates its exit outcome. | CLI adapter; `python -m textstats` from an extracted source distribution. |

## State and failure ownership

Each call yields a new immutable value. No cached input or global counts exist. File handles belong to the file adapter, stdin belongs to the invoking process, and output streams belong to the CLI environment. API exceptions retain their standard-library types; only the CLI maps them to stderr/status. Failed reads or decoding never feed incomplete text to the core.

The core can be verified without filesystem mocks. Adapter checks should use real temporary files where possible; a narrowly simulated permission denial may supplement platform-sensitive unreadability tests. CLI checks assert user-visible behavior rather than internal function calls. Separate modules are justified by distinct IO and pure-logic failure boundaries; additional factories/interfaces are unnecessary.

## Selected-input collaboration

The core applies original whole-input BOM policy exactly once before selecting CR/LF/CRLF segments with their terminators. An originally interior BOM remains content even when selection exposes it first. Unicode separators affect words without creating line positions. The file adapter never stops reading or decoding at END. Public facade signatures and exports remain whole-input operations. CLI validation and output formatting do not enter the core; private decoded-input selection is independent of its named-file or future stdin source.
