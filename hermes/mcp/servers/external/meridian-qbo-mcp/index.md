---
title: "QuickBooks Connector by Meridian MCP - Hosted QBO for Agents"
description: "Free hosted MCP server from Pilot.com's Meridian that connects AI agents to QuickBooks Online: read and write transactions including journal entries, connect multiple QuickBooks clients without configuration changes, and run bookkeeping workflows end to end. Endpoint live and OAuth-gated; sign in with Intuit."
category: Finance
stars: "n/a (hosted service)"
added: 2026-09-01
source: "mcpservers.org homepage (Sep 1, 2026 night sweep)"
relevance: ★★★
tags: [mcp-server, quickbooks, qbo, accounting, bookkeeping, finance, oauth, remote-mcp]
---

# QuickBooks Connector by Meridian MCP

**A hosted QuickBooks Online MCP server, free.** Meridian (a Pilot.com product) runs a hosted QBO connector that lets an agent read and update QuickBooks data: create invoices from spreadsheets, reconcile credit-card statements against QuickBooks, categorize expenses, and answer investor information requests from the books. Endpoint verified live Sep 1, 2026 (401 on anonymous initialize, as expected for an OAuth-gated server).

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://qbo-connector.meridian.pilot.com/mcp (401-verified live)
Auth: Sign in with Intuit (QuickBooks OAuth); no installation or configuration
Tools: capability-level across QBO read/write surfaces (served after sign-in)
Pricing: 100% free
Built by: Meridian, a Pilot.com product (pilot.com)
```

## Why This Matters for Operators

QuickBooks is where most operators' financial truth lives, and it is the system agents can least reach. Meridian's connector removes the whole integration burden: no API app registration, no hosted client, no configuration.

First, **multi-client by default.** The connector can connect to multiple different QuickBooks clients without configuration changes - an agency or bookkeeper attaches each client once and switches by context.

Second, **write access, including journal entries.** Anything you can do via the QuickBooks API, the agent can do: create invoices, categorize expenses, and post arbitrary transactions including journal entries, not just read reports.

Third, **free and fully hosted.** There is no installation and no configuration; the setup flow is sign in with Intuit, connect QuickBooks companies, connect the agent, and verify.

## Tools and Capabilities

Capability-level table sourced from the vendor's landing page; the live tool list is served from the endpoint after Intuit sign-in (anonymous enumeration is refused with 401).

| Surface | What it covers |
|---------|----------------|
| Read | Read QuickBooks data across accounts, customers, invoices, expenses and reports |
| Write | Create and update transactions, including arbitrary journal entries |
| Multi-client | Connect multiple QuickBooks companies; switch clients without configuration changes |
| Workflows | Spreadsheet-to-invoices creation, statement reconciliation, expense categorization, investor request responses |

## Installation

```bash
claude mcp add --transport http meridian-qbo https://qbo-connector.meridian.pilot.com/mcp
```

Then sign in with Intuit when the first connection opens. The vendor's setup guide lives at qbo-connector.meridian.pilot.com/setup and claims under three minutes to first use.

## Configuration

```json
{
  "mcpServers": {
    "meridian-qbo": {
      "type": "http",
      "url": "https://qbo-connector.meridian.pilot.com/mcp"
    }
  }
}
```

Works with Claude, Cowork, Codex and ChatGPT per the vendor. The Intuit grant scopes the agent to the QuickBooks companies you connect and is revocable through Intuit's connected-apps controls.

## Business Relevance

- **Bookkeepers and accounting firms** connect each client once and let the agent draft entries and reconciliations for review.
- **Founders** get investor data requests answered straight from the books without exporting to a spreadsheet.
- **Finance teams** reconcile credit-card statements and categorize expenses with the agent doing the mechanical work.
- **Agencies** keep one connector for many client companies, switching by context instead of reconfiguring.

## Integration with CorpusIQ

Meridian's connector composes with CorpusIQ as a specialist QBO surface next to the general one. Where CorpusIQ's built-in QuickBooks connector supplies read-side business data across the stack, Meridian adds a free write-side channel: an agent that assembles context from CorpusIQ's Stripe, HubSpot or Google Ads connectors can draft the resulting invoices or journal entries into QuickBooks through Meridian and keep the human review step in QuickBooks itself. The operator keeps one governance point: CorpusIQ holds the cross-source business picture, Meridian executes the accounting writes, and the Intuit grant stays revocable in one place.

## Limitations

- New listing with no public track record; verify the free tier's terms as the product matures.
- Capability-level tool table above; exact tool names appear after Intuit sign-in.
- Write access to the books is powerful - keep the human review step for journal entries and payments.
- Hosted by Pilot.com, Inc.; QuickBooks and Intuit are Intuit's registered trademarks, used with permission per the vendor site.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [QuickBooks MCP - Connect Agents to QuickBooks Online](/hermes/mcp/servers/external/quickbooks-mcp)
- [Edgrapi MCP - SEC EDGAR Structured Data for Agents](/hermes/mcp/servers/external/edgrapi-mcp)
