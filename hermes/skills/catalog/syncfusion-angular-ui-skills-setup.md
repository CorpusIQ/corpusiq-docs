---
title: "Syncfusion Angular UI Skills - Vendor Component Pack"
description: "syncfusion/angular-ui-components-skills: 17.6K combined installs. Official vendor skills for 65 Angular UI components, each with a reference folder."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/syncfusion-angular-ui-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "angular", "ui components", "syncfusion"]
---

# Syncfusion Angular UI Skills - Setup Guide

**Source:** [syncfusion/angular-ui-components-skills](https://www.skills.sh/syncfusion/angular-ui-components-skills) via skills.sh - 17.6K combined installs across 61 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [syncfusion/angular-ui-components-skills](https://github.com/syncfusion/angular-ui-components-skills) - 0 stars, no LICENSE at the repo root, branch master, last pushed 2026-10-23; 65 `SKILL.md` files, one per directory under `skills/`, each backed by a `references/` folder of per-feature documents

**Category:** Angular UI components from a commercial vendor: grids, charts, schedulers, editors, layout and theming

**Quality Tier:** 🟡 Yellow - the three sampled skills pass Gen Agent Trust Hub, Socket and Snyk, but the repository ships no LICENSE file at its root, so the terms for reuse are unstated

This is a vendor pack rather than a community one. Syncfusion publishes 65 skills for its Essential JS 2 Angular components, one per component family, versioned together at 34.1.29 and authored in the metadata as Syncfusion Inc. Each `SKILL.md` is a routing document: it states when to use the component, gives a quick start, then sends the agent to files under `references/` for the API surface, the feature guides and the known mistakes. The Grid skill, for example, points at separate references for 95+ properties, 137+ methods and 65+ events, plus a programmatic access guide covering the `@ViewChild` requirement and refresh patterns.

The content is written to stop an agent inventing APIs. The Chart skill states its own quality standards, including exact v33+ property names and a rule against guessing, and several skills open with an explicit trust boundary or a security section. The repository's GitHub description, which talks about agent prompts for organising capabilities, is generic boilerplate that does not describe the tree, so judge the pack from the skill files rather than the repo blurb.

## Installation

The README documents one command, and it is the skills CLI:

```bash
npx skills add syncfusion/angular-ui-components-skills -y
```

The README says the assistant then loads the skills automatically in supported IDEs, which it names as VS Code, Cursor and CodeStudio. The `-y` flag skips the confirmation prompt when the whole repository is installed. To read the files before installing, clone instead:

```bash
git clone --depth 1 https://github.com/syncfusion/angular-ui-components-skills.git /tmp/syncfusion-angular-ui-skills
cp -r /tmp/syncfusion-angular-ui-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

Installing the skills is not the same as installing the components. The skills document the component packages, and the packages come in through the vendor's own Angular schematics, both lines quoted from the Common skill:

```bash
ng add @syncfusion/ej2-angular-grids@latest
npm install @syncfusion/ej2-tailwind3-theme --save
```

The `syncfusion-angular-license` skill in the same pack covers the registration step that follows. It explains that key validation arrived in v20.1.0.47, that validation runs offline at startup with no network call, that a key is specific to a version and a platform or edition, and that the free community licence applies to organisations under 1M USD in revenue. Confirm the component licence with the vendor before shipping; the skill is documentation of that licence, not a grant of it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| syncfusion-angular-grid | 347 | Feature-rich data tables: sorting, filtering, aggregates, virtual scrolling, hierarchical grids and Excel or PDF export. |
| syncfusion-angular-common | 331 | Animation, drag and drop, state persistence, RTL, localization and the setup steps every other skill assumes. |
| syncfusion-angular-chart | 325 | 25+ series types, multiple axes, technical indicators, WebMCP tool registration and WCAG-compliant charts. |
| syncfusion-angular-license | 323 | Licence keys: generation, registration through `SYNCFUSION_LICENSE`, CI/CD wiring and the common validation errors. |
| syncfusion-angular-themes | 323 | Built-in themes, dark mode, CSS variables, icon sets, size modes and Theme Studio. |
| syncfusion-angular-rich-text-editor | 321 | HTML and Markdown WYSIWYG: toolbars, media insertion, mentions, slash menu, AI assist and Word or PDF round trips. |
| syncfusion-angular-tab | 320 | Responsive tabbed navigation with on-demand loading, drag reordering, state persistence and wizard patterns. |
| syncfusion-angular-scheduler | 320 | Calendar and event management: 11+ view modes, recurring events, resource grouping, timezones and ICS export. |
| syncfusion-angular-ai-assistview | 317 | Conversational UI against OpenAI, Gemini, Ollama or MCP providers, with chain-of-thought blocks and generative UI. |
| syncfusion-angular-treeview | 315 | Hierarchical trees with checkboxes, drag and drop, in-place editing, filtering and node templates. |
| syncfusion-angular-image-editor | 315 | Crop, annotate, filter, redact and transform images, with 16-step undo and 150+ localization keys. |
| syncfusion-angular-query-builder | 315 | Visual filter construction with AND/OR groups and import or export to JSON, SQL and MongoDB. |
| syncfusion-angular-gantt-chart | 315 | Project scheduling: task dependencies, critical path, resources, baselines and virtual scrolling. |
| syncfusion-angular-chat-ui | 314 | Messaging interfaces with attachments, typing indicators, mentions and Dialogflow or Bot Framework hooks. |
| syncfusion-angular-file-manager | 314 | File browsing and operations over a server API or client-side data, with virtualization and Docker providers. |
| syncfusion-angular-inline-ai-assist | 314 | Inline AI text editing with popup or inline responses, command presets, accept or reject actions and speech input. |
| syncfusion-angular-pivot-table | 313 | Pivot grids over OLAP or relational data: aggregation, calculated fields, drill-through and pivot charts. |
| syncfusion-angular-speech-to-text | 312 | Browser speech recognition with start and stop control, interim results, locale selection and cancel handling. |
| syncfusion-angular-diagram | 312 | Flowcharts, org charts, BPMN and UML on a canvas with layouts, ports, serialization and PNG or SVG export. |
| syncfusion-angular-dropdowntree | 312 | Hierarchical selection in a dropdown: checkboxes, parent-child sync, remote OData and item templates. |
| syncfusion-angular-treegrid | 312 | Hierarchical rows in a grid with mandatory `childMapping` rules, sorting, editing, aggregates and export. |

The remaining 40 indexed listings range from 259 to 310 installs. They are not stubs: every one of them is a real component directory covering a narrower surface, from maps and accumulation charts down to app bars and menus, so the threshold here only decides where the table stops. The index carries 61 listings while the tree carries 65 directories, which means four directories are not indexed at all and cannot be found by browsing skills.sh.

## Why This Matters for Hermes Agents

An agent asked to add a Syncfusion grid to an Angular app is working against an API it learned incompletely. The Grid alone exposes 137+ methods and 95+ properties, and a plausible-looking name from an older major version fails at compile time or, worse, silently does nothing. A vendor skill that carries the property tables into the context turns that guess into a lookup.

The reference-folder layout is the part other packs should copy. A single `SKILL.md` would have to choose between being too long to load and too thin to help; here the entry document stays short and names the specific reference for the specific job, so an agent working on grid events loads the events catalogue and nothing else.

Several of these skills also carry their own guardrails. The Grid and TreeGrid skills declare that they perform no remote data access and that API calls belong to a separate DataManager skill outside their trust boundary, and the Pivot Table skill opens with a data-source validation warning that names indirect prompt injection as a risk. When an agent is about to bind a table to a URL it found in a ticket, that warning is the sentence worth quoting back at it.

The licence skill earns its place for a different reason. Licence validation is the kind of failure that only appears in CI, and having the key model, the environment variable and the offline behaviour written down saves a debugging session that has nothing to do with the feature being built.

## Usage

| You say | What happens |
|---|---|
| "Add a data grid with paging, grouping and Excel export to this page" | `syncfusion-angular-grid` reads the properties and methods references and returns a standalone component with `GridModule` and only the services the features need. |
| "The chart legend property I copied does not exist in version 34" | `syncfusion-angular-chart` checks the exact name (`legendSettings`, not `legend`) against its reference set before rewriting the template. |
| "Our build prints a licence validation warning" | `syncfusion-angular-license` separates the licence key from the installer unlock key, then walks through `SYNCFUSION_LICENSE` and `npx syncfusion-license activate`. |
| "Make the app dark mode and match our brand colours" | `syncfusion-angular-themes` applies the `e-dark-mode` class and overrides the theme's CSS variables at runtime. |
| "We need a scheduler with resource grouping across two timezones" | `syncfusion-angular-scheduler` configures the timeline views, the resource data and the timezone handling, then explains the view services to inject. |
| "Turn this folder listing into a file browser with upload and rename" | `syncfusion-angular-file-manager` picks between `ajaxSettings` and client-side `fileSystemData` and returns the operation handlers. |
| "Build a pivot table over our OLAP cube with drill-through" | `syncfusion-angular-pivot-table` configures the axes and aggregation, and repeats its warning about validating the data source before binding. |

## Verification

The raw path for the Grid skill returned HTTP 200 on branch master when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} grid\n" \
  https://raw.githubusercontent.com/syncfusion/angular-ui-components-skills/master/skills/syncfusion-angular-grid/SKILL.md
```

Expect `200`. After the clone, confirm that the tree matches the directory count this guide claims and that the references arrived with each skill:

```bash
ls /tmp/syncfusion-angular-ui-skills/skills | wc -l
find /tmp/syncfusion-angular-ui-skills/skills -name SKILL.md | wc -l
ls /tmp/syncfusion-angular-ui-skills/skills/syncfusion-angular-grid/references | wc -l
```

Both counts should print 65, and the Grid references folder should hold at least six files, beginning with the properties, methods and events references. A count of one or two means the clone came down without the reference folders, and the skill will be missing the tables it exists to supply.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| syncfusion-angular-grid | Pass | Pass | Pass |
| syncfusion-angular-common | Pass | Pass | Pass |
| syncfusion-angular-chart | Pass | Pass | Pass |

Three samples out of 65 is thin coverage, and all three are the same kind of file: markdown plus reference markdown, no executable payload. The repository top level holds a README, an `apm.yml` manifest and the `skills/` directory, with no `package.json`, no install hooks and no scripts folder, so installing this pack cannot execute anything on its own. What an agent does after loading it is the exposure, and that is bounded by the prompt rather than by the pack.

The interesting security content is inside the skills. The Grid and TreeGrid skills claim no remote data access and push API calls to a separate DataManager skill, and the Pivot Table skill carries a data-source validation section that warns about indirect prompt injection, data exfiltration and code injection through untrusted sources. That is unusually direct for a vendor pack and worth keeping when the files are copied.

Two caveats belong here rather than in the limitations. There is no LICENSE file at the repository root, so the permissions for redistributing the skill text are unstated even though the sampled scanners are clean. And the components these skills document are commercial software under Syncfusion's own licence, which is a separate question from the skill files: the free community tier is scoped by revenue, and that scoping is described by the pack, not enforced by it.

## Limitations

- Snapshot data, verified 2026-11-01: 17,636 combined installs across 61 indexed listings; 0 GitHub stars; no LICENSE at the repo root; last pushed 2026-10-23. Counts drift over time.
- The index lists 61 skills but the tree holds 65 directories, so four skills are installable from the clone and invisible through skills.sh. This guide's table omits them without knowing which four they are.
- No licence file at the root. The scanner verdicts say the files are clean, not that they are free to redistribute, and this pack has no explicit grant to point at.
- The skills document a commercial product. A licence key is required for npm or trial installs, keys are version and edition specific, and the community tier is revenue-scoped, so a working copy of the skills does not mean a licensed application.
- Install counts sit between 259 and 347 across all 61 listings, a spread of 88, so rank order inside the table reflects a few dozen installs rather than clear preference.
- The repository has 0 stars and the README routes support to Syncfusion's ticket system and forums, so there is no community issue history to learn from when a skill's example does not match your version.

## Related

- [Angular Skills - Framework Development Setup](/hermes/skills/catalog/angular-skills-setup)
- [Ant Design Skills - Official antd Agent Suite Setup](/hermes/skills/catalog/ant-design-skills-setup)
- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by component, not by pack, if your IDE supports selection. Sixty-five skills is a lot of context for a project that uses a grid and a chart, and `npx skills add` against a single directory keeps the loader honest.
- Read the reference index before writing code. Every one of these skills names the file that answers the question you are about to guess at, and the Grid skill's programmatic API reference saves the most common mistake, forgetting `@ViewChild`.
- Pin the version you install against the version you compile. The skills carry 34.1.29 in their metadata and the Chart skill is explicit that property names changed at v33, so a stale copy plus a new package is a quiet source of errors.
- Wire the licence key into the build environment, not into a source file. The licence skill documents the environment variable route and the CI/CD variants, and a key committed to a repository is the one failure mode the scanners here cannot catch.
- Copy the trust-boundary paragraphs into your own project instructions. An agent that knows the Grid skill does not fetch remote data is less likely to invent a data source for it.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
