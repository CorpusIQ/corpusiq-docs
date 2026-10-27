---
title: "Taxley MCP - Free UK Corporation Tax Calculations"
description: "Seventeen free UK Corporation Tax tools over MCP: CT estimates, deadlines, late penalties, director loans, capital allowances and salary vs dividends."
category: "Finance / Accounting"
stars: n/a (new listing)
added: 2026-10-14
source: "mcpservers.org /all (October 14, 2026 evening sweep)"
relevance: ★★
tags: [uk, tax, corporation-tax, hmrc, accounting, calculators, keyless]
last_updated: "2026-10-24"
---

# Taxley MCP

**Free UK Corporation Tax calculators over MCP: an agent works out a company's tax across 17 tools modeled on the rules published on GOV.UK, covering CT estimates with small profits rate and marginal relief, deadlines, late penalties, director loans, capital allowances, benefits in kind, dividends and salary planning. Keyless endpoint, no account; every answer links back to the result on taxley.co.uk. Published by Taxley.**

```
Server type: Hosted (Streamable HTTP, JSON-RPC 2.0)
Endpoint: https://taxley.co.uk/mcp
Auth: none (keyless; free to call)
Server: taxley v1.0.0 (initialize returns 200)
Tools: 17 calculators and checkers (list below)
Basis: the rules published on GOV.UK for UK companies
Publisher: Taxley (taxley.co.uk); also available as a JSON API and site embeds
Listing: mcpservers.org /all, October 14, 2026 evening sweep
```

## Why This Matters for Operators

UK tax questions arrive constantly and answering them usually means spreadsheets, stale calculator pages, or a round trip to an accountant. "What will the corporation tax be this year", "when is the CT600 due", "what happens if we file late", "can we pay this dividend", "salary or dividends" - each is a small calculation with rules that change.

Taxley puts those calculations behind MCP tools that an assistant can call directly, with inputs like accounting period start and end, taxable profits, associated companies and short or straddled periods. Answers include the tax, the effective rate, and payment and filing dates - and every result links back to the worked calculation on taxley.co.uk. The tools are deterministic implementations of published rules, so the agent's arithmetic is reproducible instead of guessed.

## Tools

| Tool | What it works out |
|---|---|
| uk_corporation_tax_estimate | Corporation Tax for one period (up to 12 months): small profits rate, main rate and marginal relief, with associated companies, short periods and periods straddling 1 April; returns tax, effective rate and dates |
| corporation_tax_deadlines | Payment date, CT600 filing deadline and Companies House accounts deadline for a private limited company |
| corporation_tax_late_penalty_and_interest | HMRC penalties and interest for filing a CT600 late (flat penalties and the running interest) |
| directors_loan_s455_tax | Section 455 tax and repayment relief on a director's loan, with an optional benefit-in-kind estimate |
| uk_company_capital_allowances | Capital allowances for a period: annual investment allowance, full expensing and the main pools |
| company_chargeable_gain_with_indexation | Chargeable gain or allowable loss on disposals of UK land or buildings (with indexation) or shares |
| uk_company_size_micro_small_check | Micro-entity, small or neither for a financial year under the Companies Act |
| long_accounting_period_split | Split accounts covering more than 12 months (up to 18) into the two CT600 accounting periods |
| uk_company_car_tax_bik | Company car benefit in kind for 2025/26 or 2026/27: appropriate percentage, car and fuel benefit |
| uk_company_van_benefit_tax | Company van benefit in kind, including the zero-emission case |
| uk_mileage_allowance | HMRC approved mileage amounts for an employee or director using their own vehicle |
| limited_company_home_office_allowance | Use of home as office: the flat weekly or monthly amount payable without evidence |
| uk_trivial_benefits_check | Whether a non-cash benefit of GBP 50 or less including VAT qualifies as a tax-free trivial benefit |
| uk_dividend_reserves_check | Whether estimated distributable profits cover a proposed dividend (reserves check) |
| director_salary_vs_dividends | The salary and dividend mix that leaves the director the most from the year's profit |
| sole_trader_vs_limited_company_tax | Tax on the same profit as a sole trader versus a limited company |
| limited_company_pension_contribution | Employer pension contributions versus salary, for the director's position |

## Business Relevance

- **UK limited companies and their advisors** can clear routine tax questions in the assistant that already holds the surrounding context, with reproducible calculations instead of spreadsheet re-entries
- **Deadline and penalty tools** make the compliance calendar answerable in one question: when is the CT600 and accounts due, and what does a late filing actually cost
- **Planning questions** (salary vs dividends, sole trader vs limited, pension vs salary, dividend reserves) become structured comparisons
- **Free and keyless:** no account, no API key, no per-call cost; the tools are the same calculators that power taxley.co.uk

## Integration with CorpusIQ

Tax planning needs two things: the rules and the numbers. CorpusIQ supplies the numbers - current profit, expenses, invoices - from the bookkeeping and banking sources a business connects, and Taxley supplies the rule-based calculations. The same assistant can pull both into one answer, for example an estimated CT liability on this year's bookkeeping figures.

## Limitations

- **UK only:** the tools model UK Corporation Tax and related UK calculations; other jurisdictions are not covered
- **Calculations, not advice:** outputs are computed from the vendor's implementation of published rules for general information and planning; they are not tax advice and do not replace an accountant or HMRC guidance
- **Planning needed for filing dates and elections:** check any output against current GOV.UK guidance before it is used for a filing or a payment decision
- **Free service:** the endpoint is free and keyless at capture time; availability and coverage are as the publisher states
- **File-upload calculators are excluded:** calculators that need a file upload are not available through MCP, the JSON API or embeds

## FAQ

### Does the MCP server need an API key or account?

No. The endpoint is keyless and free; an unauthenticated initialize returns the tool list.

### Which rates does the CT estimate apply?

The small profits rate, the main rate and marginal relief, including associated companies, short periods and periods that straddle 1 April; a close investment-holding company is treated at the main rate.

### Is this tax advice?

No. The tools are calculators based on the rules published on GOV.UK; use them for planning and sanity checks, and confirm filing positions against current guidance.

### What does it cost?

Nothing at capture time: the MCP server is free, with no key or account, and each answer links back to the worked result on taxley.co.uk.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [gofact MCP - Local French E-Invoicing with Legal Numbering](/hermes/mcp/servers/external/gofact-mcp/)
- [BoomTax MCP - Tax Filings in Your Assistant](/hermes/mcp/servers/external/boomtax-mcp/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
