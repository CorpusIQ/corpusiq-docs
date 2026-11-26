---
title: "HelixDB Skills - Query, Memory, and Foundry MCP Setup"
description: "helixdb/skills - 3.7K combined installs: HelixDB query authoring, agent memory, and Helix Foundry MCP skills for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/helixdb-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "graph database", "helixdb", "memory"]
---

# HelixDB Skills - Setup Guide

**Source:** [helixdb/skills](https://www.skills.sh/helixdb/skills) via skills.sh - 3.7K combined installs across 18 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [helixdb/skills](https://github.com/helixdb/skills) - 6 stars, MIT license, last pushed Nov 22, 2026, main branch; skills live under skills/<name>/SKILL.md with shared docs, examples, and benchmarks alongside.
**Category:** Graph Database, Query, and Agent Memory (HelixDB)
**Quality Tier:** 🟡 Yellow - 9 of 18 listings sampled: no Fail verdicts, but five Snyk Warn cells across five query skills.

helixdb/skills covers Helix Foundry and HelixDB: query-authoring skills for the HelixDB v3 SDKs (Rust, TypeScript, Python, Go), translation skills for Cypher, Gremlin, SQL, and legacy HQL, a query optimizer, an agent memory system, and MCP skills for Helix Cloud and Helix Foundry. The query skills target the published SDK versions and produce direct POST /v2/query requests against a running Helix instance; the MCP skills read and act on Helix Cloud through a single server at https://mcp.helix-db.com/mcp, and the Foundry skills walk an ontology from nothing to a loaded, reviewable graph. All 18 indexed listings except helix-query-authoring have a matching skills/<name>/SKILL.md in the current tree.

## Installation

The README documents three install paths:

```bash
npx skills add HelixDB/skills
```

As a Claude Code plugin, which adds the Helix MCP for you:

```bash
claude plugin marketplace add HelixDB/skills
claude plugin install helixdb@helixdb
```

As a Gemini CLI extension:

```bash
gemini extensions install https://github.com/HelixDB/skills
```

The query skills assume a running Helix instance; to stand one up locally, install the Helix CLI (`curl -sSL "https://install.helix-db.com" | bash`), make sure Docker or Podman is running, then run `helix init local` and `helix start dev`.

## What It Provides

skills.sh publishes per-skill install counts for all 18 indexed listings. The 11 most-installed skills are listed below; the remaining 7 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| helix-query-json-dynamic | 325 | author and debug direct HelixDB v3 JSON query requests for POST /v2/query |
| helix-query-optimize | 324 | find and fix slow HelixDB queries: anchors, indexes, count plans, and search prefiltering |
| helix-query-from-cypher | 314 | run or port Cypher, Neo4j, openCypher, and SQL queries on HelixDB |
| helix-query-from-gremlin | 309 | translate Gremlin and TinkerPop traversals into HelixDB v3 DSL requests |
| helix-query-typescript | 300 | write and revise queries with the HelixDB TypeScript SDK (@helix-db/helix-db) |
| helix-memory-system | 299 | design and operate an agent memory system on HelixDB v3 SDKs (graph, vector, and BM25) |
| helix-query-from-hql | 285 | translate legacy HelixDB HQL (.hx) queries into v3 SDK requests |
| helix-query-rust | 284 | write and revise queries with the HelixDB Rust SDK (helix-db crate) |
| helix-query-go | 274 | write and revise queries with the HelixDB Go SDK |
| helix-cli | 273 | drive the helix CLI: local instances, the Cloud control plane, and the broker |
| helix-query-python | 267 | write and revise queries with the HelixDB Python SDK |

The remaining 7 indexed listings range from 29 to 133 installs.

## Why This Matters for Hermes Agents

These skills give an agent the exact request shapes and semantics of a v3 graph-plus-vector database, which is the kind of detail that trips up generic coding agents: batch envelopes, async index lifecycles, traversal-scoped vector and BM25 prefiltering, and retryable vs non-retryable errors. The translation skills (Cypher, Gremlin, HQL) are valuable because they tell the agent what to hand-translate and what the server natively supports, so an agent does not invent SQL outer joins or variable-length paths the engine rejects. helix-memory-system is the standout for agent work: it models the full memory lifecycle (generate, deduplicate, consolidate, forget, categorize) with hybrid recall over graph, vector, and BM25. For Helix Cloud, every query-authoring skill routes through helix-mcp first to read live indexes and observability, which keeps an agent from assuming an index exists. The MCP skills enforce confirmation gates before tenant, key, or Foundry mutations.

## Usage

| You say | What happens |
|---|---|
| Write this Helix query in TypeScript | Uses helix-query-typescript for readBatch/writeBatch and Client.query |
| Port this Cypher query | Uses helix-query-from-cypher to send natively or translate the rejected parts |
| Convert this Gremlin traversal | Uses helix-query-from-gremlin to map it to HelixDB v3 DSL |
| Optimize this slow query | Uses helix-query-optimize to fix anchors, indexes, and search prefiltering |
| Build agent memory for my app | Uses helix-memory-system for the full memory lifecycle and hybrid recall |
| Set up a Foundry ontology | Uses helix-foundry-onboarding to go from nothing to a loaded ontology |

## Verification

Confirm the README and two skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/helixdb/skills/main/skills/helix-query-typescript/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/helixdb/skills/main/skills/helix-memory-system/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| helix-query-json-dynamic | Pass | Pass | Pass |
| helix-query-optimize | Pass | Pass | Warn |
| helix-query-from-cypher | Pass | Pass | Pass |
| helix-query-from-gremlin | Pass | Pass | Pass |
| helix-query-typescript | Pass | Pass | Warn |
| helix-memory-system | Pass | Pass | Warn |
| helix-query-from-hql | Pass | Pass | Warn |
| helix-query-rust | Pass | Pass | Pass |
| helix-query-go | Pass | Pass | Warn |

Across the 9 sampled skills there are 22 Pass, 5 Warn, and 0 Fail cells. Four skills pass all three checks; helix-query-optimize, helix-query-typescript, helix-memory-system, helix-query-from-hql, and helix-query-go carry one Snyk Warn each.

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,705 combined installs across 18 indexed listings; 6 GitHub stars; MIT license; last pushed Nov 22, 2026. Counts drift over time.
- skills.sh sampled only 9 of the 18 indexed listings; the MCP skills, helix-cli, helix-query-python, and the Foundry skills carry no published verdict.
- helix-query-authoring carries an install count (29) but has no matching directory in the current tree and is not in the README's available-skill list.
- The query skills assume a running Helix instance and produce direct POST /v2/query requests; there is no compile or check step, the server validates queries.
- Installation commands stay unpinned; verify registry availability before changing release claims (per the README's source-canon note).

## Related

[Apollo GraphQL Skills - GraphQL and Rust Setup](/hermes/skills/catalog/apollographql-skills-setup) | [OpenClaw Graph New Skills - Procedural Generation, ARKit, Testing Setup](/hermes/skills/catalog/openclaw-graph-new-skills-setup) | [PlanetScale Database Skills - MySQL & Postgres](/hermes/skills/catalog/planetscale-database-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- For Helix Cloud, always let helix-mcp resolve the live database and read active indexes before authoring any query.
- Use helix-query-json-dynamic to inspect the raw request envelope when a query behaves unexpectedly.
- Pair helix-query-optimize with the /explain routes (Cypher and SQL) to see the plan before changing index choice.
- The memory system is TypeScript-first; the Rust variant lives in skills/helix-memory-system/EXAMPLES.rust.md.
- Helix Cloud has one MCP server now; the former admin-mcp and query-mcp hosts are retired, so point everything at https://mcp.helix-db.com/mcp.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
