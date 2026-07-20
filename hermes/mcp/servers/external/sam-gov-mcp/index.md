---
title: "mcp-sam-gov — US Government Contracting MCP Server"
description: "150-tool keyless MCP server for US federal + state/local government contracting, spending, regulation, and partner vetting. SAM.gov, USAspending, Grants.gov, OFAC, FDIC, EPA, CourtListener + 45 more sources."
source: github.com/cliwant/mcp-sam-gov
stars: 4
language: TypeScript
transport: stdio
auth: None (keyless — uses public APIs)
category: Government/Procurement
last_updated: 2026-07-20
---

# mcp-sam-gov — US Government Contracting MCP

**150 tools for US federal + state/local (SLED) government contracting.** First MCP server purpose-built for the $750B+ US government procurement market. Keyless — zero API keys required, all data from public government APIs.

## What It Does for Operators

If your business bids on government contracts, seeks grant funding, vets partners against sanctions lists, or monitors regulatory changes — this server gives your AI agents direct access to the primary sources:

- **SAM.gov** — Search active federal contract opportunities, entity registrations, exclusions
- **USAspending.gov** — Track federal spending by agency, recipient, and contract
- **Grants.gov** — Find and monitor federal grant opportunities
- **OFAC SDN** — Screen entities against US sanctions lists
- **FDIC** — BankFind, financial institution data
- **EPA** — Environmental data, enforcement, permits
- **CourtListener** — Federal and state court records, dockets, opinions
- **45+ additional sources** covering all major government data domains

## Installation

```bash
npx -y mcp-sam-gov
```

Or clone and run locally:

```bash
git clone https://github.com/cliwant/mcp-sam-gov.git
cd mcp-sam-gov
npm install
npm run build
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "sam-gov": {
      "command": "npx",
      "args": ["-y", "mcp-sam-gov"]
    }
  }
}
```

No environment variables. No API keys. All data from public `.gov` endpoints.

## Key Tools

| Tool | Source | Use Case |
|------|--------|----------|
| `search_contract_opportunities` | SAM.gov | Find active RFPs/RFQs by NAICS, keyword, agency, set-aside |
| `get_entity_registration` | SAM.gov | Verify vendor registrations, UEI numbers, CAGE codes |
| `search_usaspending` | USAspending.gov | Track federal awards by recipient, agency, CFDA program |
| `search_grants` | Grants.gov | Find open and forecasted grant opportunities |
| `screen_ofac` | OFAC SDN | Sanctions screening for partner/entity vetting |
| `search_fdic` | FDIC | BankFind lookup, financial institution data |
| `search_court_records` | CourtListener | Federal/state dockets, opinions, party search |
| `search_epa` | EPA | Enforcement actions, permits, environmental data |

## Operator Use Cases

1. **GovCon BD Teams** — Set up an AI agent to scan SAM.gov daily for RFPs matching your NAICS codes. Get Slack/email alerts for new opportunities.

2. **Compliance Officers** — Automate OFAC sanctions screening against vendor lists. Run batch checks from any MCP client.

3. **Grant Writers** — Monitor Grants.gov for funding opportunities. Pull full solicitation text and eligibility requirements into your AI workflow.

4. **Partner Due Diligence** — Cross-reference a company name against SAM.gov exclusions, OFAC SDN, and CourtListener in one query.

5. **Competitive Intelligence** — Track which competitors are winning federal contracts. Map agency spend patterns.

## Honesty-Hardened

The server includes "honesty-hardened" design: when data is unavailable or a query returns no results, it reports that explicitly rather than hallucinating. All responses cite the source agency.

## CorpusIQ Angle

Complementary to CorpusIQ's business data connectors. While CorpusIQ provides financial/operational data from platforms like QuickBooks and Stripe, mcp-sam-gov provides the government contracting layer — procurement opportunities, compliance screening, and regulatory intelligence. Operators in government contracting can use both together: CorpusIQ for business operations, mcp-sam-gov for the federal sales pipeline.

## Limitations

- US-focused (federal + state/local). No international government procurement.
- Keyless = public data only. No authenticated access to contractor portals.
- Early-stage project (4⭐). API stability not guaranteed.
- Rate limits on some `.gov` endpoints (varies by agency).
