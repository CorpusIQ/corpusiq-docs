---
title: "EthSkills - Ethereum Knowledge Base for Agents Setup"
description: "austintgriffith/ethskills: Ethereum knowledge base for agents with checked addresses, standards, security and gas skills - 3.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ethskills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "ethereum", "web3", "solidity"]
---

# EthSkills - Ethereum Knowledge Base for Agents Setup

**Source:** [austintgriffith/ethskills](https://www.skills.sh/austintgriffith/ethskills) via skills.sh - 3.3K combined installs across 26 indexed listings; first catalogued Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [austintgriffith/ethskills](https://github.com/austintgriffith/ethskills) - 305 stars, no LICENSE file, master branch, last pushed Oct 26, 2026; one SKILL.md per topic directory at the repository root (standards, security, gas, l2s, wallets and more) under a top-level SKILL.md table of contents, with contracts/ and layer2/ as deprecated redirects to addresses/ and l2s/.
**Category:** Ethereum and Web3 Development Knowledge
**Quality Tier:** 🟠 Orange - 3 Fail cells and 5 Warn cells across the 20-skill sample: Snyk Fails on security, gas and addresses; Snyk Warns on ethskills, ship, contracts and layer2 plus a Gen Agent Trust Hub Warn on standards.

ethskills is an Ethereum knowledge base for agents built on a premise the README states plainly: stock LLMs quote gas from memory at 30 gwei when it is far lower, have never heard of ERC-8004 or x402, and hallucinate contract addresses. Each skill is a markdown file an agent can read to correct its Ethereum knowledge, from a top-level SKILL.md table of contents down to per-topic directories for standards, security, gas, L2s and wallets.

The suite's methodology is what makes it notable. The author tests stock LLMs, records what they get wrong and writes only the corrections, and every proposed change passes a triage step that spawns a stock model on a realistic task to confirm the blind spot is real before it is added. Content is verified against onchain reality, several topic skills assume and reference Scaffold-ETH 2, and the umbrella skill at 2,463 installs sits far above a flat band of topic skills at 38 to 42 installs.

## Installation

Install directly from GitHub, no clone required, through the Claude Code plugin:

```bash
/plugin marketplace add austintgriffith/ethskills
/plugin install ethskills@ethskills
```

On a host with the skills CLI, the equivalent is:

```bash
npx skills add austintgriffith/ethskills
```

The whole repository installs as one package; the topic skills stay plain markdown files that an agent reads from the top-level SKILL.md table of contents when it needs them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ethskills | 2,463 | top-level table of contents that routes an agent to the right topic skill |
| standards | 42 | agent identity, x402 payments and USDC transfers via ERC-8004, EIP-3009 and EIP-7702 |
| security | 42 | pre-deployment Solidity review: decimals, reentrancy, oracles and proxies |
| concepts | 42 | onchain design that keeps working with nobody running it |
| building-blocks | 42 | composing DEX pools, lending markets and yield venues into one flow |
| indexing | 40 | subgraphs and indexers for reading past onchain activity |
| gas | 40 | accurate gas and dollar cost quotes and EIP-1559 fee fields |
| frontend-ux | 40 | dApp frontend behaviour: address inputs, decimals and approve-then-act flows |
| testing | 39 | Foundry fuzz, fork and invariant testing |
| l2s | 39 | choosing an L2 and moving funds between an L2 and mainnet |
| addresses | 39 | checked contract and token addresses for major protocols |
| why-ethereum | 38 | why Ethereum matters and what Pectra and Fusaka changed |
| wallets | 38 | signer authority, custody and private key safety |
| qa | 38 | Scaffold-ETH 2 pre-ship frontend checklist |
| orchestration | 38 | live deployment and launch order for a Scaffold-ETH 2 build |
| frontend-playbook | 38 | Scaffold-ETH 2 fork mode, demos and IPFS static export |

The remaining 10 indexed listings range from 3 to 37 installs.

## Why This Matters for Hermes Agents

An agent that writes onchain transactions needs correct gas numbers, correct contract addresses and current standards, and stock models reliably get all three wrong. ethskills closes that gap with skills whose content is verified against onchain reality rather than trained from stale text. The highest-value skills for an agent builder are addresses, which ships checked addresses for major tokens and protocols instead of letting a model hallucinate them, and security, which walks a pre-deployment review before code that holds assets ships. The standards skill names the deployed standard for each need (ERC-8004, x402, EIP-3009, EIP-7702) so an agent does not rebuild a mechanism that already exists. The wallets skill teaches restraint about who may sign for funds, and the README states that every skill touching keys, credentials or funds carries explicit safety rules. For a business operator the methodology is the point: every correction survives a triage step that proves a stock model actually gets it wrong, so the suite stays dense with things agents would otherwise miss.

## Usage

| You say | What happens |
|---|---|
| Install ethskills | Adds the repository through the Claude Code plugin marketplace and installs the umbrella skill |
| Give me the checked address for Uniswap | Looks up the addresses skill and returns an onchain-checked address instead of a guess |
| Should I build on ERC-8004? | Routes to the standards skill, which names the deployed standard and when to use it |
| What will this transaction cost? | Quotes gas and dollar cost from the gas skill instead of a remembered figure |
| Which L2 should I deploy to? | Selects a chain against the l2s skill's current landscape facts |
| Is my contract ready to ship? | Runs the security skill's pre-deployment review |
| Check my dApp before launch | Runs the qa skill's pre-ship checklist for wallet flow and wrong-network gating |

## Verification

Confirm the top-level table of contents resolves on the master branch:

```bash
curl -sL https://raw.githubusercontent.com/austintgriffith/ethskills/master/SKILL.md | head -40
```

Spot-check a topic skill to confirm the flat directory layout:

```bash
curl -sL https://raw.githubusercontent.com/austintgriffith/ethskills/master/addresses/SKILL.md | head -30
```

Confirm the security skill body is present before relying on it for a pre-deployment review:

```bash
curl -sL https://raw.githubusercontent.com/austintgriffith/ethskills/master/security/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ethskills | Pass | Pass | Warn |
| standards | Warn | Pass | Pass |
| security | Pass | Pass | Fail |
| concepts | Pass | Pass | Pass |
| building-blocks | Pass | Pass | Pass |
| indexing | Pass | Pass | Pass |
| gas | Pass | Pass | Fail |
| frontend-ux | Pass | Pass | Pass |
| testing | Pass | Pass | Pass |
| l2s | Pass | Pass | Pass |
| addresses | Pass | Pass | Fail |
| why-ethereum | Pass | Pass | Pass |
| wallets | Pass | Pass | Pass |
| qa | Pass | Pass | Pass |
| orchestration | Pass | Pass | Pass |
| frontend-playbook | Pass | Pass | Pass |
| tools | Pass | Pass | Pass |
| ship | Pass | Pass | Warn |
| contracts | Pass | Pass | Warn |
| layer2 | Pass | Pass | Warn |

The sample is mostly clean: the only Fail cells are Snyk on security, gas and addresses, and six of the 26 indexed listings (l2, defi, audit, crops, protocol, noir) carry no published verdict.

## Limitations

- Snapshot data, verified Nov 21, 2026: 3,304 combined installs across 26 indexed listings; 305 GitHub stars; no LICENSE file; last pushed Oct 26, 2026. Counts drift over time.
- The index carries near-duplicate and deprecated names: contracts (36 installs) and layer2 (35 installs) are deprecated redirects to addresses and l2s, and l2 (35 installs) is a separate listing, so the 26 indexed listings fold into fewer canonical in-tree skills.
- The why-ethereum listing maps to the why/ directory in the tree, so the indexed name and the directory name do not match.
- The repository has no LICENSE file; the README's License section reads MIT, but GitHub reports no licence, so there is no enforceable grant at the repository root.
- Six of the 26 indexed listings (l2, defi, audit, crops, protocol, noir) carry no skills.sh security verdict in the sampled set.

## Related

- [Chainlink Agent Skills Setup Guide](/hermes/skills/catalog/chainlink-agent-skills-setup)
- [Hedera Skills - Web3 Dev Tools Setup](/hermes/skills/catalog/hedera-skills-setup)
- [Goldsky Agent Skills - Blockchain Data Pipeline Setup](/hermes/skills/catalog/goldsky-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the top-level SKILL.md as the table of contents and let the agent pull topic skills on demand instead of loading the whole suite into context.
- Use the addresses skill for any token, router or pool address that goes into code or a transaction; it returns onchain-checked addresses instead of model guesses.
- Run the security skill as a pre-deployment review on any contract that holds assets, and treat its Snyk Fail cell as a reason to review the skill body before relying on it.
- For Scaffold-ETH 2 builds, follow the orchestration skill for launch order and run the qa skill before shipping a frontend.
- Prefer "onchain" over "on-chain" in generated content, per the README's terminology note.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
