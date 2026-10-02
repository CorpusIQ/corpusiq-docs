---
title: "Coinos Skills - AiCoin Crypto Trading Suite Setup"
description: "Setup guide for aicoincom/coinos-skills - 7 agent skills for the AiCoin crypto toolkit: real-time prices, K-lines, freqtrade, hyperliquid."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/coinos-trading-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-27"
tags: ["hermes skill", "agent skill", "skill setup", "crypto", "trading", "market data"]
---

# Coinos Skills - Setup Guide

**Source:** [aicoincom/coinos-skills](https://github.com/aicoincom/coinos-skills) (54⭐, pushed Aug 29, 2026)
**Skill:** `aicoincom/coinos-skills` (7 installable skills)
**Installs:** ~590 per top skill, ~3.3K combined (Sep 27, 2026 snapshot)
**Category:** Crypto / Trading Automation
**Quality Tier:** 🔵 Community (no skills.sh security verdicts published - verified Sep 27, 2026)

AiCoin's official agent skills expose its crypto toolkit (40+ tools) to coding agents: real-time prices, K-lines, AI market analysis, funding rates, whale tracking, on-chain data, and account management. Two of the seven skills wire into third-party trading stacks - `aicoin-freqtrade` (the Freqtrade bot framework) and `aicoin-hyperliquid` (the Hyperliquid DEX) - making the suite a bridge from market intelligence to executable strategies.

---

## Installation

```bash
# Full suite
npx skills add aicoincom/coinos-skills

# Market-data only
npx skills add aicoincom/coinos-skills --skill aicoin-market
```

## Roster - 7 Skills

| Skill | Installs | Does |
|---|---|---|
| aicoin-market | 672 | Real-time prices, K-lines, and market snapshots |
| aicoin-freqtrade | 648 | Freqtrade bot setup and strategy wiring |
| aicoin-hyperliquid | 583 | Hyperliquid DEX orders and positions |
| aicoin-account | 538 | Account, API key, and portfolio management |
| aicoin-trading | 534 | Trade execution workflows |
| aicoin-onchain | 287 | On-chain data and whale tracking |
| aicoin | 29 | Platform entry skill |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Market intelligence** | `aicoin-market` and `aicoin-onchain` feed crypto-sector research briefs |
| **Bot prototyping** | `aicoin-freqtrade` is a ready-made reference for agent-driven trading bots |
| **Client automation** | Trading-adjacent clients can get an AiCoin-powered data pipeline |

## Limitations / Verification

- Requires an AiCoin API key for most tools
- Trading skills execute real orders - add confirmation gates before any live use
- Verify: `npx skills add aicoincom/coinos-skills --list` shows 7 skills

## Security

No skills.sh security audits published (verified Sep 27, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Hithink Finance Setup](/hermes/skills/catalog/hithink-finance-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
