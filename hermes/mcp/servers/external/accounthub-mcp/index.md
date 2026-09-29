---
title: "AccountHub MCP - Gmail, Calendar, Drive, Slack and Notion"
description: "AccountHub gives an AI assistant one MCP connection to Gmail, Google Calendar, Drive, Contacts, Slack and Notion, free."
category: Productivity
stars: n/a (new listing)
added: 2026-09-29
source: "mcp.so server page (accounthub.ai)"
relevance: ★★★
tags: [productivity, gmail, google-calendar, google-drive, slack, notion, workspace, remote-mcp]
---

# AccountHub MCP

**One MCP connection for the tools a team already lives in.** AccountHub gives an AI assistant a single endpoint covering Gmail, Google Calendar, Drive, Contacts, Slack workspaces and Notion, so one sign-in replaces six separate integrations.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth per connected account
Endpoint: https://accounthub.ai/api/mcp
Tools: email, calendar, drive files, contacts, Slack messaging, Notion pages
Pricing: free
Category: Productivity
Built by: AccountHub (accounthub.ai)
```

## Why This Matters for Operators

The connective-tissue work of a business runs through email, calendar, files, chat and notes, and an assistant is only useful if it can reach all of them without a connector zoo. AccountHub consolidates that surface behind one endpoint, which means fewer tokens to manage, fewer permission screens and one place to revoke access.

For an operator handing routine work to an agent, that consolidation is the difference between an assistant that can actually complete a cross-tool task (read the email, check the calendar, file the doc, message the channel) and one that stalls at the second tool.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Gmail | Read and manage mail from one connection |
| Google Calendar | List, create and update events |
| Drive and Contacts | Read and organize files and contact records |
| Slack | Read and post in connected workspaces |
| Notion | Read and write pages and databases |

Tool names are served from the endpoint; the table reflects the vendor's published capability set.

## Installation

```bash
claude mcp add accounthub --transport http https://accounthub.ai/api/mcp
```

Connect each account through the OAuth flow; the vendor publishes a setup guide at accounthub.ai/guide.

## Configuration

```json
{
  "mcpServers": {
    "accounthub": {
      "type": "http",
      "url": "https://accounthub.ai/api/mcp"
    }
  }
}
```

## Business Relevance

- **Founders and chiefs of staff** delegate inbox, calendar and note tasks to one assistant connection
- **Small teams** avoid paying per-connector tool subscriptions for everyday workspace access
- **Agencies** connect client-facing mail and calendars without separate integrations per client tool
- **Ops teams** give agents read-write reach across the stack they already use daily

## Integration with CorpusIQ

AccountHub covers the workspace layer while CorpusIQ covers the business-data layer. A single assistant can read Gmail threads through AccountHub and reconcile them against Stripe payments, QuickBooks invoices and CRM deals through CorpusIQ connectors, closing the loop between what customers say and what the financial record shows.

For support-heavy operations, combine AccountHub mail access with CorpusIQ ticket and revenue connectors so the agent can answer from both the conversation and the account history in one session.

## Limitations

- Brand new listing, no track record yet
- No public repository or published tool catalog
- Tool depth per service is not documented on the listing
- Free tier limits are not published on the directory listing
- Consolidation means one compromised token reaches several systems, so keep sign-out hygiene tight

## FAQ

### What does one connection actually cover?

Gmail, Google Calendar, Google Drive, Contacts, Slack workspaces and Notion, all behind the single endpoint at accounthub.ai/api/mcp.

### Is it really free?

The listing advertises the service as free. Long-term pricing is not published, so treat it as a free launch state rather than a guaranteed perpetual price.

### How is this different from connecting each tool separately?

One endpoint, one auth flow and one revocation point instead of six connectors, which cuts token management and setup time and keeps the assistant's tool surface smaller.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
