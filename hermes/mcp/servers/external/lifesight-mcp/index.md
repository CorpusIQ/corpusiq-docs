---
title: "Lifesight MCP - Unified Marketing Measurement and MMM"
description: "Connect AI assistants to your marketing mix models, budget data and ad performance for plain-language answers on channel performance, budget reallocation and forecasting."
category: Marketing
stars: n/a (no public repo)
added: 2026-09-03
source: mcpservers.org
relevance: ★★★
tags: [marketing-measurement, mmm, attribution, budget-optimization, ad-performance, analytics, remote-mcp]
---

# Lifesight MCP

**Remote MCP server (Streamable HTTP, OAuth connector flow)** - Lifesight connects an AI assistant directly to a Lifesight workspace: marketing mix models, budget data, ad performance and the documentation library, answered in plain language. Ask "what was my best-performing channel last week?" or "optimize my Q4 budget for revenue" and get structured, model-backed answers.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (connector flow via console.lifesight.io/mia-connect)
Endpoint: https://mcp.lifesight.io/mcp
Tools: capability set served from the endpoint (workspace-scoped)
Pricing: Lifesight workspace required (demo-led onboarding)
Category: Marketing
Built by: Lifesight (lifesight.io)
```

## Why This Matters for Operators

Marketing measurement is stuck between two broken options: last-click attribution that over-credits bottom-funnel, and MMM spreadsheets that require a data science team. Lifesight ships unified marketing measurement with causal inference, and the MCP layer puts it inside the assistant.

**The composed answer is the product:** instead of exporting model outputs and reading charts, an operator asks a question and gets a ranked answer with a methodology footnote. The endpoint carries model lists with confidence ranges, channel performance by iROAS, budget reallocation scenarios and a documentation library the agent can cite - including a published prompt library for planning, channel, anomaly, executive and methodology questions.

## Tools & Capabilities

Capability areas documented by the vendor (live tool list served from the workspace-scoped endpoint):

| Capability | Purpose |
|---|---|
| Model access | List causal models with last-run date and confidence range |
| Performance Q&A | Channel performance by iROAS, period comparisons |
| Budget optimization | Reallocation scenarios with constraints to maximize incremental revenue |
| Planning | Seasonality, promotions and forecast base-period selection |
| Documentation search | Methodology docs (geo-lift, MMM, attribution) with link-back summaries |

## Installation

Claude Desktop: Customize, Connectors, Add Custom connectors, then add https://mcp.lifesight.io/mcp and connect. Claude redirects to console.lifesight.io/mia-connect for sign-in; new users request access to reach the demo onboarding.

## Configuration

```json
{
  "mcpServers": {
    "lifesight": {
      "type": "http",
      "url": "https://mcp.lifesight.io/mcp"
    }
  }
}
```

An active Lifesight workspace is required. The same URL works from ChatGPT with the equivalent connector flow; per-client walkthroughs are published in the Lifesight docs.

## Business Relevance

- **Performance marketers** replace dashboard exports with ranked answers and methodology footnotes
- **Finance operators** run budget scenarios against causal models instead of spreadsheet guesses
- **Agencies** answer client questions about incrementality from the assistant

## Integration with CorpusIQ

Lifesight and CorpusIQ cover the two halves of marketing truth: CorpusIQ's Google Ads, GA4 and Shopify connectors stream the raw spend, traffic and revenue data, and Lifesight's models turn that stream into causal measurement. A composed workflow: CorpusIQ reports actual revenue by channel, Lifesight's MMM answers which channel drove it incrementally, and the operator reallocates budget with both the accounting and the causal picture in one assistant. CorpusIQ's structured business data also feeds Lifesight's models through its BigQuery, Snowflake and Google Sheets integrations.

## Limitations

- Requires a Lifesight workspace - demo-led onboarding, no self-serve signup documented
- Tool list not published; verify live tools against the workspace after connecting
- Measurement depth depends on connected data sources
- No key-only or anonymous access - OAuth connector flow only

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Staats MCP - Cookieless Web Analytics for Agents](/hermes/mcp/servers/external/staats-mcp)
- [SEOmatic MCP - Real Search Console Data with Approval-Gated Fixes](/hermes/mcp/servers/external/seomatic-mcp)
- [Tracetify MCP - SEO, GEO and Growth Reports for Agents](/hermes/mcp/servers/external/tracetify-mcp)
