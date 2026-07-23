---
title: "Correctover MCP Server — Contract Validation & LLM API Failover"
description: "Integration guide for Correctover/mcp-server: 6-dimension contract validation, self-healing LLM API failover with 87 rules across 9 providers. 22μs P50 validation, 949ms E2E failover."
category: legal
tags: [mcp, contract-validation, llm-api, failover, self-healing, api-gateway]
source: awesome-mcp-servers
repo: Correctover/mcp-server
stars: 0
discovered: 2026-07-23
last_updated: 2026-07-23
---

# Correctover MCP Server — Contract Validation & API Failover

**Repo:** [Correctover/mcp-server](https://github.com/Correctover/mcp-server)
**Install:** `npx -y correctover-mcp-server`
**Pricing:** Open source
**Category:** Legal / API Infrastructure

## Overview

Correctover provides two critical capabilities for business operators who rely on AI:
1. **Contract validation** — 6-dimension verification (structure, schema, latency, cost, identity, integrity) at 22μs P50
2. **Self-healing LLM API failover** — 87 self-healing rules with MAPE-K autonomic loop across 9 LLM providers

For operators running AI agents in production, this means contracts are validated before execution and LLM API calls automatically fail over when a provider goes down — no manual intervention needed.

## Why Business Operators Need This

1. **Contract Risk Mitigation** — Before your agent signs or executes any contract, Correctover validates it across 6 dimensions. Catches errors, missing clauses, and structural issues in microseconds.
2. **API Reliability** — If your primary LLM provider (OpenAI, Anthropic, etc.) has an outage, Correctover automatically fails over to an alternative provider in under 1 second (949ms E2E). Your agents keep running.
3. **Cost Control** — The cost dimension validation ensures you're not overpaying for API calls. BYOK (Bring Your Own Key) to 9 providers for direct, transparent pricing.

## Installation

```json
{
  "mcpServers": {
    "correctover": {
      "command": "npx",
      "args": ["-y", "correctover-mcp-server"]
    }
  }
}
```

## Supported LLM Providers (9)

| Provider | Type | Failover Priority |
|----------|------|-------------------|
| OpenAI | Primary | L1 |
| Anthropic | Primary | L1 |
| DeepSeek | Secondary | L2 |
| Moonshot | Secondary | L2 |
| Zhipu AI | Secondary | L2 |
| Qwen | Secondary | L2 |
| SiliconFlow | Tertiary | L3 |
| Groq | Tertiary | L3 |
| Together AI | Tertiary | L3 |

## Key Tools

| Tool | Function | Latency |
|------|----------|---------|
| `validate_contract` | 6-dimension contract verification | 22μs P50 |
| `health_check` | Provider health monitoring | Real-time |
| `failover_status` | Current failover state and routing | Instant |
| `cost_estimate` | Token cost estimation across providers | < 100ms |
| `schema_check` | Contract schema validation | Microseconds |
| `identity_verify` | Contract signer identity verification | Varies |

## Common Queries

### Contract Validation

```
"Validate this contract before I sign it. Check structure, schema, and identity."
"Run a full 6-dimension verification on the vendor agreement."
"Check this NDA for missing standard clauses."
```

### API Failover Management

```
"Show current LLM provider health status. Which providers are available?"
"Set up failover: primary OpenAI, fallback to Anthropic, tertiary to DeepSeek."
"What was the failover event from last night? Which provider went down?"
```

### Cost Optimization

```
"Compare token costs across all 9 providers for a 10K input / 2K output query."
"Which provider is cheapest for GPT-4-level quality right now?"
"Alert me if any provider raises prices by more than 10%."
```

## Best Practices

1. **Always validate contracts before execution** — 22μs is faster than human review by 6 orders of magnitude
2. **Configure failover chains** — Set up L1 (OpenAI/Anthropic) → L2 (DeepSeek/Moonshot) → L3 (Groq/Together) for maximum reliability
3. **Monitor the health dashboard** — Check provider health before starting long agent workflows
4. **Use cost_estimate proactively** — Compare provider pricing weekly; prices change frequently
5. **BYOK for each provider** — Direct API keys give you the best pricing and avoid middleware markups

## Limitations

- New server (June 2026) — production track record still developing
- Contract validation focused on structure and schema, not legal advice (use a lawyer for legal review)
- Failover latency (949ms) may be noticeable in real-time chat applications
- Requires API keys for each provider you want to fail over to

## For Operators: Integration with CorpusIQ

- **CorpusIQ Stripe connector** + Correctover = Validate payment contracts and monitor API costs
- **CorpusIQ QuickBooks connector** + Correctover = Track LLM API spending alongside other operational costs
- **CorpusIQ cross-source analysis** + Correctover = Correlate API cost data with business outcomes

## See Also

- [Stripe MCP Guide](/hermes/mcp/#stripe)
- [QuickBooks MCP Guide](/hermes/mcp/#quickbooks)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)

---

*Discovered: July 23, 2026 · Source: awesome-mcp-servers PR #8776 · Category: Legal/API Infrastructure*
