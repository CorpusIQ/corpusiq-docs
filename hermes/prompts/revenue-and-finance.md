# Revenue and finance prompts

Money questions. Powered mostly by **QuickBooks**, with assists from
**Shopify**, ecommerce ad accounts, and **Email** for context.

---

### "What's my cash position right now?"

**What this does:** Reads your balance sheet, current AR, AP, and recent
movement to give a live cash snapshot.
**Connectors used:** QuickBooks.
**Behind the scenes:** Direct QuickBooks balance sheet + payments query.
**Sample answer shape:** Cash on hand, AR, AP, net working capital, and a
short note on what's changed in the last 30 days.

---

### "What's blocking our cash flow?"

**What this does:** Identifies overdue invoices, ranks by amount and days
overdue, suggests collection priority. Cross-references email threads with
each customer to see who's been chased and who hasn't.
**Connectors used:** QuickBooks, Email (Gmail/Outlook), Drive (for
contracts).
**Behind the scenes:** `cash-recovery-engine` skill.
**Sample answer shape:** A ranked list of overdue invoices with customer,
amount, days overdue, last-touch date, and a recommended next action per
line.

---

### "Show me overdue invoices."

**What this does:** Raw list of unpaid invoices past their due date,
sorted by days overdue.
**Connectors used:** QuickBooks.
**Behind the scenes:** Direct `get_quickbooks_overdue_invoices` call.
**Sample answer shape:** Table of customer, invoice #, amount, due date,
days overdue.

---

### "Give me the P&L for last month."

**What this does:** Pulls the Profit & Loss report from QuickBooks for the
prior month.
**Connectors used:** QuickBooks.
**Behind the scenes:** `get_quickbooks_profit_loss`.
**Sample answer shape:** Standard P&L  --  revenue lines, COGS, gross
profit, operating expenses, net income.

---

### "How's our AR aging?"

**What this does:** Accounts receivable aging report  --  current, 30, 60,
90+ buckets.
**Connectors used:** QuickBooks.
**Behind the scenes:** `get_quickbooks_ar_aging`.
**Sample answer shape:** Aging buckets with customer totals in each.

---

### "How's our AP aging? Anything urgent to pay?"

**What this does:** Accounts payable aging  --  bills coming due and
overdue.
**Connectors used:** QuickBooks.
**Behind the scenes:** `get_quickbooks_ap_aging`.
**Sample answer shape:** Aging buckets, with vendors listed and urgency
flagged.

---

### "Which customers owe us the most?"

**What this does:** Ranks customers by open balance.
**Connectors used:** QuickBooks.
**Behind the scenes:** AR aging + customer lookup.
**Sample answer shape:** Top N customers by outstanding balance with
oldest invoice age.

---

### "Run a full financial health check."

**What this does:** Comprehensive financial review  --  operating report,
cash flow stress test, customer concentration risk, late payment patterns,
expense anomalies, tax/revenue forecasts.
**Connectors used:** QuickBooks, Shopify, Email, Drive.
**Behind the scenes:** `financial-command-center` skill.
**Sample answer shape:** Multi-section finance brief covering cash,
concentration risk, expense anomalies, and forecasts.

---

### "Are any expenses unusual this month?"

**What this does:** Scans recent bills and expenses for anomalies vs
historical baseline.
**Connectors used:** QuickBooks.
**Behind the scenes:** `financial-command-center` (expense anomaly
sub-task).
**Sample answer shape:** Flagged line items with the expected range and
what was actually charged.

---

### "What's our revenue trend over the last 6 months?"

**What this does:** Month-over-month revenue chart described in text.
**Connectors used:** QuickBooks and/or Shopify.
**Behind the scenes:** P&L pulled across the window.
**Sample answer shape:** Monthly revenue figures with trend
characterization.

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts)  --  production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts)  --  production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
