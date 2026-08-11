---
title: Chainlink Agent Skills Setup Guide
description: Install and configure smartcontractkit/chainlink-agent-skills — official Chainlink oracle and CCIP skills for blockchain data access from Hermes Agent.
category: blockchain
publisher: smartcontractkit
maturity: production
source: https://github.com/smartcontractkit/chainlink-agent-skills
---

# Chainlink Agent Skills — Setup Guide

Official Chainlink oracle and Cross-Chain Interoperability Protocol (CCIP) skills by [smartcontractkit](https://github.com/smartcontractkit/chainlink-agent-skills). Production-grade blockchain data access for AI agents — price feeds, on-chain data queries, and cross-chain messaging.

## What It Provides

- **Price Feeds** — real-time asset prices from Chainlink Data Feeds
- **CCIP Messaging** — cross-chain message sending and receiving
- **Proof of Reserve** — verify collateralization of on-chain assets
- **Automation** — Chainlink Automation (formerly Keepers) for scheduled on-chain actions
- **Functions** — serverless compute for fetching off-chain data on-demand
- **VRF** — verifiable random numbers for gaming/NFT applications

## Installation

```bash
# Install via skills.sh
npx skills add https://github.com/smartcontractkit/chainlink-agent-skills

# Manual clone
git clone https://github.com/smartcontractkit/chainlink-agent-skills.git ~/.hermes/skills/chainlink
```

## Configuration

```yaml
chainlink:
  network: "ethereum-mainnet"    # or polygon, arbitrum, optimism, avalanche
  rpc_url: "${ETH_RPC_URL}"      # Your RPC endpoint (Alchemy, Infura, etc.)
  data_feeds:
    enabled: true
    default_pairs:
      - "ETH/USD"
      - "BTC/USD"
      - "LINK/USD"
  ccip:
    enabled: false               # Enable only if using cross-chain
    source_chain: "ethereum-mainnet"
    destination_chains:
      - "polygon-mainnet"
      - "arbitrum-mainnet"
  functions:
    enabled: false               # Requires Functions subscription
    subscription_id: "${CHAINLINK_SUBSCRIPTION_ID}"
```

## Key Workflows

### Query price feeds

```
What's the current ETH/USD price from Chainlink Data Feeds?
Compare BTC/USD across Ethereum and Polygon price feeds.
```

### Check proof of reserve

```
Verify the USDC reserve on Ethereum mainnet.
Is WBTC fully backed? Check the proof of reserve.
```

### Cross-chain messaging (CCIP)

```
Send a CCIP message from Ethereum to Polygon with payload: {"action": "sync_state"}
```

### Automation triggers

```
Set up a Chainlink Automation to check ETH price every hour.
If ETH drops below $2000, trigger an alert.
```

## Verification

```bash
# Test price feed
hermes chat -q "Get the current ETH/USD price from Chainlink"

# Test network connection
hermes chat -q "What's the latest block number on Ethereum mainnet?"
```

## Pitfalls

- **⚠️ RPC costs**: Ethereum mainnet RPC calls can be expensive. Use a reliable provider (Alchemy, Infura) with rate limits configured. Polygon/Arbitrum are cheaper for testing.
- **⚠️ Private key security**: NEVER store private keys in config files. Use environment variables or a hardware wallet. The skill only needs read access for price feeds — sending transactions requires explicit enable.
- **Gas fees**: CCIP messaging and Automation actions incur gas fees. Monitor costs carefully on mainnet.
- **Network congestion**: During high-traffic periods, RPC calls may timeout. Set appropriate retry and timeout values.
- **Data feed freshness**: Chainlink price feeds update based on deviation thresholds and heartbeat intervals. Prices may be up to 1 hour old for low-volatility assets.
- **Functions billing**: Chainlink Functions charges based on computation and DON (Decentralized Oracle Network) usage. Review the pricing model before enabling.

## See Also

- [smartcontractkit/chainlink-agent-skills repo](https://github.com/smartcontractkit/chainlink-agent-skills)
- [Chainlink Docs](https://docs.chain.link/)
- [Solana Setup](/hermes/skills/catalog/solana-setup/)

---

*Setup guide by CorpusIQ. Source: [smartcontractkit/chainlink-agent-skills](https://github.com/smartcontractkit/chainlink-agent-skills).*
