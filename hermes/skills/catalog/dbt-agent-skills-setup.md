---
title: "dbt Agent Skills - Official dbt Labs Analytics Suite Setup"
description: "dbt Labs official skills: 12.4K combined installs. Twelve everyday analytics skills plus semantic layer, Mesh, migration and docs lookups."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dbt-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "dbt", "analytics engineering"]
---

# dbt Agent Skills - Setup Guide

dbt Labs publishes its own Agent Skills collection for working inside dbt projects: build and modify models, write tests, create MetricFlow semantic models, govern a Mesh deployment, troubleshoot platform job failures, and migrate a project from dbt Core to dbt v2. The repo is the publisher's own, not a community mirror, and it is versioned with a changie changelog and GitHub Actions CI.

The design choice that matters is that the skills are not slash commands. Fourteen of the 17 SKILL.md files set `user-invocable: false`, so the agent loads the relevant skill when a prompt matches its description and the operator rarely has to remember a command name. The repo also ships its own evaluation harness in `evals/`, an A/B tool that compares skill variations against recorded scenarios, and a changie changelog with `CHANGELOG.md`.

**Source:** [dbt-labs/dbt-agent-skills](https://www.skills.sh/dbt-labs/dbt-agent-skills) via skills.sh - 12.4K combined installs across 19 indexed listings; first seen Jan 29, 2026
**GitHub:** [dbt-labs/dbt-agent-skills](https://github.com/dbt-labs/dbt-agent-skills) (746 stars; Apache-2.0; branch main, pushed 2026-10-22; 17 SKILL.md directories: 12 under `skills/dbt/skills/`, 3 under `skills/dbt-migration/skills/`, 1 under `skills/dbt-extras/skills/`, plus an unindexed maintainer skill at `.claude/skills/auditing-skills/SKILL.md`)
**Category:** Data / Analytics Engineering
**Quality Tier:** 🟢 Production - official dbt Labs repo under Apache-2.0, 16 of the 19 indexed listings verified against the tree, a pytest suite plus CI, and a real A/B skill-evaluation harness in `evals/`; the flagship skill carries a Snyk warn, noted under Security

## Installation

```bash
# Preview, then install every skill in the repo
npx skills add dbt-labs/dbt-agent-skills --list
npx skills add dbt-labs/dbt-agent-skills

# Install only the everyday analytics engineering skills
npx skills add dbt-labs/dbt-agent-skills/skills/dbt

# Install only the one-off migration skills
npx skills add dbt-labs/dbt-agent-skills/skills/dbt-migration

# One skill, or a global install into ~/.<agent>/skills/
npx skills add dbt-labs/dbt-agent-skills --skill using-dbt-for-analytics-engineering
npx skills add dbt-labs/dbt-agent-skills --global
```

```bash
# Claude Code plugin path, from the README
/plugin marketplace add dbt-labs/dbt-agent-skills
/plugin install dbt@dbt-agent-marketplace
/plugin install dbt-migration@dbt-agent-marketplace
```

```yaml
# Or install as dbt packages, which also works for dbt Cloud and the dbt Wizard CLI
packages:
  - git: "https://github.com/dbt-labs/dbt-agent-skills.git"
    subdirectory: "skills/dbt"
    revision: main
```

```bash
# Opt in via dbt_project.yml flags (ai_provider: claude writes to .claude/skills)
dbt deps
```

Prerequisites from the README: dbt installed and configured, a project with `dbt_project.yml`, and basic familiarity with models, tests and sources. `fetching-dbt-docs` and `configuring-dbt-mcp-server` work without an existing project. The platform skills read a `DBT_TOKEN` from the environment rather than a literal token in config.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| using-dbt-for-analytics-engineering | 1,169 | The default dbt skill: build and modify models, write SQL with ref() and source(), add tests, debug errors, explore unfamiliar sources, validate with dbt show |
| fetching-dbt-docs | 1,105 | Retrieve and search dbt documentation in LLM-friendly markdown, including an llms.txt page index and a script that caches the full docs locally |
| adding-dbt-unit-test | 1,103 | Write unit test YAML that mocks upstream inputs and asserts outputs, with per-warehouse type and caveat references for BigQuery, Snowflake, Redshift, Postgres and Spark |
| running-dbt-commands | 1,059 | Get the right dbt executable, flags, selectors and parameter formats for run, build, test, compile and show |
| answering-natural-language-questions-with-dbt | 1,035 | Answer business questions (revenue, KPIs, top customers) by querying the semantic layer or warehouse SQL, not by editing models |
| configuring-dbt-mcp-server | 1,032 | Generate MCP server config, resolve authentication, and validate connectivity for Claude, Cursor or VS Code |
| building-dbt-semantic-layer | 1,023 | Create semantic models, metrics, dimensions, entities and time spines with MetricFlow, covering latest and legacy YAML specs |
| troubleshooting-dbt-job-errors | 1,014 | Diagnose dbt platform job failures from run logs, the Admin API and git history, with an explicit iron rule against editing a test to make it pass |
| working-with-dbt-mesh | 869 | Judge whether a column rename, removal or retype is breaking, then handle model versions, contracts, access, groups and cross-project refs |
| using-dbt-state | 554 | Configure and debug dbt State (server-backed node reuse) and separate it from the state:modified selector and --state deferral |
| creating-mermaid-dbt-dag | 527 | Generate a Mermaid flowchart of model lineage from the dbt MCP lineage tools, manifest.json, or direct code parsing as a fallback |
| migrating-dbt-project-across-platforms | 526 | Move a project between warehouses (Snowflake to Databricks and back) using Fusion's real-time compilation to find SQL dialect differences |

The remaining 7 indexed listings range from 56 to 385 installs. Four of them are documented in the repo: maintaining-dbt-documentation (329), migrating-dbt-core-to-v2 (182), upgrading-dbt (129) and querying-the-dbt-information-schema (128). Three carry install counts without a matching directory in the current tree: migrating-dbt-core-to-fusion (385), upgrading-dbt-core (132) and using-dbt-index (56).

## Why This Matters for Hermes Agents

dbt work is command-line work with exact syntax: which executable, which selector, which flag order, whether a variable is a string or a dict. `running-dbt-commands` encodes those formats so an agent stops inventing flags, and `fetching-dbt-docs` gives it a way to check a reference page instead of answering from memory, including a local 24-hour cache of `docs.getdbt.com/llms-full.txt`.

The second gain is judgement, not syntax. `working-with-dbt-mesh` is built around one question an agent usually gets wrong: is this change breaking, and who consumes the model. `troubleshooting-dbt-job-errors` carries an explicit iron rule (never modify a test to make it pass without understanding the failure) and a table of rationalizations that mean stop. Those rules are exactly the ones a helpful-sounding agent skips under time pressure.

The semantic layer skills close the gap between a business question and a metric definition. `building-dbt-semantic-layer` covers metric types and both the latest and legacy YAML specs, so an agent can tell which spec a project is on before editing, and `answering-natural-language-questions-with-dbt` is scoped to querying rather than to changing models, which keeps a read-only question from turning into a schema edit.

Finally, the repo is testable like software. Everything follows the Agent Skills specification, CI validates frontmatter and links, and `evals/` A/B tests skill variations against recorded scenarios. For an operator maintaining a fleet of agents, that means a skill change can be measured rather than argued about.

## Usage

| You say | What happens |
|---|---|
| "Add a new incremental model for subscription revenue" | Loads using-dbt-for-analytics-engineering, plans the model against real sources, writes the SQL with ref(), then runs dbt show to validate |
| "Add unit tests for the orders model" | Loads adding-dbt-unit-test and writes YAML that mocks upstream rows and asserts outputs, with the warehouse-specific caveats for the project's adapter |
| "Build a revenue metric in the semantic layer" | Loads building-dbt-semantic-layer, checks whether the project is on the latest or legacy spec, then writes the semantic model, measure and metric |
| "What were sales last quarter?" | Loads answering-natural-language-questions-with-dbt and queries the semantic layer or warehouse instead of editing any model |
| "This nightly job failed and the error is vague" | Loads troubleshooting-dbt-job-errors, pulls run logs and Admin API data, checks recent git history, and reports the root cause before any fix |
| "We are renaming a column used by three dashboards" | Loads working-with-dbt-mesh and returns a breaking-change assessment plus a versioning or migration path |
| "Set up the dbt MCP server for Cursor" | Loads configuring-dbt-mcp-server, generates the config with `${DBT_TOKEN}` references and validates connectivity |
| "Draw the lineage for the finance models" | Loads creating-mermaid-dbt-dag and emits a Mermaid flowchart from the lineage tools or manifest.json |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -ci dbt
```

Read the skills before installing. The seven URLs below returned 200 with `curl -s -o /dev/null -w "%{http_code}"` when checked on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/dbt-labs/dbt-agent-skills/main/README.md
curl -sL https://raw.githubusercontent.com/dbt-labs/dbt-agent-skills/main/skills/dbt/skills/using-dbt-for-analytics-engineering/SKILL.md
curl -sL https://raw.githubusercontent.com/dbt-labs/dbt-agent-skills/main/skills/dbt/skills/running-dbt-commands/SKILL.md
curl -sL https://raw.githubusercontent.com/dbt-labs/dbt-agent-skills/main/skills/dbt/skills/fetching-dbt-docs/SKILL.md
curl -sL https://raw.githubusercontent.com/dbt-labs/dbt-agent-skills/main/skills/dbt/skills/troubleshooting-dbt-job-errors/SKILL.md
curl -sL https://raw.githubusercontent.com/dbt-labs/dbt-agent-skills/main/skills/dbt-migration/skills/upgrading-dbt/SKILL.md
curl -sL https://raw.githubusercontent.com/dbt-labs/dbt-agent-skills/main/skills/dbt-extras/skills/creating-mermaid-dbt-dag/SKILL.md
```

All three skills directories nest one level deeper, at `skills/<area>/skills/<name>/SKILL.md`, so a plain `skills/<name>/SKILL.md` fetch will 404 on this repo.

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| using-dbt-for-analytics-engineering | Pass | Pass | Warn |
| running-dbt-commands | Pass | Pass | Pass |
| fetching-dbt-docs | Pass | Pass | Pass |

Permission grants are declared per skill through `allowed-tools`, and only five SKILL.md files declare one. `using-dbt-for-analytics-engineering` grants `Bash(dbt *)`, `Bash(jq *)`, Read, Write, Edit, Glob and Grep, which is real write access to the project: the agent can edit models, tests and YAML and can run `dbt run` or `dbt build` against the configured warehouse, spending compute and changing tables. `maintaining-dbt-documentation` adds `Bash(python3 *)` and `Bash(git *)`. The two migration skills that declare grants allow `Bash(dbt:*)`, `Bash(git:*)` and `Bash(uvx:*)`, and `migrating-dbt-core-to-v2` additionally grants `WebFetch(domain:api.github.com)` to search dbt-fusion issues. `creating-mermaid-dbt-dag` grants only the two dbt MCP lineage tools, Read, Glob, Grep and `Bash(jq *)`.

The other twelve skills declare no `allowed-tools` at all, so whatever your host agent already permits is the ceiling. Network behaviour: `fetching-dbt-docs` downloads `https://docs.getdbt.com/llms-full.txt` into `~/.cache/dbt-docs` with a 24-hour cache, and `configuring-dbt-mcp-server` writes MCP config files that reference `${DBT_TOKEN}` and explicitly warns against pasting literal tokens into committed config. `troubleshooting-dbt-job-errors` needs a dbt platform service token to reach the Admin API. The single Snyk warn sits on the flagship skill, which is the one with both write access and `dbt *` shell scope, so review it against your own blast radius before enabling it on a production project.

## Limitations

- Most skills assume a working dbt installation and an existing project. Only `fetching-dbt-docs` and `configuring-dbt-mcp-server` stand alone.
- Three indexed listings have no directory in the current tree: migrating-dbt-core-to-fusion (385), upgrading-dbt-core (132) and using-dbt-index (56). They are install counts without a fetchable SKILL.md at this snapshot.
- `using-dbt-state` (554) is in the tree but absent from the README's Available Skills table, which documents 14 of the 17 skills.
- The migration skills are one-off by the README's own description. Installing the whole repo for every session loads context that only pays off during an upgrade.
- 14 of the 17 skills set `user-invocable: false`, so routing is by prompt match rather than a command name. The exceptions are `upgrading-dbt`, `migrating-dbt-core-to-v2` and the internal auditing skill.
- The docs skills fetch live documentation, so answers track docs.getdbt.com rather than the dbt version pinned in your project.
- Snapshot data, verified Oct 26, 2026: 12,357 combined installs across 19 indexed listings; 746 GitHub stars; Apache-2.0; last pushed 2026-10-22. Counts drift over time.

## Related

- [Databricks Agent Skills - Setup Guide](/hermes/skills/catalog/databricks-agent-skills-setup) - watch the warehouse side of a dbt project that runs on Databricks.
- [Amplitude Agent Skills - Product Analytics Setup](/hermes/skills/catalog/amplitude-agent-skills-setup) - the downstream analytics layer that consumes the models these skills build.
- [PlanetScale Database Skills - Setup Guide](/hermes/skills/catalog/planetscale-database-skills-setup) - schema and query work at the database layer beneath a dbt source.
- [Redis Agent Skills - Official Data Modeling & Caching Setup](/hermes/skills/catalog/redis-agent-skills-setup) - data modeling conventions for a second data store alongside the warehouse.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `skills/dbt` globally and keep `skills/dbt-migration` scoped to the migration project. The README says the migration set is one-off, and it is 3 of the 16 available skills.
- Read `allowed-tools` in the SKILL.md before enabling the analytics engineering skill on a production project. It can edit models and run builds, which is a different risk class from a read-only docs skill.
- Point the agent at `using-dbt-state` when someone reports models rebuilding that should have been reused. The skill exists specifically because dbt State gets confused with `state:modified`.
- Use `working-with-dbt-mesh` before a column rename rather than during the incident. It is designed to answer who consumes the model while the change is still optional.
- Keep the docs cache warm. `fetching-dbt-docs` reuses `~/.cache/dbt-docs` for 24 hours, so repeated lookups in a long session do not refetch `llms-full.txt`.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*