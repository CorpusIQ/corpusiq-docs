---
title: "mcp-sanctions - Watchlist Screening for KYC and AML"
description: Sanctions and watchlist screening for persons and organizations across Rosfinmonitoring, OFAC SDN, EU consolidated, UK OFSI and UN Security Council lists. Four tools with neutral match output that always carries list version and check date, designed for KYC and AML workflows in AI assistants. stdio via pipx or uvx."
category: Compliance
stars: 0
added: 2026-09-02
source: "mcp.so GitHub issue #3896"
relevance: ★★★
tags: [sanctions, watchlist, aml, kyc, ofac, compliance]
---

# mcp-sanctions - Watchlist Screening for KYC and AML

**Stdio MCP server (PyPI)** - screens persons and organizations against public watchlists (Rosfinmonitoring, OFAC SDN, EU consolidated, UK OFSI, UN Security Council) with neutral match output: match level, list version and check date in every answer, plus a disclaimer. Manual verification remains required.

## Spec Block

| Field | Value |
|---|---|
| Server name | atomno-mcp-sanctions |
| Repo | github.com/atomno-mcp/mcp-sanctions |
| PyPI | atomno-mcp-sanctions v0.1.1 |
| Transport | stdio (pipx or uvx), hosted backend for data |
| Backend | https://api.atomno-mcp.ru/sanctions |
| Auth | Pro key required, sent as X-API-Key (env MCP_SANCTIONS_API_KEY) |
| License | MIT |
| Stars | 0 (new repo) |

## Why This Matters for Operators

Screening a counterparty against five watchlists in one call, with an explicit neutral match level instead of a binary verdict, is exactly the output a compliance workflow needs: the tool reports the match against a dated list version and leaves the decision to a human. It is built to be an input to KYC/AML processes, not a replacement for them.

## Tools & Capabilities (4 tools)

| Tool | Description |
|---|---|
| screen_person | Screen a natural person by full name, optionally with date of birth |
| screen_entity | Screen an organization by name, INN or OGRN |
| screen_inn | Quick lookup by Russian tax identification number |
| list_watchlists | Metadata on supported lists and their update dates |

## Installation

```bash
pipx install atomno-mcp-sanctions
# or: uvx atomno-mcp-sanctions
```

Cursor or Claude Desktop (mcp.json):

```json
{
  "mcpServers": {
    "sanctions": {
      "command": "uvx",
      "args": ["atomno-mcp-sanctions"],
      "env": { "MCP_SANCTIONS_API_KEY": "<your-pro-key>" }
    }
  }
}
```

## Configuration

- MCP_SANCTIONS_API_KEY - Pro key from atomno-mcp.ru/pricing, sent as the X-API-Key header (required)
- MCP_SANCTIONS_API_BASE - hosted backend URL (default https://api.atomno-mcp.ru/sanctions)
- MCP_SANCTIONS_TIMEOUT - HTTP timeout in seconds (default 30)

## Business Relevance

Useful for: compliance officers screening counterparties across five jurisdictions at once, KYC onboarding checks with auditable list versions and dates, and due-diligence workflows where the answer must state its source rather than assert a verdict.

## Limitations

The Central Bank of Russia denylist is not supported (not public). The tool explicitly does not make judgements and is not a basis for decisions on its own; every answer carries a disclaimer that data may age. Pro key required for the hosted data backend.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [World Monitor MCP - Global Intelligence: Markets, Risk, Supply Chains & Procurement](/docs/hermes/mcp/servers/external/world-monitor-mcp)
- [PassportCraft MCP - EU Digital Product Passports](/docs/hermes/mcp/servers/external/passportcraft-mcp)
