---
title: Cold Leads MCP - Contact and Outreach Management for Agents
description: "MCP server letting an agent manage contacts, verify addresses, read conversations and draft outreach campaigns, with sending behind user confirmation."
category: Marketing
stars: n/a (hosted service, coldleads.app)
added: 2026-10-01
source: "mcpservers.org /all (coldleads-app-use-cases)"
relevance: ★★★
tags: [crm, contacts, email-verification, outreach, lead-generation, sales, remote-mcp]
---

# Cold Leads MCP

**Contact management and outreach where the agent drafts and the human sends.** Cold Leads exposes its contact workspace over MCP, so an assistant can work with contacts already in the workspace, import structured rows, verify email addresses, read synced conversations and maintain campaign drafts - while sending stays behind explicit user confirmation and the platform's consent and unsubscribe safeguards.

```
Server type: Remote (Streamable HTTP) plus Node SDK
Auth: secret key (Business plan) for the API
Endpoint: hosted MCP endpoint from Cold Leads
Tools: contacts, import, verification, conversations, templates, campaign drafts, lead forms
Pricing: Business plan required for API access
Category: Marketing
Built by: Cold Leads
```

## Why This Matters for Operators

The failure mode this server fixes is the assistant that invents contacts when asked for a list. By grounding the assistant in the workspace's own contact data, imports and synced conversations, Cold Leads makes an agent's outreach answers traceable to real records. Bulk email verification is the second workhorse: the documented n8n recipe sends up to 5,000 addresses as a single job, polls for results and writes status, score, reason and next step back into the rows - a job that is painful to script by hand.

The send gate is the right default. Drafts, templates, verification and reads are agent work; the send is confirmed by a person, with consent, unsubscribe and DNC safeguards applied per contact.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Contacts | Work with contacts already in the workspace |
| Import | Bring structured rows in from a user-provided file |
| Verification | Verify email addresses, including bulk jobs with score and reason |
| Conversations | Read synced email conversations |
| Templates | Maintain outreach templates |
| Campaign drafts | Build outbound campaigns (sending behind user confirmation) |
| Lead forms | Set up website lead capture forms |

The listing documents the server's capability set through its use-case recipes; exact tool identifiers are published in the vendor's own recipe configs rather than the directory page, so this guide describes the capability surface.

## Installation

```
claude mcp add --transport http coldleads https://<workspace-endpoint>/mcp
```

The hosted endpoint is published from the Cold Leads workspace; connect with the account's secret key. A Node SDK is also offered for programmatic use.

## Configuration

```json
{
  "mcpServers": {
    "coldleads": {
      "type": "http",
      "url": "https://<workspace-endpoint>/mcp"
    }
  }
}
```

## Business Relevance

- **Sales and SDR teams** can have an agent draft campaigns and clean contact lists while sending stays with a person.
- **Growth and lifecycle marketing** can run bulk verification with an agent and write status back to the source sheet.
- **RevOps** can consolidate contact records, verification status and conversation history in one agent surface.
- **AI agents** get grounded access to real contact and conversation data rather than reconstructing contacts from memory.

## Integration with CorpusIQ

CorpusIQ holds the business data - customers, revenue, product usage - and Cold Leads holds the outbound contact layer. An agent can read which accounts are worth pursuing from CorpusIQ, then pull the matching contacts, verify their addresses and draft the outreach in Cold Leads, so targeting logic and outreach execution share one workflow with the business record as the source of truth.

## Limitations

- The API needs a secret key from the Business plan; there is no free API tier.
- Sending is gated on explicit user confirmation and the platform's consent and unsubscribe safeguards, so it is not an unattended bulk-send path.
- The public listing documents the surface through use-case recipes; exact tool names live in the vendor's configs.
- Verification credits and campaign limits apply per the account plan.

## FAQ

### What does the Cold Leads MCP server do?

It lets an AI agent manage contacts, import rows, verify email addresses, read synced conversations, maintain templates and build campaign drafts, with sending behind explicit user confirmation.

### Can an agent send outreach without a person confirming?

No. Sending is gated on user confirmation, with consent, unsubscribe, DNC and content safeguards applied per contact.

### Does it need a specific plan?

Yes. API access requires the Business plan and a secret key from the account.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
