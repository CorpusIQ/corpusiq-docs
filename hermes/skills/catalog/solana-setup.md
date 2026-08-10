---
title: Solana Blockchain — Full Setup Guide for Hermes Agents
description: Query Solana on-chain data with USD pricing via CoinGecko. 8 commands for wallet portfolios, tokens, transactions, NFTs, whale detection, network stats, and price lookup. No API key needed.
---

# Solana Blockchain — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (227.9K⭐)
**Skill:** `nousresearch/hermes-agent@solana`
**Installs:** 14
**Category:** Blockchain / Web3
**First Seen:** Apr 4, 2026

Query Solana on-chain data enriched with USD pricing via CoinGecko. 8 commands covering wallet portfolios, token info, transactions, activity, NFTs, whale detection, network stats, and price lookups. Uses only Python standard library — no API key needed.

---

## Installation

```bash
npx skills add nousresearch/hermes-agent@solana
```

Or install from the Hermes Agent monorepo:

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill solana
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python 3** | For all scripts (stdlib only — `urllib`, `json`, `argparse`) |
| **Hermes Agent** | Any version |
| **No API key** | All queries run against public RPC endpoints + CoinGecko free tier |

---

## What It Provides

### 8 Built-In Commands

| Command | Description |
|---|---|
| `wallet` | Full wallet portfolio: SOL balance, token holdings with USD values |
| `token` | Detailed token information: price, market cap, supply, metadata |
| `transactions` | Recent transaction history for a wallet address |
| `activity` | Account activity summary: first/last transaction, volume, interactions |
| `nfts` | NFT holdings for a wallet: collection names, floor prices |
| `whales` | Whale detection: largest holders of a token or recent large transfers |
| `network` | Solana network stats: TPS, epoch, validators, fees |
| `price` | Quick price lookup for any token via CoinGecko |

### Architecture

All commands use Python standard library only (`urllib`, `json`, `argparse`). No external dependencies. Queries hit public Solana RPC endpoints and the CoinGecko free API. Rate-limited to respect public endpoints.

---

## Quick Start

```bash
# 1. Install
npx skills add nousresearch/hermes-agent@solana

# 2. Check network status
python3 <skill-dir>/scripts/solana_cli.py network

# 3. Look up a wallet portfolio
python3 <skill-dir>/scripts/solana_cli.py wallet <SOLANA_ADDRESS>

# 4. Get SOL price
python3 <skill-dir>/scripts/solana_cli.py price SOL

# 5. Check a token
python3 <skill-dir>/scripts/solana_cli.py token <TOKEN_MINT_ADDRESS>
```

---

## Usage Patterns

### Portfolio Tracking

```bash
# Save portfolio snapshot
python3 solana_cli.py wallet YOUR_ADDRESS > portfolio_$(date +%Y%m%d).json
```

### Whale Alert Monitoring

```bash
# Check for large SOL transfers (>1000 SOL)
python3 solana_cli.py whales --token SOL --threshold 1000
```

### NFT Collection Analysis

```bash
# List NFTs with floor prices
python3 solana_cli.py nfts YOUR_ADDRESS
```

---

## Limitations

- **Public RPC rate limits:** The free Solana RPC endpoints have rate limits. For production use, consider a dedicated RPC (Helius, QuickNode, etc.).
- **No write operations:** Read-only. Cannot send transactions, mint tokens, or interact with smart contracts.
- **CoinGecko free tier:** ~30 requests/minute. Cached responses for frequently queried tokens.

---

## Verification

After installation, verify the commands work:

```bash
# Test network connectivity
python3 <skill-dir>/scripts/solana_cli.py network

# Test price lookup
python3 <skill-dir>/scripts/solana_cli.py price SOL
```

Expected output for network: `TPS: 3,245 | Epoch: 624 | Validators: 1,987 | Avg Fee: 0.000005 SOL`

---

## Security

- [Gen Agent Trust Hub: Pass](https://www.skills.sh/nousresearch/hermes-agent/solana/security/agent-trust-hub)
- [Socket: Pass](https://www.skills.sh/nousresearch/hermes-agent/solana/security/socket)
- [Snyk: Pass](https://www.skills.sh/nousresearch/hermes-agent/solana/security/snyk)

**All three audits passed.** No external dependencies beyond Python stdlib.

---

**Related:** [hermes-agent-framework-setup.md](hermes-agent-framework-setup.md)
