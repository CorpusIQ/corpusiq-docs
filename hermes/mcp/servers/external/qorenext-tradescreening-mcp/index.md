---
title: QoreNext Trade Screening MCP - Sanctions
description: "Remote MCP from QoreNext for trade-compliance due diligence: 4 tools screen entities against US sanctions lists (OFAC, MEU, Entity List) and run full trade screenings with red-flag analysis, risk assessment and negative-news findings, with async report polling in chat. X-API-Key auth, MIT."
category: Compliance
stars: n/a (new repo)
added: 2026-08-27
source: "chatmcp/mcpso issue #3798 + github.com/QoreNext/qorenext-tradescreening-mcp"
relevance: ★★★
tags: [sanctions, ofac, restricted-parties, trade-compliance, due-diligence, screening, remote-mcp]
---

# QoreNext Trade Screening MCP

**Hosted remote MCP server (Streamable HTTP, X-API-Key header) for sanctions and trade screening.** QoreNext Trade Screening MCP moves export-compliance research into the conversation: screen entities against US sanctions lists (OFAC, MEU, Entity List and related), or run a full trade screening that combines denied/restricted-party checks, red-flag keyword analysis, risk assessment and negative-news findings into a pollable due-diligence report. Each submission returns a tracking id; `get_trade_screening_status` delivers the completed report with risk level and a recommendation.

```
Server type: Remote (Streamable HTTP)
Auth: X-API-Key header (QORENEXT_API_KEY from qorenext-app.azurewebsites.net/signup)
Endpoint: https://mcp.qorenext.com/tradescreening
Tools: 4 (health_check is public; 3 require the key)
Pricing: Vendor account required; see qorenext.com
Repo: github.com/QoreNext/qorenext-tradescreening-mcp (MIT)
Category: Compliance
```

## Why This Matters for Operators

Export and sanctions compliance is normally a per-entity slog through list checks, red-flag analysis and negative-news review. QoreNext compresses it into two prompts: an instant sanctions screen (with match score per entity) and a full trade screening whose report arrives by polling. **Both tools accept native-language entity names** - an entity can be submitted in English or its native script (e.g. Arabic, Chinese) - which matters because restricted-party lists are populated in both. For any operator shipping internationally, this is due-diligence capacity the agent can run alongside the deal.

## Tools & Capabilities

| Tool | Auth | Purpose |
|---|---|---|
| `health_check` | Public | Server liveness and version |
| `submit_sanctions_screening` | API key | Screen entities against US sanctions lists (OFAC, MEU, Entity List); returns matchFound, bestMatchScore and matches per entity |
| `submit_trade_screening` | API key | Full due diligence: denied/restricted-party checks, red-flag keywords, risk assessment, negative news; returns a tracking id |
| `get_trade_screening_status` | API key | Poll status (Pending / Processing / Completed / Failed) and retrieve the full report once Completed |

Reports include risk level and a recommendation (e.g. "Proceed with standard due diligence"), and the vendor maps the backend API's required extra fields to blanks so callers only supply name, address and website.

## Installation

```bash
claude mcp add --transport http qorenext-mcp \
  "https://mcp.qorenext.com/tradescreening" \
  --header "X-API-Key: YOUR_API_KEY"
```

## Configuration

```json
{
  "mcpServers": {
    "qorenext-mcp": {
      "url": "https://mcp.qorenext.com/tradescreening",
      "headers": {
        "X-API-Key": "YOUR_API_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Export and trade compliance teams** run sanctions screens from the chat that manages the shipment
- **Procurement and vendor teams** due-diligence new suppliers before onboarding
- **Finance ops** keep restricted-party evidence alongside payment decisions
- **International sellers** screen buyers and counterparties with native-language name support

## Integration with CorpusIQ

Trade screening is the compliance gate that CorpusIQ's operational connectors document around. A vendor flagged in a QoreNext screening can be traced through CorpusIQ's QuickBooks payables and Shopify order history to quantify the exposure, then monitored going forward. For operators selling internationally, the pair answers both compliance questions - "is this counterparty restricted" (QoreNext) - and business questions - "how much revenue and payables do we have with them" (CorpusIQ) - in one thread.

## Limitations

- Brand new - no adoption track record; new-repo MIT listing
- Known vendor backend issue (confirmed 2026-08-19): new trade-screening submissions intermittently fail with a 422 null-reference error; duplicate submissions of known companies are unaffected
- Submit/poll model: full reports are asynchronous
- US sanctions focus for the instant screen; broader lists flow through the trade-screening report
- Vendor account required for the API key

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Korea Business Verify MCP - Live KYB Checks for Korean Companies](/hermes/mcp/servers/external/korea-business-verify)
