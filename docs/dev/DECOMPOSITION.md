# TextStats logical decomposition

This refines [ARCHITECTURE](ARCHITECTURE.md). [SPEC](SPEC.md) owns normative public contracts; the interfaces below show collaboration.

| Component | Responsibility and interface | Dependencies and verification seam |
| --- | --- | --- |
| Counting core | Immutable `TextStats` value; `count_text(text, *, strip_bom=True)`; newline and word rules. Does not read files or print. | Standard library only; direct string inputs and expected counts. |
| File adapter | `count_file(path, *, strip_bom=True)` acquires, decodes, delegates, and closes its owned handle. Does not translate failures into process statuses. | Counting core; temporary files, invalid bytes, missing paths, and an independent unreadable-file check. |
| Public facade | Exports `TextStats`, `count_text`, `count_file`; keeps callers independent of internal module locations. Does not duplicate computation. | Core and file adapter; package-level import and documented calls. |
| CLI adapter | Parses one input, BOM and output options, obtains a result, formats stdout, translates read/decode failures. Owns stdin selection in milestone 2.2. | File adapter and core; subprocess checks with separate stdout/stderr/status assertions. |
| Module entry point | Delegates process invocation to the CLI and propagates its exit outcome. | CLI adapter; `python -m textstats` from an extracted source distribution. |

## State and failure ownership

Each call yields a new immutable value. No cached input or global counts exist. File handles belong to the file adapter, stdin belongs to the invoking process, and output streams belong to the CLI environment. API exceptions retain their standard-library types; only the CLI maps them to stderr/status. Failed reads or decoding never feed incomplete text to the core.

The core can be verified without filesystem mocks. Adapter checks should use real temporary files where possible; a narrowly simulated permission denial may supplement platform-sensitive unreadability tests. CLI checks assert user-visible behavior rather than internal function calls. Separate modules are justified by distinct IO and pure-logic failure boundaries; additional factories/interfaces are unnecessary.
