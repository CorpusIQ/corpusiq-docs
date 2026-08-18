---
title: "DealMachine MCP - CorpusIQ Docs"
description: DealMachine MCP integration guide — connect AI agents to real estate property intelligence for sales, marketing, prospecting, enrichment, and lead generation.
source: github.com/DealMachine/dealmachine-cli
category: Marketing / Real Estate
stars: new (July 2026)
added: 2026-07-29
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/dealmachine-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# DealMachine MCP

**Real estate property intelligence MCP server** — connects AI agents to DealMachine's property, owner, people, and company data for real estate sales, marketing, prospecting, enrichment, and lead generation.

> **Source:** [github.com/DealMachine/dealmachine-cli](https://github.com/DealMachine/dealmachine-cli)
> **API Docs:** [api.docs.dealmachine.com](https://api.docs.dealmachine.com)
> **Category:** Marketing / Real Estate
> **Transport:** Hosted remote (Streamable HTTP) + CLI
> **Auth:** OAuth 2.1 (ChatGPT, Claude, Cursor, Codex) or API Key (developer clients)
> **Stars:** New (July 2026)

## What It Does

DealMachine CLI (`dm`) is a Commander.js CLI that provides **17 command groups** covering:

- **Agent Guidance** — How-to instructions for the AI agent
- **Authentication** — OAuth 2.1 and API key management
- **Property Search** — Find properties by address, owner, parcel, or criteria
- **People Lookup** — Owner identity, contact data, skip tracing
- **Enrichment** — Layer additional data onto property records
- **Comps** — Comparable sales analysis
- **List Management** — Create and manage lead/property lists
- **Developer Utilities** — Manifests for OpenAI, Claude, Cursor, Copilot, Gemini

The CLI compiles to a single ESM bundle via TypeScript and has **zero** `@dealmachine/*` dependencies — it's a self-contained binary that communicates exclusively through DealMachine's public REST API.

## Why This Matters for Operators

Real estate operators — investors, agents, wholesalers, and property managers — spend hours manually pulling property records, skip-tracing owners, and analyzing comps. DealMachine MCP lets AI agents do this conversationally:

- **"Look up the owner of 123 Main St and find available contact data"**
- **"Pull comps for the last 6 months within 0.5 miles of this property"**
- **"Enrich this list of 50 properties with owner details and skip-trace results"**
- **"Build a lead list of vacant properties in zip code 90210 with absentee owners"**

The combination of property intelligence + AI agent = a real estate research team in your pocket.

## How It Compares

| Feature | DealMachine MCP | PropStream (no MCP) | BatchLeads (no MCP) | Google Maps Scraper MCP |
|---------|----------------|---------------------|--------------------|--------------------------|
| Property data | ✅ | ✅ | ✅ | ❌ (maps only) |
| Owner skip-tracing | ✅ | ✅ | ✅ | ❌ |
| Comps analysis | ✅ | ✅ | ❌ | ❌ |
| MCP-native | ✅ | ❌ | ❌ | ✅ |
| AI agent ready | ✅ | ❌ | ❌ | ✅ |
| Lead management | ✅ | ✅ | ✅ | ❌ |

DealMachine is the first major real estate data platform to ship an MCP server. Before this, operators had to log into a web dashboard, manually search properties, and copy-paste data into their AI tools.

## Integration Setup

### 1. Get a DealMachine Account + API Key

1. Sign up at [dealmachine.com](https://dealmachine.com)
2. Go to Settings → Developer → API Keys
3. Generate an API key for MCP access

### 2. Install via CLI

```bash
npm install -g dealmachine-cli
# or
npx dealmachine-cli
```

### 3. Configure MCP Client

**Claude Desktop (`claude_desktop_config.json`):**
```json
{
  "mcpServers": {
    "dealmachine": {
      "command": "npx",
      "args": ["dealmachine-cli"],
      "env": {
        "DEALMACHINE_API_KEY": "your-api-key"
      }
    }
  }
}
```

**Cursor / VS Code (`.cursor/mcp.json`):**
```json
{
  "mcpServers": {
    "dealmachine": {
      "command": "npx",
      "args": ["dealmachine-cli"],
      "env": {
        "DEALMACHINE_API_KEY": "your-api-key"
      }
    }
  }
}
```

### 4. OAuth 2.1 for ChatGPT/Claude

For managed AI platforms that support OAuth flows (ChatGPT, Claude.ai), DealMachine supports OAuth 2.1. The first time you connect, your AI client opens a browser to sign in and authorize access. Subsequent sessions reuse the credentials.

## Security Model

- **OAuth 2.1** for managed AI platforms — scoped access with browser-based authorization
- **API Key** for developer clients — bearer token authentication
- **Read-only tools** by default — enrichment and lookups
- **Write operations** require explicit permissions
- **API usage tracked** in your DealMachine account dashboard

## Pricing

DealMachine's API access is included in their subscription plans. Check [dealmachine.com/pricing](https://dealmachine.com/pricing) for current tiers. The MCP server itself is free and open source.

## Limitations

- **US-focused** — property data is US-centric
- **Requires DealMachine subscription** — not a standalone free tool
- **New MCP** — July 2026 launch, expect rapid iteration
- **CLI-based** — requires Node.js to run locally (or use hosted MCP endpoint)

## See Also

- [[google-maps-scraper-mcp]] — Google Maps lead data MCP
- [[basedonbusiness-mcp]] — Google Maps business lead search + enrichment
- [[quickbooks-mcp]] — QuickBooks MCP for real estate financials
