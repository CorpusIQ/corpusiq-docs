---
title: Vibe Prospecting MCP - Live B2B Data for Lead Generation
description: Live B2B data inside any AI assistant from Explorium - build lead lists, research companies, enrich contacts and personalize outreach, with sample previews before full dataset exports.
category: Lead Generation & Web Scraping
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★★
tags: [lead-generation, b2b-data, contact-enrichment, sales-intelligence, prospecting, firmographics, technographics, remote-mcp]
---

# Vibe Prospecting MCP

**Remote MCP server (Streamable HTTP, browser OAuth)** - live B2B data from Explorium inside any AI assistant: build lead lists, research companies, enrich contacts and personalize outreach. No local server, no API key management - connect to one URL and sign in once in the browser.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth browser sign-in on first use (no API key)
Endpoint: https://vibeprospecting.explorium.ai/mcp
Tools: capability areas for company search, contact discovery, firm research and dataset export (live tool list served from the endpoint)
Pricing: sample previews are credit-friendly; full exports are explicitly requested
Category: Lead Generation & Web Scraping
Built by: Explorium (explorium-ai on GitHub)
```

## Why This Matters for Operators

Prospecting data usually lives in a separate tab: export a CSV, wait, clean it, import it, then finally start the outreach. **Vibe Prospecting moves that whole loop into the chat where the outreach is being written** - the agent that drafts your cold email is the same agent that built the lead list and enriched the contact.

The preview-first design matters for cost control: every search returns a 5-10 row sample first, and the full dataset is only processed when you explicitly ask to export. Operators explore freely without burning credit on accidental full pulls.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Find companies | Search by name, domain, industry, size, location, tech stack and more |
| Discover and enrich contacts | Roles, profiles and buying signals at any company |
| Research firms | Firmographics, technographics, funding, competitors and challenges |
| Analyze and export | Preview a sample instantly, export the full dataset to CSV on request |

Exact tool names are served from the live endpoint after OAuth connect.

## Installation

```bash
claude mcp add --transport http vibe-prospecting https://vibeprospecting.explorium.ai/mcp
```

Per-client walkthroughs are published for Claude Desktop connectors, Codex CLI, Gemini CLI extensions, Manus connectors and Hermes - all point at the same remote endpoint with first-use browser sign-in.

## Configuration

```json
{
  "mcpServers": {
    "vibe-prospecting": {
      "type": "http",
      "url": "https://vibeprospecting.explorium.ai/mcp"
    }
  }
}
```

No API key to manage: the first tool call opens a browser sign-in, and the session persists after that.

## Business Relevance

- **Sales teams** build fresh lead lists and enrich contacts without leaving the AI assistant they already draft outreach in.
- **Founders validating a market** get firmographics, funding and competitor context per target account.
- **Agencies running multi-account outbound** get technographics and buying signals to segment campaigns.
- **Operators** get CSV exports on demand for CRM import - preview first, pull only what the campaign needs.

## Integration with CorpusIQ

Vibe Prospecting feeds the top of the CorpusIQ funnel: leads surfaced here flow into HubSpot as new deals, and the enrichment fields (firmographics, technographics, funding) ride along so CorpusIQ dashboards segment pipeline by segment instead of by raw name. The reverse direction works too - CorpusIQ knows which segments convert best, and that steers which company searches Vibe Prospecting runs next. Prospecting plus operations in one assistant loop.

## Limitations

- Brand new listing - no track record yet.
- OAuth sign-in requires a browser on first connect; headless hosts need the copy-back URL flow.
- Preview-first design means full datasets are credit-gated - monitor export volume.
- No published self-host option; data comes from Explorium's hosted B2B dataset.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
