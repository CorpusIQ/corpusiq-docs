---
title: "Bankr Skills - DeFi and Onchain Agent Toolkit"
description: "bankrbot/skills on skills.sh: 6.2K combined installs across 123 listings; DeFi, wallet and onchain agent skills for Bankr agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bankrbot-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "defi", "onchain", "base"]
---

# Bankr Skills - Setup Guide

**Source:** [bankrbot/skills](https://www.skills.sh/bankrbot/skills) via skills.sh - 6.2K combined installs across 123 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 1,209 stars, no LICENSE file in the repository root, last pushed 2026-11-04, 156 SKILL.md directories, one per top-level folder
**Category:** Onchain agents: Bankr skills for DeFi monitoring, token distribution, prediction markets and wallet operations
**Quality Tier:** 🟡 Review - no LICENSE file in the repo root, and all 5 sampled skills.sh audits carry a Socket or Snyk Warn (bankr, agenticbets, aeon-monitor-kalshi, pmfi-parbitrage, urizen).

Bankr Skills is a catalogue of plug-and-play tools for agents that touch onchain money. The top-level folders are individual skills, each with a SKILL.md and a `catalog.json` that tells the Bankr catalogue how the skill should appear and install. Providers contributing skills include Uniswap, Coinbase, Alchemy, Zerion, Base, EthSkills and a long tail of smaller protocols, alongside Bankr's own wallet and token launch tooling.

The shape of the repository is unusual in this catalog: it is a skills registry with a schema, not a single author's bundle. The `catalog.json` in each folder carries the slug, provider, logo, setup steps and the exact install command string, and a folder without a valid `catalog.json` is skipped by the Bankr Discover catalogue. That makes it the most directly composable set here, and also the least uniform.

## Installation

The README installs a skill by asking the agent, naming the folder URL:

```text
> install the bankr skill from https://github.com/BankrBot/skills/tree/main/bankr
```

The template form covers any folder in the repository:

```text
> install the [skill-name] skill from https://github.com/BankrBot/skills/tree/main/[skill-name]
```

That instruction is also what each folder's `catalog.json` carries as its install command, so the registry and the README agree on one mechanism:

```json
{
  "install": {
    "type": "bankr",
    "repoPath": "bankr",
    "command": "install the bankr skill from https://github.com/BankrBot/skills/tree/main/bankr"
  }
}
```

Some listings are not hosted here. Skills that install from elsewhere use the external form in `catalog.json`, and the README documents it with an example:

```json
{ "install": { "type": "external", "provider": "Acme", "command": "npx skills add acme/skills", "reference": null } }
```

Hunch is one of these: the README states that both hunch skills install from `github.com/rajkaria/hunch-skills`. If the prompt form fails for a folder, check its `catalog.json` for the external provider before assuming the path is wrong.

## What It Provides

The install index is long and flat: 123 listings, of which 13 clear 100 installs. The concentration is extreme, with `bankr` alone accounting for roughly a fifth of the combined total.

| Skill | Installs | Use For |
|---|---|---|
| bankr | 1,132 | The Bankr agent itself through the CLI or REST API: trading and swaps, balances and PnL, perps, prediction markets, NFTs, token launch, x402 paid endpoints and the LLM gateway across ten chains |
| botchan | 467 | Onchain agent messaging on Base through Net Protocol: explore agents, post to topic feeds, send direct messages, store data permanently |
| erc-8004 | 231 | Registering an agent identity on Ethereum mainnet as an ERC-8004 agent NFT, including IPFS upload, reputation setup and discoverability |
| clanker | 230 | Deploying ERC20 tokens with Uniswap V4 liquidity through the Clanker SDK, with vaults, airdrops, vesting, dev buys and fee claims |
| neynar | 218 | Farcaster through the Neynar API: read feeds, look up users, post casts, search content; requires NEYNAR_API_KEY |
| onchainkit | 213 | Coinbase OnchainKit React components and TypeScript utilities: wallet connection, swaps, mints, payments and onchain identity |
| ens-primary-name | 213 | Setting a primary ENS name and reverse resolution on Base, Arbitrum, Optimism and Ethereum mainnet |
| qrcoin | 206 | QR Coin auctions on Base: read auction status, view current bids, create or contribute to bids for the encoded URL |
| endaoment | 203 | Donating crypto to 501(c)(3) nonprofits through Endaoment on Base, Ethereum and Optimism, with automatic swap to USDC |
| veil | 199 | Private and shielded transactions on Base through Veil Cash: ZK-proof withdrawals, keypair management and pool balances |
| yoink | 198 | Playing Yoink, an onchain capture-the-flag game on Base, with stats, leaderboards and Bankr-executed transactions |
| zapper | 197 | Indexed at 197 installs, but the folder's SKILL.md is the literal placeholder "Placeholder for Zapper skill.", so there is nothing to run |
| base | 195 | Indexed at 195 installs, with the same placeholder body ("Placeholder for Base skill."); the real Base material lives in the five base-* sub-skills |

The remaining 110 indexed listings range from 7 to 85 installs, from bankr-signals (85) and siwa (70) down to urizen (7). That tail includes the 24 aeon monitors and research skills, the Uniswap and EthSkills suites, and a set of rows titled like documentation sections (Gas & Costs, Wallets, Base Node, Uniswap Viem) at 12 to 15 installs each, none of which matches a top-level folder name.

## Why This Matters for Hermes Agents

Onchain work is the highest-consequence domain an agent can be pointed at, because a wrong argument is not a failed test, it is a transaction. This repository is useful precisely because it encodes the operational shape of that work: which chain ID, which contract, which approval, which verification step, rather than leaving an agent to reconstruct a call from memory.

The provider diversity is the practical advantage. A single agent task can involve reading a wallet across 41 or more chains (zerion), simulating a transaction before signing (alchemy), finding a pool (uniswap-driver) and settling a payment over x402, and each step has a skill that documents the actual API rather than a paraphrase of it. That is the difference between an agent that writes plausible DeFi code and one that completes a transaction.

The wallet and safety patterns are worth reading even if you never install the suite. EthSkills carries explicit rules for agent key safety and a transaction safety pattern with human approval thresholds, and the `bankr` skill advertises IP whitelisting, hallucination guards and transaction verification. Those are the controls an agent handling funds needs, and they are documented here as part of the skill rather than bolted on afterwards.

The `catalog.json` schema is the other thing worth stealing. Requiring a slug that matches the folder, a provider, a logo and an install command makes a skills registry machine-readable, which is what lets a Bankr agent discover and install a capability without a human copying a URL.

It also shows the failure mode of a fast-moving registry. Two of the 13 most-installed listings are empty placeholders, and several rows in the index are section titles rather than skills. Reading the folder before trusting the install count is the habit this repository teaches.

## Usage

| You say | What happens |
|---|---|
| "What is my wallet worth across chains?" | bankr reads balances and PnL, or zerion returns interpreted portfolio data with DeFi positions |
| "Swap 50 USDC into ETH on Base" | bankr quotes and submits the swap, then verifies the transaction |
| "Launch a token with a small airdrop" | clanker deploys the ERC20 with Uniswap V4 liquidity, then configures vaults, airdrop and vesting |
| "Is this token a rug?" | bankr-token-scam-analysis produces a risk verdict backed by onchain facts |
| "Post an update to Farcaster" | neynar posts the cast; botchan messages a specific agent wallet instead |
| "What are the odds on this market?" | aeon-monitor-polymarket or aeon-monitor-kalshi surfaces material moves and cross-venue arb |
| "Donate 100 USDC to a charity" | endaoment finds the 501(c)(3) and sends, swapping other tokens to USDC first |
| "Register my agent onchain" | erc-8004 mints the agent NFT on Ethereum mainnet after the IPFS upload |

## Verification

Confirm the folder's frontmatter before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/bankrbot/skills/main/bankr/SKILL.md | head -5
```

It should open with `name: bankr` and a description naming the Wallet API, the LLM gateway and the supported chains. Then confirm the catalogue entry, since a folder without a valid `catalog.json` is skipped by the Bankr catalogue:

```bash
curl -fsSL https://raw.githubusercontent.com/bankrbot/skills/main/bankr/catalog.json | python3 -m json.tool | head -12
```

Check that `slug` equals the folder name and that `install.command` names the folder you intended. After the agent installs, confirm the skill directory exists in the agent's skills path and that its frontmatter `name` matches that folder; a mismatch is what a copy-pasted prompt usually produces.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bankr | Pass | Warn | Warn |
| agenticbets | Pass | Pass | Warn |
| aeon-monitor-kalshi | Pass | Pass | Warn |
| pmfi-parbitrage | Pass | Warn | Warn |
| urizen | Pass | Pass | Warn |

Every sampled skill carries at least one Warn, and there is no LICENSE file, so neither the verdicts nor the repository give you terms to rely on. Treat both as unresolved rather than as approval.

The domain is the bigger risk. These skills sign transactions, hold keys and spend USDC over x402. Several of them keep a keypair or an API key (veil manages Veil keypairs, neynar needs NEYNAR_API_KEY, 1claw is an HSM-backed vault with policy-gated access), and the payment flow is per-call, which means a loop in an agent can spend in a way a subscription cannot. Set an explicit spending ceiling, keep the wallet funded with what the task needs and nothing more, and require human approval above a threshold before enabling any skill that submits transactions.

The repo is also a registry of third-party code. A skill contributed by a protocol is that protocol's documentation plus that protocol's scripts; the skills.sh verdict on one folder says nothing about the next. Re-check the page for the specific skill you install.

## Limitations

- Snapshot data, verified 2026-11-05: 6,157 combined installs across 123 indexed listings; 1,209 GitHub stars; no LICENSE file; last pushed 2026-11-04. Counts drift over time.
- No LICENSE file. There is no stated grant for reuse, and contributions from a dozen providers may carry their own terms in their own repositories.
- Two of the 13 listings in the table above are empty: `zapper` and `base` contain a one-line placeholder SKILL.md with no instructions. Their install counts measure curiosity, not capability.
- The index and the tree disagree at the edges. 123 listings against 156 SKILL.md directories means some folders are unindexed, and 26 listings are titled like documentation sections (Gas & Costs, Frontend UX, Base Account) at 12 to 15 installs each rather than like a top-level folder.
- Install is prompt-driven. The README documents no package-manager command for this repository as a whole; each skill's `catalog.json` carries its own command, and external skills install from their own provider repos.
- Quality varies by provider. Some listings are thin wrappers over a single API, others are full playbooks; the install count does not distinguish them.

## Related

- [Coinbase Agentic Wallet - USDC Payments Skill](/hermes/skills/catalog/coinbase-agentic-wallet-setup)
- [Solana Dev Skill - Official Blockchain Development](/hermes/skills/catalog/solana-dev-skill-setup)
- [Binance Skills Hub - Crypto Trading Skills Setup](/hermes/skills/catalog/binance-skills-hub-setup)

## Pro Tips

- Install the suite you need, not the repository. The Uniswap, Base and EthSkills folders each install independently, and pulling five folders is cheaper in context than pulling fifty.
- Read `catalog.json` before the SKILL.md. It tells you what the skill installs and who provides it in ten lines, which is enough to reject most candidates.
- Start read-only. Portfolio reads, gas checks and monitors cost nothing and prove the credentials work before you enable anything that signs.
- Keep a separate wallet for agent work with a small balance and IP whitelisting, and set the approval threshold before the first transaction rather than after the first mistake.
- Skip the placeholders explicitly. `base` and `zapper` are indexed but empty, and an agent asked to use them will happily invent the behaviour.
- Use aeon-skill-security-scan before trusting any third-party folder. It audits installed skills for shell injection, secret exfiltration, path traversal and prompt-override payloads, which is exactly the threat model of a public registry.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
