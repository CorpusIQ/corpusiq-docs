---
title: "SplitScanner MCP - Reverse Splits With the Filing Attached"
description: "A keyless tools/list returned 24 read-only reverse-split and SEC filing tools; a tool call needed a subscription: what each surface answers"
category: "Finance and Compliance"
stars: "not applicable (hosted service)"
added: 2026-11-12
source: "the submission queue entry #7187 filed 2026-11-12T08:23Z, the official registry records com.splitscanner/mcp 0.19.0 and 0.19.1 declaring the same remote, the vendor's AI-agents page read the same day, and a live session on this host: initialize, tools/list and one tools/call request against https://mcp.splitscanner.com/mcp"
relevance: ★★★
tags: [finance, reverse-split, sec, filings, compliance, small-cap, corporate-actions, mcp, remote]
last_updated: "2026-11-12"
---

# SplitScanner MCP

**A reverse split is announced, the ratio is repeated in three places, and the number that matters is the one in the filing.** Between the board resolution, the shareholder vote and the effective date, the same event changes shape; a ticker that split once is far more likely to split again, and the exchange listing standard behind the split is usually the reason it happened at all. SplitScanner serves that record as **24 read-only tools**, each row carrying the SEC filing or exchange notice it came from.

```text
Server type:  remote Streamable HTTP, discovery-open and execution-gated
Endpoint:     https://mcp.splitscanner.com/mcp
Server:       splitscanner-mcp 0.20.0 (serverInfo), protocol 2025-03-26
Capabilities: tools (listChanged: true)
Tools:        24 measured keyless; tools/call answered 401
Registry:     com.splitscanner/mcp 0.19.0 and 0.19.1, both declaring this remote
Access:       a SplitScanner subscription or Signal8 Pro, signed in through the client
Probe:        initialize and tools/list keyless, then one tools/call
```

## The evidence tier, stated plainly

`initialize` returned **200** with no credential, reporting `splitscanner-mcp` **0.20.0** and an instruction block that describes the product as read-only reverse-split research for US-listed companies: the upcoming calendar with each split's stage, approval route and board authority, ended and abandoned splits, split history, price moves after past splits, float, and the exchange listing standards behind many splits. `tools/list` returned **200** with all **24** tools and their schemas.

Then `tools/call` on `get_upcoming_reverse_splits` answered **401** with JSON-RPC error `-32001 Authentication required`. The call carried no `WWW-Authenticate` header, so a client gets the verdict without the OAuth discovery path that would take it to a sign-in; the vendor's own page is where the subscription requirement is stated, and a client configured for OAuth resolves it when the user signs in.

So the tool surface is measured here and the answers are not. Everything below about what the tools return is the vendor's description or the schema, labelled as such, and the schema is unusually informative for a paid surface.

## The 24 tools, grouped

```text
company      search_companies, get_company_profile, get_quote, get_float,
             get_float_history
splits       get_split_history, get_split_performance, get_upcoming_reverse_splits,
             get_reverse_split_lifecycle, get_ended_reverse_splits,
             get_reverse_split_authority, get_reverse_splits_list
filings      search_sec_filings, get_filing_documents, get_filing_document,
             get_filing_exhibits, get_exhibit_content, search_filing_text,
             lookup_accession_number
standards    get_compliance (exchange listing standards for a ticker)
learning     search_learn_guides, get_learn_guide, define_term
coverage     get_signal8_pro_coverage
```

Every tool is annotated `readOnlyHint: true`. The schema shows the shape of the two strongest ones. `get_reverse_split_lifecycle` takes a ticker and returns the path from proposal to effect, which is the question a shareholder actually asks when a proxy arrives. `get_reverse_split_authority` takes `minRemaining` and `expiringBefore`, so a caller can ask *which companies hold unused split authority that expires soon* - a question that requires dates and an authority grant to be stored as fields rather than described in prose. `search_sec_filings` accepts a wide filing filter (form types, exclusions, items, date range, market cap, float, price, sectors, exchanges, company types, foreign issuer, recent IPO) and `search_filing_text` searches within documents with a snippet length and an optional section scope, which makes the citation claim checkable rather than decorative.

## What the vendor states

From `splitscanner.com/ai-agents`, read on 2026-11-12, the server answers four operator questions: which reverse splits are scheduled this week with the ratio and effective date of each; a ticker's split history and whether it is a repeat splitter; how a stock moved in the 30 days after its last reverse split; and which splits were approved with no date yet or failed a shareholder vote. The page states the limits in the vendor's own words - **scheduled is not confirmed**, **a missing value is not measured**, and nothing here is investment advice - and the data source is public filings and exchange data, which the vendor says can be late or wrong.

A note on versions, because it is the kind of drift worth recording: the registry carries **0.19.0** and **0.19.1** while the served `serverInfo` reports **0.20.0**, so the registry record lags the deployment. Neither figure is a statement about data quality; the `asOf` fields inside the answers would be, and those were not reachable without a subscription.

## Why it earns a page

Most reverse-split content on the open web is a list with a date. The operator question is different and sharper: is this split forced by a listing minimum, how much authority is left, and what happened to the last five companies that did the same thing. Those are three fields and a citation, and this is the first entry here that carries them together, next to [SEC EDGAR MCP](/hermes/mcp/servers/external/sec-edgar-mcp/), which searches the same filings without the split model on top.

### Do I need a subscription to see the tools?

No. `initialize` and `tools/list` answered **200** keyless and returned all 24 tools; only `tools/call` required authentication, answering **401** with JSON-RPC `-32001`.

### Does it recommend whether to buy or sell?

No, and the vendor says so twice - the data is information only and can be late or wrong. What it does carry is the provenance: the SEC filing or exchange notice behind each row, so a claim can be checked at the source instead of trusted from a summary.

### Is the split calendar a confirmation?

No. The vendor's own limit line says **scheduled is not confirmed**, which is the correct reading of a corporate action between the vote and the effective date.
