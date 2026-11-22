---
title: "aiBTC Skills - Bitcoin, Stacks and DeFi Setup"
description: "aibtcdev/skills: AI agent skills for Bitcoin, Stacks and DeFi operations - 11.7K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/aibtcdev-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "bitcoin", "stacks", "defi"]
---

# aiBTC Skills - Bitcoin, Stacks and DeFi Setup

**Source:** [aibtcdev/skills](https://www.skills.sh/aibtcdev/skills) via skills.sh - 11.7K combined installs across 96 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [aibtcdev/skills](https://github.com/aibtcdev/skills) - 11 stars, no LICENSE file, main branch, last pushed Nov 18, 2026; each skill is a directory with a SKILL.md, an AGENT.md and one or more TypeScript scripts run with Bun that print JSON to stdout.
**Category:** Bitcoin, Stacks and DeFi Operations
**Quality Tier:** 🟡 Yellow - no LICENSE file and 11 stars; the 20 sampled skills carry one Fail cell (a Snyk Fail on x402) plus Socket Warns on aibtc-news and stx and Snyk Warns on most skills, with Gen Agent Trust Hub clean across all 20.

aiBTC Skills is a suite of AI agent skills for Bitcoin, Stacks and DeFi operations, converted from the aibtc MCP server into standalone skill directories. Each directory ships a SKILL.md that Claude Code reads to understand the skill, an AGENT.md that defines subagent behavior and guardrails, and one or more TypeScript scripts run with Bun that print JSON to stdout. The README positions the set for Claude Code, but the layout is plain skill directories, so any agent that reads SKILL.md files can use them.

The surface is wide: encrypted BIP39 wallet management, Bitcoin L1 (balances, fees, UTXOs, ordinals and runes), Stacks L2 (STX, sBTC, SIP-010 tokens, SIP-009 NFTs, BNS and stacking), DeFi (ALEX, Zest, Bitflow and HODLMM), on-chain identity and reputation (ERC-8004), message signing (SIP-018, BIP-137, BIP-322, BIP-340 and Nostr) and x402 paid API and inbox flows. It also ships a what-to-do directory of multi-step workflow guides and a community registry of agent configurations under aibtc-agents. Many of the write skills require an unlocked wallet and move real funds, which is why this guide points at review before granting wallet access.

## Installation

Every skill runs with Bun. Install one skill on its own through the skills CLI:

```bash
npx skills add aibtcdev/skills/x402
cd .agents/skills/x402
bun install
bun run x402.ts list-endpoints
```

Or clone the full repository and install once; every skill runs from the repo root:

```bash
git clone https://github.com/aibtcdev/skills.git
cd skills
bun install
```

Install Bun if it is missing:

```bash
curl -fsSL https://bun.sh/install | bash
```

Create or import a wallet before any transaction, then unlock it:

```bash
bun run wallet/wallet.ts create --name main --password YOUR-PASSWORD
bun run wallet/wallet.ts unlock --password YOUR-PASSWORD
bun run wallet/wallet.ts status
```

Skills default to testnet; set NETWORK=mainnet for mainnet operations. Several DeFi and inscription skills are mainnet-only and return an error on testnet.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| arxiv-research | 275 | fetch and compile arXiv papers on LLMs and AI infrastructure into scored research digests |
| wallet | 220 | create, import, unlock and manage encrypted BIP39 wallets for Stacks and Bitcoin addresses |
| aibtc-news | 219 | index-only listing with no directory in the current tree |
| aibtc-news-correspondent | 218 | index-only listing with no directory in the current tree |
| btc | 216 | Bitcoin L1 balances, fees, UTXOs and BTC transfers with cardinal, ordinal and rune UTXO classification |
| defi | 201 | ALEX DEX swaps and pool queries plus Zest Protocol lending on Stacks; mainnet-only |
| inbox | 200 | send and read paid x402 messages between agents and auto-reply with an AIBTC Inference Marketplace model |
| aibtc-news-scout | 194 | index-only listing with no directory in the current tree |
| aibtc-news-fact-checker | 194 | index-only listing with no directory in the current tree |
| identity | 192 | ERC-8004 on-chain agent identity registration, metadata and operator management |
| signing | 187 | SIP-018, Stacks and Bitcoin message signing plus BIP-340 Schnorr and Nostr event signing |
| sbtc | 186 | sBTC balances, transfers, deposits and peg statistics on Stacks L2 |
| query | 185 | Stacks network and blockchain queries via the Hiro API |

The remaining 83 indexed listings range from 22 to 182 installs.

## Why This Matters for Hermes Agents

The suite's value is that it collapses the whole Bitcoin plus Stacks surface into one consistent CLI convention: every script prints a single JSON object to stdout, errors included, so an agent can call and parse any skill the same way. The wallet and credentials skills centralize secrets in AES-256-GCM encrypted files under ~/.aibtc, which keeps keys out of prompts. The nonce-manager skill coordinates cross-process nonces so concurrent skills do not collide on the mempool. For builders the interesting pattern is the SKILL.md plus AGENT.md split: one file documents the CLI interface, the other encodes the decision rules and guardrails a subagent should follow, which is a clean way to make fund-moving operations reviewable. The on-chain identity, reputation and validation skills plus the x402 inbox turn the suite into more than tooling: they wire an agent into an agent economy where identity and payments are on-chain. The cost is real and should be named: many skills sign and broadcast transactions, so a misconfigured unlock or a stale mainnet flag can move money.

## Usage

| You say | What happens |
|---|---|
| Create a new wallet and check its balance | Creates an encrypted BIP39 wallet, then reports Stacks and Bitcoin address balances |
| Send 0.001 BTC to this address | Estimates fees, classifies UTXOs as spendable or inscribed, then builds and broadcasts the transfer |
| Swap STX for a token on Bitflow | Quotes the swap with price impact, then executes the aggregated DEX swap through the Bitflow skill |
| Deposit BTC for sBTC | Routes a BTC deposit through the sBTC skill and tracks the deposit status on Stacks L2 |
| Sign this message with my Stacks address | Produces an on-chain verifiable SIP-018 signature or a SIWS-compatible plain-text signature |
| Send a paid message to that agent's inbox | Sends an x402-paid message with a sponsored sBTC transaction and can auto-reply with an inference model |
| Check my DeFi positions | Scans Bitflow, Zest, ALEX and Styx for a wallet address and returns a risk-scored portfolio summary |

## Verification

Fetch a SKILL.md before installing, especially for the fund-moving skills:

```bash
curl -sL https://raw.githubusercontent.com/aibtcdev/skills/main/wallet/SKILL.md | head -40
```

Review the signing skill before it signs anything:

```bash
curl -sL https://raw.githubusercontent.com/aibtcdev/skills/main/signing/SKILL.md | head -40
```

Read x402, the skill that carries the sample's only Fail cell, before granting it network or payment access:

```bash
curl -sL https://raw.githubusercontent.com/aibtcdev/skills/main/x402/SKILL.md | head -40
```

Confirm the sBTC skill's deposit flow before moving BTC:

```bash
curl -sL https://raw.githubusercontent.com/aibtcdev/skills/main/sbtc/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| arxiv-research | Pass | Pass | Warn |
| wallet | Pass | Pass | Warn |
| aibtc-news | Pass | Warn | Warn |
| aibtc-news-correspondent | Pass | Pass | Warn |
| btc | Pass | Pass | Warn |
| defi | Pass | Pass | Warn |
| inbox | Pass | Pass | Warn |
| aibtc-news-scout | Pass | Pass | Warn |
| aibtc-news-fact-checker | Pass | Pass | Warn |
| identity | Pass | Pass | Warn |
| signing | Pass | Pass | Pass |
| sbtc | Pass | Pass | Warn |
| query | Pass | Pass | Warn |
| x402 | Pass | Pass | Fail |
| stx | Pass | Warn | Warn |
| ceo | Pass | Pass | Pass |
| business-dev | Pass | Pass | Warn |
| credentials | Pass | Pass | Pass |
| transfer | Pass | Pass | Warn |
| aibtc-news-deal-flow | Pass | Pass | Warn |

These skills move real funds. wallet, signing, sbtc, x402 and the DeFi skills create, sign and broadcast transactions, so review each SKILL.md and its AGENT.md before granting wallet access. The sample carries one Fail cell, a Snyk Fail on x402, with Gen Agent Trust Hub clean across all 20 sampled skills.

## Limitations

- Snapshot data, verified Nov 22, 2026: 11.7K combined installs across 96 indexed listings; 11 GitHub stars; no LICENSE file; last pushed Nov 18, 2026. Counts drift over time.
- There is no LICENSE file at the repository root, so redistribution and modification rights are unclear despite the skills being public.
- These skills move real funds: wallet, signing, sbtc, x402 and the DeFi skills sign and broadcast transactions, so review each SKILL.md and AGENT.md before granting wallet access.
- Thirteen indexed listings (the ten aibtc-news listings plus paperboy, hodlmm-signal-allocator and inscription-queue-watcher) carry install counts but have no directory in the current tree, so the install index outruns the directories the repository ships.
- Only 20 of the 96 indexed listings have skills.sh security verdicts in this snapshot; the remaining 76 are unverified.
- Most write operations default to testnet unless NETWORK=mainnet is set, while several DeFi and inscription skills are mainnet-only.

## Related

- [Bankr Skills - DeFi and Onchain Agent Toolkit](/hermes/skills/catalog/bankrbot-skills-setup)
- [Uniswap AI - DeFi Integration Skills Setup](/hermes/skills/catalog/uniswap-ai-skills-setup)
- [Coinbase Agentic Wallet - USDC Payments Skill](/hermes/skills/catalog/coinbase-agentic-wallet-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start on testnet, the default, and confirm balances and status with the wallet and btc skills before switching NETWORK=mainnet.
- Create and unlock the wallet first; most write skills require an unlocked wallet before they do anything.
- Back up the seed phrase in an offline location before mainnet use; it is the only way to recover the wallet if the password is lost.
- Read each SKILL.md and AGENT.md before granting wallet access, since these skills sign and broadcast real transactions.
- Add a free Hiro API key (platform.hiro.so) with the settings skill to lift Stacks API rate limits.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
