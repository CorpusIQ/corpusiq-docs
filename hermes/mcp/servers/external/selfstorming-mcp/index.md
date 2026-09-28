---
title: "Selfstorming MCP - Marketing Libraries and Ideation"
description: "Selfstorming plugs 1,800+ award-winning campaigns, sourced marketing research and an ideation engine into an AI assistant's workflow."
category: Marketing
stars: n/a (new listing)
added: 2026-09-28
source: "mcp.so server page (selfstorming.com)"
relevance: ★★★
tags: [marketing, campaign-research, ideation, copywriting, brand-strategy, remote-mcp, oauth]
---

# Selfstorming MCP

**Curated marketing libraries and an ideation engine for AI assistants.** Selfstorming gives an assistant 1,800+ award-winning campaigns broken down to brief, idea, mechanic and strategy, 850+ sourced findings from WARC, Kantar, System1 and Ipsos, and a library of creative techniques, hooks and frameworks - then runs ideation, naming and hooks sessions grounded in all of it, saved as boards.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth login (Selfstorming account)
Endpoint: https://www.selfstorming.com/api/mcp
Tools: campaign search, marketing wisdom lookup, technique libraries, ideation and naming sessions
Pricing: Selfstorming Pro; daily fair-use limits (500 generated ideas, 10 sessions, 200 library lookups)
Category: Marketing / Creative Intelligence
Built by: Selfstorming (selfstorming.com)
```

## Why This Matters for Operators

Generic AI assistants ideate from the average of the internet. Selfstorming swaps that for curated creative material: award-winning campaigns searchable by brief, mood or mechanic, sourced findings that name the original report, and codified techniques for hooks, naming and storytelling. An operator gets brief-grade campaign research and sourced ammunition for recommendations without a creative director on staff.

The output lands as boards in your Selfstorming account, so ideation sessions are refinable and exportable to PowerPoint rather than evaporating in a chat thread.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Campaign search | Search 1,800+ award-winning campaigns by brief, mood or mechanic |
| Marketing wisdom | 850+ sourced findings from WARC, Kantar, System1 and Ipsos plus 61 marketing laws |
| Technique libraries | 100 creative techniques, 360 hooks, 66 naming techniques, 52 strategy frameworks with diagrams |
| Ideation sessions | Brief-driven ideation, naming and hooks grounded in the libraries, saved as boards |

Tool names are served from the endpoint; the table reflects the vendor's published capability set.

## Installation

```bash
claude mcp add selfstorming --transport http https://www.selfstorming.com/api/mcp
```

Setup guide and technical docs live at selfstorming.com/tools/mcp/docs.

## Configuration

```json
{
  "mcpServers": {
    "selfstorming": {
      "type": "http",
      "url": "https://www.selfstorming.com/api/mcp"
    }
  }
}
```

## Business Relevance

- **Founders** research how award-winning campaigns cracked similar problems
- **Marketers** back recommendations with sourced stats from the marketing canon
- **Copywriters** pull proven hooks and storytelling techniques instead of inventing from scratch
- **Agencies** run naming and ideation sessions that export to PowerPoint boards

## Integration with CorpusIQ

Selfstorming pairs with CorpusIQ analytics connectors as a research-to-results loop. Pull audience and channel data from GA4 and the Meta Ads connector to shape the brief, run Selfstorming campaign searches against that brief, and ship the resulting creative through the channels CorpusIQ already reports on - then measure whether sourced, proven mechanics beat the last campaign baseline.

## Limitations

- Brand new listing, no track record yet
- Requires a Selfstorming Pro subscription
- Daily fair-use limits: 500 generated ideas, names and hooks, 10 sessions, 200 library lookups
- No published tool catalog; tool names are served from the endpoint
- Libraries are marketing and creative focused; not a general business research tool

## FAQ

### What makes this different from asking a plain AI assistant?

A plain assistant ideates from training data. Selfstorming grounds the same session in 1,800+ curated award-winning campaigns, sourced marketing research and codified creative techniques, with every sourced finding naming its original report.

### What can agents actually do with it?

Search campaigns by brief, mood or mechanic, pull sourced marketing findings, apply hooks, naming and storytelling techniques, and run ideation sessions that save as exportable boards.

### Does it replace a creative agency?

No. It supplies research-grade creative material and structured ideation for teams without a creative director, but execution and judgment still belong to the operator.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
