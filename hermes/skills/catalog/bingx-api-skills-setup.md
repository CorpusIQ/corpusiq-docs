---
title: "BingX API Skills - Crypto Exchange Trading Setup"
description: "bingx-api/api-ai-skills: a 29-skill BingX exchange API library for market data, trading and account management - 4.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bingx-api-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "crypto", "trading", "exchange api"]
---

# BingX API Skills - Crypto Exchange Trading Setup

**Source:** [bingx-api/api-ai-skills](https://www.skills.sh/bingx-api/api-ai-skills) via skills.sh - 4.4K combined installs across 29 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [bingx-api/api-ai-skills](https://github.com/bingx-api/api-ai-skills) - 19 stars, no LICENSE file, main branch, last pushed Nov 16, 2026; one directory per skill under `skills/<name>/` pairing a `SKILL.md` with an `api-reference.md`, plus shared reference docs under `skills/references/`.
**Category:** Crypto Trading and Exchange APIs
**Quality Tier:** 🟠 Orange - 3 of the 20 sampled skills carry Snyk Fail cells, with 11 Snyk Warn cells and 6 all-Pass samples.

BingX publishes this skills package for AI coding assistants that drive its exchange API without hand-written request code. Each skill bundles a `SKILL.md` (agent behavior instructions) with an `api-reference.md` (the endpoint documentation), and shared references cover HMAC SHA256 signing, base URLs, error codes, execution safety and rate limits. The set splits into market data, spot and USDT-M perpetual trading, coin-margined contracts, copy trading, account management, WebSocket streams and trading analysis.

The index lists 29 skills, but the install names carry a `bingx-` prefix that the repo tree drops (`swap-trade` in the tree is `bingx-swap-trade` in the index), and the four coinm (coin-margined) listings have no matching directory in the current tree. The market-data skills are the safe first step: several need no API key at all. First seen in the Nov 21, 2026 morning sweep.

## Installation

Method 1 (AI conversation, works with OpenClaw, Cursor, Claude Code and other assistants): tell your agent "Set up the skills https://github.com/BingX-API/api-ai-skills" and it completes the install without further commands.

Method 2 (Claude Code plugin):

```bash
/plugin marketplace add BingX-API/api-ai-skills
/plugin install bingx-ai-skills
```

Method 3 (npx, for Cursor, Windsurf and other skills-protocol assistants):

```bash
npx skills add BingX-API/api-ai-skills
```

Market-data skills (`swap-market`, `spot-market`, `coinm-market`, `announcement`) need no authentication. Trading and account skills read `BINGX_API_KEY` and `BINGX_SECRET_KEY`, created at the BingX User Center API Management page. Two environments exist: `prod-live` (real funds) and `prod-vst` (simulated testnet). In `prod-live`, every write operation asks you to type CONFIRM before it runs.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| bingx-swap-trade | 214 | perpetual futures trading: place and cancel orders, set leverage and margin mode |
| bingx-swap-market | 214 | perpetual futures market data: price, depth, klines, funding rate and open interest |
| bingx-swap-account | 207 | perpetual account data: balance, positions, commission rate and fund flow |
| bingx-agent | 197 | broker and agent operations: invited users, commission queries and partner data |
| bingx-spot-market | 188 | spot market data: price, depth, klines and recent trades |
| bingx-fund-account | 187 | fund account management: balance, asset overview and inter-account transfers |
| bingx-coinm-market | 185 | coin-margined futures market data: price, depth, klines and funding rate |
| bingx-spot-trade | 184 | spot trading: place and cancel orders, order queries and OCO orders |
| bingx-spot-account | 184 | spot account data: balance, asset overview and asset transfers |
| bingx-coinm-trade | 183 | coin-margined futures trading: place and cancel orders, leverage and margin mode |
| bingx-standard-trade | 182 | standard contract: position query, order history and balance query |

The remaining 18 indexed listings range from 43 to 179 installs.

## Why This Matters for Hermes Agents

This package turns a signed REST API into natural-language skills, so an agent can pull market data and manage accounts without hand-writing HMAC SHA256 signing. The read-only market-data skills need no key, which makes them a safe first integration before any credential is issued. The write skills gate on a typed CONFIRM in `prod-live`, so order placement keeps a human in the loop rather than executing silently. Keys are masked in output (the API key shows first 5 plus last 4 characters, the secret only its last 5), which reduces the chance of a key leaking into logs.

The reference layer is shared, so every skill follows one signing path and one error-code vocabulary instead of eleven improvised ones. For operators, the trading-analysis skills close the loop: technical analysis scores 78 indicators across timeframes, trade review turns raw fills into win rate and drawdown, and the sentiment dashboard overlays Fear and Greed with funding-rate and open-interest anomalies. The `prod-vst` testnet exists specifically so an agent can exercise the write path against simulated funds before anyone touches a live account.

## Usage

| You say | What happens |
|---|---|
| Query ETH-USDT perpetual klines for the last 4 hours at 15-minute intervals | bingx-swap-market fetches the klines; no authentication needed |
| Place a BTC-USDT market buy, go long 0.01 BTC | bingx-swap-trade builds a signed request and asks for CONFIRM before submitting in prod-live |
| Market buy 50 USDT worth of BTC on spot | bingx-spot-trade places the order using the quoteOrderQty parameter |
| What are my spot balances and recent transfers | bingx-spot-account returns balance, asset overview and transfer records |
| Show the latest BingX announcements and maintenance notices | bingx-announcement lists announcements, promotions and listing or delisting changes |
| Run technical analysis on BTC with RSI and support/resistance levels | bingx-technical-analysis scores multiple timeframes across 78 indicators |
| Review my last 20 trades for win rate and drawdown | bingx-trade-review summarizes performance with charts and custom tags |

## Verification

Confirm the skill files landed in your agent's skills directory, then review one skill's instructions before adding API keys:

```bash
ls skills 2>/dev/null || ls ~/.claude/skills 2>/dev/null
```

```bash
curl -sL https://raw.githubusercontent.com/bingx-api/api-ai-skills/main/skills/swap-trade/SKILL.md | head -40
```

Check that `BINGX_API_KEY` and `BINGX_SECRET_KEY` are set only if you need the trading or account skills, and start on the `prod-vst` testnet environment before any `prod-live` order.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bingx-swap-trade | Pass | Pass | Fail |
| bingx-swap-market | Pass | Pass | Pass |
| bingx-swap-account | Pass | Pass | Pass |
| bingx-agent | Pass | Pass | Fail |
| bingx-spot-market | Pass | Pass | Pass |
| bingx-fund-account | Pass | Pass | Warn |
| bingx-coinm-market | Pass | Pass | Pass |
| bingx-spot-trade | Pass | Pass | Warn |
| bingx-spot-account | Pass | Pass | Warn |
| bingx-coinm-trade | Pass | Pass | Warn |
| bingx-standard-trade | Pass | Pass | Pass |
| bingx-sub-account | Pass | Pass | Warn |
| bingx-copytrade-swap | Pass | Pass | Warn |
| bingx-spot-wallet | Pass | Pass | Warn |
| bingx-copytrade-spot | Pass | Pass | Warn |
| bingx-announcement | Pass | Pass | Warn |
| bingx-swap-ws-market | Pass | Pass | Pass |
| bingx-swap-ws-account | Pass | Pass | Fail |
| bingx-coinm-ws-market | Pass | Pass | Warn |
| bingx-spot-ws-market | Pass | Pass | Warn |

The trading and account skills sign real requests with your API keys and can place orders and move funds. Scope the keys to the account you intend to use, start with the no-key market-data skills, and prefer the `prod-vst` testnet for anything that writes.

## Limitations

- Snapshot data, verified Nov 21, 2026: 4,429 combined installs across 29 indexed listings; 19 GitHub stars; no LICENSE file; last pushed Nov 16, 2026. Counts drift over time.
- The install index outruns the tree: the four coinm listings (bingx-coinm-market, bingx-coinm-trade, bingx-coinm-ws-market, bingx-coinm-ws-account) carry install counts but have no matching directory in the current tree.
- Install names carry a `bingx-` prefix that the repo tree drops, and four unindexed `cswap-*` directories (cswap-market, cswap-trade, cswap-ws-account, cswap-ws-market) exist in the tree with no skills.sh listing.
- Live trading and account skills hold `BINGX_API_KEY` and `BINGX_SECRET_KEY` and can place orders and move funds; the `prod-live` environment asks for CONFIRM before each write.
- Three of the 20 sampled skills carry Snyk Fail cells; read each skill's instructions before granting write access to a funded account.
- There is no LICENSE file, so treat the repository's reuse terms as unstated rather than permissive.

## Related

- [OKX CEX Agent Skills - Exchange Trading Suite Setup](/hermes/skills/catalog/okx-cex-agent-skills-setup)
- [Binance Skills Hub - Crypto Trading Skills Setup](/hermes/skills/catalog/binance-skills-hub-setup)
- [Coinos Skills - AiCoin Crypto Trading Suite Setup](/hermes/skills/catalog/coinos-trading-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start on the `prod-vst` testnet and the four no-key market-data skills, so your first requests touch simulated funds and no credential.
- Scope the API key to the account you intend, and rely on the skill's own key masking rather than pasting keys into prompts.
- Read each write skill's interaction rules before running it; the confirmation flow differs between `prod-live` and `prod-vst`.
- Use the WebSocket skills (swap-ws-market, spot-ws-market) for streaming prices instead of polling the REST market skills.
- Pair trading with the analysis skills: run trade-review after a session to get win rate and drawdown rather than trading on raw fills alone.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
