---
title: "Leadbay MCP - AI Lead Discovery for Agents"
description: "OAuth remote MCP over a Leadbay account: source scored leads, qualify them with AI, draft outreach and log activity from any agent."
category: "Marketing"
stars: n/a (hosted platform, leadbay.ai)
added: 2026-10-02
source: "mcpservers.org server page (leadbay/mcp)"
relevance: ★★★
tags: [sales, leads, prospecting, outbound, crm, b2b, remote-mcp]
---

# Leadbay MCP

**Remote MCP server (Streamable HTTP, OAuth)** - Leadbay MCP connects an assistant to a Leadbay account so an agent pulls leads, qualifies them with AI research, drafts outreach and logs what was sent, all against the operator's real Leadbay data and permissions.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in)
Endpoint: https://mcp.leadbay.app/mcp
Tools: lead sourcing, bulk qualification, title enrichment and outreach reporting
Pricing: Leadbay account required (credits bill top-ups)
Category: Marketing
Built by: Leadbay (github.com/leadbay/mcp, open source server)
```

## Why This Matters for Operators

Outbound dies when the list is bad. Leadbay scores leads against a target profile using the operator's own website and market data, so the agent works a ranked stream instead of a raw export. The MCP server puts that stream inside the assistant, which means the qualifying research and the outreach drafting happen where the operator already works.

**The mental model matters.** Leadbay delivers a daily batch sized by how many leads the operator actually acted on recently, so pulling more does not produce more; working leads does. Every lead carries a firmographic `score`, and roughly the top ten per batch are also AI-qualified into an `ai_agent_lead_score`. An agent can request deeper qualification or contact enrichment on any lead worth the credits.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Lead pull | Retrieve the current batch of scored leads for the account |
| `leadbay_bulk_qualify_leads` | Request deeper AI qualification on a set of leads |
| `leadbay_enrich_titles` | Enrich contact titles for a lead worth pursuing |
| `leadbay_report_outreach` | Log what outreach was actually sent |
| Outreach drafting | Draft outreach against the lead and the operator's context |

The server is open source at `github.com/leadbay/mcp`.

## Installation

```bash
claude mcp add leadbay --transport http https://mcp.leadbay.app/mcp
```

On Claude web, Claude Desktop or ChatGPT the fastest path is a custom connector: name it `Leadbay` and use `https://mcp.leadbay.app/mcp`, which serves every region (`/fr/mcp` is a compatibility alias). On ChatGPT use `https://mcp.leadbay.app/chatgpt/mcp` instead, since that surface cannot generate top-up links or open the billing page.

## Configuration

```json
{
  "mcpServers": {
    "leadbay": {
      "type": "http",
      "url": "https://mcp.leadbay.app/mcp"
    }
  }
}
```

Sign in with the browser on first connect. A Leadbay account is required before setup.

## Business Relevance

- **SDRs and founders doing their own outbound** work a ranked daily batch rather than building lists by hand.
- **Sales managers** get AI-qualified top-of-batch leads with the research already attached.
- **Agencies** run the same lead engine across several clients with per-account permissions.
- **RevOps** gets outreach logged back into Leadbay so activity stays in one place.
- **Any operator** trading a lead database for a scored, action-paced stream.

## Integration with CorpusIQ

Leadbay supplies the target list and the qualification; CorpusIQ supplies the account context that makes outreach specific. A HubSpot company record feeds the personalization, a GA4 or Stripe read tells the agent that a prospect's site is converting, and the drafted outreach references it. Leadbay answers "who should we approach and how qualified are they", CorpusIQ answers "what do we already know about them", and together they turn a generic sequence into a researched one.

## Limitations

- Brand new, no track record yet.
- Requires a paid Leadbay account; credits determine how much qualification runs.
- Batch size is deliberately paced by recent engagement, so volume cannot be forced.
- The ChatGPT surface cannot manage billing or top-ups by directory policy.
- Lead quality is only as good as the target profile configured in the account.

## FAQ

### Does Leadbay MCP need an API key?

No. It uses browser OAuth at `https://mcp.leadbay.app/mcp`, so there is no token to copy.

### Why does pulling more leads not produce more?

Leadbay paces each daily batch by how many leads the operator has acted on recently, so the lever is working leads, not requesting more.

### Can an agent deepen qualification on a specific lead?

Yes. `leadbay_bulk_qualify_leads` runs AI research and qualification questions on chosen leads, and `leadbay_enrich_titles` fills in contact titles.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
