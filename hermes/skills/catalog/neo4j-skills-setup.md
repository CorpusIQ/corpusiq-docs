---
title: "Neo4j Skills - Graph Database Agent Suite"
description: "neo4j-contrib/neo4j-skills: 24.1K combined installs. Thirty Neo4j skills for Cypher, modelling, drivers, imports, GraphRAG, GDS and Aura."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/neo4j-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "neo4j", "cypher", "graph database"]
---

# Neo4j Skills - Setup Guide

**Source:** [neo4j-contrib/neo4j-skills](https://www.skills.sh/neo4j-contrib/neo4j-skills) via skills.sh - 24.1K combined installs across 32 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [neo4j-contrib/neo4j-skills](https://github.com/neo4j-contrib/neo4j-skills) - 119 stars, MIT, branch main, last pushed 2026-10-26; 30 `SKILL.md` files, each in its own `neo4j-*-skill/` directory at the repository root, with plugin manifests for Claude Code, Codex, Antigravity and Gemini CLI plus an `mcp_config.json` and an `evals/` folder

**Category:** Neo4j graph database work for agents: Cypher, modelling, drivers and graph data science

**Quality Tier:** 🟡 Yellow - `neo4j-cypher-skill`, the most installed skill in the pack, carries a Snyk warn while Gen Agent Trust Hub and Socket both pass it, so the suite ships Yellow

This is the contribution track for Neo4j skills rather than a side project: the repository lives in the `neo4j-contrib` organisation, the plugin manifests list Neo4j as author with a `devrel@neo4j.com` contact, and the README points at the skills.sh listing as the install surface. Thirty skills cover the product in the shape the product actually has: querying and modelling, importing data, AI and search, graph data science, five official drivers, and the frameworks and platforms around the database.

The split by driver is the part that matters for agents. There is a Python skill, a JavaScript and TypeScript skill, a Java skill, a .NET skill and a Go skill, each with its own idioms instead of one generic driver document. The same is true of the platform skills: Kafka, Spark, Snowflake graph analytics, GraphQL, Spring Data, the Aura CLI and provisioning, the MCP server and the visualisation library all get their own skill with their own commands.

## Installation

The README's primary route is the skills CLI against the repository URL:

```bash
npx skills add https://github.com/neo4j-contrib/neo4j-skills
```

Claude Code uses the plugin marketplace, which is declared in `.claude-plugin/marketplace.json`:

```bash
/plugin marketplace add https://github.com/neo4j-contrib/neo4j-skills.git
/plugin install neo4j-skills@neo4j-skills-marketplace
```

Codex, Antigravity and Gemini CLI each get their own route, and the README documents all four in sequence: `codex plugin marketplace add neo4j-contrib/neo4j-skills` followed by `codex plugin add neo4j-skills@neo4j-skills-marketplace`, `agy plugin install https://github.com/neo4j-contrib/neo4j-skills` for Antigravity, and `gemini extensions install https://github.com/neo4j-contrib/neo4j-skills` for Gemini CLI. None of them targets Hermes, so the durable install is a directory copy that keeps each skill's `references/` and `scripts/` folders beside its `SKILL.md`:

```bash
git clone --depth 1 https://github.com/neo4j-contrib/neo4j-skills.git /tmp/neo4j-skills
cp -r /tmp/neo4j-skills/neo4j-*-skill ~/.hermes/profiles/corpusiq/skills/
```

Connection details come from the environment, and the README lists the four variables it expects: `NEO4J_URI` (`neo4j+s://<dbid>.databases.neo4j.io` on Aura or `neo4j://localhost:7687` locally), `NEO4J_USERNAME` (default `neo4j`), `NEO4J_PASSWORD`, and `NEO4J_DATABASE` (default `neo4j`). The bundled `mcp_config.json` declares the same four plus `NEO4J_READ_ONLY`, `NEO4J_TELEMETRY` and a schema sample size for the MCP server route.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| neo4j-cypher-skill | 1,551 | Writing, optimising and debugging Cypher queries, covering CYPHER 25 syntax, query planning, indexes and common patterns. |
| neo4j-modeling-skill | 1,174 | Designing and reviewing graph data models: node and relationship patterns, property choices and relational-to-graph migration. |
| neo4j-graphrag-skill | 1,146 | Building GraphRAG retrieval pipelines with `neo4j-graphrag`, including retriever selection (`VectorCypherRetriever`, `HybridCypherRetriever`), `retrieval_query` patterns and LangChain or LlamaIndex integration. |
| neo4j-driver-python-skill | 1,005 | The Python driver: `execute_query`, sessions, transactions, async, UNWIND batching and data types. |
| neo4j-document-import-skill | 950 | Extracting knowledge graphs from unstructured documents and PDFs with `SimpleKGPipeline`. |
| neo4j-query-tuning-skill | 933 | Diagnosing slow queries from execution plans: reading `EXPLAIN` and `PROFILE` output, spotting AllNodesScan, CartesianProduct and Eager operators, and prescribing indexes, hints, rewrites or a runtime change. |
| neo4j-vector-index-skill | 928 | Creating and querying vector indexes for semantic similarity search, covering index creation, embedding ingestion and `ai.text.embed()`. |
| neo4j-getting-started-skill | 910 | The zero-to-app walkthrough, provision then model then load then query, for first-time setup on Aura or Docker. |
| neo4j-agent-memory-skill | 903 | Graph-native agent memory: short-term conversations, long-term memory on the POLE+O entity model and reasoning traces, across NAMS, MCP, LangChain, CrewAI and ADK. |
| neo4j-gds-skill | 890 | Running Graph Data Science algorithms with the embedded GDS plugin on Aura Pro, self-managed, local or offline Neo4j. |
| neo4j-import-skill | 880 | Loading structured data from CSV and JSON via `LOAD CSV`, `neo4j-admin import` and the Data Importer GUI. |
| neo4j-security-skill | 845 | Programmatic security management: RBAC and ABAC, user and role lifecycle, privilege grants and denies, property-level and sub-graph access control, and LDAP or OIDC auth provider configuration. |
| neo4j-genai-plugin-skill | 834 | In-Cypher LLM integration through the `ai.text.*` functions: embeddings, text completion, structured output, chat, tokenisation and pure-Cypher GraphRAG. |
| neo4j-graphql-skill | 829 | Building GraphQL APIs over Neo4j with `@neo4j/graphql`: type definitions, `@relationship`, `@cypher` and filtering. |
| neo4j-aura-graph-analytics-skill | 819 | Serverless Aura Graph Analytics sessions through the Python client, or AuraDB Cypher API projection and session management. |
| neo4j-aura-provisioning-skill | 809 | Creating and managing Aura instances through the Aura CLI and REST API, covering async polling, credential handling and tier selection. |
| neo4j-kafka-skill | 791 | The Neo4j Connector for Kafka (sink and source) and the CDC API: Cypher, Pattern and CUD sink strategies, exactly-once semantics, DLQ handling, schema registry and `db.cdc.query` cursor loops. |
| neo4j-driver-java-skill | 791 | The Java driver: `ExecutableQuery`, managed and explicit transactions, object mapping and reactive sessions. |
| neo4j-spark-skill | 790 | Reading and writing Neo4j from Apache Spark or Databricks with the Neo4j Connector for Apache Spark 6.0 or 5.x, including DataFrame reads and writes, partitioning and Databricks secrets. |
| neo4j-driver-go-skill | 789 | The Go driver v6: `ExecuteQuery`, generic helpers, spatial types and connection configuration. |

The remaining 12 indexed listings range from 1 to 780 installs.

## Why This Matters for Hermes Agents

Graph work is where general coding models are most confidently wrong. Cypher has a small surface and sharp edges, and an agent that writes a query that returns the right answer on a 200-node test graph will happily write one that scans a production graph without an index. `neo4j-cypher-skill` and `neo4j-query-tuning-skill` are the pair that prevents it: one teaches the syntax and the patterns, the other reads execution plans and prescribes the fix.

The driver split is more useful than it looks. A Python driver question and a Go driver question have different answers, different idioms and different APIs, and a single generic driver skill would blend them. Five separate skills, each sourced from that driver's own documentation, avoid the blend.

The AI-adjacent skills are the second reason to install this. `neo4j-graphrag-skill`, `neo4j-vector-index-skill`, `neo4j-genai-plugin-skill` and `neo4j-agent-memory-skill` cover retrieval over a graph, vector indexes inside the database, LLM calls from inside Cypher and graph-native memory for agents. Those are the questions a profile building retrieval actually asks, and having the answers as skills rather than as blog posts changes how often the agent reaches for the right pattern.

Finally, the operational skills make it deployable rather than theoretical. `neo4j-aura-provisioning-skill`, `neo4j-cli-tools-skill`, `neo4j-security-skill` and `neo4j-migration-skill` cover creating instances, running admin commands, managing users and roles, and upgrading from 4.x or 5.x. That is the difference between a query helper and something an agent can drive end to end on a real deployment.

## Usage

| You say | What happens |
|---|---|
| "Write a Cypher query for customers who bought twice last quarter" | `neo4j-cypher-skill` writes the query against the loaded schema and checks the pattern against its index and planning notes. |
| "This query takes 40 seconds, why" | `neo4j-query-tuning-skill` reads the `PROFILE` output, names the offending operator, and prescribes an index, a hint or a rewrite with the runtime choice. |
| "Design a graph model for a supply chain" | `neo4j-modeling-skill` proposes nodes and relationships, argues the property choices and flags the bits that will not migrate cleanly from relational. |
| "Load this CSV into the graph" | `neo4j-import-skill` picks between `LOAD CSV`, `neo4j-admin import` and the Data Importer, and writes the statement for the file at hand. |
| "Add retrieval to our RAG pipeline" | `neo4j-graphrag-skill` selects a retriever, writes the `retrieval_query`, and wires the LangChain or LlamaIndex integration. |
| "Give the agent memory between sessions" | `neo4j-agent-memory-skill` sets up short-term and long-term memory on the POLE+O model, with the MCP or framework integration. |
| "Stream changes from Neo4j into Kafka" | `neo4j-kafka-skill` configures the source connector or the CDC cursor loop, with exactly-once semantics and DLQ handling. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} neo4j-cypher-skill\n" \
  https://raw.githubusercontent.com/neo4j-contrib/neo4j-skills/main/neo4j-cypher-skill/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and that the reference folders came along, since the depth lives in `references/` rather than in the entry file:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/neo4j-*-skill/ | wc -l
head -4 ~/.hermes/profiles/corpusiq/skills/neo4j-cypher-skill/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/neo4j-cypher-skill/references | wc -l
```

The count should print 30, the header should show `name: neo4j-cypher-skill` with its description, and the reference listing should be non-zero. Note that 30 is the directory count, while skills.sh indexes 32 listings for this repository.

## Security

One of the five sampled skills carries a warn: `neo4j-cypher-skill` is flagged by Snyk while Gen Agent Trust Hub and Socket both pass it. The other four sampled skills are clean across all three scanners.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| neo4j-cypher-skill | Pass | Pass | Warn |
| neo4j-agent-memory-skill | Pass | Pass | Pass |
| neo4j-kafka-skill | Pass | Pass | Pass |
| neo4j-mcp-skill | Pass | Pass | Pass |
| neo4j-vector-search-skill | Pass | Pass | Pass |

The content is markdown plus eleven Python scripts. They are ordinary operational helpers: schema definition and import under `neo4j-cypher-skill/scripts/`, agent management and evaluation under `neo4j-aura-agent-skill/scripts/`, query validation under `neo4j-getting-started-skill/scripts/`, and the repository's own `scripts/lint_skills.py` and `scripts/bump-version.py`. Nothing installs a package, and nothing phones home: the skills act on whatever database the environment points them at.

That database connection is the part to settle before deployment. Every skill inherits `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD` and `NEO4J_DATABASE` from the environment, and the bundled `mcp_config.json` passes them to the MCP server by variable reference rather than by value, which is the right shape. Keep the password in the environment or the MCP configuration, never in a prompt or in a file the agent writes, and use `NEO4J_READ_ONLY` where the work is read-only, because `neo4j-security-skill` is perfectly capable of creating users and granting privileges once connected.

Licensing needs one check. The `LICENSE` file is MIT, copyright Neo4j Contrib, while `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` both declare `"license": "Apache-2.0"`. The licence file wins for redistribution, but the manifests disagree with it and that is worth knowing before vendoring the skill text anywhere.

## Limitations

- Snapshot data, verified 2026-10-31: 24,115 combined installs across 32 indexed listings; 119 GitHub stars; MIT; last pushed 2026-10-26. Counts drift over time.
- Two indexed listings have no matching directory in the tree: `neo4j-agent-memory` (5 installs) and `neo4j-vector-search-skill` (1 install). The names suggest near-duplicates of `neo4j-agent-memory-skill` and `neo4j-vector-index-skill`, but nothing in the repository confirms that, so treat them as unresolved rather than renamed.
- The threshold table stops at 789 installs, which leaves twelve listings out, and they are not all noise: `neo4j-migration-skill` (494), `neo4j-driver-javascript-skill` (416), `neo4j-spring-data-skill` (403) and `neo4j-ontology-skill` (47) are real skills below the line. Read the tail before concluding the pack has no migration or JavaScript coverage.
- The licence metadata contradicts itself: MIT in the `LICENSE` file, Apache-2.0 in the Claude Code and Codex plugin manifests. Confirm which applies before redistributing.
- Every skill expects a live database and the four `NEO4J_*` variables. Without them the skills can explain Cypher but cannot run a query, and the scripts fail at connect rather than at parse.
- The four documented install routes target the skills CLI, Claude Code, Codex, Antigravity and Gemini CLI, and none targets Hermes. The directory copy above follows the repository layout by hand.
- `neo4j-cypher-skill` is the most installed skill in the pack and the one carrying the Snyk warn, so the entry point needs the most scrutiny rather than the least.

## Related

- [Upstash Skills - Serverless Backend Setup](/hermes/skills/catalog/upstash-skills-setup)
- [Tigris Data Skills - Object Storage for Agents](/hermes/skills/catalog/tigrisdata-skills-setup)
- [Metabase Skills - BI and Dashboard Agent Suite](/hermes/skills/catalog/metabase-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the Cypher and query tuning pair together. Writing Cypher and diagnosing it are separate skills, and a profile with only the first will produce queries nobody can explain the cost of.
- Match the driver skill to the language in the repository before asking anything driver-specific. The Python, JavaScript, Java, .NET and Go skills carry different APIs and different idioms.
- Set `NEO4J_READ_ONLY` for profiles doing analysis, and leave it unset only where the work genuinely needs writes, since provisioning, security and migration skills all act on the live instance.
- Start with `neo4j-getting-started-skill` on a fresh machine. It walks provision, model, load and query in order, which is faster than assembling the same sequence from four skills.
- Use `neo4j-mcp-skill` and `mcp_config.json` when the agent should reach the database through tools rather than through shell commands, and prefer the variable-reference configuration the repository ships over pasting credentials into a config file.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
