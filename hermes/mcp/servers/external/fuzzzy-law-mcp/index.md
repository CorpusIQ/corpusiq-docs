---
title: "Fuzzzy Law MCP - Georgian Statutes With Source Links"
description: "Twelve keyless tools over 24 Georgian codes and 6,517 articles plus 8,473 court decisions, each answer carrying its matsne.gov.ge link and version date."
category: "IP/Legal"
stars: n/a (vendor-hosted)
added: 2026-11-21
source: "chatmcp/mcpso submission #7774 filed 2026-11-21T17:58:51Z; the official MCP registry record com.fuzzzycore.law/georgian-law 1.0.0 published 2026-11-21T17:57:58Z; keyless initialize and tools/list, then fifteen tools/call requests on 2026-11-21"
relevance: ★★★★
tags: [legal, georgia, legislation, court-decisions, open-data, remote-mcp, keyless]
last_updated: "2026-11-21"
---

# Fuzzzy Law MCP

**Remote MCP server (Streamable HTTP, no authentication)** - the exact current text of 24 Georgian codes and laws, article by article, with the official matsne.gov.ge link and the version date on every answer, plus 8,473 published decisions of the Supreme Court and the Constitutional Court of Georgia.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://law-api.fuzzzycore.com/mcp
Tools:       12 (read-only)
Registry:    com.fuzzzycore.law/georgian-law 1.0.0
             (active, published 2026-11-21T17:57:58Z)
Server:      fuzzzy-law 1.1.0
Homepage:    https://law.fuzzzycore.com  (English at /en/)
Repository:  https://github.com/fuzzzy-bot/fuzzzy-law (MIT)
Source:      matsne.gov.ge, the Legislative Herald of Georgia
Freshness:   every response carries data_current_as_of
```

## Why This Matters for Operators

Any company with Georgian staff, a Georgian entity, Georgian customers or a Georgian counterparty argues about what the law actually says, and the usual answer is a PDF with no version date or a blog post that paraphrases. This server answers with the article, its official link, the version date and the date the copy was checked.

The design choice worth noticing is that the server never pretends to be a lawyer. Every response repeats that this is law text and its source, not legal advice, and the citation tool refuses to rule on whether a claim is supported: it reports word overlap and hands back the text.

- **24 codes and laws, 6,517 articles** - the civil, civil procedure, criminal, criminal procedure, administrative, administrative procedure, tax, labour, customs, election and enforcement codes, the constitution, and single-topic laws on personal data, domestic violence, consumer rights, patient rights, entrepreneur activity, social assistance and state pensions.
- **Earlier wordings back to about 2016** - several thousand stored versions behind the current text, so a question about a past event can be answered against the version in force at that time.
- **8,473 published decisions** - 8,116 Supreme Court, 328 Constitutional Court and 29 Supreme Court Grand Chamber decisions, with case number, court, date and a passage-level link.

## Tools & Capabilities

Twelve read-only tools were listed keyless on 2026-11-21.

| Tool | What it returns |
|---|---|
| `list_codes` | the 24 codes with article counts, official links and version dates (`codes` key) |
| `get_coverage` | what is held, what is not, court collections with counts and date ranges (`laws` key) |
| `search_law` | article search restricted to one code or across all, Georgian terms |
| `get_article` | one article in full, with paragraphs, official link, version date and a `paragraph` argument |
| `list_changes` | articles amended, added or removed since a date |
| `browse_code` | a code's chapters, or the article list of one chapter |
| `find_court_practice` | decisions by issue, with case number, court, date, snippet and link |
| `get_court_decision` | one decision in full, twenty passages per call |
| `verify_citation` | whether an article and paragraph exist, whether it is repealed, and the text itself |
| `find_legal_aid` | where a person in Georgia gets free legal help, with phone and hours |
| `search` | articles and decisions together, returning ids and links |
| `fetch` | the full text, link and version details behind a `search` id |

## Measured Behaviour

Fifteen `tools/call` requests were driven keyless on 2026-11-21. Every figure below is quoted from a response.

| Call | Arguments | Result |
|---|---|---|
| `list_codes` | none | **24** codes and laws, **6,517** articles in total |
| `get_coverage` | none | court collections: Supreme Court **8,116** (2004-11-18 to 2026-06-16), Constitutional Court **328** (1996-10-30 to 2026-06-24), Grand Chamber **29** (2001-09-27 to 2017-03-02) |
| `browse_code` | `civil_code` | chapters with article ranges, from *physical persons* (14 articles, art. 11-23) onward |
| `list_changes` | `civil_code`, since 2026-01-01 | articles amended in 2026, each with its own `version_url` |
| `get_article` | `labour_code`, `მუხლი 12` | *Conclusion of a labour contract*, version date **2026-09-16**, official link `matsne.gov.ge/ka/document/view/1155567#part_129` |
| `search_law` | `შრომითი ხელშეკრულება` | matched articles with per-article version dates |
| `search_law` | `employment contract termination` | `found: false`, with the instruction to search in Georgian |
| `verify_citation` | quote from art. 12 | `exists: true`, `is_repealed: false`, full text returned |
| `verify_citation` | a fabricated notary clause | `exists: true`, `lexical_check` **5 of 6** terms found, and the message *"The article exists. Compare the claim with the text before relying on it."* |
| `verify_citation` | `მუხლი 9999` | `exists: false`, *"It may not exist; do not cite it."* |
| `find_court_practice` | `შრომითი ხელშეკრულება` | case `ას-1343-1263-2017`, Supreme Court, **2017-12-20**, with snippet and passage |
| `find_legal_aid` | none | the state Legal Aid Service on **1485** (or 032 292 00 55), working days **10:00-18:00**, free consultation for everyone and a free lawyer for registered socially vulnerable applicants |

### The citation tool that declines to rule

`verify_citation` is the honest answer to the question every legal tool dodges. On the fabricated claim *"a labour contract is concluded only in notarial form"* against article 12 it returned the real article, marked `exists: true`, and reported only that five of six claim terms appear in the text. It did not say the claim was wrong, because it cannot: it says so itself - *"Word and number overlap only. This is not a legal judgement; read the text."*

That is the correct division of labour for an agent. The tool supplies the authoritative text and the date; the model reads it; the human signs off.

## Installation

No credential, no account, no key.

```json
{"mcpServers":{"fuzzzy-law":{"type":"http","url":"https://law-api.fuzzzycore.com/mcp"}}}
```

```
claude mcp add fuzzzy-law --transport http https://law-api.fuzzzycore.com/mcp
```

## Business Relevance

- **Georgian exposure, answered with a citation.** Payroll, employment contracts, personal data, tax and enforcement questions that previously went to outside counsel as a research request can be grounded in the article text with its version date.
- **Point-in-time questions.** A dispute about a 2021 dismissal needs the wording in force in 2021, not today's. The `as_of` argument and the stored earlier versions make that a single call.
- **Court practice beside the statute.** Whether an article has been applied, and to what effect, is a `find_court_practice` call on the same surface.
- **A referral path when the answer needs a lawyer.** `find_legal_aid` returns the state service, the Public Defender and other providers with phone numbers and hours.

## Integration with CorpusIQ

An operator already asking CorpusIQ about a Georgian entity, supplier or hire can attach this server and have the law-question answered from matsne.gov.ge text rather than model memory. The pairing that matters is citation discipline: CorpusIQ answers carry sources, and this server supplies the source of record with a version date, so a legal statement in a business answer can be traced to the article that says it.

## Limitations

- **Georgian text, Georgian search.** `search_law` with English terms returned nothing and asked for Georgian legal terms. There is no English corpus behind it.
- **24 laws, not all Georgian law.** Government and ministerial orders, municipal acts, subordinate legislation, and district and appeal court decisions are explicitly listed as not held.
- **Court collections are a selection.** The Supreme Court publishes a selection, not every decision, and the server says so in its own coverage document.
- **No legal judgement.** `verify_citation` reports existence, repeal status and word overlap only.
- **Field-name drift between two tools.** `list_codes` returns its array under `codes` while `get_coverage` returns the same 24 instruments under `laws`; a parser that assumes one key silently reads zero.
- **A missing required argument returns a validation error** in band (`isError: true`) rather than a friendly message, so clients that render only `content` see nothing.

## FAQ

### Does it hold the law as currently in force, or a snapshot?

Both. The current consolidated version is stored article by article with its version date, and earlier wordings back to about 2016 are kept, so a past event can be read against the wording that applied then.

### How fresh is the text?

Every response carries `data_current_as_of`, which read `2026-11-21` on this pass, and each law carries its own `version_date`. The submission states each law is compared with matsne.gov.ge nightly and replaced only after a word-for-word check.

### Can an agent use it as legal advice?

No, and the server says so on every response. It provides the article text, the official link and the version date; advice, and the decision, stay with a qualified lawyer, and `find_legal_aid` points to free help in Georgia.

### Does it need an API key?

No. `initialize` and `tools/list` answered 200 keyless, and fifteen `tools/call` requests were driven with no credential.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Legalize MCP - Point-in-Time Legislation with Git Provenance](/hermes/mcp/servers/external/legalize-mcp)
- [CourtListener MCP - US Legal Research for Agents](/hermes/mcp/servers/external/courtlistener-mcp)
- [Taiwan Law MCP](/hermes/mcp/servers/external/taiwan-law-mcp)
