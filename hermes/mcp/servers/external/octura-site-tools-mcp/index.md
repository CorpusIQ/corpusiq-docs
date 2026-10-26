---
title: "Octura Site Tools MCP: Deterministic ERP and Tax Calculators"
description: "Hosted keyless MCP server with 30 deterministic ERP calculators - Odoo implementation, migration, upgrade, ROI and TCO costs, US, Canada and EU sales tax, Canadian payroll source deductions, inventory maths, and ERP selection scoring. Live-probed com.octurasolutions/site-tools v1.0.0."
category: ERP
stars: n/a (hosted; repo 0 stars)
added: 2026-08-23
source: "mcpservers.org /all + GitHub README + live endpoint probe"
relevance: ★★★
tags: [odoo, erp, sales-tax, payroll, inventory-planning, roi, calculators, remote-mcp]
last_updated: "2026-10-19"
---

# Octura Site Tools MCP

**A hosted, keyless MCP server exposing 30 deterministic ERP calculators - Odoo implementation, migration and upgrade costs, ROI and total cost of ownership, sales tax for the US, Canada and the EU, Canadian payroll source deductions, and inventory maths like reorder point, safety stock and EOQ.** Every tool is a pure function: same inputs, same outputs, no model in the loop and no randomness. Live-probed this sweep: server `com.octurasolutions/site-tools` v1.0.0, protocol 2025-03-26, 30 tools returned by `tools/list`.

```
Server type: Remote (Streamable HTTP, hosted, stateless)
Auth: None (no API key)
Endpoint: https://octurasolutions.com/mcp
Tools: 30 (live-probed Aug 23, 2026)
Registry: com.octurasolutions/site-tools
Rate limits: per IP, X-RateLimit-Limit / X-RateLimit-Remaining headers
Category: ERP / Operations
Built by: Octura Solutions (Official Odoo Partner)
```

## Why This Matters for Operators

Asking a language model to compute a payback period or a Quebec QST total invites a plausible-looking wrong number. These tools return the arithmetic instead, along with the inputs they used, so the result can be checked - which matters when the number is going into an ERP budget or a payroll run. The trade-off is stated plainly by the vendor: they are calculators, not advice, and the cost models carry assumptions (regional rates, blended hourly costs) that a real quote would replace.

The Odoo cluster is the standout: implementation, migration, upgrade, TCO, ROI, EDI-readiness, hosting cost and even a project-rescue risk grader, plus an ERP selection tool that scores your shortlist across ten systems. That is the exact stack of questions a business asking "should we move to Odoo and what will it cost" wants answered without a sales call.

## Tools & Capabilities

30 tools confirmed by live probe, grouped by domain:

| Area | Tools |
|---|---|
| Odoo cost modeling | `odoo-implementation-cost-calculator`, `odoo-migration-cost-calculator`, `odoo-upgrade-cost-calculator`, `odoo-total-cost-of-ownership-calculator`, `odoo-roi-calculator`, `odoo-edi-readiness-cost-estimator`, `odoo-sh-pricing-calculator`, `odoo-stack-savings-calculator`, `odoo-app-selector`, `odoo-conf-tuner`, `odoo-project-rescue-risk-grader` |
| Sales tax | `us-sales-tax-calculator` (all 50 states + DC), `us-sales-tax-nexus-checker`, `canadian-sales-tax-calculator` (GST/HST/PST/QST), `eu-vat-calculator` (VAT rates + VIES validation) |
| Payroll | `canadian-payroll-source-deductions-calculator` (CPP, EI, income tax) |
| Inventory maths | `inventory-turnover-calculator`, `reorder-point-calculator`, `safety-stock-calculator`, `economic-order-quantity-calculator`, `inventory-carrying-cost-calculator`, `landed-cost-calculator`, `margin-and-markup-calculator`, `oee-calculator` |
| Selection & content | `erp-selection-tool`, `ask_octura`, `compare_odoo_vs`, `find_odoo_apps_for`, `get_odoo_pricing`, `get_partner_profile` |

The server is stateless and tools-only (implements `initialize`, `ping`, `tools/list`, `tools/call`; no resources, no prompts). Tax rates and payroll figures are maintained on a best-effort basis and are not a substitute for filing advice from an accountant.

## Installation

```bash
claude mcp add --transport http octura https://octurasolutions.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "octura": {
      "type": "streamable-http",
      "url": "https://octurasolutions.com/mcp"
    }
  }
}
```

No key, no signup. Rate limits are per IP and surfaced via `X-RateLimit-Limit` and `X-RateLimit-Remaining` headers; exceeding the ceiling returns HTTP 429 with a `Retry-After` header.

## Business Relevance

- **Companies evaluating or migrating ERP** get implementation, migration, upgrade, TCO and ROI estimates in one chat, plus a 10-system selection scorecard.
- **US and Canadian operators** check nexus exposure, state sales tax, GST/HST/PST/QST and source deductions with deterministic arithmetic they can audit.
- **Inventory managers** compute reorder points, safety stock, EOQ and landed cost without spreadsheet archaeology.
- **Odoo partners and implementers** can hand clients a self-service estimation surface instead of a discovery call.
