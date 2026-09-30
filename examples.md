# Real-World Examples

## Example 1: JavaScript Library

### Source Repository
```
react-query/
├── README.md
├── package.json
├── src/
│   └── ...
└── docs/
    └── ...
```

### package.json
```json
{
  "name": "@tanstack/react-query",
  "version": "5.0.0",
  "description": "Powerful asynchronous state management for TS/JS, React, Solid, Svelte and Vue Query",
  "keywords": ["query", "cache", "async", "state", "management"],
  "author": "TanStack",
  "license": "MIT",
  "dependencies": {
    "react": "^18.0.0"
  }
}
```

### Generated Manifest
```yaml
component:
  name: react-query
  version: 5.0.0
  type: library
  language: javascript
  description: Powerful asynchronous state management for TS/JS, React, Solid, Svelte and Vue Query
  keywords:
    - query
    - cache
    - async
    - state
    - management
  maintainers:
    - name: TanStack
  license: MIT
  repository: https://github.com/TanStack/query
  dependencies:
    - name: react
      version: "^18.0.0"
      type: peer
```

---

## Example 2: Python Package

### Source Repository
```
django/
├── README.md
├── pyproject.toml
├── django/
│   └── ...
└── docs/
    └── ...
```

### pyproject.toml
```toml
[project]
name = "Django"
version = "4.2.0"
description = "A high-level Python web framework that encourages rapid development."
authors = [{name = "Django Software Foundation"}]
keywords = ["web", "framework", "python", "mvc"]
license = {text = "BSD-3-Clause"}

[project.urls]
Homepage = "https://www.djangoproject.com"
Repository = "https://github.com/django/django"

[project.optional-dependencies]
testing = ["pytest>=6.0"]
```

### Generated Manifest
```yaml
component:
  name: django
  version: 4.2.0
  type: framework
  language: python
  description: A high-level Python web framework that encourages rapid development.
  keywords:
    - web
    - framework
    - python
    - mvc
  maintainers:
    - name: Django Software Foundation
  license: BSD-3-Clause
  repository: https://github.com/django/django
  homepage: https://www.djangoproject.com
  maturity: stable
  optionalFeatures:
    - name: testing
      dependencies:
        - name: pytest
          version: ">=6.0"
```

---

## Example 3: Go Module

### Source Repository
```
kubernetes/
├── README.md
├── go.mod
├── go.sum
└── ...
```

### go.mod
```
module k8s.io/kubernetes

go 1.20

require (
  k8s.io/api v0.28.0
  k8s.io/client-go v0.28.0
  github.com/spf13/cobra v1.7.0
)
```

### Generated Manifest
```yaml
component:
  name: kubernetes
  version: 1.28.0
  type: system
  language: go
  description: Production-Grade Container Orchestration
  keywords:
    - orchestration
    - containers
    - devops
  license: Apache-2.0
  repository: https://github.com/kubernetes/kubernetes
  dependencies:
    - name: k8s.io/api
      version: 0.28.0
    - name: k8s.io/client-go
      version: 0.28.0
    - name: github.com/spf13/cobra
      version: 1.7.0
  maturity: stable
```

---

## Example 4: Transformation Decision Tree

### Input: Unknown Repository

```
1. Does it have package.json?
   YES → Use JavaScript/Node.js rules
   NO → Continue

2. Does it have pyproject.toml or setup.py?
   YES → Use Python rules
   NO → Continue

3. Does it have go.mod?
   YES → Use Go rules
   NO → Continue

4. Does it have Cargo.toml?
   YES → Use Rust rules
   NO → Continue

5. Fall back to README analysis
   - Extract name from heading
   - Extract description from content
   - Infer type from repository structure
   - Use git tags for version
```

### Output: Minimal Manifest
```yaml
component:
  name: unknown-component
  version: 0.0.1
  type: unknown
  description: Description extracted from README
  repository: https://github.com/user/repo
  warnings:
    - Unable to determine package manager
    - Version inferred from git tags
    - Limited metadata extraction
```
