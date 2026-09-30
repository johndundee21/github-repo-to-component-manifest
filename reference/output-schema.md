# Component Manifest Output Schema (strict, v2)

This file is the single output contract. The translator returns one Markdown document that follows the conventions, sections, and invariants below. Nothing else is allowed.

## 0. Conventions (apply to the whole document)

### Document shape

- The first line is `# Component Manifest`. The last line is the end of Section 8. No text, summary, or commentary before, between, or after sections.
- Section headings are exactly:
  - `## 1. Repository Record`
  - `## 2. Source Coverage`
  - `## 3. Component Manifest`
  - `## 4. Dependency Manifest`
  - `## 5. Route Manifest`
  - `## 6. Configuration Manifest`
  - `## 7. Unmapped Source Items`
  - `## 8. Translation Exceptions`
- Each section contains exactly one table with the exact column headers given below, or the single plain line `none found in source`.
- Sections 1 and 2 are never empty. Sections 3 to 8 may be `none found in source`.
- No sub-headings, sub-tables, bullet lists, or blockquotes inside sections.

### Cells

- Values copied from source are written verbatim inside a code span, e.g. `"icm-architect"`.
- A literal `|` inside a value is escaped as `\|`.
- A multi-line value is shown as its first line only; the locator carries the full range.
- Free text (Exception descriptions) is plain text, never a code span, and quotes source text only via code spans.

### Locators (the only allowed forms)

- `[path:N-N]` where `N-N` are line numbers. A single line is written `[src/App.tsx:4-4]`, never `[src/App.tsx:4]`.
- `[header:repository-identifier]` and `[header:source-snapshot-identifier]` for values taken from the snapshot header.
- `[tree]` for facts taken from the FILE TREE (a path exists, or a referenced path does not).
- Multiple locators in one cell are separated by a single space.
- Validation regex for one locator:
  \[
  \[(?:[^\]:\s]+:\d+-\d+|header:(?:repository-identifier|source-snapshot-identifier)|tree)\]
  \]

### Absence

- A field with no supporting evidence is `not in source`, and its `Source` or `Evidence` cell is also `not in source`. Never pair `not in source` with a locator.
- `none found in source` is used only for an entire empty section.

### Ordering (makes output deterministic)

- Rows follow FILE TREE order, then ascending start line.
- Section 1 and Section 8 use the fixed orders stated below.

## Global invariants (checkable)

- **I1 File coverage.** Every path in the FILE TREE appears exactly once in Section 2.
- **I2 Line coverage.** Every non-exempt line of every supplied file is inside a locator range of at least one row in Sections 3 to 7. Section 7 exists to catch whatever Sections 3 to 6 leave out. Exempt lines: blank lines, lines containing only brackets, braces, parentheses, or commas, and Markdown code-fence delimiter lines.
- **I3 Locator truth.** Every locator points to lines that exist, and every code-span value in the row appears verbatim in the cited lines.
- **I4 No inference.** No cell contains a role, framework, purpose, owner, version, or architecture statement that is not written in the cited lines.

---

## 1. Repository Record

**Columns:** `Field | Value | Source`

Exactly two rows, in this order:

1. Field `repository_identifier`.  
   - Value is the exact string under `REPOSITORY IDENTIFIER`, or `not in source`.  
   - Source is `[header:repository-identifier]` or `not in source`.
2. Field `source_snapshot_identifier`.  
   - Value is the exact string under `SOURCE SNAPSHOT IDENTIFIER`, or `not in source`.  
   - Source is `[header:source-snapshot-identifier]` or `not in source`.

Package name, version, license, and similar fields are not part of this section. They appear as rows in Section 6.

---

## 2. Source Coverage

**Columns:** `Path | Lines | Mapped to | Source`

- One row per FILE TREE path (I1).
- `Lines` is the total number of lines supplied for that file, or `not supplied` if the tree lists the file but no contents were given.
- `Mapped to` is a comma-separated list of the section numbers (3 to 7) that cite this file, e.g. `3, 4, 7`. A file with no supplied content is `none`.
- `Source` is `[tree]`.

---

## 3. Component Manifest

**Columns:** `ID | Kind | Name | Definition | Stated role | Evidence`

- Scope: top-level declarations in supplied source-code files (not config files). One row per declaration.
- `ID` is sequential: `component-001`, `component-002`, and so on.
- `Kind` is the declaring keyword exactly as written in source (`function`, `class`, `const`, `interface`, `type`, `enum`, `def`, and so on). It is never a category the translator chose.
- `Name` is the declared identifier, verbatim.
- `Definition` is the declaration line only, verbatim, as a code span. No body, no JSX tree, no narrative.
- `Stated role` is filled only if the source literally states a role for the component, otherwise `not in source`.
- `Evidence` is the locator of the full declaration range (this covers the body for I2). If the same name is exported by an explicit export statement in the same file, that statement's locator is added.
- Statements that are not declarations (for example a top-level call) are not components. They are reported in Section 7.

---

## 4. Dependency Manifest

**Columns:** `Name | Version | Group | Source`

- One row per occurrence.
- `Name` is the exact package name, module specifier, or README-listed name.
- `Version` is the exact declared specifier, or `not in source`.
- `Group` is exactly one of: `dependencies`, `devDependencies`, `peerDependencies`, `optionalDependencies`, `import`, `import-local`, `readme-mention`.
  - `import` is an `import` or `require` of a non-relative specifier.
  - `import-local` is an `import` of a relative path (starts with `.`).
  - `readme-mention` is a technology or package name listed in README prose or lists that the README presents as a stack, requirement, or dependency.
- `Source` is the locator of the declaring line.

---

## 5. Route Manifest

**Columns:** `Route | Declaration | Evidence`

- `Route` is the exact route string literal.
- `Declaration` is the exact declaring call or element text, e.g. `app.get(...)` or `<Route ...>`, as a code span.
- Only routes declared with a string literal in source are listed. File-based or convention-based routing is never inferred from directory names.

---

## 6. Configuration Manifest

**Columns:** `Key | Value | Evidence`

- Scope: supplied files whose names end in `.json`, `.yaml`, `.yml`, `.toml`, `.ini`, or start with `.env`, or contain `.config.`.
- `Key` is `<path>#<dotted.key>`, e.g. `package.json#scripts.dev`, `tsconfig.json#compilerOptions.jsx`, `vite.config.ts#server.port`. Nested objects are flattened to leaf keys. A leaf that is an array is one row whose `Value` is the whole array literal.
- `Value` is the exact literal.
- Dependency maps (`dependencies`, `devDependencies`, etc.) go to Section 4, not here.
- Environment variable references in code (for example `process.env.NAME`) are rows with `Key` `env:NAME` and `Value` `not in source`.

---

## 7. Unmapped Source Items

**Columns:** `Path | Item | Evidence`

- One row per maximal contiguous run of non-exempt lines that no row in Sections 3 to 6 cites (I2).
- `Item` is the first line of the run, verbatim, as a code span.
- `Evidence` is the locator of the whole run.

---

## 8. Translation Exceptions

**Columns:** `# | Type | Exception | Evidence`

- Numbered from 1 in the order raised.
- `Type` is exactly one of:
  - `missing-referenced-file`: a path referenced by a supplied file is absent from the FILE TREE. Evidence: the referencing line plus `[tree]`.
  - `doc-code-mismatch`: a README or comment statement conflicts with, or has no counterpart in, the supplied files. The `Exception` text quotes both sides via code spans. Evidence: both locators. This is the only type that involves judgment, so it must never assert more than the cited lines show.
  - `unreadable-content`: a file is listed but content is missing, truncated, or not text. Evidence: `[tree]`.
  - `header-missing`: an optional header value was not supplied. Evidence: `not in source`.
  - `unnumbered-source`: file contents lack line numbers, so precise locators are impossible. Evidence: `[tree]`.
- Repository-wide absence claims ("no tests exist") are not exceptions. Only conditions checkable against cited lines or the FILE TREE qualify.

---

## Validation checklist

- Starts with `# Component Manifest`, eight headings exact and in order, nothing outside them.
- One table per section, exact column headers, or `none found in source`.
- Every locator matches the regex in Section 0.
- I1: every FILE TREE path is in Section 2 exactly once.
- I2: no non-exempt line is uncited by Sections 3 to 7.
- I3: sampled values appear verbatim in cited lines.
- Section 4 has one table with a valid `Group` on every row.
- No `Kind`, `Stated role`, or label is a translator invention.
- Every Section 8 row has a valid `Type` and a locator (or `not in source` only for `header-missing`).
