---
title: "BADideas.fund MCP - CEE Pre-Seed Fund and Portfolio"
description: "A Central and Eastern European pre-seed and seed fund on an eight-tool keyless server: portfolio, funding medians and a deck review in the chat."
category: "Finance"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-25
source: "Submission chatmcp/mcpso #8036 filed 2026-11-25T04:36:43Z; registry record fund.badideas/mcp 1.0.0 with the remote https://badideas.fund/mcp; a keyless initialize and a full tools/list on https://badideas.fund/mcp read 2026-11-25; list_portfolio, search_website and ask_question driven the same day; the vendor site badideas.fund for the fund terms"
relevance: "★★★"
tags: [founders, venture-capital, fundraising, funding, startups, portfolio, cee, remote-mcp]
last_updated: "2026-11-25"
---

# BADideas.fund MCP

**A founder asking a fund for money starts with the same three questions every time: what does this fund write, what does it want to see, and what happens to my deck after I send it.** BADideas.fund is a pre-seed and seed fund for Central and Eastern Europe, and its MCP endpoint answers those questions from the fund's own published material, lists the companies it backs, and runs a written deck review before the founder has spoken to anyone.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://badideas.fund/mcp
Auth:        none for every tool read; the write tools take the founder's own details
Registry:    fund.badideas/mcp 1.0.0
Pricing:     not stated on the server; the fund publishes no paid tier for the MCP endpoint
Tools:       8, read from a keyless tools/list
```

## What the server measures clean

This is the rarest gate in this catalog: **none**. An anonymous `initialize` answers **HTTP 200** with protocol `2025-06-18` and serverInfo `badideas-fund 1.0.0`, and the same keyless session returns the whole tool list:

| Tool | What it needs | What it does |
| --- | --- | --- |
| `list_portfolio` | nothing | the companies the fund shows publicly, newest first |
| `search_website` | `query` | searches the fund's answers, blog posts and reports for founders |
| `ask_question` | `question` | asks the fund's Founder Terminal, answered only from its own material |
| `request_human_answer` | `thread_id`, `email` | when `ask_question` returns `not_covered`, asks the team to write the answer |
| `review_deck` | nothing, or `review_id` | a written deck report: score, what works, what to fix |
| `start_deck_upload` | nothing | a one-time PUT link for a PDF deck up to 20 MB |
| `submit_pitch` | `email`, `linkedin_url`, `startup_name` | files the pitch with the fund |
| `subscribe_newsletter` | `email` | the founder newsletter |

The `initialize` response carries an unusually careful `instructions` string, and it is worth quoting because it is the design decision an operator should see: *"Tool names, ids and upload links are internal to this server. Founders know these services as: pitching the fund, a deck review, the Founder Terminal, a written answer from the team, and the newsletter."* The vendor is telling the assistant to translate its own API into the founder's vocabulary, and to keep `thread_id` and `review_id` out of what the founder reads. An operator wiring this into a workflow gets a usable surface and no prompt to explain.

## The portfolio, read in one call

`list_portfolio` returned **40 companies, most recent first**, each with a one-liner, headquarters and an investment date. The first ten:

| Company | HQ | Invested | What it does |
| --- | --- | --- | --- |
| Tapaya | Czechia | Apr 2026 | turns apps and NFC devices into payment terminals for in-store payments |
| BuilderBase | Sweden | Mar 2026 | infrastructure and marketplace for organizing builder events |
| Spotwise | Latvia | Feb 2026 | AI-powered ad monitoring for broadcast sales teams |
| Amorphous AI | USA | Feb 2026 | structuring healthcare data for hospital decision-making |
| Just 4 Noise | USA | Feb 2026 | generative models that let creators generate instruments |
| WhiteBridge AI | Lithuania | Dec 2025 | online identity verification and reputation insights |
| Port | Poland | Dec 2025 | hub-based e-bike rentals for last-mile delivery couriers |
| DesktopCommander | Latvia | Oct 2025 | workflow and code execution automation in plain English |
| Frankly Insure | Denmark | Sep 2025 | embedded insurance at point of sale and in-app |
| Juo | Poland | Sep 2025 | subscription infrastructure for D2C brands |

Two readings matter for a founder sizing the fund. The headquarters list is not confined to the CEE countries the fund's front page names, so the geography is wider than the pitch line. And the dates give a cadence: five investments in the first quarter of 2026 alone, which is the number to put against the fund's stated check size when you decide whether it can lead your round.

## The funding numbers the fund publishes

`search_website` does not return links only. It returns the numbers, and the answers are dated to the fund's own research:

- Median round closed by CEE startups from January to September 2026: **€380,000 at pre-seed, €2 million at seed, €7.1 million at Series A**. Baltics seed medians were **€2.8 million in Estonia** and **€1.9 million in Lithuania**.
- What CEE pre-seed founders ask for: about **€400,000**, with half asking between **€220,000 and €640,000**.
- Runway planned by pre-seed founders in 2026: **18 months**, against **12 months in 2025**.
- Planned use of a pre-seed round: **34% product and technology, 30% sales and marketing, 17% people and running costs**.
- What goes wrong after a CEE pre-seed round: finding customers, named as a problem in **86%** of the fund's calls with the founders it backs, more than any other area.

An operator who runs a services business in the region can use those medians as a benchmark for what a client is likely to have raised, and any founder can check an ask against the range before a first meeting.

## Asking the fund directly

`ask_question` answered a real question with citations and an honest negative:

> **What stage and cheque size do you invest at, and do you lead rounds?**
> We invest at pre-seed and seed, with a first check of **€200K to €1.5M**. We write the first institutional check, and each investment has one deal lead who runs the process.
> On leading rounds, our data does not show BADideas as a lead. In Latvia, BADideas.fund joined 4 pre-seed and seed rounds since January 2025 and led none. Our round record has no entry in its "Led" column either.

Every claim arrives numbered against a source URL, and the second block of the result carries the `thread_id` that continues the conversation. The refusal to claim lead status is the useful part: a founder who needs a lead investor now knows to bring one, and the answer is checkable at the fund's own round record rather than taken on trust.

The vendor site adds the terms the tools do not restate: **40+ companies backed since 2022**, a **22-day median from first meeting to term sheet**, a go-to-market review in the first 30 days after an investment, and software only, built on the application layer rather than on a model.

### Does the deck review cost anything or need an account?

No account is needed to call `review_deck`, but the tool needs the deck itself. `start_deck_upload` returns a one-time link and `review_deck` returns the written report, or a `review_id` to call again while the review is still running. Nothing in the tool list asks for a card.

### Which tools actually change something on the fund's side?

Three do, and an agent should treat them as writes: `submit_pitch` files a real submission, `subscribe_newsletter` adds an address to a mailing list, and `request_human_answer` asks a person at the fund to write back. The `subscribe_newsletter` description asks for consent on exactly this point, *"only use an address the person gave you for this, with their consent."*

### Is this useful to anyone who is not raising money?

Yes, for the market data. The medians by stage and country, the runway shift from 12 to 18 months, and the 86% go-to-market finding are the kind of numbers a consultant, an accountant or a buyer of software companies in the region otherwise pays a data vendor for.

## How this fits a CorpusIQ answer

A founder's assistant with this server connected can answer "who funds pre-seed in Poland and what do they write" from the fund's own record, then compare the check against the CEE median it publishes. That is the shape CorpusIQ is built for: the same question, answered from the source, with the number traceable to the page it came from.

## See Also

- [WeightedShares MCP - SEC Buybacks and Stock Compensation](/hermes/mcp/servers/external/weightedshares-mcp/) for the disclosure side of a company's numbers
- [Investor Shelf MCP - Funders, Deals and Cited Reports](/hermes/mcp/servers/external/investorshelf-mcp/) for the wider funder directory behind a paid key
