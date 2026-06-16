# Revenue Operations: Pipeline, Forecasting & Reconciliation

Revenue operations (RevOps) sits at the intersection of sales, marketing, finance, and customer success. The RevOps mandate is to make the revenue engine predictable, measurable, and scalable — but the data needed to do that lives in separate systems that rarely agree. Hermes Agent automates the cross-system reconciliation, reporting, and alerting that turns fragmented data into operational intelligence.

## The RevOps Data Problem

A typical revenue stack includes: CRM (HubSpot, Salesforce, Close), marketing automation (Klaviyo, Mailchimp, ActiveCampaign), billing (Stripe, QuickBooks, Chargebee), analytics (GA4, PostHog), and spreadsheets (the unofficial system of record). Each system has its own definition of "customer," "revenue," and "pipeline." Reconciling them manually means exporting CSVs and VLOOKUP-ing until your eyes cross.

Hermes automates that reconciliation and makes it continuous rather than month-end.

## Pipeline Management & Hygiene

CRM pipelines degrade. Deals sit in stages too long, close dates drift without updates, and stale opportunities inflate forecasts. Hermes can enforce pipeline discipline automatically.

**Pipeline Hygiene Monitor**

```yaml
- name: pipeline-hygiene
  schedule: "0 7 * * 1-5"  # Weekdays at 7 AM
  skill: pipeline-cleanup
  description: Identifies stale deals, missing fields, and pipeline inconsistencies
```

The skill queries the CRM (HubSpot, Close CRM, LeadConnector) and flags:
- Deals with no activity in 14+ days
- Deals past their close date that haven't been updated
- Deals missing required fields (amount, close date, contact association)
- Deals in late stages with no associated contacts or activities
- Deals with amounts that don't match line items or products

Each flag includes a severity score and a suggested action. The output routes to the sales manager's Slack with direct links to each problematic deal.

**Stage Progression Monitoring**

```yaml
- name: deal-velocity-monitor
  schedule: "0 8,16 * * *"  # Twice daily
  skill: deal-velocity
  description: Tracks deals stuck in stages beyond expected duration
```

The skill maintains expected stage durations (configurable by deal size and type). When a deal exceeds the expected time in a stage, it alerts the rep and manager. Over time, the skill builds actual velocity data that feeds more accurate forecasting.

## Forecasting Automation

Sales forecasting typically involves each rep submitting a commit, which the manager adjusts, which then rolls up through layers of spreadsheet math. Hermes can build data-driven forecasts that complement human judgment.

**Weekly Forecast Compilation**

```yaml
- name: weekly-forecast
  schedule: "0 7 * * 5"  # Friday at 7 AM
  skill: forecast-compiler
  description: Compiles weighted pipeline into forecast categories
```

The skill:
1. Pulls all open pipeline from the CRM
2. Applies stage-based probability weights (customizable by deal type and historical conversion data)
3. Categorizes into commit, best-case, and upside buckets
4. Compares against quota and prior period performance
5. Highlights deals that would make the difference between forecast categories
6. Produces a forecast summary with confidence ranges

**Forecast Accuracy Tracking**

```yaml
- name: forecast-accuracy
  schedule: "0 8 1 * *"  # 1st of each month at 8 AM
  skill: forecast-retrospective
  description: Compares prior month forecasts to actual results
```

This retrospective compares what was forecasted (at weekly intervals) against what actually closed, calculating forecast accuracy by rep, by team, and by deal stage. It identifies systematic biases (who consistently over-forecasts, which deal stages are least predictive) so managers can calibrate.

## Commission Calculation

Commission calculations are error-prone, time-consuming, and the fastest way to damage rep trust. Hermes can automate the calculation while maintaining the transparency reps need.

**Commission Engine**

```yaml
- name: commission-calculator
  schedule: "0 6 1 * *"  # 1st of each month at 6 AM
  skill: commission-calc
  description: Calculates commissions from closed-won deals with plan rules applied
```

The skill:
1. Queries the CRM for deals closed in the period
2. Applies commission plan rules: base rate, accelerators, splits, clawbacks
3. Factors in draws and guarantees
4. Handles multi-rep splits and overlay commissions
5. Produces a per-rep statement showing each deal, the rate applied, and the resulting commission
6. Generates a summary for payroll with audit trail

```yaml
- name: commission-discrepancy-check
  schedule: "0 9 2 * *"  # 2nd of each month at 9 AM
  skill: commission-audit
  description: Cross-checks commission calculations for anomalies
```

The audit skill looks for: deals missing from commission calculation, unusual rate applications, reps below minimum with closed revenue, and significant month-over-month changes in any rep's payout.

## Revenue Reconciliation

Different systems report different revenue numbers, and they should agree (or at least be reconcilable). Hermes can continuously validate these numbers against each other.

**Cross-Source Revenue Reconciliation**

```yaml
- name: revenue-reconciliation
  schedule: "0 7 * * *"  # Daily at 7 AM
  skill: revenue-reconcile
  description: Compares revenue figures across CRM, billing, and accounting systems
```

The skill:
1. Pulls closed-won revenue from the CRM for the period
2. Pulls recognized revenue from the billing system (Stripe, QuickBooks, Chargebee)
3. Pulls invoiced amounts from the accounting system
4. Identifies gaps: CRM deals with no corresponding invoice, invoices with no matching CRM deal, amounts that differ between systems
5. Produces a reconciliation report with specific items to investigate

**MRR/ARR Waterfall**

```yaml
- name: mrr-waterfall
  schedule: "0 7 1 * *"  # Monthly on the 1st
  skill: revenue-waterfall
  description: Builds MRR waterfall showing new, expansion, contraction, and churn
```

This skill builds the standard SaaS revenue waterfall: starting MRR + new business + expansion - contraction - churn = ending MRR. Each component is sourced from the billing system with CRM enrichment for segmentation (by plan, by cohort, by sales rep).

## Marketing-to-Sales Handoff

The gap between marketing qualified leads and sales accepted opportunities is where pipeline leaks.

```yaml
- name: marketing-sales-alignment
  schedule: "0 8 * * 1"  # Monday at 8 AM
  skill: mql-to-sql-tracking
  description: Tracks MQL to SQL conversion and identifies leakage points
```

The skill tracks leads from marketing systems (Klaviyo, Mailchimp, HubSpot forms) through to CRM opportunities, measuring conversion rates at each stage and flagging: MQLs that weren't contacted, leads that were disqualified without clear reason, and conversion rate changes that warrant investigation.

## Getting Started in RevOps

1. **Start with pipeline hygiene.** Clean data makes every other automation better. Pipeline cleanup provides immediate value and builds trust.
2. **Connect your CRM and billing system first.** These are the two poles of the revenue equation — everything else sits between them.
3. **Reconcile before forecasting.** If your systems don't agree on what revenue is, forecasts based on any one system are unreliable.
4. **Build commission calculations with extreme transparency.** Every rep should be able to see exactly how their number was calculated, with a clear dispute path.
5. **Use database connectors for custom metrics.** Most revenue teams have custom SQL queries they run regularly. Turn those into Hermes skills that run on schedule.

The outcome: cleaner pipeline data, more accurate forecasts, faster commission cycles, and a single source of truth for revenue numbers that finance, sales, and leadership all trust.
