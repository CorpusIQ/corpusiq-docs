---
title: "Circle Skills - USDC and Arc Payments Setup"
description: "circlefin/skills on skills.sh: 15.9K combined installs across 20 listings; USDC payments, wallets, Gateway and smart contracts for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/circlefin-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "usdc", "stablecoins", "payments"]
---

# Circle Skills - Setup Guide

**Source:** [circlefin/skills](https://www.skills.sh/circlefin/skills) via skills.sh - 15.9K combined installs across 20 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 162 stars, Apache-2.0 licence, last pushed 2026-10-16, 19 SKILL.md directories under plugins/circle/skills/
**Category:** Stablecoin payments for agents: USDC transfers, Arc, wallet types, Gateway, swaps and smart contracts
**Quality Tier:** 🟡 Beta - Snyk Warn on every sampled payments skill; Apache-2.0; 162 stars.

Circle's own skills repository ships best-practice guidance for USDC payments, crosschain transfers, wallets and smart contracts, plus a pointer to Circle's MCP server for live SDK and documentation context. Nineteen skill directories sit under `plugins/circle/skills/` and install as a single plugin, `circle-skills`, published in the `circle` marketplace.

The split is task-shaped rather than API-shaped. There is one skill per surface an agent is asked to touch: send USDC, deploy a contract, bridge a balance, compare wallet custody models, or drive the `circle` CLI. That means the agent loads a short playbook for the job in front of it instead of a general payments manual.

## Installation

The README documents two routes. Claude Code installs the marketplace, then the plugin:

```
/plugin marketplace add circlefin/skills
```

```
/plugin install circle-skills@circle
```

Any other agent can use the skills.sh CLI:

```bash
npx skills add circlefin/skills
```

Both pull the same 19 skill directories. Skills installed through the plugin route are namespaced, so the USDC skill is reached as part of `circle-skills` rather than as a bare `use-usdc` command.

## What It Provides

Sixteen listings clear the 500 install threshold.

| Skill | Installs | Use For |
|---|---|---|
| use-usdc | 1,059 | Checking balances, sending transfers, approving spenders and verifying transactions on EVM chains and Solana |
| use-arc | 1,049 | Building on Arc, where USDC is the native gas token, including chain config, contract deployment and CCTP bridging |
| use-developer-controlled-wallets | 1,007 | Custodial wallet sets for payouts, treasury and automation, where the application holds keys |
| use-smart-contract-platform | 999 | Deploying bytecode, importing contracts, using ERC-20/721/1155 templates, ABI read and write calls, and event monitoring |
| use-gateway | 990 | Holding one unified USDC balance across chains and moving it in under 500ms through deposit, burn and mint |
| use-circle-wallets | 989 | Choosing between developer-controlled, user-controlled and modular wallets before writing integration code |
| use-modular-wallets | 986 | Passkey (WebAuthn) wallets with gasless transactions and ERC-4337 account abstraction |
| use-user-controlled-wallets | 984 | Non-custodial embedded wallets with Google, Apple, Facebook, email OTP or PIN login and MPC key management |
| bridge-stablecoin | 924 | Crosschain stablecoin transfers; described at name level only in this snapshot |
| swap-tokens | 882 | Same-chain and cross-chain token swaps with estimates, slippage and status polling |
| use-agent-wallet | 839 | Standing up the programmatic USDC wallet an AI agent uses to authenticate and pay for x402 services |
| use-circle-cli | 838 | Driving the `@circle-fin/cli` command surface: wallet, bridge, gateway, services, contract and transaction |
| unify-balance | 838 | Unified cross-chain balance in browser or server apps through Unified Balance Kit or App Kit |
| pay-via-agent-wallet | 835 | Calling a paid API or data service with automatic USDC payment from the agent wallet |
| fund-agent-wallet | 831 | Funding an agent wallet by fiat on-ramp or by transfer, with no ETH needed for gas |
| agent-wallet-policy | 825 | Reading the per-transaction, daily, weekly and monthly USDC caps on an agent wallet |

The remaining 4 indexed listings range from 87 to 483 installs.

## Why This Matters for Hermes Agents

Payments are the cleanest example of a capability an agent cannot improvise. Amounts, decimals, approvals and chain IDs are exactly the details a language model gets subtly wrong, and a mistaken approval is not recoverable by retrying.

This pack encodes those details as procedures: `use-usdc` works in base units and six decimals, `use-gateway` states the under-500ms transfer path, `agent-wallet-policy` exposes the caps a human set, and the agent reads a checklist instead of reconstructing a transaction from memory.

The agent-wallet cluster is the part worth studying if you build tool-using agents. `use-agent-wallet` creates a wallet an agent owns, `fund-agent-wallet` puts USDC in it, `pay-via-agent-wallet` spends it on x402 services, and `agent-wallet-policy` bounds the damage. That is a complete loop for machine-to-machine purchasing, with a spend limit as the safety rail.

Finally, `use-circle-cli` doubles as a rescue path, telling the agent to reach for the CLI when it believes it cannot do something onchain, which is a useful pattern for any skill pack that wraps a command line tool.

## Usage

| You say | What happens |
|---|---|
| "Send 20 USDC to this address on Base" | use-usdc checks the chain, formats base units and verifies the transaction after sending |
| "Give my agent a wallet it can spend from" | use-agent-wallet sets up the CLI wallet, then fund-agent-wallet moves USDC into it |
| "What are my agent wallet limits?" | agent-wallet-policy reads the per-transaction, daily, weekly and monthly caps |
| "Charge for this API endpoint in USDC" | accept-agent-payments wires x402 pay-per-call with Gateway Nanopayments as the default |
| "Should I use developer-controlled or passkey wallets?" | use-circle-wallets compares custody model, key management and blockchain support |
| "Move USDC from Ethereum to Arc" | use-arc guides the CCTP bridge and chain configuration on the destination |
| "Deploy an ERC-20 and watch its events" | use-smart-contract-platform deploys from a template and registers webhook monitoring |

## Verification

Fetch one skill and confirm the frontmatter names the skill and its chains:

```bash
curl -fsSL https://raw.githubusercontent.com/circlefin/skills/master/plugins/circle/skills/use-usdc/SKILL.md | head -8
```

The response should start with `name: use-usdc` and a description naming EVM chains and Solana. If you installed through the skills.sh CLI, confirm the skill directories landed:

```bash
ls ~/.claude/skills
```

Inside Claude Code, `/plugin` lists installed marketplaces and plugins, and `circle-skills` should appear there with its skill list.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| use-usdc | Pass | Pass | Warn |
| use-arc | Pass | Pass | Warn |
| use-developer-controlled-wallets | Pass | Pass | Warn |
| use-agent-wallet | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified 2026-11-04: 15,869 combined installs across 20 indexed listings; 162 GitHub stars; Apache-2.0; last pushed 2026-10-16. Counts drift over time.
- skills.sh indexes 20 listings while the repo tree holds 19 skill directories, so listing names and directory names do not map one to one.
- The `bridge-stablecoin` row is described at name level only: the pack carries no SKILL.md description for it, and the repo directory list shows `bridge-tokens`, so confirm the current name before scripting around it.
- Four listings sit below the threshold (87 to 483 installs), including seller-side skills such as `accept-agent-payments` and `buy-crypto`; read those SKILL.md files directly before wiring them in.
- Every sampled skill carries a Snyk Warn. Wallets hold funds and developer-controlled flows register an entity secret, so treat that secret as a credential and test on testnet before mainnet.
- Setting spending limits requires OTP confirmation in an interactive terminal session, so a fully headless agent can read policy but not change it.

## Related

- [Coinbase Agentic Wallet - USDC Payments Skill](/hermes/skills/catalog/coinbase-agentic-wallet-setup)
- [OKX OnchainOS Skills - Wallet & DEX Setup](/hermes/skills/catalog/okx-onchainos-skills-setup)
- [Solana Mobile Skills - Android Wallet Dev Setup](/hermes/skills/catalog/solana-mobile-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start at `use-circle-cli` when the request is vague. It maps the command surface and routes to the narrower wallet skills, which is cheaper than loading all nineteen.
- Ask for the chain before any bridge or swap call. The same token has different contracts per chain, and the skills key off the chain name rather than guessing it.
- Keep `agent-wallet-policy` caps low while you are developing. A per-transaction cap is the only guardrail that survives a model mistake inside a payment loop.
- Treat `buy-crypto` as two configurations, sandbox and production. The README calls out widget-origin matching and CSP, which are the two failure modes of an embedded onramp.
- Read the installed SKILL.md rather than relying on the summary here. Circle SDK surfaces change often and the repo was last pushed in October 2026.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
