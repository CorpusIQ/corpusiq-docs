---
title: "NYSgpt Data Library MCP - SQL Over Public Records"
description: "A keyless MCP server that runs Athena SQL over United States public-record corpora, with the row counts, the refusals and two defects measured rather."

category: "Data / Public Records"
stars: "0 (remote Streamable HTTP, keyless to a daily limit; four tools, all four driven)"
added: 2026-11-16
source: "the mcp.so submission queue entry #7487 filed 2026-11-17T01:13:45Z, and a driven session on 2026-11-17 in which all four tools were called over Streamable HTTP, nine tools/call requests in total"
relevance: ★★★
tags: [sql, athena, public-records, patents, open-data, keyless, remote, mcp]
last_updated: "2026-11-19"
---

# NYSgpt Data Library

**A question about federal spending, patents or scholarly output is a question about a table nobody's model has read.** The records exist, they are public, and they are far too large to be in a prompt: USAspending, PatentsView, OpenAlex, SEC filings, LEHD jobs, EPA emissions, FERC sales, Medicare payments. The useful shape for an assistant is not a document to read. It is a SQL endpoint with the tables already loaded and a schema it can inspect before it writes a statement.

NYSgpt Data Library is that endpoint, and it is **keyless**: `list_databases`, `list_tables`, `describe_table` and a read-only `query` in the Athena (Trino) dialect, free without a key up to a daily limit. This pass called all **four** tools through **nine** requests and measured what a caller can actually rely on: **36** databases, a patents database of **128** tables holding **3,055,846,513** rows, a query that returned in **1,400** bytes scanned, a clean refusal of a write statement, and two defects worth knowing before an agent is pointed at it.

```
Server type:   remote Streamable HTTP
Endpoint:      https://data.nysgpt.com/mcp
Server:        nysgpt-data-library, version 2.0
Protocol:      2025-06-18
Auth:          none for the free tier (30 queries a day per the submission; paid keys as X-Api-Key)
Tools:         4 (list_databases, list_tables, describe_table, query)
Website:       https://nysgpt.com/data
Listed on:     the mcp.so submission queue as #7487
Registry:      com.nysgpt/data-library 2.0.0
```

## The evidence tier

**Keyless and driven.** `initialize` answered **200** as *nysgpt-data-library* **2.0** on protocol **2025-06-18** with no credential. `tools/list` returned **four** closed schemas, and all four were called: `list_databases` once, `list_tables` twice, `describe_table` twice, `query` four times (two of them deliberate failures). The free-tier allowance was not exhausted.

## The tool surface

| Tool | Arguments | What it returns |
|---|---|---|
| `list_databases` | none | The databases, one per subject, each with a one-word description. |
| `list_tables` | `database` | Every table in one database with its row count and table type. |
| `describe_table` | `database`, `table` | Field names, types and descriptions, the table description and the row count. |
| `query` | `sql` | One read-only statement, up to **1,000** rows, with column names, `bytes_scanned` and a `query_id`. |

## The catalogue, measured

`list_databases` returned **36** databases: awards, census, consumer, courts, economy, education, elections, energy, environment, executive, fec, finance, geo, grants, health, housing, insurance filings, labor, law, linked, nonprofits, oversight, patents, reactors, reference, regulations, research, scholarly, sec, siting, solar, tax, trade, trademarks, treasury, vehicles.

`list_tables` on `govblock_patents` returned **128** tables whose stated row counts sum to **3,055,846,513**. The largest are current enough to be worth naming:

| Table | Rows |
|---|---|
| `patex_transactions_25` | 504,754,561 |
| `patex_attorney_agent_25` | 366,993,004 |
| `pv_g_us_patent_citation` | 152,631,929 |
| `claims_pgpub_fulltext` | 82,017,562 |
| `cpc_master_pgpub` | 71,736,962 |
| `cpc_master_grant` | 70,324,580 |

The `_25` suffix on the prosecution tables is the year: these are PatentsView prosecution datasets, not a single concatenated archive, which is the difference between a schema an agent can bound and one it has to scan.

## One table, read end to end

`describe_table` on `govblock_patents.hist_annual` reported **175** rows and **147** fields, every one typed `string`, with an empty description on all **147**. Read literally that is a weak schema: a caller has to know that `total_app` means total applications and that `nber11_inforce` is a NBER class count in force. The table description is not prose either; it is the source path the loader recorded, `govblock-lake-638175140432/lake/v1/patents/raw/histexc//annual.csv$`.

The query is where the table earns its use:

```sql
SELECT year, total_app, total_inforce
FROM govblock_patents.hist_annual
ORDER BY year DESC
LIMIT 4
```

| year | total_app | total_inforce |
|---|---|---|
| 2014 | 412,861 | 2,565,874 |
| 2013 | 402,538 | 2,411,756 |
| 2012 | 381,508 | 2,260,800 |
| 2011 | 357,132 | 2,130,053 |

**The row count and the coverage agree.** The newest year in the table is **2014** and the table holds **175** rows, which is exactly the span from **1840** to **2014** inclusive. So this is the historical series, not the current one, and a caller asked for the newest patent count must go to `patex_*` or the grants tables rather than this one. The response reported `bytes_scanned: 1400` and a `query_id`, which is the evidence that the statement executed against Athena rather than being served from a cache of somebody's answer.

## The refusal, and the defect beside it

**A write statement is refused cleanly.** `DELETE FROM govblock_patents.hist_annual WHERE year='2024'` returned *Error: only SELECT, WITH, SHOW and DESCRIBE are allowed*. The refusal arrives as HTTP **200** with the sentence in the tool result rather than as a JSON-RPC error, so a client that only inspects the transport status will read a refusal as success.

**An unqualified table name surfaces an AWS internal error and an account identifier.** The same query with `hist_annual` instead of `govblock_patents.hist_annual` returned *query FAILED: Insufficient permissions to execute the query. User: arn:aws:sts::638175140432:assumed-role/query-api-lambda/nysgpt-query-api is not authorized to perform: glue:GetDatabase on resource: arn:aws:glue:us-east-1:638175140432:database/default*. The tool's own description says to qualify every table, so the rule is documented; what is not documented is that breaking it fails on a permissions path in the default database and hands the caller the AWS account number and the execution role's name. It is a defect to record, not a security incident: the identifier belongs to the vendor's own account and grants nothing.

## Two surfaces of one vendor that do not agree on the size

The registry record `com.nysgpt/data-library` **2.0.0** describes the corpus as **52.8B** public records. The server's own `initialize` instructions say **69 billion**. The submission to the queue says **52.8 billion records in 6,396 tables**. Three surfaces, two numbers, one vendor, and nothing in the tool output reconciles them, because the only size a caller can measure is the per-database table counts. This pass measured one database: **3.06 billion** rows in patents alone. A cumulative total across **36** databases is not something a caller should quote from a marketing line, and this guide does not.

## Is this worth a connection?

For an operator asking real questions about public money, patents or research output, yes, and the reason is the schema pass: `list_tables` plus `describe_table` is the sequence that lets an agent write a bounded statement instead of guessing table names, and `bytes_scanned` on every answer is the feedback a cost-conscious caller needs. The free tier carries no credential at all, which makes it usable in a cron or a shared agent without a secret.

What it is not: a curated dataset. Fields are text, descriptions are empty in the tables sampled, and the coverage of the historical series ends in 2014, so the useful pattern is *describe first, query second, and never assume the newest year is present*. The paid tier, the exact daily allowance and the paid-key header are vendor statements that this pass did not test.

## FAQ

### Does the NYSgpt Data Library need an API key?

Not for the free tier. `initialize`, `tools/list` and all **nine** `tools/call` requests ran with no credential, and the paid path is an `X-Api-Key` header or a `?key=` parameter.

### What SQL dialect does it speak?

Amazon Athena, which is Trino. The tool description warns that many source columns are stored as text and need `try_cast`, and the patents table this pass read typed all **147** of its fields as `string`, so cast before aggregating.

### How do I find the right table?

`list_databases`, then `list_tables` on the database, which returns each table with its row count, then `describe_table` before writing the statement. Qualify every table as `database.table`; an unqualified name fails on the default database.

### Why did a query return 2014 as the newest year?

Because that table is the historical series. The table holds **175** rows covering **1840** to **2014**, and current-year counts live in the `patex_*` and grants tables instead.

### Can it write, update or delete?

No. Only SELECT, WITH, SHOW and DESCRIBE are accepted, and a DELETE returns that sentence as the tool result.
