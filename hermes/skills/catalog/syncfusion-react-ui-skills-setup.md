---
title: "Syncfusion React UI Skills - Component Suite Setup"
description: "syncfusion/react-ui-components-skills: 42.9K combined installs. Sixty-five React UI skills with official APIs, props and per-component reference docs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/syncfusion-react-ui-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "react", "ui components", "syncfusion"]
---

# Syncfusion React UI Skills - Setup Guide

**Source:** [syncfusion/react-ui-components-skills](https://www.skills.sh/syncfusion/react-ui-components-skills) via skills.sh - 42.9K combined installs across 62 indexed listings; first seen 2026-11-02 (morning sweep)

**GitHub:** [syncfusion/react-ui-components-skills](https://github.com/syncfusion/react-ui-components-skills) - 3 stars, no `LICENSE` file in the repository root (the only licence statement is `license: Syncfusion Inc` inside `apm.yml`), branch master, last pushed 2026-10-23; 65 `SKILL.md` directories under `skills/`, each with a `references/` folder of feature-level documents, 1,115 Markdown files and 16 MB under `skills/`

**Category:** React UI component guidance for agents: Syncfusion grids, charts, schedulers and forms with API references

**Quality Tier:** 🟡 Yellow - all five sampled verdicts are Pass on Gen Agent Trust Hub and Snyk with one Socket Warn, and the README is unusually precise about what each skill covers, but the repository ships no `LICENSE` file and carries 3 stars, so this reads as vendor documentation rather than reviewed software

Syncfusion publishes this as the agent-facing arm of its React component library: 65 Markdown skill directories that teach an assistant the real props, events and methods of the EJ2 React wrappers instead of letting it guess. Each skill is self-contained, a `SKILL.md` with the core patterns plus a `references/` folder split by feature area, and each `SKILL.md` carries a `metadata.version` of 34.1.29, so the guidance is pinned to a component release rather than to "latest". The README states the intended workflow plainly: the assistant loads the skill that matches the question, extracts the APIs and patterns, generates code with the right imports and types, then applies the suite's theming and accessibility rules.

The catalogue covers the whole vendor surface, not only the famous controls: grids, tree grids, pivot tables, schedulers, Gantt, charts, accumulation charts, gauges, maps, diagrams, the rich text editor, image editor, file manager, Kanban, chat UI, AI AssistView, barcode, dashboard layout and tabs, plus utility skills for theming, shared features and licence keys. The install counts sit in a single tight band from 552 to 835, a spread narrow enough that the numbers read as one suite installed together rather than 62 components chosen one at a time.

## Installation

The README documents one install command, and it installs every skill in the repository:

```bash
npx skills add syncfusion/react-ui-components-skills -y
```

`apm.yml` at the repository root is an APM package manifest, but it carries metadata only: package name `react-ui-components-skills`, version, description, author, keywords and `license: Syncfusion Inc`. It declares no dependencies and no install command, and the README documents no plugin marketplace or per-skill install, so the `npx skills add` line above is the whole documented path.

For a Hermes profile, the copy route is the reliable one, because nothing in the repository mentions Hermes and the skills are plain directories:

```bash
git clone https://github.com/syncfusion/react-ui-components-skills.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r react-ui-components-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

To update a copy, run `git -C react-ui-components-skills pull` and copy again. There is no build step and nothing to compile: the repository holds 1,116 Markdown files and one YAML manifest, and no script, package or binary that runs on clone.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| syncfusion-react-grid | 835 | Data tables: sorting, filtering, grouping, aggregates, editing and CRUD, virtual and infinite scrolling, hierarchy grids, Excel and PDF export, state persistence. |
| syncfusion-react-scheduler | 795 | Calendar and appointment scheduling: Day, Week, Month, Timeline, Agenda and Year views, resources, recurring events, drag-and-drop, timezone-aware CRUD. |
| syncfusion-react-gantt-chart | 784 | Project scheduling: GanttComponent setup, task constraints, taskbar customization, predecessors, milestones, critical path, baselines, resource view, Excel and PDF export. |
| syncfusion-react-rich-text-editor | 768 | WYSIWYG and Markdown editing: toolbar setup, image, video and audio insertion, paste cleanup, mentions, slash menu, Word and PDF import and export, source view. |
| syncfusion-react-charts | 760 | Statistical charts: axes and series configuration, user interactions, financial indicators, accessibility, styling for dashboards. |
| syncfusion-react-treegrid | 757 | Hierarchical grids: sorting, filtering, editing, paging, aggregates, templates, virtual scrolling and performance tuning. |
| syncfusion-react-common | 743 | Shared plumbing for the suite: animation, drag and drop, state persistence, RTL, localization and globalization, templates, security. |
| syncfusion-react-themes | 740 | Theming: built-in themes, dark mode, CSS variables, icons, size modes, Theme Studio integration. |
| syncfusion-react-file-manager | 740 | File browsing and management: upload and download, create, delete and rename, multiple views, drag and drop, local and remote file systems. |
| syncfusion-react-diagram | 730 | Diagrams: nodes and connectors, flowcharts, org charts, BPMN and UML models, ER diagrams, layout algorithms, swimlanes, symbol palettes. |
| syncfusion-react-license | 729 | Syncfusion licensing: key generation, registration and validation, trial keys, CI/CD registration, edition and platform licensing models. |
| syncfusion-react-image-editor | 729 | Image editing: text, shape and freehand annotations, filters, layer management, PNG, JPEG, SVG, WEBP and BMP support. |
| syncfusion-react-tabs | 726 | Tabbed interfaces: content rendering, header positioning, drag-and-drop reordering, styling, localization, accessible tab interaction. |
| syncfusion-react-kanban | 726 | Kanban boards: drag-and-drop cards, swimlanes, WIP limit validation, card templates, event handling, API data binding. |
| syncfusion-react-chat-ui | 726 | Chat interfaces: message rendering, file attachments, typing indicators, conversation layout, theming, real-time updates. |
| syncfusion-react-ai-assistview | 723 | AI chat surfaces: conversation flow, speech input and output, attachments, chain-of-thought display, generative UI tools, telemetry, OpenAI and Azure AI wiring. |
| syncfusion-react-barcode | 722 | Barcode and QR generation: Code39, Code128, Data Matrix, styling, SVG or canvas rendering, export and print. |
| syncfusion-react-accumulation-chart | 722 | Pie, doughnut, funnel and pyramid charts: data labels, legends, grouping, smart labels, drill-down, explode effects, export and print. |
| syncfusion-react-pivot-table | 720 | Pivot tables: OLAP aggregation, JSON and remote binding, drill-down and drill-through, grouping, filtering, conditional formatting, Excel, PDF and CSV export, pivot charts. |
| syncfusion-react-dashboard-layout | 720 | Dashboard layouts: draggable and resizable panels, responsive grids, floating panel arrangement, state management. |

The remaining 42 indexed listings range from 552 to 719 installs, from syncfusion-react-maps and syncfusion-react-query-builder at 719 down to syncfusion-react-calendars at 552; they carry the rest of the catalogue, including gauges, heatmaps, treemaps, sparklines, splitter, stepper and menu.

## Why This Matters for Hermes Agents

Component libraries are where an agent's confident guess is most expensive. A React grid written from memory produces prop names that look right, an `onChange` that does not exist on that component, and a feature list the control never had. This pack replaces the guess with the vendor's own API surface: each skill carries the props, events and methods for one component family, split into reference documents by feature, so the agent can read exactly the page that covers grouping or virtual scrolling instead of inventing an API.

The split between `SKILL.md` and `references/` matches how an agent actually loads context. The description in the frontmatter is enough to route a request, the skill body carries the setup pattern and the navigation table, and the reference file is read only for the follow-up question. The React grid skill ships 42 reference documents, which is a size no agent should load whole, and progressive disclosure is the reason the pack stays usable.

Version pinning is the quiet benefit. Every `SKILL.md` in this repository declares `metadata.version: 34.1.29`, so when a generated snippet fails, the first question has an answer: the guidance matches a specific component release, and a package bumped past it needs the skill refreshed rather than the model second-guessed.

The utility skills do the work that usually goes missing. `syncfusion-react-common` covers the cross-cutting features (drag and drop, RTL, localization, state persistence) that break silently when a component is generated in isolation, and `syncfusion-react-license` covers key registration and validation, which is the failure that shows up as a watermark or a console error after the code looks correct.

## Usage

| You say | What happens |
|---|---|
| "Add grouping, aggregates and Excel export to this grid" | syncfusion-react-grid answers with the Grid prop and event set for grouping, the aggregate types, and the export call, plus the reference page for each. |
| "Build a week-view scheduler with resources and recurring events" | syncfusion-react-scheduler grounds the view configuration, resource fields, recurrence rule and drag-and-drop handlers. |
| "Why does my chart throw when I set the axis type" | syncfusion-react-charts answers from the axis and series reference rather than from the model's memory of another chart library. |
| "Wire this rich text editor to import a Word document" | syncfusion-react-rich-text-editor covers the import and export path, toolbar setup and the paste cleanup behaviour. |
| "Set the licence key in CI so the build stops warning" | syncfusion-react-license walks through key registration for the pipeline and the validation errors that follow a wrong edition. |
| "Make the theme dark and shrink the icons" | syncfusion-react-themes answers with the theme switch, CSS variable overrides, size modes and the icon library rules. |
| "Add an AI chat panel to this dashboard" | syncfusion-react-ai-assistview covers conversation flow, streaming display, attachments and the OpenAI or Azure AI wiring behind it. |

## Verification

The raw paths below returned 200 on branch master when this guide was written on 2026-11-02. They are the fastest way to read a skill before installing it:

```bash
for p in syncfusion-react-grid syncfusion-react-scheduler syncfusion-react-charts; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/syncfusion/react-ui-components-skills/master/skills/$p/SKILL.md"
done
```

After a clone, confirm the tree instead of trusting the index. The repository holds 65 skill directories against 62 indexed listings:

```bash
git clone --depth 1 https://github.com/syncfusion/react-ui-components-skills.git /tmp/react-ui-components-skills
find /tmp/react-ui-components-skills/skills -name SKILL.md | wc -l
head -6 /tmp/react-ui-components-skills/skills/syncfusion-react-grid/SKILL.md
ls /tmp/react-ui-components-skills/skills/syncfusion-react-grid/references | wc -l
```

The counts should print 65 for `SKILL.md` files and 42 for the grid reference documents. The `head` output should show the `name`, `description` and `metadata.version` frontmatter, which is what the agent routes on. Replace `/tmp/react-ui-components-skills` with the path you copied into the Hermes profile skills directory when you verify an installed set.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| syncfusion-react-grid | Pass | Pass | Pass |
| syncfusion-react-ai-assistview | Pass | Warn | Pass |
| syncfusion-react-dropdowns | Pass | Pass | Pass |
| syncfusion-react-3d-circular-chart | Pass | Pass | Pass |
| syncfusion-react-calendars | Pass | Pass | Pass |

Four of the five sampled listings pass all three scanners, and `syncfusion-react-ai-assistview` carries the single Socket Warn. No sampled listing fails Gen Agent Trust Hub, which is the scan that inspects what a skill actually instructs an agent to do, and the whole repository is 1,116 Markdown files plus one YAML manifest, so there is no code path that executes on install.

The repository ships no `LICENSE` file. The only licence statement anywhere in the tree is the field `license: Syncfusion Inc` inside `apm.yml`, which names the vendor without granting terms. Treat the content as vendor documentation under Syncfusion's own terms rather than as open source, and read those terms before redistributing the skill text or shipping it in a product.

The runtime obligation is separate from the file licence: the React components themselves are commercial Syncfusion controls, licensed by key, and the skills only document how to generate and register that key. Copying the skills does not grant a component licence, and the community licence route lives on the Syncfusion site rather than in this repository.

The residual risk is guidance rather than execution. An agent that follows an outdated skill will write code for version 34.1.29 APIs against a newer package, and the failure will look like a bug in the operator's app. Pin the package and the skill together, or refresh the copy when the package moves.

## Limitations

- Snapshot data, verified 2026-11-02: 42,927 combined installs across 62 indexed listings; 3 GitHub stars; no licence file (only `license: Syncfusion Inc` in `apm.yml`); last pushed 2026-10-23. Counts drift over time.
- No `LICENSE` file exists in the repository root, and `apm.yml` names the vendor without a grant. The terms for reuse of the skill text are not stated in the repository.
- The index and the tree disagree in one direction: 62 listings against 65 directories. `syncfusion-react-form-builder`, `syncfusion-react-form-renderer` and `syncfusion-react-modern-rich-text-editor` are in the tree and installed by the CLI, but carry no install count on skills.sh.
- The install counts span 552 to 835, a band narrow enough that the figures look like whole-suite installs rather than per-component adoption. Read them as repository traffic, not as demand for each control.
- The security sample is five skills out of 65, so the remaining 60 are unaudited by that sample; only `syncfusion-react-ai-assistview` shows a warn within it.
- The guidance is version-tagged: every `SKILL.md` declares `metadata.version: 34.1.29`. A package upgrade without a fresh copy leaves the agent describing an older API surface.

## Related

- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [Extract Design System - UI Token & Component Extraction Setup](/hermes/skills/catalog/extract-design-system-setup)
- [Tailwind 4 Docs Skill - Local Docs Snapshot Setup](/hermes/skills/catalog/tailwind-4-docs-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole suite rather than the one component you need today. The counts show the suite is installed as a unit, and the utility skills (`common`, `themes`, `license`) are the ones that keep a single generated component from breaking at the edges.
- Read `SKILL.md` first and only open `references/` for the feature in question. The grid skill has 42 reference documents, and loading them all is how a context window gets spent on grouping docs for a chart question.
- Keep the version field in view. Ask the agent which `metadata.version` the installed skill declares before debugging a generated snippet against a newer npm package.
- Put the licence skill in front of any build work. Key registration in CI is a five-minute task with the skill and an afternoon of console errors without it.
- When an answer looks too generic, name the component explicitly in the request. The descriptions trigger on component names, and routing is what selects the right skill out of 65.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
