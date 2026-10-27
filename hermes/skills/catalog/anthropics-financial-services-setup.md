---
title: "Anthropic Financial Services Skills - Deal Workflow Suite"
description: "Anthropic's official financial services suite: 31.1K combined installs. DCF, comps, 3-statement models, earnings notes, pitch decks, Excel audit."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/anthropics-financial-services-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "finance", "investment banking", "excel modeling"]
---

# Anthropic Financial Services - Setup Guide

**Source:** [anthropics/financial-services](https://www.skills.sh/anthropics/financial-services) via skills.sh - 31.1K combined installs across 13 indexed listings; first documented 2026-10-27 (Oct 27 morning sweep)

**GitHub:** [anthropics/financial-services](https://github.com/anthropics/financial-services) - 40,842 stars, Apache-2.0, branch main, 112 skill directories across `plugins/agent-plugins/`, `plugins/vertical-plugins/` and `plugins/partner-built/`

**Category:** Finance and investment banking

**Quality Tier:** 🟡 Beta - official Anthropic repository, small install spread across 13 listings, no community track record yet

This is Anthropic's own reference implementation for financial services work: investment banking, equity research, private equity, fund administration and wealth management. The repository ships named workflow agents (Pitch Agent, Market Researcher, Earnings Reviewer, Model Builder, GL Reconciler, Month-End Closer and others), vertical skill bundles that carry the individual skills and slash commands, and MCP connectors to market data providers such as Daloopa, Morningstar, FactSet, Moody's, LSEG, PitchBook and Box.

Everything is file based, markdown and JSON with no build step, and it is delivered two ways from one source: install it as a Claude Cowork plugin, or deploy the same system prompt and skills through the Claude Managed Agents API behind your own workflow engine. That second path is what makes the repository interesting outside the Claude client. The skills are the expensive part to write, and they are readable, forkable and portable.

The install index tracks thirteen of those skill directories individually, from `earnings-analysis` at the top of the list down to `initiating-coverage`. Ten are authored by Anthropic's financial services team and three, `equity-research`, `macro-rates-monitor` and `option-vol-analysis`, come from the LSEG partner plugin.

## Installation

Two paths, both documented in the repository README. For Claude Code, add the marketplace once and then install the plugins you want. The core `financial-analysis` plugin carries the shared modeling skills and all the data connectors, so it goes first:

```bash
claude plugin marketplace add anthropics/financial-services

# Core skills plus connectors
claude plugin install financial-analysis@claude-for-financial-services

# Named agents, install only the workflows you need
claude plugin install pitch-agent@claude-for-financial-services
```

The README also documents `gl-reconciler`, `market-researcher`, `investment-banking` and `equity-research` in the same `@claude-for-financial-services` marketplace. In Cowork the flow is graphical: open Settings, then Plugins, then Add plugin, and either paste `https://github.com/anthropics/financial-services` or upload a zip of any directory under `plugins/` such as `plugins/agent-plugins/pitch-agent/`. The generic skills.sh CLI path works too when you just want the markdown:

```bash
npx skills add anthropics/financial-services
```

Every agent plugin is self contained. Installing `pitch-agent` brings the skills it uses, so you do not have to install the vertical bundles as well. For a headless deployment, the `managed-agent-cookbooks/` directory holds an `agent.yaml` and steering examples per agent, and `scripts/deploy-managed-agent.sh <slug>` posts the orchestrator to `/v1/agents` using your `ANTHROPIC_API_KEY`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| earnings-analysis | 3,365 | Earnings update reports of 8 to 12 pages for companies already under coverage: beat and miss analysis, key metrics, updated estimates, a revised thesis, plus summary tables and charts. |
| equity-research | 3,190 | Equity research snapshots from the LSEG plugin: analyst consensus estimates, company fundamentals, historical prices and macroeconomic context, behind the `/research-equity` command. |
| dcf-model | 2,458 | Discounted cash flow valuation: financials pulled from SEC filings and analyst reports, cash flow projections, WACC, sensitivity analysis and an Excel model with an executive summary. |
| pitch-deck | 2,436 | Filling an existing investment banking pitch deck PowerPoint template from Excel or CSV source files. The skill explicitly does not build decks from scratch. |
| competitive-analysis | 2,402 | Competitive landscape decks: market positioning, competitor deep dives, peer comparison, market maps and strategic synthesis for investment memos. |
| macro-rates-monitor | 2,322 | Macro and rates dashboards from the LSEG plugin: macro indicators, yield curves, inflation breakevens and swap rates, including real versus nominal decomposition. |
| comps-analysis | 2,282 | Comparable company analysis in Excel: operating metrics, valuation multiples and statistical benchmarking, aimed at valuation work and IPO or round pricing. |
| ppt-template-creator | 2,268 | Turning a PowerPoint template the user supplies into a reusable skill, not a presentation. The skill says to use the pptx skill for actual deck authoring. |
| audit-xls | 2,228 | Auditing a spreadsheet for formula accuracy and model integrity: balance sheet balance, cash tie-out and logic sanity, scoped to a range, a sheet or the whole model. |
| 3-statement-model | 2,150 | Completing a 3-statement model template, income statement, balance sheet and cash flow, and linking the statements inside the existing framework. |
| clean-data-xls | 2,075 | Cleaning messy spreadsheet data: whitespace, casing, numbers stored as text, inconsistent dates, duplicates and mixed-type columns flagged before analysis. |
| option-vol-analysis | 1,998 | Options volatility work from the LSEG plugin: vol surfaces, option pricing with Greeks, and implied versus realized volatility for vol premium and strategy analysis. |
| initiating-coverage | 1,959 | Equity research initiation reports through a five-task workflow: company research, financial modeling, valuation, chart generation and final report assembly. |

All 13 indexed listings clear the 1,000-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Financial modeling is the clearest case of a task where plausible output is dangerous. A spreadsheet that balances by coincidence, a comps set whose multiples use the wrong denominator, or a DCF whose terminal value assumes a growth rate above the discount rate all look correct until someone reads them. These skills encode the checks that catch those failures, which is why several of them are written as gates rather than as generators.

The Excel skills are the practical core. `audit-xls` is a review pass over formulas, a balance sheet tie-out and cash flow logic, and `clean-data-xls` is the preparation step that stops a model from being built on columns of numbers stored as text. `dcf-model` and `3-statement-model` produce artifacts a human then reviews, with `xlsx-author` underneath them, and `comps-analysis` adds the benchmarking layer.

For an agent working outside Claude, the value is portability. The layout is one directory per skill with a `SKILL.md`, so the same files drop into a Hermes skills directory and behave like any other agent skill. The connectors are plain `.mcp.json` entries, which means the same market data wiring can be attached to a different client without rewriting the skill.

The honest caveat is scope. These are covered-company workflows for a bank or a research desk: they assume a company, a template and a data source already exist. They will not source deal flow and they do not make recommendations.

## Usage

| You say | What happens |
|---|---|
| "Write the Q3 earnings update for this covered name" | earnings-analysis drafts the update report with beat and miss analysis, updated estimates and a revised thesis, with tables and charts. |
| "Build me a DCF for this company and stress the WACC" | dcf-model pulls the financials, builds projections, runs sensitivity on WACC and terminal value, and writes an Excel model with a summary page. |
| "Fill the pitch deck template with these comps" | pitch-deck maps the source data into the existing slide layouts instead of rebuilding the deck. |
| "Check this model, it will not balance" | audit-xls walks the formulas and the balance sheet, cash and logic checks and reports the breaks by range or sheet. |
| "Who are the competitors and how do they position" | competitive-analysis builds the landscape view with peer comparison and positioning, then feeds a memo or deck. |
| "Write the initiation report on this name" | initiating-coverage runs the five-task workflow in order, stopping where a later task depends on an unverified earlier one. |
| "Clean this sheet before we model it" | clean-data-xls normalizes casing, text-stored numbers, dates and duplicates, and flags mixed-type columns. |

## Verification

Inspect the layout on main before installing anything. Every in-tree skill uses `plugins/<plugin>/skills/<name>/SKILL.md`, which differs from the flat `skills/<name>/` layout many repositories use:

```bash
for p in \
  plugins/agent-plugins/earnings-reviewer/skills/earnings-analysis/SKILL.md \
  plugins/agent-plugins/model-builder/skills/dcf-model/SKILL.md \
  plugins/vertical-plugins/financial-analysis/skills/audit-xls/SKILL.md \
  plugins/vertical-plugins/equity-research/skills/initiating-coverage/SKILL.md \
  plugins/partner-built/lseg/skills/equity-research/SKILL.md ; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/anthropics/financial-services/main/$p"
done
```

Five probes, all HTTP 200 when this guide was written on 2026-10-27. Read three skills before granting a spreadsheet or a data connector:

- https://raw.githubusercontent.com/anthropics/financial-services/main/plugins/agent-plugins/model-builder/skills/dcf-model/SKILL.md
- https://raw.githubusercontent.com/anthropics/financial-services/main/plugins/agent-plugins/earnings-reviewer/skills/audit-xls/SKILL.md
- https://raw.githubusercontent.com/anthropics/financial-services/main/plugins/partner-built/lseg/skills/equity-research/SKILL.md

After a plugin install, the skills should appear in the plugin's `skills/` directory and the slash commands should resolve in the session. The README names the commands explicitly: `/comps`, `/dcf`, `/earnings` and `/ic-memo`. If a command does not resolve, the plugin did not load, and reinstalling the agent plugin is the usual fix because agent plugins are self contained.

## Security

skills.sh verdicts were not sampled for this fire, so the table below records no third-party verdicts and the reader must check the security pages on skills.sh before any production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| earnings-analysis | Not checked | Not checked | Not checked |
| dcf-model | Not checked | Not checked | Not checked |
| audit-xls | Not checked | Not checked | Not checked |
| comps-analysis | Not checked | Not checked | Not checked |
| initiating-coverage | Not checked | Not checked | Not checked |

The risk model here is different from a documentation skill. These skills read spreadsheets, write Excel and PowerPoint files, and the connectors reach market data services with provider credentials. The README notes that MCP access may require a subscription or API key from each provider, which means secrets sit in the plugin configuration rather than in the skill files. Keep `.mcp.json` out of any repository you push, and review a skill's file writes before running it against a live model.

The repository ships its own check path. `scripts/check.py` lints every plugin manifest and managed-agent manifest, verifies that every cross-file reference resolves, and fails if a bundled skill has drifted from its vertical source. `scripts/validate.py` checks a worker's JSON output against a JSON Schema between subagents. Running the check before a Managed Agents deployment is the cheap way to catch a broken template.

## Limitations

- Snapshot data, verified 2026-10-27: 31,133 combined installs across 13 indexed listings; 40,842 GitHub stars; Apache-2.0; branch main. Counts drift over time.
- Three of the thirteen listings, `equity-research`, `macro-rates-monitor` and `option-vol-analysis`, live under `plugins/partner-built/lseg/` and are authored by LSEG rather than by Anthropic's own vertical plugin teams. They require LSEG data access through the LSEG analytics MCP connector to be useful.
- Nothing in the repository constitutes investment, legal, tax or accounting advice. The README states that these agents draft analyst work product for review by a qualified professional, that they do not make investment recommendations, execute transactions, bind risk, post to a ledger or approve onboarding, and that every output is staged for human sign-off.
- The install index does not map one to one onto installable units. Distribution is by plugin, so `claude plugin install financial-analysis@claude-for-financial-services` brings a bundle of skills rather than one named skill, and several skill names appear in more than one plugin because each agent bundles a synced copy of the skills it uses. The repository's own `scripts/check.py` fails when a bundled copy has drifted from its vertical source, which is the maintainers' acknowledgement of that risk.
- The connectors reach commercial data providers. Every one of the twelve MCP endpoints in the README may need its own subscription or API key, so a full install is not free even though the skills are Apache-2.0.
- Coverage is desk workflow, not research judgment. The skills assume a company already under coverage, a supplied deck or model template, and a licensed data source.

## Related

- [Slavingia Skills - Minimalist Entrepreneur Business Suite](/hermes/skills/catalog/slavingia-skills-setup)
- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [Arize Skills - LLM Observability and Evaluation Setup](/hermes/skills/catalog/arize-skills-setup)
- [Anthropic Cybersecurity Skills Setup Guide](/hermes/skills/catalog/anthropic-cybersecurity-skills-setup)

## Pro Tips

- Install `financial-analysis` first, before any vertical bundle or agent plugin. It carries the modeling skills and all twelve data connectors, and the other plugins assume it is present.
- Do not install the vertical bundles and the agents together. Agent plugins bundle their own copies of the skills, so a mixed install gives you two versions of `audit-xls` and a confusing precedence rule.
- Run `audit-xls` on any model an agent produced before a human sees it. It is the cheapest check in the suite and it catches the class of error that survives a visual read.
- Fork the repository for firm specific conventions rather than editing installed plugin files. Everything is markdown, so a custom house style is a diff on a `SKILL.md`, and a fork survives the next plugin update.
- Keep the LSEG skills separate from the core install. They only earn their context when you actually hold LSEG analytics access.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
