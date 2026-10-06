---
title: "Agency Handy MCP - Agency Operations from Chat"
description: "Run an agency workspace from the conversation: client cash, proposals, delivery risk, assignments and custom fields through hosted or local MCP."
category: Business Operations
stars: n/a (new listing)
added: 2026-10-06
source: "chatmcp/mcpso issue #4807 (Oct 6, 2026 midday sweep)"
relevance: ★★★
tags: [agency, project-management, crm, invoicing, cash-flow, remote-mcp]
---

# Agency Handy MCP

**Remote MCP server (Streamable HTTP, workspace API key) or local stdio** - AgencyHandy is an agency management workspace, and its MCP connection lets an assistant brief you, assign work, investigate cash and delivery risk, and fill custom fields in plain language. Both connection paths - a local `npx agencyhandy-mcp@1` package or the hosted server at `mcp.agencyhandy.com` - use the same workspace API key and expose the same tools.

```
Server type: Remote (Streamable HTTP) or local (stdio)
Auth: Workspace API key (Bearer; from Workspace Config -> API Key)
Endpoint: https://mcp.agencyhandy.com/ (hosted) or npx -y agencyhandy-mcp@1 (local)
Tools: Briefs, assignments, cash and delivery risk, custom fields, CRM actions
Pricing: Included with AgencyHandy workspace
Built by: AgencyHandy (agencyhandy.com)
Registry: com.agencyhandy/mcp
```

## Why This Matters for Operators

Agencies run on the same four questions every morning: what is on fire, what is about to be paid, what is slipping, and who should fix it. AgencyHandy's MCP surface is built specifically for those - Monday pulses across cash overdue, stale proposals and slipping work; smart assignment that reads team capacity instead of picking the busiest person; churn watchlists that combine overdue invoices and quiet orders into a short, scored list.

The design stays honest about authority: the agent acts only with the workspace API key you generate, and it asks you to confirm when a name matches more than one person. Read-style investigation and write-style actions run through the same tools, so the operator can start read-only and grant actions as comfort grows.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Cash and risk | Top clients by open AR with 30/60/90-day aging, churn-risk watchlists, next-best invoice to chase |
| Proposals | Find stale or expiring proposals, summarize comments, say whether you or the client is blocking |
| Delivery | Order health across tasks, tickets and files; find what is blocking delivery vs billing |
| Assignment | Recommend owners by capacity and assign tickets and tasks, by name or skill |
| CRM | Create leads and clients, set custom fields such as industry and estimated budget |
| Records | Explain an invoice end-to-end, with amounts, aging, linked order and related invoices |

## Installation

Hosted (cloud agents - nothing to install):

```bash
claude mcp add --transport http agencyhandy https://mcp.agencyhandy.com/ --header "Authorization: Bearer YOUR_WORKSPACE_API_KEY"
```

Local (Claude Desktop or Cursor, Node.js 20+):

```bash
npx -y agencyhandy-mcp@1
```

## Configuration

```json
{
  "mcpServers": {
    "agencyhandy": {
      "url": "https://mcp.agencyhandy.com/",
      "headers": {
        "Authorization": "Bearer YOUR_WORKSPACE_API_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Agency owners** get a Monday pulse of cash, proposals and slipping work in one question.
- **Delivery leads** see what is blocking an order on both sides, then reassign by capacity.
- **Finance-minded operators** turn invoice questions into a short action - nudge, escalate, or wait.
- **Small teams** get confirm-gated actions instead of an agent with unchecked write access.

## Integration with CorpusIQ

CorpusIQ reads the operator's business systems read-only - accounting, payments, ads, analytics. AgencyHandy adds the operational layer where that money moves: which client owes it, which order is slipping, who should fix it. One conversation can pull the financial picture from the connected stack and the action list from the agency workspace, without either side needing write access to the other.

## Limitations

- Requires an AgencyHandy workspace; the API key is scoped to one workspace.
- Cloud path is read from the key - each user connects with their own key.
- Confirm prompts are a feature, not a bug; write actions ask when a name is ambiguous.
- New listing: no track record in this catalog yet.

## FAQ

### Which connection should I use?

Local (`npx agencyhandy-mcp@1`) when Claude Desktop or Cursor runs on your computer; hosted (`mcp.agencyhandy.com`) when the agent runs in the cloud, such as Cloudflare Workers, Vercel or n8n. Both expose the same tools and use the same workspace key.

### What can it write?

Leads, clients, custom fields and assignments - through the same API key your workspace issues, with confirmation when a person match is ambiguous.

### Does it see my invoices?

Yes, read-style: amounts, aging, linked orders and related open invoices for a client, so it can tell you which invoice to chase and why.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Sitegoalie MCP - WordPress Operations for Agencies](/hermes/mcp/servers/external/sitegoalie-mcp/)
- [GumroadDNA MCP - Gumroad Store Operations](/hermes/mcp/servers/external/gumroad-dna-mcp/)
