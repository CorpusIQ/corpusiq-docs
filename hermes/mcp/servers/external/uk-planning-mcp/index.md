---
title: "UK Planning MCP - Planning Applications by LPA"
description: "UK planning applications and decisions for an LPA or postcode, with status mixes and coverage flags, as free peeks or one-time packs for property work."
category: Real Estate
stars: n/a (new listing)
added: 2026-10-06
source: "chatmcp/mcpso issue #4833 (Oct 6, 2026 evening sweep)"
relevance: ★★
tags: [uk, planning, property, proptech, open-data, remote-mcp, keyless, development]
---

# UK Planning MCP

**Remote MCP server (Streamable HTTP, keyless)** - UK planning applications and decisions for planners, surveyors and proptech agents: recent applications for an LPA or postcode with status mix and honest coverage flags, from a free peek to one-time £0.49 packs.

```
Server type: Remote (Streamable HTTP, Cloudflare Worker)
Auth: None (keyless discovery; packs pay per use)
Endpoint: https://uk-planning-mcp.donniertf.workers.dev/mcp
Tools: 4 (discovery, two pack tools, redeem)
Pricing: Free sample; GBP 0.49 one-time per pack
Built by: donniertf (uk-mcp-fleet)
Source: planning.data.gov.uk (Open Government Licence v3.0)
```

## Why This Matters for Operators

Planning activity is the leading indicator of local development: what is being built, extended, converted or refused in an area before it shows up in any other dataset. Suppliers, agents and investors read it to time outreach; developers read it to track a pipeline; analysts read it to understand how a market is changing.

The honest part is coverage. Planning data is patchy across local authorities, and this server says so with coverage flags and status mixes rather than pretending every LPA reports the same way. For a first-pass view that an agent can pull per postcode, that is the right shape: applications, decisions and a clear note on what the data can and cannot support.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `planning_discover` | Free peek: up to 5 UK planning applications for an LPA name or postcode (e.g. Doncaster); cached 24h |
| `planning_pack` | Paid pack of recent applications with decision details; Stripe Checkout link, one-time token redeem |
| `lpa_summary_pack` | Paid summary: applications plus `status_mix` and `risk_flags` for the area |
| `redeem_pack` | Instructions to redeem a paid Stripe Checkout session |

Free sample: `GET /v1/discover/planning?lpaOrPostcode=Doncaster` (up to 5 applications).

## Installation

```bash
claude mcp add uk-planning --transport http https://uk-planning-mcp.donniertf.workers.dev/mcp
```

Discovery is keyless. Paid packs return a Stripe Checkout URL inside the tool result; pay GBP 0.49 and redeem with the one-time token.

## Configuration

```json
{
  "mcpServers": {
    "uk-planning": {
      "url": "https://uk-planning-mcp.donniertf.workers.dev/mcp"
    }
  }
}
```

## Business Relevance

- **Planners and surveyors** pull recent applications for a council area as a working list.
- **Property investors** read status mixes (approved, pending, refused) as a market-activity signal.
- **Proptech products** feed structured application rows into agent workflows without portal scraping.
- **Local suppliers** spot active development sites for outreach timing.

## Integration with CorpusIQ

CorpusIQ's read-only connectors show the business's own operating numbers; the Planning server shows what is changing around it - the development pipeline of an area. Together: "where are we" from your systems, "what is coming" from the public record.

## Limitations

- Coverage varies by local authority - the packs surface that with coverage flags; check the local authority for decisions that matter.
- Free samples are capped (5 applications, 24h cache); full and summary results are behind one-time GBP 0.49 packs.
- Sourced from planning.data.gov.uk under the Open Government Licence; not an official decision notice.
- The fleet's pages offer a refund within 7 days if a pack comes back empty or errors.

## FAQ

### What can I look up?

Recent planning applications and decision details for a UK local planning authority (by name or postcode), including a status mix for the area on the summary pack.

### Where does the data come from?

planning.data.gov.uk, under the Open Government Licence v3.0. Coverage varies between authorities - the server flags this instead of hiding it.

### How much does a pack cost?

GBP 0.49 per pack, paid once via Stripe Checkout from inside the tool call. Discovery is free.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Dutch Property Context MCP - Netherlands Property Reports](/hermes/mcp/servers/external/dutch-property-context/)
- [UK Land Registry MCP - Sold Price Packs for Agents](/hermes/mcp/servers/external/uk-land-registry-mcp/)
