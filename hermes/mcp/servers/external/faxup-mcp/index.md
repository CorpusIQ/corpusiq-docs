---
title: "FaxUp MCP - Send a Fax to 62 Countries From Chat"
description: "Sixty-two countries reachable by fax, a price quote per fax, the IRS form fax numbers with their state split, and a confirmation link before anything sends."
category: "Business Operations"
stars: n/a (vendor-hosted)
added: 2026-11-22
source: "chatmcp/mcpso submission #7833 filed 2026-11-22T16:23:34Z; keyless initialize, tools/list and seven tools/call requests on 2026-11-22"
relevance: ★★★★
tags: [fax, document-delivery, government-forms, keyless, remote-mcp, compliance]
last_updated: "2026-11-22"
---

# FaxUp MCP

**Remote MCP server (Streamable HTTP, no authentication)** - the first fax entry in this catalogue. An agent asks what a fax costs, formats the number, finds the official fax number for a US government form, and prepares the document. The fax itself is never sent by the model.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://mcp.faxup.net/mcp
Server:      faxup 1.2.0, protocol 2025-06-18
Tools:       9
Registrations: none required for reads; a paid account for most countries
```

## Why This Matters for Operators

Fax survives in exactly the places where a rejected document costs a filing deadline: IRS powers of attorney, USCIS paperwork, medical referrals, property and insurance files. The work is not typing a number, it is knowing which fax line accepts which form, and whether the number on the letterhead is a fax line at all.

This server answers all three of those questions before money moves, and it refuses to send. Its own instructions say so plainly:

> send_fax never sends anything by itself: it returns a link the person must open to check every page, pay (or use their FaxUp credits/plan) and press Send on faxup.net. Always show that link to the person and tell them the fax has NOT been sent yet. Only PDFs are accepted. Faxes go to fax lines only, never mobile numbers.

## Measured Behaviour

Seven calls were driven on 2026-11-22, all keyless. Every figure below is quoted from the response.

| Call | Arguments | Answer |
|---|---|---|
| `list_supported_countries` | none | **62** countries with calling codes |
| `find_agency_fax_number` | `"IRS"` | **8** numbers, each with its form, state split, source URL and check date |
| `get_price_quote` | `+1 855 887 7734`, US, 3 pages | **$2.99** for this fax, plus the full pack table |
| `format_fax_number` | `020 7946 0958`, GB | accepted as a UK fax line, national form `2079460958` |
| `get_country_fax_guide` | `GB` | drop the leading 0, `07` numbers are mobiles, GMT/BST |
| `compare_fax_services` | `eFax` | FaxUp pay per fax against a subscription rival |
| `send_fax` | `+15550100` | refused: *not a valid phone number* |

### The coverage list is not uniform

The 62 countries are not one service tier. US and Canada take any fax line except mobiles, premium-rate and Caribbean +1 codes, and include a free single page. Outside those two, the response states that a paid account is needed and caps the volume at five international faxes a day. An agent that tells a UK or German user "you can fax this now" without a plan would be wrong, and the list marks the boundary.

### The IRS lookup is the part worth keeping

`find_agency_fax_number("IRS")` returned eight numbers, split by state because the IRS runs two CAF units:

```text
Form 2848 power of attorney (CAF Unit, Memphis)  +1 855-214-7519
  lives in AL, AR, CT, DE, DC, FL, GA, IL, IN, KY, LA, ME, MD, MA, MI, MS, NH,
  NJ, NY, NC, OH, PA, RI, SC, TN, VT, VA or WV
Form 2848 power of attorney (CAF Unit, Ogden)    +1 855-214-7522
  lives in AK, AZ, CA, CO, HI, ID, IA, KS, MN, MO, MT, NE, NV, NM, ND, OK, OR,
  SD, TX, UT, WA, WI or WY
Source: https://www.irs.gov/instructions/i2848 (checked 2026-11-12)
```

Each entry also carries its exclusion: *forms signed electronically must be submitted online instead*. That sentence is the difference between a filed form and a faxed one that never counted.

### Price is stated, not implied

The quote for a three-page fax to a US number returned **$2.99 for this fax**, then the whole ladder: 5 faxes $3.99, 10 for $5.99, 30 for $14.99, 50 for $24.99, 100 for $39.99, and an optional Unlimited plan at $3.99/week, $11.99/month or $89.99/year. One credit sends one fax of any number of pages, credits never expire, and a fax that finally fails is refunded. The tool charges nothing.

### It refuses rather than guesses

`send_fax` with a malformed number came back as an error naming the problem, not a prepared fax:

```text
isError: true
+155****0100 is not a valid phone number. Check the country code and the digits.
```

## What It Cannot Do

- The fax is prepared, never sent. A human opens the link, checks every page, pays and presses Send.
- PDF only.
- The comparison tool reads its own price against rivals it names (eFax at $16.99 to $18.99 a month) and states when those figures were read: 2026-11-12. Treat it as a dated snapshot, not a live quote from the competitor.

## Frequently Asked Questions

### Can an AI assistant send a fax, or only prepare one?

Only prepare. The server returns a confirmation link and instructs the client to say the fax has not been sent. Sending is a human action on faxup.net, after review and payment.

### Does this replace a subscription fax service?

For occasional sending, it removes the subscription: one credit is one fax regardless of length, and the cheapest pack is a single fax at $2.99. For heavy volume the Unlimited plans exist at $3.99 a week, $11.99 a month or $89.99 a year.

### Which countries need a paid account?

US and Canada work on the free single page and per-fax credits. Every other country on the 62-country list needs a paid account with a limit of five international faxes a day.

## See Also

- [Government and filing data sources in the external catalogue](/hermes/mcp/servers/external/)
