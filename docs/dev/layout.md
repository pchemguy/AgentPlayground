# TextStats physical layout

This maps [DECOMPOSITION](DECOMPOSITION.md) to intended paths. Product paths below are proposed; this preparation creates only governing documents.

| Path | Owner and purpose | Checks |
| --- | --- | --- |
| `textstats/counting.py` | Pure counting core and immutable result | `tests/test_counting.py` |
| `textstats/files.py` | UTF-8 file adapter and owned handle lifecycle | `tests/test_files.py` |
| `textstats/__init__.py` | Public exports | `tests/test_api.py` |
| `textstats/cli.py` | Arguments, stdin selection, output and errors | `tests/test_cli.py` |
| `textstats/__main__.py` | Python module entry point | CLI subprocess checks |
| `tests/__init__.py` | Discoverable unittest package | Full discovery |
| `tests/test_distribution.py` | Extracted-source import/module checks using stdlib temporary directories and archive facilities | Distribution acceptance |
| `README.md` | User installation from source, examples, API/options/statuses | Documented examples checked against CLI/API |
| `docs/dev/*.md` | Governing brief, design, specification, strategy, tasks, layout | Document consistency/navigation |

Root package placement supports direct `python -m textstats` and stdlib-only source deployment without an external build backend. Temporary UTF-8 fixtures belong in test-created temporary directories, not repository output files. Future nested test directories require `__init__.py`. Archives and temporary extraction environments are verification outputs, not tracked product files; packaging includes the package and README while excluding vendor/tooling, Git internals and credentials.

The CLI depends on core/file owners; they never import CLI. Public docstrings live with their owners, the facade documents its exports, and user instructions live in README. Preserve `vendor/sdd-manager`, existing tooling, repository instructions and retained development records as infrastructure. No location decision blocks task derivation.
