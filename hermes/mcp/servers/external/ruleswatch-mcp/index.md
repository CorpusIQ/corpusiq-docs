---
title: "RulesWatch MCP - Prediction Market Rule Change Ledger"
description: "Every edit to the rules, resolution source, end date and title of Polymarket and Kalshi markets, with the words removed and added and the price at the edit."
category: "Prediction Markets / Compliance"
stars: "n/a (hosted vendor endpoint; MCP wrapper at github.com/whosman/ruleswatch-mcp)"
added: 2026-11-20
source: "the mcp.so submission queue entry #7689 filed 2026-11-20T06:36:00Z, a keyless initialize and full tools/list the same morning, nine driven tools/call requests (recent_rule_changes on three filters, search_markets, get_market on a live and a closed market, get_rule_change on two ids, get_watch_link, and two refusal paths), the official registry record io.github.whosman/ruleswatch 1.0.0, and the vendor's pricing page fetched to HTTP 200"
relevance: ★★★
tags: [prediction-markets, polymarket, kalshi, rules, surveillance, audit-trail, trading, remote, keyless, free-tier]
last_updated: "2026-11-20"
---

# RulesWatch MCP

**A prediction market is a contract whose terms can be rewritten while your money is in it. This server keeps the diff, with the price at the moment of each edit.**

```text
Server type:   remote Streamable HTTP, stateless (no Mcp-Session-Id issued)
Endpoint:      https://ruleswatch.com/api/mcp
Server:        ruleswatch 1.1.0, protocol 2025-06-18
Registry:      io.github.whosman/ruleswatch 1.0.0 (endpoint reports 1.1.0 - see version note)
Repository:    https://github.com/whosman/ruleswatch-mcp (HTTP 200)
Vendor page:   https://ruleswatch.com (HTTP 200, 35,556 bytes), pricing at /pricing (200)
Auth:          none for light use; a Pro key for automated use beyond a small free trial
Tools:         5, all read-only
```

## The problem it answers

Polymarket and Kalshi both let an operator amend a market after it opens: the resolution text, the resolution source, the end date and even the question. The venue page shows the version in force now. It does not show what the sentence said when you bought, or what the price was when it changed. RulesWatch is a record of those edits, and the shape of the record is the product: before, after, the words removed and added, the Yes price before the edit, at the edit and after it.

The `initialize` response states the boundary in one paragraph:

> RulesWatch records edits to the rules, resolution source, end date and title of Polymarket and Kalshi markets. ... Edits appear after a public delay. `get_watch_link` returns a link where a person can watch a market for rule changes; no tool creates a watch. Light use needs no key. Automated use beyond a small free trial needs a Pro key.

## The five tools

| Tool | Arguments | What comes back |
|---|---|---|
| `search_markets` | `query` (2 to 300 chars), optional `venue` (`pm` / `kalshi`) | venue, id, title, open or closed, Yes price, and the edits already recorded for each hit |
| `get_market` | `venue` + `id` | the rules in force now in labelled parts, the resolution source, end date, status, Yes price, and every recorded edit newest first |
| `recent_rule_changes` | `limit` (max **20**), optional `venue`, `kind` (`clarification` / `rules` / `source` / `dispute` / `dates` / `title`) | the newest edits with the removed and added words and the Yes price at the edit |
| `get_rule_change` | `id` | one edit in full: the whole before and after text on each changed field, the removed and added words, the price before, at and after, and the other markets carrying the same edit |
| `get_watch_link` | `venue` + `id` | a link a person opens to watch the market, plus what an alert covers and what each plan includes |

## A rule rewrite, measured

The clearest case from this pass is a Kalshi Formula 1 market, recorded at **2026-11-19T23:35:22Z**:

```text
market      Will Max Verstappen beat Lando Norris in the Las Vegas Grand Prix?
market_id   KXF1H2HLOTP-VEGAS26NORVER-VER
kind        rules
summary     More rules: 325 words added, 168 removed
price       Yes 0.500 before the edit, 0.700 at the edit
```

The text that went out was a flat tie-breaking list ("Non-Participation: ... all markets resolve to a fair market price. Both Disqualified (DSQ) ... 50/50"). The text that came in is an ordered procedure: results under FIA's official final classification, then a decision ladder that stops at the first rule that decides the matchup. Both versions are returned in full, alongside the price move that happened in the same window. That is the piece a venue page cannot give you, because the page only ever shows the version in force.

The same second holds four more records (`118495`, `118496`, `118500` and neighbours) for the other drivers in the same group, and the tool reports `same_edit_on_other_markets` as a count, so a family-wide rewrite is distinguishable from a single-market change.

A smaller, cleaner case sits on the same feed: a Kalshi New York grocery-store market got a one-sentence clarification on **2026-11-19T15:20:25Z** - 36 words added, nothing removed - defining "open to the public" as open to the general public and operating for its primary purpose, with auxiliary facilities explicitly not counting. The Yes price read **0.710** before that clarification and **0.725** at it.

## What a market record looks like

`get_market` on a closed Polymarket market (`pm` / `562802`, "Will the Democratic Party control the House after the 2026 Midterm elections?") returned the full rules in labelled parts, including the clause that decides a chamber with no majority: control goes to the party of the first elected Speaker of the Congress that convenes after the election. The market is closed with Yes at 1.0, and the record is still readable, which matters for anyone auditing an outcome after the fact.

## Where it stops

- **The feed is dominated by date churn, not rules.** All **ten** of the newest edits on the unfiltered feed were end-date moves, every one of them on a Polymarket esports market, and one Counter-Strike market moved its end time **five times inside 98 minutes** (`07:17Z` to `08:55Z`). Use `kind: "rules"` or `kind: "clarification"` for substance; the default feed is a heartbeat.
- **A kind exists that the filter does not offer.** `get_rule_change` on id `1` returned `kind: "resolution"` ("Outcome proposed", a UMA status change from `none` to `proposed`), while the `recent_rule_changes` filter enumerates only six kinds and does not include `resolution`. A caller filtering for disputes by enum will miss the resolution stream.
- **"Edits appear after a public delay."** That is the vendor's own sentence, and the tool does not publish the length of the delay, so a same-minute alert cannot be assumed.
- **The vendor names its own blind spot:** a clarification posted only on Discord or X, with no edit to the market, stays invisible until a trader links it on the market page. For a thin market that is exactly where the decisive statement tends to appear.
- **Automated volume needs a Pro key.** The `initialize` text says so and returns `Authorization: Bearer` in the same breath. The tools answered this pass without a key at 20-record pages, but a polling loop is a Pro use.
- **Version drift between the surfaces:** the endpoint reports `ruleswatch` **1.1.0** while the registry record `io.github.whosman/ruleswatch` is **1.0.0**. Quote the endpoint when describing behaviour.

## Refusals, measured

```text
get_market  pm / 999999999
  found: false
  "No Polymarket market with id 999999999 is tracked, and Polymarket does not list one.
   The id is a number; search by title words to find it."

search_markets  query "x"
  isError: true
  "Invalid arguments: query is too short: send at least 2 characters."
```

Both name the fix, which is what an agent needs to recover without a human.

## What it costs

Free covers the feed of every edit, market pages and the record, a watchlist with **one** market, alerts to one Discord channel and private RSS. Pro is **$149 a year** - card or 149 USDC on Base - and adds up to **1,000** watched markets checked within a minute, following your Polymarket wallet, webhook alerts to up to five channels, CSV and JSON export, and the API key. Prices read from `https://ruleswatch.com/pricing` on 2026-11-20.

## Add it to Hermes

```bash
hermes mcp add ruleswatch --url https://ruleswatch.com/api/mcp
hermes mcp test ruleswatch
```

Then ask the question that started this: *did the rules on this Kalshi market change after I bought, and what did the price do when they changed?*

## Why it earns a slot

This catalog carries venues and data feeds for prediction markets, but nothing that treats a market's terms as a document with a revision history. The two most expensive disagreements in this asset class are both about wording - what the sentence said, and when it changed - and both are answerable from this record. For anyone who holds a position, or reports on one, that is the difference between an opinion and a citation.
