---
title: "Mysten Labs Skills - Sui Move Development Setup"
description: "mystenlabs/skills: Sui Move development skills maintained by Mysten Labs - 12.9K combined installs across 33 indexed listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mystenlabs-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "sui", "move", "blockchain"]
---

# Mysten Labs Skills - Sui Move Development Setup

**Source:** [mystenlabs/skills](https://www.skills.sh/mystenlabs/skills) via skills.sh - 12.9K combined installs across 33 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [mystenlabs/skills](https://github.com/mystenlabs/skills) - 25 stars, Apache-2.0 license, main branch, last pushed Nov 22, 2026; each skill is a directory at the repo root holding a SKILL.md plus supporting reference files, with scripts/ and suievals/ at the root for the eval runners and the public evals board.
**Category:** Blockchain and Move Smart Contract Development
**Quality Tier:** 🟠 Orange - two of the 20 sampled skills carry Fail cells: accessing-data fails Gen Agent Trust Hub and generate-sui-agent-config fails Snyk, with Snyk Warns on most of the remaining sample.

Mysten Labs is the company behind Sui, a Move-based Layer 1 blockchain built around an object-centric data model. This repository is the official agent-skills suite for building on Sui, spanning the whole lifecycle: Move smart contract development, project setup and testing, security review, the Sui CLI and SDKs, browser dApps, DeepBook trading, Walrus Sites hosting, and zkLogin. Install happens through the skills CLI (`npx skills add mystenlabs/skills --list` to browse, `--skill <name>` for a single skill), with an optional Sui docs MCP server for live documentation answers.

The install index carries 33 listings while the tree ships 31 top-level skill directories, and a few index names drift from the directories: sui-object-model maps to object-model, and sui-build maps to sui-build-test. One indexed listing, your-skill-name, is the contributing template placeholder rather than a shipped skill. The README recommends a three-skill starter set (sui-overview, sui-move, sui-move-project) and warns that installing all 31 skills adds real context overhead and can cause trigger collisions.

## Installation

Install through the skills CLI. Browse the available skills first:

```bash
npx skills add mystenlabs/skills --list
```

Then install a single skill, the recommended starter set, or everything:

```bash
# Install one skill
npx skills add mystenlabs/skills --skill sui-move

# Recommended starter set for new developers
npx skills add mystenlabs/skills --skill sui-overview --skill sui-move --skill sui-move-project

# Install all skills
npx skills add mystenlabs/skills --all
```

For answers from the current Sui docs while you work, connect the Sui docs MCP server:

```bash
claude mcp add --transport http sui-docs https://sui.mcp.kapa.ai
```

The skills run in whichever agent reads the SKILL.md files; there is no daemon or plugin manifest to wire. The README notes that installing all 31 skills adds real context overhead and can cause trigger collisions, so the starter set is the intended default.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sui-move | 667 | Sui Move smart contract development: abilities, TxContext, init, One-Time Witness, publishing and upgrades, events and coins |
| naming-conventions | 655 | Naming rules for Move contracts: error constants, events, capability structs, getters, hot potatoes, dynamic field keys |
| sui-move-project | 654 | Move project setup: Move.toml, dependency and build errors, the sui-stack-hello-world starter, MVR dependencies |
| sui-object-model | 651 | Ownership types, dynamic fields, collections and transfer patterns; index name for the tree's object-model directory |
| composable-move-functions | 650 | Function visibility (public vs entry), parameter ordering and return patterns for Move functions |
| move-unit-testing | 649 | Unit tests for Move contracts: naming, assertions, test attributes, context usage and cleanup |
| sui-build | 647 | Building Move code with sui move build; index name for the tree's sui-build-test directory |
| modern-move-syntax | 647 | Move 2024 edition syntax: method calls, string literals, vector ops, option handling, loops, struct unpacking |
| ptbs | 506 | Programmable Transaction Blocks: composing multiple Sui transaction commands into one atomic transaction |
| accessing-data | 506 | Reading on-chain state: gRPC, GraphQL RPC, the Archival Store, a sui-indexer-alt pipeline or Walrus |
| sui-sdks | 502 | Which SDK to pick (TypeScript, Rust, Python, Go, Dart, Kotlin, Swift) and how each one wires up |
| frontend-apps | 494 | Sui browser dApps with dapp-kit-react and dapp-kit-core: wallet connect, balances, signing and gas sponsorship |
| walrus-sites | 481 | Publishing, updating and serving decentralized websites on Walrus Sites |
| sui-client | 417 | Sui CLI client configuration, address management, faucet tokens and network switching |
| move-security | 415 | Auditing and hardening Move contracts: access control, capabilities, randomness, upgrade governance, key custody |
| sui-overview | 414 | High-level overview of Sui, the object model and the Sui Stack primitives |
| sui-publish | 413 | Publishing, upgrading and deploying Move packages across networks, with localnet and multisig flows |
| sui-install | 407 | Installing, updating and switching Sui CLI versions with suiup |
| generate-sui-agent-config | 405 | Current dApp Kit APIs and generating a CLAUDE.md or AGENT.md config for Sui projects |

The remaining 14 indexed listings range from 173 to 263 installs.

## Why This Matters for Hermes Agents

The Move skills encode compiler-backed rules and conventions, so an agent writing Sui code gets the object model, abilities, One-Time Witness and 2024 edition syntax right instead of emitting legacy patterns. The skill split mirrors the real separation of concerns in a Sui project: sui-move covers the language, sui-move-project the Move.toml setup, and sui-object-model the ownership, dynamic-field and transfer rules. The repository also ships its own eval harness, suievals, that scores agent answers with and without the skills loaded, so the quality claim is measured rather than asserted. The README itself warns against installing the full set at once because of context overhead and trigger collisions, and recommends a three-skill starter set. For operators, the caveats are the two Fail security cells in the sample and the name drift between the install index and the tree.

## Usage

| You say | What happens |
|---|---|
| Create a Sui Move project | Sets up Move.toml and the canonical sui-stack-hello-world starter with MVR dependencies |
| Write a Move module | Applies Sui Move abilities, TxContext, init and One-Time Witness patterns plus 2024 edition syntax |
| Publish the package to testnet | Walks through sui client publish, upgrade policies and UpgradeCap handling |
| Connect a wallet in my React app | Wires @mysten/dapp-kit-react with a ConnectButton, balance reads and transaction signing |
| Read on-chain balances and objects | Chooses gRPC, GraphQL RPC, an indexer or Walrus for the right data surface |
| Review my Move contract for security | Applies access control, capability, randomness and upgrade-governance checks |

## Verification

Confirm the core skill landed and read its routing before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/mystenlabs/skills/main/sui-move/SKILL.md | head -40
```

Check the naming conventions and object model skills:

```bash
curl -sL https://raw.githubusercontent.com/mystenlabs/skills/main/naming-conventions/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/mystenlabs/skills/main/object-model/SKILL.md | head -40
```

Verify the project-setup skill:

```bash
curl -sL https://raw.githubusercontent.com/mystenlabs/skills/main/sui-move-project/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sui-move | Pass | Pass | Warn |
| naming-conventions | Pass | Pass | Pass |
| sui-move-project | Pass | Pass | Pass |
| sui-object-model | Pass | Pass | Warn |
| composable-move-functions | Pass | Pass | Warn |
| move-unit-testing | Pass | Pass | Warn |
| sui-build | Pass | Pass | Pass |
| modern-move-syntax | Pass | Pass | Warn |
| ptbs | Pass | Pass | Warn |
| accessing-data | Fail | Pass | Warn |
| sui-sdks | Pass | Pass | Warn |
| frontend-apps | Pass | Pass | Warn |
| walrus-sites | Pass | Pass | Warn |
| sui-client | Pass | Pass | Warn |
| move-security | Pass | Pass | Pass |
| sui-overview | Pass | Pass | Warn |
| sui-publish | Pass | Pass | Warn |
| sui-install | Pass | Pass | Pass |
| generate-sui-agent-config | Pass | Pass | Fail |
| your-skill-name | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 22, 2026: 12.9K combined installs across 33 indexed listings; 25 GitHub stars; Apache-2.0 license; last pushed Nov 22, 2026. Counts drift over time.
- Index-vs-tree name drift: the index names sui-object-model and sui-build map to the tree's object-model and sui-build-test directories, and sui-cli has no directory in the tree (sui-client is the likely counterpart).
- One indexed listing, your-skill-name (263 installs), is the contributing template placeholder rather than a shipped skill.
- Two of the 20 sampled skills carry Fail cells: accessing-data on Gen Agent Trust Hub and generate-sui-agent-config on Snyk; the Snyk Warns across most of the sample are scanner-flagged, not confirmed vulnerabilities.
- The install counts concentrate in the core Move skills, while the DeepBook, Walrus, bridge and kiosk skills sit in a long niche tail.

## Related

- [Alchemy Skills - Blockchain API and MCP Setup](/hermes/skills/catalog/alchemy-skills-setup)
- [OKX OnchainOS Skills - Wallet & DEX Setup](/hermes/skills/catalog/okx-onchainos-skills-setup)
- [GMGN Agent Skills - On-Chain Analytics and Trading Setup](/hermes/skills/catalog/gmgn-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the three-skill starter set (sui-overview, sui-move, sui-move-project); installing all 31 skills adds real context overhead and can cause trigger collisions.
- Use sui-move for language rules and sui-move-project for Move.toml setup; they answer different failure modes.
- Fetch the SKILL.md routing before trusting a name: the index names sui-object-model and sui-build map to the tree's object-model and sui-build-test directories.
- Pair the skills with the Sui docs MCP server (sui.mcp.kapa.ai) for current documentation while you work.
- Re-check the security pages on skills.sh before production use; accessing-data and generate-sui-agent-config carry Fail cells in the sample.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
