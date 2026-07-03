---
title: "AI2Fin Tax MCP — Global Tax Rates for 50+ Countries"
description: "Free, no-login MCP server giving AI agents instant access to verified tax rates, GST/VAT, income tax, company tax, and capital gains tax for 50+ countries. Source-cited from national tax authorities with verified dates."
category: mcp
tags: [mcp-server, tax, vat, gst, finance, accounting, global, ai2fin, hermes-agent]
last_updated: 2026-07-03
---

# AI2Fin Tax MCP Server ★ New (July 3)

## Overview

AI2Fin Tax MCP is a free, public MCP server that gives any AI agent or assistant — Claude, ChatGPT, Cursor, VS Code, or a custom build — instant access to accurate, source-cited tax data for 50+ countries. No login. No API key. No setup beyond pasting one URL: `https://taxmcp.ai2fin.com`.

**Key advantage: Every answer cites the national tax authority it came from (ATO, IRD, HMRC, IRS and more) with a verified date — so you always know a number is current and where to confirm it.**

## Key Features

- **Tax rate lookup for 50+ countries**: GST/VAT standard and reduced rates, top personal income tax rate, and company tax rate from Australia and New Zealand to the UK, US, India, Canada, the EU and beyond (`tax_rate_lookup`)
- **GST/VAT calculations**: Instant tax-inclusive ↔ tax-exclusive conversion for invoices, quotes, pricing, and expense checks — automatically using the correct rate for the right country (`compute_gst_vat`)
- **Cross-country tax comparison**: Compare GST/VAT, income tax, and company tax side-by-side in one call — ideal for relocation research, market expansion, or international pricing strategy (`compare_countries`)
- **Income tax estimates**: Estimate take-home pay for Australia and New Zealand using effective-dated brackets that roll over automatically at each financial year (`income_tax_estimate`)
- **Company tax estimates**: Estimate company tax on profit for Australia, the US, UK, India, and Canada — including small-business rates and thresholds (`company_tax_estimate`)
- **Capital gains tax**: Estimate Australian CGT for resident individuals — handles capital losses, the 12-month CGT discount, and marginal-rate stacking (`cgt_estimate`)

## Installation

```bash
# Streamable HTTP — no install needed. Just add the URL:
hermes mcp add ai2fin-tax --url https://taxmcp.ai2fin.com/
```

## Configuration

```json
{
  "mcpServers": {
    "ai2fin-tax": {
      "type": "streamableHttp",
      "url": "https://taxmcp.ai2fin.com/"
    }
  }
}
```

No environment variables, API keys, or authentication required. The server is stateless and private by design — it computes over published rate data only and stores nothing you send.

## Business Relevance

- **E-commerce operators**: Calculate correct GST/VAT on cross-border sales instantly. Compare tax rates across target markets before expanding
- **Finance & accounting teams**: Automate GST/VAT calculations in agent workflows. Source-checked rates mean fewer manual verification steps
- **Pricing strategists**: Model take-home pay and effective tax rates for different country operations. Compare company tax burdens across jurisdictions
- **Freelancers & consultants**: Invoice with correct GST/VAT for any client country. Estimate quarterly tax obligations without leaving your agent workspace
- **International expansion**: Side-by-side tax comparisons for market entry decisions. Know the real tax burden before committing resources

## Integration with CorpusIQ

AI2Fin Tax MCP complements CorpusIQ's 37+ business connectors perfectly:

1. **CorpusIQ Shopify + AI2Fin**: Pull order data from Shopify, look up the customer's country tax rate via AI2Fin, and validate that the correct GST/VAT was applied — all in one agent workflow
2. **CorpusIQ QuickBooks + AI2Fin**: Cross-reference QuickBooks tax codes against AI2Fin's verified national rates to catch misconfigurations before filing
3. **CorpusIQ Stripe + AI2Fin**: Compare Stripe-collected tax amounts against AI2Fin's source-cited rates for any country — build an automated tax validation pipeline
4. **Agent workflow**: "Check all Shopify orders from EU customers this month, verify the VAT rates applied match AI2Fin's current rates for each country, and flag any discrepancies"

## Limitations

- **Not tax advice**: General information only. Every figure links to the authority so you can confirm it. For actual tax filing, use the authenticated 2Fin app MCP at `api.ai2fin.com/mcp`
- **Country coverage varies by tool**: Tax rate lookups cover 50+ countries, but income tax estimates are currently limited to Australia and New Zealand, and company tax estimates cover 5 countries (AU, US, UK, IN, CA)
- **Streamable HTTP only**: No stdio transport — requires network access to `taxmcp.ai2fin.com`
- **Read-only data**: The free MCP provides published rates. For personalized tax position calculations (your actual income, deductions, categories), the separate authenticated 2Fin app MCP is required
- **New server**: Submitted to mcp.so July 2, 2026. Community adoption and tool reliability are still developing

## See Also

- [Aikount MCP — Spanish Accounting](/hermes/mcp/servers/external/aikount/) — complementary for Spanish-market operators who need invoicing + tax compliance
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [AI2Fin Web Calculators](https://ai2fin.com/tools) — the same data powering the MCP, available as free browser tools
