📦 GitHub Repo → Component Manifest Translator
A folder-based AI translator that converts a supplied GitHub repository snapshot into a traceable inventory of components ready for extraction, inspection, or handoff.

🎯 What it does
Input	Output
Repository file tree + file contents (line-numbered)	Fixed-shape Component Manifest (8 sections, strict schema v2)
Every output claim must point to a source locator. The translator:

❌ Never fetches a repository from a URL

❌ Never guesses a framework or assigns architectural roles

❌ Never fills missing details with plausible values

✅ Always traces claims to [path:N-N], [header:...], or [tree]

✅ Always marks missing data as not in source

📁 Folder contents
text
github-repo-to-component-manifest/
├── 📄 identity.md           # What it converts (repo snapshot → manifest)
├── 📐 rules.md              # Mapping rules, evidence requirements, missing-data handling
├── 💬 examples.md           # 2 complete input/output pairs (strict schema)
├── 📖 README.md             # This file — usage instructions for Claude
└── 📚 reference/
    ├── input-format.md      # How to format the repository snapshot
    └── output-schema.md     # The exact output contract (strict, v2)
🚀 How to use in Claude
Step	Action
1	Create a Claude Project
2	Upload this complete folder as Project Knowledge
3	Paste one repository snapshot using reference/input-format.md as a template
4	Prompt: "Translate this repository snapshot into the Component Manifest contract. Apply the folder rules exactly."
5	Save the returned Markdown as component-manifest.md beside the snapshot
📋 Required input
At minimum, provide:

✅ A file tree

✅ Contents for each file you want included

✅ Stable line numbers (either supplied or added without changing content)

⚠️ A GitHub URL is optional identification metadata only. It is not permission to retrieve, assume, or invent repository content.

✅ Verification checklist
Before accepting an output, verify:

Starts with # Component Manifest, eight headings exact and in order, nothing outside them

One table per section, exact column headers, or none found in source

Every locator matches the allowed forms: [path:N-N], [header:...], [tree]

I1: every FILE TREE path is in Section 2 exactly once

I2: no non-exempt line is uncited by Sections 3 to 7

I3: sampled values appear verbatim in cited lines

Section 4 has one table with a valid Group on every row

No Kind, Stated role, or label is a translator invention

Every Section 8 row has a valid Type and a locator (or not in source only for header-missing)

📖 Example
See examples.md for two complete contract examples:

Small JavaScript repo — one exported function + lodash dependency

Sparse repo — README only, no extractable code components

🚫 Non-goals
This translator does not:

Summarize the repository

Evaluate code quality

Propose refactors

Estimate effort

Infer service boundaries

Generate documentation

Extract content from an unprovided GitHub URL

Built for the Clief Notes Weekly Comp #13: The Translator — a discipline of fidelity over judgment. Every line traces to source. Nothing invented. Nothing dropped.

Source of truth: reference/output-schema.md (strict, v2) and rules.md.
