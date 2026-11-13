---
title: "Claude for Financial Services CN - A-Share Analyst Suite"
description: "jwangkun/claude-for-financial-services-cn: 4.6K combined installs across 59 listings, Anthropic's finance workflow suite adapted to A-share research"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-for-financial-services-cn-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "finance", "china", "equity research"]
---

# Claude for Financial Services CN - Setup Guide

**Source:** [jwangkun/claude-for-financial-services-cn](https://www.skills.sh/jwangkun/claude-for-financial-services-cn) via skills.sh - 4.6K combined installs across 59 indexed listings; first seen Nov 12, 2026 (this sweep)
**GitHub:** 890 stars, Apache-2.0 license, `main` branch, last pushed 2026-09-14, 188 `SKILL.md` files under `agent-plugins/` and `vertical-plugins/`, organised as five Claude Code plugins
**Category:** Equity research and deal work for China A-shares
**Quality Tier:** 🟡 Established - a serious, well-structured adaptation of Anthropic's finance suite with 890 stars and a clean license, held back by paid data-source keys, Chinese-language output and Snyk Warns on the skills that reach the network.

Anthropic published a finance skill set for investment banks built on Bloomberg, FactSet and US GAAP. This repository keeps the workflow shape and swaps the plumbing: Wind and iFind as the paid market data sources, AkShare as the free fallback, Chinese accounting standards instead of US GAAP, China treasury yields instead of Treasuries, and the Shenwan and CITIC industry taxonomies instead of GICS. The output formats follow CICC, CITIC and Huatai research conventions.

The suite is packaged as five plugins rather than one flat directory: `china-finance` with 31 skills, `investment-banking`, `private-equity` with 9, `wealth-management` with 5, and `fund-admin`. The README counts 63 skills in total. The tree carries 188 `SKILL.md` files because the numbered skills bundle their own reference skills underneath them, which is also why the skills.sh index sees 59 listings rather than 63.

The data layer is tiered and honest about cost. Wind is the tier-0 source and needs a `WIND_API_KEY`. iFind is tier-1 and needs an `IFIND_AUTH_TOKEN`. AkShare is the free open-source fallback and needs nothing, and the skills degrade to it automatically when iFind is unavailable. Nothing in the suite ships a key, and the README states plainly that the paid sources require registration.

What the installs say: `china-market-data` is roughly five times the next skill, which suggests people are installing the suite for the data access layer first and the modelling workflows second. The remaining 48 listings sit between 1 and 84 installs.

## Installation

The README's one-minute path assumes Claude Code:

```bash
npm install -g @anthropic-ai/claude-code
claude plugin marketplace add jwangkun/claude-for-financial-services-cn
claude plugin install china-finance@claude-for-financial-services-cn
```

Install the other four plugins the same way:

```bash
claude plugin install investment-banking@claude-for-financial-services-cn
claude plugin install private-equity@claude-for-financial-services-cn
claude plugin install wealth-management@claude-for-financial-services-cn
claude plugin install fund-admin@claude-for-financial-services-cn
```

Set the data keys before the first analysis run. `china-finance` reads `WIND_API_KEY` for Wind and `IFIND_AUTH_TOKEN` for iFind; with neither, it falls back to AkShare, which needs no credentials but covers less.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| china-market-data | 149 | The data entry point: A-share quotes, financials and market data through Wind, iFind or AkShare. |
| china-dcf | 95 | DCF valuation for A-shares built on Chinese statements and China treasury rates. |
| china-audit-xls | 95 | Auditing a financial model or workbook for A-share analysis, with formula and tie-out checks. |
| china-comps | 94 | Comparable company analysis: peer groups, multiples and the comparison table. |
| china-sector-overview | 93 | Sector and industry landscape reports with policy context and competitive positioning. |
| china-financial-plan | 93 | Client financial plans covering retirement, education, estate and cash-flow needs. |
| china-dd-checklist | 92 | Due diligence checklists for A-share investments and M&A transactions. |
| china-earnings-analysis | 91 | Post-earnings updates that compare results against guidance and consensus. |
| china-morning-note | 86 | A daily pre-market note: overnight developments, sentiment and trading themes. |
| china-idea-generation | 86 | Systematic screening and idea sourcing across quantitative and thematic filters. |
| china-3-statement-model | 85 | Three-statement models adapted to Chinese accounting rules and disclosure formats. |

The remaining 48 indexed listings range from 1 to 84 installs.

## Why This Matters for Hermes Agents

Most finance skills fail on the data layer, not on the model. A DCF procedure written against US GAAP will quietly produce a wrong number when applied to a Chinese balance sheet, because the line items do not map one to one and the risk-free rate is not the US ten-year. This suite encodes the mapping.

That makes it a useful template as well as a tool. If you run an agent against any non-US market, the pattern here is the one to copy: keep the workflow, replace the data source, replace the accounting conventions, replace the taxonomy, and say which of those you replaced.

The plugin split is practical. A wealth-management advisor does not need the private-equity due diligence checklists, and a PE analyst does not need client financial plans. Installing one plugin keeps the installed instruction surface small enough to review.

The paid key requirement is a feature for once. An agent that can only reach free data will degrade silently; an agent whose data tier is configured explicitly either works or says it cannot.

## Usage

| You say | What happens |
|---|---|
| "Pull the last four quarters for this A-share ticker" | Uses `china-market-data`, resolves the ticker and returns statements with the source tier named. |
| "Build a DCF for this company" | Runs `china-dcf`, builds the projection from Chinese statements and discounts at China treasury rates. |
| "Check this model for errors before I send it" | Runs `china-audit-xls` over the workbook and reports broken ties and formula inconsistencies. |
| "Who are the real comparables for this name?" | Runs `china-comps` with Shenwan and CITIC peer selection and returns a multiples table. |
| "Write the post-earnings note" | Runs `china-earnings-analysis` against guidance and consensus and drafts the variance commentary. |
| "Give me the morning note for my coverage" | Runs `china-morning-note` over overnight developments and pre-market sentiment. |
| "Build the due diligence checklist for this deal" | Runs `china-dd-checklist` and returns the A-share specific list. |

## Verification

Probe a skill in each plugin before installing the set. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/jwangkun/claude-for-financial-services-cn/main/agent-plugins/china-earnings-reviewer/skills/china-market-data/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/jwangkun/claude-for-financial-services-cn/main/vertical-plugins/wealth-management/skills/china-financial-plan/SKILL.md
```

Confirm the plugin registered after installation:

```bash
claude plugin list | grep china-finance
```

Then run one analysis against a ticker you can check by hand. The failure mode here is a silent fallback to AkShare when a paid key is missing, which changes the coverage of the answer without changing its shape.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| china-market-data | Pass | Warn | Warn |
| china-dcf | Pass | Pass | Pass |
| china-audit-xls | Pass | Warn | Pass |
| china-comps | Pass | Pass | Warn |
| china-sector-overview | Pass | Pass | Warn |

The Warns sit on the skills that call out to a market data provider, which is what those skills are for. The practical controls are the API keys: scope them to read-only market data, keep them out of the repository, and set a spend limit on the paid tiers. `china-audit-xls` reads local workbooks, so treat any file you point it at as data it will parse in full.

## Limitations

- Snapshot data, verified 2026-11-12: 4,610 combined installs across 59 indexed listings; 890 GitHub stars; Apache-2.0 license; last pushed 2026-09-14. Counts drift over time.
- The README advertises 63 skills and skills.sh indexes 59 listings. The tree carries 188 `SKILL.md` files because each numbered skill bundles reference skills underneath, so neither number describes the install surface on its own.
- Two of the three data sources are paid and require registration. Without Wind or iFind keys, every skill that needs market data degrades to AkShare, which is free but narrower.
- The skills write Chinese output. Prompts and source material are Chinese-first, so an English-only workflow needs a translation step at the end.
- Apache-2.0 with no contribution guide visible and no release tags: the install follows `main`, and a fork of Anthropic's repository carries that upstream's structure rather than this one's.
- Nothing here is investment advice and no skill independently validates a data point. The numbers are as good as the source tier you configured.

## Related

- [Anthropic Financial Services Skills - Deal Workflow Suite](/hermes/skills/catalog/anthropics-financial-services-setup)
- [Awesome Finance Skills - Market Analysis Pack](/hermes/skills/catalog/awesome-finance-skills-setup)
- [Claude Skills Generator - Coding Setup](/hermes/skills/catalog/claude-skills-generator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `china-market-data` alone. If the data tier does not resolve for your target, none of the modelling skills will be right and the failure will look like a modelling error.
- Install one plugin, not five. `china-finance` at 31 skills is already a large instruction surface, and the other four plugins target different jobs.
- Configure AkShare first, then add a paid key. It gives you a working baseline that you can compare the paid feed against on a single ticker.
- Keep the accounting-convention swap in mind for anything you reuse. A model that reads correctly for an A-share will not read correctly for a Hong Kong dual-listed line without checking which statement set it used.
- Ask for the source tier in the answer. The skills can name which provider supplied a number, and that is the only cheap defense against a silent fallback.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
