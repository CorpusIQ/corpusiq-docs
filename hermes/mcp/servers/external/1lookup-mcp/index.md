---
title: "1Lookup MCP - Phone, Email and IP Verification"
description: "Hosted data verification MCP: validate phone numbers with line type, carrier, and DNC status, verify email deliverability with disposable and role-based flags, and look up IPs with proxy, VPN, and Tor detection. OAuth 2.1, no API keys, credit-based."
category: Compliance
stars: n/a (hosted)
added: 2026-08-25
source: "mcp.so GitHub issue #3747"
relevance: ★★
tags: [mcp-server, verification, phone-validation, email-verification, fraud-detection, dnc]
---

# 1Lookup MCP

**Contact verification without leaving the conversation.** 1Lookup is a data verification platform whose hosted MCP server lets an agent validate a phone number, verify an email address, or look up an IP mid-workflow. OAuth 2.1 with dynamic client registration (RFC 7591) and PKCE means there is no API key to paste into a config file; tool calls spend the same universal credits as the 1Lookup REST API, one credit per lookup, and `get_account` is free.

```
Server type: Remote Streamable HTTP (hosted)
Endpoint: https://app.1lookup.io/api/mcp
Auth: OAuth 2.1 with DCR + PKCE (SSE disabled)
Tools: 5 (validate_phone, verify_email, ip_lookup, bulk_verify, get_account)
Registry: io.1lookup/1lookup (active)
Plans: paid, every plan starts with a 7-day free trial
```

## Why This Matters for Operators

Lead hygiene and compliance are the same workflow: a bad list wastes outbound effort, and dialing numbers on a Do-Not-Call list is a fine. 1Lookup's tools answer the three questions that gate outbound work: is this phone real, mobile or landline, and DNC-listed? Is this email deliverable, or disposable? Is this visitor a proxy or VPN? `bulk_verify` handles up to 50 values per call, which is the shape real list-cleaning takes.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `validate_phone` | Line type, carrier, and DNC status for a phone number |
| `verify_email` | Email deliverability plus disposable and role-based flags |
| `ip_lookup` | IP geolocation with proxy, VPN, and Tor detection |
| `bulk_verify` | Up to 50 values per call |
| `get_account` | Remaining plan credits (free, spends no credits) |

## Installation

```json
{
  "mcpServers": {
    "1lookup": {
      "type": "http",
      "url": "https://app.1lookup.io/api/mcp"
    }
  }
}
```

Connect with one URL; the OAuth 2.1 flow handles registration and consent.

## Configuration

OAuth 2.1 with PKCE, no API key or secret in the config file. Requires a paid plan; tool calls spend credits at one credit per lookup. The endpoint returns 401 on anonymous initialize, which is the expected live-and-gated posture.

## Business Relevance

- **Outbound compliance:** DNC checks before dialing campaigns.
- **List hygiene:** strip disposables and role addresses before sends.
- **Fraud triage:** proxy and VPN detection on inbound leads and logins.
- **Agent-native ops:** verification inside the CRM workflow instead of a separate tab.

## Integration with CorpusIQ

1Lookup's verification results pair with CorpusIQ connectors for the CRM side: enrich and flag contacts in HubSpot or Close as they are verified, log DNC status in Airtable for campaign compliance, and trigger follow-up automations from the verification outcome.

## Limitations

- Paid plan required after the 7-day trial; credits are consumed per lookup.
- OAuth-only auth; headless environments need to complete the browser flow once.
- Verification data reflects the vendor's coverage and freshness, not a legal certification of compliance.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Korea Business Verify - Real-Time Korean Business Verification](/hermes/mcp/servers/external/korea-business-verify)
- [Atlas Verified MCP](/hermes/mcp/servers/external/atlas-verified-mcp)
