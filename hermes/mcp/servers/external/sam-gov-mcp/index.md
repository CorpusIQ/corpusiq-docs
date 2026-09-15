---
title: "mcp-sam-gov - US Government Contracting MCP Server"
description: "152-tool keyless-first MCP server for US federal + state/local government contracting, spending, regulation, and partner vetting. SAM.gov, USAspending"
source: github.com/cliwant/mcp-sam-gov
stars: 4
language: TypeScript
transport: stdio
auth: "None for 147 of 152 tools (keyless-first; 5 tools need a free key)"
category: Government/Procurement
last_updated: 2026-09-15
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/sam-gov-mcp/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# mcp-sam-gov - US Government Contracting MCP

**152 tools across 54 data sources for US federal + state/local (SLED) government contracting.** First MCP server purpose-built for the $750B+ US government procurement market. Keyless-first - 147 of the 152 tools need no API key; the remaining 5 (Census business patterns, FRED, BEA, DOL data endpoint) take a free key.

## What It Does for Operators

If your business bids on government contracts, seeks grant funding, vets partners against sanctions lists, or monitors regulatory changes - this server gives your AI agents direct access to the primary sources:

- **SAM.gov** - Search active federal contract opportunities, notice detail and attachments, exclusion/integrity screening, wage determinations
- **USAspending.gov** - Track federal spending by agency, recipient, and contract
- **Grants.gov** - Find and monitor federal grant opportunities
- **OFAC SDN** - Screen entities against US sanctions lists
- **FDIC** - BankFind, financial institution data
- **EPA** - ECHO facility compliance/enforcement, TRI facilities
- **CourtListener** - Federal court opinions (case law), via the Free Law Project's public API
- **47 additional sources** covering all major government data domains

## Installation

```bash
npx -y @cliwant/mcp-sam-gov
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
      "args": ["-y", "@cliwant/mcp-sam-gov"]
    }
  }
}
```

No environment variables or API keys are needed for 147 of the 152 tools. A few sources accept an optional free key that only raises rate limits; the `api_key_status` tool reports which keys are required, optional, or currently configured.

## Key Tools

| Tool | Source | Use Case |
|------|--------|----------|
| `sam_search_opportunities` | SAM.gov | Search active federal contracting opportunities; narrow by NAICS, agency, set-aside, state |
| `sam_check_exclusions` | SAM.gov | Screen a firm or individual by name, UEI, or CAGE against the SAM exclusions (debarment) index |
| `usas_search_individual_awards` | USAspending.gov | Line-item federal contracts with recipient, dollars, sub-agency, state, and description |
| `grants_search` | Grants.gov | Search federal grant opportunities by keyword, CFDA, agency, or opportunity number (forecasted + posted by default) |
| `ofac_screen_entity` | OFAC SDN | Screen a name against the OFAC SDN and Consolidated sanctions lists, including AKAs |
| `fdic_search_institutions` | FDIC | Search the FDIC-insured institution directory (BankFind) by name, city, state, or CERT |
| `courtlistener_search_opinions` | CourtListener | Full-text search of US federal court opinions (case law) |
| `echo_search_facilities` | EPA ECHO | Search EPA-regulated facilities by state with compliance and enforcement screening fields |

## Operator Use Cases

1. **GovCon BD Teams** - Set up an AI agent to scan SAM.gov daily for RFPs matching your NAICS codes. Get Slack/email alerts for new opportunities.

2. **Compliance Officers** - Automate OFAC sanctions screening against vendor lists. Run batch checks from any MCP client.

3. **Grant Writers** - Monitor Grants.gov for funding opportunities. Pull full solicitation text and eligibility requirements into your AI workflow.

4. **Partner Due Diligence** - Cross-reference a company name against SAM.gov exclusions, OFAC SDN, and CourtListener in one query.

5. **Competitive Intelligence** - Track which competitors are winning federal contracts. Map agency spend patterns.

## Honesty-Hardened

The server includes "honesty-hardened" design: when data is unavailable or a query returns no results, it reports that explicitly rather than hallucinating. All responses cite the source agency.

## CorpusIQ Angle

Complementary to CorpusIQ's business data connectors. While CorpusIQ provides financial/operational data from platforms like QuickBooks and Stripe, mcp-sam-gov provides the government contracting layer - procurement opportunities, compliance screening, and regulatory intelligence. Operators in government contracting can use both together: CorpusIQ for business operations, mcp-sam-gov for the federal sales pipeline.

## Limitations

- US-focused (federal + state/local). No international government procurement.
- Keyless = public data only. No authenticated access to contractor portals.
- Early-stage project (4⭐). API stability not guaranteed.
- Rate limits on some `.gov` endpoints (varies by agency).
