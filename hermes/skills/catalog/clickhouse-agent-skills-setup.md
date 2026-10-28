---
title: "ClickHouse Agent Skills - Official Analytics Suite Setup"
description: "Official ClickHouse skills: 83.2K combined installs. Schema and query rules, architecture decisions, chDB SQL, and clickhousectl cloud infra."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/clickhouse-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "clickhouse", "analytics", "database"]
---

# ClickHouse Agent Skills - Setup Guide

**Source:** [clickhouse/agent-skills](https://www.skills.sh/clickhouse/agent-skills) via skills.sh - 83.2K combined installs across 11 indexed listings; snapshot 2026-10-28 (Oct 28 morning sweep)

**GitHub:** [clickhouse/agent-skills](https://github.com/clickhouse/agent-skills) - 561 stars, Apache-2.0, branch main, last pushed 2026-10-19, 11 skill directories under `skills/`, plus a Claude Code marketplace manifest carrying 8 plugin entries

**Category:** Analytics databases: ClickHouse schema and query practice, chDB in Python, cloud infrastructure

**Quality Tier:** 🟡 Beta - vendor maintained by ClickHouse Inc with 561 GitHub stars, but one Snyk Fail and one Snyk Warn sit in the sampled security verdicts, so read the Security section before installing the cloud skills

ClickHouse Inc publishes the official skill set for its own database. It targets open-source ClickHouse, managed ClickHouse Cloud and chdb, the in-process build of ClickHouse for Python, and the skills are agent-agnostic: each directory under `skills/` holds a self-contained `SKILL.md`, most of them with their own rules, references or examples, and the README maps the config directory for ten agents from Claude Code and Cursor to Copilot, Gemini CLI, Codex and Goose, then names 13 more.

The design is unusually close to documentation engineering. `clickhouse-best-practices` is a rule corpus rather than an essay, with one file per rule and incorrect versus correct SQL examples plus impact notes where they apply. `clickhouse-architecture-advisor` sits above it and answers the design questions a rule list cannot: ingestion strategy, join and enrichment patterns, late-arriving data and upserts, time-series partitioning and real-time pre-aggregation, with every recommendation labelled `official`, `derived` or `field`. The infrastructure skills then hand the agent a real CLI surface, `clickhousectl`, for local servers and cloud services instead of leaving it to improvise commands.

## Installation

The README documents two install routes. The first is the skills.sh CLI, which auto-detects installed agents and prompts for a destination:

```bash
npx skills add clickhouse/agent-skills
```

The second uses the ClickHouse CLI itself:

```bash
clickhousectl skills
```

If `clickhousectl` is not on the machine yet, the infrastructure skills install it from a remote script, which is the spelling the repo uses:

```bash
curl -fsSL https://clickhouse.com/cli | sh
```

The chDB skills have their own runtime prerequisite, documented in their frontmatter and quick-start sections. The Python package is not installed by the skill installer:

```bash
pip install chdb
```

For any agent without a native installer path, the tree is the install source: clone the repository and copy the directories you want into your agent's skills directory.

```bash
git clone --depth 1 https://github.com/clickhouse/agent-skills.git
cp -R agent-skills/skills/clickhouse-best-practices ~/.hermes/profiles/corpusiq/skills/
```

The repository also ships a Claude Code marketplace manifest at `.claude-plugin/marketplace.json` with 8 plugin entries, but the README does not spell out a `claude plugin install` command, so confirm the entry name against the manifest before running one.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| clickhouse-best-practices | 21,833 | Reviewing a ClickHouse schema or query against the rule corpus: primary key and `ORDER BY` selection, data types, JOIN order and `PREWHERE`, insert batching, mutation avoidance, partitioning, skipping indices, materialized views and `OPTIMIZE` avoidance. |
| clickhouse-architecture-advisor | 9,943 | Deciding how a ClickHouse deployment should be shaped: ingestion strategy, join and enrichment patterns, late-arriving data and upserts, time-series partitioning and real-time pre-aggregation, each answer labelled official, derived or field guidance. |
| chdb-sql | 9,006 | Running analytical SQL with no server, in Python: `chdb.query()` on parquet, CSV, JSON, URLs, S3 and remote databases, `Session` for stateful pipelines, DB-API 2.0, parametrized queries, UDFs and streaming. |
| chdb-datastore | 7,925 | Replacing slow pandas code: the same DataFrame API backed by ClickHouse, readers for 16 or more sources including MySQL, Postgres, MongoDB, ClickHouse Cloud, Iceberg and Delta Lake, plus joins across those sources. |
| clickhouse-managed-postgres-rca | 6,632 | Root-causing slowness on a ClickHouse-managed Postgres service: one Prometheus scrape for cache hit ratio, connections and memory, per-digest evidence from the Slow Query Patterns API, then a recommended fix it does not apply. |
| clickhouse-js-node-rowbinary | 6,419 | Parsing or producing `RowBinary`, `RowBinaryWithNames` and `RowBinaryWithNamesAndTypes` streams in TypeScript or JavaScript against the ClickHouse HTTP interface, with reader and writer guides and a test suite. |
| clickstack-otel-collector | 4,908 | Wiring an OpenTelemetry collector into a Managed ClickStack service: deploying a collector with Docker or Compose, configuring an existing one, creating a dedicated ingest SQL user, sending synthetic telemetry and verifying it lands. |
| infra-clickhouse | 4,499 | Standing up ClickHouse with `clickhousectl`: local install and server start, schema creation and seed data, then ClickHouse Cloud authentication, service creation, schema migration and application connection. |
| clickhousectl-local-dev | 4,483 | No directory in the current tree: the README states `infra-clickhouse` supersedes this listing, and its local workflow is the one that now covers install, server start, schemas and seed data. |
| clickhousectl-cloud-deploy | 4,276 | No directory in the current tree either: superseded by `infra-clickhouse`, whose cloud reference covers authenticate, create a service, migrate schemas and connect an application. |
| infra-postgres | 3,322 | Running Postgres with `clickhousectl`: local Docker-backed development with psql access and `.env` wiring, managed ClickHouse Cloud Postgres in beta with TLS, replicas, failover and point-in-time restore, and `pg_dump` migration from Neon, Supabase or RDS. |

All 11 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

ClickHouse punishes habits that general SQL knowledge rewards. An agent that writes `UPDATE` statements, inserts row by row, or picks a random column for `ORDER BY` produces a schema that looks correct in review and degrades for months, because sort key and partition choices are expensive to change once data lands. The rule corpus exists precisely to be cited at that moment, and it is written so an agent can name the rule it applied rather than assert a preference.

The two chDB skills change what a Hermes job can do without infrastructure. A cron job analyzing a parquet export normally needs a warehouse connection or a pandas script that runs out of memory; `chdb-sql` runs ClickHouse SQL in process, and `chdb-datastore` keeps the pandas API while swapping the engine underneath, including reads from S3 or Postgres and joins across them.

The provenance labels in `clickhouse-architecture-advisor` are the feature most worth copying into other suites. Marking advice as `official`, `derived` or `field` lets a reviewing agent separate vendor policy from inference from operational experience, which is exactly the distinction that gets lost when a skill file reads as one confident voice.

The infrastructure skills are the part to install with intent. `infra-clickhouse`, `infra-postgres` and `clickstack-otel-collector` all drive `clickhousectl` against ClickHouse Cloud, which means an agent session can create services, ingest credentials and issue queries on a real account. That is valuable for setup work and unsuitable for an unattended agent with a broad API key.

## Usage

| You say | What happens |
|---|---|
| "Design a table for user events with a JSON properties column" | clickhouse-best-practices picks the sort key and types from its data type and primary key rules, and clickhouse-architecture-advisor answers the ingestion and partitioning questions that the rule list leaves open. |
| "This dashboard query takes nine seconds, fix it" | The agent reads the query against the indexing, `PREWHERE` and JOIN rules, explains which rule each change follows, then rewrites the query and states the impact it expects. |
| "Load this parquet file, group by country, take the top ten by revenue" | chdb-sql runs the SQL in process with no server, or chdb-datastore does the same through pandas syntax if the surrounding code is already pandas. |
| "Join my MySQL customers table to a local orders file" | chdb-datastore reads both sources and joins them in one DataFrame, or chdb-sql does it with the `mysql()` table function inside a `Session`. |
| "Give me a local ClickHouse I can develop against, then push it to Cloud" | infra-clickhouse installs and starts a local server, creates the schema, seeds data, then authenticates to Cloud, creates the service, migrates the schema and connects the application. |
| "Our managed Postgres is slow and CPU is pinned" | clickhouse-managed-postgres-rca scrapes the Prometheus endpoint once, pulls per-digest latency from the Slow Query Patterns API, reasons from IO and timing signals, and recommends a fix without applying it. |
| "Send test telemetry into our ClickStack service" | clickstack-otel-collector deploys a collector, creates a dedicated ingest user, sends synthetic logs, traces and metrics, then verifies they are visible in ClickStack. |

## Verification

The canonical layout is one directory per skill on `main`. All seven paths below returned 200 when this guide was written, five in the loop and the two review links after it:

```bash
for p in skills/clickhouse-best-practices/SKILL.md \
         skills/clickhouse-managed-postgres-rca/SKILL.md \
         skills/chdb-sql/SKILL.md \
         skills/infra-clickhouse/SKILL.md \
         skills/clickhouse-js-node-rowbinary/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/clickhouse/agent-skills/main/$p"
done
```

Read the two that touch a live account before installing them:

- https://raw.githubusercontent.com/clickhouse/agent-skills/main/skills/clickhouse-managed-postgres-rca/SKILL.md
- https://raw.githubusercontent.com/clickhouse/agent-skills/main/skills/infra-postgres/SKILL.md

After install, confirm what landed rather than trusting the installer's summary:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -cE '^(clickhouse|chdb|clickstack|infra)-'
head -5 ~/.hermes/profiles/corpusiq/skills/clickhouse-best-practices/SKILL.md
```

The `head` output should show the frontmatter name `clickhouse-best-practices`, which is also the name the install index uses. For the Python side, the chDB skills ship their own environment check, a local script that verifies the Python version, imports chdb, runs a basic query, checks DataFrame output and exercises `Session` and a parametrized query:

```bash
python3 ~/.hermes/profiles/corpusiq/skills/chdb-sql/scripts/verify_install.py
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| clickhouse-best-practices | Pass | Pass | Pass |
| clickhouse-architecture-advisor | Pass | Pass | Pass |
| chdb-sql | Pass | Pass | Warn |
| chdb-datastore | Pass | Pass | Pass |
| clickhouse-managed-postgres-rca | Pass | Pass | Fail |
| clickhouse-js-node-rowbinary | Pass | Pass | Pass |

The one Fail is `clickhouse-managed-postgres-rca`, flagged by Snyk on rule codes W007, W011 and W012, and `chdb-sql` carries a Snyk Warn on W011. The Fail sits on the workflow that asks for credentials: the RCA skill calls `https://api.clickhouse.cloud` with HTTP Basic auth from a ClickHouse Cloud API key pair, reads the OpenAPI spec to resolve field names, scrapes a Prometheus endpoint and queries the Slow Query Patterns API, which the skill itself marks as beta. Read that skill before you let an agent run it, and scope the key to the one organization and service it needs.

The install surface is thin, the run surface is not. Installing copies Markdown; nothing in the repository runs at install time, and the build tooling under `packages/` exposes only `bun` build, validate and link-check scripts. What runs later is `clickhousectl`, which the infrastructure and ClickStack skills invoke against ClickHouse Cloud with an API key and secret, sometimes passed on the command line as `--api-key` and `--api-secret`. The CLI is also installed by piping a remote script into a shell with `curl -fsSL https://clickhouse.com/cli | sh`, so pin or verify the binary if you are provisioning machines rather than a laptop.

Treat a ClickHouse Cloud key as a deploy credential for agent work. The cloud references create services, create SQL users, and in the ClickStack workflow create and later drop an ingest user, all of which are real state changes on a billed account. Keep the key in the environment or a scoped config file, keep it out of prompts and logs, and prefer a session where someone is watching the first time an agent runs the cloud half of the suite.

## Limitations

- Snapshot data, verified 2026-10-28: 83,246 combined installs across 11 indexed listings; 561 GitHub stars; Apache-2.0; last pushed 2026-10-19. Counts drift over time.
- The install index outruns the tree. `clickhousectl-local-dev` and `clickhousectl-cloud-deploy` carry install counts but have no directory in the current `skills/` tree, and the README says `infra-clickhouse` supersedes both.
- The tree also outruns the index in the other direction: `clickhouse-js-node-coding` and `clickhouse-js-node-troubleshooting` exist as skill directories but are not indexed listings, so installing by index name will miss them.
- Rule counts disagree inside the repository. The README and the marketplace manifest advertise 28 rules for `clickhouse-best-practices`, while its `SKILL.md` claims 31 and the `rules/` directory holds 31 rule files.
- The README documents two install routes, `npx skills add` and `clickhousectl skills`. The Claude Code marketplace manifest exists with 8 plugin entries against 11 skill directories, but no plugin install command is documented, so that path is unverified.
- Several features are beta. Managed ClickHouse Cloud Postgres is beta, the Slow Query Patterns API is beta, and its field names can shift, which is why the RCA skill resolves them from the OpenAPI spec on every run instead of hardcoding them.

## Related

- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [Redis Agent Skills - Official Data Modeling & Caching Setup](/hermes/skills/catalog/redis-agent-skills-setup)
- [Astronomer Agents - Airflow Data Engineering Setup](/hermes/skills/catalog/astronomer-agents-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `clickhouse-best-practices` alone first. It is the skill that changes query and schema output, and it is the one whose rules an agent can cite back at you during review.
- Ask for the rule name when the agent proposes a schema. A rule corpus that is never cited degenerates into the same generic advice you get without it, and naming the rule is how you tell the two apart.
- Reach for `chdb-sql` before spinning up a server for one-off file analysis. A `pip install chdb` and a query on a parquet file is faster than provisioning, and it composes with the Hermes jobs you already run.
- Keep the cloud skills out of unattended runs. `infra-clickhouse`, `infra-postgres` and `clickstack-otel-collector` change billed state, and the RCA skill reads live metrics from a real service.
- When the two rule counts disagree in your own reading, trust the `rules/` directory over the README headline. The directory is what the agent actually loads.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
