---
title: "Stackblade MCP - Substack Follower and Rank History"
description: "Dated follower counts, category leaderboards and rank moves for Substack writers, read over five keyless tools with no account or sign-in."
category: "Creator Economy / Media Analytics"
stars: "n/a (hosted vendor endpoint; MCP wrapper at github.com/whosman/stackblade-mcp)"
added: 2026-11-20
source: "the mcp.so submission queue entry #7691 filed 2026-11-20T06:36:03Z, a keyless initialize and full tools/list the same morning, six driven tools/call requests (list_categories, both board types for technology, get_writer on a tracked handle, recent_activity on two event kinds, and two refusal paths), the official registry record io.github.whosman/stackblade 1.0.0, and the vendor's pricing page fetched to HTTP 200"
relevance: ★★
tags: [substack, newsletters, creators, media-analytics, benchmarking, leaderboards, remote, keyless, free-tier]
last_updated: "2026-11-20"
---

# Stackblade MCP

**A newsletter's ranking is a number its owner cannot see. This server publishes those numbers for 35 Substack categories, dated, with the moves.**

```text
Server type:   remote Streamable HTTP, stateless (no Mcp-Session-Id issued)
Endpoint:      https://stackblade.app/api/mcp
Server:        stackblade 1.1.0, protocol 2025-06-18
Registry:      io.github.whosman/stackblade 1.0.0 (endpoint reports 1.1.0 - see version note)
Repository:    https://github.com/whosman/stackblade-mcp (HTTP 200)
Vendor page:   https://stackblade.app (HTTP 200, 84,011 bytes), pricing at /pricing (200)
Auth:          none for light use; a Pro key for automated use beyond a small free trial
Tools:         5, all read-only
```

## What the server is

Stackblade keeps a daily history of Substack writers: follower counts, leaderboard positions in 35 categories, and the recommendation graph between publications. The `initialize` response sets two limits before any tool is called, and both matter:

> Every tool reads public data and changes nothing. ... Paid subscriber numbers are a band or a badge, never an exact count. Automated use beyond a small free trial needs a Pro key.

So the surface is a banding system, not a subscriber database. Where a writer's plan is "Tens of thousands", the tool will not turn that into 34,000.

## The five tools

| Tool | Arguments | What comes back |
|---|---|---|
| `list_categories` | none | 35 categories with a slug, a name and a writer count each |
| `board` | `category`, `board` (`bestsellers` or `rising`) | the top of one board: rank, previous rank, handle, publication, followers, paid band, recommendation count |
| `get_writer` | `handle` | followers, rounded subscriber figure, paid band, bestseller badge, 7 and 30 day change, recommenders and their new count, what the writer recommends, and every board position |
| `recent_activity` | `kind` (`all` / `rank` / `rec` / `followers`) | the newest leaderboard moves, follower milestones and new recommendations |
| `get_follow_links` | `handle`, `audience` (`reader` / `writer`) | the follow link for a reader and the claim link for the writer |

## Boards, measured

`list_categories` returned **35** categories with a writer count on each - Finance 179, Sports 178, Business 176, Travel 175, Culture 174, Literature 174, Art & Illustration 172, Home & Garden 172, Humor 172, U.S. Politics 172 and so on down the list. That count is the tracked population per board, not the size of Substack.

The Technology bestsellers board on 2026-11-20, top three:

```text
#1  semianalysis        SemiAnalysis        388,534 followers   paid band "Tens of thousands"   72 recommenders
#2  natesnewsletter    Nate's Substack     187,346 followers   paid band "Tens of thousands"   59 recommenders
#3  pragmaticengineer  The Pragmatic Engineer 1,241,686 followers  paid band "Tens of thousands"  77 recommenders
```

Read that carefully, because it is the most useful thing in the product: the board is **not** ordered by followers. The third-ranked writer has 3.2 times the audience of the first, and the ordering holds only because bestsellers ranks by paid subscribers - which is why the rank is the honest number for a sponsor and the follower count is the flattering one.

The **rising** board is a different population and a different ordering: Gary Marcus at 158,674 followers takes first, Andrew Lu at 24,771 takes second. Rising is a movement board, not a size board, so the two must never be compared as if they shared a scale.

## One writer, measured

`get_writer` on `pragmaticengineer`:

```text
followers              1,241,686        subscribers_rounded   "1.1M+"
paid_band              "Tens of thousands"    bestseller_badge  10000
change_7d              3,068 over 7 days      change_30d         null
recommended_by         77               new_recommenders_30d   32
recommends             11
boards                 Technology bestsellers #3, Podcasts bestsellers #25, Technology rising #33
```

Two things to note. `change_30d` is **null** while `change_7d` carries a number, so the 30-day baseline is absent rather than zero, and a chart built by treating null as zero will draw a collapse that did not happen. And a writer can sit on three boards at once, including both bestsellers and rising in the same category, which is why the board list is an array rather than a rank.

## Activity, measured, and one stream that lags

`recent_activity` with `kind: "followers"` came back current to the hour: ten events between **00:36Z** and **03:10Z** on 2026-11-20, the newest reading "SheWritesAI passed 5,000 followers" at 03:10:09Z.

`recent_activity` with `kind: "rank"` had a newest entry of **2026-10-31T19:47:01Z** - twenty days behind the follower stream, with a whole batch of "entered Bestsellers at #98" and "#100" events stamped in the same second. The follower stream is live; the rank-event stream is stale, and `kind: "all"` mixes them without saying which is which. Treat rank events as history until the vendor refreshes that lane.

## Refusals, measured

```text
board            category "not-a-category"
  isError: true
  "No category matches \"not-a-category\". Some categories: finance, sports, business,
   travel, culture, literature, art, home-garden. Every category is listed at
   https://stackblade.app/categories."

get_writer       handle "zzzz-not-a-writer-9999"
  found: false, status: not_tracked
  "Stackblade does not track a writer matching ... The handle is the part after @ ..."
  suggestions: aaronrupar (667,034 followers), notboring (377,845), staceyabrams (348,846)
```

The unknown-writer path returns a "guess" field and three alternative writers, which is helpful and also a trap: a fuzzy match is not the writer asked for, and an agent that silently follows the first suggestion will report the wrong publication.

## Where it stops

- **Paid subscribers are a band, by design.** A band plus a badge (`10000` on the Pragmatic Engineer page) is all the precision the product offers, and one tracked writer (`bytebytego`) carried `null` for the band entirely. Any conversion-rate arithmetic built on a band is an estimate with a wide range.
- **The page the tools link to is not fetchable from every host.** `https://stackblade.app` answers 200, but `https://stackblade.app/categories` - the URL the refusal message prints - answered **403** to a direct request from this host and 401 through a reader proxy, so those links were not validated here. The MCP data is the evidence; the page is a convenience.
- **Rank events lag the follower events by twenty days** as measured above.
- **`change_30d` can be null** while `change_7d` is populated.
- **Version drift between the surfaces:** endpoint `stackblade` **1.1.0** against registry `io.github.whosman/stackblade` **1.0.0**.
- **No write surface at all**, which makes it safe to leave enabled in an unattended agent.

## What it costs

Everything readable is free without an account: 90 days of follower history per writer, ranks, recommendations, every category board with moves, the rising list, the activity feed, side-by-side comparison, a watchlist, badges, and public JSON for current numbers. Pro is **$18 a year** and adds a longer watchlist, digests by email, Discord, Telegram, a web address or a private feed, the full history of any writer as CSV and JSON, a filtered CSV export, API access with a licence key, and list import. Prices read from `https://stackblade.app/pricing` on 2026-11-20.

## Add it to Hermes

```bash
hermes mcp add stackblade --url https://stackblade.app/api/mcp
hermes mcp test stackblade
```

Then ask it the question a media buyer actually has: *which Technology newsletters are rising fastest this month, and how many recommenders do they have?* The same call also answers the question a writer has about their own page, which is why it earns a slot rather than being filed under marketing trivia.

## Why it earns a slot

Sponsorship and partnership decisions on newsletters are usually made on a screenshot of a follower count that a writer chose to share. This server replaces that with a dated series, a rank on a paid-subscriber board, and the recommendation graph around the publication - the three numbers that decide whether an audience is real, and the only three a writer cannot edit.
