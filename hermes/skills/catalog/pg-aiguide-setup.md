---
title: "pg-aiguide - Postgres Skills from Timescale"
description: "timescale/pg-aiguide on skills.sh: 5.6K combined installs across 12 listings; Postgres schema, pgvector and TimescaleDB skills for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pg-aiguide-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "postgres", "pgvector", "timescaledb"]
---

# pg-aiguide - Setup Guide

**Source:** [timescale/pg-aiguide](https://www.skills.sh/timescale/pg-aiguide) via skills.sh - 5.6K combined installs across 12 indexed listings; first seen 2026-11-07 (Nov 7, 2026 morning sweep)
**GitHub:** 1,885 stars, Apache-2.0, branch `main`, last pushed 2026-11-06, 11 `SKILL.md` directories under `skills/<name>/`, with a `.claude-plugin` manifest and `CLAUDE.md` at the repository root
**Category:** Postgres expertise for agents: schema design, vector and hybrid search, migrations and TimescaleDB hypertables
**Quality Tier:** 🟢 Green - all five sampled skills pass Gen Agent Trust Hub, Socket and Snyk, the repository is Apache-2.0 with a LICENSE file, and the skill tree is markdown only with no executable helpers.

pg-aiguide is Timescale's (TigerData's) PostgreSQL expertise pack for coding assistants. It ships three things: a set of curated Postgres best-practice skills, semantic search over the official PostgreSQL manual scoped by version, and extension documentation starting with TimescaleDB and PostGIS. The README's pitch is that AI tools generate Postgres code that is outdated, missing constraints and indexes, unaware of modern features and inconsistent with real practice, and that versioned knowledge fixes it.

The demo in the README is worth quoting because it is the whole argument. The same e-commerce schema prompt ran twice against Claude Code, once with the companion MCP server off and once on: 4x more constraints, 55% more indexes including partial and expression indexes, PG17-recommended patterns, and modern features such as `GENERATED ALWAYS AS IDENTITY` and `NULLS NOT DISTINCT`. Treat that as the vendor's own measurement, not an independent benchmark.

The skills themselves are short and trigger-shaped. Their frontmatter is a list of "use this skill when the user asks to" bullets plus keywords, which is what makes them load reliably: the agent matches on the trigger list, then reads the body.

## Installation

Three install surfaces are documented in the README. The skills route first, verbatim:

```bash
npx skills add timescale/pg-aiguide --skill postgres
npx skills add timescale/pg-aiguide --skill schema-exploration
npx skills add timescale/pg-aiguide
```

The first installs the umbrella `postgres` skill, the second installs the schema exploration skill for inspecting an existing database, and the third opens an interactive picker. The README states the skills route works with Claude Code, Cursor, Codex, Gemini CLI, VS Code and 40+ other agents.

The second surface is the public MCP server, which gives the agent semantic search across the PostgreSQL, TimescaleDB and PostGIS manuals:

```json
{
  "mcpServers": {
    "pg-aiguide": {
      "url": "https://mcp.tigerdata.com/docs"
    }
  }
}
```

Other documented clients use their own commands, for example `codex mcp add --url "https://mcp.tigerdata.com/docs" pg-aiguide` and `gemini mcp add -s user pg-aiguide "https://mcp.tigerdata.com/docs" -t http`.

The third surface is the Claude Code plugin, which the README describes as using the skills in the `skills` directory plus the hosted MCP endpoint:

```bash
claude plugin marketplace add timescale/pg-aiguide
claude plugin install pg@aiguide
```

The skills and the MCP server are independent. Installing skills alone gives the agent rules; adding the MCP server gives it documentation search. The README recommends both when you want the deeper result.

## What It Provides

Four listings clear the 500-install threshold, and they map cleanly onto the main Postgres jobs: general work, vectors, table design and time-series.

| Skill | Installs | Use For |
|---|---|---|
| postgres | 1,436 | The umbrella entry skill: table design, indexing, data types, constraints, extensions including pgvector, PostGIS and TimescaleDB, search and migrations |
| pgvector-semantic-search | 984 | Vector similarity search with pgvector for embeddings, RAG and semantic search, including HNSW and IVFFlat index configuration |
| design-postgres-tables | 643 | General PostgreSQL table design: data types, constraints, indexes, JSONB patterns, partitioning and identity columns |
| setup-timescaledb-hypertables | 529 | Hypertables for time-series, IoT, metrics, events and log data, with compression, retention policies and continuous aggregates |

The remaining 8 indexed listings range from 33 to 406 installs.

The tail is not filler. `find-hypertable-candidates` (406) analyses an existing database and names the tables that should become hypertables, `postgres-hybrid-text-search` (390) implements BM25 plus vector search with Reciprocal Rank Fusion, `design-postgis-tables` (369) covers geometry types, coordinate systems and spatial indexing, `migrate-postgres-tables-to-hypertables` (367) does the conversion with validation, `postgres-database-migration` (255) plans safe schema migrations on production data, `schema-exploration` (89) inspects what already exists, `ghost-database` (61) is indexed without a directory in the current tree, and `timescaledb-hyperfunctions` (33) covers the TimescaleDB function library.

The `postgres` skill is the one that carries the routing logic. Its description lists the triggers for every other area, so installing it alone gives the agent a map of when to go deeper, at the cost of a longer file in context.

## Why This Matters for Hermes Agents

Postgres is the default database for most projects an agent touches, and the failure mode is well known: a model writes `SERIAL` where identity columns belong, skips the index that the query pattern needs, stores money in `float`, or invents a migration that locks a hot table. These skills put the current best practice in front of the agent at the moment it writes DDL.

The second reason is version awareness. Postgres features arrive per major version, and a model's training data is a blur across versions. The MCP server scopes manual search by version, which is the difference between advice that applies to the cluster in front of you and advice that applies to a version three years old.

The third is that the extensions are covered, not assumed. pgvector, PostGIS and TimescaleDB each have their own conventions (index types, quantization, chunk intervals, geometry types), and the skills that clear the threshold here are exactly those extension skills. An agent that knows `halfvec` and `ef_search` writes a different index than one that only knows "add an index".

The fourth is that the skills are cheap. They are markdown trigger lists, so a Hermes agent can load one when a task is about vectors and ignore the other ten, instead of carrying a whole database handbook in context.

## Usage

| You say | What happens |
|---|---|
| "Design a schema for an IoT sensor platform" | `setup-timescaledb-hypertables` supplies the hypertable shape: partition column, segment_by, order_by, chunk interval, compression and retention |
| "Add semantic search over our documents" | `pgvector-semantic-search` picks the vector type, sets up HNSW with tuned m and ef_construction, and covers filtered search |
| "Review this table definition" | `design-postgres-tables` checks data types, constraints, keys, JSONB usage and index choices against current practice |
| "Which of our tables should become hypertables?" | `find-hypertable-candidates` inspects the schema and returns a ranked candidate list, then `migrate-postgres-tables-to-hypertables` does the move |
| "We need keyword search plus embeddings" | `postgres-hybrid-text-search` combines BM25 with vector search through Reciprocal Rank Fusion |
| "Plan a zero-downtime migration for this column change" | `postgres-database-migration` produces a staged plan, including how to test and roll back |
| "What does this existing database contain?" | `schema-exploration` walks the catalogs and reports objects and relationships before anything is changed |

## Verification

Read the entry skill before installing. Both paths returned HTTP 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/timescale/pg-aiguide/main/skills/postgres/SKILL.md | head -30
curl -fsSL https://raw.githubusercontent.com/timescale/pg-aiguide/main/skills/pgvector-semantic-search/SKILL.md | head -30
```

The first should open with `name: postgres` and a description that begins "Use this skill for any PostgreSQL database work", followed by the trigger list. The second should name HNSW, IVFFlat and halfvec in its coverage line.

After install, confirm you have the skill directories you asked for and count them against the index, which lists one more than the tree holds:

```bash
ls .agents/skills | wc -l
```

If you installed all of them from a clone, `ls skills | wc -l` in the repository returns 11 directories against 12 indexed listings.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| postgres | Pass | Pass | Pass |
| setup-timescaledb-hypertables | Pass | Pass | Pass |
| design-postgis-tables | Pass | Pass | Pass |
| schema-exploration | Pass | Pass | Pass |
| timescaledb-hyperfunctions | Pass | Pass | Pass |

The skill tree is markdown. A recursive listing of the repository shows `SKILL.md` files and `references/` directories with no scripts, no hooks and no post-install steps, so the install risk is the ordinary one of putting instructions in front of an agent.

The MCP server is a different trust boundary. It is a hosted endpoint at `mcp.tigerdata.com`, so queries and the documentation excerpts the agent retrieves travel to TigerData's service, and the answers depend on that service being up. Enabling it is a data-flow decision, not just a convenience. If you only need the rules, install the skills and skip the server.

The licence is Apache-2.0 with a LICENSE file in the root, so reuse and redistribution are on standard terms.

## Limitations

- Snapshot data, verified 2026-11-07: 5,562 combined installs across 12 indexed listings; 1,885 GitHub stars; Apache-2.0; last pushed 2026-11-06. Counts drift over time.
- Index and tree disagree by one: 12 indexed listings against 11 `SKILL.md` directories, and `ghost-database` (61 installs) has no directory in the current tree, so its behaviour is not verifiable from the source.
- The distribution is steep. Four listings carry the threshold, and the other eight sit between 33 and 406 installs, so most of the suite is lightly exercised.
- The frontmatter descriptions are trigger lists, not documentation. Use For text here is condensed from each `SKILL.md`; the actual guidance lives in the body and is worth reading before trusting it on a production database.
- TimescaleDB and PostGIS are first-class, while the README lists pgvector documentation as "coming soon" in the ecosystem section even though the pgvector skill exists. Expect the newer extension docs to trail the skills.
- The MCP server is a hosted third-party endpoint. Its availability, rate limits and data handling are TigerData's to change, and nothing in the skill files pins it.

## Related

- [Neon Agent Skills - Serverless Postgres Platform](/hermes/skills/catalog/neon-agent-skills-setup)
- [Supabase Server Skill - Edge Function Auth Setup](/hermes/skills/catalog/supabase-server-skills-setup)
- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `postgres` first and let it route. Its trigger list names every other skill's territory, so the agent asks for the specialised one when the task moves into vectors or hypertables.
- Pair it with the MCP server only for schema-design work. Documentation search pays off when the agent must cite a manual page; for routine DDL review the skills alone are enough.
- Say the version out loud. "Postgres 16 on RDS" gets version-appropriate advice from the server, while an unqualified prompt gets the generic path.
- Use `schema-exploration` before any migration prompt. Agents write migrations against the schema they imagine, and this skill replaces the imagination with the catalog.
- Check hypertable candidates before designing new tables on a Timescale cluster. The 406-install candidate finder is the most reusable piece in the tail.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
