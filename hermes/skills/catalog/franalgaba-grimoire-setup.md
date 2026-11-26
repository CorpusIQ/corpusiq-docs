---
title: "Grimoire Skills - Financial Intent Language Setup"
description: "franalgaba/grimoire - 18.4K combined installs: a language for agents to express financial intent across DeFi venues with deterministic execution."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/franalgaba-grimoire-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "defi", "onchain", "finance"]
---

# Grimoire Skills - Setup Guide

**Source:** [franalgaba/grimoire](https://www.skills.sh/franalgaba/grimoire) via skills.sh - 18.4K combined installs across 11 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [franalgaba/grimoire](https://github.com/franalgaba/grimoire) - 6 stars, no license, last pushed May 8, 2026, main branch; 8 skill folders under skills/<name>/SKILL.md.
**Category:** Finance / DeFi (Agent Skills)
**Quality Tier:** 🟠 Orange - 11 of 11 listings sampled: grimoire-lifi carries a Gen Agent Trust Hub Fail and grimoire-yellow returns no verdict on any tool; the repository has no license.

franalgaba/grimoire is Grimoire, a language for agents to express financial intent with readable, brace-delimited syntax and deterministic execution. Spells compile to an intermediate representation (IR) and run through protocol adapters for Aave V3, Uniswap V3/V4, Morpho Blue, Across, Hyperliquid, Pendle, and Polymarket, so an agent can swap venues by changing aliases and configuration instead of rewriting strategy logic. The 11 indexed listings split into the install-and-author skill (grimoire) plus per-venue snapshot and order skills; grimoire-polymarket leads at 11,941 installs.

The runtime enforces one semantic rule across both entry points: preview first, then commit for irreversible actions. Eight of the 11 listings map to a skills/<name>/SKILL.md folder in the current tree; grimoire-vm, grimoire-yellow, and grimoire-lifi carry install counts but no counterpart directory, and the repository publishes no license.

## Installation

The README installs Grimoire through its own CLI rather than the skills CLI:

```bash
npm i -g @grimoirelabs/cli

grimoire setup
```

To install the agent skills so an agent can work with Grimoire immediately:

```bash
npx skills add https://github.com/franalgaba/grimoire
```

For Claude Code, run the same install command in the Claude Code terminal and start a new session to load the skills. The library entry point is @grimoirelabs/core for embedding Grimoire into an app or agent process.

## What It Provides

skills.sh publishes per-skill install counts for all 11 indexed listings. The 8 most-installed skills are listed below; the remaining 3 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| grimoire-polymarket | 11,941 | query Polymarket market data and CLOB state, and manage CLOB orders via the venue CLI wrapper backed by the official Polymarket CLI |
| grimoire-hyperliquid | 1,101 | query Hyperliquid market data: mids, books, metadata, open orders, or a withdrawal call |
| grimoire | 1,067 | install and operate Grimoire, author .spell files, and run compile/validate/simulate/cast safely |
| grimoire-uniswap | 1,064 | retrieve Uniswap router addresses, adapter info, and V3/V4 details |
| grimoire-aave | 1,064 | fetch Aave V3 public market data: health checks, chain listings, market metadata, or reserve info |
| grimoire-morpho-blue | 1,052 | fetch Morpho Blue public deployment metadata: contract addresses or adapter info |
| grimoire-pendle | 1,022 | fetch Pendle Hosted SDK metadata: supported chains, aggregators, markets, assets, or market token details |
| grimoire-across | 64 | fetch Across Protocol bridge quotes, route availability, or cross-chain deposit status |

The remaining 3 indexed listings range from 1 to 7 installs.

## Why This Matters for Hermes Agents

Financial strategies are exactly the kind of work where an agent improvising from raw protocol SDKs goes wrong in expensive ways, and Grimoire gives that work a typed, reviewable surface instead. A spell is a compiled structure with explicit constraints, limits, and a judgment boundary (the advise block), so an agent can express what it intends to do and preview the result before anything irreversible is committed. For a builder running Hermes agents against DeFi, that preview-first rule is the important one: simulate and cast run through the same adapters and state store, so a dry run is a faithful rehearsal rather than a parallel implementation. The per-venue skills give the agent snapshot parameters (router addresses, reserve info, bridge quotes) through a single venue CLI, which keeps market data lookups deterministic and replayable. The main caveats are the 6-star footprint, the missing license, and the three listings with no counterpart in the tree, all noted below.

## Usage

| You say | What happens |
|---|---|
| Buy or sell a Polymarket position | Uses grimoire-polymarket to query the CLOB and manage orders |
| What are the Hyperliquid books right now | Uses grimoire-hyperliquid to fetch mids, books, and open orders |
| Write a yield optimization strategy | Uses grimoire to author a .spell file, then compile and simulate it |
| What is the Uniswap router address on this chain | Uses grimoire-uniswap to retrieve router and adapter details |
| Check Aave reserve info | Uses grimoire-aave to fetch health checks and reserve data |
| Get a quote to bridge USDC to Base | Uses grimoire-across to fetch bridge quotes and routes |

## Verification

Confirm the README and the entry-point skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/franalgaba/grimoire/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/franalgaba/grimoire/main/skills/grimoire/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the verdicts below.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| grimoire-polymarket | Pass | Pass | Warn |
| grimoire-hyperliquid | Pass | Pass | Warn |
| grimoire | Pass | Pass | Warn |
| grimoire-uniswap | Pass | Pass | Warn |
| grimoire-aave | Pass | Pass | Pass |
| grimoire-morpho-blue | Pass | Pass | Warn |
| grimoire-pendle | Pass | Pass | Warn |
| grimoire-across | Warn | Pass | Pass |
| grimoire-vm | Pass | Pass | Warn |
| grimoire-yellow | not parsed | not parsed | not parsed |
| grimoire-lifi | Fail | None | Warn |

Across the 11 sampled listings there is one Fail cell (grimoire-lifi on the Gen Agent Trust Hub), nine Warn cells, and 19 Pass cells; grimoire-lifi returns no Socket verdict, grimoire-yellow returns no verdict on any tool, and the repository ships no license.

## Limitations

- Snapshot data, verified Nov 25, 2026: 18,384 combined installs across 11 indexed listings; 6 GitHub stars; no license; last pushed May 8, 2026. Counts drift over time.
- The repository publishes no license, so the reuse terms for these skills are unspecified; treat them as all-rights-reserved by default before depending on them in production.
- Three indexed listings (grimoire-vm, grimoire-yellow, grimoire-lifi) carry install counts but have no matching SKILL.md in the current tree.
- grimoire-lifi carries a Gen Agent Trust Hub Fail and grimoire-yellow returns no verdict on any tool; review those pages before use.
- grim setup writes plaintext secrets to .grimoire/setup.env; keep it local-only and rotate or delete it when not needed.

## Related

[Bankr Skills - DeFi and Onchain Agent Toolkit](/hermes/skills/catalog/bankrbot-skills-setup) | [AGI Pro Trading Skills - 68 Quant and DeFi Skills](/hermes/skills/catalog/agiprolabs-trading-skills-setup) | [VectorBT Backtesting Skills - Quant Workflow Setup](/hermes/skills/catalog/vectorbt-backtesting-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Simulate before you cast: run grimoire simulate with the same --rpc-url and chain you plan to commit with, so the dry run is a faithful rehearsal.
- Use grimoire venue doctor before running venue actions in a new environment to validate adapter, env, and RPC readiness.
- Advisory steps (advise) call a model when one is configured; replay them deterministically with --advisory-replay for live execution.
- Resolve unknown venue adapter errors by updating the CLI: npm i -g @grimoirelabs/cli@latest.
- Keep the setup env file out of version control; it holds plaintext secrets and should be rotated or deleted after setup.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
