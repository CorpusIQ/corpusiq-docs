---
title: "MCP Server Discovery - October 31, 2026 (Afternoon)"
description: "Two and a half hours on: a handbook reader, an EU late-payment calculator measured live, and Quebec land data, all three answering first call."
last_updated: 2026-10-31
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october31-2026-afternoon/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 31, 2026 (Afternoon Sweep)

This pass fired at `11:00 MST`, two and a half hours after the midday read, which is short enough that the question changes: not what is new in the ecosystem, but what moved in a window where almost nothing can have. The answer came from three surfaces and only one of them was a directory page.

The mcp.so homepage `recentServers` block returned **140** parsed cards with the newest at `2026-10-31T17:06:19Z` against `14:37:33Z` at the midday read, so exactly two cards sat above the previous stamp and both were read. The mcpservers.org `/all` page came back through the r.jina.ai reader proxy with **22** unique slugs and the counter at **18,402**, and every slug was already named in a prior disposition. The submission window carried the rest: `#6509` Fonciq filed at `16:01:05Z`, which the midday pass read and did not disposition, and `#6511` PagoFix filed at `17:53:00Z`.

All three that shipped answered a live endpoint on the first request. That is the rule this pass applies, and it is the reason the guide count follows function rather than a quota.

## New: the company's own handbook, scoped by token

[HandbookHub MCP](/hermes/mcp/servers/external/handbookhub-mcp/) is remote Streamable HTTP at `https://api.handbookhub.com/mcp`, and it answered a keyless `initialize` with **HTTP 401** in 0.37 seconds carrying `A valid API token is required` with an `invalid_token` code and a requestId. That is the normal state for a connector bound to somebody's workspace, and it means the four-tool surface is the vendor's documentation rather than a list this pass drove. The documentation was read in full, and it is unusually complete: `list_handbooks` with cursor paging to 100, `get_handbook` for metadata and the nested page structure, `get_page` for the latest saved page as plain text with its URL, and `search_handbooks` over keyword, title and semantic matching with a score and a snippet per hit, returning no AI answer.

Three things make it worth a guide. The corpus is the operator's own published text, which no entry here has carried before. The token model is narrow by construction: created by the organization owner, named per client, scoped to selected handbooks or all handbooks including future ones, **120 requests per minute per token and 600 per organization** shared with the REST API, a **90-day** default expiry, and no ability to edit content, manage accounts, retrieve signatures, or read uploaded source documents or revision history. And the vendor writes the prompt boundary into the tool description itself, to treat page text as source material and not instructions, which is the correct posture for a corpus that anyone with edit rights can change.

Recorded gaps. `tools/list` needs a token, so the tool set and the read and write split are published rather than measured, and nothing was provisioned. The access gate is the practical fact: MCP comes with Starter and Growth and their trials plus the **14-day** Growth bonus after a one-time Handbook purchase, and valid tokens stop working when plan access ends.

## New: the interest an overdue invoice already owes

[PagoFix MCP](/hermes/mcp/servers/external/pagofix-mcp/) is remote Streamable HTTP at `https://pagofix.com/mcp`, **free and keyless**, and it is the opposite case to HandbookHub: the whole surface answered, `initialize` returning `serverInfo` `pagofix` at **1.0.1** and `tools/list` returning all **four** tools with their full input schemas.

Three calls measured it. A **German** claim of EUR 5,000 due 2026-08-31 came back **61 days late** with interest of **EUR 87.91** and the fixed **EUR 40.00** recovery compensation, a total of **EUR 5,127.91**, computed on the Bundesbank `Basiszinssatz` of **1.52 percent plus 9 points from 1 July 2026** and cited to **section 288(2) BGB**, **section 247 BGB** and **section 288(5) BGB**, with two primary sources linked. A **French** claim of EUR 12,500 came back **83 days late** with **EUR 352.47** of interest and the same EUR 40.00, on **Code de commerce art. L441-10 II** with the 30-day statutory default in **art. L441-10 I** and the compensation in **art. D441-5**. Both returned `status: verified` on the law block. The third call, `draft_reminder` at step 2 in English, returned a complete letter in 0.1 seconds with the calculation sheet attached, the interest line showing the period, the day count, the rate build and the amount, and a line inviting a written dispute before any further step.

Interest is computed **per half-year period**, so a claim crossing a rate boundary is split and each segment priced at the rate in force for it. That is the detail that makes the number match what a court or an accountant would produce, and it is why the response carries a `periods` array rather than one rate.

The containment is the sentence in the server's own instructions: PagoFix drafts, the creditor sends the letter and files the Form A in their own name, and the money goes straight to the creditor. The privacy notice dated the same day adds that the anonymous calculator runs in the browser and does not store invoice data server-side, with stored cases, sent-letter records and a 12-month sign-in log applying only to accounts.

Recorded gaps. `draft_eop` was not called, so the Form A output, the court mapping and the fee figures are unmeasured, and that is the tool carrying the most consequence. Only two of the eight published jurisdictions were exercised. And the GDPR position for the MCP path specifically, where invoice fields reach the vendor's server rather than staying in a browser, is a notice read rather than a processing agreement.

## New: two facts about a Quebec property, one of them free

[Fonciq MCP](/hermes/mcp/servers/external/fonciq-mcp/) is remote Streamable HTTP at `https://api.fonciq.ca/v1/mcp`, `initialize` answering with `serverInfo` `fonciq` at **1.0.0** and `tools/list` returning all **fourteen** tools. It is two products in one surface, and the free half is the reason to read it.

`flood_zones_lookup` is keyless at **30 requests per minute and 1,000 per day per IP**, and one live call at 45.4865, -73.8980 answered in 0.26 seconds with `any_zone_found: true` against the Ville de Montreal index of flood plains as a **reference layer**, dataset URL at donnees.montreal.ca, licence **CC-BY-4.0**, with source freshness stamped between `13:44:31Z` and `13:48:53Z` that day. The response refuses three assumptions in its own fields: the lot boundary is not evaluated because a point is not a polygon, an address point often sits on the street side, and no zone found never means outside a flood zone. It also records that the new-generation mapping in force by sector since 1 March 2026 is not included and links the official provincial map for confirmation. A tool that states what it cannot see is a tool whose answer can go in a due diligence file.

The paid half is the Registre foncier: lot resolution and profiles with assessment-roll values in cents, index requests, deeds and cadastral plans at **CAD 0.99 per document** excluding registry fees, batches of up to **500 lots**, and dated watches that re-check a lot's index against a baseline snapshot with a webhook. Lot reads, job reads and watch creation are not billed, and test keys are free.

Recorded gaps. Only the free tool was called. The thirteen registry tools, their output shapes and the **0.99** price are the vendor's published position, and whether a 500-lot batch bills per lot or per job is a question the first trial will answer for a lot less money than assuming it.

## Read and held

The mcpservers.org `/all` page carried no delta, but four of its slugs read as fresh to a bare slug match and are recorded here so the next pass cannot pick them up: `www-margoleads-io-docs-mcp` is **Margo**, `www-luriart-com` is **Luria** and `www-getpylot-com-agents` is **Pylot AI**, all three held in the October 30 evening pass, and `www-locusintel-io-docs-api` is **Locus Intel**, named in the October 30 midday pass. A slug derived from a vendor domain never matches a catalogue heading, which is why the cross-reference runs against every markdown file in the tree rather than the directory names.

The block count on mcp.so is worth recording as noise rather than news: **140** parsed cards here against **30** at midday. The same variance was recorded on October 30, when the block returned 16 and then 65 ten hours later, so the count is a parse artifact and the newest `createdAt` is the only reliable reading.

## The issue window, dispositioned

Two submissions, both shipped, so the window is closed rather than sampled.

`Fonciq` (`#6509`, `16:01:05Z`) was filed inside the midday issue window and not dispositioned there, which is the one gap this pass inherited and closed. `PagoFix` (`#6511`, `17:53:00Z`) is the arrival of the pass in the strict sense: free, keyless, four measured tools, and the only entry here that computes a legal number and cites the statute behind it. Its card states the operator, Nukehive OU in Tallinn, registry code 14647290, which is the kind of detail a finance tool should be judged on.

## Count

The guide tree held **1,070** server entries before this pass and holds **1,073** after it, across **1,461** files. Sources: the mcp.so homepage `recentServers` block read directly (**140** parsed cards, newest `2026-10-31T17:06:19Z`), mcpservers.org `/all` through the r.jina.ai reader proxy with `X-Return-Format: html` (**22** unique slugs, counter **18,402**), the chatmcp/mcpso issue window `#6509` and `#6511` read with bodies, a keyless `initialize` on `https://api.handbookhub.com/mcp` (**401**), a keyless `initialize`, `tools/list`, two `calc_claim` calls and one `draft_reminder` call on `https://pagofix.com/mcp` (**200**), a keyless `initialize`, `tools/list` and `flood_zones_lookup` on `https://api.fonciq.ca/v1/mcp` (**200**), and HTTP reads on `handbookhub.com`, `handbookhub.com/mcp`, `handbookhub.com/api`, `handbookhub.com/pricing`, `pagofix.com`, `pagofix.com/privacy`, `github.com/pagofix/pagofix-mcp` and `fonciq.ca/api-gratuite/zones-inondables`, all **200**.
