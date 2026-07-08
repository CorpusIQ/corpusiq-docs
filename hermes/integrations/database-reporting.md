---
title: Database + Reporting Integration for Hermes Agent  --  Automated Queries & Dashboards
description: Connect databases (PostgreSQL, MySQL, SQL Server, MongoDB) to Hermes Agent for automated reporting. Scheduled queries, dashboard generation, anomaly detection, and report distribution with MCP setup and cron patterns.
category: integrations
tags: [hermes-agent, integration, database, reporting, postgresql, mysql, mongodb, dashboards, anomaly-detection, cron]
last_updated: 2026-07-08
---

# Database + Reporting Integration  --  Automated Queries & Dashboards

## Architecture Overview

```
┌──────────┐     ┌──────────────┐     ┌───────────┐
│ Database │────▶│ Query Engine │────▶│ Reporting │
│ (SQL,    │     │ + Scheduler  │     │ (Notion,  │
│  NoSQL)  │     │              │     │ Sheets,   │
└──────────┘     └──────┬───────┘     │ Slack)    │
                        │             └───────────┘
                  ┌─────▼──────┐
                  │  Results   │
                  │  Cache +   │
                  │  Diffing   │
                  └────────────┘
```

The query engine executes parameterized SQL against production databases (or read replicas). Results are cached, diffed against previous runs to detect anomalies, and distributed to the configured reporting destinations.

## MCP Server Setup

### Database Servers

**PostgreSQL MCP Server**  --  provides `query_database`, `list_database_tables`, and `describe_table`. Configure with connection string containing host, port, database name, user, and password. **Critical: use a read-only database user.** Production write access from automation is a significant risk.

**MSSQL MCP Server**  --  provides `configure_mssql_connection`, `query_mssql_database`, and `list_mssql_tables`. Supports SQL Server authentication and Azure AD. Configure with encrypted connections enabled.

**MongoDB MCP Server**  --  provides aggregation pipeline execution for document-based data stores. Use for operational metrics stored in document collections.

**Cosmos DB MCP Server**  --  provides `configure_cosmos_connection`, `query_cosmos_database`, and `list_cosmos_containers`. Supports both key-based and Azure RBAC authentication.

### Security Configuration

```yaml
database_config:
  host: "read-replica.internal.example.com"
  port: 5432
  database: "analytics"
  user: "hermes_agent_readonly"
  ssl_mode: "require"
  statement_timeout: 30000  # 30-second query timeout
  max_rows: 10000           # Prevent accidental full-table scans
```

Always use read replicas for reporting queries. Production database load from reporting automation can cause outages. Most cloud providers (RDS, Cloud SQL, Azure DB) support read replicas with minimal configuration.

## Core Automation Scenarios

### 1. Scheduled Query Execution

**Goal:** Run business-critical queries on a schedule and distribute results.

**Query Registry Pattern:**
Define queries in a version-controlled directory with metadata:

```yaml
# queries/daily_revenue.yaml
name: "Daily Revenue Summary"
sql: |
  SELECT 
    date_trunc('day', created_at) as day,
    sum(amount) as revenue,
    count(*) as transactions,
    sum(amount) / count(*) as avg_order_value
  FROM orders
  WHERE created_at >= current_date - interval '7 days'
  GROUP BY 1
  ORDER BY 1 DESC
schedule: "0 7 * * *"
destinations:
  - type: slack
    channel: "#finance-daily"
  - type: google_sheets
    spreadsheet_id: "1ABC..."
    range: "Revenue!A1"
anomaly_detection:
  enabled: true
  metric: revenue
  method: z_score
  threshold: 2.5
```

**Workflow:**
1. Agent reads query registry at scheduled times
2. Executes each query against the database using MCP tools
3. Caches results locally for comparison
4. Diffs against previous run: are any metrics anomalous?
5. Formats results for each configured destination
6. Sends to Slack, writes to Google Sheets, updates Notion database

### 2. Automated Dashboard Updates

**Goal:** Keep reporting dashboards current without manual data refreshes.

**Workflow:**
1. Define dashboard queries with destination mappings
2. On schedule, execute all queries for a given dashboard
3. Format results into the destination's expected schema
4. Write to Google Sheets (via `read_sheet`/write operations), Notion databases (via Notion API), or Airtable
5. Log update timestamps  --  if an update fails, flag it for investigation

**Google Sheets Integration:**
```
1. list_drive_files to find the target spreadsheet
2. read_sheet to verify current structure
3. execute database query via MCP
4. format results as 2D array matching sheet layout
5. write to sheet using appropriate API
```

**Notion Integration:**
```
1. notion_search to find the database page
2. notion_get_database to read the schema
3. execute database query
4. map database columns to Notion properties
5. update or create pages in the Notion database
```

**Cron expression:** `0 8 * * *` for daily dashboards; `0 8 * * 1` for weekly rollups.

### 3. Anomaly Detection

**Goal:** Automatically detect unusual patterns in business metrics and alert the right team.

**Detection Methods:**

| Method | Best For | Threshold |
|---|---|---|
| Z-Score | Normally distributed metrics (revenue, user signups) | > 2.5 standard deviations |
| IQR | Metrics with outliers (support tickets, error rates) | > 1.5 × IQR beyond Q1/Q3 |
| Percent Change | Stable trend metrics (subscriber count, inventory) | > 20% day-over-day |
| Moving Average | Seasonal metrics (ecommerce sales, ad spend) | > 3 × rolling std dev |

**Workflow:**
1. After each scheduled query execution, compare current values to historical baseline
2. If any metric exceeds its threshold, generate an anomaly alert
3. Alert includes: metric name, current value, expected range, magnitude of deviation, possible explanations
4. Route by severity: minor anomalies → Slack channel; major anomalies → PagerDuty/on-call escalation
5. Log all anomalies (including dismissed ones) for false-positive tracking

**False Positive Management:**
Track which alerts were actionable vs dismissed. After 4 weeks, adjust thresholds:
- If > 30% of alerts for a metric are dismissed, increase the threshold
- If a real incident wasn't detected, decrease the threshold

### 4. Data Quality Monitoring

**Goal:** Proactively detect data pipeline issues before they corrupt reports.

**Quality Checks:**
```sql
-- Row count anomaly: did yesterday's ETL fail?
SELECT count(*) FROM orders WHERE created_at::date = current_date - 1;

-- Null ratio: is a critical field going missing?
SELECT 
  count(*) as total,
  count(email) as with_email,
  round(100.0 * count(email) / count(*), 2) as email_fill_rate
FROM users WHERE created_at > current_date - interval '7 days';

-- Freshness check: when was the last record written?
SELECT max(updated_at) as last_write FROM orders;

-- Referential integrity: orphaned records?
SELECT count(*) FROM order_items oi
LEFT JOIN orders o ON oi.order_id = o.id
WHERE o.id IS NULL;
```

**Workflow:**
1. Run quality queries before business-critical reporting queries
2. If any check fails, halt dependent report generation and alert the data engineering team
3. Record quality metrics over time to identify degrading data sources
4. Build a quality score per data source (0-100) based on completeness, freshness, and accuracy

**Cron expression:** `0 5 * * *`  --  runs before the main reporting window.

## Cron Schedule Summary

| Task | Cron | Rationale |
|---|---|---|
| Daily metrics queries | `0 7 * * *` | Before team standups |
| Dashboard refresh | `0 8 * * *` | Start of business day |
| Data quality checks | `0 5 * * *` | Before reporting queries run |
| Weekly rollups | `0 8 * * 1` | Monday morning |
| Anomaly detection | Triggered by query execution | Immediately after each query |
| Query performance audit | `0 2 * * 0` | Sunday, low database load |

## Implementation Notes

### Query Performance
- Every scheduled query should have an `EXPLAIN` plan reviewed before production use
- Set `statement_timeout` at the connection level (30 seconds default)
- Monitor query execution time over time  --  queries that slow down indicate missing indexes or growing data
- Use materialized views for complex reporting queries that don't need real-time data

### Idempotency
Design queries and destination writes to be idempotent  --  running the same report twice should produce the same result, not duplicate data. Use upsert patterns when writing to destinations.

### Failure Handling
- If a query fails (timeout, connection error): retry once after 5 minutes, then alert
- If a destination write fails: buffer results and retry; escalate if unresolved after 1 hour
- Never silently drop report failures  --  missing data is worse than late data

### Extending
- Add Slack slash commands so team members can trigger reports on-demand
- Connect email to deliver PDF report exports to stakeholders who prefer that format
- Integrate with BI tools (Metabase, Looker, Tableau) by refreshing their underlying datasets

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
