---
title: "Uniswap AI - DeFi Integration Skills Setup"
description: "uniswap/uniswap-ai on skills.sh: 15.3K combined installs across 19 listings; swap, liquidity, v4 hook and trading bot skills for Uniswap work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/uniswap-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "defi", "web3", "uniswap"]
---

# Uniswap AI - Setup Guide

**Source:** [uniswap/uniswap-ai](https://www.skills.sh/uniswap/uniswap-ai) via skills.sh - 15.3K combined installs across 19 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 236 stars, MIT, last pushed 2026-11-04, 18 SKILL.md files laid out as `packages/plugins/<plugin>/skills/<skill>/SKILL.md` across seven plugins, with a `docs/skills/` page per skill
**Category:** DeFi development: swap integration, liquidity provisioning, v4 hooks, CCA auctions, permissioned pools and automated trading bots
**Quality Tier:** 🟡 Yellow - MIT with a LICENSE file, but all three sampled skills carry a Snyk Warn and every skill in the set touches contract calls or funds.

Uniswap AI is the official Uniswap repository for agent tooling: skills, plugins and agents for developers building on the protocol. It is a product repository rather than a community skill collection, and the layout shows it. Seven plugins, each with a README and a `skills/` directory, shipped through the Claude Code marketplace and also installable as plain skills.

The 19 listings map onto those plugins. `uniswap-trading` holds the integration skills (`swap-integration`, `pay-with-any-token`, `pay-with-app`, `lp-integration`, `v4-sdk-integration`). `uniswap-driver` holds the two that generate deep links into the Uniswap interface. `uniswap-hooks` covers v4 hook generation and security. `uniswap-cca` configures and deploys Continuous Clearing Auctions. `uniswap-trading-tools` holds the three bots. `uniswap-viem` is general EVM plumbing with viem and wagmi. `uniswap-permissioned-pools` is the reference, configurator and deployer trio for transfer-restricted RWA tokens.

There is a documented split worth understanding before installing. The skills come in two flavours: ones that generate deep links so a human executes the trade in the Uniswap web app (`swap-planner`, `liquidity-planner`), and ones that build actual integrations against the Trading API, the v4 SDK or the LP REST API (`swap-integration`, `v4-sdk-integration`, `lp-integration`). The first is safe to try immediately; the second writes code that moves funds.

## Installation

The README gives three routes. The skills CLI works with any agent:

```bash
npx skills add Uniswap/uniswap-ai
```

The Claude Code marketplace carries all seven plugins:

```text
/plugin marketplace add uniswap/uniswap-ai
```

Individual plugins install by name, and the README comments what each one covers:

```text
/plugin install uniswap-hooks               # v4 hook development
/plugin install uniswap-trading             # swap integration
/plugin install uniswap-cca                 # CCA auctions
/plugin install uniswap-driver              # swap and liquidity planning
/plugin install uniswap-viem                # EVM integration (viem/wagmi)
/plugin install uniswap-trading-tools       # automated trading tools
/plugin install uniswap-permissioned-pools  # v4 permissioned pools
```

For a Hermes agent, the skills CLI route is the one to use, because each skill is a self-contained directory with a `SKILL.md` and, in most cases, a `references` folder of its own. Copying or linking `packages/plugins/<plugin>/skills/<skill>` into the agent skills directory gives the same result without the marketplace. There is no build step for the skills themselves; the `bun install` and `nx` commands in `docs/getting-started/installation.md` are for contributing to the repository.

Some skills need an external service on the machine before they work. `pay-with-any-token` drives the Tempo CLI for HTTP 402 payments, `pay-with-app` targets OKX's Agent Payments Protocol on X Layer, and `v4-hook-generator` generates contracts through the OpenZeppelin MCP server. Install those separately and confirm the dependency before you expect the skill to complete.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| swap-integration | 2,270 | Integrating swaps through the Trading API, Universal Router or the SDKs, including a swap frontend or a script |
| viem-integration | 1,702 | Reading chain data, sending transactions and connecting wallets with viem and wagmi in TypeScript |
| liquidity-planner | 1,240 | Planning an LP position with a price range and generating a deep link to create it in the Uniswap interface |
| swap-planner | 1,218 | Planning a swap or discovering tokens by keyword and web search, then generating a deep link to execute |
| v4-security-foundations | 1,197 | Security-first v4 hook development, covering PoolManager, beforeSwap and afterSwap, and known vulnerability classes |
| deployer | 1,136 | Deploying Continuous Clearing Auction contracts through the factory pattern |
| configurator | 1,127 | Configuring CCA parameters through an interactive bulk form flow before deployment |
| pay-with-any-token | 841 | Paying HTTP 402 challenges with tokens through the Tempo CLI and the Uniswap Trading API |
| v4-sdk-integration | 755 | Building swap and liquidity experiences with the v4 SDK: V4Planner, StateView, PositionManager and pool state |
| v4-hook-generator | 712 | Generating v4 hook contracts through OpenZeppelin MCP for custom curves, dynamic fees, MEV protection or limit orders |
| pay-with-app | 548 | Paying OKX Agent Payments Protocol challenges on X Layer with tokens from any chain |
| lp-integration | 467 | Managing v2, v3 and v4 LP positions through the LP REST API, including approvals, permits and fee claims |
| copy-trade | 431 | Mirroring a target wallet's swaps, filtered by chain, asset and position size within guardrails |
| index-bot | 428 | Building and rebalancing a weighted basket of assets that buys in one pass and rebalances on a cadence |
| dca-bot | 423 | Buying a fixed amount of a token on a schedule, optionally only when a price condition holds |
| permissioned-pools-issuer | 265 | Reference material for listing a transfer-restricted RWA token in a v4 permissioned pool |
| permissioned-pools-configurator | 265 | Collecting and validating permissioned pool parameters and emitting the JSON the deployer consumes |
| permissioned-pools-deployer | 263 | Executing the on-chain permissioned pool setup sequence, including allowlist, adapter, wrappers and pool initialisation |
| aggregator-hook-creator | 8 | Listed on skills.sh with no matching directory in the current tree |

No indexed listings fall below the threshold; all 19 appear above.

The install distribution is steep at the top and flat in the middle. `swap-integration` and `viem-integration` lead at 2,270 and 1,702, which fits a repository whose audience arrives to build a swap rather than to configure an auction. The three permissioned pool skills sit at 263 to 265 installs each, which is what a three-step workflow looks like when people install all three together.

## Why This Matters for Hermes Agents

Protocol documentation is the weakest input an agent can get. It is written for humans scanning for an entry point, and it obsoletes quietly. This set replaces it with per-task instructions attached to the current repository, including the parts that bite: approval and EIP-712 permit flows for LP positions, the ordered setup journey for permissioned pools, and the vulnerability classes in v4 hooks.

The two-tier design is the responsible pattern and worth copying. Skills that only plan and generate a deep link cannot lose funds, so an agent can use them freely. Skills that broadcast transactions are separate and explicitly named. An agent asked to "add a swap button" lands in `swap-integration`, while "swap 1 ETH for USDC" lands in `swap-planner` and ends in the browser where a human confirms.

The permissioned pools trio is a good example of encoding a procedure rather than a fact. The configurator validates parameters and emits JSON, the deployer consumes it and walks the on-chain sequence in a fixed order, and the issuer skill explains why the order is enforced and what the trust model is. That is a compliance-adjacent workflow where step order matters and prose documentation is easy to misread.

For a Hermes agent working on anything in DeFi, the practical gain is that the risky parts are already labelled. The agent does not have to infer which skill can move money.

## Usage

| You say | What happens |
|---|---|
| "Add swap functionality to my app" | `swap-integration` picks between the Trading API, Universal Router and the SDKs, then builds the integration with the right approval flow |
| "I want to provide liquidity to an ETH/USDC pool" | `liquidity-planner` proposes a range and returns a deep link, with `lp-integration` available if you need it in code |
| "Write a v4 hook that charges a dynamic fee" | `v4-hook-generator` produces the contract through OpenZeppelin MCP, and `v4-security-foundations` reviews the risky surfaces |
| "This API returned 402 Payment Required" | `pay-with-any-token` fulfils the challenge with tokens, or `pay-with-app` when the network resolves to X Layer |
| "Set up a DCA bot for ETH" | `dca-bot` builds a scheduled fixed-amount buy, optionally gated on a price condition |
| "Launch a token auction" | `configurator` collects the CCA parameters, then `deployer` deploys through the factory |
| "We need to list a restricted RWA token" | `permissioned-pools-issuer` explains the architecture, then the configurator and deployer walk the ordered setup |

## Verification

Read the main integration skill before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/uniswap/uniswap-ai/main/packages/plugins/uniswap-trading/skills/swap-integration/SKILL.md | head -20
```

It should open with a description about integrating Uniswap swaps through the Trading API, Universal Router or the SDKs. Every skill follows the same `packages/plugins/<plugin>/skills/<skill>/SKILL.md` layout, so the same path shape works for any row in the table.

After install, confirm what landed. The tree holds 18 skills across seven plugins:

```bash
ls .agents/skills | wc -l
```

If the count is not 18, something in your skills directory did not come from this repository. The repository also ships a documentation page per skill under `docs/skills/`, which is the fastest way to check whether a skill changed shape between releases.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| swap-integration | Pass | Pass | Warn |
| viem-integration | Pass | Pass | Warn |
| liquidity-planner | Pass | Pass | Warn |

The universal Warn across the sample is the right signal for this set. These skills write code that signs and broadcasts transactions, and several of them hold or reference private keys, RPC endpoints and API credentials. Nothing here should run against mainnet on the first attempt.

Test on a testnet or a fork first, with a throwaway key. Read any generated contract before deploying it, especially from `v4-hook-generator`, where the hook is the security boundary. Keep RPC and signing credentials in the environment or a signer service, never in the repository, and prefer a hardware or managed signer over a raw private key in an env file for anything holding real value.

The repository ships a `DISCLAIMER.md` covering intended use and financial information disclaimers, and the permissioned pool skills state plainly that they cover contract mechanics only and are not legal, financial, tax or compliance advice. Treat that literally: the deployer skill never emits a broadcastable command before an explicit acknowledgment, and that acknowledgment is a real decision rather than a formality.

## Limitations

- Snapshot data, verified 2026-11-07: 15,296 combined installs across 19 indexed listings; 236 GitHub stars; MIT; last pushed 2026-11-04. Counts drift over time.
- One listing has no directory. `aggregator-hook-creator` shows 8 installs on skills.sh while the tree holds 18 SKILL.md files across seven plugins, so there is nothing to install for that row today.
- The skills assume current protocol and API shapes. `swap-integration` targets the Trading API and Universal Router, `lp-integration` targets the LP REST API, and both move faster than the skills may.
- Several skills have external prerequisites. `pay-with-any-token` needs the Tempo CLI, `pay-with-app` targets X Layer through OKX's protocol, and `v4-hook-generator` needs the OpenZeppelin MCP server.
- This is a young repository by star count relative to its install volume, so the skill set is not yet battle-tested by a wide audience outside Uniswap's own teams.
- Nothing here is a strategy. The bots (`dca-bot`, `index-bot`, `copy-trade`) implement mechanics and guardrails, not advice about what to buy.

## Related

- [Coinbase Agentic Wallet - USDC Payments Skill](/hermes/skills/catalog/coinbase-agentic-wallet-setup)
- [Binance Skills Hub - Crypto Trading Skills Setup](/hermes/skills/catalog/binance-skills-hub-setup)
- [Polymarket - Prediction Market Integration Setup](/hermes/skills/catalog/polymarket-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `swap-planner` and `liquidity-planner`. They return deep links rather than transactions, so you can see how the skills reason before you let anything sign.
- Install `viem-integration` alongside whichever plugin you actually need. Almost every other skill assumes a configured viem client and a wallet.
- Read `v4-security-foundations` before `v4-hook-generator`, not after. The security skill names the failure classes the generator can produce.
- Run the permissioned pools trio in order and keep the configurator's JSON. The deployer depends on that exact document, and regenerating it mid-flight is how the ordering breaks.
- Keep a separate repository scope per network. A skill that works on a testnet fork will happily accept a mainnet RPC URL and a funded key if the environment supplies them.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
