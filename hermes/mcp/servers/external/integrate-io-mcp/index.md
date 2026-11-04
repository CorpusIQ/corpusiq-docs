---
title: "Integrate.io MCP Server - ETL Pipelines by Description"
description: "Hosted MCP for Integrate.io ETL and Reverse ETL: 46 tools to inspect, build, run and repair data pipelines from a description, with dry runs."
category: Data & Analytics
stars: n/a (hosted vendor server, no public repository)
added: 2026-11-03
source: "chatmcp/mcpso submission #6689-adjacent window item on the official Integrate.io listing at mcp.so/servers/integrate-io-mcp-server, plus a keyless probe on https://api.xplenty.com/0/api/mcp answering HTTP 401 with OAuth protected-resource metadata, and the vendor documentation at integrate.io/docs/etl"
relevance: ★★★
tags: [etl, reverse-etl, data-pipelines, data-integration, warehouse, oauth, remote-mcp]
last_updated: "2026-11-03"
---

# Integrate.io MCP Server

**Data work breaks in the gap between what a pipeline does and who can read it. The engineer who built it knows why the Salesforce sync failed at 04:00. The founder asking the question gets a dashboard that is three hours stale and nobody free to explain it.**

Integrate.io puts its ETL and Reverse ETL platform behind one hosted MCP endpoint, so the question about the pipeline is answered in the same conversation as the question about the business. The endpoint is per account and the URL tells you why:

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.xplenty.com/YOUR_ACCOUNT_ID/api/mcp
Transport:   one JSON-RPC 2.0 message per request, batching not supported
Auth:        OAuth 2.1 browser sign-in, or a Personal Access Token
Tools:       46 per the vendor documentation (44 on the directory card)
Clients:     Claude, Claude Code, ChatGPT, Cursor, Perplexity, Codex, any MCP client
Billing:     included with an Integrate.io ETL account
Site:        integrate.io/platform/mcp/
```

The domain is `api.xplenty.com` because Integrate.io was formerly Xplenty and the API predates the rebrand. The dashboard URL and the API URL both work, and the account id can be copied from the dashboard rather than assembled by hand.

A keyless `initialize` against an unpopulated account path answered **HTTP 401** with `Bearer error="invalid_token"` and `resource_metadata="https://api.xplenty.com/0/.well-known/oauth-protected-resource"`, which is a live OAuth-gated endpoint naming its own metadata rather than an empty refusal. No tool was called: the surface needs an account, so this entry is documented from the vendor's parameter-level reference and states that tier plainly.

## The tools split three ways, and the split is the design

**Reading and inspecting**, safe on a production account: `list_connections` and `get_connection` for the shape of a source without its credentials, `list_workspaces`, `list_packages` and `get_package` for the flow graph with secrets redacted, `list_clusters`, `search_all` for free-text search across connections, packages, clusters and workspaces, `validate_package` and `validate_expression`, `discover_schema` and `discover_file_schema`, `preview_data`, `preview_transformation`, `profile_data`, `test_connection`, `ask_docs` for a sourced answer out of the live documentation, and `report_issue` carrying the `call_id` the server attaches to every result.

**Building and editing**, which is where a description becomes a pipeline: create or clone a package, add, edit and remove components and edges, manage variables, save or discard a draft, and roll back a version.

**Jobs and schedules**, where the operational questions live: `list_runs`, `get_run`, `get_run_summary`, `explain_job_failure`, `list_schedules` and `get_schedule`, then `toggle_schedule`, `create_schedule`, `update_schedule`, `create_cluster`, `run_package`, `cancel_job` and `retry_job`.

Two of those deserve their own line. `get_run_summary` returns records read per source and written per destination, per flow, so a partial load is visible instead of inferred. `explain_job_failure` returns the primary error, the detected error patterns and the log tail, which is the difference between an assistant saying a job failed and an assistant saying why.

## The containment details are what an operator should read first

The vendor is unusually direct: mutating tools **take effect immediately and there is no sandbox**. A package edit or a schedule change is against production. Three published behaviours make that survivable rather than alarming:

- Tools that subclass the mutation base support a `dry_run`, which validates and returns the would-be outcome without applying it. Any agent workflow that touches a live pipeline should set it first, and the guide says so because the default is the opposite.
- `create_schedule` creates a schedule **disabled by default**, so a schedule built by an assistant does not start firing because the tool succeeded.
- `create_cluster` provisions **billed infrastructure**. It is a spend action wearing a provisioning name, and it belongs behind the same approval a payment would get.
- Package edits are versioned and can be rolled back, and every change made through MCP lands in the account's audit history.

Two smaller traps are documented rather than discovered later: `list_runs` defaults to root runs only, so child retries are excluded unless you ask for them, and `validate_package` records a validation and writes the workflow's script to S3 even though it does not alter a pipeline.

Access follows the person, not the token: every tool is scoped to the authenticated account, obeys the signed-in user's permissions, and a token for another account gets a 403. The tools return connection shapes but never credentials, TLS certificates or SSL keys.

## On the token lifetime, and why it matters more than it looks

The vendor supports OAuth 2.1, which most modern clients use, and a Personal Access Token for everything else. The PAT default lifetime is **ten years**. For an account that can build pipelines and start billed clusters, a decade-long static credential is the weakest link in an otherwise careful permission model, and it is the one setting a buyer should change on day one. Revocation and re-authentication are documented on the same page, which is the right place for them.

## Why this earns a guide

There is no ETL entry in the catalogue. The neighbours read data rather than move it: [SaturnSQL MCP](/hermes/mcp/servers/external/saturnsql-mcp/) and [Snowflake MCP](/hermes/mcp/servers/external/snowflake-mcp/) query a warehouse that something else has to fill, and [SQL Server MCP](/hermes/mcp/servers/external/sql-server-mcp/) runs a DBA console over instances.

The pipeline that fills the warehouse was the uncovered angle, and it is the one a business operator hits as "the numbers in my assistant are from yesterday". A connector can read a source directly; only the pipeline knows what was transformed, what loaded and what failed between them. Reading that from chat, and repairing it from chat with a dry run, is the operator surface nothing else in these 1,094 guides covers.

## FAQ

### Does the server need to be installed or hosted?

No. Integrate.io hosts it. You add your account's URL to the client and sign in, and stdio-only clients reach it through an `mcp-remote` bridge.

### Can an assistant change a live pipeline?

Yes, and it takes effect immediately because there is no sandbox. Mutation tools accept `dry_run`, schedules are created disabled, and every change is versioned and audited.

### Which tool counts are right, 44 or 46?

The vendor's documentation says 46 tools across the three areas; the directory card says 44. The vendor also tells you to run `tools/list` against your own account for the exact set, which is the answer that cannot drift.

### What credential should I use?

OAuth 2.1 where the client supports it, since nothing is pasted or stored. If a static token is required, mint a PAT and shorten its ten-year default before using it on an account that can start billed clusters.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [SaturnSQL MCP - Ask Your Database from Any Agent](/hermes/mcp/servers/external/saturnsql-mcp/)
- [Snowflake MCP - Data Warehouse Queries for AI Agents](/hermes/mcp/servers/external/snowflake-mcp/)
- [SQL Server MCP - Multi-Instance DBA Console](/hermes/mcp/servers/external/sql-server-mcp/)
- [AgentLedger MCP - Per-Agent Spend Management for Operators](/hermes/mcp/servers/external/agentledger-mcp/)
