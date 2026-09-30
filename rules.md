# Rules

The translator's job is fidelity, not judgment. It converts a repository snapshot into the Component Manifest defined in `reference/output-schema.md`. That schema is the only output contract. If these rules and the schema ever disagree, the schema wins.

## Hard rules

1. **Output only the manifest.** Start with `# Component Manifest`, end after Section 8. No preamble, summary, or commentary.
2. **Eight sections, exact headings, fixed order.** One table per section with the exact columns, or the single line `none found in source`.
3. **Cite everything.** Every row carries at least one locator in an allowed form: `[path:N-N]`, `[header:repository-identifier]`, `[header:source-snapshot-identifier]`, or `[tree]`. A row without a locator is invalid and must be corrected or removed.
4. **Copy, never rephrase.** Identifiers, literals, paths, dependency names, version specifiers, and route strings are copied exactly, inside code spans.
5. **Absence has one spelling.** A value cell with no evidence is `not in source`. An empty section is `none found in source`. Never mix them. A Source or Evidence cell is `not in source` only when the whole row has no evidence (a missing header value or a `header-missing` exception); every other row keeps its locators even if one of its value cells says `not in source`.
6. **No inference.** Do not infer frameworks, roles, owners, versions, purposes, or architecture. Do not name things the source does not name. Labels like "entry point", "main app", or "backend" are forbidden unless that exact label is written in source.
7. **Nothing is silently dropped.** Every supplied file appears in Section 2. Every non-exempt line ends up cited in Sections 3 to 7. Leftovers go to Section 7.
8. **When unsure, do not guess.** Put the item in Section 7 or raise a Section 8 exception. Do not omit it and do not classify it.

## Working procedure

1. Read the header. Fill Section 1 from `[header:...]` locators.
2. List every FILE TREE path into Section 2, then fill `Lines` and `Mapped to` at the end.
3. For each supplied file in tree order, extract top-level declarations (Section 3), dependency declarations and imports (Section 4), string-literal route declarations (Section 5), and config key/value pairs plus package metadata (Section 6).
4. Compute uncited non-exempt lines and emit them as Section 7 runs.
5. Raise Section 8 exceptions only for the five schema types.
6. Run the schema's validation checklist before returning the output. Manifests are also checked with `validate_manifest.py`.

## Section-specific rules

- **One table per section.** No sub-tables. Dependency origin is distinguished by the `Group` column, not by separate tables.
- **Component detail cap.** `Definition` is the declaration line only. No narrative, no JSX tree, no bullet lists. `Kind` is the declaring keyword as written in source.
- **Package metadata.** Fields such as name, version, private, and type from `package.json` are Section 6 rows, not Section 1 fields.
- **Absence claims.** Do not assert repository-wide absences (no tests, no routes, no env vars) in Section 8. Empty Sections 5 and 6 already say `none found in source`.
- **Mismatch exceptions.** A `doc-code-mismatch` is raised only for a README stack-list item whose parts match no dependency or import name, using the comparison in the schema. README claims about features or architecture are never exceptions; they stay in Section 7. An exception states the discrepancy, never a cause or a fix.
- **Unmapped runs.** Section 7 has one row per run, split at blank lines, exempt lines, cited lines, and Markdown headings.
- **README mentions.** Copy each README stack-list item whole as one `readme-mention` row.

## Determinism

- Rows are ordered by FILE TREE order, then ascending start line.
- Section 3 IDs are sequential in that order.
- Two runs on the same snapshot should produce the same section headings, same column headers, and the same row set. If they do not, the rule that allowed the difference is too loose and needs tightening.
