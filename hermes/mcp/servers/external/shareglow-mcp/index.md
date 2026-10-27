---
title: "Shareglow MCP - Link Previews and OG Images"
description: "Scan and fix link previews from your agent: Open Graph issues, platform renders, branded OG images, short links with previews and click stats."
category: Marketing
stars: n/a (new listing)
added: 2026-10-11
source: "chatmcp/mcpso #5134 (Oct 11, 2026 evening sweep)"
relevance: ★★
tags: [link-previews, open-graph, og-images, short-links, marketing, analytics, remote-mcp]
last_updated: "2026-10-24"
---

# Shareglow MCP

**Remote MCP server (Streamable HTTP, API key)** - link preview management for agents: scan any URL for Open Graph and Twitter card problems, see how it renders on major platforms, generate on-brand OG images from templates, refresh cached previews, and create short links with their own previews and click stats.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: Shareglow API key (Bearer sk_live_..., free plan available)
Endpoint: https://mcp.getshareglow.com/mcp
Tools: 7 (scan, templates, images, links, stats)
Registry: com.getshareglow/mcp (official MCP Registry)
Built by: Shareglow (github.com/Brandon-35/shareglow-mcp, MIT)
Listing: chatmcp/mcpso #5134 (Oct 2026)
```

## Why This Matters for Operators

Every product link that leaves the building - in a newsletter, a CRM sequence, a Slack message or a launch post - renders as a card somewhere, and that card is often the first and only impression. Broken or ugly previews are invisible in the CMS and obvious to every recipient.

Shareglow makes the preview itself a reviewable artifact: `scan_url` reads a public page's Open Graph and Twitter card metadata, shows how the link renders per platform, and returns the issues with fix suggestions. After the page changes, `refresh_preview` bumps the image cache-buster and re-scrapes the platforms so the new card actually shows.

**Branded share images without a designer:** `create_template_from_url` has AI design an image template from a site's brand, and `generate_og_image` renders 1200x630 images from it on demand - the same look across every campaign. Short links carry their own previews, including up to three A/B variants, with click stats broken down by day, country, device, browser and referrer.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `scan_url` | Scans a public page for Open Graph and Twitter card metadata, per-platform previews, and issues with fix suggestions |
| `refresh_preview` | Bumps the og:image cache-buster and re-scrapes platforms after a change |
| `create_template_from_url` | AI-designs an image template from a site's brand; returns the layout, variables and brand kit |
| `list_templates` | Lists the workspace templates with id, name, version and dimensions |
| `generate_og_image` | Renders a 1200x630 Open Graph image from a template; returns the permanent URL |
| `create_short_link` | Creates a short link with its own preview and up to three A/B variants |
| `get_link_stats` | Click analytics for a short link: totals plus day, country, device, browser and referrer breakdowns |

Every tool calls the REST API with the same key scope and counts against the same plan limits as the REST API, webhooks and GitHub Action.

## Installation

```bash
claude mcp add --transport http shareglow https://mcp.getshareglow.com/mcp \
  --header "Authorization: Bearer sk_live_..."
```

Claude Desktop and other stdio-only clients reach the hosted endpoint through the `mcp-remote` bridge, as documented at getshareglow.com/docs/mcp. Keys are created under Developer, API keys.

## Configuration

```json
{
  "mcpServers": {
    "shareglow": {
      "type": "http",
      "url": "https://mcp.getshareglow.com/mcp",
      "headers": { "Authorization": "Bearer sk_live_..." }
    }
  }
}
```

## Business Relevance

- **Marketing operators** can check every outbound link before it ships, instead of after a broken card appears in the wild
- **Founders announcing things** get branded, on-message preview images without a design round-trip
- **Growth teams** can A/B test link previews and read click breakdowns per campaign
- **Agencies** can run the same scan-and-fix loop across client sites on a schedule

## Integration with CorpusIQ

Shareglow closes the loop on content that starts in CorpusIQ: draft the post or email in the assistant, verify every link renders correctly, generate the branded card for the campaign, shorten with a tagged destination, and keep the click context beside the rest of the business data. The GA4 connector covers the destination page's behavior; Shareglow covers the hop before it - what people saw and clicked in the first place.

Pairs well with strict UTM discipline: put the tagged URL behind the short link so campaigns stay attributable even when the visible link is clean.

## Limitations

- Brand new (v0.1.0) - no track record yet
- API key required; free plan available but calls count against plan limits
- Template-based image generation, not a full design tool; AI template design consumes plan quota
- Short links and click stats overlap other catalogued link tools - the preview repair layer is the differentiator
- Scan results depend on the platforms' own caches; refresh exists because of exactly that

## FAQ

### What does it need to connect?

A Shareglow API key as a Bearer token (`sk_live_...`), created in the dashboard under Developer, API keys. The free plan is enough to start; all calls share the REST API's plan limits.

### What can it check and fix?

Scan any URL for Open Graph and Twitter card problems with fix suggestions and per-platform previews, then refresh the cache-buster and re-scrape so the platforms pick up the fixed card.

### Can it make share images without a designer?

Yes - `create_template_from_url` has AI build a template from a site's brand, and `generate_og_image` renders 1200x630 images from the template with a permanent URL.

### Does it do short links and analytics too?

Yes. `create_short_link` makes a short link with its own preview and up to three A/B variants, and `get_link_stats` returns click totals broken down by day, country, device, browser and referrer.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - all catalogued business-relevant servers
