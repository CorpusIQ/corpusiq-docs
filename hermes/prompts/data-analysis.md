---
title: Data Analysis Prompts for Hermes Agent — SQL, Reporting & Visualization
description: Hermes Agent data analysis prompts for SQL query generation, reporting, visualization guidance, and metric computation. Prompt templates with placeholders for your database schema, analytics tools, and business questions.
category: prompts
tags: [hermes-agent, prompts, data-analysis, sql, reporting, visualization, metrics, business-intelligence]
last_updated: 2026-06-16
---

# Data Analysis Prompts — SQL, Reporting & Visualization

---

## Exploratory Data Analysis

### First-Look Analysis

```
You are a data analyst. I'm sharing a dataset with [N] rows and [M] columns from [SOURCE SYSTEM].

Schema:
[PASTE COLUMN NAMES AND TYPES]

Answer these discovery questions:
1. What are the top 5 most frequent values in [COLUMN]?
2. What time range does [DATE COLUMN] span?
3. Which columns have the most missing/null values?
4. Are there any obvious outliers in [NUMERIC COLUMNS]?
5. What correlations exist between [COLUMN A] and [COLUMN B]?

Summarize in plain English what the data represents and flag any data quality concerns.
Provide code (Python/Pandas or SQL) for each answer so I can reproduce results.
```

### Segmentation Analysis

```
Segment my [CUSTOMERS/USERS/TRANSACTIONS] data by [DIMENSION].

Data context:
- [ENTITY] table with [KEY COLUMNS]
- Time period: [START] to [END]
- Metrics of interest: [LIST — e.g., revenue, frequency, retention]

For each segment, compute:
- Segment size and percentage of total
- Average [METRIC 1], [METRIC 2], [METRIC 3]
- Month-over-month growth rate
- Top 3 distinguishing characteristics

Identify the highest-value segment and the fastest-growing segment. Provide the SQL or Python needed to reproduce.
```

---

## SQL Generation

### Query from Plain English

```
Convert the following business question into a SQL query for [DATABASE TYPE — PostgreSQL/BigQuery/Snowflake/MySQL].

Question: [PLAIN ENGLISH QUESTION]

Available tables:
[TABLE NAME 1]: [COLUMNS WITH TYPES]
[TABLE NAME 2]: [COLUMNS WITH TYPES]
[JOIN RELATIONSHIPS BETWEEN TABLES]

Requirements:
- Use explicit JOIN syntax, not implicit joins
- Include comments explaining each CTE or subquery
- Handle NULL values appropriately
- Add query optimization notes if the query would scan large tables
- Format output as [DESIRED FORMAT — daily time series, top-N ranking, summary statistics]

Expected output columns: [DESCRIBE EACH]
```

### Query Optimization

```
Analyze and optimize this slow query:

[PASTE SLOW QUERY]

Execution context:
- Database: [TYPE AND VERSION]
- Table sizes: [TABLE 1: X rows, TABLE 2: Y rows]
- Current execution time: [DURATION]
- Target: [DURATION]
- Available indexes: [LIST EXISTING INDEXES]

Identify the bottleneck (full table scan, nested loop join, sort, etc.).
Provide the optimized query and explain what changed and why it's faster.
Suggest any new indexes (with CREATE INDEX statements) that would help.
```

---

## Reporting and Dashboards

### Automated Report Template

```
Design a [WEEKLY/MONTHLY/QUARTERLY] report for [STAKEHOLDER ROLE].

Metrics to include:
1. [METRIC 1] — [DEFINITION, TARGET, PREVIOUS PERIOD VALUE]
2. [METRIC 2] — [DEFINITION, TARGET, PREVIOUS PERIOD VALUE]
3. [ETC.]

For each metric provide:
- Current value and period-over-period change (%)
- The SQL query or data source it comes from
- A plain-language interpretation (what changed and why it matters)
- A red/yellow/green status indicator with threshold definitions

Include an executive summary section (max 200 words) synthesizing the key takeaways.
```

### Chart and Visualization Guidance

```
I need to visualize [DATA RELATIONSHIP — e.g., "revenue by channel over 12 months"].

Data characteristics:
- [N] categories
- [TIME GRANULARITY] time dimension
- [CONTINUOUS/DISCRETE] values
- Comparison: [ABSOLUTE VALUES / PERCENT CHANGE / VS TARGET]

Recommend:
1. The best chart type with justification (bar, line, area, scatter, heatmap, etc.)
2. Color scheme considerations (accessibility, brand alignment)
3. Labeling strategy (axis titles, data labels, annotations)
4. What the viewer should notice first — design for the "3-second test"

Provide the code to generate this in [PLOTLY/MATPLOTLIB/VEGA-LITE/EXCEL].
```

---

## Metric Extraction

### KPI Definition and Calculation

```
Define and calculate [METRIC NAME] for [BUSINESS CONTEXT].

Provide:
1. Plain-English definition that a non-technical stakeholder would understand
2. Mathematical formula with clear numerator and denominator
3. SQL query (or Python) that computes it from [TABLE NAMES]
4. Common pitfalls in calculation (e.g., double-counting, time window edge cases)
5. How often it should be recalculated and what refresh latency is acceptable
6. Related metrics to track alongside it for context

Benchmark: what's a "good" value for a company of our [SIZE/STAGE/INDUSTRY]?
```

### Anomaly Detection

```
Analyze this time series data for anomalies:

[PASTE DATA OR DESCRIBE SOURCE]
Metric: [METRIC NAME]
Granularity: [HOURLY/DAILY/WEEKLY]
Expected pattern: [SEASONALITY, TREND, KNOWN EVENTS]

Use [METHOD — z-score/IQR/moving average/STL decomposition] to detect anomalies.
For each anomaly found:
- Date/time and observed vs expected value
- Magnitude (how many standard deviations from baseline)
- Possible explanation based on known events in that period
- Recommended action (investigate further, ignore as noise, escalate)

Provide code to run this detection on an ongoing schedule.
```


---
*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
