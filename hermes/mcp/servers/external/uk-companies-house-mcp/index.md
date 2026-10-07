---
title: "UK Companies House MCP - KYB Packs for Agents"
description: "UK company data for agents: KYB packs with profile, officers, PSC and filings for any company number, plus newly incorporated company discovery by area."
category: Business Operations
stars: n/a (new listing)
added: 2026-10-06
source: "chatmcp/mcpso issue #4830 (Oct 6, 2026 evening sweep)"
relevance: ★★★
tags: [uk, companies-house, company-data, kyb, lead-generation, open-data, remote-mcp, keyless]
---

# UK Companies House MCP

**Remote MCP server (Streamable HTTP, keyless)** - UK Companies House data for research and lead-gen agents: a free peek at newly incorporated companies in an area, and one-time £0.49 packs with the full company record - profile, officers, people with significant control, filings and indicators.

```
Server type: Remote (Streamable HTTP, Cloudflare Worker)
Auth: None (keyless discovery; packs pay per use)
Endpoint: https://uk-ch-mcp.donniertf.workers.dev/mcp
Tools: 4 (discovery, two pack tools, redeem)
Pricing: Free sample; GBP 0.49 one-time per pack
Built by: donniertf (uk-mcp-fleet)
Source: UK Companies House (Open Government Licence v3.0)
```

## Why This Matters for Operators

Two operator motions live in this one server. The first is fresh leads: newly incorporated companies are the youngest businesses in the market, and a peek at "who just registered in London" is a prospecting signal for accountants, insurers, web agencies, IT providers - anyone whose customer is a business being born. The second is verification: a KYB pack pulls one company number's profile, officers, PSC and filings into structured JSON for counterparty checks in the conversation.

The fleet is honest about limits: the indicators are field checks on public records, not a due-diligence or Know Your Business opinion - and it is not the official register. For everything between "who is this company" and "should we sign", that is the right framing.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `new_cos_discover` | Free peek: up to 5 newly incorporated UK companies for an area (e.g. London); cached 24h |
| `new_cos_pack` | Paid pack of newly incorporated companies matching an area; returns a Stripe Checkout link, redeemed with a one-time token |
| `kyb_pack` | Paid pack for one company number: profile, officers, PSC, recent filings and indicators |
| `redeem_pack` | Instructions to redeem a paid Stripe Checkout session |

Free sample: `GET /v1/discover/new-cos?area=London` (up to 5 companies, 24h cache).

## Installation

```bash
claude mcp add uk-companies-house --transport http https://uk-ch-mcp.donniertf.workers.dev/mcp
```

No key for discovery. Paid packs return a Stripe Checkout URL inside the tool result; pay GBP 0.49, then redeemit with the one-time token from the redirect.

## Configuration

```json
{
  "mcpServers": {
    "uk-companies-house": {
      "url": "https://uk-ch-mcp.donniertf.workers.dev/mcp"
    }
  }
}
```

## Business Relevance

- **Accountants, insurers and B2B services** watch newly incorporated companies by area as a fresh lead stream.
- **Sales and ops teams** pull a structured company record for prospect qualification without leaving the chat.
- **Compliance and vendor checks** get officers, PSC and filings as JSON, with the "not a KYB opinion" caveat attached.
- **Researchers** get a cheap, agent-shaped view of the UK register instead of scraping HTML.

## Integration with CorpusIQ

CorpusIQ's read-only connectors cover the numbers inside the business - CRM, email, accounting. The Companies House server covers the outside view of a counterparty or prospect: who they are, who runs them, what they have filed. One question can now start from your pipeline and end at the official filings, each from its own source.

## Limitations

- Indicators are field checks on public Companies House records, not a due-diligence or KYB opinion; it is not the official register.
- Free samples are capped (5 rows, 24h cache); the full structured result is behind a one-time GBP 0.49 pack.
- Packs are one-time purchases, not a subscription; the fleet's pages offer a refund within 7 days if a pack comes back empty or errors.
- UK companies only.

## FAQ

### What is in a KYB pack?

Profile, officers, people with significant control, recent filings and field indicators for one UK company number - as structured JSON for your agent.

### How much does a pack cost?

GBP 0.49, paid once via Stripe Checkout from inside the tool call. There is no subscription; discovery is free.

### Where does the data come from?

UK Companies House public records, under the Open Government Licence v3.0. The server is clear that it is not the official register - check important facts there.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [The Company Atlas MCP - Trade Data and Company Registries](/hermes/mcp/servers/external/company-atlas-mcp/)
- [UK Tenders MCP - Public Sector Notices for Agents](/hermes/mcp/servers/external/uk-tenders-mcp/)
