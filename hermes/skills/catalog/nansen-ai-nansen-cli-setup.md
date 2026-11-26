---
title: "Nansen CLI - Onchain Data and Trading Skills Setup"
description: "nansen-ai/nansen-cli - 16.3K combined installs: a CLI and agent skills for on-chain research, wallet management, and trading via the Nansen API."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nansen-ai-nansen-cli-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "nansen", "onchain", "defi"]
---

# Nansen CLI - Setup Guide

**Source:** [nansen-ai/nansen-cli](https://www.skills.sh/nansen-ai/nansen-cli) via skills.sh - 16.3K combined installs across 74 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [nansen-ai/nansen-cli](https://github.com/nansen-ai/nansen-cli) - 151 stars, MIT license, last pushed Nov 26, 2026, main branch; 33 skill folders under skills/<name>/SKILL.md.
**Category:** Onchain Data and Trading (Nansen / DeFi Agents)
**Quality Tier:** 🟡 Yellow - 15 sampled skills: five pass all three checks and ten carry at least one Warning; no Fails.

nansen-ai/nansen-cli is a command-line interface for the Nansen API, built for AI agents to research on-chain data, manage wallets, and trade through `nansen trade`. The repository publishes no GitHub description; this guide is drawn from the README and the skills.sh listings. The CLI handles both analytics and execution: `nansen research` returns structured on-chain data, while `nansen trade quote` and `nansen trade execute` handle DEX swaps on Solana, Base, Ethereum, Arbitrum, Polygon, and Robinhood Chain, including cross-chain bridges, plus Hyperliquid perpetuals.

The skills.sh index lists 74 listings, but the current tree carries 33 skill folders under skills/<name>/SKILL.md; the other 41 indexed listings have no matching directory. One of the eight most-installed listings, nansen-web-fetcher, is among those without a current SKILL.md.

## Installation

```bash
npm install -g nansen-cli
npx -y skills add nansen-ai/nansen-cli --skill "*" -y  # install every agent skill, no prompts
```

Without `--skill "*" -y`, `skills add` opens a picker: space selects a skill, enter confirms. Authenticate with `nansen login` (browser approval and a saved session), or set `NANSEN_API_KEY` on a server, in a container, or in CI.

## What It Provides

skills.sh publishes per-skill install counts for all 74 indexed listings. The 8 most-installed skills are listed below; the remaining 66 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| nansen-web-searcher | 667 | Search the web for one or more queries in parallel to complement on-chain Nansen data |
| nansen-smart-money-tracker | 561 | Track smart money netflow, trades, holdings, and perp trades across chains |
| nansen-prediction-markets | 503 | Polymarket screeners: discover trending events, top markets by volume, and search specific markets |
| nansen-smart-money-alpha | 488 | Screen for tokens smart money is accumulating before they pump, cross-referenced against netflow |
| nansen-web-fetcher | 466 | Fetch web page content; no SKILL.md in the current tree, no published description |
| nansen-portfolio-tracker | 458 | Show how a wallet's portfolio changed over time: historical balances, snapshot, per-token PnL |
| nansen-token-research | 450 | Deep dive on a token: info, OHLCV, holders, flows, DEX trades, and perp PnL |
| nansen-trading | 445 | Execute DEX swaps and Hyperliquid perpetual trades across supported chains |

The remaining 66 indexed listings range from 2 to 439 installs.

## Why This Matters for Hermes Agents

For a Hermes agent doing on-chain work, Nansen CLI turns on-chain research and execution into structured commands instead of hand-built API calls. `nansen research` returns JSON across smart money, tokens, profilers, portfolios, prediction markets, search, and perps, while `nansen trade quote` and `nansen trade execute` handle swaps and perps, and the skills layer teaches the agent how to drive each category. The `nansen agent` command runs a research agent at 100 credits (400 with `--expert`), and wallet commands cover local and Privy wallets on EVM and Solana. The main caveats are the security Warnings on several skills, the 74-vs-33 index-to-tree drift, and the fact that trading, bridge, and wallet operations are real, irreversible, and paid per call.

## Usage

| You say | What happens |
|---|---|
| What is smart money buying right now? | Uses nansen-smart-money-tracker to pull netflow, trades, holdings, and perp trades |
| Research this token | Uses nansen-token-research for holders, flows, DEX trades, and perp PnL |
| What is hot on Polymarket? | Uses nansen-prediction-markets to find trending events and top markets by volume |
| What does this wallet hold? | Uses nansen-portfolio-tracker for historical balances and per-token PnL |
| Buy SOL with USDC | Uses nansen-trading for a quote, then executes the swap on Solana |
| Find the latest news on X | Uses nansen-web-searcher to run parallel web searches alongside on-chain data |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/nansen-ai/nansen-cli/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/nansen-ai/nansen-cli/main/skills/nansen-web-searcher/SKILL.md | head -40
```

Both URLs return 200. After installing, run `nansen doctor` for a full setup check and `npx -y nansen-cli mcp verify` to confirm the API key and MCP server before relying on paid tools.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nansen-web-searcher | Pass | Pass | Warn |
| nansen-smart-money-tracker | Pass | Pass | Warn |
| nansen-prediction-markets | Pass | Pass | Warn |
| nansen-smart-money-alpha | Pass | Pass | Pass |
| nansen-web-fetcher | Pass | Pass | Warn |
| nansen-portfolio-tracker | Pass | Pass | Warn |
| nansen-token-research | Pass | Pass | Pass |
| nansen-trading | Pass | Warn | Warn |
| nansen-fund-tracker | Pass | Pass | Warn |
| nansen-smart-money-trend | Pass | Pass | Pass |
| nansen-wallet-profiler | Pass | Pass | Warn |
| nansen-general-search | Pass | Warn | Warn |
| nansen-defi-positions | Pass | Pass | Pass |
| nansen-token-screener | Pass | Pass | Warn |
| nansen-polymarket-deep-dive | Pass | Pass | Pass |

Five of the 15 sampled skills pass all three checks; the other ten carry at least one Warning (twelve Warning cells across Socket and Snyk). No Fails.

## Limitations

- Snapshot data, verified Nov 25, 2026: 16,343 combined installs across 74 indexed listings; 151 GitHub stars; MIT license; last pushed Nov 26, 2026. Counts drift over time.
- The index outruns the tree: 74 indexed listings versus 33 skill folders in the current tree; 41 listings have no matching directory, including nansen-web-fetcher.
- Fifteen of the 74 listings were security-sampled; the other 59 have no published verdict on skills.sh.
- Trading, bridge, and wallet operations are real and irreversible once signed; use `--dry-run` to preview and `NANSEN_REQUIRE_CONFIRM=1` to force an agent to stop for approval.
- The repository publishes no GitHub description, so this guide's positioning comes from the README.
- The last-push timestamp is Nov 26, 2026 in UTC, one day ahead of the Nov 25, 2026 local sweep date.

## Related

[Bankr Skills - DeFi and Onchain Agent Toolkit](/hermes/skills/catalog/bankrbot-skills-setup) | [CCXT Skills - Unified Crypto Exchange API Setup](/hermes/skills/catalog/ccxt-setup) | [Uniswap AI - DeFi Integration Skills Setup](/hermes/skills/catalog/uniswap-ai-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use `--fields` to cut token burn: `nansen research smart-money netflow --chain solana --fields token_symbol,net_flow_usd --limit 10`.
- Use `--dry-run` on every trade, bridge, and perp command to preview without signing, and set `NANSEN_REQUIRE_CONFIRM=1` so agents stop for your go-ahead.
- Run `npx -y nansen-cli mcp verify` to confirm the API key and server before relying on paid tools.
- Use `--stream` for large results and `--paginate` to fetch every page of a list in one call.
- Run `nansen doctor` when anything misbehaves; it checks auth, wallets, caches, and connectivity with a fix per finding.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
