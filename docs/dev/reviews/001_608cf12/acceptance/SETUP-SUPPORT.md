# Harness setup support record

This is infrastructure verification, separate from consumer case execution. All 27 cases remain Pending.

Setup baseline: `b9a4549d8db2194917b5985d55d99a9a3ce16923`. Parent-provided plugin pin: `529e98d4d3cd7002e3a49e34394552a44bf0a8d0`. Support changed only independent harnesses, API utility and campaign metadata. No product or source-plugin changes were made.

`python -m unittest discover -s tests -v` passed 9 checker self-tests. Negative fixtures exercise one-parent and misordered/extra-parent merges, wrong branches, dirty worktrees, scope escapes, stale remote HEAD, duplicate executable IDs, ambiguous task tables, and wrong literal CLI output/exit status. API request tests use a synthetic token, reject repository/path escapes, and refuse redirects. No real token was read and no live API mutation was performed by this support task.

Limits: snapshots are point-in-time observations; task extraction supports current checkbox ID lists and optional Markdown tables; subprocess launch errors/timeouts need journal capture; CLI expectations and case assessments must be supplied independently. Self-tests establish checker behavior, not product acceptance. Commit and publication identity are reported to the campaign coordinator after push.

Correction after initial publication: the pinned task contract uses nested checkboxes and globally unique current IDs, including completed entries. The follow-up checker supports this contract, traverses local linked task children, excludes historical feature directories and rejects empty extraction. The added hierarchy test rejects a checked duplicate. No consumer assessment used the earlier table-only checker.
