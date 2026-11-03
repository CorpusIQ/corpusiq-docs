---
title: "DFX Intelligence MCP - Private Credit With Citations"
description: "Private markets answers from BDC and SEC filings: lenders, facilities, marks, maturities and allocator commitments, each claim carrying its filing."
category: Finance and Private Markets
stars: ★★★ (keyless driven, 20 tools, 6 called live, paid tiers withhold names)
added: 2026-11-03
source: "the chatmcp/mcpso submission #6666 filed 2026-11-03T12:01:31Z, a keyless driven session on https://exchange-production-9123.up.railway.app/mcp/core?c=dir-mcpso with 20 tools listed and 6 called live, and the Ares Capital schedule of investments behind accession 0001628280-26-067383"
relevance: ★★★
tags: [private-credit, bdc, sec-filings, private-equity, allocators, ria, venture, real-estate, citations, remote-mcp]
last_updated: "2026-11-03"
---

# DFX Intelligence MCP

**A lender asks who else is in the deal, at what spread, and when it matures. The answer exists, in a schedule of investments filed by each business development company every quarter, and assembling it by hand means reading the same borrower across a dozen filings and reconciling three spellings of its name. This server does that reconciliation and hands back the rows with the accession number attached.**

```
Server type:  Remote (Streamable HTTP, JSON responses)
Endpoint:     https://exchange-production-9123.up.railway.app/mcp/core?c=dir-mcpso
Auth:         none for reads, optional account key for watch tools
Tools:        20 listed, 6 called live in this pass
Version:      0.16.0, serverInfo name dfx-real-estate, title DFX Intelligence
Protocol:     2025-06-18
Registry:     referenced in the submission, not re-probed here
Access tiers: anonymous screen depth, then a 7 day trial, then paid plans
```

## What it does

The server is a read interface over a graph of private capital: private credit, real estate, family offices, independent sponsors, venture capital, private equity, registered investment advisers and public pension allocators. One tool, `research`, takes a whole question and plans the reads it needs, then answers from the rows it read. The other nineteen are those reads, exposed singly for drilling into any row.

| Tool | What it returns |
| --- | --- |
| `research` | One question in one call: resolved entities, a direct answer built only from cited claims, coverage limits, what the tier withheld, paged claim rows |
| `what_can_dfx_answer` | A plain objective in, the domain that answers it out, with the arguments and a free sample |
| `resolve_name` | A firm, fund, person or company name to canonical ids across every graph, with the roles that matched |
| `search_entities`, `get_entity` | Search by name or filter, then everything held on one id with relationships, dates and sources |
| `search_relationships`, `relationship_path`, `get_capital_paths` | Who employs, manages, lends to, invests in or owns whom, and the evidence-backed path between two ids |
| `changes_since` | What the graph learned since a time, driven by first sight rather than by filing date |
| `verify` | A claim in, `SUPPORTED`, `PARTIALLY_SUPPORTED`, `CONTRADICTED` or `UNKNOWN` out, with the evidence rows |
| `get_credit_provider`, `get_borrower_facilities` | A BDC or credit manager's quarterly tape, and every facility a borrower appears on |
| `search_ria_advisor_moves`, `search_allocator_commitments` | Adviser registrations that moved firm, and public plans' own commitment disclosures line by line |
| `get_research_records` | DFX's own published findings with permanent ids, versions and as-of dates |
| `watch_create`, `watch_list`, `watch_changes`, `watch_reevaluate`, `watch_cancel` | A saved investigation with checkpoints and material-change deliveries, account key required |

## What this pass measured

A keyless `initialize` answered **HTTP 200** with `serverInfo` `dfx-real-estate` **0.16.0**, title DFX Intelligence, and `tools/list` returned **20** tools. Six were called and all six answered.

`get_credit_provider` on **ARES CAPITAL CORP** (CIK 1287750, file number 814-00663, New York) returned the tape as of **2026-09-30**: **1,922** positions across **629** borrowers, fair value **$29,212.6 million** on the BDC's own SEC-filed total, principal held **$23,063.0 million**, cost **$29,477.5 million**, unfunded commitments **$4,878.3 million**, debt share **75.76** percent, first lien share **57.75** percent, **1,504** facilities, **54** sponsors financed, and **18** quarters on tape from **2021-12-31**. The first quarter on that tape reads **1,112** positions over **390** borrowers, fair value **$20,009.5 million**, principal **$16,384.4 million**, mark on cost **0.9863**, **121** PIK positions and an average spread of **6.27** percent. Every figure carries `cite_url` on `sec.gov`, the accession number and the source location inside the filing.

`search_entities` for Ares Capital resolved one record with `claim_type` `VERIFIED_FACT` and matched the adviser entity from 10-K text rather than from a name stem.

`search_allocator_commitments` with a query of CalPERS returned the plan's own disclosure rows: **California Public Employees' Retirement System** committed **$2,000,000,000** to **CV Consortio Fund L.P.**, managed by **Valor Equity Partners**, bucket `private_equity`, vehicle `commingled`, amount basis `printed`, cited to `calpers.ca.gov`.

`research` behaved differently on a resolvable question and an unresolvable one, and both are worth reading:

- Named entity: the question about Ares Capital's fair value and first lien share ran three operations (`resolve_name`, `get_credit_provider`, `search_private_credit_changes`), returned state `OK`, and answered from the change tape rather than from a model: **2** new lender events, **2** new portfolio companies, **1** non-accrual placement, naming **Flinn Scientific, Inc** on the non-accrual and **Essor Group Assets LLC** and **Aledade PBC** as new portfolio companies.
- No resolvable entity: the question about a dental services organization answered state **UNKNOWN** with the sentence "DFX could not resolve the subject of this question to one record, so it does not answer it", zero rows, zero claims, and `llm_calls: 0`. It declined rather than assembled a plausible paragraph.

Two more behaviours that matter before an agent is pointed at it. A `search_allocator_commitments` call with only a `limit` returned `INVALID_ARGUMENT`, `charged: false`, and the list of arguments it accepts, on the printed rule that it "refuses a call it cannot act on rather than guessing at what was meant". And `verify` checks a fixed predicate set (`INVESTED_IN`, `ACQUIRED`, `CO_INVESTED_WITH`, `WORKS_AT`, `IS_A`, `ADVISER_OF`, `COMMITTED_TO`, `LENDER_TO`, `HOLDS_POSITION`, `MOVED_FIRM`), so a sentence phrased outside that set comes back `UNKNOWN` with the reason, not a guess.

## The withholding is stated, not implied

Anonymous access is real and it is limited, and the server says so inside every payload instead of failing at the door. A record names its subject and the first **3** related names per section; a list returns its first **5** rows in full and a count of the rest. On the Ares Capital record the `locked` block reported **29** related names withheld, and contact values and decision-maker names are never returned at any tier, only their types and counts. The server's own line is the one to quote to a user: `LOCKED` means withheld, not missing.

`research` runs at depth `screen` without a plan, and the response states that `investigate`, `validate` and `monitor` come with a paid plan or the 7 day trial. So the free path answers questions of the shape "what does the tape say about this named entity", and stops short of the deeper verification modes.

## The caveats the server prints, which are the useful part

Each of these was read off the response, not inferred:

- Principal on a facility or borrower is the sum of BDC pieces on the tape. It is a **lower bound**, never the commitment.
- Fair value below cost is the lender's mark, not an impairment. Non-accrual comes only from a BDC's own footnote.
- A maturity or spread that moved between quarter ends is an observed term change, not an amendment, until the amendment document is on the graph.
- A sponsor is named only with its basis, and one-word borrower groups are never merged across BDCs.
- A BDC that tags no maturity contributes nothing to the maturity wall, so the wall is a floor.

That list is why this entry earns a guide rather than a bookmark. A private credit number is only quotable when the reader knows whether it is a filing, a derivation or a lower bound, and this is the only server here that labels the difference in the payload.

## Where this sits in the catalog

A grep of all **1,092** guides before this entry returned nothing for private credit, BDC, CMBS or allocator commitments, so the slice is empty rather than crowded. The neighbours are adjacent and stop short:

- [X1 Wealth MCP](/hermes/mcp/servers/external/x1-wealth-mcp/) reads cited family office records, which is one investor type rather than the capital structure behind a borrower.
- The institutional market data entries read public markets: prices, bonds, CDS and 13F holdings. A BDC schedule of investments is a private position with a fair value the lender itself assigns.
- The EDGAR surfaces here read what a company reported about itself. This reads what its lenders reported about it, which is the opposite direction and the only way to see a borrower's whole facility stack.
- [Prometiam Risk](/hermes/mcp/servers/external/prometiam-risk-mcp/) and the company registry entries answer who a company is. This answers who is lending to it, on what lien, at what spread and until when.

## Connect it

```json
{
  "mcpServers": {
    "dfx-intelligence": {
      "url": "https://exchange-production-9123.up.railway.app/mcp/core?c=dir-mcpso"
    }
  }
}
```

The `c=dir-mcpso` parameter is the directory referral token in the vendor's submission. Expect it to change once the listing is processed, and take the canonical endpoint from the vendor's own agents page rather than from this guide.

## Do not use it as

- **A credit opinion.** The tape carries the lender's mark and the facility terms. It does not carry default, restructuring or non-accrual unless a BDC footnote said so, and the server says as much.
- **A commitment figure.** Principal is a lower bound of what the BDCs on this tape hold, not what the borrower raised.
- **A name resolver across everything.** Resolution is good, and the record states its basis; a name that matches one short word is not merged for a reason.
- **A free bulk export.** Five rows and three related names per section is the anonymous ceiling, and the rest is a count.

## FAQ

### Does it need a key?
No for reads. `initialize` answered 200 with no credential and the six driven calls all answered. The watch tools need an account key, and their responses say so.

### Can I quote an answer to a client?
Yes, with the citation that travels on the row: `sec.gov` URL, accession number and the section inside the filing. The claim basis field tells you whether you are quoting a filing, a derivation or a carried value.

### Why did a question come back UNKNOWN?
Usually because it named no entity the graph could resolve, or because the claim used a predicate outside the ten the verifier checks. Both responses say which, and neither invents an answer.

### Can it see my own portfolio?
No. The graphs are public filings, registrations and plan disclosures. The only writes are the caller's own saved investigations.

### What does the paid tier add?
Full lists rather than five rows, related names past the first three, contact values where the vendor verified them, and the `investigate`, `validate` and `monitor` research depths. The trial is 7 days.

## See Also

- [SEC EDGAR MCP](/hermes/mcp/servers/external/sec-edgar-mcp/)
- [X1 Wealth MCP](/hermes/mcp/servers/external/x1-wealth-mcp/)
- [Prometiam Risk MCP](/hermes/mcp/servers/external/prometiam-risk-mcp/)
- [Company Atlas MCP](/hermes/mcp/servers/external/company-atlas-mcp/)
