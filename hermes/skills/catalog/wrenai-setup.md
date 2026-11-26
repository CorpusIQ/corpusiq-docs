---
title: "Wren AI Skills - Governed Text-to-SQL Setup"
description: "canner/wrenai - 2.9K combined installs: open-source GenBI text-to-SQL engine with a governed MDL semantic layer and AI context layer for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wrenai-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "text-to-sql", "genbi", "data analytics"]
---

# Wren AI - Setup Guide

**Source:** [canner/wrenai](https://www.skills.sh/canner/wrenai) via skills.sh - 2.9K combined installs across 6 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [canner/wrenai](https://github.com/canner/wrenai) - 18,407 stars, NOASSERTION license field (README states Apache 2.0), last pushed Nov 26, 2026, main branch; the discovery stub lives at skills/wren/SKILL.md and the full workflow guides under core/wren/src/wren/skills_content/<name>/SKILL.md.
**Category:** Data Analytics (GenBI / Text-to-SQL)
**Quality Tier:** 🟢 Green - 3 of 6 listings sampled: all three carry Pass across Gen Agent Trust Hub, Socket, and Snyk.

Wren AI is an open-source generative BI (GenBI) engine: it gives the AI agents you already run (Claude Code, Cursor, MCP clients, LangChain) a governed semantic layer and an AI context layer, so a business question becomes correct SQL, a shareable dashboard, and reviewable definitions instead of a plausible guess. The semantic layer is expressed in the Modeling Definition Language (MDL): Git-friendly YAML that says what the data means, not just where it lives.

The six indexed skills cover the whole loop: a discovery stub (wren), onboarding, MDL generation, day-to-day usage, and a dlt connector for SaaS data. The CLI is the real workflow engine: the skills fetch full workflow guides from the installed wren CLI on demand, so instructions always match the installed version.

## Installation

The README documents two install steps: the Python CLI, then a skills stub for your agent.

```bash
pip install wrenai
npx skills add Canner/WrenAI
```

Connector extras are added as needed, for example `pip install "wrenai[postgres,memory]"`. The skills command installs a roughly 50-line discovery stub; the agent then fetches full workflow guides from the CLI with `wren skills get <name>`.

## What It Provides

skills.sh publishes per-skill install counts for all 6 indexed listings. The 5 most-installed skills are listed below; the remaining listing is summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| wren | 1,785 | discovery stub for the Wren CLI, a semantic SQL layer over 22+ databases |
| wren-generate-mdl | 253 | generate a Wren MDL project by exploring a database schema |
| wren-usage | 250 | answer data questions end-to-end through the wren CLI semantic layer |
| wren-onboarding | 249 | install Wren Engine, scaffold a project, and run a first query |
| wren-dlt-connector | 247 | connect SaaS data (HubSpot, Stripe, Salesforce, GitHub, Slack) via dlt into DuckDB and auto-generate a Wren project |

The remaining 1 indexed listing is wren-enrich-context (81 installs), which augments a Wren project with business context the database schema cannot carry.

## Why This Matters for Hermes Agents

The value here is governance, not SQL generation. A raw agent asked for revenue will write plausible SQL and get it wrong on joins, units, and edge cases; Wren forces every query to be planned against the MDL semantic layer, dry-plan validated, and bounded by row limits before execution. The context layer is what makes it durable: enum meanings, units, NULL semantics, soft-delete filters, and named metrics (ARR, churn, DAU) live as reviewable Markdown and YAML in a repo you own, so definitions can be diffed and reviewed like code. The dlt connector and generate-mdl skills close the hardest part of agent analytics: getting arbitrary SaaS and database schemas into that governed model in the first place. The caveat is scope: this is a database-analytics suite, not a general coding collection, the discovery stub alone does nothing, and the full workflow guides are fetched from the CLI at runtime, so the agent needs the wren CLI installed and a configured connection profile.

## Usage

| You say | What happens |
|---|---|
| Set up my Postgres database | Uses wren-onboarding to check the environment, scaffold a project, and run a first query |
| Generate an MDL from my schema | Uses wren-generate-mdl to explore the database and emit MDL YAML |
| Who are our top 10 customers this quarter? | Uses wren-usage to recall MDL context, write governed SQL, and execute it |
| Connect my Stripe data | Uses wren-dlt-connector to run a dlt pipeline into DuckDB and generate a project |
| Enrich my project with business context | Uses wren-enrich-context to add enum meanings, units, and named metrics |
| Turn that into a dashboard | Uses the genbi workflow guide to build and deploy a browser-side GenBI app |

## Verification

Confirm the discovery stub and a representative workflow guide resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/canner/wrenai/main/skills/wren/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/canner/wrenai/main/core/wren/src/wren/skills_content/generate-mdl/SKILL.md | head -40
```

Both URLs return 200. After installing, review the fetched workflow guides before relying on them; the full guides ship inside the wren CLI rather than in the repository stub.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| wren | Pass | Pass | Pass |
| wren-generate-mdl | Pass | Pass | Pass |
| wren-usage | Pass | Pass | Pass |

Across the 3 sampled skills there are 9 Pass, 0 Warn, and 0 Fail cells. skills.sh sampled only 3 of the 6 listings, so wren-onboarding, wren-dlt-connector, and wren-enrich-context carry no published verdict.

## Limitations

- Snapshot data, verified Nov 26, 2026: 2,865 combined installs across 6 indexed listings; 18,407 GitHub stars; NOASSERTION license field (README states Apache 2.0); last pushed Nov 26, 2026. Counts drift over time.
- GitHub reports NOASSERTION for the license field, but the README states Apache 2.0 and the tree carries LICENSE-APACHE-2.0, LICENSE-AGPL-3.0, and LICENSE-CC-BY-4.0 files; the core engine, SDK, and skills are documented as Apache-2.0.
- skills.sh sampled only 3 of the 6 indexed listings; the other three have no published security verdict.
- The indexed listings map to two different tree layouts: wren is the discovery stub at skills/wren/SKILL.md, while the workflow guides live under core/wren/src/wren/skills_content/.
- The discovery stub alone does nothing; full workflow guides are fetched from the installed wren CLI at runtime, so the agent needs the CLI and a configured connection profile.
- This is a database-analytics suite, not a general coding collection; its value is governance over SQL and business definitions.

## Related

[Data Analytics Skills - 31-Skill Analyst Suite Setup](/hermes/skills/catalog/data-analytics-skills-setup) | [PostHog Skills](/hermes/skills/catalog/posthog-analytics-skills-setup) | [ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the CLI before the skills stub: the stub is a discovery pointer, and the full guides come from `wren skills get <name>`.
- Generate the MDL first (wren-generate-mdl), then enrich it (wren-enrich-context) before asking analytical questions.
- Keep the MDL and context files in Git; Wren's model is that business definitions are reviewable, diffable files.
- Use `wren ask "<question>" --guided` for weaker agents and `--direct` for stronger ones.
- Review the security pages on skills.sh for the three unsampled listings before production use.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
