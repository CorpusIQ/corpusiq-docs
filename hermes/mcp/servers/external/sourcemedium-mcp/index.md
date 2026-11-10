---
title: "SourceMedium MCP - Ask Your Commerce Warehouse"
description: "Agent access to a modeled commerce warehouse: canonical metric SQL, Shopify GraphQL and Meta ad reads behind a read-only OAuth session"
category: Data & Analytics
stars: "n/a (hosted; OAuth 2.0, read-only session, nine documented tools)"
added: 2026-11-10
source: "the mcpservers.org thirteen-sitemap canonical (slug sourcemed-io) and the official registry record com.sourcemedium/source-medium 1.7.0; the endpoint at mcp.sourcemedium.com/mcp measured with a POST initialize that answered HTTP 401 and a protected-resource document served at the path its own WWW-Authenticate header named; the tool list, limits and Hermes connection steps read from sourcemedium.com/docs/ai-analyst"
relevance: ★★★
tags: [commerce-analytics, shopify, meta-ads, bigquery, data-warehouse, metrics, attribution, health-check, read-only, oauth, remote-mcp, hermes]
last_updated: "2026-11-10"
---

# SourceMedium MCP

**The argument every ecommerce operator has had with an assistant ends the same way: the model writes its own revenue query, the number does not match the dashboard, and nobody can say which definition was used. SourceMedium's MCP server answers that by not letting the assistant write the metric at all. It compiles the company's own named metric into SQL, runs it against the modeled commerce warehouse, and reports the definition and filters alongside the figure.**

```text
Server type:  Remote (Streamable HTTP)
Endpoint:     https://mcp.sourcemedium.com/mcp
Auth:         OAuth 2.0, workspace sign-in; session is read-only
Scopes:       openid profile email offline_access
Issuer:       https://grounded-ghost-20.authkit.app (WorkOS AuthKit)
Registry:     com.sourcemedium/source-medium, version 1.7.0, status active,
              published 2026-09-01T23:57:51Z
Tools:        9 documented on the current tool set (11 with the legacy pair)
Docs:         https://sourcemedium.com/docs/ai-analyst/connect-an-ai-assistant
```

## What the endpoint answers before it will talk

This is an authenticated surface, so the measurement is the refusal and the document behind it rather than a tool list. A `POST initialize` to `https://mcp.sourcemedium.com/mcp` returned **HTTP 401** with an empty JSON body and one useful header:

```text
www-authenticate: Bearer resource_metadata=
  "https://mcp.sourcemedium.com/.well-known/oauth-protected-resource/mcp",
  scope="openid profile email offline_access"
```

Following that header rather than guessing the path returned **200** with a clean protected-resource document: the `resource` is the endpoint itself, the single `authorization_servers` entry is a hosted AuthKit tenant, `bearer_methods_supported` is `header`, `resource_name` is **SourceMedium**, and `resource_documentation` points at the same connection page a reader lands on below. That is a complete discovery chain: an agent that meets this server with no prior knowledge can find the issuer, the scopes and the documentation without a human reading a blog post. Nothing was driven past the handshake, because the session requires a workspace login, and this guide says so instead of implying a tool call happened.

## The nine tools, and why the split matters

The current tool set, from the vendor's own reference page:

```text
get_data_context      organization, stores with currency and timezone,
                      connected sources, the BigQuery project and datasets the
                      assistant may query, connected Shopify stores and Meta ad
                      accounts, server limits. No arguments.
get_account_health    each connection's status, data freshness, open incidents,
                      and who owns the fix. No arguments.
search_docs           SourceMedium's public documentation, for what a metric or
                      table means. Never your numbers.
search_data_catalog   tables, columns and named metric definitions, searched in
                      your own words; with no query it lists everything
                      documented, and with up to four table names it describes
                      their columns and types.
query_metrics         compiles a named SourceMedium metric into SQL and runs it,
                      applying the canonical definition and its filters.
run_bigquery_sql      one read-only SELECT against the warehouse.
shopify_admin_graphql one read-only GraphQL query against a connected store.
meta_ads_query        live reads from a connected Meta ad account.
submit_feedback       a rating a reason and a comment on whether the last
                      answer was right. Never SQL, credentials or rows.
```

Two more tools, `describe_table` and `describe_tables`, survive on connections created against the earlier tool set. The practical difference is that a buyer may see nine tools or eleven depending on when the connection was made, and the documentation is explicit that the tool list is how you tell which set you have. That is worth knowing before an operator reads a review that counts tools for them.

## The order that produces a number you can defend

The vendor publishes the sequence, and it is the most transferable part of this server because it is a general rule for any agent on a modeled warehouse:

1. `get_data_context` first in every session, and again before touching a source it has not used. It is cheap and it stops the model guessing a store or a currency.
2. `search_data_catalog` to resolve the real column and metric names.
3. `query_metrics` when a named metric matches, because it applies the canonical formula and the validity filters, including `is_order_sm_valid`, which drops draft, cancelled and refunded orders.
4. Only when `query_metrics` refuses, or the question is not a catalog metric, describe the tables and then write SQL with `run_bigquery_sql`, using only the names that came back.

The documented failure mode is the one every operator has met: an assistant invents a column. Order revenue is `order_net_revenue` on `obt_orders`; it is not `total_price`, and `dim_orders` carries no revenue column at all. When an answer looks wrong, the instruction is to ask which table and column were used, and to send the model back to `search_data_catalog` if it names something unrecognisable.

Two calls sit outside the query path and are worth asking for by name. "Are my connections working?" routes to `get_account_health`, which reports freshness and, usefully, whether the fix belongs to you, your provider or SourceMedium. "What does this metric mean?" routes to `search_docs`, so the model explains a concept from the documentation instead of inventing one.

## What the session can and cannot reach

The reach table is narrow and stated in the vendor's own words, which is why it belongs in a guide rather than a footnote:

- SourceMedium reporting data (`sm_transformed_v2`, `sm_metadata` and any dataset `get_data_context` lists) is always available.
- Other datasets in the workspace's BigQuery project are available only if the user is a direct member of a dedicated project, and only for datasets `get_data_context` lists.
- Google Sheets tables in those datasets work once each sheet is shared with the SourceMedium address shown in the workspace, and an unshared sheet returns `PROVIDER_PERMISSION_DENIED` with the sheet and the address, so the agent can tell you exactly what to share.
- Shopify and Meta answer as soon as a store or ad account is connected, and answer `SOURCE_UNAVAILABLE` if it is not.
- Agency grants are supported; a brand- or store-scoped grant sees only those stores and cannot run raw SQL.

The limits are published as numbers, which is rare enough to record: **500** warehouse rows before a result is marked truncated, **100** Shopify and Meta records per page, **10 GiB** of BigQuery billed bytes per query, **60 s** for warehouse queries and **30 s** for Shopify and Meta, and a **256 KiB** response cap. Two caveats come with the access itself and should be repeated to any operator who wires this up: the connection provides no semantic PII detection or field-level masking, and queries and results may be sent to whichever AI provider the user chose.

## Connecting from Hermes

SourceMedium is one of the few vendors in this catalog that documents Hermes by name, with the command this profile actually uses:

```bash
hermes mcp add sourcemedium --url https://mcp.sourcemedium.com/mcp --auth oauth
```

Sign in when prompted, then prove the connection rather than assuming it:

```bash
hermes mcp test sourcemedium
```

Their page also carries steps for Claude, ChatGPT, Claude Code (`claude mcp add --transport http sourcemedium https://mcp.sourcemedium.com/mcp`), Codex (`codex mcp add sourcemedium --url https://mcp.sourcemedium.com/mcp`), Cursor, Grok Bot and Muse. Any workspace member can connect, and the session sees only what that member already sees.

A sane first question, taken from the vendor's own example, is also a good test of whether the assistant is behaving: ask it to compare net revenue for the last complete week against the week before, **using SourceMedium's own metric definition through `query_metrics`**, and to name the stores, dates and timezone it used and show the definition and any filters. An answer that names none of those did not follow the sequence, and the next question should be why.

## The class it enters

The warehouse-access class already has owners here, and this one is not a duplicate of any of them. [Dataddo](/hermes/mcp/servers/external/dataddo-data-to-ai-mcp/) moves data from platforms into an AI-readable store, [Catalogian](/hermes/mcp/servers/external/catalogian-mcp/) puts a CSV or a URL behind read-only record tools with deltas, [Azquo](/hermes/mcp/servers/external/azquo-mcp/) is an audited store where every figure traces back to a source file, and [Muvia BI](/hermes/mcp/servers/external/muvia-bi-mcp/) governs queries with lineage. All four start from data you bring. SourceMedium is the only entry in the class where the model is already built: store, orders, ad spend and the metric definitions that join them, with the definitions shipped as tools so the assistant cannot quietly substitute its own.

That is the distinction worth keeping: elsewhere the risk is a wrong number because the pipeline was wrong, and here the risk the server was designed against is a wrong number because the model wrote its own SQL.

## FAQ

### Does SourceMedium MCP write to my data?

No. Every documented tool is a read. `run_bigquery_sql` takes one read-only `SELECT`, `shopify_admin_graphql` runs a read-only query, and `meta_ads_query` reads. The vendor states that no tool writes to your data, exports it, or reaches another organisation's data.

### Why does the same question give a different number than my dashboard?

Almost always because the definition differed. `query_metrics` applies SourceMedium's canonical formula and its validity filters, so the reliable way to match a dashboard is to call it by name instead of letting the model write revenue, AOV or ROAS by hand. Match dates, timezone, stores and filters before assuming either number is wrong.

### What happens if a Shopify store or Meta account is not connected?

The Shopify and Meta tools answer `SOURCE_UNAVAILABLE` rather than returning data, and warehouse questions keep working. Connecting the source in the workspace is what makes the tool answer. Unshared Google Sheets return `PROVIDER_PERMISSION_DENIED` with the exact address to share.

### Is the assistant allowed to see customer contact details?

It sees what the connecting member can see, and the vendor warns that the connection provides no semantic PII detection or field-level masking. The stated policy is to avoid requesting customer contact, address or other direct personal data unless it is necessary and authorised.

## See also

- [Muvia BI MCP](/hermes/mcp/servers/external/muvia-bi-mcp/) for governed queries with lineage
- [Dataddo Data to AI MCP](/hermes/mcp/servers/external/dataddo-data-to-ai-mcp/) for getting platform data into a store an agent can read
- [Catalogian MCP](/hermes/mcp/servers/external/catalogian-mcp/) for read-only records over a CSV or a URL
- [Azquo MCP](/hermes/mcp/servers/external/azquo-mcp/) for an audited store where every figure has a source
