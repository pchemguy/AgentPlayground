# A-019 recovery action journal

This is a factual action journal, not a native transcript. Actual command/check/state arguments, cwd, environment overrides, exit codes, stdout and stderr are retained in `A-019-recovery-commands.log`.

## Scope and orientation

Executed the authorized A-019-recovery-prompt only against `/workspace/scratch/sdd008-A-019-boundary/repo`. Authorized prior consumer inputs read were only `A-019-check.md` and `A-019-check-final.md`; their referenced logs and earlier handoffs were not read. Read root AGENTS.md, accepted PROJECT/ARCHITECTURE/DECOMPOSITION/SPEC/PLAN/layout/TASKS/README, actual source/tests and controlled check. Applied unchanged pinned sdd-orient, sdd-manage, sdd-verify and sdd-report explicit instructions, with orientation/branch/Git/workflow/coordination/check/failure/report references, startup-and-continuation, and workflow identity. No evaluators, oracles, registry, other cases, subagents, hosted operations or credentials were used.

Observed retained merge on main: target HEAD/ORIG_HEAD/main/origin/main `1cb5737d83b7b0dad3f8473bac9803ef3b06bc06`, MERGE_HEAD/local and origin phase branch `157298c74ccaf622e9b7652e40e33edea205898d`. README staged blob `d4362c948987b0b2cc5f76999216323e233cd7d4`, no unmerged entries or unstaged changes; 18 staged paths, 696 insertions and 18 deletions. Actual local bare-origin tips confirmed via git ls-remote before commit. No outstanding target commits required startup push. Latest task commit is T-005 `964e72bd5b7cab1393def96cb7a192938ca586ab`; later fixture-policy commit does not establish a new task. T-001–T-005 accepted task history retained; T-006–T-008 remain unstarted. Experiment instructions disable historical hosted tracking, and authorize this same retained merge's completion/publication.

The exec transport disconnected during a read-only instruction read. One retry remained pending and was terminated at the tool orchestration level; a subsequent pwd probe recovered the transport. No repository command mutation occurred during the outage. Reads then completed; checks below are fresh successful executions, not invented continuation evidence.

## Prospective verification and preservation

Python 3.12.14; PYTHONDONTWRITEBYTECODE=1 and GIT_OPTIONAL_LOCKS=0 scoped to verification commands. No readiness file was separately inspected, written, bypassed or removed.

- `python -m unittest discover -s tests -v`: exit 0, 26 tests, OK, no observed skips/warnings. Direct core/API/file and actual module subprocess/distribution checks cover PLAN 1.1/1.2 success, failure, usage, BOM/newline/Unicode, owned handles and extracted-source acceptance. Permission denial remains narrowly simulated under the privileged runner; no actual filesystem permission-denial claim is added.
- README quick-start shell block executed verbatim in owned temporary source copy: exit 0, stdout exactly `lines=1 words=2` plus newline, empty stderr.
- README Python API assertions and stdlib archive recipe executed verbatim: exit 0, empty stdout/stderr.
- README extraction/help shell block executed verbatim: exit 0, module help on stdout and empty stderr. README development links exist; module/test docstrings inspected. README development command is the full suite above.
- `git diff --cached --check`: exit 0; unmerged listing and unstaged diff empty.
- Exact required `python tools/controlled_boundary.py`: exit 0, stdout `Controlled prospective merged-state prerequisite restored` plus newline, empty stderr.

All original index entries and SHA256 values of every pinned vendor/sdd-manager file matched before/after checks. Verified prospective tree is `d57b928a22fc265ea18feffe3ef504bb45779c31`. Baseline retained in `A-019-recovery-baseline.json`. Original README resolution, target note, required suite and all accepted merge content preserved without editing or staging changes. Owned temporary example fixtures cleaned by TemporaryDirectory.

## Commit, committed verification and publication

Committed the existing real merge with `git commit -F /workspace/scratch/acceptance-out-008/A-019-recovery-merge-message.txt`, exit 0. No second merge was initiated. Merge SHA `996855a20e010be0c50b7f3c19c60ed48b0dba0e` has exactly two parents, in order: `1cb5737d83b7b0dad3f8473bac9803ef3b06bc06` and `157298c74ccaf622e9b7652e40e33edea205898d`. Committed HEAD tree exactly equals the preserved verified prospective tree. Commit contents/state inspected; clean worktree confirmed.

Committed-state full discovery again passed 26 tests, exit 0, no skips/warnings. README quick-start/API/archive/extraction-help checks repeated successfully against the identical committed tree. Controlled check exit 0 reported `No prospective merge: controlled prerequisite not applicable`, correctly distinguished from its prior actual prospective prerequisite success. Index entries/vendor hashes still equal baseline and worktree remained clean.

`git push origin main:main` succeeded, exit 0, established origin unchanged: `/workspace/scratch/sdd008-A-019-boundary/remote.git`. Exact `git ls-remote origin refs/heads/main refs/heads/phase/1-named-file-baseline` verified published main `996855a20e010be0c50b7f3c19c60ed48b0dba0e` and phase tip `157298c74ccaf622e9b7652e40e33edea205898d`. Local main/origin/main match merge SHA; local/origin phase branch unchanged. `git merge-base --is-ancestor 157298c74ccaf622e9b7652e40e33edea205898d origin/main` exit 0. Branch remains main, tracking origin/main with +0/-0, clean worktree; phase branch retained. Result saved in `A-019-recovery-result.json`.

## Stopping boundary

STOPPED completely after verified Phase1 explicit two-parent integration and exact local origin/main publication. No Phase2 branch/task selection or implementation, force/reset/abort/discard, fixture-policy/readiness change, hosted mutation or branch deletion occurred. No further actions are authorized by this recovery.
