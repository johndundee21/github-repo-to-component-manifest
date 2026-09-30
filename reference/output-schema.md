# Output Manifest Schema

## Top-Level Structure

```yaml
component:
  name: string
  version: string
  type: string
  language: string
  description: string
  keywords: [string]
  maintainers: [Person]
  license: string
  repository: string
  homepage: string
  documentation: string
  maturity: string
  dependencies: [Dependency]
  optionalFeatures: [Feature]
  metadata: object
  warnings: [string]
```

## Field Definitions

### name (required)
**Type:** `string`
**Pattern:** `^[a-z0-9][a-z0-9-]*[a-z0-9]$`
**Description:** Component identifier in kebab-case
**Example:** `react-query`, `django-rest-framework`

### version (required)
**Type:** `string`
**Pattern:** `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$`
**Description:** Semantic version of the component
**Example:** `1.0.0`, `2.1.3-beta.1`, `3.0.0+build.1`

### type (required)
**Type:** `string`
**Enum:** `library`, `service`, `tool`, `framework`, `template`, `configuration`, `plugin`, `driver`, `middleware`, `unknown`
**Description:** Component classification
**Example:** `library`

### language (required)
**Type:** `string`
**Enum:** `javascript`, `python`, `go`, `rust`, `java`, `csharp`, `php`, `ruby`, `swift`, `kotlin`, `other`
**Description:** Primary programming language
**Example:** `python`

### description (required)
**Type:** `string`
**MinLength:** `10`
**MaxLength:** `500`
**Description:** Short description of component purpose
**Example:** `A high-level Python web framework that encourages rapid development.`

### keywords (optional)
**Type:** `[string]`
**MaxItems:** `10`
**Description:** Search tags for categorization
**Example:** `["web", "framework", "mvc"]`

### maintainers (optional)
**Type:** `[Person]`
**Description:** List of component maintainers

#### Person Object
```yaml
maintainers:
  - name: string (required)
    email: string (optional, email format)
    url: string (optional, URL format)
    role: string (optional, enum: author, maintainer, contributor)
```

### license (optional)
**Type:** `string`
**Description:** SPDX license identifier
**Examples:** `MIT`, `Apache-2.0`, `GPL-3.0`, `BSD-3-Clause`

### repository (optional)
**Type:** `string`
**Format:** `uri`
**Description:** Git repository URL
**Example:** `https://github.com/user/repo`

### homepage (optional)
**Type:** `string`
**Format:** `uri`
**Description:** Component website or documentation homepage
**Example:** `https://example.com`

### documentation (optional)
**Type:** `string`
**Format:** `uri`
**Description:** Link to full documentation
**Example:** `https://docs.example.com`

### maturity (optional)
**Type:** `string`
**Enum:** `alpha`, `beta`, `release-candidate`, `stable`, `maintenance`, `deprecated`
**Description:** Development/lifecycle status
**Example:** `stable`

### dependencies (optional)
**Type:** `[Dependency]`
**Description:** List of component dependencies

#### Dependency Object
```yaml
dependencies:
  - name: string (required)
    version: string (required, semantic version or range)
    type: string (optional, enum: direct, peer, optional, dev, indirect)
    url: string (optional, registry or repository URL)
```

### optionalFeatures (optional)
**Type:** `[Feature]`
**Description:** Optional feature sets with their own dependencies

#### Feature Object
```yaml
optionalFeatures:
  - name: string (required)
    description: string (optional)
    dependencies: [Dependency]
```

### metadata (optional)
**Type:** `object`
**Description:** Additional arbitrary metadata
**Example:**
```yaml
metadata:
  repository.stars: 15000
  repository.watchers: 1200
  package.downloads: 5000000
  documentation.updated: "2024-01-15"
```

### warnings (optional)
**Type:** `[string]`
**Description:** Processing warnings or data quality issues
**Examples:**
- `Unable to determine package manager`
- `Version inferred from git tags`
- `Circular dependency detected`

## Complete Example

```yaml
component:
  name: axios
  version: 1.6.2
  type: library
  language: javascript
  description: Promise based HTTP client for the browser and node.js
  keywords:
    - http
    - client
    - promise
    - async
    - xhr
  maintainers:
    - name: Matt Zabriskie
      url: https://github.com/mzabriskie
      role: author
    - name: Collaborators
      url: https://github.com/axios/axios/graphs/contributors
      role: contributor
  license: MIT
  repository: https://github.com/axios/axios
  homepage: https://axios-http.com
  documentation: https://axios-http.com/docs
  maturity: stable
  dependencies:
    - name: follow-redirects
      version: ^1.15.0
      type: direct
    - name: proxy-from-env
      version: ^1.1.0
      type: direct
    - name: form-data
      version: ^4.0.0
      type: optional
  optionalFeatures:
    - name: form-data-support
      description: Support for multipart/form-data requests
      dependencies:
        - name: form-data
          version: ^4.0.0
  metadata:
    npm.downloads.weekly: 25000000
    github.stars: 103000
    github.watchers: 2500
  warnings: []
```

## JSON Schema (for validation)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Component Manifest",
  "type": "object",
  "required": ["component"],
  "properties": {
    "component": {
      "type": "object",
      "required": ["name", "version", "type", "language", "description"],
      "properties": {
        "name": {"type": "string", "pattern": "^[a-z0-9][a-z0-9-]*[a-z0-9]$"},
        "version": {"type": "string"},
        "type": {"type": "string", "enum": ["library", "service", "tool", "framework", "template", "configuration", "plugin", "driver", "middleware", "unknown"]},
        "language": {"type": "string"},
        "description": {"type": "string", "minLength": 10},
        "keywords": {"type": "array", "items": {"type": "string"}},
        "maintainers": {"type": "array", "items": {"type": "object"}},
        "license": {"type": "string"},
        "repository": {"type": "string", "format": "uri"},
        "homepage": {"type": "string", "format": "uri"},
        "documentation": {"type": "string", "format": "uri"},
        "maturity": {"type": "string"},
        "dependencies": {"type": "array", "items": {"type": "object"}},
        "optionalFeatures": {"type": "array", "items": {"type": "object"}},
        "metadata": {"type": "object"},
        "warnings": {"type": "array", "items": {"type": "string"}}
      }
    }
  }
}
```
