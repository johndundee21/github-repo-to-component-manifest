# Input Data Format Specification

## Repository Structure

The input is a GitHub repository that may contain one or more of these standard configuration files:

### JavaScript/Node.js
**File:** `package.json`

```json
{
  "name": "package-name",
  "version": "1.0.0",
  "description": "Package description",
  "keywords": ["tag1", "tag2"],
  "author": "Author Name <author@example.com>",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/user/repo.git"
  },
  "homepage": "https://example.com",
  "bugs": {
    "url": "https://github.com/user/repo/issues"
  },
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "dependencies": {
    "dependency-name": "^1.0.0"
  },
  "devDependencies": {
    "dev-tool": "^2.0.0"
  },
  "peerDependencies": {
    "peer-package": "^3.0.0"
  },
  "optionalDependencies": {
    "optional-package": "^4.0.0"
  }
}
```

### Python
**File:** `pyproject.toml` (modern) or `setup.py` (legacy)

```toml
[project]
name = "package-name"
version = "1.0.0"
description = "Package description"
authors = [
  {name = "Author Name", email = "author@example.com"}
]
keywords = ["tag1", "tag2"]
license = {text = "MIT"}
requires-python = ">=3.8"

[project.urls]
Homepage = "https://example.com"
Repository = "https://github.com/user/repo"
Documentation = "https://docs.example.com"

[project.dependencies]
dependency-name = ">=1.0.0"

[project.optional-dependencies]
dev = [
  "pytest>=6.0",
  "black>=21.0"
]
```

### Go
**File:** `go.mod`

```
module github.com/user/repo

go 1.20

require (
  github.com/dependency/one v1.0.0
  github.com/dependency/two v2.0.0
)

require (
  github.com/indirect/dep v1.5.0 // indirect
)
```

### Rust
**File:** `Cargo.toml`

```toml
[package]
name = "package-name"
version = "1.0.0"
edition = "2021"
authors = ["Author Name <author@example.com>"]
description = "Package description"
license = "MIT"
repository = "https://github.com/user/repo"
homepage = "https://example.com"
keywords = ["tag1", "tag2"]
categories = ["category1", "category2"]

[dependencies]
dependency-name = "1.0"

[dev-dependencies]
dev-tool = "2.0"

[optional-dependencies]
feature-name = ["optional-dep = 1.0"]
```

## README Metadata

**File:** `README.md` (or `README.rst`, `README.txt`)

Extracted data:
- Title (first heading)
- Description (first paragraph or introduction)
- Features (bulleted or numbered lists)
- Installation instructions
- Usage examples and code snippets
- Badges and metadata
- Links to documentation
- Contributor information

## Git Metadata

Extracted from repository:
- Repository URL
- Default branch
- Latest tag/version
- Commit history
- Release notes
- Contributors list

## GitHub-Specific Metadata

**From repository settings:**
- Topics/tags
- Description
- Homepage URL
- Visibility (public/private)
- Is fork status
- License (detected)
- Primary language

## Structured Data

### Dependency Object
```json
{
  "name": "dependency-name",
  "version": "1.0.0",
  "type": "direct|peer|optional|dev|indirect",
  "url": "https://registry.example.com/package",
  "optional": false
}
```

### Person Object
```json
{
  "name": "Full Name",
  "email": "email@example.com",
  "url": "https://github.com/username",
  "role": "author|maintainer|contributor"
}
```

### URL Object
```json
{
  "type": "homepage|repository|documentation|issues|changelog",
  "url": "https://example.com/path"
}
```

## Data Validation

### Required Fields
- Package name (non-empty string)
- Version (semantic versioning format)
- Description (minimum 10 characters)

### Optional but Recommended
- Author/Maintainer information
- License (SPDX identifier)
- Repository URL
- Keywords/tags (3-5 recommended)
- Homepage URL

### Format Constraints
- Names: alphanumeric, hyphens, underscores (no spaces)
- Versions: MAJOR.MINOR.PATCH format
- URLs: valid HTTP/HTTPS URLs
- Emails: valid email format
- License: SPDX license identifier
