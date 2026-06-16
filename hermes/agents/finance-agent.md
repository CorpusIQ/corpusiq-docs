# Finance Agent Configuration

## Role Description

The Finance Agent automates financial operations — invoice processing, expense tracking, account reconciliation, and financial reporting. It connects to your accounting platform, payment processor, banking data, and expense management tools to provide a real-time financial picture without manual data entry or spreadsheet wrangling. The agent answers questions like "what's our cash position this month?" or "show me all unpaid invoices over 30 days" and runs scheduled reconciliations and reports.

This agent is built for finance teams, fractional CFOs, and business owners who need accurate, timely financial data without living inside QuickBooks. It surfaces anomalies (duplicate invoices, unexpected fee spikes, reconciliation gaps), tracks AR aging, and prepares month-end close summaries. It does not replace your accountant — it makes their job faster and your financial visibility better.

## Recommended Model

**Claude Sonnet 4** or **DeepSeek V3** — financial analysis demands precision with numbers and the ability to spot patterns across accounts. Both models handle structured financial data reliably. For scheduled reporting and simple queries, **Claude Haiku** works well. Avoid models known to hallucinate numerical details for financial use cases.

## Key Skills to Load

- `invoice-processing` — Monitor new invoices, flag duplicates, categorize by GL code, track payment status
- `expense-tracking` — Categorize expenses, flag uncategorized items, detect policy violations
- `reconciliation` — Match Stripe payouts to bank deposits, identify unmatched transactions, flag gaps
- `ar-aging` — Accounts receivable aging report, overdue invoice alerts, customer payment trend analysis
- `financial-reporting` — Monthly P&L, balance sheet snapshot, cash flow summary, budget vs. actual
- `tax-prep` — Categorize transactions by tax category, estimate quarterly liabilities, flag missing vendor W-9s

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **QuickBooks** | Invoices, bills, P&L, balance sheet, chart of accounts, AR/AP aging |
| **Stripe** | Payment processing, payouts, disputes, balance transactions |
| **Odoo** | Alternative ERP for invoices, payments, journals, taxes |
| **Slack** | Financial alerts, approval requests, report distribution |
| **Email** | Invoice receipt monitoring, vendor communications |
| **Google Drive / OneDrive** | Receipt and statement storage, report archiving |
| **Airtable / Notion** | Budget tracking, expense policies, approval workflows |

## Sample Cron Schedule

```cron
# Daily reconciliation check at 8:00 AM
0 8 * * 1-5 hermes skill reconciliation --since yesterday

# Overdue invoice alert every weekday at 9:00 AM
0 9 * * 1-5 hermes skill ar-aging --overdue-only --format slack

# Expense categorization every 4 hours
0 9,13,17 * * 1-5 hermes skill expense-tracking --uncategorized --auto-categorize

# Weekly cash flow snapshot every Monday at 8:00 AM
0 8 * * 1 hermes skill financial-reporting --report cash-flow --period last_week

# Month-end close checklist on the 1st at 7:00 AM
0 7 1 * * hermes skill financial-reporting --month-end-close
```

## Quick-Start Command

```bash
hermes agent create finance \
  --model claude-sonnet-4 \
  --skills invoice-processing,expense-tracking,reconciliation,ar-aging,financial-reporting,tax-prep \
  --connectors quickbooks,stripe,slack,gmail,drive \
  --profile finance \
  --description "Financial operations and accounting automation agent"
```

## Daily Workflow

Every morning the agent checks Stripe payouts against bank deposits, flags any unmatched transactions, and posts a reconciliation summary. It monitors AR aging and alerts on invoices approaching or past due dates with customer context. Throughout the day it categorizes uncategorized expenses using historical patterns and GL mappings. On Mondays it delivers a cash flow snapshot. On the 1st of each month, it runs the month-end close checklist — reconciling all accounts, generating P&L and balance sheet reports, and flagging any anomalies for human review before close.

## Configuration Notes

Define your chart of accounts mapping and GL codes in canonical facts so the agent categorizes transactions correctly. Set your expense policy thresholds (auto-approve under $X, flag above $Y). Store your fiscal calendar. Configure which financial reports go to which stakeholders and channels. For tax prep, define your tax categories and jurisdiction rules.

## Extending

Add `budget-variance` that compares actuals against budget with narrative explanations for material variances. Integrate with Ramp, Brex, or Bill.com for corporate card and bill pay automation. Add `revenue-recognition` for SaaS companies that need to track deferred revenue. Build a `financial-forecast` skill using historical trends and pipeline data.
