---
title: "Astronomer Agents - Airflow Data Engineering Setup"
description: "Astronomer's skills for Airflow: 25.5K combined installs. DAG authoring, debugging, lineage, dbt/Cosmos and warehouse SQL analysis for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/astronomer-agents-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "airflow", "data engineering", "dbt"]
---

# Astronomer Agents - Setup Guide

**Source:** [astronomer/agents](https://www.skills.sh/astronomer/agents) via skills.sh - 25.5K combined installs across 38 indexed listings; first documented 2026-10-27 (Oct 27 morning sweep)

**GitHub:** [astronomer/agents](https://github.com/astronomer/agents) - 456 stars, Apache-2.0, branch main, 35 in-tree skill directories: 34 under `skills/` plus `airflow-adapter` under `astro-airflow-mcp/.claude/skills/`

**Category:** Data engineering and orchestration

**Quality Tier:** 🟡 Beta - vendor-maintained Apache-2.0 repository, 456 stars, skills plus a bundled Airflow MCP server

Astronomer builds Astro, the managed Airflow platform that the README describes as optional but a good fit for managed deployments, built-in alerting and centralized observability. This repository is their agent layer for data engineering: an Airflow MCP server (`astro-airflow-mcp`), an `af` command line tool that talks to the Airflow REST API, and a set of skills that teach a coding agent how to write, test, deploy and reason about pipelines.

The suite is wider than a typical vendor drop because it covers three different jobs. One group works on the warehouse (schema discovery, SQL analysis, profiling, freshness, lineage). One group works on DAG code (authoring, testing, debugging, plugins, human-in-the-loop steps, the Airflow 2 to 3 migration). The third group is operational (Astro project setup, local environment control, deployment and production troubleshooting). The split matters in practice: a question about a failing task and a question about revenue by product route to different skills with different tools behind them.

The repository is Apache-2.0 and explicitly usable without Astro. The README states that the MCP server works against any Airflow 2.x or 3.x REST API, that skills are tool-agnostic, and that open-source users should point `AIRFLOW_API_URL` at their own instance and use Docker Compose or the Helm chart for deployment.

## Installation

The skills install through skills.sh. The README's quick start takes the whole collection:

```bash
npx skills add astronomer/agents --skill '*'
```

The command prompts you to pick which agents to install into. Omitting `--skill` makes the CLI prompt you per skill instead, which is the documented way to take a subset. There is no per-skill install flag in the README, so for a single skill either use that prompt path or copy `skills/<name>/` out of the repository after cloning it.

Cursor gets its own target, and the README notes the skills land in `.cursor/skills/`:

```bash
npx skills add astronomer/agents --skill '*' -a cursor
```

Claude Code users are pointed at the plugin instead, because it wires the MCP server and hooks in one step:

```bash
claude plugin marketplace add astronomer/agents
claude plugin install astronomer-data@astronomer
```

The MCP server is separate from the skills and runs from PyPI through `uvx`. For any MCP client:

```bash
uvx astro-airflow-mcp --transport stdio
```

For a remote instance, pass the connection through the environment rather than the config file:

```bash
AIRFLOW_API_URL=https://your-airflow.example.com \
AIRFLOW_USERNAME=admin \
AIRFLOW_PASSWORD=admin \
uvx astro-airflow-mcp --transport stdio
```

The `af` CLI ships from the same package. The README suggests an alias for frequent use:

```bash
alias af='uvx --from astro-airflow-mcp af'
```

Warehouse connections are configured in `~/.astro/agents/warehouse.yml` with credentials in `~/.astro/agents/.env`. Snowflake, Postgres and BigQuery have built-in connectors; the `sqlalchemy` type auto-detects drivers for 25 or more databases, and it is the one type that requires the `databases` list.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| airflow | 1,461 | Entry point for Airflow operations through the `af` CLI: list and trigger DAGs, retry runs, read task logs, inspect connections, variables and pools, and route to sibling skills. |
| managing-astro-local-env | 1,456 | Start, stop and restart the local Airflow environment with the Astro CLI, read logs, query the Airflow API and fix environment problems. |
| analyzing-data | 1,416 | Answer business questions with SQL against the warehouse: counts, metrics, trends, joins and ad-hoc analysis through a background Jupyter kernel. |
| authoring-dags | 1,229 | Write new DAGs and extend existing ones with follow-up or downstream tasks, following the repository's DAG patterns and conventions. |
| debugging-dags | 1,213 | Structured root cause investigation for import, parse and task failures, with prevention recommendations beyond a quick log read. |
| testing-dags | 1,162 | Iterative test, debug and fix cycles: run a DAG locally, diagnose what broke, patch it and run again. |
| migrating-airflow-2-to-3 | 1,120 | Port Airflow 2.x projects to 3.x: breaking changes, compatibility issues and the modernization steps. |
| setting-up-astro-project | 1,059 | Initialize an Astro or Airflow project, pin dependencies, configure connections and variables, and understand the project layout. |
| tracing-upstream-lineage | 1,048 | Trace where data comes from: what feeds a table, which DAGs and sources sit upstream, and where the data originates. |
| profiling-tables | 1,030 | Profile a named table for statistics, structure and data quality signals. |
| tracing-downstream-lineage | 1,023 | Impact analysis before a change: what depends on a table or DAG and what breaks if it moves. |
| checking-freshness | 1,009 | Check whether a table is current, stale or when it was last updated before relying on it. |
| annotating-task-lineage | 973 | Add lineage metadata to tasks with inlets and outlets so operators without built-in OpenLineage extraction still report datasets. |
| cosmos-dbt-core | 964 | Turn a dbt Core project into an Airflow DAG or TaskGroup with Astronomer Cosmos, after checking engine, warehouse and manifest. |
| airflow-hitl | 954 | Human-in-the-loop DAG steps: approval gates, form input and branching on a human decision with the Airflow 3.1+ HITL operators. |
| creating-openlineage-extractors | 935 | Build custom OpenLineage extractors for third-party operators, including column level lineage. |
| cosmos-dbt-fusion | 900 | Run a dbt Fusion project with Cosmos, limited to local execution on Snowflake or Databricks and explicit that it does not cover dbt Core. |
| warehouse-init | 816 | One-time schema discovery that writes `.astro/warehouse.md` so later lookups do not rescan the warehouse. |
| deploying-airflow | 788 | Deploy DAGs and projects: pushing code, setting up CI/CD, and targets including Astro, Docker Compose and Kubernetes. |
| troubleshooting-astro-deployments | 626 | Investigate Astronomer production deployments with the Astro CLI: deployment issues, production logs, failure analysis and environment variables. |
| airflow-plugins | 596 | Build Airflow 3.1+ plugins: FastAPI apps, custom UI pages, React components, middleware, macros and operator extra links. |
| managing-astro-deployments | 570 | Manage Astronomer deployments with the Astro CLI: authenticate, switch workspaces, create and update deployments and ship code. |
| blueprint | 554 | Reusable task group templates validated with Pydantic, composed into DAGs from YAML with shared variables and per-environment profiles. |

The remaining 15 indexed listings range from 3 to 389 installs.

Three of them, `init`, `initializing-warehouse` and `discovering-data`, have no matching directory under `skills/` in the current tree; `airflow-adapter` ships from `astro-airflow-mcp/.claude/skills/airflow-adapter` rather than the main skills directory.

## Why This Matters for Hermes Agents

Airflow work fails in ways a model cannot see from the code alone. A DAG parses locally and dies on import in the scheduler, a task succeeds but the table it writes is stale, a column rename breaks three downstream models nobody listed. These skills are written for those cases: each one names the tool call that produces evidence, whether that is `af` against the REST API, a Jupyter kernel against the warehouse, or an OpenLineage query.

The router design is the second reason to install the whole set rather than one skill. `airflow` is an entry point that inspects the request and hands off to `authoring-dags`, `testing-dags`, `debugging-dags` or the migration skill, so an agent with the collection installed picks a procedure instead of improvising one. That is also where the cost sits: each skill is a narrow instruction file, and a single skill installed alone loses the routing.

The bundled MCP server is what turns these skills from documentation into actions. With `astro-airflow-mcp` connected, a Hermes agent can list DAGs, trigger a run, pull task logs and read system health itself, which means the loop of propose, run and verify closes inside one session instead of handing commands back to a human.

For teams already on Astro the deployment skills cover the managed path. For teams on open-source Airflow, the same skills apply: the README is explicit that the MCP server talks to any 2.x or 3.x REST API and that `AIRFLOW_API_URL` is the only thing that changes.

## Usage

| You say | What happens |
|---|---|
| "Why did the etl_pipeline DAG fail last night?" | airflow pulls the run and task logs through `af`, and debugging-dags escalates to a structured root cause analysis with a prevention note. |
| "Create a DAG that loads S3 data into Snowflake every morning" | authoring-dags writes the DAG against the repository's patterns, and testing-dags runs it locally when you ask for a test and fix pass. |
| "How many customers ordered twice last quarter?" | analyzing-data issues SQL through the background Jupyter kernel and returns the number with the query it used. |
| "What breaks if I rename this column?" | tracing-downstream-lineage walks the impact set, and annotating-task-lineage fills the lineage gap for operators that do not report it automatically. |
| "Is this table fresh enough for today's report?" | checking-freshness reads the last update for the table, and profiling-tables adds statistics if you want more than a timestamp. |
| "Move this project to Airflow 3" | migrating-airflow-2-to-3 walks the breaking changes, and the agent flags 2.x code it finds even when you did not ask. |
| "We need an approval step before the publish task" | airflow-hitl scaffolds the approval gate with the Airflow 3.1+ HITL operators and branches on the human decision. |

## Verification

Confirm the raw layout on `main` before installing. Every path below returned HTTP 200 on 2026-10-27:

```bash
for p in skills/airflow/SKILL.md \
         skills/authoring-dags/SKILL.md \
         skills/analyzing-data/SKILL.md \
         skills/blueprint/SKILL.md \
         skills/troubleshooting-astro-deployments/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/astronomer/agents/main/$p"
done
```

Read the entry point before you install, because it defines the routing the rest of the collection depends on:

- https://raw.githubusercontent.com/astronomer/agents/main/skills/airflow/SKILL.md
- https://raw.githubusercontent.com/astronomer/agents/main/skills/debugging-dags/SKILL.md
- https://raw.githubusercontent.com/astronomer/agents/main/skills/analyzing-data/SKILL.md

After install, the skills appear as one folder per skill in your agent's skills directory. `npx skills add astronomer/agents --skill '*'` prompts before writing, so the selection screen is itself a check that the index resolves. Then verify the half that can actually fail silently: run `af health` and `af dags list` with your Airflow environment set, and confirm the MCP server reports the same instance your DAGs live on.

## Security

skills.sh verdicts were not sampled for this fire, so the Gen Agent Trust Hub, Socket and Snyk results below are unverified - check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| airflow | Not checked | Not checked | Not checked |
| analyzing-data | Not checked | Not checked | Not checked |
| authoring-dags | Not checked | Not checked | Not checked |
| debugging-dags | Not checked | Not checked | Not checked |
| blueprint | Not checked | Not checked | Not checked |

Read the trust model from the code rather than from a badge. Two skills hold real power in a data platform: `analyzing-data` connects to the warehouse and runs SQL that you did not write, and the deployment skills authenticate to Astro and push code to production. Both need scoped credentials and a human read of the skill before they run unattended.

The other exposure is credential layout. The README stores credentials in a dotenv file at `~/.astro/agents/.env` and has `warehouse.yml` reference them, so the pair is a filesystem secret rather than a vault secret. Keep both out of any repository the agent can push to.

Two disclosures from the README that belong here rather than in a footnote: the `af` CLI collects anonymous usage telemetry, command name only, with `af telemetry disable` as the opt-out, and the repository README loads a Scarf analytics pixel.

## Limitations

- Snapshot data, verified 2026-10-27: 25,523 combined installs across 38 indexed listings; 456 GitHub stars; Apache-2.0; branch main. Counts drift over time.
- The install index outruns the tree at the tail: 38 indexed listings against 35 in-tree skill directories. `init`, `initializing-warehouse` and `discovering-data` carry install counts but have no matching directory in the current `skills/` tree, and `airflow-adapter` lives under `astro-airflow-mcp/.claude/skills/`.
- The README documents a subset of the collection. Language SDK skills, `dag-factory`, `delegating-to-otto`, `airflow-state-store`, `airflow-plugins` and the Astro deployment skills exist in the tree but are not in the README's skill tables, so their behaviour comes from their own `SKILL.md` files.
- Install counts measure distribution, not quality. Nothing in the repository states which skills are production tested.
- Several skills require Airflow 3.1 or newer: `airflow-hitl` and `airflow-plugins` both target the 3.1 plugin and HITL APIs, and `cosmos-dbt-fusion` requires Cosmos 1.11 or newer with local execution on Snowflake or Databricks only.
- The Astro specific skills (`setting-up-astro-project`, `managing-astro-local-env`, `managing-astro-deployments`, `troubleshooting-astro-deployments`) assume the Astro CLI. Open-source Airflow users get the DAG and warehouse skills but not those four workflows.

## Related

- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [Nia Skill - Code and Docs Indexing Setup](/hermes/skills/catalog/nozomio-nia-skill-setup)
- [Dynatrace for AI - Observability Skills Setup](/hermes/skills/catalog/dynatrace-for-ai-setup)
- [Arize Skills - LLM Observability and Evaluation Setup](/hermes/skills/catalog/arize-skills-setup)

## Pro Tips

- Install `airflow` first and treat it as the router. If you take one skill from this repository, take that one; the rest are specialists it calls.
- Run `warehouse-init` once per project before any analysis question. It writes `.astro/warehouse.md`, and every later lookup reads that file instead of scanning the warehouse again.
- Wire the MCP server before the skills if you want the agent to close its own loop. Skills describe procedure; the server is what lets the agent list DAGs and read logs itself.
- Match the skill to the failure. A single failed task is `airflow` plus logs, a repeatedly failing DAG is `debugging-dags`, and a DAG that will not import is a parse problem the debug skill handles with a different procedure.
- Keep `AIRFLOW_API_URL` and the warehouse credentials in the environment or `~/.astro/agents/.env`, never in a prompt, and scope the Airflow user to the instances the agent is allowed to trigger runs on.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
