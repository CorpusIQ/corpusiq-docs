---
title: Financial Close Blueprint for Hermes Agent  --  Monthly Reconciliation Automation
description: Monthly financial close automation blueprint for Hermes Agent. Data pull, account reconciliation, variance analysis, reporting, and forecasting  --  connected to QuickBooks, Stripe, banking data. Cron-driven with human sign-off gates.
category: blueprints
tags: [hermes-agent, blueprint, financial-close, reconciliation, accounting, quickbooks, stripe, monthly-reporting]
last_updated: 2026-06-16
---

# Financial Close Blueprint  --  Monthly Reconciliation Automation

## Close Timeline

```
DAY 1          DAY 2-3        DAY 4-5        DAY 6-7
─────          ───────        ───────        ──────
Data Pull      Reconcile      Reports        Review +
Begin Close    All Accounts   + Variance     Forecast
```

## Architecture Overview

```
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│Accounting│  │Payment   │  │ Banking  │  │  CRM /   │
│(QBO/Xero)│  │Processor │  │  Data    │  │ Billing  │
└────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │             │             │
     └─────────────┴──────┬──────┴─────────────┘
                          │
                ┌─────────▼─────────┐
                │ Close Engine      │
                │ - Data pull       │
                │ - Reconciliation  │
                │ - Variance check  │
                │ - Report gen      │
                └─────────┬─────────┘
                          │
                ┌─────────▼─────────┐
                │  Outputs          │
                │ - P&L, Balance    │
                │ - Variance report │
                │ - Forecast update │
                │ - Close package   │
                └───────────────────┘
```

## Day 1: Data Collection and Initial Close

### Morning: Trigger the Close

**Cron:** `0 6 1 * *`  --  6 AM on the 1st of each month.

The close automation begins by pulling data from all financial sources for the period that just ended.

### Step 1: Pull Accounting Data

From the accounting system (QuickBooks, Xero, etc.), extract:
1. **Trial Balance**  --  all accounts with ending balances for the period
2. **Profit & Loss**  --  revenue and expense categories with period totals and year-to-date
3. **Balance Sheet**  --  assets, liabilities, and equity as of period end
4. **Transaction Detail**  --  general ledger detail for key accounts flagged for review
5. **Accounts Receivable Aging**  --  outstanding invoices by age bucket
6. **Accounts Payable Aging**  --  unpaid bills by age bucket

### Step 2: Pull Payment Processor Data

From Stripe or other payment processors:
1. **Gross revenue** for the period (charges, net of refunds)
2. **Fees**  --  processing fees, dispute fees, platform fees
3. **Payouts**  --  what actually hit the bank, by date
4. **Disputes**  --  open and resolved chargebacks with amounts
5. **Refunds**  --  period refunds with reasons

### Step 3: Pull Banking Data

If bank feeds are available:
1. **Ending balances** for each bank account as of the last day of the period
2. **Outstanding checks or pending transactions** that haven't cleared
3. **Bank fees and interest** for the period

### Step 4: Pull Supplementary Data

From other systems:
- **CRM:** New customers added, churned customers, expansion/renewal revenue (for SaaS metrics)
- **Subscription management:** MRR, ARR, active subscriptions, plan breakdowns
- **Expense management:** Employee expenses awaiting reimbursement, corporate card transactions
- **Payroll:** Period payroll totals if available

### Step 5: Generate Close Checklist

The agent generates a personalized close checklist based on what data was successfully pulled and what needs attention:

```markdown
# Monthly Close Checklist  --  [MONTH YEAR]

## Data Status
| Source | Status | Notes |
|---|---|---|
| QuickBooks | ✅ Complete | All accounts pulled |
| Stripe | ✅ Complete | 3 pending disputes flagged |
| Bank (Primary) | ✅ Complete | |
| Bank (Savings) | ⚠️ Partial | Missing last 2 days of transactions |
| CRM | ✅ Complete | |

## Reconciliation Tasks
- [ ] Reconcile Stripe revenue vs QBO revenue (variance threshold: 1%)
- [ ] Reconcile bank balance vs QBO bank account balance
- [ ] Verify all invoices issued match period revenue
- [ ] Review uncategorized transactions (> $500)
- [ ] Confirm inter-company transfers net to zero
- [ ] Verify prepaid expense amortization
- [ ] Accrue expenses for received-not-invoiced items

## Review Items
- [ ] Any expense > [THRESHOLD] without proper documentation?
- [ ] Revenue recognition: any multi-period contracts misclassified?
- [ ] Fixed assets: any additions or disposals this month?
```

## Day 2-3: Reconciliation

### Automated Reconciliation

**Cron:** `0 7 2 * *`  --  Day 2 reconciliation run, with a follow-up on Day 3 if variances remain.

### Revenue Reconciliation

The most critical reconciliation: does payment processor revenue match accounting system revenue?

```
Stripe gross revenue (period):   $XXX,XXX.XX
QuickBooks revenue (period):     $XXX,XXX.XX
Variance:                        $X,XXX.XX  (X.XX%)

Variance sources:
- Timing differences (items recorded in different periods)
- Refund timing (processed vs recorded)
- Fee classification (gross vs net reporting)
- Failed/declined charges appearing in one system but not the other
```

**Automatic actions when variance > 1%:**
1. Flag the discrepancy with a detailed breakdown by day
2. Identify the specific transactions causing the variance
3. If the pattern matches a known issue (e.g., refund timing), note it
4. If the cause is unknown, escalate to the finance team with a suggested investigation plan

### Bank Reconciliation

Match the accounting system's bank balance to the actual bank balance:
1. Pull ending balance from bank statement
2. Pull balance per accounting system for the same account
3. List outstanding checks and deposits in transit
4. Compute adjusted balance: `Book Balance + Deposits in Transit - Outstanding Checks`
5. Compare to bank statement balance  --  should match within de minimis threshold

### Accounts Receivable Reconciliation

1. Pull AR aging from accounting system
2. Cross-reference with CRM/billing to identify which outstanding invoices are actually in dispute or likely uncollectible
3. Flag AR > 90 days for potential write-off
4. Generate AR health score: current AR / monthly revenue (should be stable or declining)

## Day 4-5: Reporting and Variance Analysis

**Cron:** `0 6 4 * *`  --  Day 4 report generation.

### Financial Package

Generate the monthly financial package:

**1. Executive Summary (1 page)**
- Revenue: actual vs budget, variance %, key drivers
- Gross margin: actual vs target, trend
- Operating income: actual vs budget
- Cash position: ending balance, burn rate, runway
- 2-3 key highlights and 1-2 concerns

**2. Profit & Loss with Variance Analysis**
```
| Category          | Actual  | Budget  | Variance | Var % | Commentary |
|---|---|---|---|---|---|
| Revenue           | $XXX    | $XXX    | $XX      | X.X%  | [Auto]     |
| COGS              | $XXX    | $XXX    | $XX      | X.X%  | [Auto]     |
| Gross Profit      | $XXX    | $XXX    | $XX      | X.X%  |            |
| Gross Margin %    | XX.X%   | XX.X%   | X.Xpp    |       |            |
| Operating Expenses|         |         |          |       |            |
| - Sales & Marketing| $XXX   | $XXX    | $XX      | X.X%  |            |
| - R&D              | $XXX   | $XXX    | $XX      | X.X%  |            |
| - G&A              | $XXX   | $XXX    | $XX      | X.X%  |            |
| Total OpEx        | $XXX    | $XXX    | $XX      | X.X%  |            |
| Operating Income  | $XXX    | $XXX    | $XX      | X.X%  |            |
```

**3. Balance Sheet**
- Assets, liabilities, equity with prior period comparison
- Key ratios: current ratio, quick ratio, debt-to-equity

**4. Cash Flow Summary**
- Operating, investing, and financing cash flows
- Net cash change and ending balance
- Burn rate and runway calculation (for startups)

### Automated Commentary

For line items with variance > 5% or > $[THRESHOLD], the agent generates commentary:
1. What changed (automated data comparison)
2. Possible drivers (based on transaction detail analysis)
3. Whether this is a one-time item or a trend (compare to prior months)
4. Recommended follow-up questions for the finance team

## Day 6-7: Review and Forecast

**Cron:** `0 8 6 * *`  --  Day 6 forecast update.

### Forecast Update

Based on the just-closed month and year-to-date results, update the rolling forecast:

1. **Revenue forecast:** Update based on actual YTD performance, pipeline data from CRM, and seasonality patterns
2. **Expense forecast:** Update based on actual run rate, known changes (hires, contract changes)
3. **Cash forecast:** Project ending cash for the next [3/6/12] months based on updated revenue and expense forecasts
4. **Scenario modeling:** Generate best-case, base-case, and worst-case scenarios with key assumptions

### Close Package Distribution

**Cron:** `0 9 7 * *`  --  Day 7 package distribution.

The completed close package is distributed:
1. Full package → finance team (email with PDF/Notion link)
2. Executive summary → leadership team (Slack message + 1-pager)
3. Department P&Ls → department heads (their actuals vs budget)
4. Investor update → if applicable, formatted for investor reporting
5. Board materials → if board meeting is within 30 days, flag topics for inclusion

### Close Retrospective

After distribution, the agent generates a process retrospective:
- What data was missing or late?
- Which reconciliations took the most manual effort?
- What variances were unexpected and needed investigation?
- Recommended process improvements for next month

## Full Cron Schedule

| Day | Time | Task | Cron |
|---|---|---|---|
| 1st | 06:00 | Trigger close  --  pull all data | `0 6 1 * *` |
| 2nd | 07:00 | Run automated reconciliations | `0 7 2 * *` |
| 3rd | 07:00 | Re-run reconciliations for unresolved items | `0 7 3 * *` |
| 4th | 06:00 | Generate financial package and variance analysis | `0 6 4 * *` |
| 5th | 08:00 | Human review of package (reminder) | `0 8 5 * *` |
| 6th | 08:00 | Update rolling forecast | `0 8 6 * *` |
| 7th | 09:00 | Distribute close package | `0 9 7 * *` |

### Mid-Month and Pre-Close

Don't wait for month-end to start the close process:

| Timing | Task | Cron |
|---|---|---|
| 15th | Mid-month estimate: project month-end results | `0 8 15 * *` |
| 25th | Pre-close prep: identify missing transactions, chase outstanding items | `0 8 25 * *` |
| Last day | Soft close: preliminary data pull to identify issues early | `0 18 L * *` |

## Implementation Notes

### Materiality Thresholds
Not every variance needs investigation. Configure materiality thresholds:
```yaml
materiality:
  revenue_variance_pct: 1.0     # Flag if revenue miss > 1%
  expense_line_min: 500          # Don't investigate < $500 variance
  bank_reconciliation_max: 0.01  # Must match to within 1 cent
  aging_alert_days: 90           # Flag AR items > 90 days
```

### Chart of Accounts Standardization
The automation relies on consistent account names and numbers. If your chart of accounts changes, update the automation mappings immediately. Run a check on Day 25 of each month: do all mapped accounts still exist?

### Audit Trail
Every automated journal entry suggestion, reconciliation adjustment, and report generation should be logged with:
- Timestamp
- Source data references
- Calculation methodology
- Human approval status

This is essential for audit readiness and debugging why a number changed between months.

### Extending
- Connect **spreadsheet-based budgets** so variance analysis compares to the official budget, not last month
- Add **multi-entity consolidation** for organizations with subsidiaries
- Integrate **tax compliance** checks  --  estimated tax payment adequacy, sales tax collection gaps
- Connect to **investor reporting templates** for automatic investor update generation

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
