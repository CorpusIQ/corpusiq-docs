---
title: "MCP Server Discovery - November 2, 2026 (Night)"
description: "Night sweep of mcp.so and mcpservers.org: two new servers catalogued with guides, a versioned data record surface and a dilution intelligence surface."
last_updated: 2026-11-02
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november2-2026-night"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 2, 2026 (Night Sweep)

## Summary

Six hours after the evening pass. The mcp.so `recentServers` block carried **30** cards with a date and the newest at `2026-11-02T09:04:11Z`, so exactly **two** sat above the evening stamp of `2026-11-02T01:54:34Z`: `docuwriter-ai` and `signal8`. The mcpservers.org `/all` page behaved as the two previous passes recorded and the counter moved by two, from **18,883** to **18,885**, with `catalogian-mcp` and `opsis-osint/opsis-mcp` at the top.

Two arrivals earned guides. **Catalogian MCP** turns a CSV or JSONL source into a versioned record with its own MCP endpoint and a delta per ingest, and it was driven end to end keyless, including a revision that returned 100 new and 100 deleted rows. **Signal8 MCP** computes what the cap table does next: a dilution pressure score, baby shelf capacity against the live float and a cash runway calendar, over 109 measured tools, and no other guide in this catalogue mentions dilution at all.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| mcp.so homepage `recentServers` | direct, 30 cards with a date | newest `2026-11-02T09:04:11Z`, two above the evening stamp `2026-11-02T01:54:34Z` |
| mcpservers.org `/all` | r.jina.ai, `X-Return-Format: html`, read twice | first read **18,883** (the evening pass counter, stale), second read **18,885** live, 30 slugs |
| Endpoint probes | keyless JSON-RPC | 2 endpoints open on discovery, 2 OAuth 401, 1 open with a working anonymous session |

The two read rule held for a third pass. The first `/all` fetch returned the same counter and the same thirty slugs the evening pass had dispositioned, and the second fetch, cache busted with a nanosecond stamp and a different user agent, returned 18,885 with the page turned over. The read whose counter has moved is the live one.

## New Servers Catalogued

### Catalogian MCP - A Data Record Your Agent Can Question

Relevance: HIGH. **Endpoint driven end to end** (`initialize` HTTP 200, `serverInfo` `catalogian` **1.1.0**, **18** tools listed, and live calls across schema, query, filter, search, editions, delta, edition diff and export).

The product is a **record**: a CSV, TSV or JSONL source from a URL or an upload, keyed on a column, indexed, and versioned on every ingest. Each record ships its own MCP endpoint and eighteen read only tools. Onboarding needs no account: `POST /v1/ephemeral/ingest` with a URL returns a session token good for twenty four hours, three ingests and fifty tool calls, with 10,000 rows indexed.

Measured on a public dataset: **300** rows and **117** fields ingested under key field `id`; `snapshot_schema` returned the types, null rates and example values; `query_snapshot` with `group_by` on `permit_type` returned the full distribution, **299** and **1**, in one object; `filter_snapshot_rows` returned the single matching row; `search_snapshot` returned rows ranked by relevance. A second ingest at a different slice landed on the same record and produced an exact delta of **100** new, **100** deleted and **200** unchanged, which `list_editions` recorded as edition **2** with `kind: revision` and `get_edition_diff` returned at row level with field level values.

It earns a guide because nothing in this catalogue treats a file as a versioned object. [Settra MCP](/hermes/mcp/servers/external/settra-mcp/) syncs sheets and files into PostgreSQL behind a semantic layer and answers what an approved definition says; this answers which rows arrived this week and what value moved, which is a different question about a single file.

Guide: [Catalogian MCP](/hermes/mcp/servers/external/catalogian-mcp/)

### Signal8 MCP - Dilution Intelligence for US Filings

Relevance: HIGH. **Discovery verified** (keyless `initialize` HTTP 200, `serverInfo` `signal8-mcp` **0.19.0**, `tools/list` **109** tools in 221,131 bytes), **calls gated** (seven tools attempted keyless, all JSON-RPC `-32001 Authentication required`).

The slice is what the cap table does next. `get_dilution_coverage` is a cheap precheck, `get_dilution_risk` returns a Dilution Pressure Score from 0 to 100 across seven components, `get_baby_shelf_capacity` recomputes the Form S-3 General Instruction I.B.6 one third of float cap against the live float, and `get_dilution_instruments`, `get_dilution_snapshot` and `get_dilution_history` complete the family. Cash runway, must raise screening, filing text and structure, insider and institutional ownership, and a congressional trading family with profit and loss and FEC donors run beside it.

It earns a guide on a catalogue gap rather than on novelty alone: a grep across all **1,082** guides returns no entry mentioning dilution, baby shelf or cash runway, and the nine EDGAR entries here read what a company reported rather than what can still arrive.

Guide: [Signal8 MCP](/hermes/mcp/servers/external/signal8-mcp/)

## Also Identified (Not Catalogued)

From the mcp.so block, the newest card above the evening stamp besides Signal8 is `docuwriter-ai` (DocuWriter.ai, Developer Tools, **401** with OAuth protected resource metadata on `https://app.docuwriter.ai/mcp`, 77 tools documented over codebase documentation generation, held as developer documentation tooling rather than an operator data surface).

From `/all`, the fresh slugs are all vendors of covered classes: `catalogian-mcp` is the new entry; `opsis-osint/opsis-mcp` is Opsis OSINT, the agent OSINT surface held at the evening pass on the [OpenOSINT MCP](/hermes/mcp/servers/external/openosint-mcp/) precedent, OAuth with three free searches and no new disposition; `testedmcp-com` answers a keyless `initialize` on `https://testedmcp.com/mcp` as `testedmcp` **0.1.0** with read only lookups over **197** installed and handshake tested MCP servers, held as a directory and benchmark fixture, which is this catalogue's own subject; `nexusbro-com` is the NexusBro surface held on **October 31** against eight SEO audit entries; `heritagedeed-com-developers` is the entry catalogued at the evening pass; `shipvo/shipvo` is the Shipvo developer mobile testing hold from **October 31**; `alfa-reza/cvss-calculator-mcp` and the remaining personal handle slugs are listings without a product surface; `nova-civai-co-agent-content-pipeline-agent` scans trends, generates drafts and publishes for one vendor's own products behind a Nova account, held as single vendor product tooling; and `abullycoin-com` serves facts about one meme token on Robinhood Chain, held as consumer crypto.

The `docuwriter-ai` card, `testedmcp-com` and `nova-civai-co-agent-content-pipeline-agent` were read in full before the hold. The submission window on chatmcp/mcpso was outside this run's scope and was not read.

## Core Listing Verification

| Surface | Result |
| --- | --- |
| mcpservers.org `/servers/corpusiq-io` | not re-probed this run |
| Glama and the official registry | not re-probed this run |
| mcp.so four direct slugs | not re-probed this run |

The listing probes are recorded as not run rather than presumed green, and the next pass should re-probe all five surfaces.

## Verification

- Both guides were written against measured responses, not vendor pages. Catalogian was driven across nine tools with a real dataset, a real revision and real deltas. Signal8 was measured at discovery and gated at call time, and the gate is stated in the guide rather than smoothed.
- Two defects are recorded rather than resolved. `download_snapshot` on Catalogian answers an S3 signature mismatch, so the export path is broken while the query path works. `compare_snapshots` reported **Removed 0** on an edge where `get_delta` reported `deletedCount: 100`, so deletions should be read through `get_delta` or `get_edition_diff`.
- A vendor sample file exposed a byte order mark defect: the key field was taken as the BOM prefixed `ID` and the revision was then refused with `KEY_FIELD_MISSING` on headers that visibly contain the column.
- Guide tree counted from disk: **1,082** server directories before, **1,084** after, **1,085** index files under the guide tree.

## Sources

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Catalogian MCP](/hermes/mcp/servers/external/catalogian-mcp/)
- [Signal8 MCP](/hermes/mcp/servers/external/signal8-mcp/)
