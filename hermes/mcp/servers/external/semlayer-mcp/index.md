---
title: "semlayer MCP - A Metric Layer Inferred From the Warehouse"
description: "It reads your warehouse, works out which columns are measures, which joins fan out and which status code means cancelled, then serves that layer to any agent over MCP - so two assistants stop giving two numbers."
category: Data & Analytics
stars: n/a (Fair Source, free for internal use, no key; ~$0.70 per 100 tables in your own model calls)
added: 2026-11-06
source: "The mcpservers.org twelve-sitemap addition semlayer-dev/semlayer in the 03:00 MST canonical refresh (19,728 server URLs against 19,513); the official MCP registry record dev.semlayer/mcp 0.7.0b2 at https://semlayer.dev with a stdio PyPI package `semlayer` run through uvx; the repository README at github.com/semlayer-dev/semlayer (12,309 bytes, licence FSL-1.1-ALv2) and docs/mcp.md (27,652 bytes); the PyPI metadata for semlayer 0.7.0b2; and a locally driven session - a six-table DuckDB fixture inferred with `--no-llm`, then served over stdio MCP with twenty-one tools listed and six called"
relevance: ★★★★
tags: [data, semantic-layer, metrics, warehouse, duckdb, postgres, snowflake, bigquery, mcp, stdio, sql-linting, provenance, claude, cursor]
last_updated: "2026-11-06"
---

# semlayer MCP

**Two assistants answer the same revenue question with two different numbers, and neither one is lying.** One summed `tot_amt` over every order ever written; the other summed the same column with the cancelled ones dropped. Nobody chose either rule, so nobody can defend either number, and the mistake is silent: the query runs, the chart draws, the total is 36 percent too high. semlayer attacks that at the root by reading the warehouse itself, inferring what each table and column *means*, and handing every agent the same definitions with a confidence and a provenance trail attached to each one.

```
Server type: Local, stdio (also runnable from a checkout)
Package:     semlayer 0.7.0b2 on PyPI, `uvx --with "semlayer[warehouses]" semlayer mcp layer.yaml`
Registry:    dev.semlayer/mcp 0.7.0b2, published 2026-11-05T02:24:10Z
Warehouses:  DuckDB, PostgreSQL, Snowflake, BigQuery, Iceberg on S3 via the DuckDB bridge
LLM:         optional. `--no-llm` is fully deterministic; otherwise Anthropic API, escalation only
Licence:     Fair Source FSL-1.1-ALv2 - free for any internal use including production and CI,
             no fee and no key; the one prohibition is reselling it as a competing service.
             Every release converts to Apache-2.0 two years after publication; the format
             spec and its JSON Schemas are Apache-2.0 from the start
Cost:        the tool is free; the money is your own model spend, ~$0.70 per 100 tables by
             the vendor's measured cost model (about 80 percent of columns resolve from
             statistics alone)
Tools:       21 over MCP
```

**Evidence tier: driven, not quoted.** This entry was measured on this machine rather than read off a pricing page. A six-table DuckDB fixture was built with the traps that make warehouse answers wrong - a status code column whose decode lives in a separate dimension, an order header that a line table fans out, a customer master in SCD2 shape, a legacy twin of the order table, and an aggregate that only reconciles when cancelled orders are excluded. `semlayer infer duckdb:store.db --no-llm` wrote `layer.yaml`: **6 tables, 25 columns, valid=True, 4 items awaiting review**, in deterministic mode with **no API key and no model call**. The MCP server was then started over stdio and driven: `initialize` answered protocol **2025-06-18** as `semlayer` **1.30.0**, `tools/list` returned **21** tools, and six were called with real arguments.

## What it inferred without a model

| Inferred | Measured on the fixture |
|---|---|
| **Measure vs dimension** | `tot_amt` and `ext_amt` typed `monetary_value` with `sum`, `avg`, `min`, `max`, `count` allowed and `sum` as the default; `ord_dt` typed `date` as a dimension |
| **Grain** | `ord_hdr`: "one row per ord_id"; `ord_lin`: "one row per lin_id"; `cust_mstr`: "one row per cust_id, eff_end_dt (one row per version of each entity)" |
| **SCD2 shape** | `cust_mstr` classified `snapshot_scd2` from the `eff_start_dt` / `eff_end_dt` / `is_curr_flg` trio, with the as-of join rule attached |
| **Joins + fan-out risk** | `ord_hdr -> cust_mstr` and `ord_hdr -> sts_dim` inferred as `many_to_one` left joins, the first flagged `fanout_risk: true` at confidence 0.84 |
| **Status decode** | Read `sts_dim` as the dictionary, decoded `C=Completed`, `X=Cancelled`, `P=Processing`, and produced a metric `total_tot_amt_completed` carrying `filter: sts_cd = 'C'` with the provenance line "status filter via dictionary decode (C=Completed)" |
| **Routing and deprecation** | `repo_knowledge.routing` sends "analysis of ord hdr" to `ord_hdr` and names `ord_hdr_legacy` as avoid, reason "legacy-named table; superseded by ord_hdr" |
| **Ratios** | `avg_tot_amt_per_order` as a ratio of `SUM(tot_amt) / COUNT(ord_id)`, with the synonyms "average order value" and "tot_amt per order" |
| **Tier** | `agg_` prefix read as an aggregate table, `sts_` as a dimension, with the tier carrying its own confidence (0.9) and provenance |

Every claim above carries `confidence`, `provenance` (which signal produced it - naming rule, statistic, dictionary decode) and `lifecycle` (`inferred`, then `reviewed`, then `certified`, plus `deprecated`). That is the part an operator can use in an argument with their own team: the layer does not merely assert that revenue excludes cancellations, it says which evidence made it say so and how sure it is.

## The two numbers, measured

The compiled metric and the naive query were both run against the same fixture.

```
compile_metric total_tot_amt_completed
  -> SELECT SUM(ord_hdr.tot_amt) AS total_tot_amt_completed
     FROM raw.ord_hdr AS ord_hdr WHERE (sts_cd = 'C')            -> 240,857.05

compile_metric total_tot_amt            (the unfiltered twin)
  -> SELECT SUM(ord_hdr.tot_amt) AS total_tot_amt
     FROM raw.ord_hdr AS ord_hdr                                  -> 378,881.81
```

**138,024.76 apart, on 300 orders of which 188 are completed.** The aggregate table in the fixture sums to **240,857.05**, matching the filtered metric exactly - which is how the status rule is confirmed rather than guessed. An agent handed the raw schema has no way to know which of the two numbers the business means; an agent handed this layer is told, and told why.

## The linter is the part that catches the silent error

`check_sql` (and `semlayer lint` on the CLI) is deterministic - no model in the path. Fed a query that joins the line table and then sums a header measure, it refuses with the reason and the fix:

```
{"ok": false, "errors": 1,
 "findings": [{"rule": "fanout_aggregate", "severity": "error",
   "message": "SUM(ord_hdr.tot_amt) in a block that joins ord_lin (many rows per ord_hdr)
               multiplies ord_hdr's values",
   "fix": "aggregate ord_lin in a subquery first, or restrict ord_hdr with EXISTS/IN
           (SELECT ... FROM ord_lin) instead of joining it"}]}
```

The same query without the join returns `{"ok": true, "findings": []}`. The documented rule set covers missing required filters, fan-out sums, deprecated tables, SCD2 read without a validity window, hallucinated columns and vacuous correlated subqueries. In the deterministic run the fan-out rule fired correctly; the "missing required filter" rule needs the business rule to have been inferred into the layer first, and on this fixture that rule was not inferred without a model - a real limit of `--no-llm`, recorded here rather than papered over.

## What the rest of the surface does

- `status` - what the server has, which layers are on the machine, which warehouses it can see, what to do next. Works with no layer built yet.
- `discover_connections` - finds warehouse connections by name from the machine (DuckDB files in the working directory, DSNs in the environment). The vendor's own caution is worth repeating: a `.db` file may be SQLite rather than DuckDB, and it says so rather than guessing.
- `context_for_question` - returns only the part of the layer a question needs; `semantic_search`, `get_tables`, `table_detail`, `get_metrics`, `route_intent`, `get_domains` for navigation.
- `compile_metric` - turns a metric plus a grouping into SQL with joins, filters and time bucketing already applied.
- `run_sql` - one read-only SELECT, with `check_sql` in front of it. It refused in this session with "no warehouse connection is selected" because the layer was loaded from a file and no connection was opened - the safe failure, and the message says exactly that.
- `review_questions` / `review_answer` / `review_decisions` - the four undecided items come back as questions a person can answer, each saying what accepting or rejecting does and whether the agent may decide it itself. The design principle is that the agent may accept what it inferred from evidence and never silently set a definition on a person's behalf.
- `infer` / `cancel_infer` / `save_layer` / `export_layer` - build from inside the conversation, then write the layer into the project and export it to dbt (dbt is the only exporter today; losses are reported rather than dropped).

## Where it fits in this catalog

The semantic-layer idea was already here twice, and neither entry is the same mechanism. **Dataddo** serves twelve tools over a semantic layer connecting 400+ CRM, ad, ERP and payment SaaS apps - a hosted stack that maps connectors it already holds into business entities and blessed metrics. A **sheets-and-files into PostgreSQL** entry puts an approved definition behind an answer. Both require someone to declare the layer, or to accept the vendor's declaration of it.

semlayer is the first entry here that **infers the definitions from the warehouse's own statistics** - undeclared foreign keys, status decodes, grain, SCD2 shape, and the business rule hiding in an aggregate table - and gives each one a confidence and a provenance line a human can review or overturn. It also does not need an account: the layer is a YAML file on the operator's disk, and the server is a local process.

For a business that already runs its numbers through an AI assistant, that is the difference between an assistant that is told the definitions and an assistant that keeps choosing new ones. It is the closest external tool this catalog carries to the problem CorpusIQ exists to solve, and the reason it earns a guide rather than a class hold.

## How an operator would use it

1. `pip install "semlayer[warehouses]"` (or let `uvx` fetch it on first MCP launch - no terminal step needed).
2. `semlayer infer postgres -o layer.yaml --context ./docs/ --context ./etl-repo/CLAUDE.md` - the `--context` files are read as priors, and where a doc contradicts the data the contradiction goes to review rather than overriding it silently.
3. `semlayer review layer.yaml` - answer the open questions; each verdict records who stands behind it.
4. `semlayer mcp layer.yaml` from any MCP client, or `uvx --with "semlayer[warehouses]" semlayer mcp` to start with nothing and let `status` guide the first step.
5. `semlayer lint layer.yaml query.sql` in CI, and `semlayer drift layer.yaml postgres` on a schedule - the layer is only useful while it is still true, and an `ALTER TABLE` is what makes every hand-written layer go stale.

## Limits, stated plainly

- **Beta, 0.7.0b2.** The vendor says so on the tin and publishes its negative results: on clean, well-named TPC-DS-shaped schemas the vendor's own benchmark shows raw DDL is already sufficient, so a tidy warehouse may not need this.
- **The numbers are the vendor's.** 82 percent correct business answers against 42 percent from the raw schema on their messy-warehouse benchmark, and the 21.3 percent Spider 2.0 figure for frontier models, are vendor claims with published methodology, fixtures and recorded model responses - reproducible with `pytest` and no API key, but not independently measured here.
- **A DuckDB storage-version trap, hit during this session.** The pinned `duckdb` is 1.x (1.5.6 bound by `duckdb<2`); a database file written by a 2.x duckdb (storage version 69) fails with "we can only read versions between 64 and 68". Build the file with the same major version you point the tool at.
- **LLM access is Anthropic only today** (Bedrock and Vertex are stated as next), and descriptions, business-rule hypothesis testing and validated joins are the parts that want a key. `--no-llm` still types and roles columns usefully (0.780 typing / 0.834 role on the vendor's seven fixtures).
- **Privacy knobs are real and worth using**: `--no-sample-egress` keeps every warehouse cell value out of the prompts at no measured net accuracy cost on the vendor's fixtures; model responses are cached on local disk (`~/.cache/semlayer/cassettes`) and contain no credentials and no result sets; telemetry is anonymous, shows exactly what it sends via `semlayer telemetry --show`, and opts out with `--off` or `SEMLAYER_TELEMETRY=off`.
- **Read-only by construction**: `init` generates a minimal-grant script and the reader persona is tested unable to write, on PostgreSQL in ordinary CI and on Snowflake against a live account.
- **Licence is Fair Source, not open source.** Free for internal use including production and CI with no fee and no key; the one prohibition is offering semlayer to third parties as a competing product or service. Releases 0.1.0b1 through 0.4.0b5 were Apache-2.0 and stay that way permanently.
- **No hosted service, no ontology enrichment** (it failed the vendor's own ablation gate, and they published the receipts), no LookML or RDF exporter, and Postgres-protocol engines such as Redshift are reachable but untested.
