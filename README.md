# TextStats

TextStats counts logical lines and Unicode whitespace-separated words in UTF-8 text. Use Python 3.11 or newer from this source checkout; no external dependencies are needed.

See the [project and repository guide](docs/README.md) for the project’s purpose, development documents and workflow acceptance records.

## Named-file quick start

From the checkout root, create a small UTF-8 file and run the module:

```sh
python -c "from pathlib import Path; Path('sample.txt').write_text('alpha beta\n', encoding='utf-8')"
python -m textstats sample.txt
```

Output:

```text
lines=1 words=2
```

The command succeeds with status 0 and empty stderr. `--keep-bom` retains a leading UTF-8 BOM; otherwise exactly one leading BOM is removed. CR, LF and CRLF terminate lines, and a final terminator creates no extra line.

## Python calls

```python
from textstats import TextStats, count_file, count_text

assert count_text("alpha beta\n") == TextStats(lines=1, words=2)
assert count_file("sample.txt") == TextStats(lines=1, words=2)
```

Results are immutable. The file API reads strict UTF-8, leaves files unchanged and closes its own handle.

The API preserves `OSError` (including missing/unreadable input) and `UnicodeDecodeError` for invalid UTF-8, without printing or returning partial counts. The CLI returns status 1 with a useful input/cause diagnostic on stderr and no stdout or traceback. Every successful CLI invocation writes exactly `lines=<N> words=<N>` followed by one newline. `--json` is an unknown option returning status 2; a file named `--json` remains usable after `--`. Invalid usage returns status 2; `--help` returns status 0. Use `--` before dash-prefixed filenames.

## UTF-8 stdin

Input `-` reads binary stdin through EOF and decodes the complete input strictly
as UTF-8, independent of the locale or Python's stdin text encoding. TextStats
leaves the caller's stdin open. Use `./-` for a literal file named `-`.

```sh
printf 'alpha beta\nbeta\nlast two' | python -m textstats -
printf 'alpha beta\nbeta\nlast two' | python -m textstats --lines 2:3 -
printf '' | python -m textstats -
python -c "import sys; sys.stdout.buffer.write('\ufeff a\nb'.encode('utf-8'))" | python -m textstats --keep-bom -
```

Outputs respectively: `lines=3 words=5`, `lines=2 words=3`,
`lines=0 words=0`, and `lines=2 words=3`, each followed by a newline,
status 0 and empty stderr. `--keep-bom` and `--lines` compose for both sources.
Read or decode failures identify stdin on stderr, return status 1, and produce
no success output. Invalid UTF-8 anywhere, including outside selected lines,
fails before counting. Complete input is held in memory; no streaming guarantee
is provided.

## Selected named-file lines

Use `--lines START:END` to count existing one-based inclusive logical lines.
Endpoints are positive ASCII decimal integers; leading zeros are accepted.
Requests extending beyond EOF count only available lines; selection beyond
EOF returns zero counts. Blank lines count as lines, and only CR, LF and CRLF
terminate logical lines. Unicode separators may divide words without creating
line positions. Repeated, reversed, zero, signed or open ranges are usage errors.

```sh
python -c "from pathlib import Path; Path('ranges.txt').write_text('alpha beta\nbeta\nlast two', encoding='utf-8')"
python -m textstats --lines 1:1 ranges.txt
python -m textstats --lines 2:3 ranges.txt
python -m textstats --lines 2:99 ranges.txt
python -m textstats --lines 4:99 ranges.txt
```

Outputs respectively: `lines=1 words=2`, `lines=2 words=3`,
`lines=2 words=3`, and `lines=0 words=0`, each followed by a newline.
`--lines=START:END` also works and composes with `--keep-bom`.
The complete file is strictly decoded even when invalid bytes lie outside the
selection. The original input BOM policy runs once before numbering lines;
a BOM originally on a later line remains ordinary content when selected.
Public Python calls continue to count the whole input with unchanged signatures.
The same selection semantics apply to stdin selected by `-`.

## Source distribution

Create a self-contained source archive from the checkout root with the standard library:

```python
from pathlib import Path
import tarfile

with tarfile.open("TextStats.tar.gz", "w:gz") as archive:
    for path in sorted(Path("textstats").glob("*.py")):
        archive.add(path, arcname=str(path))
    archive.add("README.md", arcname="README.md")
```

The archive contains the Python package and this README. It excludes tests, development records, vendored infrastructure, tools, bytecode, Git internals and credentials. This is source deployment, without a wheel or external build backend. Extract the archive into a new directory and run Python from that directory:

```sh
python -c "import tarfile; tarfile.open('TextStats.tar.gz').extractall('TextStats', filter='data')"
cd TextStats
python -m textstats --help
```

On Python 3.11, use a current patch release supporting the `data` extraction filter. Alternatively, extract this locally created archive with your archive application. The named-file, stdin and Python examples work from the extracted directory. UTF-8 decoding is strict; no locale-specific codec is used. Word splitting follows Unicode whitespace, while only CR, LF and CRLF terminate logical lines. Empty text after BOM handling yields zero lines and words; other Unicode line separators affect words without creating lines. File reads and CLI invocations leave input bytes unchanged.

## Development

```sh
python -m unittest discover -s tests -v
```

Core/API/file tests live in `tests/unit/`; module subprocess and distribution tests live in `tests/integration/`. See [delivery plan](docs/dev/PLAN.md) and [tasks](docs/dev/TASKS.md) for the intended increments and current evidence.


## Workflow acceptance records

The completed [acceptance campaign](docs/dev/reviews/001_608cf12/README.md) and [independent final assessment](docs/dev/reviews/001_608cf12/runs/A-027/A-027-final.md) record 27 passing cases in explicit skill-source mode. Installed-client discovery, routing and activation remain untested. Historical case snapshots and oracles are assessment records; current product contracts and task ownership remain in docs/dev/. The original evidence branch is retained.

Independent harness checks live in tests/workflows/ and run with the full development suite above. The source-distribution recipe still includes only the TextStats package and this README.
