---
title: "DocQuery MCP - Spreadsheet and PDFs, One Queryable Table"
description: "A read-only MCP over a workbook and the PDFs beside it: four tools, a public demo key, and rows joined by a declared foreign key"
category: "Data / Documents"
stars: "0 (closed source; demo key published on docquery.io)"
added: 2026-11-13
source: "the submission queue entry #7252, the official registry records io.docquery/docquery 1.0.0 and 1.0.1, the vendor page docquery.io read the same day, and a live session on this host: Bearer dq_demo_readonly against https://docquery.io/api/v1/mcp with initialize, resources/list, prompts/list, tools/list and eight tools/call requests"
relevance: ★★★
tags: [documents, spreadsheets, airtable, excel, pdf, relational, read-only, demo-key, mcp, remote]
last_updated: "2026-11-13"
---

# DocQuery MCP

**Every operator has a customer list in one place and the paperwork that belongs to those customers in another**, and the question that matters lives between them: which invoices belong to which account, which contract covers which project, which pro-plan customer is behind on payment. A spreadsheet-to-JSON tool hands the agent one flat table. A PDF parser hands it fields from one document at a time. Neither answers the join, so the person asking goes back to cross-checking two windows by hand and the agent goes back to guessing.

DocQuery is a small hosted service that takes the sheet and the documents, extracts them into real tables, and lets you declare the link between them - a foreign key, no migrations - then publishes the same relational model over REST, GraphQL and MCP. The MCP surface is the part measured here, and it is deliberately narrow: **four read-only tools**, a public demo key so the claims can be checked without an account, and an instruction string that tells the model what to cite and what never to invent.

```text
Server type:   remote Streamable HTTP, JSON-RPC 2.0, sessionless (no Mcp-Session-Id issued)
Endpoint:      https://docquery.io/api/v1/mcp
Server:        docquery-mcp 1.0.0, protocol 2025-06-18,
               capabilities: tools, resources, prompts
Registry:      io.docquery/docquery 1.0.0 and 1.0.1, streamable-http, same URL
Auth:          Bearer token; the public read-only demo key works with no signup,
               OAuth 2.1 is offered to Claude and ChatGPT, your own workspace key
               is read/write
Tools:         4, every one annotated readOnlyHint: true
Resources:     3 (two tables plus the workspace schema)
Prompts:       3 (schema_overview, find_rows, count_by)
```

## The evidence tier

Fully driven, keyless-equivalent. `initialize` answered **200** with `serverInfo` `docquery-mcp` **1.0.0** on protocol **2025-06-18**, no session header was issued, and `capabilities` carried **tools**, **resources** and **prompts** - so this is not a tool-only endpoint, it also exposes data as addressable resources and ships three prompt templates.

The key is the one DocQuery prints on its own homepage for exactly this purpose: `dq_demo_readonly`, a read-only workspace holding an example customer list and an example invoice set, already linked. **Eight `tools/call` requests were driven** against it, plus `resources/list`, `resources/templates/list` and `prompts/list`.

`io.docquery/docquery` answers in the official registry at **1.0.0** and **1.0.1** with the remote declared as the same URL and the description *Read-only MCP over your Excel or Airtable plus the PDFs beside it, joined as one relational dataset.*

The server's own `instructions` string is a contract about honesty, and it is unusually specific: rows returned by `query_table` carry `source_page` **when the PDF page, PowerPoint slide or Google Slides slide is known, and null otherwise** (Word, spreadsheets, Airtable), the caller should cite the filename and the page when reporting an extracted value, and - verbatim - **do not invent a page when `source_page` is null**.

## What the four tools do

| Tool | Required arguments | What it returns |
|---|---|---|
| `list_tables` | none | every table with slug, name, row count, columns (name, type, slug, primary key), and `source_document` |
| `list_relations` | none | the declared foreign keys as `table.column` to `table.column`, with `many_to_one` and its siblings |
| `query_table` | `table_slug` | rows, with `offset`, `limit`, `columns`, exact-match `filter`, case-insensitive `search`; response carries `total` and `returned` |
| `related_rows` | `table_slug`, `column`, `value` | the rows on the far side of the relation, per relation, with `matched` |

The resource surface mirrors the tables at `docquery://tables/example_customers`, `docquery://tables/example_invoices` and `docquery://schema`, all `application/json`, so a client that supports resources can read a table without spending a tool call. `resources/templates/list` came back empty - there is no parameterised template.

## What came back when it was driven

`list_tables` returned **two** tables. `example_customers` holds **4** rows with `id`, `name`, `plan`, `country`, `contact_email`. `example_invoices` holds **6** rows with `number`, `customer_id`, `issued_on`, `due_on`, `total`, `status`. `list_relations` returned exactly one link, `many_to_one`, from `example_invoices.customer_id` to `example_customers.id`.

`query_table` on `example_invoices` returned `total: 6` with the six invoices, including an oddity worth seeing: **INV-1006 carries `total: 0` and status `paid`**. A zero that is a real value, not a missing field, and the kind of row a summary written by a language model will happily round out of existence.

The filter is exact-match and it is honest about what it matched:

```json
{"table_slug": "example_invoices", "filter": {"status": "paid"}}
-> {"table": "example_invoices", "total": 3, "returned": 3, "rows": [...]}
```

Three of six invoices are `paid`: INV-1001 (4,200), INV-1005 (980.50) and INV-1006 (0). The response carries both `total` (matching rows in the table) and `returned` (rows in this page, bounded by `limit`), which is the difference between "three match" and "three fit in the answer" - a distinction most list endpoints blur and every agent needs.

`query_table` on `example_customers` with `{"plan": "pro"}` returned **2** rows: Acme Corp (US) and Initech (CA), each with a contact address.

The join is the point of the product, and it is one call:

```json
{"table_slug": "example_invoices", "column": "customer_id", "value": 2}
-> {"related": [{"relation": "example_invoices.customer_id → example_customers.id",
                 "kind": "many_to_one", "matched": 1,
                 "target_table": "example_customers",
                 "rows": [{"id": 2, "name": "Globex", "plan": "starter",
                           "country": "MX", "contact_email": "finance@globex.example"}]}]}
```

So "which invoices belong to Globex, and is the account in good standing" is answered from two tables in one hop, with the relation named in the response rather than assumed.

## The defect, recorded

Call a valid tool with a **missing** required argument and the error names the wrong problem. `tools/call` on `query_table` with `{"table": "example_invoices"}` (the wrong key, so `table_slug` is absent from the arguments) returned HTTP **200** with `isError: true` and this text:

```json
{"error": "Unknown tool: query_table"}
```

The tool exists; the argument was missing. An agent that retries on "unknown tool" by re-listing tools or switching approach is being steered away from a one-word fix. `related_rows` with the same mistake produced the correct message instead (*related_rows requires table_slug, column, and value*), so the misleading branch is specific to the tool with an optional-argument set, not to the server as a whole. Worth knowing before you wire retries: **on this surface, treat "Unknown tool" as "check your arguments" first.**

The schema itself is precise where it matters - `query_table` declares `table_slug` required and the five optional parameters, `related_rows` declares all three - which is why the failure reads as a bug rather than a design.

## Connecting it

Claude (web or desktop) and ChatGPT both take a remote MCP server by URL; DocQuery documents OAuth 2.1 for those clients. For the demo, a static header is enough:

```json
{
  "mcpServers": {
    "docquery": {
      "type": "http",
      "url": "https://docquery.io/api/v1/mcp",
      "headers": { "Authorization": "Bearer dq_demo_readonly" }
    }
  }
}
```

On Hermes:

```bash
hermes mcp add docquery --url https://docquery.io/api/v1/mcp --auth none
```

Then send the header, or use a client-side bearer token if your client supports one. Your own workspace issues a private key with full read/write against the REST and GraphQL surfaces; the demo key is read-only and sees only the example workspace.

## Questions this answers that a chat window alone cannot

### Which customers have unpaid invoices?

Two calls: `query_table` on the invoice table filtered by status, then `related_rows` per `customer_id`. The answer arrives with the account name and plan attached instead of a list of invoice numbers and a mental join.

### Which page of the contract does this figure come from?

`source_page` is populated where the extraction knows it - a PDF page, a PowerPoint or Google Slides slide - and `null` where it cannot (Word, spreadsheets, Airtable). The server's own instruction is to cite filename and page when it is known and **not to invent one when it is not**, which is the failure mode that makes document-extraction answers untrustworthy in the first place.

### Can it change my data?

Not through this surface as measured: four tools, all `readOnlyHint: true`, all reads. Writes live on the REST and GraphQL APIs behind your own workspace key. A read-only MCP in front of a writable API is a deliberate split and worth preferring when the agent is drafting rather than executing.

### What does it cost for the demo?

Nothing - the demo key is public and the free tier is documented as **5 documents and 10,000 rows**, no card required. Pro raises the document and row ceilings; team workspaces, audit logs and row-level security are listed as coming, not shipped.

## Verdict

A three-star catalog entry on the strength of one idea executed properly: **the join is declared once and then reused by every client**. The measured surface is small (4 tools, 3 resources, 3 prompts) and completely read-only, the demo workspace is checkable in five minutes with a key printed on the vendor's homepage, and the instruction string is the kind of guardrail most extraction products leave to the prompt the user happens to write.

What holds it back is depth: four tools cover listing and reading, and everything that makes this a product - upload, extraction review, relation authoring, live Excel sync, Airtable and Google Sheets connectors - sits on REST and GraphQL, not on MCP. The `Unknown tool` error on a missing argument is a real defect that will cost an agent a retry loop, and the surface is closed source, so the extraction behaviour that produces `source_page` cannot be inspected.

For a team whose data is a spreadsheet plus a folder of documents, this is the shortest path from that pair to an agent that can answer a question across both. It is not a warehouse and does not pretend to be.

See also: [Basis MCP](/hermes/mcp/servers/external/basis-mcp/) for an Excel engine an agent can audit, [SumOffice MCP](/hermes/mcp/servers/external/sumoffice-mcp/) for editing a real workbook, and [OpenDocKit MCP](/hermes/mcp/servers/external/opendockit-mcp/) for a local document reader.
