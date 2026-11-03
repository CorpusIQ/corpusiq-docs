---
title: "JSON Render - Generative UI Framework Setup"
description: "vercel-labs/json-render: 105.8K combined installs. Skills for JSON-driven generative UI: React, Vue, Svelte, PDF, video and 36 shadcn components."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/json-render-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "generative ui", "react", "vercel", "json"]
---

# JSON Render - Setup Guide

**Source:** [vercel-labs/json-render](https://www.skills.sh/vercel-labs/json-render) via skills.sh - 105.8K combined installs across 38 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [vercel-labs/json-render](https://github.com/vercel-labs/json-render) - 18,893 stars, Apache-2.0, branch main, last pushed 2026-11-03; 31 skill directories under `skills/` plus one internal skill at `.agents/skills/technical-writer`, each skill a single `SKILL.md`, alongside 33 directories under `packages/` in a pnpm and Turbo workspace

**Category:** Generative UI, the framework that constrains model output to a component catalog and renders the resulting JSON as React, Vue, Svelte, Solid, mobile, video, PDF, email, terminal or image output

**Quality Tier:** 🟢 Green - all three sampled listings pass Gen Agent Trust Hub, Socket and Snyk, and the repository ships an Apache-2.0 LICENSE file

json-render is the Vercel Labs take on generative UI, and its premise is the inverse of "let the model write JSX". The model emits JSON that conforms to a schema you define, restricted to components you registered in a catalog, and the renderer turns that JSON into a real interface. The README states the four properties it is selling: guardrailed, because the model can only use catalog components; predictable, because output matches the schema every time; fast, because the spec streams and renders progressively; and cross-platform, because the same catalog targets React, Vue, Svelte and Solid on the web, React Native on mobile, plus video, PDF, email, terminal and image renderers.

The skills in the repository are per-package documentation, not per-package wrappers. `core` covers schemas, catalogs, prompt generation and the SpecStream format. `react`, `vue`, `svelte`, `solid`, `next` and `tanstack-start` cover the renderers. `directives`, `codegen` and `yaml` cover the spec language and its exports. The `devtools` family covers the inspector that drops into an app to show the spec tree, live state, dispatched actions and stream patches. Taken together they are enough for an agent to scaffold a catalog, wire a renderer and debug why one element is not rendering, without reading the source.

## Installation

The packages install from npm, and the README gives one line per target. A React app needs two:

```bash
npm install @json-render/core @json-render/react
```

Add the prebuilt component libraries if the catalog should start populated rather than empty:

```bash
npm install @json-render/shadcn
npm install @json-render/shadcn-svelte
```

The skills themselves install through skills.sh by repository and skill name, which is how the indexed listings are published:

```bash
npx skills add vercel-labs/json-render --skill react
npx skills add vercel-labs/json-render --skill core
```

For a Hermes profile, the manual route is a sparse clone plus a copy. Each skill is a single directory holding one `SKILL.md`, so nothing else has to travel with it:

```bash
git clone --depth 1 https://github.com/vercel-labs/json-render.git /tmp/json-render
cp -r /tmp/json-render/skills/react ~/.hermes/profiles/corpusiq/skills/
```

Install `core` first whichever route you take. Every renderer skill assumes the schema, catalog and spec vocabulary that `core` defines, and the renderer files spend their space on registry and provider wiring rather than on re-explaining the model.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| react | 17,580 | Turning JSON specs into React components: `@json-render/react`, component catalogs, rendering AI-generated specs. |
| core | 16,226 | Schemas, catalogs and AI prompt generation: `defineSchema`, `defineCatalog`, Spec and SpecStream, the vocabulary every other skill assumes. |
| codegen | 8,888 | Generating code from a UI spec: custom code exporters, spec traversal, prop serialisation for `@json-render/codegen`. |
| next | 8,592 | Rendering specs as full Next.js applications with routes, layouts, SSR and metadata. |
| devtools | 8,344 | The drop-in inspector: spec tree, runtime state editing, dispatched actions, live stream patches, catalog browsing, DOM pick to spec key. |
| directives | 8,062 | Prebuilt directives for formatting, math, string work and i18n: `$format`, `$math`, `$concat`, `$count`, `$truncate`, `$pluralize`, `$join`, `$t`. |
| mcp | 5,866 | MCP Apps integration, for servers that render interactive UI inside Claude, ChatGPT, Cursor or VS Code. |
| react-native | 3,220 | Native mobile UIs from the same specs, with mobile component catalogs. |
| shadcn | 2,489 | The 36 prebuilt shadcn/ui components (Radix UI plus Tailwind); indexed under the package name, directory `skills/json-render-shadcn`. |
| react-pdf | 2,335 | Rendering specs to PDF buffers, streams or files for documents. |
| react-three-fiber | 2,334 | 3D scenes from specs: meshes, lights, models, environments, including the GaussianSplat component. |
| zustand | 1,880 | Wiring json-render's StateStore to Zustand. |
| remotion | 1,757 | JSON timeline specs to video compositions and rendered video. |
| image | 1,558 | SVG and PNG output through Satori, for OG images and social cards. |
| remotion-best-practices | 1,538 | Remotion practice for the video renderer: composition structure and video creation in React. |
| vue | 1,397 | Vue 3 UIs from specs, Vue component registries and providers. |
| react-email | 1,388 | HTML or plain-text transactional and marketing email built from specs. |
| skill-creator | 1,349 | Writing a new skill or updating an existing one, which is how the catalog in this repo is maintained. |
| ink | 1,276 | Interactive terminal UIs from specs, with the built-in Ink components. |
| svelte | 1,213 | Svelte 5 component trees from specs, with runes-based reactivity. |

The remaining 18 indexed listings range from 17 to 1,136 installs.

## Why This Matters for Hermes Agents

An agent that renders UI from a prompt is one bad generation away from shipping something broken, and the usual failure is not visual. It is structural: a component that does not exist, a prop that does not match, an action nobody registered. json-render's answer is to make those failures impossible at the schema layer, which is precisely the property an agent needs, because an agent cannot look at a screenshot and decide the layout is wrong. It can, however, produce JSON that validates.

The second property is the streaming format. SpecStream is JSONL, one patch at a time, and the renderer applies patches as they arrive. For an agent that is generating a dashboard or a report card, that means the first frame appears while the model is still working, and a truncated stream still leaves valid UI on screen. The `core` skill documents the stream utilities alongside the schema, so the agent does not have to invent the transport.

The third is that the catalog is the contract. `defineCatalog` takes zod schemas for component props and a description per component, and that description is what goes into the prompt. So the quality of the generated UI is a function of how well the catalog is written, which is a reviewable artefact in the repository rather than a hidden prompt inside a framework. For a team that has to justify what the agent can and cannot emit, that is the difference between a policy and a hope.

## Usage

| You say | What happens |
|---|---|
| "Build a dashboard that renders from JSON instead of hardcoded JSX" | `core` sets up `defineSchema` and `defineCatalog` with zod prop schemas, `react` wires `defineRegistry` and `Renderer`, and the spec renders through the registry. |
| "Add the devtools panel, I cannot see why this element is blank" | `devtools` installs the framework-agnostic core plus the React, Vue, Svelte or Solid adapter, which shows the spec tree, state and stream patches and lets you pick a DOM element to find its spec key. |
| "Turn this spec into a Next.js app with routes and SSR" | `next` maps routes, layouts, SSR loaders and metadata out of the spec instead of rendering a single component. |
| "Generate OG images for every product page from the same data" | `image` renders SVG or PNG through Satori, so the same spec that drives a page produces the social card. |
| "Make a 30 second product video from this timeline" | `remotion` takes the JSON timeline spec and builds the Remotion composition; `remotion-best-practices` covers how to structure it. |
| "The same catalog should work in Vue and in React Native" | `vue` or `react-native` registers the matching renderer against the shared catalog, so component names and prop contracts stay identical. |
| "Let the model emit the report as a PDF" | `react-pdf` renders the spec to a buffer, stream or file, and `codegen` exports the spec as source if the output has to be checked in. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/vercel-labs/json-render/main/skills/react/SKILL.md
```

After a clone, confirm the skill count and that both halves of the framework are present:

```bash
git clone --depth 1 https://github.com/vercel-labs/json-render.git /tmp/json-render
ls /tmp/json-render/skills | wc -l
head -3 /tmp/json-render/skills/core/SKILL.md
grep -n '"name"' /tmp/json-render/packages/core/package.json | head -2
```

The count should print 31, `head` should show `name: core` with the schema and catalog description, and the package file should name `@json-render/core`. On a project that already installed the packages, the version check matters more than the file check, because the packages are released together:

```bash
npm ls @json-render/core @json-render/react
```

If those two lines disagree on version, pin them to the same one before debugging anything else. The `core` skill says exactly that for its experimental APIs, and the same advice holds for the stable ones.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react | Pass | Pass | Pass |
| core | Pass | Pass | Pass |
| codegen | Pass | Pass | Pass |

Three passes out of three is the reason this guide is green, and it matches what the repository contains: the skills are Markdown that documents the packages, and the packages are ordinary npm dependencies with zod as the schema layer.

The real security surface is the one the framework is designed around. A generative UI is a place where model output reaches a user's screen, and json-render limits that to components you registered and props that validate. Keep it that way: do not add a component that pipes a spec string into `dangerouslySetInnerHTML` or an arbitrary URL, because the catalog's guarantee stops at the component boundary. The `mcp` skill is the other place to look, since MCP Apps render UI inside Claude, ChatGPT, Cursor or VS Code, and that is a cross-origin surface where the spec and the host have to agree about what is allowed.

The `devtools` skill deserves a note too. Its SKILL.md states that the panel renders nothing when `process.env.NODE_ENV === "production"`, including when a bundler substitutes the expression. That is a deliberate production guard, and it argues for installing the devtools package as a development dependency rather than trusting the environment variable alone.

## Limitations

- Snapshot data, verified 2026-11-03: 105,845 combined installs across 38 indexed listings; 18,893 GitHub stars; Apache-2.0; last pushed 2026-11-03. Counts drift over time.
- The listings outnumber the skills. There are 38 indexed names and 31 directories under `skills/`, and several listings carry a copied description: `json-render-shadcn`, `json-render-react`, `json-render-core`, `json-render-remotion`, `json-render-image` and `json-render-react-email` all repeat the `codegen` text in the index. Match the package name, not the listing blurb.
- The `shadcn` listing has no directory of that name. Its content lives at `skills/json-render-shadcn`, and `shadcn-svelte` is a separate skill with a separate package.
- Installing the skills gives an agent documentation, not a working renderer. Every path here assumes a TypeScript project with the packages installed and a catalog defined; nothing in the skill set scaffolds an app.
- Version alignment is manual. The packages are published together and the `core` skill warns that experimental exports can change in any release, so pinning exact matching versions is the only safe default.
- Several skills are documentation for one package and read thin on their own. `remotion-best-practices` and `skill-creator` are general practice guides that happen to live in this repo, not part of the rendering model.

## Related

- [OpenUI Skill - Generative UI Setup](/hermes/skills/catalog/openui-setup)
- [Design Doc Mermaid Skill - Diagram & Documentation Setup](/hermes/skills/catalog/design-doc-mermaid-setup)
- [Archify - Interactive Architecture Diagram Skill Setup](/hermes/skills/catalog/archify-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Write the catalog before the prompt. The component descriptions in `defineCatalog` are what the model reads, so a vague description produces vague UI and no amount of prompt tuning fixes it.
- Install `core` and `devtools` even if the project only uses one renderer. The inspector answers "why is this element not rendering" in seconds, which is the question a generated spec raises most often.
- Keep every `@json-render/*` package on one version. The skills and the packages are released together, and a mixed install produces errors that look like schema bugs.
- Start from the 36 shadcn definitions when a catalog needs standard components, then write custom entries only for the parts that are genuinely yours.
- Use the YAML skill when a spec has to be edited by hand or streamed through an AI SDK transform. JSON is better for machines; the YAML wire format is easier to review in a pull request.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
