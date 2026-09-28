---
title: Handl MCP - Billing Operations for Small Agencies
description: "Handl exposes a whole billing operation as MCP tools: projects, quotes, invoices, payment links, reminders, reports and approvals."
category: Finance
stars: n/a (new listing)
added: 2026-09-27
source: "mcp.so server page (mcp.handl.works)"
relevance: ★★★
tags: [invoicing, billing, quotes, payment-links, accounts-receivable, scope-management, cash-flow, remote-mcp]
---

# Handl MCP

**A billing operation an AI assistant can drive end to end, inside your autonomy rules.** Handl is an AI-native financial operations platform for freelancers and small agencies (1-10 people) that consolidates quoting, invoicing, payment collection and scope management in one workspace. Its hosted MCP endpoint at `https://mcp.handl.works/api/mcp` exposes projects, invoices, clients, reports and approvals as tools any assistant can call, with OAuth sign-in on first connect.

```
Server type: Remote (Hosted)
Auth: OAuth (browser sign-in on first connect)
Endpoint: https://mcp.handl.works/api/mcp
Tools: projects, quotes, invoices, clients, reports, approvals
Pricing: vendor pricing (handl.works)
Category: Finance / Billing
Built by: Handl (handl.works)
```

## Why This Matters for Operators

The most expensive billing problem for small service businesses is not creating invoices; it is collecting payment without damaging the client relationship. Handl was designed by an agency founder with 20-plus years in client services around exactly that: professional quotes and invoices with one-click payment links, automatic payment reminders before and after due dates, real-time scope change tracking to prevent billing disputes, and AI-powered follow-ups that keep a personal tone.

Handl also frames its agent tools around operator autonomy rules, so the assistant works the billing motion while the human keeps approval control over the steps that need it.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Quotes and invoices | Professional documents with one-click payment links |
| Payment reminders | Automatic reminders before and after due dates |
| Scope tracking | Real-time scope change tracking to prevent disputes |
| Follow-ups | AI-powered payment follow-ups with a professional tone |
| Dashboard | Outstanding invoices, payment status and cash flow visibility |
| Reports and approvals | Reporting and approval tools for the billing operation |

## Installation

```bash
claude mcp add handl --transport http https://mcp.handl.works/api/mcp
```

The first connection opens a browser window to sign in and authorize; the credentials are reused for future sessions.

## Configuration

```json
{
  "mcpServers": {
    "handl": {
      "type": "http",
      "url": "https://mcp.handl.works/api/mcp"
    }
  }
}
```

## Business Relevance

- **Freelancers** get quotes, invoices and reminders from one chat surface
- **Small agencies** track scope changes in real time to avoid write-offs
- **Founders** get cash-flow visibility without a bookkeeper
- **Client-service teams** collect payment without manual awkward follow-ups

## Integration with CorpusIQ

Handl complements the CorpusIQ QuickBooks connector: QuickBooks holds the accounting truth including AR aging, while Handl runs the client-facing billing motion, payment links and reminders. CorpusIQ's cash-recovery runbook can pair its QuickBooks overdue list with Handl's follow-up tools to execute collection sequences with a human tone.

## Limitations

- Built for freelancers and 1-10 person agencies; larger orgs may outgrow it
- Hosted endpoint; no self-hosted option published
- Live tool list is served from the endpoint after authentication
- New listing; the product surface is young

## FAQ

### Who is Handl built for?

Freelancers and small agencies of one to ten people that want quotes, invoices and payment collection in one workspace.

### How does authentication work?

OAuth with a browser sign-in on first connect, then reused credentials.

### What billing problem does it target?

Collecting payment without damaging client relationships, via payment links, reminders and scope tracking.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
