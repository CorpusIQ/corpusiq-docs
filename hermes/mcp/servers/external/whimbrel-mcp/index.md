---
title: "Whimbrel MCP - MedTech Funding and Regulatory Data"
description: "A US medtech BD analyst on demand: funded companies, NIH and NSF grants, federal contracts, FDA clearances and breakthrough designations, sourced."
category: Research
stars: n/a (new listing)
added: 2026-10-06
source: "chatmcp/mcpso issue #4813 (Oct 6, 2026 midday sweep)"
relevance: ★★
tags: [medtech, funding, grants, fda, business-development, research, remote-mcp]
---

# Whimbrel MedTech Analyst MCP

**Remote MCP server (Streamable HTTP, OAuth)** - a MedTech BD analyst on demand for US research. Connect it to Claude, ChatGPT or another client and ask about up-and-coming US medtech companies: who got funded this week through NIH and NSF grants and federal contracts, plus FDA clearances and Breakthrough marketing authorizations. Company research comes with every line linked to its source.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in; one-month free trial of the full product (card required)
Endpoint: https://data.whimbrelresearch.com
Tools: Signal feed, funding events, grants, contracts, FDA clearances, company research
Pricing: One-month free trial, then subscription
Built by: Whimbrel Research
Registry: com.whimbrelresearch/whimbrel-research
```

## Why This Matters for Operators

Medtech business development runs on weekly signals - a competitor's Series B, a competitor's FDA clearance, a grant that just landed at a company you should know. Catching them normally means subscriptions, alerts and manual tracking. Whimbrel packages the signal feed - pulse, signal of the day, NSF awards, federal contracts, NIH news when the window has it - behind one endpoint, and every research line comes with its link.

The honest framing helps here too: quiet NIH weeks still count as the product working, because the feed reports what actually happened. For BD, partnership and market-research work in medtech, the sourced shape means answers can go straight into a deck or a meeting note.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Signal feed | The week's funded and notable events across the US medtech space |
| Funding events | Who got funded this week, through NIH and NSF grants and federal contracts |
| Regulatory | FDA clearances and Breakthrough marketing authorizations |
| Company research | Profiles of up-and-coming medtech companies, with every line linked |
| Discovery | Machine-readable discovery at /v1/about and /.well-known/* |

## Installation

```bash
claude mcp add --transport http whimbrel https://data.whimbrelresearch.com
```

Then finish OAuth at Whimbrel sign-in and start the one-month free trial (or subscribe). The same URL works in ChatGPT desktop, Codex, Cursor and VS Code; setup snippets for each are on whimbrelresearch.com/connect.

## Configuration

```json
{
  "mcpServers": {
    "whimbrel": {
      "url": "https://data.whimbrelresearch.com"
    }
  }
}
```

## Business Relevance

- **Medtech BD teams** catch funding and regulatory events the week they happen, with sources attached.
- **Investors and analysts** track the US medtech pipeline - grants, contracts, clearances - without a research subscription stack.
- **Founders** monitor competitive movement and emerging players in their device category.
- **Consultants** pull company research where every line can be shown to a client.

## Integration with CorpusIQ

CorpusIQ reads a business's own numbers read-only; Whimbrel adds the external medtech signal layer. For a medtech operator, one conversation can hold the inside view - pipeline, revenue, marketing data from the connected stack - next to the outside view: who just got funded, who just cleared the FDA, and what the grants and contracts say, each with its source visible.

## Limitations

- US medtech focus; coverage is the US funding and regulatory surface.
- A card is required to start the one-month trial.
- Signal feed coverage varies by week - quiet windows show fewer events, honestly.
- New listing: no track record in this catalog yet.

## FAQ

### How do I know it worked?

Connect the server, finish sign-in, then ask: who got funded this week? Sourced events from the signal feed mean the install worked.

### What is covered?

US medtech signals: NIH and NSF grants, federal contracts, FDA clearances and Breakthrough marketing authorizations, plus company research with every line linked to its source.

### Is there a free trial?

Yes - a one-month free trial of the full product, started at Whimbrel sign-in after the OAuth connection.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Silicon Floor MCP - AI and Chip Stock Research](/hermes/mcp/servers/external/silicon-floor-mcp/)
- [GovContractScout MCP - State and Local Contracts](/hermes/mcp/servers/external/govcontractscout-mcp/)
