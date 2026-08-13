---
title: JaxSuite AI MCP
description: AI-native cold outreach and CRM platform — 27 MCP tools for campaign lifecycle, content writing, contact management, and deliverability analytics
category: Marketing / Sales
stars: 0 (brand new)
added: 2026-08-11
source: mcpservers.org
relevance: ★★★
tags: [cold-outreach, email, crm, sales, b2b, deliverability, campaigns]
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/jaxsuite-ai-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# JaxSuite AI MCP

**AI-native cold outreach and CRM platform with built-in deliverability, a 300M+ verified B2B contact database, and an MCP server that lets AI agents run campaigns end to end.**

```
Server type: Remote (Streamable HTTP)
Auth: API token (Bearer)
Endpoint: https://www.jaxsuite.com/api/v1/mcp
Rate limit: 20 calls/hour, 100 calls/day per token
Category: Sales / Cold Outreach / CRM
```

## Why This Matters for Operators

Cold outreach is the highest-ROI growth channel for B2B operators, but running it effectively requires juggling: contact databases, email verification, content writing, campaign management, deliverability monitoring, and analytics. JaxSuite AI MCP consolidates all of this into 27 tools that AI agents can orchestrate — no browser tab needed.

This is the first end-to-end cold outreach MCP server with built-in deliverability infrastructure. Combined with [LinkedIn MCP (GTM API)](/hermes/mcp/servers/external/linkedin-mcp-gtm/) and [Apollo.io MCP](/hermes/mcp/servers/external/apollo-io-mcp/), operators can build fully autonomous B2B outbound pipelines.

## Tools & Capabilities (27 tools)

### Campaign Lifecycle (7 tools)
| Tool | Description |
|---|---|
| List Campaigns | List all campaigns accessible to your token |
| Get Campaign | Fetch full details for a single campaign |
| Create Campaign | Create a new outreach campaign |
| Pause Campaign | Pause a running campaign |
| Resume Campaign | Resume a paused campaign |
| Delete Campaign | Remove a campaign |
| Schedule Campaign / Get Schedule | Set or read campaign scheduling |

### Content Writing (3 tools)
| Tool | Description |
|---|---|
| Write Campaign Content | Write multi-step, multi-variant email content with personalization, spintax, and unsubscribe links |
| Update Campaign Step Content | Surgically patch a single step's content |
| Get Campaign Content | Read back current campaign content |

### Campaign Settings (2 tools)
| Tool | Description |
|---|---|
| Get Campaign Settings | Read tracking, send pacing, bounce protection, ESP routing |
| Update Campaign Settings | Patch campaign configuration |

### Contacts (5 tools)
| Tool | Description |
|---|---|
| Upload Contacts | Add contacts to a campaign |
| List Campaign Contacts | List all contacts in a campaign |
| Get Campaign Contacts | Fetch individual contact details |
| Update Campaign Contacts | Modify contact data |
| Remove Campaign Contacts | Remove contacts from a campaign |

### Sending Accounts (6 tools)
| Tool | Description |
|---|---|
| List Email Accounts | Discover available mailboxes |
| List Email Account Tags | View mailbox tags |
| Get Campaign Sending Accounts | See what a campaign sends from |
| Add/Remove Campaign Sending Accounts | Attach or detach senders |
| Update Campaign Sending Accounts | Modify sender configuration |

### Deliverability & Analytics (3 tools)
| Tool | Description |
|---|---|
| Get Campaign Analytics | Pull performance stats |
| Check Content Deliverability | Pre-flight spam risk check |
| Get Campaign Sender Health | Monitor sender reputation |

## Configuration

```json
{
  "mcpServers": {
    "jaxsuite": {
      "type": "streamableHttp",
      "url": "https://www.jaxsuite.com/api/v1/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_API_TOKEN>"
      }
    }
  }
}
```

## Getting Started

1. **Sign up** at [jaxsuite.com](https://www.jaxsuite.com/auth/signin/signup)
2. **Generate API token** from Settings → API in your JaxSuite dashboard
3. **Add config** to your MCP client
4. **Start prompting**: "Create a cold outreach campaign targeting SaaS founders, write a 3-step email sequence with spintax, upload these 50 contacts, check deliverability, and schedule it for Monday"

## Use Cases for Business Operators

- **B2B SaaS founders**: Run outbound sequences without a sales team
- **Agencies**: Manage multiple client outreach campaigns from one AI agent
- **Growth operators**: A/B test email sequences at scale
- **Fractional sales leaders**: Delegate campaign execution to AI agents

## Rate Limits

- 20 calls per hour per token
- 100 calls per day per token
- Workspace-scoped (token only accesses your team's data)

## Limitations

- Brand new server (August 2026) — API may evolve
- Rate limits may constrain high-volume operators
- Not open source (commercial SaaS product)
- Requires paid JaxSuite plan (pricing details on their website)

## See Also

- [LinkedIn MCP (GTM API)](/hermes/mcp/servers/external/linkedin-mcp-gtm/) — LinkedIn outreach at scale
- [Apollo.io MCP](/hermes/mcp/servers/external/apollo-io-mcp/) — 275M+ B2B contact enrichment
- [JaxSuite API Docs](https://www.jaxsuite.com/api/v1/docs/ui)
- [JaxSuite MCP Page](https://www.jaxsuite.com/mcp)
