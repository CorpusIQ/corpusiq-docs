---
title: Linkonda MCP
description: Privacy-first short links over MCP — shorten, list, update and delete links with total redirect counts only, no visitor tracking data ever collected.
category: Marketing
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [short-links, link-management, privacy, marketing-ops, bulk-shortening, no-tracking, stdio, self-hosted]
---

# Linkonda MCP

**MCP server (stdio via npx, optional API key)** — creates and manages Linkonda short links from Claude, Claude Code, Cursor, or any other MCP client. Linkonda records a total redirect count per link and nothing else — no IP addresses, geolocation, device data, or referrers.

```
Server type: stdio (npx -y @veranoapp/linkonda-mcp)
Auth: None for anonymous mode; LINKONDA_API_KEY for persistent links
Endpoint: api.linkonda.com (vendor API, client runs locally)
Tools: 7 (shorten_link, shorten_links_bulk, list_links, update_link, delete_link, get_link_stats, check_quota)
Pricing: anonymous free; persistent links require a paid plan
Category: Marketing
Built by: Verano (linkonda.com) — npm @veranoapp/linkonda-mcp
```

## Why This Matters for Operators

Agents generate links in bulk — every campaign, every share, every report. With a tracking shortener, that bulk generation quietly builds a visitor dataset you then have to secure, retain, and answer requests about. Linkonda's model removes the liability: the service records only a per-link redirect total, so there is no visitor dataset to protect because there is no visitor data at all.

**The anonymous tier works immediately**: no key, no account, shorten links on install — capped per network and expiring after 30 days. Add a key when links need to persist and be managed. Bulk shortening is partial-success by design: some entries can fail on quota or an invalid URL while others are created, and the tool reports both lists rather than only the successes. For workflows that do need click attribution, the vendor's own docs point at tracking shorteners instead — the honest boundary is part of the product.

## Tools & Capabilities

| Tool | Purpose | Key required |
|---|---|---|
| `shorten_link` | Shorten one URL | No |
| `shorten_links_bulk` | Shorten up to 100 URLs in one request | Yes |
| `list_links` | List your links with destinations and click counts | Yes |
| `update_link` | Change a destination, pause or resume a link | Yes |
| `delete_link` | Permanently delete a link | Yes |
| `get_link_stats` | Total redirect count for a link | No |
| `check_quota` | Links live versus plan allowance | No |

## Installation

```bash
npx -y @veranoapp/linkonda-mcp
```

## Configuration

```json
{
  "mcpServers": {
    "linkonda": {
      "command": "npx",
      "args": ["-y", "@veranoapp/linkonda-mcp"],
      "env": { "LINKONDA_API_KEY": "lk_your_key_here" }
    }
  }
}
```

Create the key in the Linkonda dashboard under API keys (shown once). `LINKONDA_API_BASE_URL` points at another instance if self-hosting.

## Business Relevance

- **Marketing operators** shorten campaign links in bulk without creating a tracking liability
- **Privacy-first businesses** get link shortening with a defensible no-tracking answer
- **Content teams** can manage, pause, and update links without leaving the agent workflow
- **EU operators** avoid a referrer-and-IP dataset that GDPR turns into work

## Integration with CorpusIQ

Linkonda slots into the CorpusIQ content and email stack as the link layer. A CorpusIQ workflow can draft a campaign, shorten every destination through Linkonda, and send through the CorpusIQ email connectors — with the compliance answer baked in: Linkonda holds no visitor data, so the only tracking signals come from the platforms themselves (GA4 sessions, Klaviyo clicks) that CorpusIQ already reads. The composition keeps click attribution where the analytics connectors own it and keeps the link layer clean. For public content, the CorpusIQ public-content guard can pair Linkonda's anonymous tier with share links that carry no tracking weight at all.

## Limitations

- Brand new — no track record yet; listed August 17, 2026
- No per-visitor attribution — geographic, device, and referrer breakdowns are never collected
- Anonymous links expire after 30 days; persistence requires a paid plan
- stdio client only — no hosted MCP endpoint published
- Bulk tools require the paid plan

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
