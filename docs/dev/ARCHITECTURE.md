# TextStats architecture

The [project brief](PROJECT.md) calls for a small local utility with two consumers: Python callers and the module CLI. This document describes the intended system, not existing implementation.

## Blocks and dependency direction

The counting core owns decoded-text statistics. The file adapter owns UTF-8 decoding and its file handle. The command-line adapter owns arguments, stdin, presentation, diagnostics, and process outcomes. The public facade exports the core result type and counting operations.

CLI → file adapter → counting core; CLI stdin → counting core; public facade → core and file adapter. The core has no filesystem or CLI dependency. No network access, persistent application state, plugin registry, or shared mutable counter is needed. Results belong to each invocation; callers retain their input strings and stdin.

## Choices and invariants

Use functions and an immutable result value rather than inheritance or a service container. Both CLI formats consume the same result to prevent duplicated counting rules. Read and decode one input before counting; a streaming framework would add complexity without a required load constraint. The file adapter closes owned handles on success and failure; the CLI never closes process stdin.

BOM policy and counting semantics have one owner in the core, defined by [SPEC](SPEC.md). Unicode decoding and OS failures propagate through the API and become useful stderr diagnostics at the CLI boundary. No failure emits a partial success result. JSON and stdin extend the adapters without coupling the core to argument parsing.

## Verification seams

Pure text examples verify the core; temporary UTF-8 files verify decoding and handle ownership; subprocess invocations verify the public module entry point, output channels, exit codes, and stdin. [DECOMPOSITION](DECOMPOSITION.md) refines these logical owners and [layout](layout.md) assigns physical homes.
