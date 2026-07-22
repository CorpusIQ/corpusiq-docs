---
title: EU VAT VIES MCP Server
subtitle: EU VAT number validation with legal audit trail
source: honest-vies-mcp
github: https://github.com/bartosz-kuc/honest-vies-mcp
created: 2026-07-22
category: Finance/Tax
stars: 0
tags: [vat, vies, eu, tax, compliance, ecommerce]
---

# EU VAT VIES MCP Server

Part of the **Honest MCP** suite. Validates EU VAT numbers through the official VIES (VAT Information Exchange System) and includes a **consultation number** for legal audit proof. Essential for EU e-commerce operators validating B2B customers.

## What It Does

VAT validation is required for EU cross-border B2B transactions (reverse charge mechanism). This MCP server:

- Validates VAT numbers against the official EU VIES database
- Returns the **consultation number** (legal proof of validation)
- Works fully offline/local — no data leaves your machine
- Part of a suite of Polish/EU business MCP servers

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **B2B Customer Validation** | "Validate this German customer's VAT ID before issuing a 0% invoice" |
| **Audit Preparation** | "Show me all VAT validations from Q3 with consultation numbers" |
| **E-commerce Compliance** | "OSS/IOSS validation for EU marketplace sellers" |
| **Supplier Verification** | "Check this Polish supplier's VAT before payment" |

## Installation

```bash
git clone https://github.com/bartosz-kuc/honest-vies-mcp
cd honest-vies-mcp
pip install -r requirements.txt
```

## Configuration

```json
{
  "mcpServers": {
    "vies-vat": {
      "command": "python",
      "args": ["-m", "honest_vies_mcp"],
      "env": {}
    }
  }
}
```

No API keys needed. Calls the public EU VIES SOAP API directly.

## Tools Provided

- `validate_vat` — Validate a single VAT number (country code + number)
- `validate_vat_batch` — Validate multiple VAT numbers
- `get_consultation_number` — Retrieve the consultation number for audit proof

## Limitations

- **VIES API reliability** — The public VIES API has known uptime issues. Validation may fail during EU business hours.
- **0 stars, brand new** — Created July 22, 2026.
- **EU only** — Doesn't cover non-EU VAT systems (UK, Norway, Switzerland).
- **No caching** — Each validation hits the API. Rate limits may apply.

## Operator Verdict

★★★ **Simple, essential, audit-ready.** For any EU e-commerce or B2B operator, VAT validation is a daily task. The consultation number for legal proof is the killer feature — most VIES wrappers don't include it. Low risk because it uses the official public API with no third-party dependency.
