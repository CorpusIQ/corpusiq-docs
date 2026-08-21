---
title: "Mobbin MCP — 600,000 Real Product Screens for AI-Driven Design Research"
description: "Official Mobbin MCP server connecting AI agents to 600,000+ real product screens: natural-language search across screens, multi-step user flows and website sections, with inline images and canonical Mobbin links for citation. OAuth over Streamable HTTP."
category: Design & Product Research
stars: n/a (new listing)
added: 2026-08-21
source: mcp.so
relevance: ★★
tags: [design, ui, ux, screens, product, research, oauth, remote-mcp]
---

# Mobbin MCP

**Real product screens, searchable by an agent — so what gets built starts with what already works.** Mobbin is the established screen-reference library (600,000+ screens across top products); its official MCP server exposes three natural-language search tools over that corpus. Results return inline images with metadata, and every screen carries its canonical `mobbin_url` so agent output can cite the source a human can open.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth
Endpoint: https://api.mobbin.com/mcp
Tools: 3 (screen, flow and section search)
Pricing: Mobbin plans (not published on listing)
Category: Design & Product Research
Built by: Mobbin (github.com/mobbin/mobbin-mcp-server)
```

## Why This Matters for Operators

"Let's redesign the onboarding" used to mean a designer hand-collecting screenshots from ten competitors. **Mobbin's tools make that research a question**: "show me how fintech apps do first-run onboarding" returns real screens with their source links; "find checkout flows with one-page payment" returns multi-step flow previews. Because the tools return inline images, an agent with vision can actually analyze the screens — layout, copy, hierarchy — rather than guess from metadata.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_screens` | Natural-language search for UI screens; returns inline images + metadata + canonical mobbin_url |
| `search_flows` | Multi-step user flows (onboarding, checkout) with evenly-spaced preview images per screen |
| `search_sections` | Website sections (About, Pricing, Footer) with inline images |

Tool instructions enforce citation discipline: when presenting results, each screen must be linked to its `mobbin_url`, and descriptions must come from examining the images, not from metadata alone.

## Installation

```bash
claude mcp add mobbin --transport http https://api.mobbin.com/mcp
```

First connect opens a browser OAuth flow to sign in to your Mobbin account.

## Configuration

```json
{
  "mcpServers": {
    "mobbin": {
      "type": "http",
      "url": "https://api.mobbin.com/mcp"
    }
  }
}
```

## Business Relevance

- **Founders validating a feature** pull every competitor's take on the flow in one session
- **Designers** start projects from real, cited screens instead of memory
- **Product teams** brief engineers with actual UI references linked to their sources
- **Agencies pitching redesigns** ground proposals in what the category's best products actually ship

## Integration with CorpusIQ

Mobbin informs what to build; CorpusIQ measures whether it worked. A product session can research patterns in Mobbin (how do top SaaS apps price and onboard), implement, then validate through CorpusIQ — GA4 conversion funnels, Stripe checkout data, HubSpot win rates — so the design loop runs from reference to result in one agent workflow. For competitive product teardowns, Mobbin's screens pair with CorpusIQ's web-fetch and market connectors for evidence-backed comparisons.

## Limitations

- Design reference only — no code, no components, no analytics
- Requires a Mobbin account and plan for full corpus access; OAuth on connect
- Vision-capable clients get the most value; text-only clients see metadata without the images
- New MCP listing (Aug 2026) for a long-established vendor
- Three tools is a deliberately narrow surface — search is the whole product

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
