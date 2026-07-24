---
title: "Gainium MCP — AI-Powered Crypto Trading Automation"
description: "Open-source crypto trading automation platform with MCP integration. Build, test, and automate trading strategies without coding. Multi-exchange support with Docker Compose deployment."
category: mcp
tags: [mcp, finance, trading, crypto, automation, gainium, docker, hermes-agent]
github: https://github.com/Gainium/docker-sh
stars: 4
verified: true
source: mcp.so
discovered: 2026-07-24
pricing: Free · Open Source (Apache 2.0)
---

# Gainium MCP — AI-Powered Crypto Trading Automation

**Gainium** is an AI-powered, open-source crypto trading automation platform that enables traders to build, test, and automate trading strategies without coding. It supports multiple cryptocurrency exchanges and provides powerful tools for developing, validating, and deploying automated trading strategies.

The MCP integration lets AI agents interact with the Gainium trading platform — querying markets, managing strategies, and monitoring portfolio performance — all through a standardized protocol.

## What It Does

- **No-code strategy builder**: Visual strategy creation with drag-and-drop components
- **Multi-exchange support**: Connect to Binance, Coinbase, Kraken, and other major exchanges
- **Backtesting engine**: Validate strategies against historical data before deploying live
- **Docker Compose deployment**: Full stack (microservices, databases, frontend) in one command
- **AI agent integration**: MCP tools let agents monitor, analyze, and manage trading operations
- **Strategy marketplace**: Community-contributed strategies for discovery and reuse

## Key Tools

| Tool | Description |
|------|-------------|
| `gainium_market_data` | Fetch real-time and historical price data across exchanges |
| `gainium_portfolio` | View current holdings, P&L, and allocation |
| `gainium_list_strategies` | List active and paused trading strategies |
| `gainium_deploy_strategy` | Activate a strategy (requires confirmation for live trading) |
| `gainium_backtest` | Run a strategy against historical data |
| `gainium_alerts` | Check triggered alerts and notifications |

## Quick Start

### 1. Deploy with Docker Compose

```bash
git clone https://github.com/Gainium/docker-sh
cd docker-sh
docker compose up -d
```

This spins up the full stack: API server, strategy engine, database, Redis, and frontend.

### 2. Configure Your MCP Client

```json
{
  "mcpServers": {
    "gainium": {
      "command": "docker",
      "args": ["exec", "-i", "gainium-mcp", "node", "/app/mcp-server.js"],
      "env": {
        "GAINIUM_API_URL": "http://localhost:3001",
        "GAINIUM_API_KEY": "your-api-key"
      }
    }
  }
}
```

### 3. First Interaction

Once connected, agents can:
- "Show me my portfolio allocation across exchanges"
- "Backtest the momentum strategy against the last 90 days of BTC/USDT"
- "What's the 24h volume on ETH/USDT across Binance and Coinbase?"

## Hermes Agent Integration

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  gainium:
    command: "docker"
    args: ["exec", "-i", "gainium-mcp", "node", "/app/mcp-server.js"]
    env:
      GAINIUM_API_URL: "http://localhost:3001"
      GAINIUM_API_KEY: "${GAINIUM_API_KEY}"
```

## Use Cases for Business Operators

1. **Portfolio monitoring**: Agent checks positions daily and alerts on significant changes
2. **Strategy validation**: Agent backtests strategies against multiple timeframes before manual review
3. **Market scanning**: Agent monitors volume spikes, trend changes, and arbitrage opportunities
4. **Risk management**: Agent tracks exposure across exchanges and flags concentration risk
5. **Reporting**: Agent generates daily/weekly performance summaries from Gainium data

## Architecture

```
┌─────────────┐     MCP      ┌──────────────┐
│  AI Agent   │◄────────────►│  Gainium MCP  │
│ (Hermes,    │              │  Server       │
│  Claude)    │              └──────┬───────┘
└─────────────┘                     │
                          ┌─────────▼─────────┐
                          │  Gainium Core     │
                          │  ┌─────────────┐  │
                          │  │ Strategy     │  │
                          │  │ Engine       │  │
                          │  ├─────────────┤  │
                          │  │ Backtester   │  │
                          │  ├─────────────┤  │
                          │  │ Exchange     │  │
                          │  │ Connectors   │  │
                          │  └─────────────┘  │
                          └───────────────────┘
```

## Limitations

- **Docker required**: Full stack needs Docker — no lightweight install option
- **Crypto-only**: No support for stocks, forex, or traditional assets
- **Self-hosted**: No managed cloud version — you run the infrastructure
- **Early MCP integration**: MCP server is new; tool coverage expanding
- **Live trading risk**: Always use paper trading first and set position limits

## Security Notes

- **API keys**: Exchange API keys are stored in Gainium's encrypted database, not passed through MCP
- **Paper trading default**: New strategies start in simulation mode — must be explicitly switched to live
- **Read-only mode**: Configure agents with read-only exchange API keys for monitoring-only use
- **Confirmation gates**: Live deployment and large trades require explicit confirmation

## Category

**Finance** — Gainium joins tools like Capital.com MCP and Alpha Vantage in the finance MCP category. It differentiates by focusing on crypto trading automation with a no-code strategy builder and AI agent integration.

---

*Discovered via [mcp.so](https://mcp.so/servers/gainium) on July 24, 2026. Verified listing. GitHub: [Gainium/docker-sh](https://github.com/Gainium/docker-sh). 4 stars.*
