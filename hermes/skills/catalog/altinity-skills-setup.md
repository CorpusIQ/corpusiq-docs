---
title: "Altinity Skills - ClickHouse DBA and Dev Setup"
description: "altinity/altinity-skills - 1.9K combined installs: Altinity's official ClickHouse skills for schema, performance, and DBA diagnostics."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/altinity-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "clickhouse", "database", "dba"]
---

# Altinity Skills - Setup Guide

**Source:** [altinity/altinity-skills](https://www.skills.sh/altinity/altinity-skills) via skills.sh - 1.9K combined installs across 27 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [altinity/altinity-skills](https://github.com/altinity/altinity-skills) - 18 stars, Apache-2.0 license, last pushed Sep 17, 2026, main branch; 19 diagnostic skills under altinity-expert-clickhouse/skills/<name>/SKILL.md plus the altinity-profiler-clickhouse profiler.
**Category:** ClickHouse Development and DBA (Altinity)
**Quality Tier:** 🟡 Yellow - 12 of 27 listings sampled: nine pass all three checks, and three carry a single Snyk Warn each (ingestion, reporting, memory).

altinity/altinity-skills is Altinity's official collection of agent skills for ClickHouse development and DBA tasks, published under the Apache-2.0 license. The centerpiece is altinity-expert-clickhouse, a modular diagnostic skill set whose modules each target one failure domain, plus altinity-profiler-clickhouse, which profiles a live cluster via MCP and generates a per-cluster analyst skill.

The diagnostic skills live under altinity-expert-clickhouse/skills/<name>/SKILL.md with a checks.sql and reference.md alongside each. Several indexed listings (skill-installer, skill-creator, github-triage, and others) carry install counts but have no matching directory in the current tree, so the install index outruns the tree.

## Installation

The README documents a skills-CLI one-liner per group, installing all expert skills or the profiler into the agent's skills directory:

```bash
npx skills add --agent claude-code Altinity/altinity-skills/altinity-expert-clickhouse/
npx skills add --agent claude-code Altinity/altinity-skills/altinity-profiler-clickhouse/
```

A single skill can be installed by pointing at its directory, for example altinity-expert-clickhouse/skills/altinity-expert-clickhouse-overview. The same pattern works with --agent codex and --agent gemini. Manual install clones the repo and copies or symlinks a skill directory into ~/.claude/skills/. A pre-built Docker image (ghcr.io/altinity/expert) bundles Claude Code, Codex CLI, and the Altinity MCP server, and a Helm chart runs skills as Kubernetes jobs.

## What It Provides

skills.sh publishes per-skill install counts for all 27 indexed listings. The 13 most-installed skills are listed below; the remaining 14 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| altinity-expert-clickhouse-schema | 114 | diagnose table design: partitioning, ORDER BY and primary key, Nullable usage, and materialized views |
| altinity-expert-clickhouse-logs | 107 | check system log tables for freshness, TTL, disk footprint, and crash records |
| altinity-expert-clickhouse-ingestion | 107 | diagnose INSERT performance, batch sizing, part creation, and materialized-view overhead |
| altinity-expert-clickhouse-overview | 104 | fast server health snapshot that routes to the specialist skills |
| altinity-expert-clickhouse-mutations | 104 | diagnose mutations: ALTER UPDATE/DELETE, MATERIALIZE, and column changes |
| altinity-expert-clickhouse-merges | 104 | diagnose merge performance, part backlog, and too-many-parts errors |
| altinity-expert-clickhouse-metrics | 103 | resource saturation from system.metrics, system.events, and asynchronous metrics |
| altinity-expert-clickhouse-storage | 102 | diagnose disk usage, compression, part sizes, and storage policies |
| altinity-expert-clickhouse-reporting | 102 | diagnose SELECT performance, slow queries, and repeated expensive query patterns |
| altinity-expert-clickhouse-replication | 102 | diagnose replication health, Keeper connectivity, and replica lag |
| altinity-expert-clickhouse-memory | 102 | diagnose RAM usage, memory limits, and OOM errors |
| altinity-expert-clickhouse-dictionaries | 102 | diagnose external dictionaries: load status, memory, and lookup performance |
| altinity-expert-clickhouse-caches | 101 | analyze mark, uncompressed, query, and compiled-expression caches: hit ratios and RAM footprint |

The remaining 14 indexed listings range from 1 to 99 installs.

## Why This Matters for Hermes Agents

Altinity is the ClickHouse specialist vendor, and this suite encodes their operational playbook into skills an agent can run. The overview module is the entry point: it snapshots server health and routes to the specialist module for the affected domain, so an agent does not need to know which of memory, merges, replication, or storage to check first. Each module pairs a SKILL.md with a checks.sql the agent can execute against the cluster, turning a diagnosis into concrete, reproducible queries rather than prose advice. The profiler goes further: it profiles a live cluster through MCP and generates a reusable analyst skill, which is a genuinely agent-native deliverable. The security module (below threshold) carries a 15-reference deep dive, and the repo ships a test harness and a Helm chart, so the skills are engineered for non-interactive, production use.

## Usage

| You say | What happens |
|---|---|
| Is this server healthy | Uses altinity-expert-clickhouse-overview for a health snapshot and routing |
| Inserts are slow | Uses altinity-expert-clickhouse-ingestion for batch sizing and part creation |
| The server keeps running out of memory | Uses altinity-expert-clickhouse-memory for limits and OOM allocation breakdown |
| Replicas are lagging | Uses altinity-expert-clickhouse-replication for lag and Keeper checks |
| Merges seem stuck | Uses altinity-expert-clickhouse-merges for part backlog and too-many-parts errors |
| Queries are too slow | Uses altinity-expert-clickhouse-reporting for query patterns and optimization |
| Profile my cluster | Uses altinity-profiler-clickhouse to generate a per-cluster analyst skill |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/altinity/altinity-skills/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/altinity/altinity-skills/main/altinity-expert-clickhouse/skills/altinity-expert-clickhouse-overview/SKILL.md | head -40
```

Both URLs return 200. After installing, review each altinity-expert-clickhouse/skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| altinity-expert-clickhouse-schema | Pass | Pass | Pass |
| altinity-expert-clickhouse-logs | Pass | Pass | Pass |
| altinity-expert-clickhouse-ingestion | Pass | Pass | Warn |
| altinity-expert-clickhouse-overview | Pass | Pass | Pass |
| altinity-expert-clickhouse-mutations | Pass | Pass | Pass |
| altinity-expert-clickhouse-merges | Pass | Pass | Pass |
| altinity-expert-clickhouse-metrics | Pass | Pass | Pass |
| altinity-expert-clickhouse-storage | Pass | Pass | Pass |
| altinity-expert-clickhouse-reporting | Pass | Pass | Warn |
| altinity-expert-clickhouse-replication | Pass | Pass | Pass |
| altinity-expert-clickhouse-memory | Pass | Pass | Warn |
| altinity-expert-clickhouse-dictionaries | Pass | Pass | Pass |

Across the 12 sampled skills there are 33 Pass, 3 Warn, and 0 Fail cells. Nine skills pass all three checks; three carry a single Snyk Warn each (ingestion, reporting, memory).

## Limitations

- Snapshot data, verified Nov 26, 2026: 1,948 combined installs across 27 indexed listings; 18 GitHub stars; Apache-2.0 license; last pushed Sep 17, 2026. Counts drift over time.
- The install index outruns the tree: altinity-clickhouse-expert, skill-installer, skill-creator, github-triage, codex-summarize-pipeline, clickhouse-profiler, and altinity-expert-clickhouse-audit carry install counts but have no matching directory in the current tree.
- skills.sh sampled only 12 of the 27 indexed listings; the other 15 carry no published verdict.
- Several indexed skill names duplicate the altinity-expert-clickhouse prefix and read as near-clones (for example altinity-clickhouse-expert and altinity-profiler-clickhouse vs clickhouse-profiler), which inflates the listing count without adding distinct tree content.
- The profiler and audit skills are maintained and released as a separate workflow group; the profiler is packaged on profiler-v* tags rather than as part of the expert skill set.

## Related

[ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup) | [PlanetScale Database Skills - MySQL & Postgres](/hermes/skills/catalog/planetscale-database-skills-setup) | [Neon Postgres Skills](/hermes/skills/catalog/neon-postgres-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start every diagnosis with altinity-expert-clickhouse-overview and let it route to the specialist module.
- Run the checks.sql files against the cluster for reproducible, query-backed findings instead of prose advice.
- Install the single-skill form (pointing at a skill directory) when you only need one module.
- Prefer the Docker image (ghcr.io/altinity/expert) for a self-contained Claude Code or Codex environment with the Altinity MCP server.
- Re-check the security pages on skills.sh for ingestion, reporting, and memory, which carry the sample's three Warns.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
