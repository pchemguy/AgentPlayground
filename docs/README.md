# TextStats project and repository guide

## What TextStats is

TextStats is a small Python utility for counting logical lines and Unicode whitespace-separated words in UTF-8 text. It offers an importable Python API and a command-line interface through `python -m textstats`. The CLI accepts a named file or stdin, supports optional inclusive line selection and leading BOM handling, and emits predictable plain text counts. The public API counts whole inputs.

The project uses the Python standard library and unittest, with Python 3.11 or newer as its declared requirement. The [user README](../README.md) provides runnable examples, API usage, options, failure behavior and source-distribution instructions. Exact counting and input contracts are defined in [SPEC](dev/SPEC.md).

## Why this project exists

TextStats is the deliberately small sample application built in AgentPlayground to evaluate [Skill-SDD-Manager](https://github.com/pchemguy/Skill-SDD-Manager). Its limited functionality makes outcomes independently checkable while providing real development work for specification-driven agent workflows.

The campaign exercised project preparation, incremental implementation, verification, hosted task tracking, explicit Git integration, feature incorporation and archiving, steering amendments, and interrupted or rejected-operation recovery. Agents implemented the application through the pinned skill instructions; assessors checked actual behavior, task ownership, Git history and publication evidence.

The delivery history includes a named-file baseline, a temporary JSON output increment, a line-range feature, an amendment removing JSON, and final stdin delivery. The current application provides plain output, named-file/stdin input and optional ranges. Earlier JSON examples in archived case evidence describe their historical checkpoints.

The application and its development evidence are both retained in this repository. The completed evidence branch was explicitly merged into main; the original branch and lifecycle history remain available.

## Repository contents

| Location | Purpose |
| --- | --- |
| [README.md](../README.md) | User entry point: running TextStats, public API, options and deployment. |
| [textstats/](../textstats/) | Application code: counting core, UTF-8 file adapter, public exports and CLI. |
| [tests/unit/](../tests/unit/) | Product checks for counting, file behavior and public API. |
| [tests/integration/](../tests/integration/) | CLI subprocess and extracted-source distribution checks. |
| [tests/workflows/](../tests/workflows/README.md) | Independent workflow harnesses and their regression checks. |
| [tools/](../tools/) | Campaign observation, evidence publication and controlled scenario support. Setup tools belong to their recorded scenarios; existing completed fixtures should be preserved. |
| [vendor/](../vendor/) | Exact portable SDD-manager snapshot and [provenance](../vendor/PROVENANCE.json), including source identity and file hashes. |
| [docs/dev/](dev/) | Current product requirements/design/delivery documents and retained development history. |

## Reading docs/dev/

These documents have distinct responsibilities. Start with the project brief, then follow the specification, design and delivery links according to your task.

| Document | What it owns |
| --- | --- |
| [PROJECT.md](dev/PROJECT.md) | Product purpose, scope, constraints and terminology. |
| [SPEC.md](dev/SPEC.md) | Normative behavior: counting, inputs, output, API and failure contracts. |
| [ARCHITECTURE.md](dev/ARCHITECTURE.md) | Intended components, dependency direction and design invariants. |
| [DECOMPOSITION.md](dev/DECOMPOSITION.md) | Logical responsibilities, collaborating interfaces and verification seams. |
| [layout.md](dev/layout.md) | Intended source/test/document paths and their owners. |
| [PLAN.md](dev/PLAN.md) | Delivery phases, milestones, prerequisites and exit criteria. |
| [TASKS.md](dev/TASKS.md) | Current executable task ownership and recorded completion evidence, with stable project-wide IDs. |

Design and strategy documents describe their intended system; current task evidence and verification records establish delivery. Historical paragraphs retain the state at which they were written. Use the current specification and task dispositions when interpreting earlier checkpoints. Hosted issue metadata supplements the local task evidence.

### Feature and review history

[features/002_8a53078/](dev/features/002_8a53078/README.md) preserves the completed line-range feature’s original delta specification, decomposition, plan and task snapshots. Its archived task rows are historical; current ownership is in the main TASKS document.

[reviews/003_d0eeeff/](dev/reviews/003_d0eeeff/REVISION-REPORT.md) records the subtractive JSON-removal amendment and its verification/integration.

[reviews/001_608cf12/](dev/reviews/001_608cf12/README.md) contains the composed runtime acceptance campaign. Useful entry points are:

- [ACCEPTANCE-REPORT.md](dev/reviews/001_608cf12/ACCEPTANCE-REPORT.md): case results and scope.
- [A-027 final assessment](dev/reviews/001_608cf12/runs/A-027/A-027-final.md): independent campaign conclusions and limitations.
- [FINDINGS.md](dev/reviews/001_608cf12/FINDINGS.md): observed problems, assistance and corrections.
- [MAIN-INTEGRATION.md](dev/reviews/001_608cf12/MAIN-INTEGRATION.md): integration of the completed evidence with the product.
- [RESUME.md](dev/reviews/001_608cf12/RESUME.md): current stop disposition followed by historical recovery checkpoints.

Within that campaign, `acceptance/` holds case definitions and independent expected results; `runs/` holds retained consumer inputs, journals, observations, logs and recovery artifacts; integration folders hold source/repository publication evidence. Case snapshots preserve earlier versions of product documents and tasks. Workflow ownership checks exclude these review archives. Future acceptance consumers should follow the isolation instructions in [AGENTS.md](../AGENTS.md) when handling assessor records and oracles.

## What the acceptance evidence establishes

All 27 campaign cases passed within the recorded explicit skill-source execution mode. The records distinguish real agent actions and hosted effects from controlled local failure fixtures, and disclose corrections and review assistance. Available journals and logs are retained as such, without claiming complete native transcripts.

The observed runtime was Python 3.12.14; Python 3.11 execution was not performed. Installed-client skill discovery, routing and activation remain untested. The final assessment records these limits alongside the supported workflow outcomes.
