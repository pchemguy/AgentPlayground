# Independent workflow acceptance tools

Run from the repository root with Python 3.11+:

```sh
python -m unittest discover -s tests -v
python -m tests.workflows.git_snapshot capture /path/to/consumer runs/A-001-git.json
python -m tests.workflows.git_snapshot check runs/A-001-git.json --branch phase/1 --first-parent BASE_OID --second-parent TOPIC_OID --allow src --allow tests --require-remote
python -m tests.workflows.task_ownership /path/to/consumer/docs > runs/A-001-owners.json
python -m tests.workflows.cli_expectations acceptance/oracle/A-001-cli.json runs/A-001-cli-actual.json --cwd /path/to/consumer
```

Replace paths and literal contract values with assessor-authored values recorded before execution. The capture command performs only Git reads, including `ls-remote`; it does not fetch, checkout, merge, or expose remote URLs. Parent order is significant. The scope checker examines all paths changed relative to the first parent, including deletions; every path must equal an allowed path or descend from an allowed directory. A clean worktree and exactly two expected parents are required. `--require-remote` additionally checks the captured remote branch HEAD. A snapshot records a point in time, not continuous enforcement.

The task checker reads `TASKS.md` and active `FEATURE-TASKS.md` beneath the supplied root. Directory names containing `archive` are excluded. Use Markdown tables with `ID` (or `Task ID`) and `Status` columns. Each nonterminal row is an executable owner; Done, Complete, Completed, Cancelled, Canceled, Superseded and Archived rows are excluded, case-insensitively. An identical executable ID in any two rows fails, including duplicates within one document. Historical references outside task tables are ignored. Other task syntaxes require an explicit assessor-reviewed adapter; do not interpret an empty result as proof that unsupported syntax has no duplicates.

CLI expectation files contain literal `argv`, `returncode`, `stdout`, `stderr`, optional `stdin`, and optional `timeout_seconds` (default 30). Example:

```json
{"argv":["python","-m","textstats","--help"],"returncode":0,"stdout":"EXACT EXPECTED TEXT\n","stderr":""}
```

This example is a template, not an accepted product expectation. Expectations are authored from the external contract, never imported or derived from product code. The runner executes without a shell, writes actual output and mismatch keys, and exits nonzero on a mismatch. A launch failure or timeout fails without a completed result record; preserve the invocation/error in the case journal. These harnesses test observable behavior and Git/task evidence, not source text policies.

# Protected repository API utility

```sh
python tools/github_api.py GET /repos/pchemguy/AgentPlayground/milestones --token-file /protected/path/gh.tkn
python tools/github_api.py POST /repos/pchemguy/AgentPlayground/milestones --token-file /protected/path/gh.tkn --body-file request.json
python tools/github_api.py PATCH /repos/pchemguy/AgentPlayground/milestones/NUMBER --token-file /protected/path/gh.tkn --body-file - < request.json
```

Only explicitly authorized GET, POST and PATCH repository operations are supported. The caller controls pagination through endpoint query parameters. Tokens are read from a file, never supplied as literal arguments or printed. Responses use `{ "status": HTTP_STATUS, "body": JSON_OR_TEXT }`; HTTP failures return nonzero and local failures return a generic sanitized message. Redirects are refused so bearer credentials cannot follow another destination. Test coverage uses synthetic credentials and performs no live API writes. Response artifacts may contain private repository data and belong in assessor evidence.
