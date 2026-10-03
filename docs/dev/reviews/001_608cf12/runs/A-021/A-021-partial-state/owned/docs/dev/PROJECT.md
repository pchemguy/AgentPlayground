# TextStats project brief

TextStats helps Python users and shell users count lines and whitespace-separated words in UTF-8 text. It provides an importable API and `python -m textstats` with predictable machine-readable output and exit status.

## Scope

The complete intended system includes named files, optional removal of a leading UTF-8 BOM, universal newline handling, baseline failures, optional JSON output, optional one-based inclusive CLI line-range selection, and stdin selected by `-`. Delivery is incremental; [PLAN](PLAN.md) defines the usable slices and [TASKS](TASKS.md) defines executable work.

## Constraints and non-goals

Python 3.11 or newer, standard-library runtime and unittest, no external dependencies or services. Existing vendored tools and repository infrastructure are preserved. Public Python range parameters, multiple ranges, negative/from-end positions, recursive traversal, multiple-input aggregation, alternate encodings, wheel publication, and performance guarantees for arbitrarily large inputs are outside scope. The brief describes the complete intended system; delivery status and verified evidence belong to TASKS.

## Terms and navigation

A line is a logical segment separated by LF, CR, or CRLF; a trailing terminator does not create an extra line. Words are whitespace-separated tokens. [SPEC](SPEC.md) owns exact semantics and failures; [ARCHITECTURE](ARCHITECTURE.md) and [DECOMPOSITION](DECOMPOSITION.md) own design; [layout](layout.md) owns paths.
