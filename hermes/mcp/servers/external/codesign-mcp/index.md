---
title: "CoDesign MCP - Editable Design Engine for AI Agents"
description: "CoDesign gives coding agents a real design engine through IMG.LY's CE.SDK: create, edit and export structured, editable designs, apply brand kits, batch variants across formats, and import PSD, IDML, PowerPoint and PDF as working files. Runs locally over npx stdio."
category: Content
stars: n/a (new listing)
added: 2026-09-15
source: "mcp.so feed (Sep 15 midday) + mcp.so detail page + vendor overview at img.ly (CE.SDK)"
relevance: ★★
tags: [design, graphics, brand-kit, templates, batch-automation, pdf, print-ready, stdio]
---

# CoDesign MCP

**Designs that stay editable, generated from where you already work.** CoDesign (powered by IMG.LY's CE.SDK) returns structured scenes and an editable design rather than a flat image: you click the text, fix the typo, move the logo. One design resizes, rebrands or translates into every format and channel you need, the layout reflows instead of stretching, and every variant comes back editable.

```
Server type: Local (stdio via npx)
Auth: none for the runtime itself; IMG.LY / CE.SDK licensing applies to the SDK
Package: @imgly/codesign-mcp (npm)
Endpoint: npx -y @imgly/codesign-mcp@latest stdio
Tools: Live tool list from the local server (the listing shows none extracted)
Pricing: CE.SDK licensing (see img.ly)
Category: Content / Design automation
Built by: IMG.LY (img.ly)
```

## Why This Matters for Operators

Image generators make you regenerate and pray when a headline typo slips through. CoDesign inverts that: output arrives as an editable design, so corrections are edits, not rerolls. Brand kits load once and apply fonts, colors and logos to every output instead of being re-imagined per generation. And because one design can reflow into every channel format, a campaign asset set stops being five separate design requests.

## Capabilities

| Capability | What it covers |
|---|---|
| Editable output | Structured scenes, not pixels; edit text, logos and layout after generation |
| One design, every format | Resize, rebrand or translate with reflowing layouts; variants stay editable |
| Brand kits | Fonts, colors and logos applied to every output |
| Import working files | PSD, IDML, PowerPoint decks and PDFs come in as structured designs |
| Export what you need | PDF, image, SVG or the editable design file; print-ready with bleed |
| Batch automation | One asset per row: speaker cards from a CSV, business cards, price updates |

Vendor use cases include on-brand social carousels, localized flyers, template color variants, speaker cards from a CSV, cross-channel resizes and print-ready PDFs.

## Installation

```bash
claude mcp add codesign -- npx -y @imgly/codesign-mcp@latest stdio
```

## Configuration

```json
{
  "mcpServers": {
    "codesign": {
      "command": "npx",
      "args": [
        "-y",
        "@imgly/codesign-mcp@latest",
        "stdio"
      ]
    }
  }
}
```

## Business Relevance

- **Marketing teams** produce channel-ready variants from one design instead of rebuilding assets per format.
- **Founders and small teams** get professional-looking launch kits (hero, social posts, banners) without a designer in the loop for every size.
- **E-commerce operators** batch-generate on-brand product cards, price updates and campaign variants from lists.
- **Agencies** localize and rebrand client work with the layout reflowing around new text instead of breaking.

## Integration with CorpusIQ

CorpusIQ surfaces the business data (product catalogs via Shopify, performance numbers via GA4 and Stripe, customer context via HubSpot); CoDesign turns that data into on-brand visual assets in the same working session. A composed pattern: pull best-selling products or a month's metrics through CorpusIQ, then generate a carousel, report cover or launch kit through CoDesign, all editable and brand-kit applied. Neither replaces a design system; together they shorten the path from data to publishable asset.

## Limitations

- Local runtime: needs Node/npx on the machine running the agent.
- CE.SDK licensing applies; check img.ly for terms and platform support.
- The listing does not extract a tool list; run the server to enumerate its tools.
- Design quality still depends on the model driving the session; the engine guarantees editability, not creative judgment.
- Brand new to this catalog.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
