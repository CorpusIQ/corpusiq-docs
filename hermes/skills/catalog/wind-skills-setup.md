---
title: "Wind Skills - 82-Skill Financial Terminal Cluster"
description: "wind-alice/alicemarket - 82 skills, 157K+ combined installs. The official agent skill set for Wind, China's dominant financial data terminal - MCP data access plus 79 investment research workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wind-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-11"
tags: ["hermes skill", "agent skill", "skill setup", "finance"]
---

# Wind Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/wind-alice/alicemarket) (157K+ combined installs)
**GitHub:** [Wind-Alice/AliceMarket](https://github.com/Wind-Alice/AliceMarket) (108⭐, 14 forks, pushed Sep 10, 2026)
**Category:** Financial Data & Investment Research
**First Seen:** August 13, 2026 sweep (as `wind-information-co-ltd/wind-skills`); publisher renamed Sep 11, 2026 sweep - `github.com/wind-information-co-ltd/wind-skills` now 301-redirects to `Wind-Alice/AliceMarket`
**Quality Tier:** 🟢 Production (data access) / 🟡 Beta (research skills)

Wind Information is China's Bloomberg-equivalent - the dominant financial data terminal for Chinese markets (A-shares, bonds, funds, macro). This official cluster gives agents two things: MCP-based access to Wind's data feeds, and a large library of investment-research workflows (DCF models, valuation snapshots, backtests, post-market debriefs, earnings analysis). The strongest signal for agent-native institutional finance from an Asian data vendor to date.

---

## Installation

```bash
npx skills add wind-alice/alicemarket
```

> **Publisher rename (Sep 11, 2026):** the skills.sh source and GitHub repo moved from `wind-information-co-ltd/wind-skills` to `wind-alice/alicemarket` (Wind-Alice/AliceMarket). Install commands referencing the old slug should be updated.

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| wind-mcp-skill | 151.6K | MCP integration for Wind data access |
| wind-find-finance-skill | 24.5K | Finding the right Wind financial dataset |
| wind-alice | 3.1K | Wind's AI assistant (Alice) integration |
| post-market-debrief | 549 | End-of-day market summary generation |
| equity-investment-thesis | 450 | Thesis construction for equity positions |
| backtest-expert | 447 | Strategy backtesting workflows |
| sector_rotation_radar_skill | 422 | Sector rotation signals |
| a-share-primary-theme-identification | 420 | A-share market theme detection |
| valuation-pricing-framework / dcf-model / valuation_snapshot_skill | 264-297 | Valuation: framework, DCF, snapshot |
| earnings-analysis / guidance_change_impact_skill / sec_filing_question_answer_skill | 166-262 | Earnings and filings research |
| position_sizing_decision_skill / position-sizer / stop_loss_discipline_skill / take_profit_ladder_skill | 190-257 | Trade construction and risk discipline |
| avatar-warren-buffett-investing / avatar-charlie-munger-thinking / avatar-nassim-taleb-risk / avatar-naval-ravikant-thinking | 95-115 | Investor-persona reasoning lenses |
| (63 more) | <100 each | Market regime, themes, breadth, announcements, PEAD, dividends, watchlists |

Full inventory: 82 skills spanning data access, research, trade planning, and persona-based reasoning.

## Prerequisites

- Wind terminal account or Wind MCP access (data skills require credentials)
- For A-share data: mainland China data-access terms apply

## CorpusIQ Use Cases

- **Business-data connector parity** - Wind's MCP pattern is a reference architecture for CorpusIQ's own multi-connector endpoint; study how they expose terminal data to agents
- **Finance vertical intelligence** - research workflows (DCF, earnings analysis) as templates for finance-focused CorpusIQ users
- **Market-ecosystem insight** - the persona-avatar skills show how established finance vendors package reasoning frameworks for agents

## Limitations / Verification

- Data access is gated by Wind credentials; the research skills work standalone with any data source
- Verify: `wind-mcp-skill` MCP endpoint returns a dataset query successfully before relying on it

## Related

- [Microsoft Azure Skills - Cloud Platform Setup](/hermes/skills/catalog/microsoft-azure-skills-setup/)
- [CorpusIQ - one MCP endpoint, all your business tools](https://corpusiq.io)
