---
title: "htsapi.dev MCP - US Tariff Classification Sources"
description: "The US tariff schedule with its legal notes, 222,000 CBP rulings with status, and what importers actually paid on a code."
category: "Business Operations / Trade"
stars: "n/a (hosted service, no server repository; docs at github.com/rozetyp/htsapi-mcp)"
added: 2026-11-19
source: "the mcp.so submission queue entry #7637 filed 2026-11-19T07:11:28Z, a live handshake and full tools/list on 2026-11-19, eleven tools/call requests across seven keyless tools, the official MCP registry record and the vendor's price, developer and status pages"
relevance: ★★★
tags: [tariff, hts, customs, cbp, rulings, imports, trade-compliance, landed-cost, census, remote, keyless]
last_updated: "2026-11-19"
---

# htsapi.dev MCP

**Every landed-cost model has one number in it that nobody can defend: the tariff code.** The rate follows from the code, the code follows from the notes and from what CBP has already decided about similar goods, and the statutory rate is not the rate that got paid. Three different sources answer those three questions, and this catalog already carries one of them.

[Tariff Monitor](/hermes/mcp/servers/external/tariff-monitor-mcp/) is the calculator: give it a ten-digit line and an origin and it stacks MFN, Section 301 and Section 232 into a percentage and a dollar figure. htsapi.dev is the other half. It serves the schedule one level at a time with the legal notes that decide between headings, the CBP rulings corpus with each ruling's current status, and the rate importers from a country actually paid on a code in the latest Census months. It does not calculate a duty for you, and the vendor is explicit about why.

```text
Server type:   remote Streamable HTTP (hosted, stateless, no session id issued)
Endpoint:      https://htsapi.dev/mcp
Server:        htsapi, version 1.0.0, protocol 2025-06-18
Auth:          none for seven of eight tools; X-API-Key for classify_product
Tools:         8          7 keyless · 1 credit-priced
REST:          https://htsapi.dev/v1, same data, X-API-Key header
Registry:      dev.htsapi/mcp 1.0.0, published 2026-11-19T07:10:50Z
Queue:         mcp.so #7637, filed 2026-11-19T07:11:28Z
Sources:       USITC tariff schedule · CBP rulings (CROSS) · US Census Bureau
Free tier:     50 calls a day per IP, 10 a minute, no key
```

## The instrument panel is the rulings, not the schedule

A schedule lookup is commodity. The difficult question in an import business is never "what does 6404.11.20 say". It is "has anyone imported something like mine, and what happened". That is a precedent question, and htsapi answers it from the CBP rulings corpus rather than from a model's opinion.

`search_rulings` on the plain words **led camping lantern** returned three rulings, each carrying a similarity score and the field that produced it. The top hit was N081456, issued 2009-11-17, status `current`, code 8513.10.4000, `similarity` 0.736, `matched_via` meaning. The second was F88523 from 2000-07-11 on the same code. The facts field quotes the product description CBP actually examined, which is what makes a precedent usable: not "a lantern", but a plastic battery lantern with 8 white LEDs and a three-position slide switch.

`rulings_under_code` reads the same corpus from the other direction. For 6403.99 it reported **719 current rulings** and **1** ruling whose goods CBP moved away from the code, which is a cheap way to see whether a code is settled or contested.

## What each of the eight tools returns

| Tool | Arguments | What comes back |
|---|---|---|
| `lookup_hts_code` | `code` (optional, any depth) | the 22 sections and their chapters with no argument; a heading's subheadings and line count; a line's rates, and the newest rulings under it |
| `get_notes` | `code` (optional) | the section and chapter notes for a code, or the General Rules of Interpretation with no argument |
| `heading_scope` | `heading`, `product` | the passages CBP rulings quote when deciding a heading, with the note they cite and what CBP concluded |
| `search_rulings` | `query`, `limit` | rulings for a product described in plain words, by meaning, with status |
| `rulings_under_code` | `code`, `product`, `limit`, `offset` | every ruling under a code, current and moved |
| `get_ruling` | `ruling_number` | one ruling in full, its codes, status, what revoked or modified it and what it cites |
| `importers_paid` | `code`, `country_of_origin` | the rate importers from that country paid over the latest three Census months |
| `classify_product` | `description`, `country_of_origin`, `material` | the vendor's own classifier suggestion. Needs a key, costs one credit |

## What was driven, and what came back

Eleven calls across seven keyless tools, no account and no key. Three of them carry the guide.

**The schedule, one level at a time.** `lookup_hts_code` with no argument returned all 22 sections and their chapters in 18,207 characters. With `6404` it returned the heading's own path, three subheadings and their line counts (6404.11 with 41, 6404.19 with 79, 6404.20 with 9, `lines_total` 129), and the newest rulings under the heading. The two stepwise reads are the point: a classifier reads down the tree, and this tool serves the tree instead of guessing a leaf code.

**The notes that decide.** `get_notes` on 6404 returned chapter 64's exclusions verbatim (disposable shoe coverings, footwear without an affixed outer sole, orthopedic footwear under 9021, toy footwear), note 3's definitions of rubber and plastics, note 4's rule that the material with the greatest external surface area wins, and the subheading note that limits "sports footwear" to designated athletic categories. Those four paragraphs are what an argument between two codes is actually made of.

**What importers paid.** `importers_paid` for 6404.11.20 from CN returned a general duty of 10.5 percent and then three monthly effective rates: **29.8 percent in 2026-07, 33.0 percent in 2026-08, 34.7 percent in 2026-09**. The gap between 10.5 and 34.7 is Chapter 99 duties, and the response says so, alongside three things it will not do: it does not include anti-dumping or countervailing duties, it is an average of past entries rather than a quote, and Census publishes about two months late.

## Where it refuses, and where it substitutes

The refusals are informative, which is rare enough to record.

- **Chapter 99 is not served.** `lookup_hts_code` on `9999999999` returned an error stating that temporary-duty lines (Section 301, 232, 122 and the like) are not covered by that tool, that they add to the goods' own code, and that `importers_paid` shows what was paid with those duties folded in. The tool refuses the question and names the tool that answers it.
- **A short query is refused in band.** `search_rulings` with an empty query returned "query needs at least 3 characters" as an error rather than an empty result set.
- **The classifier is gated, cleanly.** `classify_product` returned "needs an API key (it costs a credit). The other tools work without one."
- **An eight-digit code falls back to the six-digit group.** `importers_paid` on 6404.11.20 answered at `level: HS6` with `rate_pct: null` and the months filled, and the note states that Census reports six and ten digit codes but not eight. A reader who quotes the top-level `rate_pct` sees nothing; the numbers are in `months`.
- **A heading carries no single rate.** `lookup_hts_code` on 6404 returned `general_duty: null` while each subheading carried an aggregate string such as "10.5% / 7.5% / 37.5% / 48% / …". An agent asked for the duty on a heading gets a spread, not a number, which is honest and also the moment to go one level deeper.
- **A ruling number accepts its office prefix.** `get_ruling` on "NY N301234" resolved to N301234 and returned the full text, three codes, `status: current`, and the same codes repeated in `obsolete_codes`, which is how a 2018 ruling whose codes have since been superseded reads.

## The legal line the vendor draws

The vendor states that CBP has ruled that an unlicensed platform suggesting codes beyond six digits for goods to be entered is conducting customs business, and that an importer may classify its own goods. That sentence explains the shape of the product: the schedule, the notes and the precedents are free, the agent does the reading, and the vendor's own classifier sits behind a paid credit as a second opinion rather than as the answer. Its classifier page repeats the boundary: guidance, not a binding ruling or a determination for entry.

That is the right posture for an operator too. The useful integration is a research assistant that shortens the loop before a broker call or an entry, not an automatic classifier that writes a code into a declaration.

## Freshness and price

The REST status route answered with three sources, each carrying its own sync time and staleness flag: `usitc_hts` synced 2026-11-16T02:02:45Z, `cbp_cross` synced 2026-11-17T04:33:16Z with a newest ruling dated 2026-10-30, `usitc_ch99` synced 2026-11-16T02:03:13Z, and `overall_healthy` true with none stale. Ruling coverage is the number to watch on this product, because the precedent layer is only as good as its last CROSS sync.

The free tier is 50 calls a day per IP and 10 a minute. The vendor's price page lists $9 a month for unlimited read tools under fair use, arranged by email, and classification credits at 100 for $10 or 1,000 for $50, one per classification, never expiring. A credit purchase also issues an API key that reads the REST endpoints free. The key is shown once for 24 hours after payment and is not emailed, and the vendor states there is no self-service reset yet, so it has to be stored at the checkout.

## Who should connect it

An operator importing physical goods with a landed-cost model, a sourcing decision between two countries, or a recurring argument with a broker about how a product is classified. It pairs with Tariff Monitor: that one prices the rate, this one shows the notes and the precedents behind it, and `importers_paid` is the control that says whether the statutory stack matches what competitors actually paid.

## FAQ

### Can an AI agent classify a product under the HTS without a licence?

Not as a filing decision. The vendor's own position is that an unlicensed platform suggesting codes beyond six digits for goods to be entered is conducting customs business, and that the importer may classify its own goods. The seven keyless tools serve the sources a classifier reads: the schedule, the notes, the rulings and the Census rates. The vendor's classifier is a separate, credit-priced second opinion, labelled guidance rather than a binding ruling.

### How do I check whether a CBP ruling is still current?

`get_ruling` returns the ruling's `status` and, when it has been superseded or modified, the ruling that did it and the codes CBP moved the goods to. `rulings_under_code` counts both sides: 719 current rulings under 6403.99 against 1 ruling whose goods moved away.

### What did importers actually pay compared with the statutory rate?

`importers_paid` returns the general duty line beside three monthly effective rates from Census. On 6404.11.20 from China the statutory general rate read 10.5 percent while paid rates ran 29.8, 33.0 and 34.7 percent across 2026-07 to 2026-09, the difference being Chapter 99 duties that the response names and anti-dumping and countervailing duties that it states are excluded.

### What does htsapi.dev cost?

The seven read tools are free without a key at 50 calls a day per IP and 10 a minute. The vendor lists $9 a month for unlimited read tools under fair use, and classification credits at 100 for $10 or 1,000 for $50, one credit per classification and never expiring. A credit purchase also issues a REST API key.

---

*Driven on 2026-11-19 against `https://htsapi.dev/mcp`, server `htsapi` 1.0.0, eight tools listed, seven driven keyless across eleven `tools/call` requests with one API-key refusal and two argument refusals recorded. Registry record `dev.htsapi/mcp` 1.0.0 checked the same day. Vendor figures are quoted as stated on the vendor's own pages.*
