---
title: Mailercloud MCP - Email Marketing Operations for Agents
description: Connect AI assistants to the Mailercloud email marketing platform. Manage campaigns, contacts, lists and templates, run sends, and pull AI-powered campaign analysis and deliverability audits from a hosted Streamable HTTP endpoint.
category: Communication & Email
stars: n/a (new listing)
added: 2026-09-08
source: mcp.so
relevance: ★★★
tags: [email-marketing, campaigns, contacts, deliverability, automation, email, remote-mcp]
---

# Mailercloud MCP

**Remote MCP server (Streamable HTTP, API key)** - the official Mailercloud MCP server puts the full email marketing platform in front of AI assistants: campaigns, contacts, lists, templates, sending, plus AI-powered campaign analysis and deliverability audits, all through one hosted endpoint. Listed Verified + Featured on mcp.so with a live, auth-gated endpoint probe-confirmed.

```
Server type: Remote (Streamable HTTP)
Auth: API key
Endpoint: https://mcp.mailercloud.com/mcp
Tools: campaign, contact, list, template, sending and analysis tools (live tool list served from the endpoint)
Pricing: Mailercloud platform plans (free tier + paid)
Category: Communication & Email
Built by: Mailercloud (mailercloud.com)
```

## Why This Matters for Operators

Email marketing is one of the last manual-heavy operator workflows. List hygiene, campaign setup, template updates and send tracking still mean clicking through a web UI, and performance review usually means exporting CSVs and rebuilding charts by hand. **Mailercloud MCP lets an agent run that loop end to end**: create and update campaigns, manage contacts and lists, build and reuse templates, trigger sends, then pull AI-powered campaign analysis and deliverability audits back into the conversation.

The deliverability angle is the differentiator. Instead of reacting to a degraded sender reputation after open rates fall, an agent can pull deliverability audits on demand and catch list quality or authentication problems before they burn the domain. The agent-facing surface turns "check my email performance" from a dashboard task into a plain-language question with a working answer.

## Tools & Capabilities

The listing does not publish a static tool list - the live tool list is served from the endpoint once a client authenticates. Capability areas per the official listing:

| Area | What the agent can do |
|---|---|
| Campaigns | Create, update, review and send email campaigns |
| Contacts | Manage subscribers, segments and list membership |
| Lists | Build and maintain audience lists |
| Templates | Create, edit and reuse email templates |
| Sending | Trigger and track campaign sends |
| AI analysis | AI-powered campaign performance analysis |
| Deliverability | Deliverability audits and diagnostics |

## Installation

```bash
claude mcp add mailercloud --transport http https://mcp.mailercloud.com/mcp
```

Per-client setup snippets (Claude Code, Codex, Cursor, VS Code) are published on the mcp.so listing and in the Mailercloud help center.

## Configuration

```json
{
  "mcpServers": {
    "mailercloud": {
      "type": "http",
      "url": "https://mcp.mailercloud.com/mcp"
    }
  }
}
```

Authentication uses a Mailercloud API key - create one in the Mailercloud dashboard and attach it to the client connection as the API-key authorization header. The endpoint returns HTTP 401 to unauthenticated requests, which confirms the hosted server is live and gated as documented.

## Business Relevance

- **E-commerce operators** get campaign sends, contact syncing and performance analysis without leaving the agent conversation
- **Marketing teams** keep templates and campaigns under agent control so weekly sends become a repeatable, reviewable routine
- **Agencies** managing multiple client lists get one MCP surface to run campaigns across accounts
- **Founders without a marketing hire** get deliverability audits and AI campaign analysis on demand instead of hiring an email consultant for every question

## Integration with CorpusIQ

Mailercloud MCP pairs naturally with the CorpusIQ connector surface: CorpusIQ's Shopify connector reads the customer and order data that feeds Mailercloud segments, and the HubSpot or contact connectors keep the audience lists aligned between CRM and email platform. The composed workflow runs one direction - CorpusIQ reads the business, Mailercloud executes the outreach - with GA4 closing the loop on how campaign traffic converts after the send. Operators get a single conversation that spans "who should get this campaign" through "how did it perform", instead of three separate dashboards.

## Limitations

- Brand new listing (September 8, 2026) - no track record, tool list not yet captured by the directory
- Hosted endpoint only - no self-host or stdio option
- API-key auth means key rotation and scoping discipline sit with the operator
- Free-tier caps on the Mailercloud platform apply to sends and contact volume
- Tool names and schemas change as the vendor iterates - re-list tools after connecting

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/hermes/mcp/servers/external/imap-mcp)
- [BusyMail MCP - Human-Approval Email over MCP](/hermes/mcp/servers/external/busymail-mcp)
- [smtp-mcp - Guardrailed Outbound Email over SMTP for Agents](/hermes/mcp/servers/external/smtp-mcp)
