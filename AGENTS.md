# AgentPlayground instructions

Use the requested SDD skill entries under vendor/sdd-manager/skills as explicit instructions. All tracked project changes require scoped commits and pushes. Use main as the established integration branch and origin as the established remote. Preserve unrelated work and use explicit two-parent boundary merges.

Use Python 3.11+ and standard-library unittest. Run python -m unittest discover -s tests -v for the declared full suite once tests exist; empty collection does not verify acceptance. Each test directory needs discoverable package structure. Professional module docstrings and blank lines around Markdown headings are required.

Use existing Git authentication first. If access fails, sdd-manage may recover from the ignored root gh.tkn through a protected mechanism. Never output or track tokens. Hosted task tracking is authorized when requested by the case.

Maintain brief action journals identifying significant commands/results, changes, commits and actual scope decisions in the requested run output; do not invent native transcripts. During consumer acceptance runs, do not inspect retained evaluator records or oracle files under docs/dev/reviews/. Assessors and explicitly authorized repository maintenance may inspect them. Stop at the user-requested boundary.
