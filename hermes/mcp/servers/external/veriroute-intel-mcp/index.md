---
title: VeriRoute Intel MCP - Live Phone Number Intelligence
description: "Hosted MCP server for live US and Canada phone number intelligence: carrier of record, line type, LRN routing, porting date, CNAM caller-ID name and spam, scam and robocall reputation. Five tools including bulk lookups up to 10,000 numbers, prepaid balance billing with no charge for failed lookups, and free sandbox test keys."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-04
source: mcp.so feed
relevance: ★★★
tags: [phone-validation, carrier-lookup, cnam, spam-detection, lead-hygiene, remote-mcp, telecom]
---

# VeriRoute Intel MCP

**Remote MCP server (Streamable HTTP)** - live phone number intelligence for US and Canada numbers: current carrier of record, line type, LRN routing data, porting activation date, caller-ID name (CNAM) and spam/scam/robocall reputation. Five tools, prepaid balance billing, free sandbox test keys.

```
Server type: Remote (Streamable HTTP, JSON-RPC 2.0)
Auth: Bearer API key (free sandbox keys return deterministic sample data at zero charge)
Endpoint: https://verirouteintel.com/api/mcp
Tools: 5 (vri_number_lookup, vri_spam_check, vri_bulk_lookup, vri_submit_job, vri_bulk_status)
Registry: com.verirouteintel/lookup (official MCP registry)
```

## Why This Matters for Operators

Dead numbers, ported numbers, VoIP lines and spam-flagged caller IDs quietly wreck outbound operations: sales dialers burn minutes on disconnected lines, and outbound calls from flagged numbers land in Spam Likely. VeriRoute reads the live numbering infrastructure - never a stale cache - so every lookup reflects current carrier and porting state. **An agent cleaning a calling list can verify carrier, line type and spam reputation per number before a single dial.**

The billing model is operator-friendly: prepaid balance, every result reports what it cost, failed lookups are never charged, and calls that would exceed the balance are refused up front. Bulk work runs as async jobs (up to 10,000 numbers) with reserved balance and a status tool.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `vri_number_lookup` | Live intelligence for one number: carrier, line type, LRN routing, porting date; optional CNAM, spam reputation, messaging provider |
| `vri_spam_check` | Spam / scam / robocall reputation for one number |
| `vri_bulk_lookup` | Up to 100 numbers in one call |
| `vri_submit_job` | Async bulk job up to 10,000 numbers; balance reserved up front |
| `vri_bulk_status` | Progress of one of your bulk jobs |

## Installation

```bash
claude mcp add --transport http vri https://verirouteintel.com/api/mcp
```

Get a key at verirouteintel.com/dashboard/api-keys. Free sandbox test keys return deterministic sample data with zero charges, so an agent can be wired up and tested before any balance is funded. Attach the key as a bearer authorization header.

## Configuration

```json
{
  "mcpServers": {
    "vri": {
      "url": "https://verirouteintel.com/api/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

Per-lookup rates match the REST API and draw from the same prepaid balance.

## Business Relevance

- **Sales operations** clean calling lists before dialing (dead, ported, VoIP detection).
- **Fraud and risk teams** verify carrier and line type during signup and checkout screening.
- **Marketing teams** check their own outbound caller IDs for Spam Likely flags before campaigns.
- **Data teams** run async bulk jobs for list hygiene at scale.

## Integration with CorpusIQ

CorpusIQ's CRM connectors hold the prospect lists; VeriRoute grades the numbers on them. A CorpusIQ agent preparing an outbound campaign can pull the list from the CRM, run VeriRoute validation, and write back only the verified, non-flagged numbers - improving deliverability without the operator leaving the workflow.

## Limitations

- US and Canada numbers only.
- Brand new (repo created Sep 1, 2026, 0 stars, no license declared) - service stability is unproven.
- Prepaid balance model; live lookups cost per call (failed lookups free).
- Sandbox keys return sample data, not real lookups - verify live-key behavior before production use.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [NeuralVerge MCP - B2B People and Company Data](/hermes/mcp/servers/external/neuralverge-mcp)
- [CampaignStack MCP - Safe LinkedIn and Email Outreach](/hermes/mcp/servers/external/campaignstack-mcp)
