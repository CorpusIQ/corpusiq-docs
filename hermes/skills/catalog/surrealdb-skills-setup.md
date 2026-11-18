---
title: "SurrealDB Agent Skills - Official Database Skills Setup"
description: "surrealdb/agent-skills: 4.9K combined installs across 10 listings; official SurrealDB skills for SurrealQL, vectors, SDKs, and schema management."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/surrealdb-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "surrealdb", "surrealql", "database"]
---

# SurrealDB Agent Skills - Setup Guide

**Source:** [surrealdb/agent-skills](https://www.skills.sh/surrealdb/agent-skills) via skills.sh - 4.9K combined installs across 10 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 28 stars, MIT license, `main` branch, last pushed 2026-09-29. Skills live under `skills/<name>/` with a SKILL.md plus optional `references/` files for detailed documentation.
**Category:** Official SurrealDB database skills
**Quality Tier:** 🟡 Yellow - 29 Pass and 1 Warn across the 30 sampled verdict cells; MIT licence.

SurrealDB publishes these ten skills as the official agent companion to its database. They are provider-neutral agent skills (folders of instructions, scripts, and resources) that work with Claude Code, GitHub Copilot, Cursor, Cline, and most other agents. The set covers the SurrealQL query language, vector search, performance tuning, the built-in function catalog, the Python and JavaScript SDKs, the `surreal` CLI, and SurrealKit schema management. Because the repository carries only ten indexed listings, the whole roster is shown below.

## Installation

Install all ten skills with one command:

```bash
npx skills add surrealdb/agent-skills
```

Install a specific skill with `--skill`:

```bash
npx skills add surrealdb/agent-skills --skill surrealql
npx skills add surrealdb/agent-skills --skill surrealdb-vector
```

For a local install, clone the repository and copy the `skills/` directory to where your agent reads its skills:

```bash
git clone https://github.com/surrealdb/agent-skills.git
```

The skills follow the Agent Skills open standard: each has a required SKILL.md manifest and optional `references/` files for detailed documentation. Once installed they are available automatically, and the agent uses them when relevant tasks are detected.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| surrealql | 816 | Generates and modifies SurrealQL queries for records, schemas, graph relationships, and live queries. |
| surrealdb-vector | 636 | Vector search with SurrealDB using HNSW indexes, KNN queries, and similarity scoring for semantic search and RAG. |
| surrealql-performance | 524 | Optimizes SurrealDB performance through record ID and key design, indexing strategy, and computed fields. |
| surrealql-functions | 522 | Discovers built-in SurrealQL functions with version-current signatures via the language server and tree-sitter grammar. |
| surrealdb-python | 521 | Connects to SurrealDB from Python with the SDK in client/server and embedded modes, plus CRUD operations. |
| surrealdb-cli | 505 | Runs and operates SurrealDB from the terminal with the surreal binary: server, SQL REPL, import/export, and maintenance. |
| surrealkit | 500 | Manages and migrates SurrealDB schemas with SurrealKit: scaffolding, sync, rollouts, typegen, and tests. |

The remaining 3 indexed listings range from 184 to 488 installs.

## Why This Matters for Hermes Agents

These are the vendor's own skills, so SurrealQL syntax, function signatures, and CLI usage stay current with the SurrealDB release you run. The documentation skills are read-only and send only search terms and doc paths to surrealdb.com, which keeps agent context small instead of pasting the docs wholesale.

For a Hermes agent, the practical value is deterministic database work: schema design, vector indexes, and migrations come from the same source the vendor maintains, which matters when a wrong query is costly at the database layer.

## Usage

| You say | What happens |
|---|---|
| "Write a SurrealQL query to find users who follow each other" | Uses $surrealql to generate the query and explain its schema and graph relationship pieces. |
| "Create an HNSW vector index for semantic search on my documents table" | Uses $surrealdb-vector to define the index and the KNN query. |
| "My queries are slow, help me tune this" | Uses $surrealql-performance to review record ID design, indexes, and computed fields. |
| "What is the signature for string::lowercase?" | Uses $surrealql-functions to look up the built-in function signature for your version. |
| "Connect to SurrealDB from my Python app" | Uses $surrealdb-python to set up the SDK in client/server or embedded mode. |
| "Start a local SurrealDB server and import a backup" | Uses $surrealdb-cli to run the surreal binary with start, import, and export. |
| "Set up schema migrations for my project" | Uses $surrealkit to scaffold, sync, and roll out schema changes. |

## Verification

Probe one skill on the `main` branch before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/surrealdb/agent-skills/main/skills/surrealql/SKILL.md | head -12
```

Then install and confirm the skill directory is present:

```bash
npx skills add surrealdb/agent-skills
```

The README documents no test suite. Each skill ships a SKILL.md manifest plus optional reference files, so verification means reading the manifest and running one skill once.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| surrealql | Pass | Pass | Pass |
| surrealdb-vector | Pass | Pass | Pass |
| surrealql-performance | Pass | Pass | Pass |
| surrealql-functions | Pass | Pass | Pass |
| surrealdb-python | Pass | Pass | Pass |
| surrealdb-cli | Pass | Pass | Pass |
| surrealkit | Pass | Pass | Pass |
| surrealdb-js | Pass | Pass | Pass |
| surrealdb-docs | Pass | Warn | Pass |
| surrealdb-agent-memory-docs | Pass | Pass | Pass |

The sample covers all 10 indexed listings; the single Warn is a Socket flag on the surrealdb-docs listing.

## Limitations

- Snapshot data, verified Nov 18, 2026: 4,947 combined installs across 10 indexed listings; 28 GitHub stars; MIT license; last pushed 2026-09-29. Counts drift over time.
- Three listings are not shown above: surrealdb-js and the two documentation skills, which range from 184 to 488 installs.
- The documentation skills send search terms and doc paths to surrealdb.com, so those two need network access while the others are self-contained.
- The query and function skills describe version-current SurrealQL; results may differ if the running SurrealDB server is on an older release.
- A local install means copying the `skills/` directory into your agent's skill path by hand; only the npx path places the skills for you.

## Related

- [OpenAI Codex Skills - Official Skills Catalog Setup](/hermes/skills/catalog/openai-codex-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [CodeStable Skills - AI Coding Workflow Setup](/hermes/skills/catalog/codestable-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole set once; the ten skills are small and the agent picks the right one per task.
- Use $surrealql for day-to-day queries and reach for $surrealql-performance only when a query is slow.
- Let $surrealkit own schema migrations instead of hand-editing DEFINE statements; it adds rollback, typegen, and tests.
- Pair $surrealdb-vector with the Python or JavaScript SDK skills when building semantic search so the index and the client line up.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
