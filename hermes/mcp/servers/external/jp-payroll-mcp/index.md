---
title: jp-payroll-mcp - Japanese Payroll and Social Insurance
description: Japanese payroll, social insurance and labour-law MCP server that computes answers from published government tables instead of looking them up. 29 tools over a free HTTP API, with the statute or ministerial notice cited for every figure. Ideal for HR operators, payroll service providers and accounting agents handling Japanese employment."
category: Business Operations
stars: 1
added: 2026-09-02
source: "mcp.so GitHub issue #3906"
relevance: ★★★
tags: [payroll, japan, social-insurance, hr, labour-law, compliance]
---

# jp-payroll-mcp - Japanese Payroll and Social Insurance for Agents

**Stdio MCP server (npm) plus a free HTTP API** - computes Japanese payroll, social insurance and labour-law answers from published government tables, verified cell by cell with 4,661 assertions on every data change. Every answer cites the statute or ministerial notice it rests on.

## Spec Block

| Field | Value |
|---|---|
| Server name | jp-payroll-mcp |
| Repo | github.com/kishida-devil/jp-payroll-mcp |
| npm | jp-payroll-mcp v0.4.3 |
| Transport | stdio (npx) plus HTTP API |
| HTTP API | https://japan-payroll-api.tsumugi.workers.dev (44 endpoints, OpenAPI 3.0) |
| Auth | none for MCP use; paid bulk plan on RapidAPI |
| License | MIT |
| Stars | 1 |

## Why This Matters for Operators

Payroll arithmetic in Japan is full of traps that look-plausible wrong answers fall into: retiring on March 30 instead of March 31 moves a full month of social insurance premiums; someone born April 1 turns 40 on March 31 and starts paying long-term-care insurance a month early; the "two grades or more" rule for mid-year remuneration revision is not in the Health Insurance Act but in a 1961 ministerial notice. This server answers from the published rate tables and cites the legal basis, so an AI assistant can produce payroll figures an auditor will accept.

## Tools & Capabilities (29 tools)

| Group | Tools |
|---|---|
| Payslip & tax | calculate_payslip, calculate_withholding_tax, calculate_year_end_adjustment, calculate_bonus, calculate_annual_cost, calculate_overtime_pay, calculate_payroll_batch |
| Insurance & remuneration | get_insurance_rates, check_insurance_eligibility, lookup_standard_remuneration, decide_regular_remuneration, decide_regular_remuneration_batch, check_leave_exemption, national_insurance, list_workers_compensation_rates |
| Revision & leave judgements | judge_monthly_revision, judge_leave_end_revision, judge_annual_average, judge_annual_leave, judge_worker_type, get_age_milestones |
| Reference data | get_minimum_wage, business_days, consumption_tax, get_statute_text, check_data_freshness |
| Validation | validate_corporate_number, validate_invoice_numbers_batch, commuting_allowance_exemption |

## Installation

```bash
claude mcp add jp-payroll -- npx -y jp-payroll-mcp
```

The server is a thin layer over the HTTP API, so both paths return identical answers. For software integration, the API exposes 44 endpoints (prefecture lists, insurance rates, standard-remuneration table, minimum-wage history, payroll computation, holidays and business-day arithmetic, consumption-tax history, corporate and invoice-number validation).

## Configuration

No API key for MCP use. Bulk processing at scale goes through the paid RapidAPI plan (rapidapi.com/kishidadevil/api/japan-payroll-and-labor-constants). Data freshness is verifiable through check_data_freshness.

## Business Relevance

Useful for: HR operations with Japanese entities or contractors, payroll bureaus and accounting firms computing Japanese social insurance, e-commerce or services companies hiring in Japan, and any agent workflow that needs minimum wage, withholding tax, or leave-accrual figures with legal citations. The free tier covers conversational and workflow use.

## Integration with CorpusIQ

Pairs naturally with CorpusIQ's QuickBooks and finance connectors: computed Japanese payroll figures can be cross-checked against booked payroll expenses, and corporate-number validation complements supplier onboarding checks for Japanese counterparties.

## Limitations

Japan-only coverage. Numbers reflect published government tables as of the packaged version; verify check_data_freshness for live data age. Not a substitute for a certified social insurance labour consultant (sharoushi) on contested cases.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Worklittle Jobs MCP - Job Search and Market Data for AI Agents](/docs/hermes/mcp/servers/external/worklittle-jobs)
- [QuickBooks MCP - Business Accounting Data for Agents](/docs/hermes/mcp/servers/external/quickbooks-mcp)
