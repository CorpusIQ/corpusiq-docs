---
title: "Data Analytics Skills - 31-Skill Analyst Suite Setup"
description: "nimrodfisher/data-analytics-skills: 8.0K combined installs across 31 listings, the analyst workflow: EDA, root cause, dashboards, exec summaries, QA"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/data-analytics-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "data analytics", "sql", "dashboards"]
---

# Data Analytics Skills - Setup Guide

**Source:** [nimrodfisher/data-analytics-skills](https://www.skills.sh/nimrodfisher/data-analytics-skills) via skills.sh - 8.0K combined installs across 31 indexed listings; first seen Nov 13, 2026
**GitHub:** 530 stars, MIT license, `main` branch, last pushed 2026-11-08, 31 `SKILL.md` files in six numbered category folders, 178 files in total
**Category:** Analytical workflow skills for analysts, analytics engineers and data teams
**Quality Tier:** 🟢 Green - a 31-for-31 listing tree, an MIT licence and a categorised README with a zero-setup quick start.

Thirty-one skills, six numbered folders, and a README that argues a position: traditional AI assistants need schemas, metric definitions and business rules loaded before they are useful, and these skills instead ask for the minimum viable context at the moment they run.

The numbers are clean. Every indexed listing has a folder, every folder has a `SKILL.md`, and the install band runs from 228 to 326, a spread of 98 across all 31. That flatness says the suite is installed as a unit, so the ranking tells you which skills the maintainer leads with rather than which ones are independently popular.

The structure is the analyst workflow in order: 3 data quality and validation skills, 7 for documentation and knowledge, 7 for analysis and investigation, 5 for storytelling and visualisation, 5 for stakeholder communication, 4 for workflow optimisation. That adds to 31, and it means the suite has an opinion about what a good piece of analysis contains.

Seven of the 31 are about writing down what you did: `analysis-documentation`, `analysis-assumptions-log`, `semantic-model-builder`, `data-catalog-entry`, `sql-to-business-logic`, `metric-reconciliation` and `schema-mapper`. That ratio is the unusual part of the pack.

## Installation

There is no packaged installer and no `npx skills add` command in this repository. The README documents a clone and a copy:

```bash
git clone https://github.com/nimrodfisher/data-analytics-skills.git
```

Claude Code, personal skills for all projects:

```bash
cp -r 01-data-quality-validation/programmatic-eda ~/.claude/skills/
```

Codex, user skills for all repositories:

```bash
cp -r 01-data-quality-validation/programmatic-eda ~/.agents/skills/
```

Swap the folder for any skill you want, and repeat per skill. For project-scoped installs the README points at `.claude/skills/` inside the project for Claude Code and `.agents/skills/` at the repository root for Codex.

The README also links QUICKSTART.md, which walks through a first skill in five minutes, and STRUCTURE.md, which describes how a skill is packaged.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| time-series-analysis | 326 | Trend detection, seasonality and forecasting over time-based data. |
| executive-summary-generator | 297 | Turning detailed analysis into an executive summary for a deck or a board paper. |
| dashboard-specification | 294 | Dashboard requirements as a spec: metrics, layout and behaviour. |
| data-quality-audit | 288 | Quality assessment against business rules, schema constraints and freshness expectations. |
| metric-reconciliation | 288 | Tracing and resolving the same metric showing different values in two sources. |
| funnel-analysis | 287 | Conversion funnels with drop-off investigation at each step. |
| programmatic-eda | 282 | Systematic exploratory profiling: structure, nulls and sanity checks on a new dataset. |
| insight-synthesis | 278 | Turning findings into insights a business reader can act on. |
| root-cause-investigation | 276 | Structured diagnosis when a metric moves unexpectedly. |
| visualization-builder | 268 | Chart type selection, design guidance and a spec the agent can build from. |
| segmentation-analysis | 260 | Customer or user segments with profiles attached. |
| cohort-analysis | 256 | Time-based cohorts with retention and behaviour tracking. |
| business-metrics-calculator | 255 | Standard metric maths (MRR, churn, conversion) with benchmark comparison. |
| analysis-assumptions-log | 253 | A running log of analytical assumptions and decisions. |
| data-narrative-builder | 251 | A story arc built from the findings rather than a list of charts. |
| analysis-qa-checklist | 250 | A pre-delivery quality gate before results go to a stakeholder. |

The remaining 15 indexed listings range from 228 to 246 installs.

## Why This Matters for Hermes Agents

Analysis is where an agent has the most room to be plausible and wrong. The tools rarely fail; the framing does. A model asked to explain a metric drop will happily produce five hypotheses, three of which are the same hypothesis, and none of which is written down anywhere afterwards.

This suite's contribution is sequence. `analysis-planning` comes before the work, `programmatic-eda` and `data-quality-audit` come before the analysis, `analysis-assumptions-log` runs alongside it, and `analysis-qa-checklist` runs before delivery. An agent with those four loaded behaves differently from one with a single analysis skill, because the workflow has a start and an end rather than a middle.

The documentation skills are the other half. `sql-to-business-logic`, `semantic-model-builder` and `data-catalog-entry` produce artefacts that outlive the request, which is the difference between an agent that answers a question and one that leaves the team with something reusable.

The communication skills address the most common complaint about AI analysis output: it is technically correct and impossible to forward. `technical-to-business-translator`, `methodology-explainer` and `impact-quantification` are written for the gap between the person who ran the numbers and the person who has to approve the decision.

None of these skills ship a connector. They assume the agent can already reach the data, through SQL, a file, or a tool you have wired up, and they tell it what to do once it gets there.

## Usage

| You say | What happens |
|---|---|
| "I need to understand why activation dropped 12% last week" | Runs `root-cause-investigation` and works a structured diagnosis with hypotheses. |
| "Profile this dataset before we trust it" | Runs `programmatic-eda` then `data-quality-audit` and reports structure, nulls and rule violations. |
| "Review this SQL before it goes into the model" | Runs `query-validation` on correctness, performance and edge cases. |
| "Our revenue number is different in the dashboard and the finance report" | Runs `metric-reconciliation` and traces the two definitions. |
| "Spec a dashboard for the weekly leadership review" | Runs `dashboard-specification` and returns metrics, layout and behaviour. |
| "Turn these findings into a two-page summary for the board" | Runs `executive-summary-generator` and `insight-synthesis`. |
| "Explain what this query actually calculates, in business terms" | Runs `sql-to-business-logic` and returns the plain-language definition. |
| "Review my analysis before I send it" | Runs `analysis-qa-checklist` as a pre-delivery gate. |

## Verification

Two skills on the branch, both returning 200:

```bash
curl -fsSL https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/main/03-data-analysis-investigation/time-series-analysis/SKILL.md | head -10
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/nimrodfisher/data-analytics-skills/main/01-data-quality-validation/programmatic-eda/SKILL.md
```

After installing, confirm the folder count: 31 skill directories spread across the six numbered folders, one `SKILL.md` each, and 178 files in the repository overall. If a copy produced a folder with no `SKILL.md`, the `cp -r` picked up the wrong level of the tree.

Check the agent's discovery path too. Claude Code reads `~/.claude/skills/` and `.claude/skills/`; Codex reads `~/.agents/skills/` and `.agents/skills/`. A skill copied into the wrong one is invisible rather than broken.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| time-series-analysis | Pass | Pass | Pass |
| executive-summary-generator | Pass | Pass | Pass |
| dashboard-specification | Pass | Pass | Pass |
| data-quality-audit | Pass | Pass | Pass |

Four of the 31 listings carry published verdicts; the other 27 are unrated rather than cleared. Every file in the tree is prose, so the risk profile is the ordinary one for a skill pack: the agent will follow instructions, and the instructions are about data you have already decided it can see. Scope that access before you install, not after.

## Limitations

- Snapshot data, verified 2026-11-13: 7,984 combined installs across 31 indexed listings; 530 GitHub stars; MIT license; last pushed 2026-11-08. Counts drift over time.
- There is no packaged installer. Install is a clone plus `cp -r` per skill, which means no version pinning, no update command and no manifest to diff when the repository moves.
- The install band is extremely flat: the whole suite runs from 228 to 326 installs, so these numbers describe a suite installed as a unit and say nothing about relative quality between skills.
- The skills assume the agent can already reach the data. No connector ships, so without SQL access, a warehouse tool or a file path the agent can read, most of the set has nothing to work on.
- One maintainer. The README footer says version 1.2.0 and last updated September 2026 while the repository was pushed 2026-11-08, so the documentation lags the tree slightly.
- The README cross-promotes the maintainer's paid product, Caliboard, for plan review. The 31 skills are the free part.

## Related

- [Metabase Skills - BI and Dashboard Agent Suite](/hermes/skills/catalog/metabase-skills-setup)
- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `programmatic-eda` on a dataset you already know. It shows you how the other 30 will behave before you rely on them for something that matters.
- Load `analysis-planning` first on any request that is more than one query. It is the skill that turns a prompt into a scoped piece of work.
- Add a `references/` folder inside the skills you use most, with your schema, metric definitions and business rules. The README documents this as the customisation path, and it is what makes the output company-specific without forking the skill.
- Keep `analysis-assumptions-log` running for anything that will be revisited. The assumptions are the part nobody remembers six weeks later.
- Use `metric-reconciliation` the moment two numbers disagree, not after the deck is built. It is the cheapest skill in the pack to run and the most expensive one to skip.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
