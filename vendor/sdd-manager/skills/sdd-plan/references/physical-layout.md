# Physical layout

`docs/dev/layout.md` maps the accepted logical design to physical ownership in the repository. It makes source, test, documentation, packaging, generated-artifact, and other relevant locations discoverable before TASKS selects concrete edit scopes. Preserve project conventions and actual paths where appropriate; do not invent a new tree merely for symmetry.

## Establish ownership

1. Inspect the actual tree and relevant project instructions. For proposed areas, distinguish intended paths from existing ones without claiming absent files exist.
2. Assign a home to each significant architectural block and decomposed component. Show where public interfaces, implementations, tests, fixtures, packaging, and developer and user documentation belong as applicable. Identify shared infrastructure and its owner. Map logical units to directories or stable files only to the level that prevents ambiguous placement.
3. Define placement and dependency rules where multiple units could otherwise claim a path. Explain exceptions needed to keep the layout coherent. Avoid duplicating behavior from SPEC or interfaces from DECOMPOSITION.
4. Check navigation in both directions: a component should lead to its source and checks, and a directory should have an intelligible owner. Check that expected task-sized changes can stay within one module or a few collaborating modules where feasible, while allowing genuine integration work.
5. Record any unresolved placement choice that would block TASKS. Do not enumerate speculative files or bind every future task to a path. TASKS can identify expected touched files and propose a focused layout update when implementation exposes a legitimate new home.

Keep `layout.md` a concise authoritative entry point. If physical organization needs substantial independent detail, use focused children under `docs/dev/layout/` with explicit scopes and links from the root. The root retains repository-wide conventions and the ownership map; children refine distinct areas without repeating it. Do not use layout as a phase plan, task list, or completion tracker.

For an existing project, a proposed change may alter only a few ownership rules. Update the affected main layout nodes to describe the intended final physical organization when the decision is accepted; an active feature plan can describe the transition work. Preserve accurate unaffected areas. A path's presence does not prove a component is complete, and a proposed path is not an implementation claim.
