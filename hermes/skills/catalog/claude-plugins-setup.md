---
title: "Claude Plugins (Bankr) - Web3 Development Toolkit"
description: "bankrbot/claude-plugins: 14.5K combined installs across 40 listings; Claude Code plugins for Web3 trading, transfers and onchain transactions."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-plugins-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "defi", "onchain", "web3", "claude code"]
---

# Claude Plugins (Bankr) - Setup Guide

**Source:** [bankrbot/claude-plugins](https://www.skills.sh/bankrbot/claude-plugins) via skills.sh - 14.5K combined installs across 40 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 88 stars, MIT license, `main` branch, last pushed 2026-03-24, three plugins (bankr-agent, bankr-agent-dev and bankr-x402-sdk-dev), 40 SKILL.md files across their `skills/` directories
**Category:** Web3 development plugins for Claude Code and other coding agents
**Quality Tier:** 🟠 Orange - skills.sh publishes no security verdicts for this publisher; the plugins build and sign onchain transactions against a Bankr API key.

Bankr publishes three Claude Code plugins that wrap its multi-chain DeFi API: bankr-agent for conversational trading and Polymarket, bankr-agent-dev as a developer toolkit for building on the Bankr Agent API, and bankr-x402-sdk-dev for the Bankr SDK. Between them the listings cover token transfers and swaps, portfolio and market reads, NFT operations, token deployment, leveraged trading and prediction markets, with x402 micropayments at $0.01 USDC per SDK request.

Only the skills are portable across tools. Agents, commands, hooks and the MCP server require Claude Code, so an install on Cursor, OpenCode or Gemini CLI via `bunx skills add` gets the SKILL.md files but not the bankr-agent MCP server or its `/bankr-agent` command.

## Installation

Add the marketplace, then install the plugin you want:

```bash
claude plugin marketplace add BankrBot/claude-plugins
```

```bash
# For bankr-agent (conversational trading and Polymarket)
claude plugin install bankr-agent@bankr-claude-plugins

# For bankr-agent-dev (developer toolkit)
claude plugin install bankr-agent-dev@bankr-claude-plugins

# For bankr-x402-sdk-dev (Web3 development SDK)
claude plugin install bankr-x402-sdk-dev@bankr-claude-plugins
```

For other coding tools, install only the skills:

```bash
bunx skills add BankrBot/claude-plugins
```

bankr-agent also ships an MCP server. Its README has you export the API key, then build the server with Bun:

```bash
export BANKR_API_KEY=bk_your_api_key_here
cd mcp-server
bun install
bun run build
```

Requirements are the Claude Code CLI, Node.js 20+ and USDC on Base for x402 payments.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| bankr-agent-transfers | 460 | Send or transfer tokens to wallets, ENS names and social handles. |
| bankr-x402-sdk-balance-queries | 407 | Read token balances, portfolio value and NFT holdings across chains with the Bankr SDK. |
| bankr-dev-nft-operations | 382 | Build NFT marketplace integrations with OpenSea browsing, floor prices and purchases. |
| bankr-dev-transfers | 381 | Build payment flows with token transfers and ENS or social handle resolution. |
| bankr-agent-job-workflow | 375 | Run the submit-poll-complete job pattern behind every Bankr API call. |
| bankr-dev-market-research | 374 | Build market data displays with prices, market caps, technical analysis and sentiment. |
| bankr-agent-nft-operations | 374 | Browse, buy and manage NFTs, including mints and listings. |
| bankr-dev-arbitrary-transactions | 371 | Submit raw EVM transactions and pre-built calldata through Bankr. |
| bankr-dev-token-trading | 370 | Build trading bots and swaps with cross-chain bridge support and ETH/WETH conversion. |
| bankr-agent-portfolio | 370 | Check balances and token holdings across chains. |
| bankr-agent-polymarket | 370 | Search Polymarket markets, check odds and place bets. |

The remaining 29 indexed listings range from 322 to 369 installs.

## Why This Matters for Hermes Agents

The three plugins map onto the two kinds of onchain work an agent does: bankr-agent answers in conversation, while bankr-agent-dev and bankr-x402-sdk-dev hand you the API patterns to build against. The transferable idea is the job model: every Bankr call is an asynchronous job you submit and then poll, so an agent that fires a trade and forgets it fails silently. Reading bankr-job-workflow before wiring anything is the difference between a script that polls for completion and one that assumes a synchronous response. The transfers and arbitrary-transaction skills document recipient resolution and raw calldata, the two places a funds-moving call most often goes wrong. If your agent touches money, start read-only with portfolio and market-research calls, confirm the key works, then enable anything that signs.

## Usage

| You say | What happens |
|---|---|
| "Add the Bankr marketplace" | Runs `claude plugin marketplace add BankrBot/claude-plugins`, making the three plugins installable. |
| "Install the trading agent" | Runs `claude plugin install bankr-agent@bankr-claude-plugins`. |
| "Buy $50 of BNKR on Base" | bankr-agent submits a Bankr API prompt and polls the job until the trade resolves. |
| "What are my balances across chains?" | bankr-portfolio reads balances and token holdings. |
| "What are the odds on this market?" | bankr-polymarket searches markets and returns the odds. |
| "Send 10 USDC to this wallet" | bankr-transfers resolves the recipient and submits the transfer. |
| "Install the skills in Cursor" | Runs `bunx skills add BankrBot/claude-plugins`; skills only, since agents, commands, hooks and the MCP server need Claude Code. |

## Verification

Probe two SKILL.md files on the `main` branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/BankrBot/claude-plugins/main/bankr-agent/skills/bankr-transfers/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/BankrBot/claude-plugins/main/x402-sdk-dev/skills/sdk-balance-queries/SKILL.md
```

Each SKILL.md opens with a `name` and a `description` naming its trigger phrases. The 40 skills are split across `bankr-agent/skills/`, `bankr-agent-dev/skills/` and `x402-sdk-dev/skills/`, one directory per listing.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use: skills.sh publishes no verdict for any of the 20 sampled Bankr listings; the Gen Agent Trust Hub, Socket and Snyk columns all return "not parsed" for every one, so this marketplace carries no third-party security signal.

The skills that build, sign or broadcast onchain transactions are bankr-transfers, bankr-arbitrary-transactions, bankr-sign-submit-api, bankr-token-trading, bankr-token-deployment, bankr-leverage-trading, bankr-nft-operations and bankr-polymarket, each in an agent and a dev variant, plus the SDK equivalents sdk-transaction-builder, sdk-token-swaps and sdk-wallet-operations. Every one of them runs against a Bankr API key. bankr-agent requires the key exported as `BANKR_API_KEY` (prefix `bk_`), issued from bankr.bot/api, and both the agent plugins and the MCP server authenticate against it. Set an explicit spending ceiling and require human approval before any skill that submits a transaction.

## Limitations

- Snapshot data, verified 2026-11-17: 14,547 combined installs across 40 indexed listings; 88 GitHub stars; MIT; last pushed 2026-03-24. Counts drift over time.
- The repository has not been pushed since 2026-03-24, months before this snapshot; confirm the live README before building against a moving API.
- Only the skills are portable. Agents, commands, hooks and the MCP server require Claude Code, so a `bunx skills add` install on other tools gets SKILL.md files only.
- Funds-moving skills need a Bankr API key and a funded wallet, and x402 SDK requests cost $0.01 USDC each; a looping agent can spend per call.
- Install counts in the table cluster tightly between 370 and 460; a narrow spread across sibling skills from one publisher is normal.
- skills.sh has parsed no verdict for this publisher, so treat the marketplace as unaudited until you review the skills yourself.

## Related

- [Bankr Skills - DeFi and Onchain Agent Toolkit](/hermes/skills/catalog/bankrbot-skills-setup)
- [Solana Dev Skill - Blockchain Development Setup](/hermes/skills/catalog/solana-dev-skill-setup)
- [Uniswap AI - DeFi Integration Skills Setup](/hermes/skills/catalog/uniswap-ai-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start read-only: portfolio, market-research and balance-queries calls cost nothing and prove the key works before you enable anything that signs.
- Read bankr-job-workflow first; a Bankr call that is not polled fails silently, and the job pattern is the same across the whole API.
- Install the plugin you need, not the marketplace; the three plugins are independent and pulling one is cheaper in context.
- Keep a separate wallet for agent work with a small balance, and require human approval on any transaction before the first one goes out.
- On non-Claude tools the MCP server does not come along with `bunx skills add`, so conversational trading stays Claude Code only.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
