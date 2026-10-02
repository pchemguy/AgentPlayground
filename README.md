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

This milestone delivers named-file success paths. CLI failure polish and source-distribution verification remain in milestone 1.2; JSON and stdin are planned for phase 2. Input `-` currently names a file.

## Development

```sh
python -m unittest discover -s tests -v
```

Core/API/file tests live in `tests/unit/`; module subprocess and distribution tests live in `tests/integration/`. See [delivery plan](docs/dev/PLAN.md) and [tasks](docs/dev/TASKS.md) for the intended increments and current evidence.
