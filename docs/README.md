# TextStats: SDD plugin test project

## Purpose of this repository

TextStats is the controlled development project used to test [Skill-SDD-Manager](https://github.com/pchemguy/Skill-SDD-Manager). The repository retains the application built during those tests, the development artifacts consumed and produced by agents, and the independent evidence used to assess the plugin’s workflows.

The subject of the evaluation is how agents follow the plugin through a software project: preparing governing documents, selecting bounded work, implementing and verifying it, maintaining task ownership, integrating branches, responding to amendments, and recovering interrupted operations. TextStats supplies concrete work and observable results for those exercises.

Its small text-counting problem was chosen so assessors could check behavior against literal expectations without external services or complex infrastructure. Working code and passing application tests provide evidence that selected development work was delivered; workflow assessment also checks document scope, Git ancestry/publication, hosted state and preservation of unfinished or unrelated work.

## Why the product documents read like a real project

[docs/dev/PROJECT.md](dev/PROJECT.md) is the product brief inside the test scenario. It describes TextStats in ordinary product terms because the plugin must work with normal software-development inputs. The specification, architecture, plan and tasks serve the same role: they govern the sample project while providing artifacts through which the plugin’s behavior can be assessed.

This document explains the evaluation context. The [root README](../README.md) supplies the sample application’s usage documentation, which was itself part of the implementation/documentation/verification exercises. Read [SPEC](dev/SPEC.md) when checking a scenario’s expected application behavior.

## How the sample capabilities exercise the plugin

| Scenario material | Workflow exercised |
| --- | --- |
| Named-file counting through an API and CLI | Preparation, decomposition, task derivation and incremental delivery of an early usable slice. Simple inputs support independent acceptance checks. |
| Input failures, BOM/newline boundaries and source deployment | Behavioral verification, failure/resource handling, documentation and milestone/phase exit checks. |
| Temporary JSON output | A bounded capability increment on the next phase while preserving completed baseline behavior. |
| Line-range counting | Separate feature preparation, selected-document incorporation, implementation, unique task-owner transfer and historical source archiving. |
| Removing JSON | A subtractive steering amendment: retire obsolete scope, reassess affected completed work and retain identity/history while preserving required behavior. |
| Stdin delivery after the feature and amendment | Continuation on the amended phase, compatibility with the incorporated feature, complete phase verification and explicit integration into main. |

Interrupted transfers, failing checks, conflicting merges, rejected pushes and controlled API failures exercise preservation and recovery around those workflows. Real hosted observations and injected local failures are identified separately in the case records.

## Development artifacts under docs/dev/

| Artifact | Role in testing the plugin |
| --- | --- |
| [PROJECT.md](dev/PROJECT.md) | Sample product objective and constraints used to orient the development workflow. |
| [SPEC.md](dev/SPEC.md) | Behavioral authority against which implementation and independent acceptance are assessed. |
| [ARCHITECTURE.md](dev/ARCHITECTURE.md) | Architectural decisions and boundaries carried into downstream artifacts. |
| [DECOMPOSITION.md](dev/DECOMPOSITION.md) | Logical responsibilities and interfaces used to derive implementation work. |
| [layout.md](dev/layout.md) | Path ownership and intended structure checked during scoped edits and verification. |
| [PLAN.md](dev/PLAN.md) | Incremental strategy, dependencies and exits used to assess delivery and integration decisions. |
| [TASKS.md](dev/TASKS.md) | Stable task identities, current executable ownership and completion/reassessment evidence. |
| [features/002_8a53078/](dev/features/002_8a53078/README.md) | Archived feature artifacts showing incorporation and source-retention outcomes. |
| [reviews/003_d0eeeff/](dev/reviews/003_d0eeeff/REVISION-REPORT.md) | JSON-removal amendment and its verification/integration record. |
| [reviews/001_608cf12/](dev/reviews/001_608cf12/README.md) | Independent composed-runtime campaign: case definitions, expectations, observations and assessments. |

Current governing documents describe the scenario’s accepted state. Archived snapshots preserve the state at an earlier test checkpoint; their task rows are historical evidence. Ownership checks exclude review/feature archives. Earlier proposals and outcomes should be interpreted through their recorded scope and date.

## Test material and evidence

The [textstats/](../textstats/) code is the implementation produced by the consumer agents. [Unit](../tests/unit/) and [integration](../tests/integration/) tests check that implementation. [tests/workflows/](../tests/workflows/README.md) contains independent workflow checkers and their sensitivity/regression tests. [tools/](../tools/) supports observation, evidence publication and controlled scenario setup. The tested plugin snapshot and exact source/file identity are retained under [vendor/](../vendor/PROVENANCE.json).

The main evaluation entry points are:

- [ACCEPTANCE-REPORT.md](dev/reviews/001_608cf12/ACCEPTANCE-REPORT.md): per-case outcomes and scope.
- [A-027 final assessment](dev/reviews/001_608cf12/runs/A-027/A-027-final.md): independent coverage conclusions and limits.
- [FINDINGS.md](dev/reviews/001_608cf12/FINDINGS.md): observed problems, assistance and corrections.
- [RESUME.md](dev/reviews/001_608cf12/RESUME.md): final disposition and historical interruption/recovery checkpoints.
- [MAIN-INTEGRATION.md](dev/reviews/001_608cf12/MAIN-INTEGRATION.md): publication of the completed evidence alongside the test application.

Inside the campaign, `acceptance/` contains case definitions and independent expected results; `runs/` retains consumer inputs, journals, logs, observations and recovery artifacts. Integration folders retain publication checks. The evidence branch is preserved after its merge into main. Future acceptance consumers follow [AGENTS.md](../AGENTS.md) isolation rules for assessor records and oracles; completed setup drivers are not continuation instructions.

## Scope of the conclusions

All 27 campaign cases passed in the recorded explicit skill-source loading mode. These results support the tested plugin workflows with their disclosed assistance, corrections and fixture limits. They do not establish installed-client discovery, routing or activation, which remain untested.

The observed runtime was Python 3.12.14; Python 3.11 execution was not performed. Retained journals/logs are available action evidence, not complete native transcripts. The final assessment distinguishes these limitations from the workflow outcomes actually observed.
