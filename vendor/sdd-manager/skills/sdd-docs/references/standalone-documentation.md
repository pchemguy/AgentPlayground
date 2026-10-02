# README and standalone documentation

Identify the intended reader and selected documentation targets. Follow the project's layout and documentation conventions. Maintain existing focused guides instead of duplicating their content in README or creating guides without a demonstrated need.

## Align content

| Area | Review |
| --- | --- |
| README | Project purpose, supported capabilities, prerequisites, installation, quick start, examples, limitations, and links to deeper documentation. |
| Usage and configuration | Actual API or CLI behavior, option names, defaults, units, required inputs, and relevant examples. |
| Development guidance | Declared setup, build, test, documentation, and packaging commands; contribution guidance when present. |
| Troubleshooting | Supported diagnosis and corrective steps for documented failure cases. |
| Migration guidance | Verified compatibility changes, affected users, transition steps, and limitations when relevant. |
| Navigation and structure | Valid paths and links, discoverable entry points, coherent headings, and focused ownership of detailed explanations. |

Align README and guides with accepted scope and the supported implementation. Label planned or incomplete capabilities explicitly. Keep important limitations visible where users make decisions. Report conflicts that require changes to governing design, SPEC, PLAN, or layout to the user rather than resolving them through a documentation rewrite.

## Examples and checks

- Verify snippets against actual imports, signatures, options, paths, and prerequisites. Use current project facts rather than copying scenario-specific details from another project.
- Run examples or relevant documentation checks where practical within the authorized environment. Distinguish inspected examples from executed examples and record expected versus observed outcomes.
- Check local links and referenced files; assess external links when relevant to the requested work and access permits. Report links that could not be checked.
- Remove stale references and unnecessary duplication within scope. Follow layout rules for placement; propose a layout amendment to the user if the required organization cannot fit them.
- Separate Markdown headings from adjacent content with blank lines, including examples and templates. The beginning of a file or template needs no leading blank line.
