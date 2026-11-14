---
title: "Dagster Skills - Data Orchestration Setup"
description: "dagster-io/skills: 11.1K combined installs across 7 listings, AI skills for building workflows and data pipelines with Dagster."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dagster-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "dagster", "data orchestration", "pipelines"]
---

# Dagster Skills - Setup Guide

**Source:** [dagster-io/skills](https://www.skills.sh/dagster-io/skills) via skills.sh - 11.1K combined installs across 7 indexed listings; first seen Nov 14, 2026
**GitHub:** 218 stars, Apache-2.0 license, `master` branch, last pushed 2026-11-12, 2 `SKILL.md` files in the tree
**Category:** Data orchestration skills for Dagster
**Quality Tier:** 🟡 Yellow - the dagster-expert skill passes all three auditors, but three of six sampled listings carry a Snyk Warn and most indexed names have no SKILL.md in the tree.

Dagster Skills is Dagster's official collection of AI skills for building workflows and data pipelines. The index serves 7 listings with 11,064 combined installs, but the current tree holds only 2 `SKILL.md` files - `plugins/dagster-expert/skills/dagster-expert/SKILL.md` and `plugins/dagster/skills/dagster-expert/SKILL.md`. Only `dagster-expert` can be grounded in the tree; the other six indexed names (dignified-python, dagster-integrations, dagster-best-practices, dg, dagster-conventions and integrations-index) have no matching SKILL.md path, so this guide describes them only from their skills.sh listing text.

The repo bundles the `dagster-expert` skill for authoring pipelines with the Dagster+ MCP server for access to a live Dagster+ deployment. The default branch is `master`, and all documented install paths deliver a `release-stable` branch that moves to each weekly Dagster release.

## Installation

Install the Claude Code plugin:

```text
/plugin marketplace add dagster-io/skills
/plugin install dagster@dagster
/dagster-expert "What's an asset?"
```

Or install with the skills.sh CLI:

```bash
npx skills add dagster-io/skills#release-stable
```

The plugin includes the Dagster+ MCP server; run `/mcp` to authenticate and give the skill access to your deployed organization's runs, assets, deployments and Insights. Codex installs the same plugin with `codex plugin marketplace add dagster-io/skills --ref release-stable` then `codex plugin add dagster@dagster`; Copilot uses `copilot plugin install dagster-io/skills:plugins/dagster`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| dagster-expert | 6,517 | Expert guidance for building Dagster projects: CLI commands, asset patterns, automation and implementation workflows. |
| dignified-python | 4,378 | Opinionated production Python standards with automatic version detection (3.10-3.13). |
| dagster-integrations | 124 | Discover and understand Dagster integration libraries. |

The remaining 4 indexed listings range from 4 to 18 installs.

## Why This Matters for Hermes Agents

Dagster Skills gives a Hermes agent a grounded way to author and debug Dagster pipelines through the dagster-expert skill, which covers the dg CLI, asset patterns, declarative automation, scheduling and sensors. The bundled Dagster+ MCP server extends that from code generation to live operations: an agent can fetch run logs, materialize assets, inspect deployments and read Insights metrics against a real Dagster+ organization, not just emit scaffolding.

The drift is the thing to watch. The install index lists 7 skills, but only dagster-expert exists in the current tree; the remaining names (dignified-python, dagster-integrations, dagster-best-practices, dg, dagster-conventions and integrations-index) carry install counts on skills.sh yet have no SKILL.md file to fetch. Treat those as index-only listings until a matching tree path reappears.

The plugin packaging matters too. The skill now ships in a plugin named dagster, not dagster-expert, and the older dagster-expert plugin has become a stub. An agent setup script that installs the stale stub can shadow the real skill, so the migration step (uninstall dagster-expert) is load-bearing.

## Usage

| You say | What happens |
|---|---|
| "Create a new Dagster project called analytics" | Runs dagster-expert to scaffold the project via the dg CLI. |
| "How do I set up declarative automation?" | Runs dagster-expert guidance on automation, schedules and sensors. |
| "Why did my materialization fail?" | Runs dagster-expert debugging guidance, then the MCP can fetch the run logs. |
| "Fetch the run logs for the most recent failure" | The Dagster+ MCP server retrieves logs from the deployment. |
| "What is my materialization success rate this month?" | The MCP server pulls Insights metrics for assets and jobs. |
| "Launch all assets tagged with priority=high" | Runs dagster-expert to launch the matching assets. |

## Verification

Probe the dagster-expert skill on the `master` branch before installing. Both paths return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/dagster-io/skills/master/plugins/dagster-expert/skills/dagster-expert/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/dagster-io/skills/master/plugins/dagster/skills/dagster-expert/SKILL.md
```

The skill ships in two plugin directories: `plugins/dagster/skills/dagster-expert/SKILL.md` is the current plugin, and `plugins/dagster-expert/skills/dagster-expert/SKILL.md` is the deprecated stub.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| dagster-expert | Pass | Pass | Pass |
| dignified-python | Pass | Pass | Pass |
| dagster-integrations | Pass | Pass | Warn |
| dagster-best-practices | Pass | Pass | Warn |
| dg | Pass | Pass | Pass |
| dagster-conventions | Pass | Pass | Warn |

Three of the six sampled skills carry a Snyk Warn; the other three pass all auditors. The sample covers 6 of the 7 indexed listings, but four of those sampled names have no SKILL.md in the current tree, so their verdicts may not correspond to fetchable code.

## Limitations

- Snapshot data, verified 2026-11-14: 11,064 combined installs across 7 indexed listings; 218 GitHub stars; Apache-2.0; last pushed 2026-11-12. Counts drift over time.
- The install index outruns the tree: only dagster-expert has a matching SKILL.md path; dignified-python, dagster-integrations, dagster-best-practices, dg, dagster-conventions and integrations-index have no counterpart in the current tree and are described here only from their skills.sh listing text.
- The default branch is `master`; keep it in every raw URL and install path rather than `main`.
- Three of six sampled verdicts carry a Snyk Warn, and the sample overlaps names that have no fetchable SKILL.md in the tree.
- The dagster-expert plugin is a deprecated stub; installing it alongside the dagster plugin can shadow the real skill.

## Related

- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)
- [Looker Skills - Official LookML Development Suite](/hermes/skills/catalog/looker-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install via `npx skills add dagster-io/skills#release-stable` to get the weekly release branch rather than `master`.
- Run `/mcp` after installing the plugin to authenticate the Dagster+ MCP server for live deployment access.
- If you installed the old dagster-expert plugin, run `/plugin uninstall dagster-expert` so it does not shadow the real skill.
- For EU-hosted organizations, set DAGSTER_CLOUD_MCP_URL before launching Claude Code.
- Treat dignified-python and the other index-only names as unverifiable until a tree path reappears.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
