---
title: "Subtraq MCP - Link Attribution and Sales Tracking"
description: "Short links with per-placement UTMs, click analytics and attributed sales your AI can create, read and report on per client workspace."
category: Marketing
stars: n/a (new listing)
added: 2026-10-06
source: "chatmcp/mcpso issue #4798"
relevance: ★★
tags: [marketing, attribution, links, utm, analytics, ecommerce, remote-mcp]
---

# Subtraq MCP

**Remote MCP server (Streamable HTTP, API key)** - short links, click tracking and sales attribution for agents. Subtraq organises links into workspaces (one per client, brand or project), splits "parent" links from the UTM-carrying "placements" you publish per post, and reads back the numbers that matter: clicks, leads, sales, and attributed versus unattributed revenue. Eight tools, one API key, no SDK to install.

```
Server type: Remote (Streamable HTTP)
Auth: API key (stq_sk_...) created under Settings, API Keys
Endpoint: https://subtraq.co/api/mcp
Tools: 8 (spaces, links, analytics, sale tracking)
Pricing: Free plan, no credit card; plan limits apply to links created
Built by: Subtraq (subtraq.co)
Registry: co.subtraq/subtraq
```

## Why This Matters for Operators

Attribution is the gap between "we posted a lot" and "this made money". Operators and agencies publish links across newsletters, social posts, booths and chats, and then cannot say which placement brought the sale without a spreadsheet of UTMs. Subtraq makes links and their outcomes a conversational surface: the agent creates the link mid-draft, reads back clicks over 30 days, and reports attributed revenue client by client.

**One workspace per client, one parent link per destination, one placement per post.** A parent link carries the destination; placements inherit it and carry their own UTMs, so a newsletter link and a social link point to the same place and still count separately. Names and addresses can change without breaking anything: old short URLs keep redirecting to the same destination and their clicks stay on the link. Links are never deleted, only archived, so history survives reorganisations.

The offline-sale case is the sleeper feature. A contract signed over the phone can be recorded with `track_sale`, tied back to the person's originating placement, idempotent by invoice id, so the channel that actually converted finally gets credit.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `list_spaces` / `create_space` | List or create client workspaces (one per client, brand or project) |
| `list_links` / `get_link` | List links; detail a link with its final destination (UTMs included) and 30-day clicks |
| `create_link` | Create a parent link from a destination, or a placement that inherits it and adds UTMs |
| `update_link` | Change destination, label or address; old addresses keep redirecting; archive instead of delete |
| `get_analytics` | Clicks, leads, sales, attributed and unattributed revenue, placement by placement (amounts in cents) |
| `track_sale` | Record a sale tied to the originating placement; idempotent by `invoiceId`; cannot be sent from a browser |

## Installation

```bash
claude mcp add --transport http subtraq https://subtraq.co/api/mcp
```

Then create an API key in Subtraq under Settings, API Keys, and send it as an `Authorization: Bearer` header.

## Configuration

```json
{
  "mcpServers": {
    "subtraq": {
      "url": "https://subtraq.co/api/mcp",
      "headers": {
        "Authorization": "Bearer stq_sk_your_key"
      }
    }
  }
}
```

The MCP server and the v1 REST API share the same registry: the tool list is imported from what the server exposes, and the same key drives both surfaces.

## Business Relevance

- **Agencies** keep one workspace per client and answer "what brought in revenue this week, client by client" in plain language.
- **E-commerce and DTC operators** attribute sales to the placement that earned them, including offline and phone sales.
- **Newsletter and community operators** create placement links while drafting, without leaving the conversation.
- **Marketing leads** read attributed versus unattributed revenue to see how much of the funnel is actually measured.

## Integration with CorpusIQ

CorpusIQ is the system of record for what happened inside the business: Stripe, Shopify and QuickBooks show the revenue, GA4 shows on-site behaviour, Google Ads and Meta Ads show spend. Subtraq sits at the front of the funnel, marking which link, post or placement the person arrived through. Composed, an operator can reconcile campaign-level attribution against the actual revenue numbers in one conversation, and flag the gap between what attribution claims and what the accounting system counted.

## Limitations

- Free plan; your plan's limits apply to links created, wherever they come from.
- Amounts are in cents and are not currency-converted: when `mixedCurrencies` is true, totals only cover one currency.
- Attribution depends on the model chosen; the response always says which one was used.
- Archived links stop redirecting (old addresses included); only history remains.
- Brand new listing: no track record from this catalog yet.

## FAQ

### Does my agent need an SDK?

No. Subtraq exposes one endpoint with standard MCP: initialize, tools/list, tools/call. One URL and one API key is the whole setup.

### Can editing a link break what I already published?

No. Changing a link's address keeps the old address redirecting to the same destination, and placements that shared the domain follow the change. History stays on the link.

### How do offline sales get attributed?

Call `track_sale` with the amount and the originating placement; pass an `invoiceId` and replays are idempotent, so a retried call never records twice.

### What does it cost?

The plan is free to start with no credit card; your plan's limits apply to links created.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Cello MCP - Referral Program Intelligence for Agents](/hermes/mcp/servers/external/cello-mcp/)
- [RouterGrowth MCP - GTM Data and Actions for Agents](/hermes/mcp/servers/external/routergrowth-mcp/)
