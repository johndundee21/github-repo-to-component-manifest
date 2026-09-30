Examples
Two complete input/output pairs that show the contract holding.

Example 1: Small JavaScript repo with one component
Input snapshot
text
REPOSITORY IDENTIFIER
example/tiny-js-repo

SOURCE SNAPSHOT IDENTIFIER
main-2026-09-30

FILE TREE
package.json
src/math.js

--- package.json ---
1: {
2:   "name": "tiny-js-repo",
3:   "version": "1.0.0",
4:   "dependencies": {
5:     "lodash": "^4.17.21"
6:   }
7: }

--- src/math.js ---
1: import _ from "lodash";
2: 
3: export function add(a, b) {
4:   return a + b;
5: }
Output (strict schema)
text
# Component Manifest

## 1. Repository Record

| Field | Value | Source |
|-------|-------|--------|
| `repository_identifier` | `example/tiny-js-repo` | `[header:repository-identifier]` |
| `source_snapshot_identifier` | `main-2026-09-30` | `[header:source-snapshot-identifier]` |

## 2. Source Coverage

| Path | Lines | Mapped to | Source |
|------|-------|-----------|--------|
| `package.json` | 7 | 4, 6 | `[tree]` |
| `src/math.js` | 5 | 3, 4, 7 | `[tree]` |

## 3. Component Manifest

| ID | Kind | Name | Definition | Stated role | Evidence |
|----|------|------|------------|-------------|----------|
| `component-001` | `function` | `add` | `export function add(a, b) {` | `not in source` | `[src/math.js:3-5]` |

## 4. Dependency Manifest

| Name | Version | Group | Source |
|------|---------|-------|--------|
| `lodash` | `"^4.17.21"` | `dependencies` | `[package.json:5-5]` |
| `lodash` | `"lodash"` | `import` | `[src/math.js:1-1]` |

## 5. Route Manifest

none found in source

## 6. Configuration Manifest

| Key | Value | Evidence |
|-----|-------|----------|
| `package.json#name` | `"tiny-js-repo"` | `[package.json:2-2]` |
| `package.json#version` | `"1.0.0"` | `[package.json:3-3]` |

## 7. Unmapped Source Items

| Path | Item | Evidence |
|------|------|----------|
| `src/math.js` | `import _ from "lodash";` | `[src/math.js:1-1]` |

## 8. Translation Exceptions

| # | Type | Exception | Evidence |
|---|------|-----------|----------|
| 1 | `header-missing` | No `REPOSITORY IDENTIFIER` line supplied. | `not in source` |
Example 2: Sparse repo (README only)
Input snapshot
text
REPOSITORY IDENTIFIER
example/readme-only

SOURCE SNAPSHOT IDENTIFIER
export-1

FILE TREE
README.md

--- README.md ---
1: # Sample
2: 
3: A repo with no code.
Output (strict schema)
text
# Component Manifest

## 1. Repository Record

| Field | Value | Source |
|-------|-------|--------|
| `repository_identifier` | `example/readme-only` | `[header:repository-identifier]` |
| `source_snapshot_identifier` | `export-1` | `[header:source-snapshot-identifier]` |

## 2. Source Coverage

| Path | Lines | Mapped to | Source |
|------|-------|-----------|--------|
| `README.md` | 3 | 7 | `[tree]` |

## 3. Component Manifest

none found in source

## 4. Dependency Manifest

none found in source

## 5. Route Manifest

none found in source

## 6. Configuration Manifest

none found in source

## 7. Unmapped Source Items

| Path | Item | Evidence |
|------|------|----------|
| `README.md` | `# Sample` | `[README.md:1-3]` |

## 8. Translation Exceptions

none found in source
