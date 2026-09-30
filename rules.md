# Processing Rules and Guidelines

## Data Extraction Rules

### From README
- Extract title/name from first heading
- Extract description from first paragraph
- Identify features from bulleted lists
- Extract installation instructions if present
- Pull usage examples and code snippets

### From package.json (JavaScript/Node.js)
- `name` → Component name
- `description` → Component description
- `version` → Component version
- `keywords` → Component tags/classification
- `author` → Maintainer information
- `dependencies` → Component dependencies
- `repository.url` → Source repository
- `homepage` → Documentation URL
- `license` → License identifier

### From pyproject.toml (Python)
- `project.name` → Component name
- `project.description` → Short description
- `project.version` → Component version
- `project.authors` → Maintainer information
- `project.keywords` → Classification tags
- `project.dependencies` → Component dependencies
- `project.urls.Homepage` → Documentation URL
- `project.license.text` → License identifier

### From go.mod (Go)
- Module name → Component name
- Comments → Purpose/description
- require statements → Dependencies
- Version constraints → Dependency versions

## Normalization Rules

### Naming
- Convert to kebab-case for identifiers
- Use PascalCase for type names
- Use UPPER_SNAKE_CASE for constants

### Versioning
- Enforce semantic versioning (MAJOR.MINOR.PATCH)
- Tag pre-releases with -alpha, -beta, -rc
- Include build metadata when available

### Dependency Resolution
- Expand version ranges to explicit constraints
- Identify transitive dependencies
- Mark optional vs. required dependencies
- Flag version conflicts

## Enrichment Rules

### Classification
1. Determine component type:
   - Library/Package
   - Service/Application
   - Tool/CLI
   - Framework
   - Template/Boilerplate
   - Configuration

2. Assign domain tags:
   - infrastructure, database, api, ui, testing, etc.

3. Identify maturity level:
   - Alpha, Beta, Stable, Maintenance, Deprecated

### Relationships
- Identify parent/child components
- Detect sibling/related components
- Mark known consumers
- Flag known dependencies

## Validation Rules

### Required Fields
- Component name (non-empty)
- Description (minimum 10 characters)
- Version (semantic format)
- Type (from defined list)

### Constraints
- No circular dependencies
- All dependencies must be resolvable
- License must be SPDX-compliant
- URLs must be valid and accessible

## Export Rules

### Format Compliance
- Output valid JSON/YAML
- Include all required schema fields
- Preserve data types (no string-encoded numbers)
- Escape special characters properly

### Metadata
- Include extraction timestamp
- Record data source version
- Note any warnings or conflicts
- Track manual edits if applicable
