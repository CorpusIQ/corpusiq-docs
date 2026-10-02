---
title: "Flyn MCP - Short Links, Click Analytics and QR Codes"
description: "Remote MCP from Flyn, a URL shortener built for AI assistants: 8 tools create and re-point short links, pull click analytics with country, device and referrer detail, and generate QR codes, with Google Safe Browsing checks and destructive-action confirmations. OAuth on the free plan."
category: Marketing
stars: n/a (hosted)
added: 2026-08-27
source: "mcpservers.org /all page 2 (www-flyn-to-ai)"
relevance: ★★
tags: [url-shortener, link-analytics, qr-codes, click-tracking, marketing-ops, remote-mcp]
---

# Flyn MCP

**Hosted remote MCP server (Streamable HTTP, OAuth sign-in or Bearer API key) for short links and QR codes.** Flyn's MCP exposes its whole dashboard as 8 tools: shorten any URL into a trackable flyn.to link, re-point a live link without changing the printed URL, pull click analytics with timing and referrer detail, and generate QR codes - including WiFi-network and plain-text codes. Every request is scoped to the authenticated account, destinations are checked against Google Safe Browsing before going live, and destructive actions are annotated so assistants confirm before deleting.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in on any plan (including free) or Bearer API key (Pro / Lifetime / Team)
Endpoint: https://www.flyn.to/mcp
Tools: 8
Pricing: Free plan 25 links/month with click totals; paid adds country/device/referrer detail, custom domains, up to 5 API keys
Docs: https://www.flyn.to/ai
Category: Marketing
```

## Why This Matters for Operators

Short links carry marketing attribution, and re-pointing one is usually a dashboard errand. Flyn puts it in the assistant that already writes the campaigns: "shorten the spring-sale URL", "how many clicks did the launch link get", "re-point flyn.to/menu to the new page". **The re-point trick is the operator win: printed QR codes and old URLs keep working while the destination moves, because the code encodes the short link, not the target.** Team roles carry over (viewers cannot create or edit), and revoked keys stop working instantly.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `create_short_link` | Shorten any URL into a trackable link, with optional custom slug and expiration |
| `list_links` | Search and browse links by text, tag or status |
| `get_link` | One link with destination, settings and total clicks |
| `update_link` | Re-point a live short link to a new destination without changing the printed URL |
| `delete_link` | Permanently remove a link (flagged destructive for confirmation) |
| `get_link_analytics` | Click events with totals, timing, country, device and referrer detail (per plan) |
| `get_link_qr_code` | Scannable QR for a link, shown in chat; re-pointable after printing |
| `create_qr_code` | QR for a URL, plain text or WiFi network; vCard/email/call/SMS on Pro |

## Installation

```bash
claude mcp add --transport http flyn https://www.flyn.to/mcp \
  --header "Authorization: Bearer flyn_sk_live_YOUR_KEY"
```

Keep the `www.` in the URL - without it the address redirects and the connector finds no tools. OAuth-capable clients add the bare URL and sign in through the browser on any plan.

## Configuration

```json
{
  "mcpServers": {
    "flyn": {
      "url": "https://www.flyn.to/mcp",
      "headers": {
        "Authorization": "Bearer flyn_sk_live_YOUR_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Marketing teams** shorten campaign links and read click analytics without the dashboard
- **Restaurants and retail** print re-pointable QR codes for menus and table cards
- **Event operators** make WiFi QR codes and expiring promo links in conversation
- **Affiliates** tag and track links while Safe Browsing keeps destinations clean

## Integration with CorpusIQ

Flyn handles the link layer of campaigns; CorpusIQ measures the conversion layer behind them. A Flyn short link's click analytics show the top of funnel, while CorpusIQ's GA4 and Shopify connectors show what those clicks actually bought - the two joined give a full click-to-revenue picture per campaign. For printed-material campaigns (menus, table cards, packaging), Flyn's re-pointable codes pair with CorpusIQ's revenue reporting to test new landing pages without reprinting anything.

## Limitations

- Free plan caps at 25 links/month with click totals only
- API keys are a paid-plan feature (free plan uses OAuth sign-in)
- Analytics depth follows plan tier; downgrades drop back to totals
- Not listed in Claude or ChatGPT directories yet - add as a custom connector
- Link destinations must pass Google Safe Browsing and AUP checks

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
