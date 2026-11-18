---
title: "Teneo Skills - Onchain Agent Network Setup"
description: "teneoprotocolai/teneo-skills: 11.1K combined installs across 27 listings; query a decentralized network of AI agents for swaps and crypto analytics."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/teneo-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "onchain", "ai agents", "crypto", "social data"]
---

# Teneo Skills - Setup Guide

**Source:** [teneoprotocolai/teneo-skills](https://www.skills.sh/teneoprotocolai/teneo-skills) via skills.sh - 11.1K combined installs across 27 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 35 stars, no LICENSE file, `main` branch, last pushed 2026-04-15, one CLI skill plus a `skills/agents/` directory of auto-generated agent skills
**Category:** Onchain agent network / crypto data, social scraping and product search
**Quality Tier:** 🟡 Yellow - 43 Pass and 17 Warn across the 20 sampled listings; no Fail, and the repository ships no LICENSE file.

Teneo Skills connects a coding agent to a decentralized network of AI agents that perform real tasks: token swaps, social media scraping, crypto analytics and product search. The suite ships one CLI skill, teneo-cli, plus a directory of auto-generated skills, one per network agent, each documenting that agent's commands and pricing. A wallet is generated on first use and funded with USDC to pay agents, and transactions are auto-signed through the same CLI.

The listing names carry a `-teneo` suffix that is part of the skill name on skills.sh (instagram-agent-teneo, youtube-teneo and so on), so the exact name matters when installing or referencing one.

## Installation

Claude Code plugin install:

```bash
npx skills add teneoprotocolai/teneo-skills
```

Standalone CLI install, which needs Node.js 18+:

```bash
sh install.sh
```

The install script copies source files, installs npm dependencies and creates a wrapper at `~/teneo-skill/teneo`. A wallet is auto-generated on first use; fund it with USDC to query paid agents or deploy your own. Then discover agents:

```bash
~/teneo-skill/teneo --version
~/teneo-skill/teneo list-agents
~/teneo-skill/teneo list-agents --search "swap"
~/teneo-skill/teneo info <agentId>
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| instagram-agent-teneo | 575 | Extract Instagram posts, profiles, hashtags and comments through the Teneo network. |
| teneo-cli | 548 | Discover and query agents, manage rooms and wallets, deploy agents, and settle x402 USDC payments. |
| x-platform-agent-teneo | 543 | Query the X platform agent for social data via the bundled Teneo CLI. |
| amazon-teneo | 543 | Turn Amazon product searches into structured data. |
| teneo-agents | 539 | Find which network agent handles swaps, social scraping, crypto data or product search. |
| messari-btc-eth-tracker-teneo | 537 | Pull BTC and ETH data from Messari market data sources. |
| coinmarketcap-agent-teneo | 537 | Read real-time and historical crypto market data through CoinMarketCap. |
| gas-war-sniper-teneo | 534 | Multi-chain gas monitoring and spike detection. |
| tiktok-teneo | 533 | Extract TikTok video metrics, creator profiles and hashtag velocity. |
| linkedin-teneo | 525 | Enrich a LinkedIn profile URL into structured JSON. |
| squid-router-teneo | 523 | Cross-chain token swaps through the Squid Router agent. |
| cryptoquant-pro-2-10-teneo | 522 | Query the CryptoQuant Pro 2.10 agent for crypto market data. |
| google-search-agent-teneo | 521 | Web search through the Google Search agent. |
| youtube-teneo | 520 | Query the YouTube agent for video data. |

The remaining 13 indexed listings range from 1 to 517 installs.

## Why This Matters for Hermes Agents

Teneo puts a network of third-party agents behind one CLI, so a Hermes agent can reach token swaps, social scraping and crypto data without a separate integration for each. teneo-cli is the hub: 39 commands covering agent discovery, rooms, wallets, agent deployment and a background daemon over WebSocket. Because a wallet is generated on first use and transactions are auto-signed, the useful habit is to fund it with exactly what a task costs in USDC and treat any loop as a spending risk. The auto-generated agent skills are thin frontmatter that point back at the CLI for live commands and pricing, so they are navigation aids rather than self-contained documentation. Read the live SKILL.md for an agent before trusting a cached copy, because the network changes under you.

## Usage

| You say | What happens |
|---|---|
| "Which agents can swap tokens?" | Runs `~/teneo-skill/teneo list-agents --search "swap"` and lists matching agents with pricing. |
| "What is gas costing across chains?" | Runs `teneo command "gas-sniper-agent" "gas"` and returns slow, normal, fast and base prices. |
| "Enrich this LinkedIn profile" | Runs `teneo command "linkedin-agent" "enrich_url <url>"` and returns structured profile data. |
| "Bridge 100 USDC to another chain" | Runs `teneo command "layerzero" "bridge <amount> <token> <fromChain> <toChain>"`, auto-signing the transaction. |
| "Deploy my own agent" | Walks the CLI agent workflow: `agent create`, `agent deploy`, `agent publish`. |

## Verification

Probe the CLI skill and one agent skill on the `main` branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/TeneoProtocolAI/teneo-skills/main/skills/teneo-cli/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/TeneoProtocolAI/teneo-skills/main/skills/agents/teneo-agent-amazon/SKILL.md
```

The CLI skill lives at `skills/teneo-cli/SKILL.md`, and each auto-generated agent skill lives under `skills/agents/teneo-agent-<name>/SKILL.md`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| instagram-agent-teneo | Pass | Pass | Warn |
| teneo-cli | Warn | Pass | Warn |
| x-platform-agent-teneo | Pass | Pass | Pass |
| amazon-teneo | Pass | Warn | Warn |
| teneo-agents | Pass | Warn | Warn |
| messari-btc-eth-tracker-teneo | Pass | Pass | Pass |
| coinmarketcap-agent-teneo | Pass | Warn | Pass |
| gas-war-sniper-teneo | Pass | Pass | Pass |
| tiktok-teneo | Pass | Pass | Warn |
| linkedin-teneo | Pass | Warn | Warn |
| squid-router-teneo | Pass | Pass | Pass |
| cryptoquant-pro-2-10-teneo | Pass | Warn | Pass |
| google-search-agent-teneo | Pass | Pass | Pass |
| youtube-teneo | Pass | Warn | Pass |
| aave-v3-liquidation-watcher-teneo | Pass | Warn | Pass |
| uniswap-monitor-teneo | Pass | Pass | Pass |
| vc-attention-teneo | Pass | Pass | Pass |
| google-maps-teneo | Pass | Pass | Warn |
| layerzero-teneo | Pass | Warn | Warn |
| predexon-prediction-market-trading-1-5-teneo | Pass | Pass | Pass |

The sample covers 20 of 27 indexed listings: every auditor Pass plus 17 Warns, no Fail. The repository ships no LICENSE file, so there is no stated grant for reuse. Trading and payment skills (squid-router-teneo, gas-war-sniper-teneo and teneo-cli) auto-sign onchain transactions against the auto-generated wallet, and teneo-cli handles x402 USDC micropayments. The social agents (instagram-agent-teneo, tiktok-teneo, linkedin-teneo and x-platform-agent-teneo) pull data from platforms that restrict automated access, which can put an account or IP at risk under those platforms' terms. The README states wallet keys are encrypted at rest with AES-256-GCM and that credentials are never transmitted or stored; fund the wallet with only what a task costs.

## Limitations

- Snapshot data, verified 2026-11-17: 11,108 combined installs across 27 indexed listings; 35 GitHub stars; no LICENSE file; last pushed 2026-04-15. Counts drift over time.
- No LICENSE file ships in the repository, so there is no stated grant for reuse.
- Install counts cluster tightly between 520 and 575; a narrow spread across sibling agent skills is normal.
- The social-platform agents (Instagram, TikTok, LinkedIn, X) extract data from sites that restrict automated access, so querying them carries account or IP risk under those platforms' terms.
- Trading agents auto-sign onchain transactions against the auto-generated wallet; keep its balance small and pay only for what a task costs.
- Four tail listings duplicate aave-v3-liquidation-watcher with "powered-by-teneo-protocol" repeated in their names (2, 1, 1 and 1 installs), an indexing artifact on skills.sh.

## Related

- [Apify Awesome Skills - Lead and Market Intelligence](/hermes/skills/catalog/apify-awesome-skills-setup)
- [CCXT Skills - Unified Crypto Exchange API Setup](/hermes/skills/catalog/ccxt-setup)
- [Coinos Skills - AiCoin Crypto Trading Suite Setup](/hermes/skills/catalog/coinos-trading-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use teneo-cli for everything; the per-agent skills are navigation aids that point back at the CLI for live commands and pricing.
- Run `list-agents --search` before querying; the network changes, and a cached agent name may be stale.
- Start with a read (messari, coinmarketcap, google-search) to confirm the wallet and network before touching a swap or bridge.
- Fund the wallet with exactly what the task costs in USDC, and never commit `.env` or log credentials.
- For Claude Code the plugin wraps the same CLI; use the `sh install.sh` path in plain shell or CI.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
