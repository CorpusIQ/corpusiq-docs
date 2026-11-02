---
title: "Catalogian MCP - A Data Record Your Agent Can Question"
description: "Keyless data records over MCP: point it at a CSV or a URL, query the data with 18 read-only tools, and receive a delta every time the source changes."
category: Data & Analytics
stars: ★★★ (keyless anonymous records, 18 tools driven)
added: 2026-11-02
source: "the mcpservers.org newest page on 2026-11-02 (slug catalogian-mcp), the product documentation at catalogian.com/docs, and a driven session on https://api.catalogian.com/v1/mcp: an anonymous ingest of a public CSV, initialize HTTP 200, 18 tools listed, and live calls to snapshot_schema, get_snapshot_rows, query_snapshot, filter_snapshot_rows, search_snapshot, list_editions, get_delta, get_edition_diff and compare_snapshots"
relevance: ★★★
tags: [data-records, csv, jsonl, delta-tracking, data-versioning, read-only, keyless, remote-mcp]
last_updated: "2026-11-02"
---

# Catalogian MCP

**A spreadsheet answer is only as current as the evening somebody re-exported it. The useful question is not what the file says, it is what changed in it since the last time anyone looked.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.catalogian.com/v1/mcp
Auth:        anonymous session token, record key or account key
Tools:       18 measured, all read-only
Record:      a CSV, TSV or JSONL source, versioned on every ingest
Delta:       per row, new, changed or deleted, with the key
Pricing:     free 2 records, $4 and $12 per record monthly
```

## What it does

Catalogian turns a data source into a **record**: a CSV, TSV or JSONL file, fetched from a URL or uploaded, keyed on a column, indexed, and versioned. Every ingest becomes an edition, and every edition produces a delta event that names the rows added, changed and deleted. Each record carries its own MCP endpoint, so an agent gets the record and the tools in one address.

The eighteen tools split into three groups.

| Group | Tools |
| --- | --- |
| Shape and sample | `snapshot_schema`, `profile_snapshot`, `sample_snapshot` |
| Read and query | `get_snapshot_rows`, `query_snapshot`, `filter_snapshot_rows`, `search_snapshot`, `download_snapshot`, `download_filtered_snapshot` |
| History and change | `list_editions`, `get_edition_diff`, `get_delta`, `get_delta_rows`, `compare_snapshots` |

`list_records`, `get_record_by_slug`, `get_health` and `list_tools` complete the set. The aggregations run server side rather than in the client, so `query_snapshot` answers a `group_by` over a large record without the model reading every row.

The onboarding path is the part worth noticing. No account is needed to start: `POST /v1/ephemeral/ingest` with a URL returns a session token, and that token is the credential for all eighteen tools for twenty four hours, three ingests and fifty tool calls, with 10,000 rows indexed per record. A record that matters is then claimed and becomes a watched record with a schedule and a delta feed.

## What this pass measured

A driven session against the live endpoint, not a documentation read.

An anonymous ingest of a public business dataset (`https://data.cityofchicago.org/resource/ydr8-5enu.csv?$limit=300&$order=id`) returned a session and a source in one call: `rowCount` **300**, `indexedRows` **300**, `rowsSeen` **300**, `keyField` **id**, `format` **csv**, `tier` **free**, `truncated` **false**, and a first delta of **300** new rows.

`initialize` answered **HTTP 200** with `serverInfo` `catalogian` **1.1.0**, and `tools/list` returned all **18** tools with schemas in 28,237 bytes. `list_records` confirmed the session is scoped to one record and returned the meter: **49** of **50** tool calls remaining, session expiry the next day.

`snapshot_schema` describes the record rather than dumping it: total rows **300**, sampled **100**, and **117** fields each with a null rate, a type hint and example values. `get_snapshot_rows` returned rows as `rowKey` plus `data`, which is the shape a model can cite.

Four calls on the same record, all answered:

- `query_snapshot` with `group_by` on `permit_type` returned the whole distribution in one object: **299** rows in the express permit program and **1** in signs.
- `filter_snapshot_rows` with `contains SIGNS` returned **1** matching row and stated that all matches were shown.
- `search_snapshot` for `electric` returned rows ranked by relevance rather than by position.
- `download_snapshot` **failed**. The presigned export answered `The request signature we calculated does not match the signature you provided`, an S3 signing error on the vendor side, so the export path is broken while the query path works.

The change machinery was then driven with a second ingest of the same record at a different slice (`$offset=100`). It landed on the same record, `ingestCount` moved to **2**, and the delta was exact: **100** new, **100** deleted, **200** unchanged, **300** total. `list_editions` showed edition **1** with `kind: first` and edition **2** with `kind: revision` carrying its own `deltaEventId`. `get_edition_diff` from edition 1 to edition 2 returned row level results with `changeType: new` and the full field set for each row, which is the before and after an operator needs.

One inconsistency is recorded rather than smoothed. `compare_snapshots` on the same two editions answered **Added 100, Removed 0, Modified 0**, while `get_delta` on the same edge answered `deletedCount: 100`. The two tools disagree about deletions, so a deletion test should be run through `get_delta` or `get_edition_diff` until the vendor reconciles them.

## Where it sits in this catalogue

Nothing else here treats a file as a versioned object. [Settra MCP](/hermes/mcp/servers/external/settra-mcp/) is the nearest neighbour and it goes the other way: it syncs Google Sheets, CSV, Excel and Parquet into PostgreSQL behind a semantic layer, so an agent queries governed definitions that a data team approved. That is the right shape when several people share one warehouse. Catalogian is the shape when one operator has one file that keeps arriving, wants to know what changed in it, and does not want to stand up a database to find out.

The distinction matters in practice. Settra answers "what does the approved definition of revenue say". Catalogian answers "which rows in this week's export are not in last week's, and what was the previous value of the field that moved". Those are different questions, and only one of them is about a single file.

## What this pass did not establish

The key field is a closed list, not any unique column. The ingest refused a clean state population CSV with `NO_KEY_FIELD`, naming the accepted keys: `id`, `product_id`, `item_id`, `variant_id`, `sku`, `item_number`, `upc`, `ean`, `gtin`, `isbn`, `asin`, `mpn`. A dataset keyed on a name, an email or a region is not addressable without renaming a column first.

A second defect was met on a vendor sample file. The WooCommerce sample products CSV opens with a byte order mark on its header, and Catalogian took the key field as the BOM prefixed `ID`, then refused the revision with `KEY_FIELD_MISSING` because the established key could not be found in headers that plainly contain it. Files exported from Excel or from a vendor sample can carry that mark, so a failed revision on a file whose columns look correct should be read as a BOM problem, not as a data problem.

Scheduled checks, webhooks and the claimed hourly cadence were not driven, because they need a claimed record and a paid rung. The free anonymous path has no schedule at all: it is a snapshot and a manual revision. The row cap was not reached, so sampling behaviour above 10,000 rows is the vendor's statement. `download_filtered_snapshot`, `sample_snapshot`, `profile_snapshot` and `get_delta_rows` were listed and not called.

## FAQ

### Is it free to try?

Yes, and without an account. One call creates an anonymous record and returns a token that opens all eighteen tools for twenty four hours, three ingests and fifty tool calls, with 10,000 rows indexed.

### What counts as a record?

One source file, CSV, TSV or JSONL, capped at 520 MB per ingest with gzip read directly, keyed on one column, versioned on every ingest. Each record gets its own MCP endpoint.

### Do I need to write SQL to ask a question?

No. `query_snapshot` runs `distinct`, `count`, `group_by`, `min`, `max`, `avg`, `sum` and `filter` server side, and `filter_snapshot_rows` joins conditions with AND. The measured group_by returned one object with every category and its count.

### How do I know what changed since last time?

`get_delta` returns the counts and the keys per event, `get_delta_rows` returns the rows, and `get_edition_diff` returns field level before and after between two editions. On the measured revision the delta was 100 new and 100 deleted against 200 unchanged.

### Does it work in Claude, ChatGPT and Cursor?

Yes. The record page issues a self-contained MCP URL that carries the token, for clients that cannot set an `Authorization` header, and the docs prefer the header where the client supports it.

### What happens when the data does not have one of the accepted key columns?

The ingest fails with `NO_KEY_FIELD` and lists the accepted keys. Rename one column to `id` or `sku` and re-ingest.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [Settra MCP - Governed Tabular Data](/hermes/mcp/servers/external/settra-mcp/) - the semantic layer that turns sheets and files into approved definitions for many users
- [Silicon Floor MCP - AI and Chip Stock Research](/hermes/mcp/servers/external/silicon-floor-mcp/) - the opposite end of the same question: a curated dataset with every figure dated and sourced, rather than a file you brought yourself
