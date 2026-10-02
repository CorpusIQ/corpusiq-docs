---
title: QoreNext CRM MCP - Company Hierarchy and Address
description: "Remote MCP from QoreNext for CRM data intelligence: 5 tools submit companies for address verification, corporate hierarchy mapping (top-parent and subsidiary relationships) and duplicate-record detection from JSON, CSV or Excel, then poll async results in chat. X-API-Key auth, MIT."
category: Business Operations
stars: n/a (new repo)
added: 2026-08-27
source: "chatmcp/mcpso issue #3797 + github.com/QoreNext/qorenext-crm-mcp"
relevance: ★★★
tags: [crm, entity-intelligence, address-verification, hierarchy, deduplication, data-quality, remote-mcp]
---

# QoreNext CRM MCP

**Hosted remote MCP server (Streamable HTTP, X-API-Key header) for CRM entity intelligence.** QoreNext CRM MCP lets an AI assistant run the data-quality work a CRM team otherwise does by hand: verify company names and registered addresses, map corporate ownership hierarchies down to top-parent and subsidiary relationships, and detect duplicate account records from JSON, CSV or Excel files. The model is submit-then-poll: submissions return an entity/request id, and `get_request_status` fetches the completed results - so long-running checks never block the conversation.

```
Server type: Remote (Streamable HTTP)
Auth: X-API-Key header (QORENEXT_API_KEY from qorenext-app.azurewebsites.net/signup)
Endpoint: https://mcp.qorenext.com/crm
Tools: 5 (health_check is public; 4 require the key)
Pricing: Vendor account required; see qorenext.com
Repo: github.com/QoreNext/qorenext-crm-mcp (MIT)
Category: Business Operations
```

## Why This Matters for Operators

CRM decay is silent revenue decay: duplicate accounts split pipelines, stale addresses break mail, and ownership structure sits invisible in spreadsheets. QoreNext CRM MCP puts the fixes in the agent that already holds the CRM context - "verify these 40 accounts", "map who actually owns this customer", "find the duplicates in this export" - with structured inputs and pollable results. **The duplicate detector takes a plain file (JSON array, CSV with headers, or Excel with crmAccountId/crmAccountName/addressLine1/country columns) and returns the duplicate-pair count with per-record detail**, turning a manual audit into one prompt.

## Tools & Capabilities

| Tool | Auth | Purpose |
|---|---|---|
| `health_check` | Public | Server liveness and version |
| `submit_address_verification` | API key | Submit companies (companyName, country, address; optional crmid, website) for address verification and legitimacy validation |
| `submit_hierarchy_creation` | API key | Submit companies for corporate hierarchy analysis: top-parent and subsidiary relationships |
| `submit_duplicates` | API key | Submit CRM account records as JSON, CSV or Excel for duplicate detection |
| `get_request_status` | API key | Poll status (PENDING / PROCESSING / COMPLETE / FAILED) and retrieve results by request id |

Example results include verified address status with business status (ACTIVE), and hierarchy chains like "Acme Corp → Acme Holdings (USA) → GlobalCorp (UK)".

## Installation

```bash
claude mcp add --transport http qorenext-mcp \
  "https://mcp.qorenext.com/crm" \
  --header "X-API-Key: YOUR_API_KEY"
```

## Configuration

```json
{
  "mcpServers": {
    "qorenext-mcp": {
      "url": "https://mcp.qorenext.com/crm",
      "headers": {
        "X-API-Key": "YOUR_API_KEY",
        "Content-Type": "application/json",
        "Accept": "application/json"
      }
    }
  }
}
```

## Business Relevance

- **Sales ops** verify prospect addresses and legitimacy before outreach without leaving the CRM workflow
- **Account managers** map parent-subsidiary structures to see who really owns an account
- **Rev ops** dedupe CRM exports in one prompt instead of a manual spreadsheet pass
- **Compliance-adjacent teams** keep entity records accurate for KYC-adjacent bookkeeping

## Integration with CorpusIQ

QoreNext CRM MCP cleans the entity layer that feeds CorpusIQ's CRM and HubSpot connectors. Duplicate detection and hierarchy mapping run against CRM exports, then the corrected account structure flows back into HubSpot - which CorpusIQ already reads - so pipeline analytics stop double-counting and ownership roll-ups become accurate. Address verification complements CorpusIQ's business data with a hygiene pass: CorpusIQ answers "what is this account doing financially", QoreNext answers "is this account who it says it is".

## Limitations

- Brand new - no adoption track record yet; new-repo MIT listing
- Submit/poll model: results are asynchronous, not instant lookups
- Vendor account required for the API key (signup on the QoreNext app portal)
- Hierarchy and verification results depend on QoreNext's reference data coverage
- No self-host option documented

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Korea Business Verify MCP - Live KYB Checks for Korean Companies](/hermes/mcp/servers/external/korea-business-verify)
