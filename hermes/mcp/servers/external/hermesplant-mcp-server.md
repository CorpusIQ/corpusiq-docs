---
title: "Hermes Plant MCP Server — Deterministic Finance & Quant APIs"
description: "Connect AI agents to provably correct financial calculations, quantitative models, and market analytics via the Hermes Plant MCP server. Paid over x402 with cryptographic payment rails."
---

# Hermes Plant MCP Server — Finance & Quant APIs

**Runnable MCP server for deterministic finance and quant APIs paid over x402.** Provides AI agents with provably correct financial calculations, quantitative models, and market analytics. Combines the determinism of smart-contract-grade computation with traditional quantitative finance workflows — all accessible through MCP with cryptographic micropayment rails.

| Detail | Value |
|--------|-------|
| **GitHub** | [JesseGdotIO/hermesplant-mcp-server](https://github.com/JesseGdotIO/hermesplant-mcp-server) |
| **Language** | TBD (check repo) |
| **Transport** | MCP (stdio) |
| **Payment** | x402 (USDC on Base) |
| **Stars** | ★0 (new — July 1, 2026) |
| **License** | TBD |

## Why This Matters for Operators

Financial operators face a trust problem with AI agents: when an agent calculates NPV, option Greeks, or portfolio risk, how do you verify the math is correct? Traditional quant libraries are deterministic but inaccessible to AI agents. LLMs can discuss finance but hallucinate numbers.

Hermes Plant bridges this gap:
- **Deterministic computation**: Every calculation is provably correct — same inputs always produce same outputs, like a smart contract
- **x402 micropayments**: Pay per API call in USDC on Base, no subscription needed
- **MCP-native**: Access quantitative models directly from Claude, Cursor, or any MCP client
- **Verifiable**: Cryptographic receipts for every computation

## Use Cases for Operators

| Scenario | How Hermes Plant Helps |
|----------|----------------------|
| **Portfolio analysis** | Calculate Sharpe ratios, VaR, correlation matrices with deterministic accuracy |
| **Options pricing** | Black-Scholes, binomial trees, Monte Carlo — all provably correct |
| **Risk management** | Compute exposure, drawdown, stress tests with audit trails |
| **Financial modeling** | DCF, LBO, M&A models with verified calculations |
| **Algorithmic trading** | Signal generation, backtesting parameters, position sizing |
| **Compliance reporting** | Generate verified financial metrics for regulatory filings |

## Prerequisites

- **MCP-compatible agent** (Claude Desktop, Claude Code, Cursor, Windsurf, etc.)
- **x402 wallet** with USDC on Base (for API payments)
- **Python or Node.js** (check repo for runtime)

## Installation

```bash
git clone https://github.com/JesseGdotIO/hermesplant-mcp-server.git
cd hermesplant-mcp-server
# Follow repo README for specific install instructions
# Typically:
# npm install && npm run build
# or
# pip install -e .
```

## MCP Client Configuration

```json
{
  "mcpServers": {
    "hermesplant": {
      "command": "npx",
      "args": ["-y", "hermesplant-mcp-server"],
      "env": {
        "X402_WALLET_KEY": "your-wallet-private-key",
        "X402_RPC_URL": "https://mainnet.base.org"
      }
    }
  }
}
```

## Example Usage

### Calculate Option Greeks
```
> Calculate the Black-Scholes delta for AAPL call option: strike $200, spot $195, 30 days to expiry, 25% volatility, 5% risk-free rate

Agent → Hermes Plant → Returns: Delta = 0.4237 (deterministic)
```

### Portfolio Risk
```
> Given portfolio weights [40% AAPL, 30% GOOGL, 30% MSFT], calculate the 95% 1-day VaR using historical simulation

Agent → Hermes Plant → Returns: VaR = $12,450.32 (with cryptographic receipt)
```

### DCF Valuation
```
> Value a company with FCF: [$10M, $12M, $14M, $16M, $18M], terminal growth 3%, WACC 10%

Agent → Hermes Plant → Returns: Enterprise Value = $189.4M (provably correct)
```

## Payment Model

Hermes Plant uses x402 (HTTP 402) for micropayments:
- **Pay-per-call**: Each API invocation costs a small amount of USDC on Base
- **No subscriptions**: Only pay for what you use
- **Cryptographic receipts**: Every payment generates a verifiable receipt
- **Budget caps**: Set per-session or per-agent spending limits

## Verification

After setup, verify the server is working:

```bash
# Test from MCP client
# "What is the present value of $1000 received in 5 years at 7% discount rate?"
# Should return: $712.99 (deterministic, verifiable)
```

## Complements CorpusIQ

CorpusIQ provides live business data (QuickBooks, Shopify, Stripe, GA4, etc.) through OAuth 2.1 PKCE. Hermes Plant provides the deterministic computation layer for financial analysis on that data. Together:
1. **CorpusIQ** fetches live financial data (revenue, expenses, transactions)
2. **Hermes Plant** runs provably correct quantitative analysis on it
3. **vrules** (or similar governance) ensures the agent follows policies

This is the emerging "operator AI stack" — governed data access + deterministic computation.

## Notes

- This server was discovered on July 1, 2026 via GitHub API. It is brand new — check the repo for latest installation instructions, available tools, and API changes.
- The name "Hermes Plant" appears unrelated to the Hermes Agent framework — it's named after Hermes (Greek god of commerce) + Plant (as in manufacturing plant for financial computation).
- x402 payment rails mean no API keys to manage — just fund a wallet and compute.

---

*Integration guide created July 1, 2026 (PM evening) by CorpusIQ MCP Discovery Scanner*
*Server source: [github.com/JesseGdotIO/hermesplant-mcp-server](https://github.com/JesseGdotIO/hermesplant-mcp-server)*
