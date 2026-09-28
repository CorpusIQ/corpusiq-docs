---
title: Warmerly MCP - Cold Email and B2B Leads for AI Agents
description: "Official Warmerly MCP server: find B2B leads, run cold email campaigns, check mailbox health and DNS, triage replies and verify emails."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + docs.warmerly.com/ai"
relevance: ★★★
tags: [cold-email, b2b-leads, email-verification, deliverability, spf, dkim, dmarc, remote-mcp]
---

# Warmerly MCP

**One OAuth connection that turns your AI assistant into the operator of your Warmerly cold email workspace.** The official Warmerly MCP server is a remote streamable-HTTP endpoint at `https://app.warmerly.com/api/mcp`, hosted by Warmerly and listed in the official MCP registry as `com.warmerly/warmerly`. Sign in with a normal Warmerly account and pick one workspace; the connection can only see and act inside that workspace. Every plan can connect, including Free, and no API key is required.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (browser sign-in, no API key)
Endpoint: https://app.warmerly.com/api/mcp
Tools: workspace-scoped (leads, campaigns, mailboxes, inbox, verification)
Pricing: all Warmerly plans, including Free
Category: Sales & Outreach / Cold Email
Built by: Warmerly (warmerly.com; repo github.com/WarmerlyApp/mcp)
```

## Why This Matters for Operators

Cold outreach lives or dies on deliverability, and deliverability dies quietly. Operators typically discover a warmed-up domain has been burning reputation only after replies stop coming. Warmerly MCP lets an agent ask the questions directly: which mailboxes are unhealthy and why, what SPF/DKIM/DMARC/MX looks like for a domain, and which campaigns are bouncing above a threshold, then act on the answers by pausing offenders.

The second win is triage. Instead of reading a replies inbox one thread at a time, an operator can ask the agent to list every reply that needs an answer, draft a response to each, and send on approval. Lead building gets the same treatment: describe an ICP like "UK marketing agencies with 10-50 staff" and have the agent assemble and launch a two-step campaign.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Lead finding | Build B2B lead lists from firmographic and ICP criteria |
| Campaigns | Create, edit and launch multi-step cold email sequences |
| Mailbox health | Inspect connected mailboxes and report why any are unhealthy |
| DNS checks | Check SPF, DKIM, DMARC and MX for any domain |
| Inbox triage | List replies needing answers and draft responses |
| Email verification | Verify addresses before they enter a sequence |
| Campaign control | Pause or stop campaigns breaching bounce thresholds |

## Installation

```bash
claude mcp add --transport http warmerly https://app.warmerly.com/api/mcp
```

Then run `/mcp` and sign in. Claude desktop and claude.ai users add the same URL under Settings > Connectors > Add custom connector. A Claude Code plugin with four workflow skills ships via the plugin marketplace (`WarmerlyApp/claude-plugin`).

## Configuration

```json
{
  "mcpServers": {
    "warmerly": {
      "type": "http",
      "url": "https://app.warmerly.com/api/mcp"
    }
  }
}
```

First connect opens a browser window for Warmerly sign-in and workspace selection. No client ID, API key or redirect setup is needed.

## Business Relevance

- **Founders and SDRs** get lead lists, sequences and reply triage from plain-language asks instead of dashboard clicks
- **Growth operators** get a health check on every sending domain before a campaign ships
- **Agencies** can pin each connection to one client workspace and prevent cross-account bleed
- **Small teams on Free** get the same agent surface as paid workspaces

## Integration with CorpusIQ

Warmerly pairs with CorpusIQ's email connectors: Gmail and Klaviyo can feed reply context into CorpusIQ recaps while Warmerly runs the outbound motion, and verified lead lists from Warmerly can be matched against HubSpot contacts in the CorpusIQ CRM connector to dedupe before outreach. The natural division is Warmerly for outbound campaigns and deliverability, CorpusIQ for cross-source business recaps and CRM truth.

## Limitations

- Workspace-scoped: one connection acts in one chosen workspace
- No self-hosting; the server is operated by Warmerly
- Cold email performance still depends on list quality and warmup discipline, not the connector
- New listing with no long public track record under MCP yet

## FAQ

### Does Warmerly MCP need an API key?

No. Sign in with a normal Warmerly account over OAuth; every plan can connect, including Free.

### What can the agent do with it?

Find B2B leads, build and launch campaigns, check mailbox health and DNS records, triage and draft replies, and verify emails.

### Can one connection touch multiple workspaces?

No. Each connection is pinned to one chosen workspace, which keeps client accounts separated.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
