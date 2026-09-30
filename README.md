🧭 GitHub Repo → Component Manifest
Property	Value
Input	Repository snapshot (file tree + file contents, line-numbered)
Output	Fixed-shape Component Manifest (8 sections, strict schema)
Contract	Every output line cites [path:N-N], [header:...], or [tree], or says not in source
What this converts
text
┌─────────────────────────────────────┐
│  Repository Snapshot                │
│  - FILE TREE                        │
│  - File contents (line-numbered)    │
│  - Optional headers                 │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Component Manifest (strict, v2)    │
│  1. Repository Record               │
│  2. Source Coverage                 │
│  3. Component Manifest              │
│  4. Dependency Manifest             │
│  5. Route Manifest                  │
│  6. Configuration Manifest          │
│  7. Unmapped Source Items           │
│  8. Translation Exceptions          │
└─────────────────────────────────────┘
Purpose
Convert repository evidence into a component-level handoff that another engineer or AI agent can extract, inspect, or replace without guessing. The manifest indexes:

✅ Source files (with coverage tracking)

✅ Top-level declarations (functions, classes, consts, etc.)

✅ Dependencies (package.json, imports, README mentions)

✅ Routes (string-literal route declarations only)

✅ Configuration keys (explicit declarations in config files)

✅ Unmapped items (nothing silently dropped)

✅ Translation exceptions (missing files, doc/code mismatches, etc.)

Non-negotiable rules
Rule	Enforcement
Fixed output shape	Eight mandatory sections in exact order; empty sections say none found in source
Nothing invented	Every claim requires a locator ([path:N-N], [header:...], [tree]); missing fields say not in source
Nothing dropped	Every supplied file appears in Section 2; every non-exempt line is cited in Sections 3–7
This is an inventory and mapping tool, not an architectural review, summary, recommendation, or refactor plan.

Source of truth: reference/output-schema.md (strict, v2) and rules.md.
