---
title: "Postbye MCP - How to Cancel Any Subscription"
description: "Eight thousand cancellation guides with the method, notice period, mailing address and a ready-to-send letter, read over MCP with no key."
category: Operations / Vendor Management
stars: n/a (free, keyless, read-only)
added: 2026-10-27
source: "live JSON-RPC probes on https://postbye.com/mcp answering initialize as postbye 1.2.0 with its instructions string and the four tool schemas from tools/list, the executed calls search_companies, get_cancellation_guide and list_categories, the mcp.so feed card filed 2026-10-27T07:26:04Z and the guide pages it cites"
relevance: ★★★
tags: [subscriptions, vendor-management, expense-control, cancellation, cost-reduction, letters, keyless, streamable-http]
last_updated: "2026-10-27"
---

# Postbye MCP

**Cancelling a business subscription is a process nobody documents until the renewal is already charged, and the reason it costs money is that the vendor's cancellation method is buried in a terms page rather than in the product.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://postbye.com/mcp
Auth:        none, read-only
Tools:       4 (search_companies, get_cancellation_guide,
             get_cancellation_letter, list_categories)
Coverage:    8,600+ companies across 30 categories
Databases:   updated April 2026, 584 software guides of which
             109 verified by hand
Built by:    Postbye (postbye.com)
```

## Why This Matters for Operators

A tool stack accumulates and none of it announces its own exit. The seat-based plan billed annually, the domain registrar with the auto-renew, the membership that renews by mailed letter in a state nobody works in. Each one is small and the total is not, and the cancellation step for each is different by design.

The useful part of this server is that it returns the method, not just a link. For a company that takes cancellations only by mail, it returns the mailing address and offers a certified letter, which is the difference between a request and proof of the date it was made. For one that cancels in the account, it returns the click path.

For an operator reviewing spend, or an assistant asked to cut costs, a lookup that answers "how do I get out of this and what will I need to do first" in one call is the missing half of every expense report.

## What It Returns, Verified

Four tools and no key. `search_companies` takes a query and a limit up to 10, `get_cancellation_guide` takes a slug, `get_cancellation_letter` takes a slug plus a customer name and returns a plain-text letter built on the same template as the vendor's free letter tool, and `list_categories` returns the hubs.

One schema correction worth recording: `get_cancellation_guide` requires `slug`, not `company`, and returns `Missing required argument: slug` with `isError: true` if you send the friendlier name. Search first, then use the slug it returns.

`list_categories` returned 30 categories with the guide count and the number verified by hand in each: News and magazines at 863, Insurance and protection plans at 714, Software and apps at 584 with 109 verified by hand, Streaming and entertainment at 454 with 74, Phone and internet at 420, Finance and credit at 419.

The software category is the one that matters here, and three searches were run against it:

- `hubspot` returned one match, Software and apps, cancellable by mailed letter only
- `adobe` returned five, including Adobe itself by online account and separate entries for Acrobat and Lightroom, each plan cancelled separately
- `quickbooks` returned one, QuickBooks Online, with the full click path through the Intuit Account Manager and a note that a subscription bought in the App Store or Play Store is cancelled there instead

`get_cancellation_guide` for hubspot returned the method, two mailing addresses on file (2 Canal Park, Cambridge MA 02141 as primary, plus a Sydney address), and three checks to run before sending: whether the plan is billed per seat, what happens to files at the end of the term, and whether the annual terms carry an early-cancellation fee. It also states plainly that those checks are general points for any software subscription rather than rules lifted from HubSpot's pages, which is the honest version of the same caveat.

The vendor can mail a letter by certified mail on your behalf, priced on postbye.com/how-it-works, which is the paid surface behind a free read.

## Limits Worth Recording

- **The database is dated, not live.** Guides carry a dataset month rather than a per-page check date, and the HubSpot guide said April 2026, so a vendor that changed its process since then will read as current.
- **Not every guide is hand-verified.** 109 of 584 software entries carry hand verification. The rest are built from published terms, which is why the guide names its sources per company page.
- **The pre-cancellation checks are generic.** They apply to the class, not to the specific contract, so early-termination fees and notice periods still need the invoice.
- **Read-only, and no account access.** Nothing here cancels anything for you unless you buy the certified-mail service, and no subscription account is connected.
- **Consumer-weighted coverage.** Streaming, insurance and phone categories outnumber software, so a niche B2B vendor may simply be absent.

## Wiring It Up

```json
{"type": "streamable-http", "url": "https://postbye.com/mcp"}
```

No auth, no key, no account. The instruction string is explicit that every answer matches the company's page on postbye.com, so a claim can be checked by opening the cited guide.

## FAQ

### Can it cancel a subscription for me?

No. It returns the method, the notice period, the traps to check, the mailing addresses on file and a ready-to-send letter. The only execution path is Postbye's own certified-mail service, bought from postbye.com.

### Does it cost anything?

The MCP server is free and keyless for all four tools. Postbye charges only if you have it mail a cancellation letter by certified mail.

### Which vendors are covered?

8,600+ companies across 30 categories, with 584 in Software and apps, 419 in Finance and credit, 420 in Phone and internet, 714 in Insurance and 863 in News and magazines.

### How do I get a letter rather than a guide?

Search for the company to get its slug, call `get_cancellation_guide` for the method and addresses, then `get_cancellation_letter` with that slug and a customer name to get plain text you can print and post.
