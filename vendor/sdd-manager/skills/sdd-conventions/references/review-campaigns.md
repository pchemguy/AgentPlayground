# Review and revision campaign records

Apply this convention when naming, organizing, or referencing review and revision artifacts. **sdd-manage** owns the workflow; **sdd-report** owns artifact formats. Respect an established project convention when it specifies equivalent organization.

## Campaign identity and storage

Use `docs/dev/reviews/<sequence>_<baseline-sha>/` for the entire review/remediation lifecycle. For example, `003_39374c8` identifies the third repository campaign and its starting Git baseline.

- **Sequence:** Allocate the next unused repository-wide positive campaign number, padded to at least three digits. Use the shared [workflow identity](workflow-identity.md) allocation across reviews and features. Inspect both collections and relevant remote state; resolve concurrent collisions before publication. Do not renumber established campaigns.
- **Baseline:** Use the campaign's starting commit, with at least seven hexadecimal characters and enough characters to resolve it uniquely. Record the full SHA inside each artifact. Keep the directory name stable as review/report/revision commits advance HEAD.
- **Start:** Create the directory when writing the first artifact, not only after completion. A focused review can begin directly from a prompt; missing optional stages need no placeholder files.
- **Files:** Use `REVIEW-PLAN.md`, `REVIEW-REPORT.md`, `REVISION-PLAN.md`, and `REVISION-REPORT.md`. Keep one current artifact per stage; Git retains its edit history. Do not repeat sequence or commit suffixes in filenames.
- **Independent reviews:** Distinguish the campaign starting baseline from the exact source reviewed by each reviewer. When importing a report with no recorded source commit, say **reviewed baseline unknown**; its addition commit does not establish what was reviewed. Additional independently authored reports may use named subdirectories such as `independent/REVIEW-REPORT.md`; retain attribution and avoid overwriting another report.

Steering uses the same directory/branch association but may retain only a concise revision report; do not invent absent review/plan stages. Full campaigns and lightweight amendments share stable identity, not mandatory artifact counts.

## Stable references

Use local finding IDs such as `R-001` and external references such as `003_39374c8/R-001`. Allocate IDs once, never reuse them, and retain IDs when a finding is deferred, superseded, or resolved. Criterion, unit, and scenario IDs may similarly identify coverage and evidence within the campaign.

For existing records, preserve their established IDs rather than renumbering evidence. Qualify a legacy ID with its campaign when necessary. Keep each finding's canonical record in the review report; link revision actions and verification back to it rather than creating conflicting copies.

## Authority and retention

Campaign records hold scope, analysis, findings, accepted repair plans, and observed evidence. They remain after accepted changes are incorporated into PROJECT, design, SPEC, PLAN, layout, or task lists. Those governing documents describe the accepted resulting project; they do not become chronological review logs.

A review finding is not an accepted requirement or permission to mutate. Record acceptance, deferral, and scope explicitly. Keep the reviewed baseline evidence separate from current source and revision results. A reviewed unit means coverage was assessed, not that every finding is corrected. A planned check is not an observed result, and a revised finding becomes verified only after its stated recheck supports that disposition.
