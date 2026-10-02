# TextStats specification

This specifies the complete intended system from [PROJECT](PROJECT.md), with responsibilities in [DECOMPOSITION](DECOMPOSITION.md). [PLAN](PLAN.md) schedules realization without removing later requirements.

## Counting contract

`TextStats` is an immutable public value with integer fields `lines` and `words`, both nonnegative. `count_text(text: str, *, strip_bom: bool = True) -> TextStats` and `count_file(path: str | os.PathLike[str], *, strip_bom: bool = True) -> TextStats` are importable directly from `textstats`.

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

Invocation: `python -m textstats [--keep-bom] [--json] INPUT`. Exactly one input is required. `--keep-bom` selects `strip_bom=False`; otherwise removal is enabled. `--json` becomes available in milestone 2.1. In milestone 2.2, input `-` selects stdin instead of a file; earlier named-file slices treat it as a filename. `--` supports named files beginning with a dash. Standard `--help` writes help and exits 0.

Default success writes exactly `lines=<N> words=<N>\n` to stdout and no stderr. JSON success writes one valid JSON object with exactly the keys `lines` and `words`, each holding an integer count, followed by a newline; insignificant JSON whitespace/key order is not contractual. JSON and BOM options compose.

Success returns 0. Missing/unreadable inputs and invalid UTF-8 return 1, produce no success stdout, and write a useful nonempty stderr diagnostic identifying the input and cause, without a traceback. Usage errors (including missing/extra inputs and unknown options) return 2 with useful stderr and no success stdout. Diagnostic wording is flexible. Files are never modified.

Stdin bytes are decoded strictly as UTF-8 independent of locale, read until EOF, and are not closed by TextStats. Empty stdin yields zero counts. Stdin decoding/read failures have the same CLI status/channel contract, identifying stdin. Named-file behavior remains available after stdin support.

## Quality and acceptance

Runtime and test dependencies are standard library, Python >=3.11. Professional module and public API docstrings explain purpose, arguments, results, exceptions, and resource ownership where relevant. Meaningful unittest coverage checks independent expected counts, real named-file/public imports, module subprocesses, channels/statuses, malformed bytes, BOM modes, mixed terminators, and option composition. Test directories must be discoverable packages.

Acceptance requires successful named-file API and module CLI examples, the table boundaries and Unicode whitespace, failure and usage channels/statuses, JSON parsed by the stdlib decoder, UTF-8 stdin despite locale settings, and an extracted source package launched through its module entry point. No empty test collection establishes acceptance. No line-selection behavior is included.
