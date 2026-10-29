---
title: "occasioni.it MCP - Italian Business Grants and Incentives"
description: "Search Italian national, regional and chamber-of-commerce grants for a business, match a profile to open calls and track each closing date."
category: Finance
stars: ★★ (200 keyless, full tools/list verified)
added: 2026-10-28
source: "live probe of https://occasioni.it/mcp answering HTTP 200 keyless on initialize as occasioni.it 1.1.0 on protocol 2025-06-18 with a session header and a full tools/list of 18 tools, plus chatmcp/mcpso issue #6334 and the vendor developers page"
relevance: ★★★
tags: [grants, funding, incentives, italy, smb, public-funding, keyless, remote-mcp]
last_updated: "2026-10-28"
---

# occasioni.it MCP

**A business that does not know a call exists cannot apply to it. The money is published every night and read by almost nobody.**

```
Server type: Remote (Streamable HTTP), keyless
Endpoint:    https://occasioni.it/mcp
Auth:        None for search, matching and catalogue reads
Server:      occasioni.it 1.1.0, protocol 2025-06-18
Tools:       18 at tools/list
Refresh:     Nightly, national catalogue plus regional and chamber calls
Vendor:      occasioni.it, official registry it.occasioni/bandi
```

## Why This Matters for Operators

Public funding for small businesses is published, indexed, dated and free, and it is still missed because nobody reads four hundred pages of regional notices a month. The calls that pay for a machine, a hire or an export push close on a date, and the date is the whole opportunity.

This server turns the catalogue into questions an operator already asks: which calls fit a company described in one sentence, what does one call actually require on the banking and insurance side, and what closes in the next thirty days. `match_business` ranks open calls against a business profile and explains each score, and the vendor states the scoring is a database calculation rather than a model call, so the same profile returns the same ranking.

Nothing in this catalogue covered this class before. The finance entries here are about reading a company's own numbers, this one is about money a company can apply for.

## What It Returns, Verified

A bare `initialize` on `https://occasioni.it/mcp` returned **HTTP 200** with no credential, `serverInfo` name `occasioni.it`, version `1.1.0`, protocol `2025-06-18`, and a session header. `tools/list` returned **eighteen tools**:

- **Search and match**: `search_incentives`, `get_incentive`, `match_business`, `quick_check`, `closing_soon`, `catalogue_stats`.
- **History and forecasting**: `catalogue_trends` (calls opened per month since 2021, seasonality), `expected_calls` (a call that recurs every year, with the expected next opening and a confidence), `region_brief`.
- **Adjacent to the relocation surface**: `search_places`, `get_place`, `relocation_programmes`, `free_services`, `plan_preview`, `search_remote_jobs`.
- **Paid reports**: `list_products`, `create_order`, `get_order`. Without credit `create_order` returns a Stripe `checkout_url` for the human rather than charging anything.

`quick_check` answers the question that decides whether to read further: who may apply, size, region, sector, timing, and what the call asks on the bank and insurance side, meaning a loan, a guarantee or a surety.

## Limits Worth Recording

Italy only, and the catalogue is Italian, so the reasoning comes back in Italian even when the operator writes in English. The paid reports are a separate product with a price list, and this entry records the free reads as free and does not describe the reports as included. `secondlife.it` serves the **same eighteen tools** on a second domain aimed at people moving rather than businesses, so the two are one server behind two front doors and are recorded once here rather than twice. A call absent from a result is not a call that does not exist: the vendor reads a national catalogue plus the regional and chamber layers, and a chamber notice published locally that morning may not be in yet.

## FAQ

### Do I need an account or an API key?
No. The search, matching, statistics and place tools answer without a credential, which is how this entry was verified.

### Which funding sources does it read?
The national incentives catalogue at incentivi.gov.it plus regional and chamber-of-commerce calls, refreshed every night according to the vendor.

### Can it apply for a grant on my behalf?
No. It finds calls, explains requirements and drafts a report. The application is submitted by the business, and the vendor exposes paid eligibility checks and application drafts as separate products.

### What does match_business actually score?
A business described in one sentence against open calls, returning ranked calls with the reasons for each score. The vendor states it is a transparent database score with no model call, so it is reproducible and auditable.

### Is there a non-Italian equivalent in this catalogue?
Not for public grants. The finance entries cover company data, accounting and market data, and the compliance entries cover rules a business must follow, not money it can claim.
