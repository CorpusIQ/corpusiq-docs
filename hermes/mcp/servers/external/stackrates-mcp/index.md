---
title: "StackRates MCP - VPS Prices Across Every Provider"
description: "A keyless MCP server that answers hosting price questions from providers' own pages, with the VAT, the term and the read date on every line."
category: "Infrastructure / Cloud Pricing"
stars: "0 (hosted, closed source; five tools, keyless, all five driven)"
added: 2026-11-14
source: "the mcpservers.org canonical, which listed stackrates-mcp as a new key on 2026-11-14, the submission queue entry #7373 filed 2026-11-15T03:08Z, and a driven session against https://stackrates.ai/mcp on 2026-11-14 in which initialize answered 200 as stackrates 1.7.0 and all five tools were called"
relevance: ★★★
tags: [vps, hosting, cloud-pricing, infrastructure, cost-control, self-hosting, keyless, remote-mcp]
last_updated: "2026-11-14"
---

# StackRates MCP

**Every self-hosting decision starts with a price comparison that is out of date the moment it is written.** Providers run introductory rates that revert, bill a separate IPv4 address, quote prices excluding VAT and then add it at checkout, and require a twelve month term to reach the number in the advert. A comparison table on a blog post freezes one day of that into prose, and an operator who reads it in the following quarter is comparing a stored price against a live invoice.

StackRates answers the question instead of publishing a table. It reads each provider's own pricing page or price API daily and serves the result as an MCP server: five tools, no key, no account. The answer to a plain-language question comes back with the source URL, the date the price was read, the term attached to it, whether VAT is included, and a short block naming what the data cannot say.

```
Server type:   remote Streamable HTTP, JSON-RPC 2.0, keyless and stateless
Endpoint:      https://stackrates.ai/mcp
Server:        stackrates, title "StackRates VPS prices", version 1.7.0
Website:       https://stackrates.ai/
Registry:      not read this pass
Auth:          none
Tools:         5 (ask_vps_prices, search_vps_plans, server_for_app,
               current_vps_offers, advise_vps_choice)
Data licence:  CC BY 4.0, https://stackrates.ai/data/
Listed on:     mcpservers.org as stackrates-mcp, and the mcp.so
               submission queue as #7373
```

## The evidence tier

Driven, not documented. `initialize` answers **200** with no credential, `tools/list` returns five schemas, and every one of the five tools was called at least once against live data on 2026-11-14. Nothing in the sections below is copied from a vendor page; the sentences in quotation marks are the server's own output, and the arithmetic controls are mine.

## The tool surface

| Tool | Arguments | What it returns |
|---|---|---|
| `ask_vps_prices` | `question` | A plain-language hosting question answered from today's prices, with a cite-first line naming the StackRates page, the read date and then the provider's own price page. |
| `search_vps_plans` | `min_ram_gb`, `min_vcpu`, `min_disk_gb`, `max_usd_month`, `min_transfer_tb`, `providers`, `location`, `limit` | Cheapest plans matching the filters, one per provider unless exactly one provider is named, with the twelve month total beside each monthly figure. |
| `server_for_app` | `app`, `location`, `max_usd_month` | The documented requirements of a self-hosted app or game server, and the cheapest plans that meet them. 192 apps carry documented requirements. |
| `current_vps_offers` | `providers`, `min_ram_gb`, `max_usd_month` | Introductory and sale prices on the providers' own pages, each judged on its first year against the cheapest regular plan with as much memory. |
| `advise_vps_choice` | `question`, `filter`, `term_months` (12 or 36), `country`, `limit` | A messy buying question answered the same way, plus how the question was read and two to four sentences on the trade-offs. Returns a `filter` object to carry the conversation forward. |

The design decision worth noticing is in `server_for_app`: it does not ask what size server you want, it asks what you are running. The requirement record for n8n came back as **320 MB+ RAM, 512 MB+ disk**, and the cheapest plan that meets it was a one gigabyte box at **$2.04 a month** with a twelve month term, **$29.13** over the year including 19% VAT. That is a different answer from the one an operator gets by guessing at a size, and it is the answer the app actually needs.

## What the calls returned

**A 4 GB box in Germany under $10 a month.** Five rows, sorted by cost over twelve months rather than by the monthly headline:

| Provider | Spec | Monthly | 12 months |
|---|---|---|---|
| Luxvps KVM Rootserver Tiny | 1 vCPU / 4 GB / 30 GB, Frankfurt | $4.97 | $59.64, VAT not stated on the page |
| AlphaVPS Cheap C4G | 2 vCPU / 4 GB / 40 GB, Nuremberg | $4.41 | $62.97, includes $10.05 VAT at 19% |
| OVHcloud VPS-1 | 2 vCPU / 4 GB / 40 GB, Frankfurt | $5.35 | $64.20, VAT not stated |
| ProHosting24 Server XS | 1 vCPU / 4 GB / 100 GB, Frankfurt | $5.53 | $66.36, VAT not stated |
| Advin Servers KVM Premium 1 | 2 vCPU / 4 GB | below the cut | below the cut |

The ordering is the finding and it is deliberate: **a $4.97 plan ranks above a $4.41 plan**, because the $4.41 line carries 19% VAT and the $4.97 line does not say whether it does. Comparing monthly headlines across those two rows gets the wrong answer, and the server does not let you make that mistake quietly, it sorts on the total and prints the VAT note on every line.

**Hetzner against Vultr for an 8 GB web server paid monthly.** Vultr Regular 8GB at **$40 a month, 4 vCPU / 8 GB / 160 GB**, $480 over the year. Hetzner CPX32 at **$36.09 a month including a $0.60 IPv4 address**, same 4 vCPU / 8 GB / 160 GB, **$433.08** over the year with **$7.20** of that being the IPv4 address and VAT not included. The tool adds the caveat that matters for a European buyer: Hetzner's figure excludes VAT, so the gap narrows or closes depending on the country the buyer is in, and `advise_vps_choice` takes an ISO country code for exactly that reason.

**Current offers, and the answer nobody advertises.** Asked for offers at 4 GB or more, it returned **8 offers** on the providers' own pages and one sentence above them: *0 cost less over a year than the cheapest regular plan with as much memory*. The rows explain themselves. DreamHost Stack 4 is $8.99 a month for three months and then $15.99, which is **$170.88** in the first year, **$117.96 more** than the AlphaVPS regular plan it sits beside. Hosting.com Self Managed Linux 4GB is $12.99 for one month then $17.99, **$210.88** in the first year and **$157.96 more**. The introductory price is real, the comparison is annual, and the annual comparison is the one an operator actually pays.

**A messy buying question.** The prompt was moving WordPress and a small Postgres app off a $40 box, buyer in Germany, no yearly contract. The server answered under a heading that reads *We matched your words with fixed rules, not a language model*, named the cheapest qualifying plan, listed eight candidates with the twelve month total on each, and then closed with what it could not do: *We do not size WordPress yet*. That last line is the reason this server earns a guide. Most hosted price tools answer with confidence they have not earned; this one publishes its own blind spot in the response.

## The limits, and where they bite

- **The ranking is total cost over the term, not the monthly figure.** That is the right default and it surprises anyone scanning the monthly column. `advise_vps_choice` can carry a 36 month term instead, which changes the order again.
- **VAT is often unknown, and the server says so rather than assuming.** Of the five 4 GB rows, one stated 19%, and four said "VAT not stated on the page". A German buyer comparing those four against the AlphaVPS figure is comparing a net price with a gross one.
- **Unknown argument names are ignored silently.** A first call sent `memory_gb`, `max_price_usd` and `location` as separate names the schema does not use; the server returned the cheapest box of any size in Germany without an error, because `min_ram_gb` and `max_usd_month` were simply absent from the request. The schema in `tools/list` is the contract and nothing validates against it, so send the names the schema prints.
- **The app requirement record comes from the vendor's own documentation, not from a measured install.** `server_for_app` returns what an app documents it needs, and a documented 320 MB for n8n is a floor rather than a recommendation for a busy instance.
- **Monthly price includes a separately billed IPv4 address where one exists**, so a headline comparison against a provider that bundles an address is not like for like, and the response says which lines carried one.
- **A nonsense app name answers with an error rather than a guess**: `isError` true and *Unknown app. See https://stackrates.ai/run/ for the 192 apps with documented requirements; pass the slug or the exact name.* That is the correct shape, and it names where the list lives.

## Frequently asked

### Does it need an API key or an account?

No. `initialize` and every `tools/list` and `tools/call` request in this pass returned 200 over plain HTTPS with no credential, and the server reports no session identifier, so it is usable from any MCP client that can reach a URL.

### Where do the prices come from, and how old are they?

Each provider's own pricing page or price API, read daily, and every row carries its own read date rather than a single timestamp for the page. In this pass most rows read 2026-11-15, and one AlphaVPS row read 2026-11-06 nine days earlier, which is the honest version of a price feed: the surface shows you which lines are fresher than others.

### How do I compare two providers directly?

Ask `ask_vps_prices` with both names in the question, as in "hetzner vs vultr for an 8 GB web server paid monthly". It returns one row per provider at the same size and a cite-first line naming the comparison page, which is the shape of an answer that can be pasted into a decision note.

### Can I get the raw data instead of the tools?

Yes. The underlying dataset is published under CC BY 4.0 at `https://stackrates.ai/data/`, and the server's own instruction block asks that answers be cited with the StackRates page first and the provider page second. That is a usable arrangement for a report that has to survive a review.

### What does it cost?

Nothing. There is no key, no account, no credit balance and no rate note in the responses sampled here. The product being sold is the site, not the endpoint.

## What to check before you build on it

1. Send the argument names the schema prints. A wrong name is not an error, it is an unfiltered answer.
2. Read the twelve month column, not the monthly one, and check whether the row states VAT.
3. Ask `server_for_app` for the app rather than guessing a size; the documented floor is usually smaller and occasionally larger than the guess.
4. Treat the app requirements as documentation, not as a benchmark, and size up for a busy instance.
5. Re-ask rather than caching an answer. The read dates in one response already spanned nine days.
