---
title: "Truthifi MCP - Verified Household Finance Records"
description: "One verified household record for AI assistants - accounts, holdings, fees, performance and the Truthifi Score across 18,000+ institutions, read-only."
category: Finance
stars: n/a (hosted platform, truthifi.com)
added: 2026-10-05
source: "mcpservers.org /all"
relevance: ★★★
tags: [finance, wealth, household, portfolio, advisors, oauth, registry, read-only, remote-mcp]
---

# Truthifi MCP

**One verified household record your AI can actually read.** Truthifi is the financial hub for families, advisors and their agents: accounts, activity, holdings, fees, performance and cash flow from 18,000+ supported institutions, held in one verified record that is shared only on the household's terms. Its MCP server brings that record into Claude, ChatGPT, Cursor or any other client, with a Truthifi Score and the findings behind it. Nothing the assistant does can move money or place trades.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth with Dynamic Client Registration
Endpoint: https://api.truthifi.com/mcp
Tools: 30 (accounts, holdings, performance, fees, spending, diagnostics, controls)
Pricing: Free to start with limits; paid plans add connections, history and credits
Registry: com.truthifi/mcp
Built by: Truthifi, Inc.
```

## Why This Matters for Operators

An operator's financial life does not fit in one statement, and it does not fit in one AI chat either unless the data is actually assembled somewhere trustworthy first. Truthifi keeps the record whole: it decodes 18,000 institution dialects into one model, keeps it whole when a connection breaks, and reviews it nightly into a score with findings. The MCP layer then makes that record answerable: fees across every account, look-through stock exposure, benchmarked performance, and spending by category, each backed by the stored record rather than an estimate.

**The access model is the point.** The server is read-only against banks and brokerages; the only writes happen inside Truthifi (assets you track by hand, and a manual refresh), each with a preview and confirmation step. The assistant reads the truth; the household stays in control, and access can be revoked at any time.

## Tools

30 tools, grouped by what they answer:

| Group | Tools | What it covers |
|---|---|---|
| Accounts | `get_accounts`, `get_groups`, `connect_account`, `fix_connections` | Linked accounts and their history depth; groups, goals and wealth buckets; secure links to connect or repair institutions |
| Holdings | `get_dated_holdings`, `get_composition`, `get_equity_concentrations`, `get_market_cap_allocation` | Positions on a date; splits by asset class, sector, industry or country; true stock exposure through funds; market-cap sizing |
| Performance | `get_balance_history`, `get_performance_history`, `get_investment_transactions_summary` | Opening and closing balances; return, income and gain or loss against a benchmark; buys, sells and dividends by period |
| Fees | `get_fees` | Fees per account and type: maintenance, margin interest, advisory, commissions, fund fees |
| Cash flow | `get_transactions`, `get_budget_flow_summary` | Filterable transactions; spending and income by period and category |
| Diagnostics | `get_findings`, `get_truthifi_score_history`, `run_scan`, `get_scan_status` | The findings behind the Truthifi Score, its history, and manual refreshes |
| Manual records | `get_asset_liabilities`, `create_asset_liability`, `delete_asset_liability` | Assets and liabilities tracked by hand (home, car, mortgage), with preview and confirm |
| Reference | `get_security_info`, `get_security_distributions`, `get_security_news`, `get_truthifi_info` | Security details, distributions, ticker news and how Truthifi works |
| Account control | `get_advisors`, `get_subscription_info`, `get_subscription_catalog`, `upgrade`, `get_prompt_catalog` | Advisors from public regulatory records; plan, credits and tool access; ready-made prompt walkthroughs |

Tools draw MCP credits by plan, and some need a higher plan; `get_subscription_info` reports what the connection can use.

## Installation

Claude Code adds the hosted server in one line:

```bash
claude mcp add --transport http truthifi https://api.truthifi.com/mcp
```

The plugin variant bundles connector plus skills:

```bash
/plugin marketplace add truthifi/truthifi-mcp
/plugin install truthifi@truthifi
```

Claude (web and desktop): Settings, Connectors, Add custom connector, paste the server URL. ChatGPT connects through developer mode. Cursor, VS Code, Copilot CLI, Windsurf, Kiro, Zed, JetBrains, Cline and more have configs in the vendor's repository, and skills-aware agents can run `npx skills add truthifi/truthifi-mcp`.

## Business Relevance

- **Founders with personal portfolios** get fee audits, concentration checks and cash-flow reviews without exporting spreadsheets to each tool.
- **Advisors** work from the same verified household record their clients see, with the advisors' own details pulled from public regulatory records.
- **Family offices and operators** answer "what is this costing me" questions on fees and fund layers in seconds, each finding tied to stored data.
- **Anyone delegating finance questions to an agent** gets read-only access by construction: the assistant can analyze, not transact.

## Integration with CorpusIQ

CorpusIQ answers business questions from the systems a company runs on: Stripe, QuickBooks, Shopify, GA4 and 40+ connectors, read-only. Truthifi covers the other side of an operator's life: the household record, its fees, holdings and cash flow. In one chat they compose naturally: business performance from CorpusIQ, personal and family wealth from Truthifi, each from its own verified, read-only record. Neither writes to the institutions behind it, so asking should never require trusting an agent with money movement.

## Limitations

- A Truthifi account is required and available data varies by institution; aggregator delays apply, so check material figures against statements.
- Some tools and higher connection counts need paid plans, and tools consume MCP credits per call.
- Coverage is US-focused: 18,000+ institutions through US data partners.
- Truthifi provides data and analysis, not investment, tax or legal advice.
- ChatGPT support depends on developer-mode connectors and plan rules set by OpenAI.

## FAQ

### Can the assistant move money?

No. Bank and brokerage access is read-only. Three tools change data inside Truthifi only (assets you track by hand and a refresh), always with preview and confirmation.

### How do I connect it in Claude?

Settings, Connectors, Add custom connector, paste `https://api.truthifi.com/mcp`, sign in with OAuth. On Team and Enterprise, an owner adds it first.

### What is the Truthifi Score?

A nightly review of the whole record that surfaces where to focus, with the findings behind it readable through `get_findings` and `get_truthifi_score_history`.

### Is there a free tier?

Yes, you can start free with limits; `get_subscription_info` and `get_subscription_catalog` show what each plan includes, and `upgrade` returns a link.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [X1 Wealth MCP - Cited Family Office Records](/hermes/mcp/servers/external/x1-wealth-mcp/)
- [Velarion MCP - Executive Compensation and Governance](/hermes/mcp/servers/external/velarion-company-intelligence/)
- [Accountable MCP - AI Bookkeeping for Startups](/hermes/mcp/servers/external/accountable-mcp/)
