# T-001 reassessment completed and published

Completed **T-001 only** against the current accepted SPEC/TASKS. Added a committed public-API regression retaining the first result across a distinct-input second call with the opposite BOM policy; both policy orders assert literal counts for both results after the second call. The existing valid counting algorithm and public signatures are unchanged. The API docstring now states the verified independence guarantee.

Resolved the pending T-001 reassessment note with fresh evidence. Its original historical verification text and checked status are preserved. T-002 through T-008, their dependencies and all milestone/phase checkboxes remain unchanged. FEATURE-SPEC remains active; no optional archival was performed.

Verification:

- New focused regression: **1 test / 2 policy subcases passed** before any documentation edit; this characterizes existing behavior, with no genuine production RED or manufactured history claimed.
- `python -B -m unittest tests.test_counting tests.test_api -v`: **7 tests passed**.
- `python -B -m unittest discover -s tests -v`: **7 tests passed**, no warnings/skips.
- Isolated faulty shared-result callable: **2 intended assertion failures**, no setup errors; sensitivity evidence only, never a production change.
- Scoped/staged diff, whitespace, unchanged historical evidence/task boundaries and production AST excluding docstrings checked successfully. Final checkout clean.

Published commit: `332f2a49822cd82ae17b4a16b7a00bc4c86d14a7` on `phase/1-named-file-baseline`; exact local bare origin ref independently confirmed after push. Startup publication prerequisite had already confirmed `88dd40678e31c2b4fbce5ed7ca84519940ce9b9d`. Main remains `e750d1c6f07a9e6cda49a7cf0924d2c605c82c0d`.

Current T-001 acceptance is complete, verified, committed and pushed on its phase branch. Phase 1 is incomplete; no phase merge, main integration, T-002 execution, hosted API/token operation or new branch occurred. Stopped at the requested one-task checkpoint. Later tasks require separate authorization.
