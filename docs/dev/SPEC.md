# TextStats specification

This specifies the complete intended system from [PROJECT](PROJECT.md), with responsibilities in [DECOMPOSITION](DECOMPOSITION.md). [PLAN](PLAN.md) schedules realization without removing later requirements. It defines intended behavior, not implementation status.

## Counting contract

`TextStats` is an immutable public value with integer fields `lines` and `words`, both nonnegative. `count_text(text: str, *, strip_bom: bool = True) -> TextStats` and `count_file(path: str | os.PathLike[str], *, strip_bom: bool = True) -> TextStats` are importable directly from `textstats`. These public Python operations count the whole input; line selection introduces no public range parameter or export.

When `strip_bom` is true, remove exactly one U+FEFF at the start of decoded input. Preserve an interior BOM; false preserves all BOMs. File bytes are decoded strictly as UTF-8. Apply this policy equally to strings, files, and stdin. BOM retention treats U+FEFF as an ordinary non-whitespace character; it may therefore contribute a word.

Recognize CRLF as one terminator and lone CR or LF as one terminator. Nonempty text has one line per terminator plus one for a nonempty final segment. A final terminator adds no phantom line; empty text after BOM handling has zero lines. Other Unicode line separators do not terminate lines. Words are maximal tokens separated by Python Unicode whitespace (`str.split()` semantics), independent of line counting.

| Input after BOM handling | lines | words |
| --- | ---: | ---: |
| empty string | 0 | 0 |
| `alpha beta` | 1 | 2 |
| `alpha\n` | 1 | 1 |
| `\n` | 1 | 0 |
| `alpha\r\nbeta\rgamma\n` | 3 | 3 |
| `alpha\n\n` | 2 | 1 |
| space followed by tab | 1 | 0 |
| `alpha` + U+2028 + `beta` | 1 | 2 |

`count_file` closes its own file handle on every outcome. Missing/unreadable files raise an `OSError` subtype; invalid UTF-8 raises `UnicodeDecodeError`. Calls produce no stdout/stderr and never return partial counts. Invalid caller argument types are outside the guaranteed input domain.

## CLI contract

Invocation: `python -m textstats [--keep-bom] [--lines START:END] INPUT`. Exactly one input is required. `--keep-bom` selects `strip_bom=False`; otherwise removal is enabled. Input `-` selects stdin; `--` supports named files beginning with a dash. Standard `--help` writes help and exits 0. Omitting `--lines` preserves whole-input behavior.

Success writes exactly `lines=<N> words=<N>\n` to stdout and no stderr. BOM and range options compose in either order. Selection adds no metadata or extra output fields. `--json` is an unknown option and returns usage status 2 before acquiring input; a literal file named `--json` remains usable after `--`.

Success returns 0. Missing/unreadable inputs and invalid UTF-8 return 1, produce no success stdout, and write a useful nonempty stderr diagnostic identifying the input and cause, without a traceback. Usage errors (including missing/extra inputs and unknown options) return 2 with useful stderr and no success stdout or traceback. Diagnostic wording is flexible. Files are never modified.

### Range syntax and validation

One optional `--lines START:END` may appear in normal argparse option order; `--lines=START:END` is also supported. Endpoints consist of one or more ASCII decimal digits representing positive integers, with START <= END. Leading zeros have decimal meaning; there is no arbitrary upper endpoint limit. Signs, whitespace, Unicode digits, empty/open endpoints, extra colons, zero, reversed ranges and repeated `--lines` options are usage errors.

Malformed or missing range values and repetitions return status 2 with useful nonempty stderr, no success stdout and no traceback. Validate usage before acquiring input: an invalid range is a usage error even when the input does not exist. Help documents inclusive one-based endpoints and available-subset behavior.

### Selected counting

Read and strictly decode the complete source as UTF-8 before counting. Read/decode failures anywhere, including outside the requested range, return status 1 with no partial success output. Apply the configured BOM policy to the complete decoded input exactly once before identifying and numbering logical lines by the counting contract.

Number lines from 1. Select existing lines whose positions satisfy START <= position <= END, retaining their original contents and terminators. Count only the selected lines and their Unicode whitespace-separated words. `lines` is the number actually selected, including blank logical lines; it need not equal END minus START plus one when a request extends beyond EOF. Selection beyond EOF or from empty input succeeds with (0,0), status 0 and no stderr. A nonempty unterminated final segment is selectable; a final terminator creates no phantom line. Unicode separators other than CR/LF may divide words but never line positions.

Removing the only leading BOM can make input empty before numbering. An interior U+FEFF is never removed because selection exposes it at the beginning. `--keep-bom` affects the actual leading input BOM only; if line 1 is excluded that leading BOM contributes no selected word. Retaining it follows ordinary-character semantics. Selection preserves input and source resource ownership.

### Stdin compatibility

Stdin bytes are decoded strictly as UTF-8 independent of locale, read until EOF, and are not closed by TextStats. Empty stdin yields zero counts. Stdin decoding/read failures have the same CLI status/channel contract, identifying stdin. Named-file behavior remains available after stdin support.

Range selection is source-independent: it applies identically to the complete decoded input from a named file or stdin, with the same BOM, newline, EOF-subset, output and error semantics. Named-file range delivery is independent of planned stdin delivery; compatibility of the selection interface is required, while actual stdin acquisition and integration acceptance remain part of stdin delivery.

## Unsupported behavior

No public Python range parameter or export, multiple ranges, negative/from-end positions, alternate encodings or streaming guarantee is provided. The complete decoded input is required even for a range ending before EOF.

## Quality and acceptance

Runtime and test dependencies are standard library, Python >=3.11. Professional module and public API docstrings explain purpose, arguments, results, exceptions, and resource ownership where relevant. Meaningful unittest coverage checks independent expected counts, real named-file/public imports, module subprocesses, channels/statuses, malformed bytes, BOM modes, mixed terminators, and option composition. Test directories must be discoverable packages. No empty test collection establishes acceptance.

Whole-input acceptance requires successful named-file API and module CLI examples, the counting table boundaries and Unicode whitespace, failure and usage channels/statuses, an extracted source package launched through its module entry point.

Selected-counting acceptance uses these literal expected counts, with default BOM removal unless stated. Exercise named-file CLI exact plain output; pure counting checks establish the same boundaries.

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

Also accept `01:02` as decimal (1,2), a singleton range on an unterminated final line, all-lines ranges equivalent to no range, and LF/CR/CRLF blank-line boundaries. Reject `0:1`, `2:1`, `-1:2`, `1:`, `:2`, `1:2:3`, `1.0:2`, `+1:2`, whitespace and Unicode digits, missing values, and repeated options with status/channel assertions. Verify invalid-range precedence over nonexistent input and actual invalid UTF-8 after END. Preserve no-range core/API/CLI/failure/distribution acceptance and unchanged files/owned-handle cleanup.

Named-file range acceptance includes extracted-source invocations and documented selected examples with exact plain output, plus review of the source-independent selection interface for stdin compatibility. Future actual stdin acceptance exercises whole-input and selected empty/BOM/mixed-newline cases with exact plain output, locale-independent UTF-8, stream lifetime and read/decode failures (including after END). These stdin checks belong to stdin delivery and do not gate named-file range delivery.
