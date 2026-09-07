---
title: "Ambassly MCP - Affiliate Program Operations for Agents"
description: "Ambassly MCP is the hosted MCP server for Ambassly's affiliate program platform: company-scoped tools list programs, report commission totals by currency, review and approve or reject pending commissions, create affiliate invitations and prepare payout batches; affiliate-scoped tools show creator stats, links and referral-link creation."
category: Marketing
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3969"
relevance: ★★★
tags: [affiliate, referral, commissions, payouts, marketing, remote-mcp, hosted]
---

# Ambassly MCP - Affiliate Program Operations for Agents

**Remote MCP server (Streamable HTTP, scoped API keys)** - Ambassly's official hosted MCP server brings affiliate program operations into any MCP client. Company-scoped keys manage programs, commissions and payouts; affiliate-scoped keys show creator stats and create referral links. Write tools affect the authenticated account and should only run with the operator's authorization.

```
Server type: Remote (Streamable HTTP)
Auth: Scoped company or affiliate API key, sent as a bearer authorization header
Endpoint: https://ambassly.com/api/mcp (probe-verified live; 401 invalid_token without auth)
Tools: Company-scoped and affiliate-scoped program, commission and payout operations
Pricing: Hosted commercial service; account and API access required
Category: Marketing
Built by: Ambassly (ambassly.com); docs at ambassly.com/docs/mcp
```

## Why This Matters for Operators

Affiliate program administration is spreadsheets and portals: commission totals, pending approvals, payout batches and creator invitations each live in their own screen. Ambassly MCP collapses them into the agent, with the scoping model doing the safety work: a company-scoped key sees programs and commissions, an affiliate-scoped key sees only the creator's own stats and links.

**The write surface is explicitly operator-authorized: approve, reject and payout tools affect the authenticated account, so the agent's role is preparation and execution under direction, not autonomous decision-making over money movement.**

## Tools & Capabilities

| Scope | What the agent does |
|---|---|
| Company - programs | Lists affiliate programs and their configuration |
| Company - commissions | Reports commission totals by currency, lists and reviews pending commissions |
| Company - decisions | Approves or rejects commissions |
| Company - recruiting | Creates affiliate invitations |
| Company - payouts | Prepares payout batches |
| Affiliate | Shows the creator's stats and links; creates referral links |

## Installation

Create a company or affiliate API key in the Ambassly dashboard or portal settings, then add the endpoint to any Streamable HTTP MCP client.

```json
{
  "mcpServers": {
    "ambassly": {
      "url": "https://ambassly.com/api/mcp",
      "headers": {
        "Authorization": "Bearer amb_YOUR_API_KEY"
      }
    }
  }
}
```

## Configuration

The public docs at ambassly.com/docs/mcp include Claude Code and Cursor setup. Authenticated initialization and company-scoped read calls were verified against the endpoint on Sep 6, 2026 by the vendor's submission; our probe confirms the endpoint enforces auth with an invalid_token response.

## Business Relevance

- **Growth teams** run affiliate recruiting, commission review and payout prep from the agent.
- **Finance teams** reconcile commission totals by currency before payouts are batched.
- **Creators and partners** check their own stats and mint referral links without contacting the company.
- **Marketplaces** offer affiliate-scoped keys to partners as a native agent surface.

## Integration with CorpusIQ

Ambassly administers the referral motion; CorpusIQ measures whether it converts. A composed workflow: the agent approves commissions in Ambassly based on the attributed revenue verified in CorpusIQ's Stripe and GA4 connectors, closing the loop between referral activity and real business performance.

## Limitations

- Brand new listing (issue #3969, Sep 6, 2026); hosted commercial service with no public repository.
- No anonymous mode; all operations require an account and API key.
- Tool names are capability-level from the vendor's submission and docs; the full list is served after authentication.

## See Also

- [BulkPublish MCP - Multi-Platform Social Publishing for Agents](/hermes/mcp/servers/external/bulkpublish-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
