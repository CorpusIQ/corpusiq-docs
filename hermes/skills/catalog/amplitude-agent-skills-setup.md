---
title: "Amplitude Agent Skills - Product Analytics Setup"
description: "Setup guide for amplitude/mcp-marketplace: 38 official Amplitude agent skills for product analytics, instrumentation, taxonomy and event discovery."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/amplitude-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skill setup", "amplitude", "analytics", "product data"]
---

# Amplitude Agent Skills - Setup Guide

**Source:** [amplitude/mcp-marketplace](https://github.com/amplitude/mcp-marketplace) (42 stars, MIT LICENSE; actively maintained - pushed Oct 8, 2026)
**Skill family:** `amplitude/mcp-marketplace` (39 SKILL.md files in-repo; 38 indexed listings)
**Combined Installs:** ~175,215 across indexed listings (Oct 8, 2026 snapshot)
**Category:** Analytics / Product Data
**Quality Tier:** Production (official Amplitude publisher; MIT LICENSE in-repo; active development - verified Oct 8, 2026)

The official Amplitude plugin for AI coding tools: "Turn your AI assistant into a product analyst - instrument analytics, analyze charts, run experiments, and understand users directly from your editor." It works with Claude Code, Cursor, Codex, Gemini CLI, and Claude. The roster covers the full product-data loop: discover where events can be captured, plan and diff instrumentation changes, implement events against a tracking plan (taxonomy, naming conventions, data-quality audits, funnel design, event deprecation policy), then analyze charts, dashboards, experiments, cohorts, and user journeys, with daily and weekly briefs for ongoing reporting. A first-run onboarding skill handles US vs EU data residency, Docs MCP setup, and project access, and `event-description-generator` shows an orchestrator pattern that delegates chunk work to worker subagents. 38 skills are indexed on skills.sh; six flagship workflows carry nearly all of the installs so far.

---

## Installation

```bash
# skills.sh - install the full suite
npx skills add amplitude/mcp-marketplace

# Or install a single skill
npx skills add amplitude/mcp-marketplace --skill taxonomy
```

Claude Code users can install the plugin directly:

```bash
claude plugin install amplitude
```

Or from inside a Claude Code session:

```text
/plugin install amplitude
/reload-plugins
```

## Roster - Indexed Skills

Six flagship skills carry the suite (installs from the Oct 8, 2026 skills.sh snapshot):

| Skill | Domain | Installs | What It Does |
|---|---|---|---|
| discover-event-surfaces | Event discovery | 29,271 | Scans a codebase for surfaces where events can be captured before instrumentation is added |
| diff-intake | Change planning | 29,262 | Intakes and diffs instrumentation changes so tracking edits stay reviewable |
| discover-analytics-patterns | Analytics discovery | 29,259 | Finds analytics patterns in an app to guide instrumentation and reporting |
| instrument-events | Instrumentation | 29,202 | Implements event instrumentation in the codebase |
| taxonomy | Taxonomy / governance | 29,101 | "Taxonomy Generation & Data Auditing": tracking plans, event and property naming conventions, data-quality audits (duplicates, stale events, missing metadata), funnel design, event deprecation policy, AI-readiness |
| add-analytics-instrumentation | Instrumentation | 28,969 | Adds analytics instrumentation to a product surface |

**Long tail (32 skills, 1-6 installs each):** the analysis, monitoring, and reporting class - `create-chart`, `create-dashboard`, `analyze-chart`, `analyze-dashboard`, `analyze-experiments`, `monitor-experiments`, `compare-user-journeys`, `user-cohort-forensics`, `live-data-forensics`, `replay-ux-audit`, `debug-replay`, `diagnose-errors`, `daily-brief`, `weekly-brief`, `scheduled-report-refresh`, `tracking-plan-audit`, and more. Two standouts: `event-description-generator` (5 installs) orchestrates and delegates chunk work to worker subagents, and `getting-started-with-amplitude` (in the repo tree; not in the indexed roster) covers first-run onboarding: US vs EU data residency, Docs MCP, and project access.

## Why This Matters for Hermes Agents

Product-analytics instrumentation and reporting is a recurring operator workflow: wiring events correctly, keeping tracking plans clean, and turning charts and experiments into decisions. This suite keeps that loop inside the agent session - discover event surfaces, plan and diff instrumentation changes against a tracking plan, then pull daily or weekly briefs without a human re-explaining metric definitions each time. Clean tracking plans also matter because agents read the same event names humans do: a consistent taxonomy is what keeps product data queryable by the automations built on top of it.

## Usage and Triggers

| Action | Prompt / Command |
|---|---|
| Plan instrumentation | "Find where signup and checkout events should be instrumented in this codebase" |
| Audit taxonomy | "Review our tracking plan for naming-convention violations, duplicate events, and missing metadata" |
| Instrument events | "Implement the events in this tracking plan and show me the diff before applying it" |
| Analyze experiments | "Analyze the results of our latest A/B experiment and summarize the winner" |
| Report | "Generate this week's product brief from our Amplitude dashboards" |

## Verification

```bash
# Spot-check the source repo (expect: 42 stars, pushed 2026-10-08, MIT)
curl -s https://api.github.com/repos/amplitude/mcp-marketplace | grep -E '"stargazers_count"|"pushed_at"'
```

After installing, start with an audit-style workflow - run the `taxonomy` skill against a sample tracking plan and review its output - before letting the agent touch production instrumentation. No live install test was performed for this guide; counts and verdicts are the Oct 8, 2026 skills.sh snapshot.

## Security

skills.sh per-skill verdicts (sampled: taxonomy, verified Oct 8, 2026) - verdicts vary per skill; check the skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| taxonomy | Pass | Pass | Warn |

## Limitations

- The repo is named `mcp-marketplace` while the Amplitude plugin content ships under `plugins/amplitude/skills/` (37 skills), plus one skill each under `plugins/amplitude-grok/` and `plugins/amplitude-experimental/`. The tree carries 39 SKILL.md files against 38 indexed listings, so small index/repo drift is normal.
- Install distribution is top-heavy: the six flagship skills carry 175,064 of the 175,215 combined installs; the remaining 32 sit at 1-6 installs each, so treat the long tail as new rather than field-proven.
- First seen in the Mar 31, 2026 sweeps; all numbers here are the Oct 8, 2026 snapshot and will drift.
- Only a subset of skill bodies was reviewed for this guide (taxonomy, event-description-generator, getting-started-with-amplitude); other descriptions derive from skill names and the README.
- Instrumentation skills change real product code: run them on a branch and review diffs before merging.

## Related

- [HubSpot Agent CLI Skills Setup Guide](/hermes/skills/catalog/hubspot-agent-cli-skills-setup) - official CRM tooling as agent skills; the closest product-ops sibling in the catalog
- [Datadog Agent Skills Setup](/hermes/skills/catalog/datadog-agent-skills-setup) - monitoring and observability skills for the operational half of the stack
- [Databricks Agent Skills - Data & AI Platform Skills](/hermes/skills/catalog/databricks-agent-skills-setup) - data platform skills for warehouse and lakehouse workflows
- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

1. Start with the flagships: `discover-event-surfaces` then `diff-intake` then `taxonomy` is the natural order for a fresh instrumentation project; review each output before moving on.
2. Run `taxonomy` before generating new events - it audits duplicates, stale events, and missing metadata first, so you instrument only what the plan actually needs.
3. `event-description-generator` delegates chunk work to worker subagents; scope each chunk to one module or file and verify the merged output.
4. The long tail is where monitoring and reporting live (`daily-brief`, `weekly-brief`, `monitor-experiments`); install the full suite rather than just the flagships.
5. Install counts lag reality: when a long-tail skill matches your workflow, read its SKILL.md and test it instead of dismissing it on its 1-6 install count.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
