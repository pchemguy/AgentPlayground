# T-001 acceptance reassessment action journal

Request A-022-reassess-prompt.txt read. Selected T-001 only under accepted SPEC/TASKS; preserve valid implementation and historical evidence; no T-002+, phase integration, hosted APIs/tokens or new agents.

Orientation: eligible clean phase/1-named-file-baseline at published 88dd40678e31c2b4fbce5ed7ca84519940ce9b9d; historical task commit 57234b333e533d6bd606d3c5dda7275cf74ddacf, pending completion reassessment note observed. Root AGENTS and pinned manage/implement/orient/TDD/docs/verify/report entries and references read; accepted SPEC/FEATURE-SPEC and actual core/facade/tests inspected. First execution action: git push origin HEAD:refs/heads/phase/1-named-file-baseline returned Everything up-to-date (exit 0); git ls-remote origin refs/heads/phase/1-named-file-baseline confirmed exact HEAD. Remote publication prerequisite met before tests/edits.

No production defect observed: core has local counts and constructs a fresh frozen result. Add characterization coverage of existing behavior, not manufactured RED; no algorithm/signature changes intended. New test retains first result, calls distinct input/opposite policy, checks fixed literal counts for both after second call; both policy directions ensure input/BOM state cannot leak.

Characterization command: `python -B -m unittest tests.test_api.PublicApiTests.test_retained_results_are_independent_across_bom_policies -v`; exit 0, one test/two subcases passed against unchanged production. No behavioral RED occurred.

Controlled sensitivity command: isolated process patches only the package callable with a faulty shared mutable return object; executes the new test, expects two assertion failures and zero setup errors, restores patch on exit. Driver exit 0; observed output:

```text
test_retained_results_are_independent_across_bom_policies (tests.test_api.PublicApiTests.test_retained_results_are_independent_across_bom_policies)
Later calls cannot alter prior counts or inherit their BOM policy. ... 
  test_retained_results_are_independent_across_bom_policies (tests.test_api.PublicApiTests.test_retained_results_are_independent_across_bom_policies) (strip_first=True)
Later calls cannot alter prior counts or inherit their BOM policy. ... FAIL
  test_retained_results_are_independent_across_bom_policies (tests.test_api.PublicApiTests.test_retained_results_are_independent_across_bom_policies) (strip_first=False)
Later calls cannot alter prior counts or inherit their BOM policy. ... FAIL

======================================================================
FAIL: test_retained_results_are_independent_across_bom_policies (tests.test_api.PublicApiTests.test_retained_results_are_independent_across_bom_policies) (strip_first=True)
Later calls cannot alter prior counts or inherit their BOM policy.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/sdd008-A-022/repo/tests/test_api.py", line 36, in test_retained_results_are_independent_across_bom_policies
    self.assertEqual((first.lines, first.words), first_counts)
AssertionError: Tuples differ: (2, 3) != (0, 0)

First differing element 0:
2
0

- (2, 3)
+ (0, 0)

======================================================================
FAIL: test_retained_results_are_independent_across_bom_policies (tests.test_api.PublicApiTests.test_retained_results_are_independent_across_bom_policies) (strip_first=False)
Later calls cannot alter prior counts or inherit their BOM policy.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/sdd008-A-022/repo/tests/test_api.py", line 36, in test_retained_results_are_independent_across_bom_policies
    self.assertEqual((first.lines, first.words), first_counts)
AssertionError: Tuples differ: (2, 2) != (1, 1)

First differing element 0:
2
1

- (2, 2)
+ (1, 1)

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=2)
```

This is sensitivity evidence, not an actual production RED or a reconstructed historical TDD cycle. Existing implementation remains intact.

Docs reviewed: existing core/facade/test modules professional Google-style/module docstrings; add call independence to count_text Returns only. No runtime logic/signature changes. Acceptance campaign: `python -B -m unittest tests.test_counting tests.test_api -v` and `python -B -m unittest discover -s tests -v` each exit 0, all seven tests pass; no warnings/skips. Runtime 3.12.14. New literal retained-result test covers both opposite-policy directions; prior pure counting/BOM/newline/immutability/public import coverage passes.

TASKS resolved pending note with current evidence, kept checked T-001 and exact prior Verified T-001 line, preserved T-002 onward byte-for-byte and all task/parent checkboxes. No parent completion. Structural checks: production AST after stripping docstrings identical, diff restricted to task evidence/test/API docstring, all assertions passed. `git diff --check` exit 0.

Command: `git branch --show-current`; exit 0.

```text
phase/1-named-file-baseline
```

Command: `git diff --cached --name-only`; exit 0.

```text
```

Command: `git add -- tests/test_api.py textstats/counting.py docs/dev/TASKS.md`; exit 0.

```text
```

Command: `git diff --cached --check`; exit 0.

```text
```

Command: `git diff --cached --name-only`; exit 0.

```text
docs/dev/TASKS.md
tests/test_api.py
textstats/counting.py
```

Command: `git commit -m 'Verify retained call independence and reassess T-001' -m 'Add a public-API regression retaining first results across distinct-input calls with opposite BOM policies in both directions; fixed literal counts are checked after the later call. Preserve valid counting implementation and original task evidence, clarify its API docstring, and resolve current acceptance reassessment. Focused counting/API tests and full discovery pass all 7 tests; a controlled shared-result fixture fails both cases as intended. New coverage is characterization of existing behavior, not a claimed production RED. Pause after T-001 on the incomplete phase branch.'`; exit 0.

```text
[phase/1-named-file-baseline 332f2a4] Verify retained call independence and reassess T-001
 3 files changed, 21 insertions(+), 2 deletions(-)
```

Command: `git rev-parse HEAD`; exit 0.

```text
332f2a49822cd82ae17b4a16b7a00bc4c86d14a7
```

Command: `git show --stat --oneline HEAD`; exit 0.

```text
332f2a4 Verify retained call independence and reassess T-001
 docs/dev/TASKS.md     |  2 +-
 tests/test_api.py     | 17 +++++++++++++++++
 textstats/counting.py |  4 +++-
 3 files changed, 21 insertions(+), 2 deletions(-)
```

Command: `git status --porcelain=v1 --untracked-files=all`; exit 0.

```text
```

Command: `git push origin HEAD:refs/heads/phase/1-named-file-baseline`; exit 0.

```text
To /workspace/scratch/sdd008-A-022/remote.git
   88dd406..332f2a4  HEAD -> phase/1-named-file-baseline
```

Command: `git ls-remote origin refs/heads/phase/1-named-file-baseline refs/heads/main`; exit 0.

```text
e750d1c6f07a9e6cda49a7cf0924d2c605c82c0d	refs/heads/main
332f2a49822cd82ae17b4a16b7a00bc4c86d14a7	refs/heads/phase/1-named-file-baseline
```

Publication exact ref confirmed; complete final handoff saved A-022-reassess-final.md. Stop after T-001 only; no phase integration/next task.
