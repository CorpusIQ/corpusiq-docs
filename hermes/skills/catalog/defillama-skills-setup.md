---
title: "DefiLlama Skills - DeFi Analytics Setup"
description: "DefiLlama/defillama-skills: agent skills for the DefiLlama MCP server, 23 DeFi analytics tools with guided workflows - 4.5K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/defillama-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "defi", "defillama", "onchain analytics"]
---

# DefiLlama Skills - DeFi Analytics Setup

**Source:** [defillama/defillama-skills](https://www.skills.sh/defillama/defillama-skills) via skills.sh - 4.5K combined installs across 11 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [DefiLlama/defillama-skills](https://github.com/DefiLlama/defillama-skills) - 38 stars, no LICENSE file, master branch, last pushed Mar 26, 2026 (eight months stale); eleven skill directories under `<name>/SKILL.md` plus a README.md at the root.
**Category:** DeFi Analytics and Onchain Data
**Quality Tier:** 🟡 Yellow - 38 stars but no LICENSE file and an eight-month-stale push; the 11 sampled skills carry no Fail cells, with a Gen Agent Trust Hub Warn on defillama-setup and a Snyk Warn on yield-strategies.

DefiLlama is the reference open DeFi analytics platform, and this repository packages agent skills for its hosted MCP server, which exposes 23 tools for TVL, token prices, yields, protocol metrics, stablecoins, bridges, ETFs, hacks, raises, treasuries and more. The suite is organized around guided workflows: a setup skill that installs and configures the MCP server, a core defi-data reference that maps any DeFi question to the right tool call, and nine analysis skills covering yields, protocol deep dives, chain ecosystems, capital flows, market screening, token research, institutional exposure and risk.

Every skill reads public DeFi data through the MCP server and none of them move funds, sign transactions or write to the blockchain. The repository is eight months stale (last pushed Mar 26, 2026) and carries no LICENSE file at the root, so redistribution terms are unclear even though the skills themselves are public.

## Installation

The README's quick start is a paste-in prompt that reads the defillama-setup SKILL.md, which walks through the OAuth login and subscription requirement:

```
Read https://raw.githubusercontent.com/DefiLlama/defillama-skills/master/defillama-setup/SKILL.md and follow the instructions to install DefiLlama MCP.
```

Manual setup is three steps. First, add the MCP server at `https://mcp.defillama.com/mcp` to your agent. Claude Code:

```bash
claude mcp add defillama --transport http https://mcp.defillama.com/mcp
```

Codex:

```bash
codex mcp add defillama --url https://mcp.defillama.com/mcp
```

The README also lists JSON configs for Claude Desktop, Cursor, Windsurf, Gemini CLI, OpenCode and OpenClaw (which bridges stdio-only agents via `mcp-remote`).

Second, log in. The server requires an active DefiLlama API subscription (https://defillama.com/subscribe) and uses OAuth rather than API keys or env vars, so you sign in once and you are done.

Third, install the skills:

```bash
npx skills add DefiLlama/defillama-skills --yes
```

This installs the skills only; the MCP server and its login are configured separately in the first two steps.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| yield-strategies | 455 | query DeFi yield and APY via get_yield_pools, with pool filtering, APY conventions and lending vs borrowing rates |
| institutional-crypto | 413 | institutional and TradFi exposure: public company holdings, ETF flows and accumulation patterns |
| defi-market-overview | 406 | broad DeFi market snapshot combining category rankings, chain comparison, total TVL and events |
| defi-data | 404 | core reference mapping DeFi questions to the right MCP tool call and parameters |
| risk-assessment | 403 | protocol and DeFi risk: hacks, oracles, treasury health, TVL concentration, yield sustainability |
| market-analysis | 403 | screening and comparison via valuation ratios, growth trends and cross-entity analysis |
| token-research | 401 | full token analysis: price, market cap, unlocks, DeFi deposits and yield opportunities |
| protocol-deep-dive | 401 | single-protocol report combining TVL, fees, revenue, yields, events and user activity |
| flows-and-events | 398 | capital flows and events: bridges, ETF flows, stablecoins, hacks, raises, open interest |
| chain-ecosystem | 397 | blockchain ecosystem overview: TVL, protocols, bridges, stablecoins, DEX volume, users |
| defillama-setup | 395 | install and configure the DefiLlama MCP server with OAuth login |

All 11 indexed listings clear the 300-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

DefiLlama's MCP server is the fastest way to give a Hermes agent authoritative DeFi numbers without hardcoding API endpoints. The defi-data reference is the most valuable piece: it encodes the entity conventions, metric interpretations, stock-vs-flow distinctions and error recovery rules, so the agent resolves a fuzzy name like ETH to the right entity before querying instead of guessing slugs. The nine analysis skills are pre-built workflows that chain many tools into one report, so an ask like "tell me everything about this protocol" produces a complete answer rather than a raw tool dump. Because every skill reads through one authenticated MCP server, the agent gets a consistent schema across TVL, fees, yields, stablecoins and flows. The caveats are practical: the server needs an active paid subscription and OAuth login, and the skills only read public data, so they inform decisions but never execute trades or move funds.

## Usage

| You say | What happens |
|---|---|
| What's happening in DeFi this week? | defi-market-overview combines category rankings, chain comparison, total TVL trends and market events into a high-level snapshot |
| Is this protocol safe? | risk-assessment evaluates hack history, oracle dependencies, treasury health, TVL concentration and yield sustainability |
| Tell me everything about Uniswap | protocol-deep-dive combines TVL, fees, revenue, yields, events, income and user activity into a full protocol report |
| Where can I earn yield on USDC? | yield-strategies queries get_yield_pools with filtering by token, chain, protocol and category, including stablecoin-only mode |
| What are institutions buying? | institutional-crypto pulls public company holdings, Bitcoin and Ethereum ETF flows and accumulation patterns |
| Analyze this token | token-research combines price, market cap, unlock schedule, DeFi deposits and yield opportunities |
| What's happening on Solana? | chain-ecosystem covers TVL, top protocols, bridge flows, stablecoin supply, DEX volume, fees and user activity |

## Verification

Confirm the setup skill landed and read its install routing before wiring the server:

```bash
curl -sL https://raw.githubusercontent.com/DefiLlama/defillama-skills/master/defillama-setup/SKILL.md | head -60
```

Review the core reference that maps DeFi questions to tool calls:

```bash
curl -sL https://raw.githubusercontent.com/DefiLlama/defillama-skills/master/defi-data/SKILL.md | head -60
```

Inspect the yield workflow before hunting for APY:

```bash
curl -sL https://raw.githubusercontent.com/DefiLlama/defillama-skills/master/yield-strategies/SKILL.md | head -60
```

All three paths live on the master branch and return 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| yield-strategies | Pass | Pass | Warn |
| institutional-crypto | Pass | Pass | Pass |
| defi-market-overview | Pass | Pass | Pass |
| defi-data | Pass | Pass | Pass |
| risk-assessment | Pass | Pass | Pass |
| market-analysis | Pass | Pass | Pass |
| token-research | Pass | Pass | Pass |
| protocol-deep-dive | Pass | Pass | Pass |
| flows-and-events | Pass | Pass | Pass |
| chain-ecosystem | Pass | Pass | Pass |
| defillama-setup | Warn | Pass | Pass |

The suite reads public DeFi data and does not move funds, sign transactions or write to the blockchain. The MCP server uses OAuth rather than API keys. Note the repository carries no LICENSE file, so redistribution terms are unclear.

## Limitations

- Snapshot data, verified Nov 22, 2026: 4.5K combined installs across 11 indexed listings; 38 GitHub stars; no LICENSE file; last pushed Mar 26, 2026. Counts drift over time.
- There is no LICENSE file at the repository root, so redistribution and modification rights are unclear despite the skills being public.
- The repository is eight months stale (last pushed Mar 26, 2026), so tool names and parameters may lag the live DefiLlama MCP server.
- The MCP server requires an active DefiLlama API subscription, so the skills are not usable without a paid account.
- The skills read public DeFi data and do not move funds; they cannot place orders, transfer assets or sign transactions.
- The default branch is master; every raw SKILL.md URL above uses master, so do not rewrite the branch to main when re-probing.

## Related

- [Chainlink Agent Skills Setup Guide](/hermes/skills/catalog/chainlink-agent-skills-setup)
- [AGI Pro Trading Skills - 68 Quant and DeFi Skills](/hermes/skills/catalog/agiprolabs-trading-skills-setup)
- [OKX OnchainOS Skills - Wallet & DEX Setup](/hermes/skills/catalog/okx-onchainos-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Paste the README's quick-install prompt once and let the setup skill drive the OAuth login and subscription check end to end.
- Log in once through the agent's MCP screen; no API keys or env vars are needed, but an active DefiLlama subscription is.
- Route ambiguous questions through defi-data first so the agent resolves entity names and metric interpretations before calling tools.
- Use the stablecoin-only and category filters in yield-strategies before listing every pool, to keep responses scoped.
- Because the repository has no LICENSE file and is eight months stale, read each SKILL.md and re-check the security pages on skills.sh before production use.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
