---
title: Aikount MCP Server Integration Guide
description: Spanish accounting for AI agents — issue invoices, OCR expense PDFs, reconcile bank movements, and prepare quarterly VAT returns (Modelo 303) with Aikount MCP
category: mcp
tags: [mcp, aikount, accounting, spanish, iva, modelo-303, invoices, expenses, autónomo, hermes-agent]
last_updated: 2026-06-28
---

# Aikount MCP — Spanish Accounting Automation for Hermes Agent

Spanish accounting (contabilidad) for AI agents. Issue invoices, OCR expense PDFs into deduplicated purchases, reconcile bank movements, and prepare quarterly VAT returns (Modelo 303) — all through the Aikount REST API, accessible via MCP.

## What It Does

Aikount brings Spanish tax-compliant accounting to AI agents:

- **Invoice issuance** — Create and send facturas compliant with Spanish tax requirements
- **Expense capture** — OCR expense PDFs (facturas de gastos) into categorized, deduplicated purchase records
- **Bank reconciliation** — Match bank movements to invoices and expenses automatically
- **VAT returns (Modelo 303)** — Prepare quarterly IVA returns with all required calculations
- **Autónomo-ready** — Designed for freelancers and SMEs in the Spanish tax system

## Quick Setup

### Prerequisites
- **Aikount account:** Sign up at [aikount.com](https://aikount.com)
- **Aikount API key:** Generate from your Aikount dashboard

### Add to Hermes Agent

```bash
# With API key
hermes mcp add aikount -- env AIKOUNT_API_KEY=your_key -- npx -y aikount-mcp
```

Or manual config:

```json
{
  "mcpServers": {
    "aikount": {
      "command": "npx",
      "args": ["-y", "aikount-mcp"],
      "env": {
        "AIKOUNT_API_KEY": "ak_your_api_key"
      }
    }
  }
}
```

## Key Capabilities

| Tool | Description |
|------|-------------|
| `create_invoice` | Issue a factura with client details, line items, IVA rates, and IRPF withholding |
| `ocr_expense` | Submit an expense PDF for OCR extraction and categorization |
| `list_expenses` | List captured expenses with categories, IVA, and deductible status |
| `reconcile_bank` | Match bank CSV/statement entries to invoices and expenses |
| `prepare_modelo_303` | Generate quarterly VAT return (Modelo 303) with all calculations |
| `get_tax_summary` | Get current-period IVA soportado, repercutido, and net position |

## Use Cases for Business Operators

### 1. Automated Invoice Processing
Have your AI agent handle invoice creation end-to-end:

```
Agent prompt: "Issue an invoice to ClienteTech SL (NIF B12345678) 
for our consulting work in June: 40 hours at €85/hour. 
Apply 21% IVA and 15% IRPF withholding. Email to administracion@clientetech.es."
```

### 2. Expense PDF OCR
Process a stack of expense receipts automatically:

```
Agent prompt: "OCR these 12 expense PDFs from my June purchases. 
Categorize them, extract IVA amounts, flag any that are 
non-deductible, and add them to my Q2 expenses."
```

### 3. Bank Reconciliation
Close the month by reconciling bank movements:

```
Agent prompt: "Here's my June bank statement CSV from BBVA. 
Reconcile all movements against my June invoices and expenses. 
Flag any unmatched transactions for manual review."
```

### 4. Quarterly VAT Return (Modelo 303)
Prepare the quarterly IVA filing:

```
Agent prompt: "Prepare my Q2 2026 Modelo 303. 
Calculate IVA repercutido from all issued invoices, 
IVA soportado from all captured expenses, 
apply prorrata if applicable, and show the net result 
(a pagar or a devolver)."
```

## Integration with CorpusIQ

Aikount + CorpusIQ = complete Spanish business operations:

1. **CorpusIQ Stripe connector** → pull payment data for invoice matching
2. **CorpusIQ email connector** → find supplier invoices for expense capture
3. **AI agent** → reconcile Stripe payouts against Aikount invoices
4. **Aikount** → generate Modelo 303 from reconciled data

This gives Spanish-market operators an AI-native accounting stack from sales to tax filing.

## Spanish Tax Compliance

Aikount handles key Spanish tax requirements:

- **IVA rates:** 21% general, 10% reducido, 4% superreducido, 0% exento
- **IRPF withholding:** Professional retention rates (15% general, 7% nuevos autónomos)
- **Modelo 303:** Quarterly VAT self-assessment with casilla mapping
- **Recargo de equivalencia:** Supported for retail/trade businesses
- **FacturaE format:** Structured electronic invoice format (when required)

## Pricing

Check [aikount.com](https://aikount.com) for current plans. Typically offers free tier for basic autónomo needs with paid plans for SMEs and gestorías.

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*

*↑ [MCP Documentation](/hermes/mcp/)*
