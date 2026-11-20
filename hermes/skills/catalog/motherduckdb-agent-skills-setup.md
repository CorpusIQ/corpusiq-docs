---
title: "MotherDuck Skills - Analytics Apps on DuckDB Data"
description: "motherduckdb/agent-skills: 9.1K combined installs across 39 listings for building analytics apps and pipelines on MotherDuck."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/motherduckdb-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "motherduck", "duckdb", "data engineering", "analytics"]
---

# MotherDuck Skills - Setup Guide

**Source:** [motherduckdb/agent-skills](https://www.skills.sh/motherduckdb/agent-skills) via skills.sh - 9.1K combined installs across 39 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)

**GitHub:** 62 stars, no LICENSE file (the repository tree carries a LICENSE and the README shows an MIT badge), main branch, last pushed Nov 16, 2026. Source skills live in `skills/<name>/SKILL.md` with generated packages under `plugins/motherduck-skills/` and `plugins/motherduck-skills-claude/`, plus `.claude-plugin/`, `.codex-plugin/` and `.cursor-plugin/` manifests.

**Category:** MotherDuck analytics and data engineering

**Quality Tier:** 🟡 Yellow - 4 Warn and 0 Fail among the 16 sampled skills.sh verdicts (two Socket, two Snyk); no LICENSE file.

motherduckdb publishes opinionated agent skills for building applications with MotherDuck, the serverless DuckDB cloud. The 21 source skills span utility tasks such as connecting and querying, workflow tasks such as loading data and building Dives, and use-case skills that combine them for end-to-end analytics apps, pipelines and migrations.

Each skill ships focused instructions plus, where useful, detailed references and runnable Python and TypeScript examples. Installing the skills does not configure a MotherDuck connection or MCP server, so live work still needs credentials supplied through your normal secret or environment setup.

## Installation

Choose one route for your agent. Commands starting with `/` run inside the agent; the rest run in a terminal.

Claude Code or GitHub Copilot CLI:

```
/plugin marketplace add motherduckdb/agent-skills
/plugin install motherduck-skills@motherduck-skills
```

Codex:

```bash
codex plugin marketplace add motherduckdb/agent-skills
```

Gemini CLI:

```bash
gemini extensions install https://github.com/motherduckdb/agent-skills
```

The Skills CLI (needs Git and Node.js 22.20+) installs interactively with no global CLI:

```bash
npx -y skills add motherduckdb/agent-skills
```

To install the whole catalog for Cursor in one shot:

```bash
npx -y skills add motherduckdb/agent-skills --agent cursor --skill '*' --yes --global
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| motherduck-duckdb-sql | 481 | DuckDB SQL syntax and MotherDuck feature support |
| motherduck-query | 478 | Write, run and optimize DuckDB SQL against MotherDuck |
| motherduck-build-dashboard | 464 | Build MotherDuck dashboards as Dives with metrics and queries |
| motherduck-build-cfa-app | 464 | Customer-facing analytics with tenant isolation and serving APIs |
| motherduck-ducklake | 457 | Decide and operate DuckLake open table storage safely |
| motherduck-build-data-pipeline | 457 | Build ingestion-to-serving pipelines on MotherDuck |
| motherduck-load-data | 456 | Load files, storage and external databases into MotherDuck |
| motherduck-connect | 456 | Set up connections, MCP server and authentication |
| motherduck-model-data | 454 | Design analytical schemas and transformation models |
| motherduck-explore | 454 | Find and understand databases, tables, columns and shares |
| motherduck-enable-self-serve-analytics | 454 | Roll out governed analytics to internal teams |
| motherduck-create-dive | 450 | Create, edit, publish, share and embed Dives |
| motherduck-share-data | 449 | Create and manage data shares and audience grants |
| motherduck-partner-delivery | 448 | Standardize delivery across client engagements |
| motherduck-migrate-to-motherduck | 448 | Plan migrations with validation, cutover and rollback |
| motherduck-pricing-roi | 446 | Assess MotherDuck costs, plan fit and ROI |
| motherduck-rest-api | 443 | Service accounts, tokens, Ducklings and embed sessions |
| motherduck-security-governance | 410 | Permissions, isolation, residency and compliance |

The remaining 21 indexed listings range from 9 to 307 installs.

## Why This Matters for Hermes Agents

This collection shows how a vendor can ship agent skills that encode its own product's correct usage instead of leaving an agent to guess. The skills favor DuckDB SQL, live schema discovery and native MotherDuck storage by default, which is exactly the kind of opinion an agent needs to avoid emitting PostgreSQL-only syntax or misnamed tables against a MotherDuck database.

The layering is worth copying. Utility skills handle single operations, workflow skills cover one capability, and use-case skills compose them end to end, so an agent can pick the right granularity for the job rather than loading a monolith. The machine-readable catalog and the generated plugin packages for Claude, Codex and Cursor keep the same source skills consistent across harnesses.

For a builders audience, the runnable examples are the point: several skills bundle working Python and TypeScript artifacts, so the instructions are exercised rather than asserted.

## Usage

| You say | What happens |
|---|---|
| "Use motherduck-connect to choose the connection path for this app" | The skill picks the right connection, auth and client runtime |
| "Explore my MotherDuck workspace and build a sales dashboard as a Dive" | The workspace is discovered, then a Dive is built from the analytical story |
| "Plan a migration to MotherDuck with validation and rollback" | SQL translation, source-to-target validation and cutover are planned |
| "Load this CSV into MotherDuck" | motherduck-load-data runs bulk ingestion |
| "Fix this SQL that fails on MotherDuck" | motherduck-duckdb-sql repairs the dialect-specific syntax |
| "Share this data with a partner" | motherduck-share-data sets audiences, grants and table filters |

## Verification

After installing, confirm the skill folders are present under `skills/` in the repository checkout and that your harness discovers them. To review one skill before relying on it, fetch its definition directly:

```bash
curl -sL https://raw.githubusercontent.com/motherduckdb/agent-skills/main/skills/motherduck-query/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| motherduck-duckdb-sql | Pass | Pass | Pass |
| motherduck-query | Pass | Pass | Pass |
| motherduck-build-dashboard | Pass | Pass | Pass |
| motherduck-build-cfa-app | Pass | Warn | Pass |
| motherduck-ducklake | Pass | Pass | Pass |
| motherduck-build-data-pipeline | Pass | Warn | Pass |
| motherduck-load-data | Pass | Pass | Warn |
| motherduck-connect | Pass | Pass | Pass |
| motherduck-model-data | Pass | Pass | Pass |
| motherduck-explore | Pass | Pass | Warn |
| motherduck-enable-self-serve-analytics | Pass | Pass | Pass |
| motherduck-create-dive | Pass | Pass | Pass |
| motherduck-share-data | Pass | Pass | Pass |
| motherduck-partner-delivery | Pass | Pass | Pass |
| motherduck-migrate-to-motherduck | Pass | Pass | Pass |
| motherduck-pricing-roi | Pass | Pass | Pass |

No sampled skill fails a verdict. Four carry a single Warn: motherduck-build-cfa-app and motherduck-build-data-pipeline in Socket, and motherduck-load-data and motherduck-explore in Snyk.

## Limitations

- Snapshot data, verified Nov 19, 2026: 9,095 combined installs across 39 indexed listings; 62 GitHub stars; no LICENSE file; last pushed Nov 16, 2026. Counts drift over time.
- The 39 listings include 17 plain-name re-listings (connect, query, load-data and the rest) of the same motherduck-prefixed skills, so the index double-counts most skills.
- motherduck-design-dive carries 156 installs in the index but has no matching directory in the current tree.
- GitHub metadata reports no licence while the tree contains a LICENSE file and the README shows an MIT badge, so the licensing status is unclear despite the README.
- Installing the skills does not configure a MotherDuck connection or MCP server; live queries still need your own credentials and access.

## Related

- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)
- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup)
- [Amplitude Agent Skills - Product Analytics Setup](/hermes/skills/catalog/amplitude-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run motherduck-explore first on an unfamiliar workspace so later skills reuse the schema context instead of rediscovering it.
- Supply credentials through your normal secret or environment setup, never in prompts or committed files.
- For live work, configure the MotherDuck MCP server or an authenticated database client, since skills provide guidance rather than account access.
- Treat PostgreSQL wire compatibility as transport only: it does not change the SQL dialect, so use motherduck-duckdb-sql for any syntax question.
- Install one route per agent and reload the agent afterward; skills are discovered at startup.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
