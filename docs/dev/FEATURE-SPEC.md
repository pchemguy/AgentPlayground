# Line-range counting specification delta

Status: proposed and unimplemented. Package: [002_8a53078](features/002_8a53078/README.md). This additive delta revises the main [SPEC](SPEC.md) CLI invocation and its explicit exclusion of line selection; it also adds a selected-counting contract. The [PROJECT](PROJECT.md) line-selection non-goal remains the accepted main baseline until later explicit incorporation. All unchanged counting, UTF-8, resource, output and quality contracts stay owned by main SPEC. [FEATURE_DECOMPOSITION](FEATURE_DECOMPOSITION.md) owns affected collaboration.

## CLI range contract

Proposed invocation: `python -m textstats [--keep-bom] [--json] [--lines START:END] INPUT`. One optional range may appear in normal argparse option order; `--lines=START:END` is also supported. Both endpoints consist of one or more ASCII decimal digits representing positive integers, with START <= END. Leading zeros are accepted with decimal meaning; no arbitrary upper endpoint limit is imposed. Signs, whitespace, Unicode digits, empty/open endpoints, extra colons, zero and reversed ranges are unsupported. Repeating `--lines` is a usage error rather than silently overriding a previous value.

Malformed/missing range values and repetitions return status 2 with useful nonempty stderr, no success stdout and no traceback. Validate usage before acquiring the input, so an invalid range is a usage failure even with a nonexistent input. Help documents inclusive one-based endpoints and available-subset behavior. Existing help status 0 and `--` semantics remain.

Omitting the option preserves existing whole-input behavior and public Python API signatures. This feature introduces no public Python range parameter or export, multiple ranges, negative/from-end positions, alternate encodings or streaming guarantee.

## Selected counting contract

Strictly decode the entire source as UTF-8 before counting; read/decode failures anywhere, including outside the requested range, keep main SPEC status 1 and no partial success output. Apply the configured BOM policy to the complete decoded input exactly once, then identify logical lines using main SPEC: CRLF is one terminator, lone CR/LF terminate lines, a nonempty unterminated final segment is a line, and a final terminator adds no phantom line. Other Unicode separators may divide words but never line positions.

Number logical lines from 1. Select existing lines whose positions satisfy START <= position <= END, retaining their original contents and terminators. Count only these lines and their Unicode whitespace-separated words. `lines` reports the number selected, not END minus START plus one when the request extends beyond EOF. Selection beyond EOF or from empty input yields (0,0), status 0 and no stderr. Blank logical lines count as selected lines and can contain zero words. Removing the only leading BOM can make input empty before numbering; retaining it follows main SPEC ordinary-character semantics.

An interior U+FEFF is never removed because selection exposes it at the beginning. `--keep-bom` affects the actual leading input BOM only; when line 1 is excluded that leading BOM contributes no selected word. Inputs are unchanged and file/stdin resource ownership is preserved.

## Formats and planned stdin

Default selected success remains exactly `lines=<N> words=<N>\n`; JSON remains one object with exactly `lines` and `words` integer fields plus newline. Both have status 0 and empty stderr. Add no selection metadata or extra output fields. Options compose in either order with JSON and BOM policy.

Once main milestone 2.2/T-007 delivers `-`, selection applies identically to complete strictly decoded stdin, independent of locale, with EOF and stream-lifetime rules from main SPEC. This preparation does not implement or resume stdin; at the observed checkpoint `-` remains a named file. Invalid UTF-8/read failures identify the applicable source and keep status 1.

## Objective acceptance

The following are literal expected counts, with default BOM removal unless stated. Use each appropriate case with named-file CLI text and JSON; pure-core checks establish the same counting boundaries.

| Complete decoded input | Range | Selected lines | Selected words |
| --- | --- | ---: | ---: |
| `alpha beta\nbeta\nlast two` | `2:3` | 2 | 3 |
| `alpha beta\nbeta\nlast two` | `1:1` | 1 | 2 |
| `alpha beta\nbeta\nlast two` | `2:99` | 2 | 3 |
| `alpha beta\nbeta\nlast two` | `4:99` | 0 | 0 |
| empty input | `1:3` | 0 | 0 |
| `a\n\n` | `2:9` | 1 | 0 |
| `a\r\nb c\rd\n` | `2:3` | 2 | 3 |
| `a` + U+2028 + `b\nc` | `1:1` | 1 | 2 |
| U+FEFF only | `1:1` | 0 | 0 |
| U+FEFF only, keep BOM | `1:1` | 1 | 1 |
| U+FEFF + ` a\nb`, either BOM mode | `2:2` | 1 | 1 |
| `a\n` + U+FEFF + ` b` | `2:2` | 1 | 2 |
| two leading U+FEFF characters | `1:1` | 1 | 1 |

Also accept `01:02` as decimal (1,2), a singleton range on an unterminated final line, all-lines ranges equivalent to no range, and LF/CR/CRLF blank-line boundaries. Reject representative syntax `0:1`, `2:1`, `-1:2`, `1:`, `:2`, `1:2:3`, `1.0:2`, `+1:2`, whitespace and Unicode digits, missing values, and repeated options with status/channel assertions. Real invalid UTF-8 after END still fails. Existing no-range core/API/CLI/failure/JSON/distribution checks remain green. After T-007, exercise empty/BOM/mixed-newline stdin in both formats with locale-independent UTF-8 and source lifetime/read/decode failures. Extracted-source invocation and documented examples must show selected named-file and stdin use at the feature exit. No unresolved material specification decisions remain.
