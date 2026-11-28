---
title: "Power BI Agentic Development - Skills and Agents Suite"
description: "data-goblin/power-bi-agentic-development: 2.4K combined installs. Power BI and Fabric skills, subagents and hooks for DAX, TMDL and reports."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/power-bi-agentic-dev-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "power bi", "microsoft fabric", "dax", "tmdl"]
---

# Power BI Agentic Development - Setup Guide

**Source:** [data-goblin/power-bi-agentic-development](https://www.skills.sh/data-goblin/power-bi-agentic-development) via skills.sh - 2.4K combined installs across 38 indexed listings; first seen Nov 28 2026 (morning sweep)

**GitHub:** [data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development) - 1,115 stars, GPL-3.0 license, branch main, last pushed 2026-11-25; skills live under `plugins/<plugin>/skills/<name>/SKILL.md` with a `.claude-plugin/marketplace.json` at the root.

**Category:** Power BI and Microsoft Fabric agent skills - semantic models, DAX, TMDL, PBIP/PBIR tooling, reports and dashboards

**Quality Tier:** 🟠 Orange - Gen Agent Trust Hub fails pbir-cli and deneb-visuals; Warn cells land on pbir-cli (Socket), connect-pbid (Gen Agent Trust Hub), pbir-format (Snyk), deneb-visuals (Snyk) and te-docs (Snyk).

data-goblin/power-bi-agentic-development is a plugin marketplace that teaches Claude Code and GitHub Copilot Power BI and Microsoft Fabric. Published by Kurt Buhler (Data Goblins, part of Tabular Editor), it ships 14 child plugins: goblin-mode, tabular-editor, pbi-desktop, pbip, reports, paginated-reports, custom-visuals, semantic-models, fabric-cli, fabric-admin, databricks-cli, fabric-data-app, etl and dashboards. Each plugin bundles skills, subagents, hooks and mods around a focused topic, and the README flags a weekly release cadence.

The 38 indexed listings span the Power BI and Fabric lifecycle: semantic models (DAX, Power Query and TMDL), reports (PBIP and PBIR formats, themes, design and review), custom visuals (Deneb, SVG, R, Python and pbiviz), Fabric administration, and ETL with Spark and DuckDB. The top listings are pbi-report-design (149 installs) and pbir-format (127 installs), followed by a long tail of smaller guides.

## Installation

The README installs the repository as a Claude Code plugin marketplace. Register it once, then install the child plugins you need:

```text
claude plugin marketplace add data-goblin/power-bi-agentic-development
```

Then install plugins through `/plugin` and the marketplace UI, or add them directly from the command line:

```text
claude plugin install goblin-mode@power-bi-agentic-development
claude plugin install tabular-editor@power-bi-agentic-development
claude plugin install pbi-desktop@power-bi-agentic-development
claude plugin install pbip@power-bi-agentic-development
claude plugin install semantic-models@power-bi-agentic-development
claude plugin install reports@power-bi-agentic-development
claude plugin install paginated-reports@power-bi-agentic-development
claude plugin install custom-visuals@power-bi-agentic-development
claude plugin install fabric-cli@power-bi-agentic-development
claude plugin install fabric-admin@power-bi-agentic-development
claude plugin install databricks-cli@power-bi-agentic-development
claude plugin install fabric-data-app@power-bi-agentic-development
claude plugin install etl@power-bi-agentic-development
claude plugin install dashboards@power-bi-agentic-development
```

The standalone Copilot CLI reads the same `.claude-plugin/marketplace.json` manifest, so the layout works unchanged. Register the marketplace then install a named child plugin, or install a single plugin straight from its subdirectory:

```text
copilot plugin marketplace add data-goblin/power-bi-agentic-development
copilot plugin install tabular-editor@power-bi-agentic-development
copilot plugin install data-goblin/power-bi-agentic-development:plugins/pbip
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| pbi-report-design | 149 | The Power BI report design canon: design identity, visual hierarchy, layout, color discipline, chart selection and accessibility. |
| pbir-format | 127 | Author and edit PBIR metadata files directly: visual.json, report.json, themes, filters, report extensions and visual calculations. |
| create-pbi-report | 118 | Step-by-step workflow for building a complete report from scratch via the pbir CLI. |
| pbip | 114 | Power BI Project (PBIP) format, structure and file types. |
| pbir-cli | 112 | Programmatic report manipulation via the pbir CLI, including live Power BI Desktop refresh and page screenshots. |
| power-query | 107 | Write M expressions, debug query folding, and execute M locally or via the Fabric API. |
| dax | 107 | Write, debug and optimize DAX in semantic models. |
| tmdl | 105 | Author and edit TMDL files directly for semantic models. |
| modifying-theme-json | 103 | Design, enforce, audit and validate Power BI report themes through the pbir CLI. |
| review-report | 90 | Actionable feedback on report quality, usage and effectiveness. |
| deneb-visuals | 81 | Deneb visual creation and Vega/Vega-Lite spec authoring for PBIR reports. |
| connect-pbid | 81 | Explore, query and modify a model in Power BI Desktop, and reload or screenshot the report canvas via the Desktop Bridge. |
| bpa-rules | 74 | Create and improve Best Practice Analyzer rules for semantic models. |
| svg-visuals | 71 | SVG generation via DAX measures for inline chart visualizations like sparklines and bullet charts. |
| te2-cli | 69 | Tabular Editor 2 CLI usage and automation (not TE3). |
| lineage-analysis | 67 | Trace downstream reports from a semantic model across Fabric workspaces. |
| semantic-model | 66 | Design, build, refresh and review semantic models through a te-first tool cascade. |
| fabric-cli | 62 | Fabric CLI (fab) for remote operations across workspaces, items, semantic models and reports. |
| te-docs | 61 | Tabular Editor documentation search and TE3 configuration files. |
| refresh-semantic-model | 61 | Trigger or troubleshoot semantic model refreshes. |
| c-sharp-scripting | 61 | C# scripting and macros for Tabular Editor. |
| r-visuals | 55 | Custom R visuals (ggplot2) for Power BI reports. |
| audit-tenant-settings | 55 | Audit Fabric and Power BI tenant settings, delegated overrides and Entra security group membership. |
| standardize-naming-conventions | 54 | Naming-convention standardization; no counterpart in the current repo tree. |
| python-visuals | 52 | Custom Python visuals (matplotlib/seaborn) for Power BI reports. |
| powerbi-custom-visuals | 44 | Power BI developer custom visual (.pbiviz) development with the pbiviz toolchain and MCP server. |
| te-cli | 37 | Cross-platform Tabular Editor CLI (te, preview) for semantic models from the terminal. |
| paginated-report | 37 | Author, validate and publish Power BI paginated reports in RDL format. |
| executing-spark | 31 | Execute Python or PySpark code on Fabric Spark compute without creating a notebook artifact. |
| using-duckdb | 30 | Query Fabric lakehouse and warehouse data with DuckDB, locally or in a notebook. |
| help-me-get-started | 23 | A jargon-free guide to agentic development for people new to agents. |
| review-semantic-model | 22 | Semantic model review; no counterpart in the current repo tree. |
| improve-my-agent-setup | 21 | Setup-wide health check across skills, memory, tools, permissions and secrets, with fixes. |
| organize-semantic-model | 15 | Organize a model end to end: names, folders, hierarchies, descriptions, formats, UDFs and roles. |
| fabric-capacity | 13 | Read Fabric capacity utilization and per-item CU metrics, and start, pause or monitor a capacity. |
| creating-good-dashboards | 10 | Dashboard comment etiquette and visual style after Stephen Few and Edward Tufte. |
| querying-fabric | 7 | DAX and T-SQL queries through a Fabric connector or MCP server for Claude Dashboards. |
| refreshing-semantic-model | 3 | Semantic model refresh; no counterpart in the current repo tree. |

All 38 indexed listings appear in the table above. Three listings carry install counts but have no directory in the current repo tree: standardize-naming-conventions, review-semantic-model and refreshing-semantic-model.

## Why This Matters for Hermes Agents

This suite is a complete, well-structured reference for teaching a coding agent a vendor BI stack. The skills are organized as a plugin marketplace, each plugin bundling skills, subagents, hooks and mods around one topic, and the README explicitly warns against installing every plugin because each skill competes for the agent's attention and context window. That design guidance is worth copying for any multi-skill publisher.

The skills encode deep domain knowledge rather than shallow templates: DAX performance patterns, TMDL file authoring, PBIR JSON schemas and a te-first tool cascade for semantic models. A Hermes builder wiring Power BI or Fabric capabilities into a router can lift these as reference material for how a domain skill should carry references, examples and scripts rather than a prompt alone.

The hooks are deterministic validators that fire on tool use, checking PBIR and TMDL structure, DAX references and measure metadata. That is a useful pattern for adding automated guardrails to an agent loop. The subagents (pbip-validator, deneb-reviewer, svg-reviewer, r-reviewer, python-reviewer and semantic-model-auditor) show a review-and-validation layer a Hermes pipeline can mirror.

The security verdicts are a useful calibration too: two skills (pbir-cli and deneb-visuals) fail the Gen Agent Trust Hub, so even a focused single-domain suite deserves a scan before it enters a production profile.

## Usage

| You say | What happens |
|---|---|
| "Create a Power BI report from this data model" | Uses create-pbi-report with the pbir CLI to scaffold pages, theme, visuals and field binding. |
| "Optimize this slow DAX measure" | Uses dax to diagnose the measure and apply performance patterns. |
| "Add a measure to my semantic model" | Uses semantic-model to drive the change through te CLI, then TOM or TMDL. |
| "Validate my PBIP project" | Uses the pbip hooks to check PBIR structure, TMDL syntax and report binding. |
| "Audit our Fabric tenant settings" | Uses audit-tenant-settings to review tenant settings, delegated overrides and security groups. |
| "Why is our Fabric capacity throttled?" | Uses fabric-capacity to read CU utilization and per-item usage from the Capacity Metrics model. |
| "Build a paginated report for printing" | Uses paginated-report to author, validate and publish an RDL report. |

## Verification

The README installs through the Claude Code plugin marketplace, so the cleanest pre-install check is to fetch a skill's SKILL.md directly and read its frontmatter. The layout on branch main is `plugins/<plugin>/skills/<name>/SKILL.md`:

```bash
curl -sL https://raw.githubusercontent.com/data-goblin/power-bi-agentic-development/main/plugins/pbip/skills/pbir-format/SKILL.md
```

After a clone, confirm the plugin directories and the marketplace manifest:

```bash
git clone --depth 1 https://github.com/data-goblin/power-bi-agentic-development.git /tmp/pbi-agentic-dev
ls /tmp/pbi-agentic-dev/plugins/
cat /tmp/pbi-agentic-dev/.claude-plugin/marketplace.json
```

The `plugins/` directory should list the 14 child plugins (goblin-mode through dashboards). The repo root additionally holds the `.claude-plugin/marketplace.json` manifest plus `release-notes/` and `useful-stuff/` directories.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pbi-report-design | Pass | Pass | Pass |
| pbir-format | Pass | Pass | Warn |
| create-pbi-report | Pass | Pass | Pass |
| pbip | Pass | Pass | Pass |
| pbir-cli | Fail | Warn | Pass |
| power-query | Pass | Pass | Pass |
| dax | Pass | Pass | Pass |
| tmdl | Pass | Pass | Pass |
| modifying-theme-json | Pass | Pass | Pass |
| review-report | Pass | Pass | Pass |
| deneb-visuals | Fail | Pass | Warn |
| connect-pbid | Warn | Pass | Pass |
| bpa-rules | Pass | Pass | Pass |
| svg-visuals | Pass | Pass | Pass |
| te2-cli | Pass | Pass | Pass |
| lineage-analysis | Pass | Pass | Pass |
| semantic-model | Pass | Pass | Pass |
| fabric-cli | Pass | Pass | Pass |
| te-docs | Pass | Pass | Warn |
| refresh-semantic-model | Pass | Pass | Pass |

This guide is Orange because the Gen Agent Trust Hub fails pbir-cli and deneb-visuals. The Warn cells sit on pbir-format (Snyk), pbir-cli (Socket), connect-pbid (Gen Agent Trust Hub), deneb-visuals (Snyk) and te-docs (Snyk). Only 20 of the 38 indexed listings were sampled.

## Limitations

- Snapshot data, verified 2026-11-28: 2,395 combined installs across 38 indexed listings; 1,115 GitHub stars; GPL-3.0 license; last pushed 2026-11-25. Counts drift over time.
- The install index outruns the tree: standardize-naming-conventions (54), review-semantic-model (22) and refreshing-semantic-model (3) carry install counts but have no matching directories in the current repo tree.
- fabric-capacity (13) is present in the tree at `plugins/fabric-admin/skills/fabric-capacity/` but is not listed in the README's fabric-admin plugin table.
- The README warns the suite is under active development with a weekly release cadence and expects regular renaming and restructuring; versions 26.26 through 26.38 are a deliberate breaking transition, and it says to pin 26.25 or earlier for the pre-transition structure.
- GPL-3.0 licensing: the README states the plugins are for free community use, but copying them into your own products, trainings, courses or tools requires attribution and a link to the original project.
- The security verdicts cover 20 of the 38 indexed listings; the other 18 were not sampled.

## Related

- [Microsoft Fabric Skills - Power BI Agent Suite](/hermes/skills/catalog/microsoft-fabric-skills-setup)
- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the plugins you need: the README warns each skill competes for the agent's attention and context window, and it prefers project-scoped installs over user-scoped ones.
- Pin 26.25 or earlier if you depend on the pre-transition skill structure, since 26.26 through 26.38 are a breaking transition.
- Read a skill's SKILL.md before installing the whole plugin: two frontmatter fields plus instructions define what it does.
- Follow the semantic-model skill's cascade: drive every operation through te CLI first, then TOM (connect-pbid) or a model MCP, then TMDL authoring, rather than hand-editing files.
- Two skills fail the Gen Agent Trust Hub (pbir-cli and deneb-visuals), so re-check the skills.sh security pages before pulling the suite into a production profile.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
