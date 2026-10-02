---
title: "More Good Reviews MCP - Review Management and Reputation Ops"
description: "Official More Good Reviews MCP server for reputation operations: work with customers, review requests, reviews, ratings, feedback, messages, locations, sources, tags, charges, and share templates in plain language, project-scoped with sign-in auth."
category: Marketing
stars: n/a (hosted)
added: 2026-08-25
source: mcpservers.org /all listing
relevance: ★★
tags: [mcp-server, reviews, reputation, google-reviews, customers, feedback]
---

# More Good Reviews MCP

**Reputation management, operated from chat.** More Good Reviews is a review-generation and reputation platform. Its MCP server connects assistants such as Claude to one project at a time so operators can work in plain language with customers, review requests, reviews, ratings, feedback, messages, locations, sources, tags, charges, and share templates. A separate Agency MCP server manages clients, team seats, and every business at once for white-label agencies.

```
Server type: Remote (hosted, per-project URL)
Auth: Sign-in flow (no API key hunting)
Scope: One project per connection, fixed by the URL you paste
Agency variant: /agencies/mcp-server for white-label multi-business management
Docs: docs.moregoodreviews.com/platform/mcp-server
```

## Why This Matters for Operators

Reviews are revenue, and the workflow is scattered: request reviews, read what came in, publish replies to Google and Facebook, and clean data. More Good Reviews puts the whole loop in the assistant with guardrails: integrations do not bypass your throttles or unsubscribe rules, Google/Facebook replies publish only after you confirm each draft, and access is project-scoped so an assistant connected to one business cannot touch another.

## Tools & Capabilities

Capability-level table from the vendor's MCP documentation (exact tool names are listed per project after connecting):

| Capability | What it does |
|---|---|
| Customers | Look up, add, update, tag, archive, or restore directory records; inspect related charges, messages, and reviews |
| Review requests | Schedule email or SMS requests per your strategy, reminders, eligibility, and sending limits |
| Reviews | Search and read feedback; create reviews manually; set hidden or duplicate flags; tag; mark as replied; publish replies to Google or Facebook; generate share images from saved templates |
| Messages | Review outbound history for delivery summaries; remove individual messages for audit tidiness |
| Locations | List, add, edit, or remove locations for multi-site attribution |
| Charges | Record or delete spend signals tied to customers for billing sync |
| Sources and tags | Maintain the sources catalog and the tag vocabulary used across customers and reviews |
| Share templates | List saved layouts for social-style review graphics |

## Installation

In the product: open Settings → MCP Server in the project, copy the MCP Server URL (it already includes the project identifier), and paste it into your assistant's connector setup. Use the exact value; do not substitute a generic host-only link.

## Configuration

Sign-in based, not API-key based: the assistant completes the platform's sign-in and the connection is scoped to the project in the URL. Revoke access per connected app from Settings → MCP Server at any time. White-label agencies use the Agency MCP Server URL instead.

## Business Relevance

- **Review velocity:** schedule requests and monitor inflow from chat.
- **Reply operations:** draft and publish Google and Facebook replies with a confirm gate.
- **Data hygiene:** moderation flags, duplicates, and tagging without opening the dashboard.
- **Agency scale:** one assistant flow across client businesses via the Agency server.

## Integration with CorpusIQ

More Good Reviews' customer and review data pairs with CorpusIQ connectors for the growth stack: pull review counts into Airtable or Notion reports, join customer records with your CRM in HubSpot or Close, and render reputation dashboards next to marketing metrics.

## Limitations

- One project per connection; multi-business access requires the Agency MCP server.
- Capability-level tool list published in vendor docs; exact tool names appear after sign-in.
- Google/Facebook reply publishing depends on those integrations being connected to the project.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Xpoz MCP - Social Media Intelligence](/hermes/mcp/servers/external/xpoz-mcp)
