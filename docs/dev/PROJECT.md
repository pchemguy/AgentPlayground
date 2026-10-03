# TextStats project brief

TextStats helps Python users and shell users count lines and whitespace-separated words in UTF-8 text. It provides an importable API and `python -m textstats` with predictable plain output and exit status.

## Scope

The complete intended system includes named files, optional removal of a leading UTF-8 BOM, universal newline handling, baseline failures, inclusive named-file line selection through `--lines START:END`, and stdin selected by `-` with the same selection semantics. Delivery is incremental; [PLAN](PLAN.md) defines the usable slices and [TASKS](TASKS.md) defines executable work.

## Constraints and non-goals

Python 3.11 or newer, standard-library runtime and unittest, no external dependencies or services. Existing vendored tools and repository infrastructure are preserved. Recursive traversal, multiple-input aggregation, alternate encodings, wheel publication, and performance guarantees for arbitrarily large inputs are outside scope. Public Python APIs retain whole-input counting; range selection is a CLI option.

## Terms and navigation

A line is a logical segment separated by LF, CR, or CRLF; a trailing terminator does not create an extra line. Words are whitespace-separated tokens. [SPEC](SPEC.md) owns exact semantics and failures; [ARCHITECTURE](ARCHITECTURE.md) and [DECOMPOSITION](DECOMPOSITION.md) own design; [layout](layout.md) owns paths.
