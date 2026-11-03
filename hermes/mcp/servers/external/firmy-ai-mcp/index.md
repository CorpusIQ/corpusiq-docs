---
title: "firmy.ai MCP - A Polish Company Dossier Without an Account"
description: "Free keyless KRS registry access: financial statements, boards, sanctions across EU and MSWiA lists, public tenders, and market-wide revenue rankings for Polish companies."
category: Finance / Company Data
stars: ★★★ (keyless, 8 tools listed, 6 called live)
added: 2026-11-03
source: "the mcpservers.org /all newest page at position 5 of 30 as firmy.ai, and a driven keyless session on https://firmy.ai/mcp on 2026-11-03: initialize HTTP 200 as firmy.ai 1.0.0, tools/list returning 8 tools, and live calls to get_account, search_companies, get_company (twice, one rejected on a bad section name), and rank_companies on revenue, margin and Altman"
relevance: ★★★
tags: [company-registry, poland, krs, financial-statements, sanctions, tenders, vat, due-diligence, keyless, remote-mcp]
last_updated: "2026-11-03"
---

# firmy.ai MCP

**A supplier sends an invoice from a Polish entity. Before paying it you want three things that live on three different government sites: the company's filed accounts, whether it appears on a sanctions list, and whether it actually exists on the VAT white list. Each site has its own identifier format, its own captcha and its own definition of the company's name. The cost is not the lookup, it is assembling four registries into one answer you would sign.**

```
Server type:  Remote (Streamable HTTP), text/event-stream responses, Cloudflare
Endpoint:     https://firmy.ai/mcp
Auth:         none in free mode, no key, no account
Server info:  firmy.ai 1.0.0, protocol 2025-06-18
Tools:        8
Sections:     22, each with its own ready or missing state
Identifiers:  KRS (10 digits), NIP (10), REGON (9 or 14), a firmy.ai URL, or p- person id
Language:     Polish output; English query terms are accepted
```

## What it does

firmy.ai is a merged view of the Polish business registers, served over MCP with a free mode that needs no account. The server has two modes, and it tells you which one you are in rather than failing quietly. Free mode reads what the service already knows: the KRS record, its cache, the free KRS API. A section it has never fetched comes back with `status: "missing"` and `error_code: "AUTH_REQUIRED"` instead of a silent gap. Pro mode, still marked unavailable, would fetch missing sections on demand at up to 40 operations per call with `estimate: true` priced before it runs.

The eight tools split into search, dossier, screening and ranking:

| Tool | What it does |
| --- | --- |
| `search_companies` | Name, NIP, KRS or REGON search with city filter and paging |
| `search_persons` | People in the KRS by first and last name, with a connection count |
| `get_company` | One company dossier, sections selected by `include` |
| `get_person` | One person: roles, shareholdings, co-managed companies, sanctions |
| `list_companies` | Browse 100 per page by city, PKD division, legal form or initial |
| `rank_companies` | Rank the market by revenue, profit, growth, margin or Altman Z |
| `refresh_company` | Invalidate the cached page and reload it with statements |
| `get_account` | Which mode you are in, and how the server expects to be used |

## What this pass measured

Every figure below came from a live keyless call on 2026-11-03. `get_account` returned `mode: "free"`, `authenticated: false`.

**Search.** `search_companies {query: "CD Projekt", limit: 3}` reported 10 matches for the name. The three returned carried KRS, NIP, city, legal form and status: `0000006865` CD PROJEKT RED SPÓŁKA AKCYJNA, active; `0000096654` and `0000521325`, both `deregistered`. Status is on every row, so a search for a group name does not hand back three entities as if they were one.

**The dossier.** `get_company {id: "0000006865"}` resolved the identifier type itself (`id_resolved: {type: "krs", value: "0000006865"}`) and returned the profile: NIP 7342867148, REGON 492707333, entered 2001-04-06, last entry 2026-08-10, share capital 99,910,510 PLN, PKD 62.10.A, registered office Jagiellońska 74 in Warsaw, 14 people in management, 29 documents on file.

The `available` map is the feature worth copying. Every one of the 22 sections carries a state before you ask for it: `sanctions` ready, `tenders` ready, `financials` ready with a count of 1 period, `documents` ready with 29, `beneficial_owners` missing, `vat` missing, `bankruptcy` missing. An agent that reads the map does not spend three turns guessing.

**Financials, 2024, from the filed statement.** Revenue 985,030,000 PLN against 1,230,199,000 the prior year, a fall of 19.9 percent. Net income 469,874,000 PLN. EBITDA 379,785,000. Net margin 47.7 percent, EBITDA margin 38.56 percent. The document years on file are 2024, 2023 and 2022. Balance-sheet fields return null on this source, so ROE, ROA, the current ratio, debt to equity and the Altman Z come back null with them. That is honest behaviour from a filing reader rather than a scoring engine pretending.

**Screening, dated.** `sanctions` returned `found: false`, `verdict: "clear"`, lists `eu` and `mswia`, `as_of: 2026-11-03`, which is the day of the call and not the day of the registry cache. `tenders` returned `found: false` since 2024-02-01 across `bzp` and `ted`, also `as_of: 2026-11-03`. Two sections priced like compliance checks are live while the profile is cached, and the response says which is which on every section.

**What free mode will not give you.** `vat` and `beneficial_owners` came back `AUTH_REQUIRED`. The VAT white-list lookup needs Pro mode. The beneficial-owner section from the CRBR register needs a logged-in account with a declared purpose, and the hint says so in plain language rather than implying the data does not exist. For any supplier where the true owner matters, that is the wall to know about before you promise an answer.

**Market screening.** `rank_companies {metric: "revenue", limit: 5}` returned ORLEN at 294,976,000,000 PLN, Jeronimo Martins Polska at 101,987,368,889, Totalizator Sportowy at 52,248,125,432.71, Polskie Sieci Elektroenergetyczne at 27,127,834,461.33 and Dino Polska at 25,658,552,000. A revenue league table over the whole register, keyless, is a market-sizing input that no other entry here provides for Poland.

## Two defects the drive found

**The ratio rankings are unbounded.** `rank_companies` on `margin` returned a top five of 3,569,778.83 percent, 1,231,818.17 percent, 1,032,032.58 percent, 808,208.63 percent and 794,595.35 percent net margin. `altman` returned 33,576.07, 3,393.6 and 1,037.62 points. These are ratio artefacts from tiny or near-zero denominators, and they sit above every real company in the market. A revenue or profit ranking is usable as printed. A margin or Altman ranking needs a revenue floor and a positivity filter before it is read as a screen, and the tool has neither. The workaround is a two-step: rank by revenue into a set, then read ratios on the members.

**REGON is null in search results but present on the dossier.** Every row returned by `search_companies` carried `regon: null`, while `get_company` on the same KRS returned REGON 492707333. Anything that builds a key from search output will propagate a null it did not have to.

A third behaviour is worth recording because it is the good kind of strict. Passing an invented section name returned `isError: true`, `code: "INVALID_INPUT"`, a hint listing all 22 valid sections, and a `suggested_call` with the corrected arguments. A wrong guess costs one round trip, not a dead end.

## What to ask it

- "Dossier on this Polish supplier: filed accounts, board, sanctions, tenders. What is not checkable on the free tier?"
- "Is this NIP on any sanctions list, and as of what date?"
- "Who sits on the board of this company, and do any of them manage competitors?"
- "Rank Polish companies by revenue in this PKD division and give me the top twenty."
- "Which sections of this company's record are missing, so I know what I could not verify?"

## The limits this guide will not paper over

- **Output is Polish.** Names, roles, section text and the AI-written description all come back in Polish. An English query is accepted; the answer is not translated.
- **Free mode is a cache, not a live registry.** The profile carried `as_of: 2026-08-10`. Screening sections were dated the day of the call. Treat the profile as a snapshot with a date on it.
- **Balance-sheet ratios are null on the RDF statement source.** If you need ROE, leverage or the Altman Z for a specific company, check the section state before promising it.
- **No PESEL, no dates of birth.** The person surface returns public roles and connections only, and the server states this.
- **VAT and beneficial ownership need an account with a declared purpose.** That is a legal boundary around the CRBR register, not a paywall the vendor invented.
- **AI-written text is labelled.** Descriptions, valuations and biographies carry `ai_generated: true` and a citation list. Treat the citations as the source and the prose as a draft.

## Where this sits in the catalog

Poland is the thin spot in this catalogue's registry coverage. [company-atlas-mcp](/hermes/mcp/servers/external/company-atlas-mcp/) reads eight markets and Poland is not one of them. [UK Companies House](/hermes/mcp/servers/external/uk-companies-house-mcp/) and [registry-mcp](/hermes/mcp/servers/external/registry-mcp/) (Norway) are single-jurisdiction. [Prometiam Risk MCP](/hermes/mcp/servers/external/prometiam-risk-mcp/) covers thirteen European countries including PL and is the closest neighbour, but its Polish financial statements sit on the paid Scale tier and its sanctions screening starts at the Starter tier.

firmy.ai earns a guide on the combination rather than on novelty: a full dossier with filed statements, two sanctions lists, public tenders from BZP and TED, an officer list, and market-wide ranking, free and keyless, with the state of every section declared before it is asked for. For an operator with Polish suppliers or a Polish entity, that is the difference between four registry sites and one query. The Catalogue held Compabase on the geo-niche class in an earlier pass; the reason this one is catalogued is that it was driven and returns dated screening rather than a listing claim.

## Verification

```
https://firmy.ai/mcp         initialize    HTTP 200, firmy.ai 1.0.0, SSE
                             tools/list    8 tools
                             get_account   mode free, authenticated false
                             search_companies
                             get_company x2 (one INVALID_INPUT, by design)
                             rank_companies x3 (revenue, margin, altman)
```

No key, no account, no sign-in. All on 2026-11-03, from a clean client.

## FAQ

### Is the free mode a trial?
The server describes it as a mode, not a trial: it reads what the service already holds and never fetches on demand. Pro mode, which does fetch on demand, is marked as not yet available at the time of this pass.

### Does it work for UK or US companies?
No. It is the Polish registers: KRS, the VAT white list, the CRBR beneficial-owner register, BZP and TED tenders. For those other markets use the entries linked above.

### How fresh is the cache?
The profile page carried `as_of: 2026-08-10`, while the sanctions and tender sections reported `as_of: 2026-11-03`. Read the date on the section you are quoting.

### Why are the margin rankings wrong?
The ranking applies a ratio across the whole register with no revenue floor, so companies with near-zero denominators produce absurd percentages and sort to the top. Rank by revenue or profit, or impose your own floor on the returned set.
