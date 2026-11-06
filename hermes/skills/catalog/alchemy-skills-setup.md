---
title: "Alchemy Skills - Blockchain API and MCP Setup"
description: "alchemyplatform/skills on skills.sh: 5.9K combined installs across 7 listings; Alchemy blockchain APIs for live agent queries, CLI, MCP and app code."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/alchemy-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "alchemy", "blockchain", "mcp"]
---

# Alchemy Skills - Setup Guide

**Source:** [alchemyplatform/skills](https://www.skills.sh/alchemyplatform/skills) via skills.sh - 5.9K combined installs across 7 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep, first documentation)
**GitHub:** 55 stars, MIT, last pushed 2026-11-03, 10 SKILL.md directories across `skills/` and a mirrored `plugins/alchemy/skills/` tree
**Category:** Blockchain APIs for agents: Alchemy live queries, CLI and MCP wiring plus application-code integration
**Quality Tier:** 🟡 Caution - alchemy-cli is Warned by both Socket and Snyk, and opensea and alchemy-codex each carry a Snyk Warn in the sampled audits; MIT, 55 stars.

Alchemy Skills is the vendor's own skill set, and it is organised around one question the README asks twice: is the agent doing live work in this session, or wiring Alchemy into code that ships? Live work routes to the CLI, or to the hosted MCP server when no CLI is installed. Code that ships routes to the API skill when there is an API key, and to the agentic gateway when there is not.

That routing is enforced in the files rather than left to the reader. Each SKILL.md carries "When to use this skill" and "When to use a different skill" sections, so an agent that lands on the wrong skill is told where to go. The README's decision tree is a mermaid flowchart over the same two questions, and the second table maps seven concrete situations, including the awkward one where app code has no API key but the CLI is installed, which resolves through `alchemy auth login`, `alchemy apps select` and `alchemy --reveal config get api-key`.

Four skills cover the core product surface and two more sit under `skills/ecosystem/` for partner data. Each source skill is self-contained, shipping a `SKILL.md`, a `LICENSE.txt` and `agents/openai.yaml` metadata for ecosystems that read it.

## Installation

The README recommends the CLI directly for live agent work:

```bash
npm i -g @alchemy/cli
alchemy auth login
```

The skills bundle installs through the skills CLI:

```bash
npx skills add alchemyplatform/skills --yes
```

The MCP route needs no local install at all. Add the hosted server `https://mcp.alchemy.com/mcp` to a client that supports remote MCP, and the client handles the OAuth flow. For Codex, the repository ships `scripts/install_codex_plugin.py`, which installs the bundled plugin into `~/plugins` and registers the `alchemy-skills` marketplace defined in `.agents/plugins/marketplace.json`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| alchemy-api | 1,676 | Wiring Alchemy into app code with an API key: JSON-RPC, Token, NFT, Transfers, Prices, Portfolio, Simulation, Webhooks, Solana and Sui |
| alchemy-mcp | 1,146 | Live blockchain queries and admin work through the hosted MCP server, 159 tools across 100+ chains, no local install |
| agentic-gateway | 1,046 | App integration without an API key: x402 or MPP gateway with SIWE and SIWS wallet auth and per-request USDC payments |
| alchemy-cli | 783 | Live agent work from the terminal: transaction lookups, NFT, token and portfolio queries, simulation, tracing, contract writes, swaps and bridges |
| allium | 650 | Wallet PnL, holdings history, Hyperliquid trading data and custom SQL across 70+ chains |
| opensea | 599 | OpenSea marketplace data and Seaport trades: listings, offers, sales, floor prices, collection stats and traits |

The remaining 1 indexed listing is alchemy-codex (47 installs), which carries no matching directory in the current tree.

## Why This Matters for Hermes Agents

Blockchain data work fails in a specific way for agents: the model knows the shape of an RPC call but not which endpoint, which chain identifier, or which product answers the question. The `alchemy-cli` skill is a mapping from every Alchemy product to a concrete `alchemy <command>` invocation with structured JSON output, so the agent reads a command instead of composing an HTTP request from memory.

The live-versus-shipping split is the useful part. An agent asked for a wallet balance right now should call the CLI or the MCP server; an agent asked to build a backend that reads balances should write code against the API skill with a key. Those are different tasks with different failure modes, and the repository states the rule once and then repeats it inside each skill.

The auth ladder is unusually complete for an autonomous agent. With a key, use the API. Without one, and with the CLI installed, fetch a key from the user's account. Without either, the agentic gateway lets the agent pay per request in USDC over x402, or by card through MPP, with SIWE or SIWS wallet auth. That is a documented path for an agent that has to buy its own access rather than ask a human for a secret.

The MCP path matters when the harness has no shell. A single hosted server with 159 tools across 100+ chains means a client-only agent still gets token prices, NFT metadata, transaction simulation and app administration, with OAuth handled by the client.

## Usage

| You say | What happens |
|---|---|
| "What is the floor price on this collection?" | Routes to alchemy-cli for live data, or opensea when the question is marketplace-specific |
| "Trace why this transaction reverted" | alchemy-cli simulation and tracing, with structured JSON output |
| "Add a webhook for transfers to this address" | alchemy-cli webhook management, or alchemy-api when the webhook belongs in shipped code |
| "Wire NFT metadata reads into my Node backend" | alchemy-api, with the API key path and the product endpoints for the job |
| "I have no API key, build it anyway" | agentic-gateway with x402 or MPP, wallet auth and per-request payment |
| "How much did this wallet make on Hyperliquid?" | allium wallet PnL and Hypercore trading data |
| "Sweep this wallet to another chain" | alchemy-cli wallet-signed sends and cross-chain bridges |

## Verification

Read the skill the agent will actually load before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/alchemyplatform/skills/main/skills/alchemy-cli/SKILL.md | head -6
```

It should open with `name: alchemy-cli` and a description naming `@alchemy/cli`, live queries and app-code routing. Then confirm the CLI is authenticated and knows your app:

```bash
alchemy auth login
alchemy apps select
```

For the MCP route, ask the client to list tools after connecting to `https://mcp.alchemy.com/mcp`. The README's claim is 159 tools across 100+ chains, so a much smaller list means the server connected with a restricted scope or the client truncated the tool table.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| alchemy-api | Pass | Pass | Pass |
| alchemy-mcp | Pass | Pass | Pass |
| alchemy-cli | Pass | Warn | Warn |
| opensea | Pass | Pass | Warn |
| alchemy-codex | Pass | Pass | Warn |

The tree is markdown and reference files, so the audit surface is the tooling the skills drive: a global npm CLI, a hosted MCP endpoint and an RPC provider. Two operational cautions follow from the README's own commands. `alchemy --reveal config get api-key` prints the key into the terminal, and therefore into a transcript if an agent runs it, so route that step through a human or a secret store. The agentic gateway spends real USDC per request from a funded wallet, which deserves a spending limit before an autonomous loop touches it. The agentic-gateway skill carries an explicit notice that the repository is experimental and subject to change.

## Limitations

- Snapshot data, verified 2026-11-05: 5,947 combined installs across 7 indexed listings; 55 GitHub stars; MIT; last pushed 2026-11-03. Counts drift over time.
- The install index outruns the tree: alchemy-codex carries 47 installs and has no matching directory under `skills/`, `skills/ecosystem/` or `plugins/alchemy/skills/`.
- Four skills are duplicated across `skills/` and `plugins/alchemy/skills/`. Which copy an installer picks depends on the client, so a stale edit in one tree can be the file your agent loads.
- The ecosystem skills need their own credentials: allium wants `~/.allium/credentials` with `API_KEY` and `QUERY_ID`, opensea wants `OPENSEA_API_KEY`. Neither is covered by the Alchemy login.
- The 159-tool MCP claim and the 100+ chain coverage are the README's figures, not something this guide measured.
- Low star count for a vendor repository. Adoption here is early, so expect churn in the routing text that decides which skill an agent picks.

## Related

- [Coinbase Agentic Wallet - USDC Payments Skill](/hermes/skills/catalog/coinbase-agentic-wallet-setup)
- [Solana Dev Skill - Official Blockchain Development](/hermes/skills/catalog/solana-dev-skill-setup)
- [Chainlink Agent Skills Setup Guide](/hermes/skills/catalog/chainlink-agent-skills-setup)

## Pro Tips

- Decide live versus shipping before the first call. The wrong branch here means the agent either builds throwaway scripts or ships code with no key.
- Install the CLI even if you plan to use MCP. The README makes the CLI the preferred local path and the MCP the fallback when no CLI exists.
- Keep the reveal step out of agent reach. Fetching an API key should be a human action, not a tool call in a loop.
- Cap the gateway wallet. Per-request USDC pricing plus an autonomous retry loop is an unbounded spend unless you bound it.
- Tell the agent which chain up front. Every product skill branches on chain, and naming it removes a clarifying round trip.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
