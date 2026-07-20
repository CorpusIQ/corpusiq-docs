---
title: "openInvest — Research-Grade Investment Decision Engine MCP"
description: "Multi-agent investment committee for AI agents — isolated agents debate each position, auditable verdicts with lookahead-protected backtests, published negative results. 63⭐. Python."
source: github.com/longsizhuo/openInvest
stars: 63
language: Python
transport: stdio
auth: None (bring your own data sources)
category: Finance & Fintech
last_updated: 2026-07-20
---

# openInvest — Research-Grade Investment Decision Engine

**63⭐ open-source investment decision engine for AI agents.** Instead of a single LLM making buy/sell calls, openInvest runs an isolated multi-agent committee where independent agents debate each position. Verdicts are auditable with lookahead-protected backtests. Negative results are published alongside positive ones — rare integrity in quant finance.

## What It Does for Operators

- **Multi-agent committee** — Each investment thesis gets debated by independent agents with different perspectives (fundamental, technical, macro, risk). No single-agent bias.
- **Auditable verdicts** — Every decision includes the full debate transcript, evidence chain, and confidence scores. Not a black box.
- **Lookahead-protected backtests** — Backtest engine prevents the model from "seeing" future prices when simulating historical decisions. Honest performance metrics.
- **Published negative results** — The system publishes losing trades with the same detail as winners. No survivorship bias.
- **Python-native** — Runs locally or on any Python environment. No cloud dependency.

## Installation

```bash
pip install openinvest
# or
git clone https://github.com/longsizhuo/openInvest.git
cd openInvest
pip install -e .
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "openinvest": {
      "command": "python",
      "args": ["-m", "openinvest.server"]
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `convene_committee` | Spawn multi-agent committee to debate a ticker/investment thesis |
| `get_verdict` | Retrieve the committee's final recommendation with confidence scores |
| `run_backtest` | Backtest a strategy with lookahead protection |
| `get_debate_transcript` | Full agent debate log for audit and review |
| `list_published_results` | All verdicts — including negative results |
| `analyze_position` | Deep-dive on a single position across all agent perspectives |

## Operator Use Cases

1. **Portfolio Managers** — Run investment theses through the committee before execution. Get multi-perspective analysis in minutes instead of days.

2. **Analysts** — Use the backtest engine to validate strategies with lookahead protection. Publish auditable research.

3. **Family Offices** — Automate initial screening of investment opportunities. Flag the ones worth human review.

4. **Fintech Builders** — Embed the committee engine into investment platforms. Give users AI-powered second opinions on their portfolio decisions.

## Architecture

```
openInvest/
├── agents/
│   ├── fundamental.py    # Financial statement analysis
│   ├── technical.py      # Chart patterns, indicators
│   ├── macro.py          # Economic context, rates
│   └── risk.py           # VaR, correlation, tail risk
├── committee/
│   ├── convene.py        # Spawn & orchestrate agents
│   ├── debate.py         # Structured deliberation protocol
│   └── verdict.py        # Confidence-weighted aggregation
├── backtest/
│   └── engine.py         # Lookahead-protected simulation
└── server.py             # MCP server entry point
```

## CorpusIQ Angle

openInvest's multi-agent committee architecture is philosophically aligned with CorpusIQ's multi-agent approach to business intelligence. Financial operators using CorpusIQ for business data (QuickBooks, Stripe, etc.) could pair it with openInvest for investment decisions — operational data feeding the investment committee. Potential deep integration opportunity.

## Limitations

- Bring your own data sources — openInvest doesn't provide market data feeds. You'll need Alpha Vantage, Yahoo Finance, or similar.
- Python-only. No TypeScript/Node version.
- Multi-agent committees are token-intensive. Budget ~200K tokens per full analysis.
- Active development — API may change.
