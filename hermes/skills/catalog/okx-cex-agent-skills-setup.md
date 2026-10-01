---
title: "OKX CEX Agent Skills - Exchange Trading Suite Setup"
description: "Setup guide for okx/agent-skills - 9 official OKX skills for AI agents: market data, spot/perp trading, grid & DCA bots, portfolio, earn, and smart-money analytics."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/okx-cex-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-30"
tags: ["hermes skill", "agent skill", "skill setup", "crypto exchange", "trading bot", "okx"]
---

# OKX CEX Agent Skills - Setup Guide

**Source:** [okx/agent-skills](https://github.com/okx/agent-skills) (184⭐, MIT, pushed Sep 23, 2026)
**Skill family:** `okx/agent-skills` (9 installable skills, ~79K combined installs)
**Sibling family:** [okx/onchainos-skills](/docs/hermes/skills/catalog/okx-onchainos-skills-setup) (224K installs - onchain / DeFi side of the same publisher)
**Category:** Finance / Crypto Exchange
**Quality Tier:** 🟢 Verified (official OKX publisher, MIT LICENSE file in-repo, active release cadence - verified Sep 30, 2026)

OKX publishes this official skill family for AI agents driving the OKX **centralised exchange** (CEX) through a single `okx` CLI. Each skill is a self-contained Markdown file with YAML frontmatter that routes on natural-language triggers (English + Chinese). Coverage spans public market data with 70+ technical indicators, spot/perpetual/futures/options order management, grid and DCA-Martingale bots, account and portfolio operations, Simple/On-chain Earn, smart-money leaderboard analytics, and crypto sentiment tracking. This is the CEX counterpart to OKX's larger onchain skills family - together they form the largest crypto skill footprint on skills.sh.

---

## Installation

Skills require the `okx` CLI (npm package `@okx_ai/okx-trade-cli`):

```bash
# 1. Install the CLI
npm install -g @okx_ai/okx-trade-cli

# 2. Add the skill family
npx skills add okx/agent-skills

# Or install a single skill
npx skills add okx/agent-skills --skill okx-cex-market
```

Credentials for authenticated skills (OAuth recommended, or API key):

```bash
okx config init          # API-key path, writes ~/.okx/config.toml
# Or run the okx-cex-auth skill for OAuth 2.0 device-flow login
```

## Roster - Core Skills

| Skill | Installs | Does |
|---|---|---|
| okx-cex-market | 9,988 | Public market data: prices, tickers, order books, candles, funding rates, open interest, 70+ indicators (RSI, MACD, Bollinger, SuperTrend, AHR999) |
| okx-cex-trade | 9,895 | Order management: spot, perpetual swap, dated futures, options, event contracts; TP/SL, trailing stop, iceberg, TWAP, OCO |
| okx-cex-portfolio | 9,700 | Balances, positions, P&L, trading fees, account config, transfers, position-mode switching |
| okx-cex-bot | 9,536 | Grid bots (spot / USDT-margin / coin-margin) and DCA-Martingale bots; create, amend, stop, monitor, AI-suggested params |
| okx-cex-earn | 8,861 | Simple Earn (flexible / fixed / lending), Flash Earn, On-chain Earn, Dual Investment (DCD), AutoEarn |
| okx-cex-skill-mp | 7,772 | OKX Skills Marketplace: search, browse, install, update, remove, verify Ed25519 signatures |
| okx-sentiment-tracker | 7,345 | Crypto news, coin-level sentiment, trending coins, social buzz, market mood |
| okx-cex-auth | 5,487 | OAuth 2.0 device-flow login / API-key setup; install and manage the `okx-auth` helper binary |
| okx-cex-smartmoney | 5,446 | Smart-money analytics: leaderboard traders, position tracking, trade records, consensus signals |

Additional indexed listings: `earn-hunter` (2,823), `okx-outcomes` (2,054).

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Market-research enrichment** | `okx-cex-market` supplies indicator and funding-rate data for operator research briefs without a separate data vendor |
| **Agentic automation patterns** | The family is a reference implementation of CLI-backed, frontmatter-routed agent skills - useful for CorpusIQ's own skill authoring |
| **Sentiment signals** | `okx-sentiment-tracker` + `okx-cex-smartmoney` feed crypto/product sentiment into competitive and market monitoring |
| **Catalog cross-link** | Pairs with the documented `okx/onchainos-skills` guide to complete OKX coverage across CEX + onchain |

## Limitations / Verification

- Authenticated skills (trade, portfolio, bot, earn, smartmoney, skill-mp, sentiment) require OKX credentials; `okx-cex-market` is public and needs no auth
- Skills drive a **live trading CLI** - use read-only skills first; never enable trade/bot skills without explicit user intent and small position limits
- Description fields carry a 1024-char Codex limit (OKX targets ≤900); skills share helpers via `skills/_shared/` (e.g. `preflight.md`)
- Verify: `npx skills add okx/agent-skills --list` shows 9 skills
- Repo tree at sweep time: 10 `SKILL.md` files under `skills/` (9 published + shared helper)

## Security

No skills.sh Trust Hub / Socket / Snyk verdicts published (verified Sep 30, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

**Note:** the `okx-cex-skill-mp` SKILL.md itself carries a third-party-content warning - skills installed *from* the OKX Marketplace are authored by independent developers and are not reviewed by OKX. Treat marketplace-sourced skills with standard third-party due diligence.

## Related

- [OKX OnchainOS Skills - Wallet & DEX Setup](/docs/hermes/skills/catalog/okx-onchainos-skills-setup)
- [Hermes Agent Official Skills Setup](/docs/hermes/skills/catalog/hermes-agent-official-skills-batch-setup)
- [Skills Catalog](/docs/hermes/skills/catalog)
- [Skills Marketplace](/docs/hermes/skills/marketplace)
