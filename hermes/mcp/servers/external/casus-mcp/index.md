---
title: Casus MCP - French Tax and Legal Corpus in Chat
description: "Remote MCP over the French tax and legal corpus: code articles at a chosen date, BOFiP doctrine and 3.4M court decisions, with citation checking built in."
category: Legal and Compliance
stars: n/a (new listing)
added: 2026-10-30
source: "mcpservers.org /all newest page carrying casus-mcp at position 2 and flagged official, whose detail page publishes the server address https://mcp.wearecasus.com/mcp, the volumes as of 18 October 2026, the legal:read scope, the skill resource names and the logging disclosure, plus probes on that endpoint answering HTTP 401 to a keyless tools/list and HTTP 405 to a bare GET"
relevance: ★★★
tags: [legal, tax, france, legifrance, bofip, case-law, citation-checking, oauth, read-only, remote-mcp]
last_updated: "2026-10-30"
---

# Casus MCP

**A legal answer that cites a code article without the version that applied on the date of the facts is not a weaker answer, it is a different and wrong one. Most legal retrieval tools do not model time at all.**

Casus publishes a remote MCP endpoint at `https://mcp.wearecasus.com/mcp` over Streamable HTTP. A keyless `tools/list` answers **HTTP 401** and a bare `GET` answers **HTTP 405**, which is the normal pair for an OAuth-gated Streamable HTTP endpoint that only speaks POST.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.wearecasus.com/mcp
Auth:        OAuth 2, Casus Starter or Pro subscription
Scope:       legal:read (read-only)
Corpus:      230,419 articles across 77 codes, BOFiP, 3.4M+ decisions
Vendor:      Casus (wearecasus.co)
Skills:      5, served as skill:// resources
Call quota:  included per plan, top-up packs available
```

## What it does

The corpus is deliberately specific rather than broad. As of 18 October 2026 the vendor publishes **230,419 articles of 77 codes** from the Légifrance base with their successive versions, the BOFiP administrative doctrine, **more than 3.4 million court decisions** searchable by number or ECLI, tax treaties, and EU law.

Four tool families carry the work:

- `get_code_article` reads a code article in the version applicable to a given date.
- `resolve_references` takes legal citations and returns found, found with a difference, ambiguous, not found, not applicable at the date, or outside the corpus.
- The BOFiP tools read and list administrative doctrine documents by series.
- `search` runs across the whole corpus.

## The date dimension is the reason to care

Asking for an article "as of today" is the easy case and the least interesting one. The hard case is an article as it stood when the facts happened, because French tax and legal questions are routinely decided on a date that moved the rules underneath them.

`get_code_article` takes that date as a parameter rather than pretending the present is the only tense. `resolve_references` then goes further and grades the citation: a reference that exists but whose wording shifted returns as found with a difference rather than as a clean hit, and one that did not exist at the date returns as not applicable at the date.

That grading is the most useful thing in the entry, and it is also a trap for a careless agent. The statuses are not a boolean. Collapsing "ambiguous" and "not applicable at the date" into "not found" throws away exactly the signal a lawyer needs.

## Limits it states about itself

Two self-descriptions deserve to be quoted rather than paraphrased, because both are the kind of honesty that most corpora hide.

The first: a text **absent from the Casus corpus is not a text that does not exist**. The connector says "absent du corpus Casus" rather than answering nothing, which keeps the distinction between an empty result and a negative finding.

The second: code version history is **partial and reaches back mostly to 2025**, so a question about a date before that can return "undetermined at the date". The vendor frames this as deliberate, that the connector does not guess.

An assistant answering a pre-2025 question through this server must therefore surface the uncertainty rather than smooth it. A confident sentence built on an undetermined version is precisely the failure the whole entry exists to prevent.

## What it logs, in the vendor's words

The disclosure is specific enough to quote. One line per tool call records the Casus account identifier, the tool name, the duration, the result, the OAuth client identifier and the call-count state. Some tools add the source consulted and a truncated query.

Semantic search queries pass through Casus's search service to Voyage AI for embeddings and reranking and to Pinecone for the index, which is worth knowing before you paste a confidential client question into `search`. The other tools query the corpus database directly. The connector does not read your Casus conversations or your documents, and the logging lines may be forwarded to Better Stack.

The call-counting service receives the call identifier, your identifier, the tool name, the OAuth client and the outcome, but no tool arguments: no query text, no document identifiers.

## Why it belongs in this catalogue

The legal entries already here split by jurisdiction and by shape. The US retrieval and formation entry is American; the EU grounding entry is European but generic across member states. Neither covers a **national** corpus with versioning and administrative doctrine attached.

That combination is the new slice: a country's codified law, its administrative interpretation, and its case law in one index, with the temporal axis as a first-class parameter and a citation checker on top. For a French business, that is the difference between an assistant that can find a rule and one whose references survive a reviewer.

## What this pass did not establish

`tools/list` needs a token, so the tool names above come from the vendor's published documentation and not from a list this pass drove. Two things a trial should settle: whether `resolve_references` returns per-citation statuses in a machine-readable shape an agent can branch on, and whether the call quota is a hard stop or a soft warning, because a legal workflow can burn through tool calls quickly on a long document.

## FAQ

### Does it work without a Casus subscription?
No. It needs a Casus Starter or Pro subscription, either personal, on trial, or through a subscribed organisation. A cancelled subscription cuts connector access.

### Is it read-only?
Yes. The granted scope is `legal:read` and the connector states it cannot modify anything in your account.

### Which clients can connect?
Claude through Settings then Connectors with a custom connector, Claude Code with `claude mcp add --transport http`, and ChatGPT through Plugins and Add custom MCP server. Any MCP client that speaks Streamable HTTP over OAuth works.

### How far back does the law version history go?
Partially. The vendor says history reaches back mostly to 2025 and that earlier dates can return "undetermined at the date" by design, rather than a guess.

### Does it read my own documents?
No. It queries the Casus public corpus only, not your conversations or your uploaded documents.

## See Also

- [Kvasir Legal MCP - EU Law Grounding for AI Agents](/hermes/mcp/servers/external/kvasir-legal) - EU-level grounding rather than a national corpus
- [Corpus Law MCP - US Legal Search and Business Formation](/hermes/mcp/servers/external/corpus-law-mcp/) - the same retrieval shape for the United States
- [Taiwan Law MCP - Official-Source Taiwan Legal Research](/hermes/mcp/servers/external/taiwan-law-mcp) - another single-jurisdiction corpus, without the date axis