---
title: "Syncfusion MAUI UI Skills - Component Suite Setup"
description: "syncfusion/maui-ui-components-skills - 16.8K combined installs across 81 indexed listings: Syncfusion .NET MAUI skills for DataGrid, charts, and more."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/syncfusion-maui-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "maui", "dotnet", "ui components"]
---

# Syncfusion MAUI UI Skills - Setup Guide

**Source:** [syncfusion/maui-ui-components-skills](https://www.skills.sh/syncfusion/maui-ui-components-skills) via skills.sh - 16.8K combined installs across 81 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 62 stars, no LICENSE file, `master` branch, last pushed 2026-10-27, `SKILL.md` files under `skills/syncfusion-maui-<control>/` each with a `references/` folder of feature-level documents
**Category:** .NET MAUI UI component guidance for agents - DataGrid, charts, scheduler, editors, and navigation controls
**Quality Tier:** 🟡 Yellow - all sampled verdicts pass the Gen Agent Trust Hub with one Socket Warn on syncfusion-maui-combobox, but the repository ships no LICENSE file.

This is the .NET MAUI arm of Syncfusion's agent skills: one skill per control family that teaches the real APIs of the `Syncfusion.Maui.*` packages. Each skill is a `SKILL.md` with When to Use, Component Overview, and navigation links, plus a `references/` folder split into getting-started, advanced-features, and troubleshooting documents, so a follow-up question about exporting the grid to Excel resolves to one reference file rather than the whole component.

The catalogue spans DataGrid, charts, scheduler, editors, inputs, layout and navigation controls, plus three utilities that matter more than their install counts suggest: getting-started for project setup and licensing, migration for Xamarin.Forms upgrades, and theming for Material and Cupertino styling. The README states 76 skill guides, the install index lists 81, and the tree holds 81 directories; the repository ships no LICENSE file, so the skill text is vendor documentation rather than open source.

## Installation

The recommended route passes the full repository URL:

```bash
npx skills add https://github.com/syncfusion/maui-ui-components-skills
```

The README's manual route clones the repository and adds it as a second root folder in a VS Code workspace file:

```bash
git clone https://github.com/syncfusion/maui-ui-components-skills.git
```

No configuration is required after that; the assistant detects and loads the relevant skill from the workspace. Prerequisites live outside the skills: an AI coding assistant that reads context files, the .NET 9 SDK, and a Syncfusion license key (a free community licence is available).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| syncfusion-maui-parallax-view | 232 | Parallax scrolling where the background moves slower than the foreground, for ScrollView and ListView. |
| syncfusion-maui-cartesian-charts | 229 | Cartesian Chart (SfCartesianChart): 20+ chart types including line, area, column, bar and financial. |
| syncfusion-maui-button | 228 | Button (SfButton): icons, visual states, Liquid Glass, RTL, and checkable buttons. |
| syncfusion-maui-listview | 227 | ListView (SfListView): lists, selection, swipe actions, pull-to-refresh, and drag-drop items. |
| syncfusion-maui-combobox | 226 | ComboBox (SfComboBox): editable and searchable dropdowns, multi-select, and AI-powered smart search. |
| syncfusion-maui-picker | 224 | Picker (SfPicker): multi-column and dialog pickers, data binding, and accessibility. |
| syncfusion-maui-popup | 223 | Popup (SfPopup): alerts, custom views, modal dialogs, positioning, and animations. |
| syncfusion-maui-date-picker | 223 | DatePicker (SfDatePicker): date selection, formatting, restrictions, and dialog modes. |
| syncfusion-maui-datagrid | 223 | DataGrid (SfDataGrid): tabular data, sorting, filtering, grouping, and Excel/PDF export. |
| syncfusion-maui-checkbox | 223 | CheckBox (SfCheckBox): three-state and indeterminate states, groups, and visual states. |
| syncfusion-maui-tab-view | 222 | Tab View (SfTabView): tab navigation, nested tabs, swipe gestures, and Liquid Glass indicators. |
| syncfusion-maui-chips | 221 | Chips (SfChip/SfChipGroup): tags, selection and filter chips, and data binding. |
| syncfusion-maui-ai-assistview | 221 | AI AssistView (SfAIAssistView): AI chat interfaces, conversation flows, and AI suggestions. |
| syncfusion-maui-text-input-layout | 221 | Text Input Layout (SfTextInputLayout): floating labels, helper text, validation, and password toggle. |

The remaining 67 indexed listings range from 41 to 219 installs.

## Why This Matters for Hermes Agents

MAUI is a framework where the agent's mistake is usually quiet, not loud. C# component parameters are typed, so a wrong property name fails at compile time, but the failures that cost hours are the ones that compile: a NuGet package never registered, a service never added in MauiProgram.cs, a licence key never set. The getting-started skill exists for exactly those, covering installation, licensing, themes and AI service integration in one place.

The frontmatter descriptions are written for triggering. Each SKILL.md names the control and the scenarios that should activate it, so asking about the DataGrid loads the DataGrid skill rather than the general catalogue. The references/ folder keeps the deep material behind the trigger: the SKILL.md holds the routing, and the per-feature reference files hold the implementation.

The boundary skills matter too. licensing documents the Syncfusion key path the components require, and migration covers the Xamarin.Forms to .NET MAUI upgrade, which is the highest-risk move an agent will be asked to do in this stack. Neither is glamorous, but both are where an unaided assistant fails.

## Usage

| You say | What happens |
|---|---|
| "Bind data to the Syncfusion DataGrid in .NET MAUI" | syncfusion-maui-datagrid grounds column configuration, sorting, filtering, and grouping. |
| "Add a cartesian chart with line and area series" | syncfusion-maui-cartesian-charts documents the axes, legends, tooltips, and trendlines. |
| "Show a modal confirmation dialog" | syncfusion-maui-popup covers positioning, layout templates, and modal behavior. |
| "Add a date picker with min and max dates" | syncfusion-maui-date-picker covers formatting, restrictions, and dialog modes. |
| "Add an AI chat interface to the app" | syncfusion-maui-ai-assistview documents conversation flows and AI service integration. |
| "Migrate my Xamarin.Forms app to .NET MAUI" | syncfusion-maui-migration walks the Xamarin.Forms upgrade guide. |
| "Set up a new project with licensing and themes" | syncfusion-maui-getting-started covers installation, licensing, and themes. |

## Verification

The raw paths below returned 200 on branch master when this guide was written, and they are the fastest way to read a skill before installing it:

```bash
curl -fsSL https://raw.githubusercontent.com/syncfusion/maui-ui-components-skills/master/skills/syncfusion-maui-datagrid/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/syncfusion/maui-ui-components-skills/master/skills/syncfusion-maui-button/SKILL.md | head -20
```

Each skill lives under `skills/syncfusion-maui-<control>/` with its `references/` subfolder; the repository's default branch is master, not main, so raw.githubusercontent paths must use master.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| syncfusion-maui-parallax-view | Pass | Pass | Pass |
| syncfusion-maui-cartesian-charts | Pass | Pass | Pass |
| syncfusion-maui-button | Pass | Pass | Pass |
| syncfusion-maui-listview | Pass | Pass | Pass |
| syncfusion-maui-combobox | Pass | Warn | Pass |
| syncfusion-maui-picker | Pass | Pass | Pass |
| syncfusion-maui-popup | Pass | Pass | Pass |
| syncfusion-maui-date-picker | Pass | Pass | Pass |
| syncfusion-maui-datagrid | Pass | Pass | Pass |
| syncfusion-maui-checkbox | Pass | Pass | Pass |
| syncfusion-maui-tab-view | Pass | Pass | Pass |
| syncfusion-maui-chips | Pass | Pass | Pass |

All sampled listings pass the Gen Agent Trust Hub, and syncfusion-maui-combobox carries the single Socket Warn. The repository ships no LICENSE file, so the reuse terms for the skill text are not stated in the repository.

## Limitations

- Snapshot data, verified Nov 16, 2026: 16,766 combined installs across 81 indexed listings; 62 GitHub stars; no LICENSE file; last pushed 2026-10-27. Counts drift over time.
- The repository ships no LICENSE file, so the skill text is vendor documentation under Syncfusion's own terms rather than open source.
- The README states 76 skill guides while the index lists 81 listings and the tree holds 81 directories, so the README count is stale.
- Name drift: the indexed listing implementing-interactive-viewer (41 installs) corresponds to the tree directory syncfusion-maui-interactive-viewer.
- The security sample covers 12 of 81 listings; the other 69 remain unaudited by that sample.
- The components are commercial Syncfusion controls licensed by key; the skills document key handling without granting one, and the README points at the free community licence.

## Related

- [Syncfusion WPF UI Skills](/hermes/skills/catalog/syncfusion-wpf-ui-skills-setup)
- [Syncfusion Blazor UI Skills](/hermes/skills/catalog/syncfusion-blazor-ui-skills-setup)
- [Syncfusion React UI Skills](/hermes/skills/catalog/syncfusion-react-ui-skills-setup)
- [Dotnet Skills](/hermes/skills/catalog/dotnet-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with getting-started and migration, then find the control skill for the component you are actually building.
- Read SKILL.md before references/; the per-feature reference files are useful one at a time and wasteful as a set.
- Name the control in your prompt; skills match on the SKILL.md description field, so "DataGrid" triggers the right skill.
- Remember the default branch is master, so raw.githubusercontent and clone-based paths must use master, not main.
- Set the Syncfusion licence key early; the components are commercial and the watermark stays until the key is registered.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
