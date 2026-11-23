---
title: "DFINITY ICP Skills - Agent Development Setup"
description: "dfinity/icskills: agent-readable skill files for Internet Computer (ICP) development that prevent AI hallucinations - 8.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dfinity-icp-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "internet computer", "icp", "canister", "motoko"]
---

# DFINITY ICP Skills - Agent Development Setup

**Source:** [dfinity/icskills](https://www.skills.sh/dfinity/icskills) via skills.sh - 8.4K combined installs across 58 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [dfinity/icskills](https://github.com/dfinity/icskills) - 40 stars, Apache-2.0 license, main branch, last pushed Nov 20, 2026; one SKILL.md per skill under skills/ with references/ and scripts/ subfolders, plus .agents/skills/ and .brand/ copies and a skills/skill.schema.json frontmatter schema.
**Category:** Internet Computer (ICP) and Canister Development
**Quality Tier:** 🟠 Orange - 1 Fail cell and 15 Warn cells across the 20-skill sample: Snyk Fails on icp-cli and Warns on most integration skills, with Socket Warns on icp-cli and canhelp.

Agent-readable instructions for every Internet Computer need. This repository packages each ICP capability as a single markdown skill that an agent reads to build correctly, on the stated premise that agents building on the Internet Computer hallucinate canister IDs, use deprecated APIs and miss critical pitfalls when they rely on human-facing documentation alone.

Every skill typically includes a What This Is paragraph, exact prerequisite versions (ic-cdk >= 0.19, @icp-sdk/auth >= 4.0.1), a numbered Common Pitfalls section, tested copy-paste-correct implementation code, and Deploy and Test plus Verify It Works steps. The skills are under active development and reviewed and signed off by DFINITY engineers, and each can carry an evaluation file that compares agent output with and without the skill using an LLM judge.

## Installation

The quickest path for any agent is to point it at the discovery index:

```text
Fetch https://skills.internetcomputer.org/llms.txt and follow its instructions when building on ICP
```

Install through the skills CLI for any agent that supports skills (Claude Code, Cursor, Windsurf, Copilot and more):

```bash
npx skills add dfinity/icskills
```

Or fetch a single skill manually and place it wherever your agent reads instructions from:

```bash
curl -sL https://skills.internetcomputer.org/.well-known/agent-skills/ckbtc/SKILL.md
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| icp-cli | 420 | building and deploying IC apps with the icp CLI: icp.yaml, recipes, identity and bundling |
| canister-security | 355 | IC security patterns: access control, reentrancy prevention, callback traps and upgrade safety |
| stable-memory | 346 | persisting canister state across upgrades with StableBTreeMap, MemoryManager and persistent actors |
| internet-identity | 345 | Internet Identity login and user authentication for IC apps |
| https-outcalls | 343 | HTTPS requests from canisters to external APIs with consensus and cycle pricing |
| cycles-management | 333 | managing cycles, top-ups, freezing thresholds and ICP-to-cycles conversion |
| certified-variables | 326 | serving cryptographically verified query responses with Merkle trees and BLS signatures |
| multi-canister | 325 | designing and deploying multi-canister dapps with inter-canister calls and the factory pattern |
| wallet-integration | 317 | integrating an external wallet signer via @icp-sdk/signer and the ICRC signer standards |
| evm-rpc | 310 | calling Ethereum and EVM chains from Rust canisters via the EVM RPC canister |
| ic-dashboard | 308 | querying the public dashboard.internetcomputer.org REST APIs for canister and ledger data |
| icrc-ledger | 304 | deploying and using ICRC-1 and ICRC-2 token ledgers for transfers, balances and allowances |
| ckbtc | 304 | accepting, sending and managing ckBTC with BTC deposit and withdrawal flows |
| sns-launch | 295 | configuring and launching an SNS DAO to decentralize a dapp |
| canhelp | 238 | showing a human-readable summary of a canister interface from its canister ID |
| custom-domains | 228 | registering custom domains for canisters via the HTTP gateway and DNS records |
| asset-canister | 228 | serving certified static frontends from the asset canister |
| deploy-to-cloud-engine | 213 | deploying a built project to a cloud engine such as OpenCloud |

The remaining 40 indexed listings range from 1 to 198 installs.

## Why This Matters for Hermes Agents

An agent that builds on the Internet Computer without these skills will quote wrong canister IDs, reach for deprecated APIs and miss the pitfalls that cost real cycles. Each skill is written for the agent rather than the human reader, so the exact library versions, tested code blocks and numbered pitfalls load directly into context. The highest-value skills for a builder are canister-security, which enforces access control, reentrancy prevention and upgrade safety before any state-changing canister ships, and stable-memory, which keeps data alive across upgrades with StableBTreeMap and MemoryManager. icp-cli is the entry point for project setup and deployment, and https-outcalls and evm-rpc cover the two outbound integration paths (external APIs and EVM chains). For operators the evaluation harness matters: every skill can carry an evaluation that compares agent output with and without the skill loaded, so the suite stays grounded in measurable correctness rather than prose.

## Usage

| You say | What happens |
|---|---|
| Build and deploy an IC canister | The icp-cli skill drives icp.yaml, recipes, identity and deployment |
| Make my canister hold tokens safely | The canister-security skill applies access control and reentrancy prevention |
| Persist state across upgrades | The stable-memory skill picks StableBTreeMap or a persistent actor |
| Call an external API from my canister | The https-outcalls skill sets up outcalls with consensus and cycle pricing |
| Send ckBTC | The ckbtc skill walks the BTC deposit, transfer and withdrawal flow |
| Decentralize my dapp | The sns-launch skill configures and submits the SNS DAO proposal |
| Fetch skills for any agent | The llms.txt discovery index points the agent at skills on demand |

## Verification

Confirm the CLI skill resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/dfinity/icskills/main/skills/icp-cli/SKILL.md | head -30
```

Confirm the persistence skill body is present before relying on it for upgrades:

```bash
curl -sL https://raw.githubusercontent.com/dfinity/icskills/main/skills/stable-memory/SKILL.md | head -30
```

Spot-check a domain skill to confirm the flat skills/ layout:

```bash
curl -sL https://raw.githubusercontent.com/dfinity/icskills/main/skills/ckbtc/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| icp-cli | Pass | Warn | Fail |
| canister-security | Pass | Pass | Pass |
| stable-memory | Pass | Pass | Pass |
| internet-identity | Pass | Pass | Pass |
| https-outcalls | Pass | Pass | Warn |
| cycles-management | Pass | Pass | Warn |
| certified-variables | Pass | Pass | Pass |
| multi-canister | Pass | Pass | Warn |
| wallet-integration | Pass | Pass | Warn |
| evm-rpc | Pass | Pass | Warn |
| ic-dashboard | Pass | Pass | Warn |
| icrc-ledger | Pass | Pass | Warn |
| ckbtc | Pass | Pass | Warn |
| sns-launch | Pass | Pass | Pass |
| canhelp | Pass | Warn | Warn |
| custom-domains | Pass | Pass | Warn |
| asset-canister | Pass | Pass | Warn |
| deploy-to-cloud-engine | Pass | Pass | Warn |
| vetkd | Pass | Pass | Pass |
| mops-cli | Pass | Pass | Warn |

The only Fail cell is Snyk on icp-cli; Warn cells are concentrated on Snyk across the integration skills plus Socket on icp-cli and canhelp, and 38 of the 58 indexed listings were outside the 20-skill sample.

## Limitations

- Snapshot data, verified Nov 23, 2026: 8,379 combined installs across 58 indexed listings; 40 GitHub stars; Apache-2.0 license; last pushed Nov 20, 2026. Counts drift over time.
- The README marks the project as under active development: skill files are still being reviewed and signed off by DFINITY engineers, and content may change.
- The install index outruns the tree in a few spots: internet-identity (345) and asset-canister (228) carry install counts but have no skills/<name>/ directory in the current tree, the index lists vetkd while the tree uses vetkeys, and the spaced listings ckBTC Integration and IC Dashboard APIs sit at 2 and 1 installs.
- Most implementation skills target Motoko and Rust canisters, and the icp CLI has replaced dfx for project workflows; the discovery index keeps legacy fields (files and hash) only so older installed sync scripts keep working.
- 38 of the 58 indexed listings carry no published skills.sh security verdict in the sampled set.

## Related

- [EthSkills - Ethereum Knowledge Base for Agents Setup](/hermes/skills/catalog/ethskills-setup)
- [Chainlink Agent Skills Setup Guide](/hermes/skills/catalog/chainlink-agent-skills-setup)
- [Hedera Skills - Hedera Web3 Dev Tools Setup](/hermes/skills/catalog/hedera-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Point any agent at the llms.txt index first for on-demand fetching before installing anything.
- npx skills add dfinity/icskills works across Claude Code, Cursor, Windsurf and Copilot.
- Start with icp-cli for project setup and canister-security before writing any state-changing canister code.
- Read the Common Pitfalls section before each canister change; every pitfall documented is a hallucination prevented.
- Run each skill's Verify It Works commands before trusting it, and prefer the per-skill evaluation files when you want a measured baseline.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
