---
title: "Oromi Agent Services MCP"
server_name: "Oromi Agent Services"
repo_url: "https://agents.oromi.co.uk"
mcp_endpoint: "https://agents.oromi.co.uk/mcp"
install_command: "npx -y oromi-agent-services-mcp"
stars: N/A
stars_display: "N/A"
category: "Business Intelligence"
relevance: "HIGH — UK business data, property, verification"
date_added: "2026-07-26"
source: "mcp.so (Jul 23, 2026) + direct API discovery"
status: "active"
---

# Oromi Agent Services MCP

**AI agents for UK business operations** — 25 pay-per-call tools accessible through any MCP client. Companies House registry, HM Land Registry property data, agent-readiness audits, domain/email verification, and even human-in-the-loop tasks.

## What It Is

Oromi Agent Services provides machine-payable APIs (via x402/USDC on Base) that expose verified UK business and property data to AI agents. All 25 tools auto-generate from a live OpenAPI spec, so your agent always has current schemas. Two MCP access methods: `npx` package (auto-pays via x402) or remote `/mcp` endpoint.

## Why Business Operators Should Care

If you or your agents operate in the UK market, Oromi replaces four separate data sources with one MCP connection:

- **UK Company Due Diligence**: Companies House profiles, officers, SIC codes, accounts due dates, domain trust signals — one call with a red-flag verdict (`/api/uk-business/due-diligence`, $0.10)
- **Property Market Intelligence**: Sold prices, price trends, area crime stats, mortgage math, EPC ratings — all from HM Land Registry and official sources
- **Business Name Checking**: Verify proposed company names against the live Companies House register before filing
- **Agent Readiness Scanning**: Audit any website for agent-usable structured data (schema.org, contact channels, booking links) with a 0-100 score
- **Citation Insurance**: Verify URLs, emails, domains, EU VAT numbers, and IBANs before your agent acts on them
- **Human-in-the-Loop**: Real humans answer yes/no questions ($0.50) or perform small tasks ($3.00) — answered within 2 hours during UK business hours

## Setup

### Remote MCP (Recommended)

Add to any MCP client as a remote server:

```
Endpoint: https://agents.oromi.co.uk/mcp
Transport: Streamable HTTP
Auth: x402 (USDC on Base)
```

### Local Package

```bash
npx -y oromi-agent-services-mcp
```

The npx package auto-handles x402 micropayments. All 25 tools are discovered automatically from the live OpenAPI spec — no manual tool registration needed.

### Claude Desktop Configuration

```json
{
  "mcpServers": {
    "oromi-agent-services": {
      "command": "npx",
      "args": ["-y", "oromi-agent-services-mcp"]
    }
  }
}
```

### Claude Code / Cursor

```bash
claude mcp add oromi-agent-services -- npx -y oromi-agent-services-mcp
```

## Key Tools

| Tool | Price | What It Does |
|------|-------|--------------|
| `uk-business-due-diligence` | $0.10 | Full company profile + officers + domain trust + red-flag verdict |
| `uk-business-search` | $0.005 | Search Companies House by name |
| `uk-business-name-check` | $0.01 | Check proposed business name availability |
| `uk-property-market-summary` | $0.03 | Area price trends, momentum, FTB price point, market read |
| `uk-property-sold-prices` | $0.02 | Actual sold transactions for a postcode |
| `uk-property-area-crime` | $0.02 | Street-level crime stats for a postcode |
| `uk-property-mortgage-context` | $0.005 | Deterministic mortgage math + stress test |
| `agent-ready-scan` | $0.05 | Website agent-readiness score (0-100) |
| `verify-email` | $0.005 | MX check + deliverability verdict |
| `verify-domain` | $0.01 | RDAP age + DNS/HTTPS + trust signal |
| `verify-vat-eu` | $0.01 | EU VAT validation via VIES |
| `verify-iban` | $0.002 | MOD-97 checksum validation |
| `official-rates` | $0.005 | UK statutory figures (BoE rate, CPI, min wage, tax thresholds) |
| `url-status` | $0.001 | Citation insurance — bulk-check URLs |
| `human-verify` | $0.50 | Real human answers yes/no (async, <2hr) |
| `human-task` | $3.00 | Real human performs small check/task (async, <2hr) |
| `crypto-context` | $0.005 | Calibrated market context for one asset |
| `web-extract` | $0.01 | Fetch any page as clean text |
| `pdf-extract` | $0.02 | PDF to text (up to 100 pages) |
| `validate-json` | $0.002 | JSON Schema validation with path-precise errors |

## Business Use Cases

### Due Diligence on UK Prospects
Your agent pulls a full due-diligence pack ($0.10): company status, officers, domain age, HTTPS status, and a red-flag verdict — all before you spend time on outbound.

### Property Investment Research
Agent checks an area's market summary ($0.03) + sold prices ($0.02) + crime stats ($0.02) + mortgage math ($0.005) — $0.075 total for a complete investment snapshot from official data.

### Business Name Validation
Before registering a UK company, your agent checks name availability ($0.01) against the live Companies House register — catches exact matches and similar names that would be rejected.

### Agent-Ready Website Audits
Scan any business website ($0.05) to see if AI agents can interact with it programmatically — schema.org data, booking links, opening hours, contact channels, and a 0-100 readiness score with per-check breakdown.

### Human Sanity Checks
For high-stakes decisions where you want a second pair of eyes: `human-verify` ($0.50) gets a real person to answer yes/no questions like "Does this website look legitimate?" or "Is this photo actually the product described?"

## Limitations

- **UK-only**: All business/property data is UK-specific. Companies House, HM Land Registry, FSA, and UK statutory rates.
- **x402 micropayments required**: Pay-per-call via USDC on Base. Budget accordingly for high-volume agent workflows.
- **Human tasks async**: `human-verify` and `human-task` are async (typically <2 hours, UK business hours 08:00-22:00).
- **Scotland/NI property**: EPC data is England & Wales only (separate registers for Scotland/NI return zero with explanatory note).
- **No bulk endpoints**: Each call is priced individually. For bulk due diligence, batch multiple calls.

## Pricing Summary

- **Micro-checks**: $0.001-$0.01 (URL status, IBAN, rates, email verify, fx)
- **Business data**: $0.005-$0.10 (search, company profile, due diligence)
- **Property data**: $0.005-$0.03 (mortgage math, sold prices, market summary, crime)
- **Agent tools**: $0.01-$0.05 (web extract, PDF extract, agent-ready scan, JSON validate)
- **Human tasks**: $0.50-$3.00 (async verification, small tasks)

## CorpusIQ Integration Potential

Oromi's agent-readiness scan ($0.05) could complement CorpusIQ's business connector approach — identify whether a prospect's website is structured for agent interaction before CorpusIQ attempts integrations. The due-diligence endpoint ($0.10) could feed lead qualification pipelines.

## Tags

`uk-business` `companies-house` `property-data` `due-diligence` `verification` `x402` `micropayments` `business-intelligence` `human-in-the-loop`
