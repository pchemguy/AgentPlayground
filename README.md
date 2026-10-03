# AgentPlayground — TextStats

TextStats counts logical lines and Unicode whitespace-separated words in UTF-8 text. Use Python 3.11 or newer from this source checkout; no external dependencies are needed.

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

The API preserves `OSError` (including missing/unreadable input) and `UnicodeDecodeError` for invalid UTF-8, without printing or returning partial counts. The CLI returns status 1 with a useful input/cause diagnostic on stderr and no stdout or traceback. Invalid usage returns status 2; `--help` returns status 0. Use `--` before dash-prefixed filenames.

JSON and stdin are planned for phase 2. Input `-` currently names a file; `--json` is not supported yet.

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

On Python 3.11, use a current patch release supporting the `data` extraction filter. Alternatively, extract this locally created archive with your archive application. The named-file quick start and Python examples work from the extracted directory. UTF-8 decoding is strict; no locale-specific codec is used. Word splitting follows Unicode whitespace, while only CR, LF and CRLF terminate logical lines. Empty text after BOM handling yields zero lines and words; other Unicode line separators affect words without creating lines. File reads and CLI invocations leave input bytes unchanged.

## Development

```sh
python -m unittest discover -s tests -v
```

Core/API/file tests live in `tests/unit/`; module subprocess and distribution tests live in `tests/integration/`. See [delivery plan](docs/dev/PLAN.md) and [tasks](docs/dev/TASKS.md) for the intended increments and current evidence.
