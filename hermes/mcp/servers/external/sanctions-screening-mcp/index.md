---
title: Sanctions Screening MCP Server
subtitle: OFAC/EU/UK/UN compliance screening through MCP
source: sanctions-screening-mcp
github: https://github.com/apifymcpfactory-droid/sanctions-screening-mcp
created: 2026-07-22
category: Compliance
stars: 0
tags: [sanctions, ofac, compliance, aml, kyc, fintech]
---

# Sanctions Screening MCP Server

MCP server for **OFAC, EU, UK, and UN sanctions screening**. Hosted on MCPize. Enables AI agents to perform compliance checks directly — essential for fintech AML/KYC workflows, payment processors, and any business handling international transactions.

## What It Does

Sanctions screening is legally required for financial services. This MCP server wraps consolidated sanctions lists into agent-callable tools:

- **OFAC** — US Treasury Office of Foreign Assets Control (SDN list)
- **EU Consolidated List** — European Union sanctions
- **UK Sanctions List** — HM Treasury / OFSI
- **UN Security Council** — United Nations consolidated sanctions

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **Customer Onboarding** | "Screen this customer against all sanctions lists before activating their account" |
| **Payment Screening** | "Check this SWIFT transaction beneficiary against OFAC" |
| **Periodic Review** | "Re-screen all high-risk customers monthly" |
| **Vendor Due Diligence** | "Screen this new supplier against EU/UK sanctions" |

## Installation

Hosted on **MCPize** — no local install required. Connect directly:

```json
{
  "mcpServers": {
    "sanctions-screening": {
      "type": "url",
      "url": "https://api.mcpize.com/sanctions-screening/mcp"
    }
  }
}
```

For self-hosted:

```bash
git clone https://github.com/apifymcpfactory-droid/sanctions-screening-mcp
cd sanctions-screening-mcp
npm install
```

## Tools Provided

- `screen_individual` — Screen a person/entity by name against all lists
- `screen_batch` — Batch screen multiple entities
- `check_ofac` — OFAC-specific screening
- `check_eu` — EU-specific screening
- `check_uk` — UK-specific screening
- `check_un` — UN-specific screening

## Limitations

- **0 stars, brand new** — Created July 22, 2026. Not proven.
- **Hosted on MCPize** — Third-party dependency. Data goes through their infra.
- **No watchlist monitoring** — One-time screening only. No ongoing monitoring.
- **Regulatory gap** — Sanctions screening results must be reviewed by humans for regulatory compliance. Agent-only screening is insufficient for audit.

## Operator Verdict

★★★ **Critical capability, watch for maturity.** Sanctions compliance is non-negotiable for fintech. This fills a real gap in the MCP ecosystem. The hosted MCPize model reduces setup friction but introduces third-party risk. Wait for adoption signals (>20 stars, first production deployment report) before relying on it for actual compliance workflows.
