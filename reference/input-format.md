Input Format
Supply a repository snapshot in plain text using this structure:

text
REPOSITORY IDENTIFIER (optional)
owner/repo

SOURCE SNAPSHOT IDENTIFIER (optional)
commit-or-export-label

FILE TREE
path/to/file1
path/to/file2
...

--- path/to/file1 ---
1: line one
2: line two
3: line three

--- path/to/file2 ---
1: ...
Required elements
FILE TREE — List every file path you want included, one per line.

File contents — For each file, provide the full text under a header --- path/to/file ---.

Line numbers — Prefix each line with N: where N is the line number (1-based). Do not change the content; only add line numbers.

Optional elements
REPOSITORY IDENTIFIER — A single line with owner/repo or similar. If omitted, Section 1 will have not in source for repository_identifier.

SOURCE SNAPSHOT IDENTIFIER — A label such as a commit SHA, branch name, or export date.

Constraints
Paths in the file tree must match the paths used in file headers.

Preserve original content exactly; add line numbers only.

For binary, generated, or unreadable files, list the path in FILE TREE and either:

Provide no content (then Lines will be not supplied), or

Explicitly mark content as unavailable in a comment. The translator will report this in Section 8 (unreadable-content).

Example (minimal)
text
REPOSITORY IDENTIFIER
example/repo

SOURCE SNAPSHOT IDENTIFIER
main-2026-09-30

FILE TREE
README.md

--- README.md ---
1: # Example
2: 
3: A minimal repo.
