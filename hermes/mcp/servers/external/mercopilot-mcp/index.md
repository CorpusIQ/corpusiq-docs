---
title: Mercopilot MCP
description: Shopify and Google Ads over MCP — connect your store and ad account to an AI assistant, ask plain-English questions about revenue and spend, get a ranked fix list, and approve changes applied directly in Shopify or Google Ads.
category: Marketing / Advertising
stars: n/a (new listing)
added: 2026-08-16
source: mcpservers.org
relevance: ★★★
tags: [shopify, google-ads, ecommerce, advertising, oauth, approvals]
---

# Mercopilot MCP

**Hosted commerce-operations server (Streamable HTTP, OAuth)** — Mercopilot connects a Shopify store and a Google Ads account to Claude, ChatGPT, and other MCP clients. Ask plain-English questions about store performance and ad spend, get a ranked list of what to fix and where to grow, and approve specific changes that are made directly in Shopify or Google Ads. No separate dashboard, no reports to download, no API key.

```
Server type: Hosted remote (Streamable HTTP)
Auth: OAuth — no API key; sign in with Mercopilot when the client prompts
Endpoint: https://api.mercopilot.com/mcp
Tools: 9 tools covering store performance, products, orders, and ad spend
Pricing: Commercial — account at mercopilot.com
Category: Marketing / Advertising
Built by: mercopilot.com
```

## Why This Matters for Operators

This is the exact problem CorpusIQ's audience runs every day: a Shopify operator with Google Ads spend and no time to dig through two dashboards. Mercopilot collapses both into a conversation. The questions it is built to answer are the operator questions — "Where am I losing money right now?", "Which slow sellers should I discount, and by how much?" — and every fix comes with what it is worth.

The architecture is approval-gated by design: anything that changes the store (price, title, stock, discount) is shown for approval before it happens. That matches the emerging production pattern across serious commerce MCPs — the agent proposes, the human approves, the change lands in the source system.

## Tools & Capabilities

Nine tools, split across the two connected surfaces:

| Area | Capability |
|---|---|
| Store analytics | Revenue, orders, and product performance in plain language |
| Fix recommendations | Ranked list of issues with estimated value per fix |
| Shopify mutations | Price, title, stock, and discount changes — approval-gated |
| Google Ads | Ad spend and campaign questions against the connected account |

## Installation

```bash
claude mcp add --transport http mercopilot https://api.mercopilot.com/mcp
```

Setup is four steps and about five minutes: (1) create a Mercopilot account and connect your `your-store.myshopify.com` domain (Shopify asks you to approve the install), (2) copy the MCP URL — it is the same for every store, (3) add it as a custom connector in Claude (Settings → Connectors) or with the command above, (4) toggle the connector on in a new chat. Connectors are off by default per conversation — the step people miss.

## Business Relevance

- **Shopify operators** replace dashboard digging with direct questions about revenue and stock
- **Ad spenders** get Google Ads context alongside store data in one thread
- **Lean teams** gain a ranked fix list with dollar estimates instead of intuition
- **Agencies** can connect client stores per workspace and review agent-proposed changes before they land

## Integration with CorpusIQ

Mercopilot and CorpusIQ share the same audience but different surfaces: CorpusIQ brings 40+ read-only business connectors (including Shopify and Google Ads) across accounting, analytics, and CRM; Mercopilot adds the conversational operating layer with approval-gated writes into Shopify and Google Ads. Together they bracket the operator workflow — CorpusIQ for the cross-source truth, Mercopilot for the ranked fix list and the gated execution of changes.

## Limitations

- Shopify plus Google Ads scope only — no other platforms connected
- Per-chat connector toggles cause "no access" confusion until users learn the pattern
- Write operations require the human approval loop, which is a feature and a ceiling for full autonomy
- Commercial service; pricing not published on the listing — verify before committing

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
