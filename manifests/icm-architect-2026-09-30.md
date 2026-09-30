# Component Manifest

## 1. Repository Record

| Field | Value | Source |
|---|---|---|
| `repository_identifier` | `RinDig/icm-architect` | [header:repository-identifier] |
| `source_snapshot_identifier` | `main-as-of-2026-09-30` | [header:source-snapshot-identifier] |

## 2. Source Coverage

| Path | Lines | Mapped to | Source |
|---|---|---|---|
| `README.md` | 27 | 4, 7 | [tree] |
| `package.json` | 22 | 4, 6, 7 | [tree] |
| `src/App.tsx` | 17 | 3, 4 | [tree] |
| `src/main.tsx` | 10 | 4, 7 | [tree] |
| `src/index.css` | 9 | 7 | [tree] |
| `tsconfig.json` | 21 | 6, 7 | [tree] |
| `vite.config.ts` | 9 | 4, 6, 7 | [tree] |

## 3. Component Manifest

| ID | Kind | Name | Definition | Stated role | Evidence |
|---|---|---|---|---|---|
| component-001 | `function` | `App` | `function App() {` | not in source | [src/App.tsx:3-15] [src/App.tsx:17-17] |

## 4. Dependency Manifest

| Name | Version | Group | Source |
|---|---|---|---|
| `React + TypeScript` | not in source | readme-mention | [README.md:18-18] |
| `Vite` | not in source | readme-mention | [README.md:19-19] |
| `Tailwind CSS` | not in source | readme-mention | [README.md:20-20] |
| `react` | `^18.2.0` | dependencies | [package.json:12-12] |
| `react-dom` | `^18.2.0` | dependencies | [package.json:13-13] |
| `@types/react` | `^18.2.0` | devDependencies | [package.json:16-16] |
| `@types/react-dom` | `^18.2.0` | devDependencies | [package.json:17-17] |
| `@vitejs/plugin-react` | `^4.0.0` | devDependencies | [package.json:18-18] |
| `typescript` | `^5.0.0` | devDependencies | [package.json:19-19] |
| `vite` | `^5.0.0` | devDependencies | [package.json:20-20] |
| `react` | not in source | import | [src/App.tsx:1-1] |
| `react` | not in source | import | [src/main.tsx:1-1] |
| `react-dom/client` | not in source | import | [src/main.tsx:2-2] |
| `./App` | not in source | import-local | [src/main.tsx:3-3] |
| `./index.css` | not in source | import-local | [src/main.tsx:4-4] |
| `vite` | not in source | import | [vite.config.ts:1-1] |
| `@vitejs/plugin-react` | not in source | import | [vite.config.ts:2-2] |

## 5. Route Manifest

none found in source

## 6. Configuration Manifest

| Key | Value | Evidence |
|---|---|---|
| `package.json#name` | `"icm-architect"` | [package.json:2-2] |
| `package.json#private` | `true` | [package.json:3-3] |
| `package.json#version` | `"0.0.1"` | [package.json:4-4] |
| `package.json#type` | `"module"` | [package.json:5-5] |
| `package.json#scripts.dev` | `"vite"` | [package.json:7-7] |
| `package.json#scripts.build` | `"tsc && vite build"` | [package.json:8-8] |
| `package.json#scripts.preview` | `"vite preview"` | [package.json:9-9] |
| `tsconfig.json#compilerOptions.target` | `"ES2020"` | [tsconfig.json:3-3] |
| `tsconfig.json#compilerOptions.useDefineForClassFields` | `true` | [tsconfig.json:4-4] |
| `tsconfig.json#compilerOptions.lib` | `["ES2020", "DOM", "DOM.Iterable"]` | [tsconfig.json:5-5] |
| `tsconfig.json#compilerOptions.module` | `"ESNext"` | [tsconfig.json:6-6] |
| `tsconfig.json#compilerOptions.skipLibCheck` | `true` | [tsconfig.json:7-7] |
| `tsconfig.json#compilerOptions.moduleResolution` | `"bundler"` | [tsconfig.json:8-8] |
| `tsconfig.json#compilerOptions.allowImportingTsExtensions` | `true` | [tsconfig.json:9-9] |
| `tsconfig.json#compilerOptions.resolveJsonModule` | `true` | [tsconfig.json:10-10] |
| `tsconfig.json#compilerOptions.isolatedModules` | `true` | [tsconfig.json:11-11] |
| `tsconfig.json#compilerOptions.noEmit` | `true` | [tsconfig.json:12-12] |
| `tsconfig.json#compilerOptions.jsx` | `"react-jsx"` | [tsconfig.json:13-13] |
| `tsconfig.json#compilerOptions.strict` | `true` | [tsconfig.json:14-14] |
| `tsconfig.json#compilerOptions.noUnusedLocals` | `true` | [tsconfig.json:15-15] |
| `tsconfig.json#compilerOptions.noUnusedParameters` | `true` | [tsconfig.json:16-16] |
| `tsconfig.json#compilerOptions.noFallthroughCasesInSwitch` | `true` | [tsconfig.json:17-17] |
| `tsconfig.json#include` | `["src"]` | [tsconfig.json:19-19] |
| `tsconfig.json#references` | `[{ "path": "./tsconfig.node.json" }]` | [tsconfig.json:20-20] |
| `vite.config.ts#plugins` | `[react()]` | [vite.config.ts:5-5] |
| `vite.config.ts#server.port` | `3000` | [vite.config.ts:7-7] |

## 7. Unmapped Source Items

| Path | Item | Evidence |
|---|---|---|
| `README.md` | `# ICM Architect` | [README.md:1-1] |
| `README.md` | `An intelligent agent system for enterprise architecture and business-IT alignment.` | [README.md:3-3] |
| `README.md` | `## Overview` | [README.md:5-5] |
| `README.md` | `ICM Architect uses a multi-agent system to analyze and design enterprise architectures aligned with business strategy.` | [README.md:7-7] |
| `README.md` | `## Features` | [README.md:9-9] |
| `README.md` | `- Business capability modeling` | [README.md:11-14] |
| `README.md` | `## Tech Stack` | [README.md:16-16] |
| `README.md` | `## Getting Started` | [README.md:22-22] |
| `README.md` | `npm install` | [README.md:25-26] |
| `package.json` | `"scripts": {` | [package.json:6-6] |
| `package.json` | `"dependencies": {` | [package.json:11-11] |
| `package.json` | `"devDependencies": {` | [package.json:15-15] |
| `src/main.tsx` | `ReactDOM.createRoot(document.getElementById('root')!).render(` | [src/main.tsx:6-9] |
| `src/index.css` | `:root {` | [src/index.css:1-2] |
| `src/index.css` | `body {` | [src/index.css:5-8] |
| `tsconfig.json` | `"compilerOptions": {` | [tsconfig.json:2-2] |
| `vite.config.ts` | `export default defineConfig({` | [vite.config.ts:4-4] |
| `vite.config.ts` | `server: {` | [vite.config.ts:6-6] |

## 8. Translation Exceptions

| # | Type | Exception | Evidence |
|---|---|---|---|
| 1 | missing-referenced-file | tsconfig.json references `./tsconfig.node.json`, which is not listed in the FILE TREE. | [tsconfig.json:20-20] [tree] |
| 2 | doc-code-mismatch | README.md lists `Tailwind CSS` under its stack list; no `dependencies`, `devDependencies`, or import entry in the manifest matches that name. | [README.md:20-20] [package.json:11-21] |
