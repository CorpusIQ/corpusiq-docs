---
title: "Microsoft Fabric Skills - Power BI Agent Suite"
description: "microsoft/skills-for-fabric: 3.6K combined installs across 17 listings, official Fabric and Power BI skills for semantic models, reports and OneLake."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/microsoft-fabric-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "microsoft fabric", "power bi", "analytics"]
---

# Microsoft Fabric Skills - Setup Guide

**Source:** [microsoft/skills-for-fabric](https://www.skills.sh/microsoft/skills-for-fabric) via skills.sh - 3.6K combined installs across 17 indexed listings; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 1,355 stars, MIT license, `main` branch, last pushed 2026-11-12, 55 `SKILL.md` files under `plugins/fabric-skills/skills/` across three installable bundles
**Category:** Microsoft Fabric, Power BI and analytics engineering
**Quality Tier:** 🟢 Green - the three sampled skills pass all three auditors.

Microsoft's Fabric skills are the platform team's own instructions for agents working in the Microsoft analytics stack. They are packaged as plugins for GitHub Copilot CLI and other compatible hosts, and they cover the parts of Fabric that agents get wrong: semantic model authoring, report design, medallion architecture, OneLake catalog operations and the CLI surfaces that drive each workload.

The packaging is worth reading before installing. There are three bundles (`fabric-skills`, `powerbi-authoring` and a consumption bundle), and the older persona bundles (fabric-authoring, fabric-consumption, fabric-operations) are retired while still resolving as aliases. Copilot CLI installs whole bundles rather than filtering individual skills, so choosing the bundle is the way to control scope.

## Installation

Add the marketplace inside GitHub Copilot CLI, then install the bundle you need:

```bash
/plugin marketplace add microsoft/skills-for-fabric
/plugin install fabric-skills@fabric-collection
```

For Power BI authoring specifically, install the focused bundle instead:

```bash
/plugin install powerbi-authoring@fabric-collection
```

Update a bundle with `/plugin update fabric-skills@fabric-collection`, or update everything from a terminal with `copilot plugin update --all`. Automatic update checking is handled by the agent host, not by a skill, and is opt-in through `extraKnownMarketplaces` in `~/.copilot/settings.json`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| semantic-model-authoring | 502 | Building and editing Power BI semantic models, including relationships, measures and model structure. |
| powerbi-report-authoring | 407 | Authoring Power BI reports and pages from the file format up. |
| powerbi-report-design | 394 | Report layout, visual choice and design rules. |
| e2e-medallion-architecture | 323 | Designing bronze, silver and gold layers end to end. |
| powerbi-report-planning | 313 | Planning a report before authoring: questions, measures and structure. |
| powerbi-report-cli | 277 | Driving Power BI report work through the command line. |
| powerbi-report-management | 265 | Managing existing reports and their lifecycle. |
| fabriciq | 257 | Working with Fabric IQ, the platform's data agent surface. |
| databricks-migration | 226 | Migrating Databricks workloads to Fabric. |
| e2e-fabric-cost-estimation | 144 | Estimating Fabric capacity and workload cost before building. |
| fabriciq-ontology-cli | 114 | Managing Fabric IQ ontologies from the CLI. |

The remaining 6 indexed listings range from 22 to 94 installs.

## Why This Matters for Hermes Agents

Fabric is a stack where the file formats are unforgiving. A semantic model or a report is a folder of JSON and TMDL files, not a wizard session, and an agent that invents a property name produces something the service refuses to open. The authoring skills are grounded in those formats, which is the difference between a draft and a broken artifact.

The suite also covers the decision layer rather than only the mechanics. `powerbi-report-planning` asks what the report is for before anything is authored, and `powerbi-report-design` carries the visual rules. `e2e-fabric-cost-estimation` exists because Fabric capacity is billed by the unit, and an agent that builds first and discovers the cost later has wasted a migration cycle.

The migration and ontology skills are the newest surface. `databricks-migration` covers moving workloads across platforms, and the `fabriciq` pair covers the data agent layer that Microsoft is pushing as the way agents query OneLake. If your roadmap includes Fabric IQ, those two listings are the only grounded guidance in this catalog.

## Usage

| You say | What happens |
|---|---|
| "Model sales, returns and inventory as a semantic model" | Uses semantic model authoring to build the model structure with the documented properties. |
| "Design a report for regional sales managers" | Runs planning first, then the design skill for layout and visuals. |
| "Lay out a medallion architecture for this source system" | Uses the end-to-end medallion skill to draw bronze, silver and gold layers with the transformations at each. |
| "What will this capacity cost per month?" | Uses the cost estimation skill to size capacity against the workload. |
| "Move our Databricks notebooks to Fabric" | Uses the Databricks migration skill for the porting path. |
| "Point our data agent at the gold layer" | Uses the Fabric IQ skills and the ontology CLI to wire the agent to the curated tables. |

## Verification

Check the bundle metadata and one skill file before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/microsoft/skills-for-fabric/main/plugins/fabric-skills/skills/semantic-model-authoring/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/microsoft/skills-for-fabric/main/README.md
```

Every skill path sits under `plugins/fabric-skills/skills/<name>/SKILL.md`, so a raw URL built from the skill name alone is wrong.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| semantic-model-authoring | Pass | Pass | Pass |
| powerbi-report-authoring | Pass | Pass | Pass |
| fabriciq | Pass | Pass | Pass |

The repository is first-party Microsoft content: Markdown skills plus plugin manifests, with no third-party binaries.

## Limitations

- Snapshot data, verified 2026-11-14: 3,559 combined installs across 17 indexed listings; 1,355 GitHub stars; MIT; last pushed 2026-11-12. Counts drift over time.
- The install index is smaller than the tree: 17 listings against 55 `SKILL.md` files, so most skills in the repository carry no install count yet.
- Copilot CLI installs whole bundles. There is no documented way to install a single skill from `fabric-skills`.
- The persona bundles `fabric-authoring`, `fabric-consumption` and `fabric-operations` are retired. They resolve as aliases for existing installs, but new setups should install `fabric-skills` or `powerbi-authoring`.
- Auto-update is not handled by the skill set. It comes from the agent host and has to be enabled in the host's settings.
- Fabric itself is required for anything beyond authoring files: capacity, workspaces and the ontology CLI are Microsoft service surfaces.

## Related

- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)
- [Dagster Skills - Data Orchestration Setup](/hermes/skills/catalog/dagster-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `powerbi-authoring` when the work is reports or models; it is the smaller bundle and the one that matches that job.
- Ask the cost estimation skill for a capacity estimate before a migration, not after.
- Point the agent at the skill file for the exact workload, since the bundle carries 55 of them and loading all is wasteful.
- Keep retired persona bundle names out of new setup scripts; they still resolve, which hides the drift.
- If a report fails to open, diff the generated TMDL against the authoring skill's structure before rewriting the report by hand.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
