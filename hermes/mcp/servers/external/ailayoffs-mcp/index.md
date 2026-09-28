---
title: "AI Layoffs MCP - Open AI Job-Loss Data for Agents"
description: "AI Layoffs serves a source-cited register of AI-attributed layoffs and a live job-loss index over MCP, with no key required."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-28
source: "mcpservers.org server page (ailayoffs.org)"
relevance: ★★
tags: [job-market, layoffs, labor-data, datasets, research, data-analytics, remote-mcp]
---

# AI Layoffs MCP

**An open, source-cited register of AI-attributed layoffs an agent can query.** The AI Layoffs Index publishes a live 0-100 AI job-loss index, its component signals and a register of 111 source-cited layoff events as open data. The MCP server exposes the whole dataset to AI assistants, no account, no API key, CORS-enabled.

```
Server type: Remote (Streamable HTTP)
Auth: none, open data
Endpoint: https://ailayoffs.org/mcp
Tools: index and components, event register, signals, history
Pricing: free, open data
Category: Data & Analytics / Labor Market
Built by: AI Layoffs (ailayoffs.org, built on Founden.ai)
```

## Why This Matters for Operators

Labor-market pressure is a leading indicator for every business decision operators face: hiring cost, pricing power, buyer budgets, category demand. The AI Layoffs Index turns that into a queryable number set with methodology you can inspect, and because every event is source-cited, the agent can pull the underlying evidence instead of asserting a headline.

For operators the honest framing matters: this is a neutral observatory built only on free and open data, methodology v1.28, not a vendor selling a narrative.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Live index | The 0-100 AI job-loss index and its band |
| Components | The three component signals with their inputs |
| Event register | 111 source-cited AI-attributed layoff events |
| History | Reconstructed index history for trend work |
| Raw data | JSON index endpoint plus CSV register download |

The REST endpoints are published at ailayoffs.org/api/index and /api/register.csv; the MCP tools expose the same data to assistants.

## Installation

```bash
claude mcp add ailayoffs --transport http https://ailayoffs.org/mcp
```

No key or account is required; the endpoint is CORS-enabled for browser and agent clients alike.

## Configuration

```json
{
  "mcpServers": {
    "ailayoffs": {
      "type": "http",
      "url": "https://ailayoffs.org/mcp"
    }
  }
}
```

## Business Relevance

- **Founders** track labor-market pressure when planning hiring and budget
- **Analysts** pull source-cited layoff events for market briefs
- **Investors** monitor job-loss signals across portfolio categories
- **Agencies** add a neutral labor data source to client reporting

## Integration with CorpusIQ

AI Layoffs feeds the market-intelligence layer of CorpusIQ reporting. An agent pulls the current index and recent events, then composes them with QuickBooks P&L data and GA4 demand signals into an executive brief where labor-market context explains what the numbers show.

For deeper analysis, the CSV register lands in a data pipeline alongside other CorpusIQ sources, and the assistant can cite specific events with sources in board decks.

## Limitations

- New listing, no track record yet
- Single-domain dataset: AI-attributed layoffs only
- Methodology-driven numbers, not ground-truth employment statistics
- No authentication or service guarantees, it is open data

## FAQ

### Is the data free?

Yes. No account, no API key, CORS-enabled, because open data is the point.

### What does the index measure?

A live 0-100 AI job-loss index built from three component signals with a full methodology published at ailayoffs.org/methodology.

### Can I get the raw data?

Yes. The JSON index endpoint and a CSV register of every source-cited event are both public.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
