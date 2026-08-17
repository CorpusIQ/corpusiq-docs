---
title: "FCA Handbook MCP (Metis Harness) — UK Financial"
server: fca-handbook-mcp
rating: ★★★
category: Finance / Regulatory Compliance
transport: stdio
auth: Metis API Key
added: 2026-08-10
source: mcp.so
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/fca-handbook-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
description: "The primary tool — evaluates which FCA Handbook entries apply to an entity. Metis Harness MCP server gives agents direct access Financial Conduct Authority."
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# FCA Handbook MCP — Integration Guide

## Overview

The Metis FCA Handbook AI Harness MCP server gives AI agents direct access to the UK Financial Conduct Authority (FCA) Handbook — 10,000+ regulatory entries with verbatim citations, structured applicability evaluations, and binding-level classifications (R=Rule, G=Guidance).

This is the first dedicated regulatory compliance MCP server. For UK financial services operators, it transforms compliance research from manual handbook searching to conversational AI queries.

## Relevance to Business Operators

| Use Case | Value |
|----------|-------|
| Regulatory applicability | "Which FCA rules apply to a B2B payments platform serving SMEs?" |
| Compliance gap analysis | "What are our obligations under SYSC for outsourcing to AI vendors?" |
| Due diligence | "What FCA conduct rules apply to cryptoasset promotions?" |
| Audit prep | "Cite every FCA rule related to client money segregation." |
| Policy drafting | "What FCA guidance exists for operational resilience of cloud infrastructure?" |

## Setup

### Prerequisites
- Python 3.8+
- Metis API key ([get one here](https://fcahandbookharnessimplementation.onrender.com))

### Installation
```bash
pip install fca-handbook-harness-mcp
```

### Claude Desktop Configuration
```json
{
  "mcpServers": {
    "fca-handbook-harness": {
      "command": "fca-handbook-harness-mcp",
      "env": {
        "METIS_API_KEY": "sk_live_your_key_here"
      }
    }
  }
}
```

> **PATH note:** If the command doesn't resolve, replace `"command": "fca-handbook-harness-mcp"` with the absolute path from `which fca-handbook-harness-mcp`.

## Tools

### `evaluate_fca_handbook_applicability`

The primary tool — evaluates which FCA Handbook entries apply to an entity.

| Parameter | Type | Description |
|-----------|------|-------------|
| `user_input` | string (required, max 5000 chars) | Firm type, products/services, target market, regulatory question |
| `analysis_mode` | string (optional) | `"quick"` (default, 60-120s) or `"full"` (detailed conditional reasoning) |

**Returns:**

| Field | Description |
|-------|-------------|
| `summary` | 2-3 sentence overview of applicability |
| `entry_analysis` | Retrieved FCA Handbook entries with reasoning |
| `obligations` | High-confidence, conditional, and low-confidence obligations |
| `gaps` | What the analysis couldn't determine |
| `refinement_suggestions` | Follow-up info that would improve accuracy |
| `citations` | Verbatim quotes with binding levels (R=Rule, G=Guidance) |
| `tokens` | Token count for cost/complexity tracking |

## Security & Design

The Harness is built for enterprise compliance environments:

| Feature | Description |
|---------|-------------|
| **Stateless** | Each request independent — no session coupling |
| **One-shot** | Complete analysis in a single call |
| **Clear contract** | Explicit input/output schemas |
| **Hosted** | Single canonical source — no version drift |
| **Verbatim citations** | Quotes FCA Handbook entries directly, not LLM-synthesized text |
| **OWASP-aligned** | Designed against OWASP Top 10 for Agentic Applications 2026 |

## Use Cases for Business Operators

### Regulatory Applicability Check
```
> "We're a UK-authorised EMI offering B2B payment accounts to SMEs in 12 EEA countries. We custody client funds in segregated accounts and use AI for transaction monitoring. Evaluate which FCA Handbook entries apply."
```

### Compliance Gap Analysis
```
> "We're migrating our core banking to AWS. Run a full FCA Handbook evaluation on our operational resilience and outsourcing obligations under SYSC."
```

### Policy Drafting
```
> "What FCA guidance exists on fair treatment of vulnerable customers? Give me verbatim citations I can reference in our policy document."
```

### Audit Preparation
```
> "A regulator is reviewing our anti-money laundering controls. Give me every FCA rule related to AML transaction monitoring, with binding levels."
```

## Limitations

- **UK only** — FCA Handbook only; no EU (ESMA/EBA), US (SEC/FINRA), or other jurisdictions
- **Paid** — Metis API key requires paid account (pricing via fcahandbookharnessimplementation.onrender.com)
- **Stateless** — no multi-turn context; each query is independent
- **FCA Handbook only** — doesn't cover FCA guidance consultations, thematic reviews, or enforcement actions
- **Full mode is slow** — detailed analysis can take several minutes

## Verdict

★★★ — **Essential for UK-regulated financial services operators.** This is the first MCP server that makes regulatory compliance conversational. The verbatim-citation design (rather than LLM-synthesized answers) is critical for regulated environments where accuracy matters. For any UK fintech, EMI, payment institution, or investment firm using AI agents, this is a must-install.

Pair with The Bot Wire (US regulatory/economic primary sources, catalogued Jul 31) and Lawstronaut (155+ jurisdiction legal research, catalogued Aug 10 morning) for a complete regulatory intelligence stack.

## Related MCP Servers in Catalog

- **The Bot Wire** — US regulatory primary sources (SEC, Federal Register, court opinions) (★★★)
- **Lawstronaut MCP** — 50M+ laws and cases across 155+ jurisdictions (★★★)
- **Sanctions Screening MCP** — OFAC/EU/UK/UN sanctions screening (★★★)
- **Honest VIES MCP** — EU VAT number validation with audit trail (★★★)
