---
title: "MCP Server Discovery - October 23, 2026 (Midday Supplement)"
description: "A fifty-minute delta that produced one entry: liquor license and permit filings fused into per-metro restaurant openings, driven with real calls."
last_updated: 2026-10-24
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october23-2026-midday-supplement/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 23, 2026 (Midday Supplement)

A fifty-minute delta after the midday capture, and the surfaces behaved exactly as they should at that gap: nothing new on the directories, one new submission, and one card on the feed. The submission was the entry, and it was the rare kind that can be driven end to end without an account.

mcpservers.org `/all` pages 1 to 3 returned 90 unique slugs against the midday pass's 89, and the net one resolved to a slug already carrying a disposition (the pagination spillover the night pass recorded in the other direction). Every other slug matched a prior record, including the sixteen read to detail pages yesterday. The mcp.so feed page 1 carried one card posted after the midday capture closed at `17:11Z`, and it was held. The submission window advanced by exactly one issue, `#5993`, filed at `17:06Z`.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [PourWire MCP](/hermes/mcp/servers/external/pourwire-mcp/) | Data & Analytics | Pre-opening intelligence for the hospitality trade: liquor license applications and building permits fused into per-metro feeds of restaurants and bars opening in the next 60 to 120 days, each row carrying the filing that produced it. `https://pourwire.com/mcp`, Streamable HTTP, keyless public tier. Probed live: `POST initialize` returned HTTP 200 with `serverInfo` `pourwire` 1.0.0 on protocol 2025-06-18 and the tools capability, and `tools/list` returned two read-only tools. `search_openings` takes a metro (`los-angeles`, `new-york`, `austin`, `waco-temple`, `dallas-fort-worth`, `houston`, `san-antonio`), an optional status (`new`, `in_buildout`, `approved`, `opened`) and a limit defaulting to 20; `metro_stats` returns tracked totals, new, filed in the last 30 days and the source agencies. Driven with four real calls: `search_openings` on `austin` returned Proper Ash (bar, PROPER ASH LLC, Drifting Wind Run Dripping Springs 78620, estimated Dec 2026 to Feb 2027, stage new, confidence 0.6, first filed 2026-09-23) with two dated TX TABC application events, one of them 2026-10-14, plus Fresa's Chicken and Himalayan Flavor in the same shape; `metro_stats` on `austin` returned 237 tracked, 154 new, 33 filed in 30 days, sourced from Austin DSD and TX TABC; `search_openings` on `los-angeles` filtered to `approved` returned chain filings with an empty trade name and the brand inside the legal name (CHIPOTLE MEXICAN GRILL #4864 in Palmdale, confidence 0.8, one CA ABC `license_issued` event dated 2026-09-23) and PIH GOOD SAM SPORTS LOUNGE under Sodexo America; and `metro_stats` on `new-york` returned 2,819 tracked, 124 new and 204 filed in 30 days, sourced from NY SLA, NYC DOB and NYC DOHMH. Public tier is free and deliberately delayed: filings older than 30 days, block-level address, no owner contacts, with each row linking to its venue page. Pricing from the vendor's own page: Scout $149 per metro per month ($1,490 annual) for the Monday digest, dashboard, full names and CSV; Operator $249 per metro per month ($2,490 annual) adding the daily digest, owner names and business contacts, a webhook or Zapier into a CRM, and REST plus MCP access; annual is billed as ten months, the trial is 14 days with no card, and seats are capped at five per trade per metro and published as a live table. Official registry entry `com.pourwire/pourwire` 1.0.0, active since `2026-10-23T12:44:22Z`; Glama connector page returns HTTP 200. **Gap named rather than claimed:** the subscriber tier was not tested, because it needs an account this sweep does not create. **Data shape worth knowing before a join:** `count` in `search_openings` is the rows returned rather than the metro total (a limit of 3 returned `count: 3` while `metro_stats` reported 237 tracked), confidence ships as 0.6 or 0.8 with no published definition, chain filings return `business_name: null`, and the vendor's CC BY 4.0 CSV (`github.com/Tintin-Intellegence-Limited/us-liquor-license-applications`, 0 stars) has no LICENSE file in the repository despite the claim in its description. |

## Candidates Read and Held

**From the mcp.so feed, the one card posted after the midday capture closed at `17:11Z`:**

- **Pokemon TCG Restock Alerts** (`bujusjujus-pokemon-tcg-restock-alerts`, `createdAt 2026-10-23T17:20:32Z`, Finance & Commerce, submitted by bujusjujus LLC, marked verified and featured, remote): real-time trading-card restock alerts, MSRP lookups and retailer restock timing for card shops, apps and agents, with signed webhooks and a per-alert evidence field. Held as consumer collectibles data, the class carried by CARDZ, and as a retail stock-checking utility: the surface answers where a boxed product is on a shelf, which is not a business record an operator's own systems are missing. The webhook-plus-evidence design is the strongest part and is recorded here for a future retail-inventory pass.

**From the submission window `#5993`, one issue:** catalogued above. No other issue arrived in the window; `#5992` was the midday pass's last read.

## Listing Verification

Re-checked live this cycle: mcpservers.org `/servers/corpusiq-io` still serves the listing under the page title `CorpusIQ MCP Server | Awesome MCP Servers`, and `glama.ai/mcp/servers/CorpusIQ/corpusiq-docs` returns HTTP 200. mcp.so remains absent on the six slug forms probed in the midday pass (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`, `corpusiq-docs`, the publisher handle form), unchanged since August. The midday pass's correction stands: Smithery is listed on the detail route (`registry.smithery.ai/servers/@Cprusiq`, `qualifiedName` `Cprusiq`, public page titled `CorpusIQ - MCP`), and the PulseMCP beta API stays unclaimed while it is inside its sunset window.

For the new entry: mcp.so has no detail page for PourWire yet (`/server/pourwire` returns 404, the submission is still an open issue), mcpservers.org blocks direct detail probes with a 403 to a non-browser client, and the official registry and Glama both answer 200.

## Sweep Notes

- **A fifty-minute gap is a submission-window check, not a directory check.** Three surfaces, one new card, one new issue. The correct read after an hour of ingestion is that nothing has been invented yet, and the next productive window is the next submission batch rather than another page-1 crawl.
- **A real tool call changes the record's weight.** Of roughly forty entries added this month, the ones that could be driven keyless carry filed evidence instead of a 401. PourWire returned venue rows, filing dates, license types and per-agency sources on every call, so the entry states what the data is, not what the card claims it is.
- **Read the numbers the tool prints, not the number in the summary.** `count` reported the page size while `metro_stats` reported 237. An agent that trusts the first number understates a market by two orders of magnitude, and that is now written into the guide as a limitation rather than left for the next reader to discover.
- **A license claim in a README is not a license file.** The vendor describes its free CSV as CC BY 4.0 and the repository carries no LICENSE. Recorded as an open item rather than repeated as fact.

Catalog 980 to 981 servers (+860 to +861 guides).
