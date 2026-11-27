---
title: "WikiVectors MCP - Cited Wikipedia Paragraphs for Grounding"
description: "Five tools over live English Wikipedia: paragraphs with link, revision id and licence, plus page watches and a change feed, keyed at 1,000 free a month."
category: "Knowledge"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-27
source: "mcp.so submission queue issue #8225 filed 2026-11-27T09:44:43Z; official registry com.wikivectors/search; keyless initialize 200 as wikivectors 1.0.0 on protocol 2025-06-18 and a keyless 5-tool tools/list at https://wikivectors.com/mcp on 2026-11-27, with four tools/call attempts answering 401 missing_api_key; pricing, call units and result fields read from https://wikivectors.com/docs the same day"
relevance: "★★"
tags: [knowledge, wikipedia, search, grounding, citations, rag, change-monitoring, remote-mcp]
last_updated: "2026-11-27"
---

# WikiVectors MCP

**An assistant that answers from memory cannot show its work, and Wikipedia is the one corpus where showing the work is possible: every paragraph has a permanent revision id and a licence that permits reuse with attribution.** WikiVectors exposes that corpus as five MCP tools and returns, for each paragraph, the page link, the exact revision behind the text, and the licence line, so an answer can cite a version rather than a page that may have changed since.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://wikivectors.com/mcp
Registry:     com.wikivectors/search
Auth:         Authorization: Bearer wv_live_...   (free key, 1,000 searches a month, no card)
Discovery:    initialize 200 and tools/list 200 without a key; tools/call 401 without one
REST mirror:  https://wikivectors.com/v1/search
Tools:        5
```

`initialize` answers **200** at protocol **2025-06-18** as `wikivectors` **1.0.0** with no credential, and the `instructions` block tells the client how to use it: *"Use search_wikipedia for facts, get_pages when you know the page names, or answer_question for a short cited answer. Quote the returned text and cite its url; text is CC BY-SA 4.0. Use watch_page to get a callback when a page changes, or changes_since to poll for changes."* That is an unusually explicit grounding contract, and it is the reason this server is worth a guide rather than a line.

## The five tools

Read from a keyless `tools/list`:

| Tool | What it does | Call units |
|---|---|---|
| `search_wikipedia` | Keyword plus meaning search over current English Wikipedia, returning short citable paragraphs | 1 |
| `answer_question` | The shortest accurate answer, then one to three sentences with numbered citations | 5 |
| `get_pages` | Up to 20 pages by exact title in one call, following redirects ("JFK" gives "John F. Kennedy") | 1 per title |
| `changes_since` | Edits, moves and deletes since a time, oldest first, with diff links, narrowable to 50 pages | 1 |
| `watch_page` | A signed JSON callback POSTed to your HTTPS URL each time a page is edited, moved or deleted | free |

The pricing is per unit and published, which is rare among knowledge servers: **1,000** searches a month free with no card, then **$2 per 1,000** from prepaid credits bought at **$10** that never expire and are spent only after the free allowance, with a **$1 per 1,000** volume rate above a million a month. An `answer_question` costs **5** units and a **watch is free**, so monitoring a page is cheaper than asking about it.

## What a result carries

The vendor's own captured example for a search on the northern lights returns an object per hit with `title`, `section`, `text`, `url`, `permalink`, `license`, `description`, and then the envelope fields `mode: "hybrid"`, `index_synced_at` and a `request_id`:

```
"url":       "https://en.wikipedia.org/wiki/Aurora"
"permalink": "https://en.wikipedia.org/w/index.php?oldid=1382287719"
"license":   "CC BY-SA 4.0"
"index_synced_at": "2026-11-26T00:19:12Z"
```

**The `permalink` with an `oldid` is the field that matters.** It pins the paragraph to a revision, so a citation stays checkable after the page moves on, and the `license` line travels with the text instead of being a footer an assistant forgets. A client that quotes `index_synced_at` as the page date is quoting the index batch time rather than the revision, which is why the permalink is the datum to cite.

## What this pass could and could not drive

Honest limits, measured:

- **Read keyless:** `initialize` (200) and `tools/list` (5 tools, with full descriptions and the instructions block quoted above).
- **Refused keyless:** four `tools/call` attempts, on `search_wikipedia`, `answer_question`, `get_pages` and `changes_since`, each answered **401** with `{"error": {"code": "missing_api_key", "message": "Send your key as: Authorization: Bearer ... (get one at https://wikivectors.com/#get-key)", "request_id": "..."}}`. The refusal is clean, names the fix and returns a request id.
- **No payload was driven.** Every figure in this entry is the vendor's own published documentation, read on 2026-11-27; the key is free but issuing one requires an email, which this pass does not do on a vendor's behalf.

## Why a citation-pinned source is worth carrying

- **Grounding with an audit trail.** A paragraph with a revision id can be re-read by a sceptical colleague in six months and still be the same text.
- **Answer refusal is a feature.** `answer_question` is documented to say "no answer" rather than guess, which is the behaviour a business answer needs when the corpus is silent.
- **Change monitoring is priced at zero.** A watch posts a signed JSON callback on every edit, move or delete, so a page that matters to a process can notify rather than be polled.
- **Licence clarity.** CC BY-SA 4.0 travels in the payload, so attribution is a formatting decision rather than a legal question.

## Frequently asked questions

### Is any of it usable without an account?

Discovery is: `initialize` and `tools/list` answer with no credential, so a client can inspect the surface before anyone signs up. Every tool call needs a `wv_live_` key however, so a "keyless" reading of this server is true of the card and false of the calls.

### English Wikipedia only?

Yes. Every tool description says English Wikipedia, and the vendor's own product page scopes the corpus the same way. A multilingual answer needs another source.

### How fresh is the text?

Pages are stated to be updated from live Wikipedia edits within the hour, and each response carries the revision behind the text. For anything where being current matters, cite the `permalink` and treat the index timestamp as a separate fact.

### What does it cost at volume?

**1,000** units a month free, then **$2 per 1,000** prepaid, dropping to **$1 per 1,000** above a million a month on the vendor's volume tier. Searches, change queries and each page title cost **1**; an answer costs **5**; watches cost nothing.

## See also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
