---
title: "Looker Skills - Official LookML Development Suite"
description: "looker-open-source/looker-skills: 3.3K combined installs across 26 listings for LookML views, explores, tests and CLI onboarding"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/looker-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "looker", "lookml", "business intelligence", "analytics"]
---

# Looker Skills - Setup Guide

**Source:** [looker-open-source/looker-skills](https://www.skills.sh/looker-open-source/looker-skills) via skills.sh - 3.3K combined installs across 26 indexed listings; first seen Jun 9, 2026 (Nov 12, 2026 sweep)
**GitHub:** 47 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-11, 26 `SKILL.md` files under `skills/`, one per skill, with a matching `dashboards/` folder of examples
**Category:** Business intelligence: LookML modeling, explores, fields, tests, access grants, dashboard authoring, CLI and MCP onboarding
**Quality Tier:** 🟢 Production - an official Looker organization repository with a permissive license, clean scanner results on every sampled skill and a push on the day before this sweep, with a star count that understates it because the vendor publishes here rather than promoting it.

LookML is a modelling language with rules that are easy to state and easy to break. A view declares a table, a model declares connections and includes, an explore declares joins and access, and a field declares the SQL that defines it. Get the structure wrong and the project builds into something that answers a different question than the one that was asked, which is the failure mode that makes business intelligence untrustworthy.

This repository teaches agents that structure. Eleven skills cover LookML itself: views, models, explores, fields, Liquid, refinements, tests, sets and access grants. The rest cover the work around it: a seven-step developer onboarding pipeline that runs from a preflight check through CLI install, OAuth, a BigQuery connection, project setup, model creation and a first dashboard.

Two master skills sit above the pipeline. `looker-architect` scaffolds, builds, refactors, validates and audits LookML projects against a raw and refined separation convention. `looker-performance-optimizer` audits query performance and enforces caching alignment and persistent derived table materialisation. `looker-mcp-skill` covers connecting to the Looker MCP server, which is how an agent reaches an existing instance rather than only writing files.

The onboarding sequence is the reason the pack is useful on day one. It encodes the order in which a Looker project has to be created, and it names the checks that catch a mismatch early: a missing CLI, an unauthenticated session, a connection pointed at the wrong project.

## Installation

The README recommends the skills CLI:

```bash
npx skills add looker-open-source/looker-skills
```

Claude Code can load the repository as a plugin, either for one session or persistently:

```bash
git clone https://github.com/looker-open-source/looker-skills.git
claude --plugin-dir ./looker-skills
claude plugin install ./looker-skills
```

Other agents have their own documented routes: `agy plugin install https://github.com/looker-open-source/looker-skills` for Antigravity, and an installer script that registers the repository in a personal marketplace for Codex. All of them install the same 26 skills.

The onboarding skills assume a Google Cloud project with BigQuery, the `gcloud` and `bq` CLIs and a Looker instance you can authenticate against. The pack guides the agent through using those tools; it does not install Looker.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| lookml-view | 170 | LookML view definitions, `sql_table_name`, file organisation and view patterns. |
| lookml-model | 169 | Model files: connections, includes and configuration for a `.model.lkml`. |
| lookml-explore | 169 | Explore definitions, joins, access grants and query configuration. |
| lookml-liquid | 168 | Liquid variables for dynamic SQL, HTML and links, including optimisation patterns. |
| lookml-fields | 168 | Choosing between dimension, measure, filter and parameter, and writing the `sql` for each. |
| lookml-refinements | 165 | Includes, refinements and project layering, the part that keeps a large project maintainable. |
| lookml-tests | 164 | Writing LookML data tests for integrity, accuracy and logic validation. |
| lookml-sets | 164 | Sets for grouping fields, controlling visibility and managing drill paths. |
| lookml-access-grants | 159 | Row-level and object-level security with access grants. |
| lookml-modeling-guidelines | 135 | House rules for modelling and command execution across a project. |
| creating-looker-dashboard | 134 | The final onboarding step: a LookML dashboard imported as a user-defined dashboard. |
| creating-lookml-model | 124 | Onboarding step six: views and models built from the stated goal, then validated. |
| exploring-data-for-looker | 123 | Onboarding step one: explore BigQuery data and define the modelling goal. |
| installing-looker-cli | 121 | Onboarding step two: verify or install the `looker-cli` binary. |
| looker-developer-onboarding | 120 | The parent skill that orchestrates the whole seven-step onboarding journey. |
| looker-performance-optimizer | 119 | Query performance audits: caching alignment, PDT materialisation, expensive patterns. |
| setting-up-looker-project | 119 | Onboarding step five: create the project and configure Git integration. |
| authenticating-looker-cli | 118 | Onboarding step three: OAuth against the Looker instance. |
| onboarding-preflight-check | 116 | Onboarding step zero: verify `gcloud`, `bq`, write permissions and fix what is missing. |
| connecting-looker-to-bigquery | 113 | Onboarding step four: create the database connection inside Looker. |
| looker-mcp-skill | 112 | Connecting to and using the Looker MCP server against an existing instance. |
| using-looker-cli | 110 | The `looker-cli` surface: profiles, defaults, persistent sessions and commands. |
| looker-architect | 106 | Scaffolding, refactoring, validating and auditing enterprise LookML projects. |

The remaining 3 indexed listings range from 27 to 50 installs.

The install numbers are close together because the skills are installed as one repository. That is a good sign for a vendor pack: people take the set, not one file.

## Why This Matters for Hermes Agents

An agent that has never written LookML produces something that looks like LookML. It will declare a view with a `sql_table_name`, add dimensions with `sql` blocks, and join two views in an explore. What it typically gets wrong is structural: where a field belongs, whether a join should be a refinement, whether a measure needs a symmetric aggregate, whether an access grant covers the fields it claims to. The project builds, the query runs, and the number is wrong in a way nobody notices for a month.

The eleven LookML skills pre-empt that by teaching the language's structure before the SQL. The tests skill is the one worth calling out: a LookML test asserts that a field returns what it should, and an agent that has been taught to write them leaves behind a project that can be checked on every change. That is the difference between an agent that produced a model and one that produced a model a team can maintain.

The onboarding pipeline matters for a different reason. Most agent failures on a platform like Looker are setup failures: the CLI is missing, the session is not authenticated, the connection points at the wrong BigQuery project, the Git integration is not configured. The seven-step sequence runs those checks in order, so the failure surfaces at the step that caused it rather than as an opaque error three steps later.

The performance and architecture skills are for the second visit. Once a project exists, the questions change to why a dashboard is slow, how to layer refinements without duplicating logic, and what to refactor before adding another explore. Both skills answer those with the platform's own conventions rather than general advice.

## Usage

| You say | What happens |
|---|---|
| "Set up a new Looker project on top of this BigQuery dataset" | Runs the onboarding pipeline: preflight, CLI, auth, connection, project, model, dashboard. |
| "Explain why this explore is slow" | Applies the performance optimiser: caching alignment, PDT materialisation and query patterns. |
| "Add a measure for revenue per active customer" | Writes the field with the correct measure type and the `sql` that matches the view's grain. |
| "Refactor this project into raw and refined layers" | Applies the architect skill's separation convention and validates the result. |
| "Write tests for these three fields" | Produces LookML data tests that assert the values and will fail on a regression. |
| "Give this team row-level access by region" | Uses the access grants skill rather than a filter that leaks the underlying rows. |
| "Connect to our existing Looker instance" | Uses the MCP skill to reach the instance instead of writing local files. |

## Verification

The skills live under `skills/` in the repository, one folder each. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/looker-open-source/looker-skills/main/skills/lookml-view/SKILL.md | head -6
```

Check the onboarding parent, since it is the entry point that references the seven step skills:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/looker-open-source/looker-skills/main/skills/looker-developer-onboarding/SKILL.md
```

After installing, confirm all 26 folders arrived. A partial install that skips the onboarding parent leaves the individual steps present but unsequenced, which is the failure mode this pack exists to prevent.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| lookml-view | Pass | Pass | Pass |
| lookml-model | Pass | Pass | Pass |
| lookml-explore | Pass | Pass | Pass |
| lookml-liquid | Pass | Pass | Pass |

All four sampled skills pass all three scanners. The skills are instruction files plus example LookML, and the only external access they describe is through the documented CLIs.

The operational risk is credential scope rather than code. The onboarding pipeline authenticates against BigQuery and Looker, writes a Git configuration into a project and can create a connection. An agent running that sequence holds real credentials for a real instance. Scope the service account to the project it is onboarding, and run the pipeline against a development instance before it touches production.

## Limitations

- Snapshot data, verified 2026-11-12: 3,277 combined installs across 26 indexed listings; 47 GitHub stars; Apache-2.0 license; last pushed 2026-11-11. Counts drift over time.
- 47 stars is a thin community signal for a repository this capable. It is published by the Looker open source organization, so the code is first-party even though the star count does not show adoption.
- The onboarding pipeline assumes Google BigQuery. The steps cover `gcloud`, `bq` and a BigQuery connection; other warehouses are not covered by the sequence.
- The skills assume a Looker instance you can reach and authenticate against. Nothing in the pack provisions one.
- The MCP skill depends on the Looker MCP server being available for your deployment. Confirm that before relying on the MCP path.
- Instructions are written for a current Looker release and a current `looker-cli`. Neither version is pinned, so a major CLI change can move the commands under the skills.

## Related

- [ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup)
- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [Metabase Skills - BI and Dashboard Agent Suite](/hermes/skills/catalog/metabase-skills-setup)
- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `looker-developer-onboarding` rather than the individual steps. It sequences the seven skills and stops at the first failure, which is where the useful error is.
- Ask for tests in the same pass as the fields. A model written without tests is a model nobody will change confidently, and the tests skill is right there.
- Run the preflight before anything else on a new machine. It checks `gcloud`, `bq` and write permissions, which is where most failed onboardings actually end.
- Use `looker-architect` for the second project, not the first. The separation and refactoring rules make sense once you have seen a project that grew without them.
- Keep the MCP path for read work and the file path for model changes. An agent that edits a live instance through tools is harder to review than one that proposes files in a branch.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
