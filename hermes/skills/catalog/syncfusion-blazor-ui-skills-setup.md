---
title: "Syncfusion Blazor UI Skills - Component Suite Setup"
description: "syncfusion/blazor-ui-components-skills: 23.8K combined installs. Sixty-nine Blazor component skills for Server, WebAssembly and Hybrid apps."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/syncfusion-blazor-ui-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "blazor", "dotnet", "ui components"]
---

# Syncfusion Blazor UI Skills - Setup Guide

**Source:** [syncfusion/blazor-ui-components-skills](https://www.skills.sh/syncfusion/blazor-ui-components-skills) via skills.sh - 23.8K combined installs across 66 indexed listings; first seen 2026-11-02 (morning sweep)

**GitHub:** [syncfusion/blazor-ui-components-skills](https://github.com/syncfusion/blazor-ui-components-skills) - 4 stars, no `LICENSE` file in the repository root (the only licence statement is `license: Syncfusion Inc` inside `apm.yml`), branch master, last pushed 2026-10-20; 69 `SKILL.md` directories under `skills/`, each with a `references/` folder of feature-level documents, 1,007 Markdown files under `skills/` and 17 MB in total

**Category:** Blazor UI component guidance for agents: Server, WebAssembly and Hybrid hosting with grids, charts and forms

**Quality Tier:** 🟡 Yellow - four of the five sampled verdicts pass all three scanners with one Socket Warn on the file manager skill, and the README states its prerequisites and hosting models clearly, but the repository ships no `LICENSE` file and carries 4 stars, so this is vendor documentation rather than reviewed software

This is the Blazor arm of Syncfusion's agent skills: 69 Markdown skill directories that teach an assistant the real APIs of the `Syncfusion.Blazor.*` component packages, written for every hosting model the framework supports. The README names them explicitly, Server, WebAssembly, Hybrid and Auto, and the skill descriptions follow through, with the data grid skill noting that its patterns apply to Blazor Server, WebAssembly, Web App and MAUI. Each skill is a `SKILL.md` with the core patterns plus a `references/` folder split by feature area, so a question about exporting the grid to Excel resolves to one reference document rather than the whole component.

The suite covers the component catalogue rather than a sample of it: data grid, tree grid, pivot table, data form, scheduler, Gantt, charts, accumulation and stock charts, gauges, maps, diagram, rich text editor, file manager, dropdowns, inputs, buttons, calendars, popups, notifications and layout controls, plus three utilities that matter more than their install counts suggest: `common` for project setup and service registration, `themes` for Theme Studio and Sass overrides, and `license` for key handling. The install counts span 252 to 450, a band narrow enough that the figures read as a suite installed as one package.

## Installation

The README documents two routes. The recommended one passes the full repository URL rather than the owner and repo shorthand:

```bash
npx skills add https://github.com/syncfusion/blazor-ui-components-skills
```

The README's manual route clones the repository and adds it as a second root folder in a VS Code workspace file, which is how the author expects an editor to pick the skills up:

```bash
git clone https://github.com/syncfusion/blazor-ui-components-skills.git
```

```json
{
  "folders": [
    { "path": "/path/to/your-blazor-app" },
    { "path": "/path/to/blazor-ui-components-skills" }
  ]
}
```

`apm.yml` at the repository root is an APM package manifest with metadata only: package name `blazor-ui-components-skills`, version, description, author, keywords and `license: Syncfusion Inc`. It declares no dependencies and no install command, and there is no Claude Code plugin marketplace line in the README, so those two routes are the whole documented path.

For a Hermes profile, copy the skill directories in directly. Nothing in the repository mentions Hermes, and the skills are plain folders:

```bash
git clone https://github.com/syncfusion/blazor-ui-components-skills.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r blazor-ui-components-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

To update, run `git -C blazor-ui-components-skills pull` and copy again. The repository holds 1,008 Markdown files and one YAML manifest, with no script, package or binary that runs on clone. The README's prerequisites sit outside the skills: an AI coding assistant that reads context files, the .NET 8 SDK or later, a Syncfusion licence key, and working knowledge of at least one Blazor hosting model.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| syncfusion-blazor-datagrid | 450 | SfGrid tabular work: sorting, filtering, paging, grouping, editing, aggregates, virtualization, lazy-load grouping, row and column spanning, Excel and PDF export, state persistence, Server, WebAssembly, Web App and MAUI. |
| syncfusion-blazor-common | 416 | Project setup: project creation, NuGet packages, service registration, script loading, bUnit testing, localization and globalization. |
| syncfusion-blazor-dropdowns | 408 | The dropdown family: AutoComplete, ComboBox, DropDownList, MultiSelect and ListBox, with data binding, filtering, cascading dropdowns and templates. |
| syncfusion-blazor-charts | 402 | SfChart: 30+ chart types including line, bar and column, area, financial, scatter, bubble, candlestick, waterfall, histogram and polar. |
| syncfusion-blazor-popups | 401 | Dialogs: modal and modeless windows, confirmations, custom forms, positioning, animations, accessibility. |
| syncfusion-blazor-license | 394 | Licence keys: generate, register, secure, validate and troubleshoot across Blazor project types. |
| syncfusion-blazor-themes | 393 | Theming: Theme Studio colour customization, CSS and SCSS integration, lightweight themes, component filtering, Sass variable overrides. |
| syncfusion-blazor-inputs | 391 | Inputs: FileUpload, TextBox, NumericTextBox, TextArea, Signature, RangeSlider, OtpInput, Rating, InputMask, ColorPicker, with validation and events. |
| syncfusion-blazor-scheduler | 389 | Scheduling: day, week, month, timeline and agenda views, drag and drop, resizing, resources, timezone-aware recurring events and CRUD. |
| syncfusion-blazor-datamanager | 386 | SfDataManager: UrlAdaptor, ODataAdaptor, WebApiAdaptor and GraphQLAdaptor, custom binding with DataAdaptor, DataManagerRequest and DataOperations. |
| syncfusion-blazor-accumulation-chart | 383 | Pie, doughnut, funnel and pyramid charts: data labels, legends, tooltips, slice grouping, part-to-whole layouts. |
| syncfusion-blazor-calendars | 382 | Calendar, DatePicker, DateRangePicker, DateTimePicker and TimePicker: date constraints, formatting, globalization, accessible date input. |
| syncfusion-blazor-buttons | 381 | The button family: Button, ButtonGroup, CheckBox, Chip, DropdownMenu, FloatingActionButton, ProgressButton, SpeedDial, SplitButton, ToggleSwitch. |
| syncfusion-blazor-diagram | 379 | SfDiagramComponent: flowcharts, org charts, mind maps, BPMN, UML sequence, swimlanes, symbol palettes, layouts, serialization, export and print. |
| syncfusion-blazor-rich-text-editor | 377 | SfRichTextEditor: HTML, Markdown and IFrame modes, toolbar configuration, media and table insertion, paste cleanup, Word and PDF import and export, RTL. |
| syncfusion-blazor-dataform | 376 | DataForm: dynamic data-bound forms, validation, FormItems and FormAutoGenerateItems, templates, events, data annotation validation. |
| syncfusion-blazor-file-manager | 376 | FileManager: hierarchical file systems, file operations, data binding patterns, cloud provider integration. |
| syncfusion-blazor-security | 376 | Content Security Policy for Blazor Server, WebAssembly and Auto render modes, self-hosted and CDN scenarios. |
| syncfusion-blazor-pivot-table | 375 | PivotView: OLAP analysis, aggregation, drill-down and drill-through, grouping, filtering, conditional formatting, Excel, PDF and CSV export, pivot charts. |
| syncfusion-blazor-gantt-chart | 375 | SfGantt: GanttTaskFields, GanttColumns, GanttEditSettings, taskbar editing, dependencies, resources, timeline, critical path, baselines, Excel and PDF export. |
| syncfusion-blazor-notifications | 375 | Toast, Message and Skeleton: toasts, alert boxes, success and error messages, loading skeletons, shimmer placeholders. |

The remaining 45 indexed listings range from 252 to 374 installs, from syncfusion-blazor-treegrid at 374 down to syncfusion-blazor-chart-wizard at 252; they carry the rest of the catalogue, including toolbars, menus, carousels, gauges, heatmaps, maps, stepper and splitter.

## Why This Matters for Hermes Agents

Blazor is the framework where an agent's guesswork is hardest to spot. C# component parameters are typed, so a wrong property name fails at compile time, but the failures that cost hours are the quiet ones: a service that was never registered, a script that was never loaded, a data adaptor that returns the right shape and the wrong events. `syncfusion-blazor-common` exists for exactly those, covering project creation, NuGet packages, service registration, script loading and bUnit testing, and it is the second most installed skill in the suite for a reason.

The hosting model is the second trap. The same component behaves differently across Server, WebAssembly, Hybrid and Auto, and the descriptions keep that context in view: the data grid skill names all four models plus MAUI, and `syncfusion-blazor-security` covers the Content Security Policy differences between render modes. An assistant that has read the skill routes the question through the right model instead of handing a WebAssembly pattern to a Server app.

The routing hints are unusually good. Each `SKILL.md` frontmatter carries a description written for triggering, and the sharper ones include negative routing: the pivot table skill says Blazor-only, not React, Angular, Vue or JavaScript. For a Hermes agent working across several Syncfusion suites, that sentence is the difference between reading the right skill and a near-miss.

The suite also stops at the boundary an agent should not cross alone. `syncfusion-blazor-dataform` covers model validation through data annotations rather than inventing a validation layer, `syncfusion-blazor-datamanager` covers the adaptors rather than hand-rolled HTTP, and the security skill covers CSP rather than leaving the agent to guess which CDN host the components need.

## Usage

| You say | What happens |
|---|---|
| "Set up a Blazor WebAssembly project with Syncfusion components registered" | syncfusion-blazor-common answers with project creation, NuGet packages, service registration and script loading, in the order the template needs them. |
| "Add grouping and Excel export to this DataGrid" | syncfusion-blazor-datagrid grounds the grid parameters, the aggregate configuration and the export call, with the reference page for each. |
| "Why does my scheduler not fire the event on drag" | syncfusion-blazor-scheduler covers the drag-and-drop and resize events, the resource fields and the CRUD handlers behind them. |
| "Configure CSP so the components load from the CDN" | syncfusion-blazor-security answers per render mode, self-hosted or CDN, with the host entries the policy needs. |
| "Build a pivot table over an OData feed" | syncfusion-blazor-pivot-table covers OLAP aggregation, the data binding path and the export formats. |
| "Make this DataForm validate with my model attributes" | syncfusion-blazor-dataform walks through data annotation validation, FormItems and the auto-generated field setup. |
| "Set the licence key for this project" | syncfusion-blazor-license covers key registration per project type and the validation error that follows a wrong key. |

## Verification

The raw paths below returned 200 on branch master when this guide was written on 2026-11-02, and they are the fastest way to read a skill before installing it:

```bash
for p in syncfusion-blazor-datagrid syncfusion-blazor-common syncfusion-blazor-security; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/syncfusion/blazor-ui-components-skills/master/skills/$p/SKILL.md"
done
```

After a clone, count the tree rather than trusting the index, which carries 66 listings against 69 directories:

```bash
git clone --depth 1 https://github.com/syncfusion/blazor-ui-components-skills.git /tmp/blazor-ui-components-skills
find /tmp/blazor-ui-components-skills/skills -name SKILL.md | wc -l
head -4 /tmp/blazor-ui-components-skills/skills/syncfusion-blazor-datagrid/SKILL.md
ls /tmp/blazor-ui-components-skills/skills/syncfusion-blazor-datagrid/references | wc -l
```

The counts should print 69 for `SKILL.md` files and 49 for the grid reference documents. The `head` output should show the `name` and `description` frontmatter, which is what the assistant matches on. One directory name needs care: the data form skill lives in `skills/syncfusion-blazor-data-form/` while its frontmatter `name` is `syncfusion-blazor-dataform`, so a path check based on the install listing will miss it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| syncfusion-blazor-datagrid | Pass | Pass | Pass |
| syncfusion-blazor-file-manager | Pass | Warn | Pass |
| syncfusion-blazor-smart-textarea | Pass | Pass | Pass |
| syncfusion-blazor-listview | Pass | Pass | Pass |
| syncfusion-blazor-chart-wizard | Pass | Pass | Pass |

Four of the five sampled listings pass all three scanners, and `syncfusion-blazor-file-manager` carries the single Socket Warn. No sampled listing fails Gen Agent Trust Hub, the scan that inspects what a skill instructs an agent to do, and the repository holds 1,008 Markdown files plus one YAML manifest, so nothing executes on install.

The repository ships no `LICENSE` file. The only licence statement in the tree is `license: Syncfusion Inc` inside `apm.yml`, which names the vendor without granting terms, so treat the skill text as vendor documentation under Syncfusion's own conditions rather than as open source.

Two obligations sit outside the file licence. The Blazor components are commercial Syncfusion controls licensed by key, and the skills document key registration without granting one; the README points at the free community licence as a route. And the folder is one the file manager skill instructs an agent to integrate with cloud providers, so the trust question there is about the credentials an operator hands a Blazor app, not about the Markdown.

The residual risk is version drift. A skill written against one component release can describe parameters that a newer `Syncfusion.Blazor.*` package has renamed, and the failure shows up as a compile error in the operator's project.

## Limitations

- Snapshot data, verified 2026-11-02: 23,778 combined installs across 66 indexed listings; 4 GitHub stars; no licence file (only `license: Syncfusion Inc` in `apm.yml`); last pushed 2026-10-20. Counts drift over time.
- No `LICENSE` file exists in the repository root. The reuse terms for the skill text are not stated in the repository, and `apm.yml` only names the vendor.
- The index and the tree disagree in both directions: 66 listings against 69 directories. `syncfusion-blazor-dataform` is indexed but its directory is `data-form/`, and `inline-ai-assist`, `sunburst-chart` and `tabs` are in the tree with no install count on skills.sh.
- The README says the repository contains "50+ AI-ready skill guides" while the tree holds 69 directories, so the README figure is a floor rather than a count. The install index sits in between at 66.
- The security sample is five skills out of 69, so 64 remain unaudited by that sample; only `syncfusion-blazor-file-manager` shows a warn within it.
- The prerequisites are real: the .NET 8 SDK or later, a Syncfusion licence key and a host assistant that reads context files. The skills guide Blazor development, they do not supply the components, the key or the SDK.

## Related

- [Aaronontheweb Dotnet Skills - Akka.NET Suite](/hermes/skills/catalog/aaronontheweb-dotnet-skills-setup)
- [Dotnet Skills - .NET AI Coding Setup](/hermes/skills/catalog/dotnet-skills-setup)
- [Microsoft Learn MCP Skills Setup](/hermes/skills/catalog/microsoft-learn-mcp-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the three utility skills, not the component you came for. `common` sets up registration and script loading, `themes` sets the styling path, `license` stops the watermark, and every component skill assumes that ground is prepared.
- Name the hosting model in your request. "Blazor Server" and "Blazor WebAssembly" produce different answers for security, data access and prerendering, and the descriptions are written to route on it.
- Read `SKILL.md` before `references/`. The grid skill's 49 reference documents are useful one at a time and wasteful as a set.
- Check the directory name before scripting an install check. `syncfusion-blazor-data-form` is the folder, `syncfusion-blazor-dataform` is the skill name, and an index-driven path will not find it.
- Treat the pivot table skill as the routing example: it states which frameworks it is not for. Ask the agent which sibling skill a question belongs to when a component has near neighbours.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
