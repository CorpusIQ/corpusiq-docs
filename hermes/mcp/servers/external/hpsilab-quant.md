---
title: "HPSILab Quant Finance MCP — Options Analytics & Monte Carlo"
description: "Connect HPSILab institutional-grade quant finance to Hermes Agent. Black-Scholes options pricing, implied volatility surfaces, Monte Carlo simulations, quantum ML signals, strategy backtesting."
category: mcp
tags: [mcp-server, hpsilab, quant-finance, options, black-scholes, monte-carlo, greeks, volatility]
last_updated: 2026-07-17
---

# HPSILab — Quant Finance MCP Server

## What It Is

HPSILab is an institutional-grade quantitative finance MCP server. It gives AI agents access to options analytics (Black-Scholes, Greeks), implied volatility surfaces, Monte Carlo simulations, AI market signals, and strategy backtesting. Uses Qiskit for quantum machine learning and includes regime detection.

**Key differentiator from Hermes Plant**: HPSILab targets the full quant stack (options, volatility, Monte Carlo, quantum ML) while Hermes Plant focuses on deterministic computation with crypto payment rails.

## Tools Available

| Tool Name | Description |
|-----------|-------------|
| `analyze_stock` | Comprehensive stock analysis with fundamentals and technical indicators |
| `get_iv_radar` | Implied volatility surface visualization and skew analysis |
| `get_option_pressure` | Options flow analysis — call/put volume, open interest, unusual activity |
| `get_monte_carlo` | Monte Carlo path generation, scenario analysis, VaR calculation |
| `get_ai_prediction` | AI-driven price predictions with confidence intervals |
| `get_equity_curves` | Strategy backtesting with transaction costs, slippage, benchmark comparison |
| `generate_stock_images` | Generate annotated stock charts with technical indicators |
| `generate_stock_research_report` | Full research report with fundamentals, technicals, and risk metrics |
| `get_pretrade_risk_scan` | Pre-trade risk assessment: margin, exposure, concentration limits |

## Quick Start

```bash
# Option 1: Remote endpoint (recommended — no local install)
hermes mcp add hpsilab --url https://hpsilab.com/mcp

# Option 2: Via PyPI (local install)
pip install hpsilab-mcp

# Option 3: From GitHub
git clone https://github.com/haiyunsky/hpsilab-quant-finance-mcp.git
cd hpsilab-quant-finance-mcp
pip install .
cp env.example .env
# edit .env and set HPSILAB_API_KEY=***

# Run the MCP server
hpsilab-quant-finance-mcp

# Add local install to Hermes
hermes mcp add hpsilab --command "hpsilab-quant-finance-mcp"
```

See also: [PyPI package](https://pypi.org/project/hpsilab-mcp/) | [Official site](https://hpsilab.com)

## Business Use Cases

1. **Options Trading**: Price options, compute Greeks, and visualize volatility surfaces before executing trades
2. **Risk Management**: Run Monte Carlo VaR simulations across portfolios, stress-test for tail events
3. **Quant Research**: Backtest trading strategies with realistic transaction costs and slippage
4. **Regime Detection**: Automatically classify market regimes (trending, mean-reverting, high-vol) for strategy selection

## Comparison: Finance MCP Landscape (July 2026)

| Server | Focus | Best For |
|--------|-------|----------|
| **HPSILab** | Full quant stack | Options traders, quant researchers, risk managers |
| Hermes Plant | Deterministic finance + crypto payments | Trustless financial computation, pay-per-call models |
| SentiSense | Market sentiment | Sentiment-driven investors, analyst consensus tracking |
| mcp-tradier | Real-time market data | Real-time quotes, streaming data |
| mcp-eodhd | Historical data | Backtesting, fundamental analysis |
| Kalshi MCP | Prediction markets | Event-driven trading, political forecasting |

## Limitations

- Requires HPSILab account/API access
- Quantum ML features are experimental (Qiskit dependency adds complexity)
- Monte Carlo simulations are compute-intensive — not suitable for real-time trading
- New server — models and signals unvalidated in production

## See Also

- SentiSense MCP — for market sentiment and analyst ratings
- pipeworx-io/mcp-tradier — for real-time stock/options market data
- Hermes Plant MCP — for deterministic financial computation with crypto rails
- Kalshi MCP — for prediction market analysis and trading
