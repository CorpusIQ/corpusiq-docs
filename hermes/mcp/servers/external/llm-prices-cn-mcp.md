---
title: "LLM Prices CN MCP Server — Daily-Verified LLM Pricing Dataset"
description: "Integration guide for szp2005/llm-prices-cn: 44+ LLM models, daily-verified pricing (CN & global), hosted MCP server for live price queries and token cost estimation."
category: finance
tags: [mcp, llm-pricing, cost-optimization, api, token-estimation]
source: awesome-mcp-servers
repo: szp2005/llm-prices-cn
stars: 0
discovered: 2026-07-23
last_updated: 2026-07-23
---

# LLM Prices CN MCP Server — LLM API Pricing Dataset

**Repo:** [szp2005/llm-prices-cn](https://github.com/szp2005/llm-prices-cn)
**Pricing:** Free, hosted
**Category:** Finance / Cost Optimization

## Overview

LLM Prices CN is a daily-verified dataset of LLM API pricing covering 44+ models across Chinese and global providers. It includes a hosted MCP server for live price queries and token cost estimation — critical for business operators managing AI agent infrastructure costs.

## Why Business Operators Need This

1. **Cost Visibility** — With 44+ LLM models available, pricing changes frequently. LLM Prices CN verifies prices daily so your cost estimates are always current.
2. **Provider Comparison** — Compare input/output token pricing across OpenAI, Anthropic, DeepSeek, Moonshot, Zhipu, Qwen, and more in one query.
3. **Budget Planning** — Estimate monthly LLM costs based on expected token volume before committing to a provider.
4. **China + Global Coverage** — Unique coverage of Chinese LLM providers (DeepSeek, Moonshot, Zhipu, Qwen) alongside global providers — essential for operators with multi-market needs.

## Installation

### Hosted (Remote)

The server is hosted and requires no local installation:

```json
{
  "mcpServers": {
    "llm-prices": {
      "url": "https://llm-prices-cn.example.com/mcp",
      "transport": "streamable-http"
    }
  }
}
```

### Local

```json
{
  "mcpServers": {
    "llm-prices": {
      "command": "python",
      "args": ["-m", "llm_prices_cn"]
    }
  }
}
```

## Key Tools

| Tool | Function |
|------|----------|
| `get_all_prices` | Retrieve current pricing for all 44+ tracked models |
| `get_model_price` | Get pricing for a specific model (e.g., `gpt-4o`, `claude-sonnet-4`) |
| `estimate_cost` | Calculate estimated cost for given token volumes |
| `compare_providers` | Side-by-side pricing comparison for equivalent capability tiers |
| `price_history` | Track pricing changes over time for a model |
| `get_lowest_cost` | Find the cheapest model meeting your capability requirements |

## Covered Providers & Models (44+)

| Provider | Models Tracked | Region |
|----------|---------------|--------|
| OpenAI | GPT-4o, GPT-4o-mini, o3, o4-mini | Global |
| Anthropic | Claude Opus 4, Sonnet 4, Haiku 3.5 | Global |
| DeepSeek | V3, R1, V4-Pro | CN/Global |
| Moonshot | Kimi series | CN |
| Zhipu AI | GLM-4 series | CN |
| Qwen | Qwen-Max, Qwen-Plus | CN |
| Google | Gemini 2.5 Pro, Flash | Global |
| xAI | Grok 3 | Global |
| SiliconFlow | Various open-source | CN |
| Groq | Llama, Mixtral | Global |
| Together AI | Various | Global |

*Pricing verified daily. Last verification date included in every response.*

## Common Queries

### Cost Estimation

```
"Estimate my monthly LLM costs: 500K input tokens/day, 100K output tokens/day. Compare GPT-4o vs Claude Sonnet 4."
"What's the cheapest model that can handle 128K context for my document processing pipeline?"
"If I switch from Claude Opus 4 to DeepSeek V4-Pro, how much will I save monthly?"
```

### Provider Comparison

```
"Compare input/output pricing for all Chinese LLM providers. I need 1M tokens/day."
"Show me the pricing history for GPT-4o over the last 3 months — has it changed?"
"Which provider has the best price/performance ratio for coding tasks?"
```

### Budget Planning

```
"I have a $500/month LLM budget. How many tokens can I process with each provider?"
"Alert me if any provider changes prices by more than 5%."
"What's the total cost difference between using OpenAI exclusively vs a multi-provider setup?"
```

## Best Practices

1. **Check prices weekly** — LLM pricing changes frequently, especially among Chinese providers competing aggressively
2. **Use estimate_cost before large jobs** — A 10M token batch job can cost $0.50 or $15.00 depending on the model
3. **Compare tiers fairly** — Match capability tiers (e.g., GPT-4o vs Claude Sonnet 4, not GPT-4o vs Haiku)
4. **Factor in quality** — Lowest cost isn't always best. Cross-reference with your quality requirements
5. **Monitor price_history** — Track trends to spot providers getting cheaper (or more expensive) over time

## Limitations

- New server (July 2026) — data freshness guarantees still being established
- China-focused dataset — some global providers may have less frequent updates
- Token cost estimation assumes standard tokenization — actual costs vary with prompt structure
- Hosted endpoint URL may change — verify the current endpoint on the GitHub repo

## For Operators: Integration with CorpusIQ

- **CorpusIQ QuickBooks connector** + LLM Prices CN = Track actual LLM spend against estimated costs
- **CorpusIQ Stripe connector** + LLM Prices CN = Monitor API billing against provider pricing
- **CorpusIQ cross-source analysis** + LLM Prices CN = Build LLM cost dashboards with actual vs budget tracking

## See Also

- [Correctover MCP Guide](/hermes/mcp/servers/external/correctover-mcp/) — LLM API failover and cost validation
- [Stripe MCP Guide](/hermes/mcp/#stripe)
- [QuickBooks MCP Guide](/hermes/mcp/#quickbooks)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)

---

*Discovered: July 23, 2026 · Source: awesome-mcp-servers PR #9542 · Category: Finance/Cost Optimization*
