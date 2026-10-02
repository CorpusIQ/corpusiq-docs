---
title: "Wind Skills - 82-Skill Financial Terminal Cluster"
description: "wind-alice/alicemarket - 71 skills indexed, 174K+ combined installs (Sep 15, 2026 snapshot). The official agent skill set for Wind, China's dominant financial data terminal - MCP data access plus a large library of investment research workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wind-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-15"
tags: ["hermes skill", "agent skill", "skill setup", "finance"]
---

# Wind Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/wind-alice/alicemarket) (174K+ combined installs)
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
| wind-mcp-skill | 157.6K | MCP integration for Wind data access |
| wind-find-finance-skill | 24.5K | Finding the right Wind financial dataset |
| wind-alice | 3.1K | Wind's AI assistant (Alice) integration |
| post-market-debrief | 670 | End-of-day market summary generation |
| equity-investment-thesis | 569 | Thesis construction for equity positions |
| sector_rotation_radar_skill | 510 | Sector rotation signals |
| a-share-primary-theme-identification | 501 | A-share market theme detection |
| trade_plan_builder_skill | 418 | Trade plan construction |
| market_regime_switch_skill | 404 | Market regime detection |
| valuation-pricing-framework / valuation_snapshot_skill | 393 / 324 | Valuation: framework, snapshot |
| peer_comparison_decision_skill | 338 | Peer comparison decisions |
| theme_leader_identification_skill | 334 | Theme-leader identification |
| position_sizing_decision_skill / stop_loss_discipline_skill / take_profit_ladder_skill | 326 / 251 / 231 | Trade construction and risk discipline |
| breakout_candidate_finder_skill / pullback_opportunity_finder_skill | 298 / 278 | Entry-pattern scanning |
| bull_bear_case_builder_skill / business_model_decoder_skill | 278 / 275 | Thesis building |
| institutional_position_shift_skill / major_announcement_impact_skill | 273 / 273 | Event-driven research |
| high_quality_compounder_finder_skill / moat_strength_review_skill | 268 / 250 | Quality screening |
| conference_call_takeaway_skill / guidance_change_impact_skill / sec_filing_question_answer_skill | 232 / 203 / 202 | Earnings and filings research |
| industry_chain_signal_skill / macro_event_market_impact_skill | 228 / 188 | Macro and industry signals |
| avatar-warren-buffett-investing / avatar-charlie-munger-thinking / avatar-nassim-taleb-risk / avatar-naval-ravikant-thinking | 154 / 146 / 149 / 129 | Investor-persona reasoning lenses |
| market_sentiment_temperature_skill / market_breadth_health_skill / daily_watchlist_morning_brief_skill / intraday_abnormal_move_alert_skill | 149 / 146 / 148 / 147 | Sentiment, breadth, watchlist, alert workflows |
| premarket_trade_checklist_skill / theme_heat_tracker_skill / volume_spike_reasoning_skill | 121 / 119 / 114 | Premarket, theme-heat, volume-spike workflows |
| ~20 more workflow skills | 100-133 | Dip-buy, PEAD, dividends, buybacks, breakout execution, exits, earnings calendars, capital flows |
| (8 more) | <100 each | Long tail below the 100-install bar |

Full inventory: 71 skills indexed on skills.sh (Sep 15, 2026 snapshot) - 63 at 100+ installs, 8 below the bar; the repo ships the full Alice skill library. Data access, research, trade planning, and persona-based reasoning.

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

- [Microsoft Azure Skills - Cloud Platform Setup](/hermes/skills/catalog/microsoft-azure-skills-setup)
- [CorpusIQ - one MCP endpoint, all your business tools](https://corpusiq.io)
