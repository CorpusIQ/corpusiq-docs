# Financial Services: Portfolio Monitoring & Reconciliation

Financial services firms operate on data density: portfolios, transactions, market feeds, regulatory filings, and counterparty communications all flow simultaneously. Hermes Agent provides the connective tissue between these streams — monitoring, reconciling, and alerting without adding headcount.

## The Financial Automation Opportunity

Whether you're an RIA managing client portfolios, a fintech startup reconciling transactions, or an enterprise finance team closing the books, the pattern is the same: data arrives from multiple sources, must be validated against each other, and exceptions need immediate attention. Hermes Agent replaces the manual spreadsheet-reconciliation workflow with continuous automated monitoring.

## Portfolio Monitoring

Investment advisors and wealth managers can use Hermes to track client portfolios against targets, monitor for drift, and generate review-ready reports.

**Portfolio Drift Detection**

```yaml
- name: portfolio-drift-check
  schedule: "0 17 * * 1-5"  # Weekdays at 5 PM (after market close)
  skill: portfolio-drift-monitor
  description: Checks all portfolios against target allocations, flags drift > threshold
```

This skill connects to portfolio management systems via database connectors or API-based MCP integrations. For each portfolio, it:
1. Retrieves current holdings and market values
2. Calculates actual allocation percentages
3. Compares against target allocation bands
4. Flags any position exceeding drift thresholds
5. Generates rebalancing recommendations

The output lands in a compliance-ready format: which accounts need rebalancing, estimated tax impact of proposed trades, and a timestamped audit trail.

**Client Report Generation**

```yaml
- name: monthly-client-reports
  schedule: "0 6 1 * *"  # 1st of each month at 6 AM
  skill: client-portfolio-reports
  description: Generates monthly performance reports for all client households
```

Hermes pulls performance data, benchmarks, and allocation summaries, then compiles them into standardized report templates. Reports can be written to Google Drive folders organized by client, emailed directly, or posted to a client portal.

## Transaction Reconciliation

Reconciliation is the quintessential Hermes use case: matching records across systems that should agree but often don't.

**Daily Transaction Match**

```yaml
- name: daily-transaction-reconciliation
  schedule: "0 7 * * *"  # Daily at 7 AM
  skill: transaction-reconciliation
  description: Matches internal transaction ledger against bank/custodian feeds
```

The skill:
1. Queries the internal transaction database (via PostgreSQL/MSSQL connector)
2. Pulls custodian or bank transaction feeds (via API connectors or database queries)
3. Matches on transaction ID, amount, date, and counterparty
4. Produces three lists: matched, unmatched-internal, unmatched-external
5. For unmatched items, searches across date windows for near-matches (amount matches but date differs by 1-3 days)

Unmatched items route to an exceptions Slack channel with direct links to investigate.

**Cash Reconciliation**

```yaml
- name: cash-position-reconciliation
  schedule: "0 8,16 * * *"  # Twice daily
  skill: cash-reconciliation
  description: Reconciles cash balances across all custodial accounts
```

## Fraud Detection Alerts

Hermes can serve as a first-line fraud detection layer by monitoring for anomalous patterns:

```yaml
- name: fraud-pattern-scan
  schedule: "0 */3 * * *"  # Every 3 hours
  skill: fraud-detection
  description: Scans recent transactions for fraud indicators
```

Detection rules include:
- Unusual transaction velocity (same account, rapid succession)
- Off-hours transactions outside historical patterns
- New counterparty with high-value transfer
- Geographic anomalies (transactions originating from unexpected locations)
- Amount patterns just below reporting thresholds

When a rule triggers, Hermes creates a detailed case packet: the suspicious transaction, surrounding transaction history, counterparty information, and risk score. This routes to the compliance team's ticketing system with appropriate priority.

## Regulatory Filing Automation

Financial firms face filing obligations with FINRA, SEC, CFTC, and other regulators. Many filings are recurring with standard formats.

```yaml
- name: regulatory-filing-prep
  schedule: "0 5 * * 1"  # Weekly Monday at 5 AM
  skill: regulatory-filing-prep
  description: Gathers and formats data for upcoming regulatory filings
```

The skill maintains a filing calendar, and when a filing deadline approaches:
1. Queries the required data sources for the reporting period
2. Validates data completeness and format requirements
3. Generates draft filing in the required template
4. Routes for human review with a checklist of what's new since last period

## Market Data Integration

Hermes can pull market data from financial data providers through API connectors:

```yaml
- name: market-data-ingest
  schedule: "0 18 * * 1-5"  # Weekdays after close
  skill: market-data-sync
  description: Pulls end-of-day pricing and updates portfolio valuations
```

## Getting Started in Financial Services

1. **Start with reconciliation.** It's the highest-ROI, lowest-risk automation. Pick one account type and one custodian.
2. **Build exception handling first.** Don't try to automate every case — automate the 90% that match and route the 10% exceptions to humans with full context.
3. **Use database connectors for internal systems.** Most financial systems expose SQL access, making Hermes's PostgreSQL and MSSQL connectors immediately useful.
4. **Layer detection rules incrementally.** Start with 3-5 fraud detection rules, monitor false-positive rates for two weeks, then expand.
5. **Maintain the human-in-the-loop for regulatory filings.** Hermes prepares; humans review and submit.

The outcome: a single operations analyst can manage reconciliation and monitoring that previously required a team, while exceptions get surfaced in minutes instead of discovered at month-end.
