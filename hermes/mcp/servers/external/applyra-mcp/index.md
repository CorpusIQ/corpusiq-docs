---
title: "Applyra MCP - App Store Keyword Data for AI Agents"
description: "App Store and Google Play keyword data for AI assistants - rankings, difficulty, traffic, competitors and ASO health audits."
category: Marketing
stars: 0
added: 2026-09-29
source: mcpservers.org
relevance: ★★★
tags: [aso, app-store, google-play, keywords, rankings, competitor-analysis, marketing, self-hosted]
---

# Applyra MCP

**App Store Optimization data inside your AI assistant.** Applyra connects App Store and Google Play keyword data to Claude, Cursor, Codex and other MCP clients: rank tracking, difficulty and traffic scoring, listing audits and metadata simulation, competitor visibility, autocomplete mining, niche clustering and top charts. 25 tools across both stores.

```
Server type: Local stdio (npm)
Auth: Applyra API key (Unlimited plan)
Endpoint: npx -y @applyra/mcp-server
Tools: 25 (rank tracking, difficulty and traffic, listing audits, metadata simulation, competitors, autocomplete, niches, top charts)
Pricing: Requires Applyra Unlimited plan (applyra.io pricing)
Category: Marketing
Built by: Applyra (github.com/applyra-io/mcp-server, MIT)
```

## Why This Matters for Operators

App operators live and die by keyword visibility, and the classic ASO workflow is exporting CSVs and pasting them into a dashboard. Applyra puts the data where the analysis already happens: your assistant can pull rankings, simulate metadata changes, check what competitors rank for and mine autocomplete - then act on it in the same session.

The metadata simulation is the practical win. Instead of shipping a title or subtitle change and waiting weeks for store impact, the assistant can model candidate changes against current rankings before anything goes live.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Rank tracking | Keyword rankings on the App Store and Google Play, per country |
| Difficulty and traffic | Keyword difficulty scores and traffic estimates for prioritisation |
| Listing audits | App listing audits with concrete improvement findings |
| Metadata simulation | Model title, subtitle and keyword-field changes against current rankings |
| Competitor visibility | What competitors rank for, with gap analysis |
| Autocomplete mining | Store autocomplete suggestions as keyword research input |
| Niche clustering | Keyword grouping into niches for structured roadmaps |
| Top charts | Category and country top charts for market context |

Tool names are served from the endpoint; the vendor documents the full tool set in the repo (github.com/applyra-io/mcp-server).

## Installation

```bash
claude mcp add applyra -e APPLYRA_API_KEY=your_api_key -- npx -y @applyra/mcp-server
```

Generate the API key at applyra.io/dashboard/api after upgrading to the Unlimited plan. Node.js 20 or later is required.

## Configuration

```json
{
  "mcpServers": {
    "applyra": {
      "command": "npx",
      "args": ["-y", "@applyra/mcp-server"],
      "env": {
        "APPLYRA_API_KEY": "your_api_key"
      }
    }
  }
}
```

Per-client walkthroughs for Cursor, VS Code Copilot, Claude Code, Codex and Windsurf are published in the repo README.

## Business Relevance

- **App founders** run weekly keyword reviews inside the assistant instead of exporting dashboards
- **ASO agencies** manage multiple client apps with simulated metadata changes and competitor gaps
- **Growth marketers** mine autocomplete and niche clusters for store listing roadmaps
- **Product teams** track top charts and category movement for market context

## Integration with CorpusIQ

Applyra covers store visibility while CorpusIQ covers business performance. A composed workflow: CorpusIQ reports revenue, conversion and retention through its connectors - Stripe, GA4, app analytics - while Applyra explains the top-of-funnel keyword picture in the same session. An assistant can connect a ranking drop to a competitor's metadata change and quantify it against install and revenue data.

## Limitations

- Requires the paid Unlimited plan; no free tier access to the MCP server
- Brand new repo (0 GitHub stars), young project
- App stores only - no web SEO data
- Local stdio server with an API key; no OAuth flow

## FAQ

### What plan do I need for the MCP server?

The MCP server requires an Applyra account on the Unlimited plan, with an API key generated at applyra.io/dashboard/api.

### Does it cover both stores?

Yes. All 25 tools operate on both the App Store and Google Play, so rankings, difficulty and competitor data are comparable across stores.

### Can it change my listing for me?

No. Applyra is a data and simulation layer - it reads rankings and models metadata changes, but actual listing edits stay in App Store Connect and Google Play Console.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
