---
title: "SendAI Skills - Solana Agent Skill Marketplace Setup"
description: "sendaifun/skills - 8.2K combined installs: a public marketplace of Solana agent skills spanning DeFi, infrastructure, trading, oracles and security."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sendaifun-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "solana", "defi", "trading", "web3"]
---

# SendAI Skills - Setup Guide

**Source:** [sendaifun/skills](https://www.skills.sh/sendaifun/skills) via skills.sh - 8.2K combined installs across 50 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [sendaifun/skills](https://github.com/sendaifun/skills) - 129 stars, Apache-2.0 license, last pushed Jul 31, 2026, main branch; a skills/ directory with one folder per skill (545 files), a .claude-plugin/marketplace.json manifest, and a scripts/validate-marketplace.js validator.
**Category:** Solana Agent Skills (DeFi, Infrastructure, Trading, Oracles, Security)
**Quality Tier:** 🟡 Yellow - 1 Gen Agent Trust Hub Fail cell (surfpool) and 14 Warn cells across the 15 sampled skills; several skills handle wallets, keys and funds, so review each before use.

sendaifun/skills is a public marketplace of Solana-related agent skills from SendAI, organized so a single plugin install exposes the whole catalogue to an agent. The 50 indexed listings span DeFi protocols (Jupiter, Raydium, Orca, Meteora, Kamino, MarginFi, PumpFun), infrastructure (Helius, QuickNode, Light Protocol, Squads), trading (dFlow, Ranger Finance), oracles (Pyth, Switchboard), data (CoinGecko, Birdeye), and security (vulnhunter, zz-code-recon). Each skill is a folder under skills/ with a SKILL.md plus reference docs, examples, and templates, and the repo validates the marketplace shape with its own script.

Several skills in this marketplace move funds or touch wallets and keys: the DEX and lending skills sign and send transactions, solana-kit and solana-agent-kit build signers and transfer SOL, Squads manages multisig treasuries, and the Phantom and wallet-related skills bridge a wallet connection. Read the Security section before pointing any of these at a funded wallet.

## Installation

In Claude Code, add the marketplace, then install individual skills:

```
/plugin marketplace add sendaifun/skills
```

```
/plugin install jupiter
/plugin install helius
/plugin install meteora
```

In Cursor, open Settings (Cmd+Shift+J or Ctrl+Shift+J), then Rules & Commands, Project Rules, Add Rule, Remote Rule (GitHub), and enter https://github.com/sendaifun/skills.git. Skills are auto-discovered by context. For any other agent:

```bash
npx skills add sendaifun/skills
```

## What It Provides

Of the 50 indexed listings, 17 sit at 200 installs or more and appear below; descriptions are drawn from the skills.sh per-skill descriptions and the README's Available Skills table.

| Skill | Installs | Use For |
|---|---|---|
| solana-kit | 359 | @solana/kit JS SDK: RPC, signers, transaction building and sending |
| helius | 359 | Helius RPC, DAS API, webhooks, priority fees and streaming |
| pumpfun | 333 | PumpFun token launches, bonding curves and PumpSwap AMM |
| meteora | 287 | Meteora liquidity pools, DLMM, bonding curves and vaults |
| vulnhunter | 282 | security vulnerability detection and variant analysis |
| coingecko | 249 | CoinGecko token prices, DEX pool data and OHLCV charts |
| raydium | 247 | Raydium swaps, CLMM and CPMM pools, and LaunchLab |
| solana-agent-kit | 245 | build Solana agents with 60+ actions, LangChain and MCP |
| zz-code-recon | 241 | architectural context building for security audits |
| surfpool | 228 | Solana test environment with mainnet forking and cheatcodes |
| solana-kit-migration | 216 | migrate @solana/web3.js v1 code to @solana/kit |
| pyth | 213 | Pyth price feeds, confidence intervals and streaming |
| orca | 210 | Orca Whirlpools swaps, liquidity and positions |
| pinocchio-development | 208 | Pinocchio zero-copy Solana program development |
| squads | 206 | Squads multisig, smart accounts and treasury management |
| metaplex | 205 | Metaplex NFTs: Core, Token Metadata and Candy Machine |
| kamino | 203 | Kamino lending, borrowing and liquidity management |

The remaining 33 indexed listings range from 39 to 197 installs.

## Why This Matters for Hermes Agents

For a Hermes builder working on Solana, this marketplace is the fastest way to give an agent correct protocol knowledge without memorizing SDKs. Each skill is a self-contained folder with a SKILL.md, reference docs, code examples and templates, so the agent can produce working TypeScript against Jupiter, Raydium, Helius or Pyth instead of approximating an API it half-remembers. The catalogue spans the whole stack: RPC and indexing infrastructure, DEX and lending protocols, oracles, NFTs, program development and security review. Because SendAI maintains it with a validation script and a Claude Code plugin manifest, the marketplace shape is consistent, and a single plugin command exposes every skill. The serious caveat is financial: many of these skills sign and send transactions, manage multisigs, or connect a wallet, so a Hermes agent should treat them as code to review, not as a safe default. For read-only work (prices, analytics, audits) the marketplace is low-risk; for anything that moves value, review the specific skill and its SDK first.

## Usage

| You say | What happens |
|---|---|
| Get a quote and swap on Jupiter | Uses the jupiter skill's API patterns for quotes, limit orders and swaps |
| Track token prices and trending tokens | Uses coingecko or birdeye for prices, OHLCV and trending data |
| Launch a token on a bonding curve | Uses pumpfun for token creation and buy/sell on bonding curves |
| Migrate from @solana/web3.js v1 to @solana/kit | Uses solana-kit-migration for API mappings and edge cases |
| Audit this Solana contract for vulnerabilities | Uses vulnhunter to hunt dangerous APIs and variants |
| Set up a multisig treasury | Uses squads for multisig creation and vault transactions |
| Fetch real-time price feeds for a DeFi app | Uses pyth for price feeds with confidence intervals |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/sendaifun/skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/sendaifun/skills/main/skills/solana-kit/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it; the README's Available Skills table lists the documented skills, and scripts/validate-marketplace.js checks the marketplace shape.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| solana-kit | Pass | Pass | Warn |
| helius | Pass | Warn | Warn |
| pumpfun | Pass | Pass | Warn |
| meteora | Pass | Warn | Warn |
| vulnhunter | Pass | Warn | Pass |
| coingecko | Pass | Pass | Pass |
| raydium | Pass | Pass | Warn |
| solana-agent-kit | Pass | Warn | Warn |
| zz-code-recon | Pass | Pass | Pass |
| surfpool | Fail | Warn | Warn |
| solana-kit-migration | Pass | Pass | Pass |
| pyth | Pass | Pass | Pass |
| orca | Pass | Pass | Warn |
| pinocchio-development | Pass | Pass | Pass |
| squads | Pass | Pass | Warn |

surfpool draws the only Fail (Gen Agent Trust Hub), and Warns land on Socket and Snyk across the rest; the sample covers 15 of 50 listings. Treat funds-moving and wallet/key-handling skills as high review priority: solana-kit, solana-agent-kit, pumpfun, meteora, raydium, orca, kamino, squads, dflow, lavarage, marginfi, lulo, sol-incinerator, debridge, lifi, helius, and the Phantom and wallet skills all touch signing, sending, or balances.

## Limitations

- Snapshot data, verified Nov 25, 2026: 8,166 combined installs across 50 indexed listings; 129 GitHub stars; Apache-2.0 license; last pushed Jul 31, 2026. Counts drift over time.
- Several skills move funds or handle wallets and keys (solana-kit, solana-agent-kit, pumpfun, meteora, raydium, orca, kamino, squads, dflow, lavarage, marginfi, lulo, sol-incinerator, debridge, lifi, helius, and the Phantom and wallet skills); review any of them before pointing them at a funded wallet.
- A few index names do not match the current tree: integrating-jupiter maps to skills/jupiter, metengine-data-agent to skills/metengine, and inco-svm to skills/inco, while my-skill-name and drift carry install counts but have no skills/<name>/ directory.
- The marketplace targets Solana only, with no other-chain coverage, and the last push is Jul 31, 2026, so protocol details may lag newer releases.
- skills.sh sampled 15 of 50 listings for security verdicts; the other 35 have no published verdicts.

## Related

[Chainlink Agent Skills Setup Guide](/hermes/skills/catalog/chainlink-agent-skills-setup) | [Mysten Labs Skills - Sui Move Development Setup](/hermes/skills/catalog/mystenlabs-skills-setup) | [aiBTC Skills - Bitcoin, Stacks and DeFi Setup](/hermes/skills/catalog/aibtcdev-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install via /plugin marketplace add sendaifun/skills in Claude Code so the whole catalogue is available, then /plugin install only the skills you need.
- Keep read-only skills (coingecko, birdeye, pyth, switchboard) separate from funds-moving skills in your agent's config.
- For any skill that signs or sends transactions, read its SKILL.md and examples, then test on a devnet or a fresh wallet first.
- Use surfpool for mainnet forking and cheatcodes when testing swaps and programs, but treat its security Fail as a reason to keep it in a sandboxed environment.
- Treat the skills.sh verdicts as a starting point only; the 35 un-sampled listings have no published verdicts.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
