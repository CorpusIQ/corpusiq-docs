---
title: "MCP Server Discovery - November 26, 2026 (Evening)"
description: "A directory flat to the key but up 101 raw entries, four feed cards, thirty-three filings, and two new guides driven end to end."
category: "MCP Ecosystem"
last_updated: "2026-11-26"
---

# MCP Server Discovery - November 26, 2026 (Evening)

Fired on the **21:00 MST** tick, eleven hours after the [midday pass](/hermes/mcp/sweeps/sweep-november26-2026-midday) and ten after its [supplement](/hermes/mcp/sweeps/sweep-november26-2026-midday-supplement) closed, into a window that added **101 raw `<loc>` entries** and **not one new server slug**: the thirteen numbered server maps returned **38,251** entries against **38,150** at midday, the per-map distinct counts were unchanged at their caps, and the union held at **24,528**. The one apparent arrival is a **slug normalisation** of a server already held. The productive surface was the submission queue, **#8181 to #8213**, and the feed's late rotation, which produced the two guides below.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, 17 maps named, 13 numbered server maps
raw <loc>, maps 1..13         38,251   against 38,150 at the 10:00 MST midday read
  servers/1  ..... 4,134      servers/8  ..... 2,774
  servers/2  ..... 2,503      servers/9  ..... 2,604
  servers/3  ..... 2,952      servers/10 ..... 2,536
  servers/4  ..... 3,162      servers/11 ..... 2,515
  servers/5  ..... 3,332      servers/12 ..... 2,398
  servers/6  ..... 2,894      servers/13 .....   528
  servers/7  ..... 5,919      sum ............ 38,251 exact
distinct keys per map        1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7 / 528
server-map distinct slugs    24,494   unchanged
priority-servers.xml         251 raw / 34 keys
remote-mcp-servers.xml        15 raw /  1 key
union of keyed slugs         24,528   identical to the midday read
lastmod pairs, server maps   38,251
  at or after 10:55:14Z           419 rows -> 347 distinct slugs
  of those, not in the baseline     1   -> sparten11740/mc-blockpilot
  newest anywhere            2026-11-26T23:02:40Z
```

**The 101 raw entries are duplicates, and the diff proves it.** Against the stored `20261126_1100` baseline the set difference is **one addition and one removal**, and the pair is the same server in two spellings: `sparten11740/mc-blockpilot#mcp-for-ai-agents` left and `sparten11740/mc-blockpilot` arrived. The **419** stamped rows that are at or after the midday top collapse to **347** distinct slugs, of which exactly one is new to the baseline, so the rest are restamps of slugs already catalogued. **A raw-count rise with a zero set-delta is the shape of a re-index, not a wave**, and this pass measured both rather than trusting the larger number.

## The feed rotated late, and its URL shape changed under the reader

`mcp.so/feed` answered **200** at **159,662** bytes with **36** distinct slugs and **30** paired stamps. Four cards arrived after the midday read and one re-appeared:

- **sourcemed** at **08:42 PM** UTC, a free source-verified medical evidence library, **9,534** topic shelves and **33,429** evidence cards, listed as Verified and Featured
- **cryptonews-is** at **08:50 PM**, crypto news as data, **18** tools
- **movemate-gym-workout-tracker-30aad5** at **11/27 12:16 AM**, a consumer gym training log
- **busca-para-agentes** at **11/27 12:53 AM**, a Cloudflare-compatible `/.well-known/search` endpoint for Next.js sites
- **wayvz-sms** re-appeared at **08:23 PM**, the card the midday pass held on the business-telephony class, still held

**The extractor that read this page for three passes returned zero cards against a document carrying thirty-six, and the cause is a one-character move:** feed anchors changed from `/server/<slug>` to `/servers/<slug>` during this window. The byte count barely moved (**160,433** at midday, **159,662** now), so nothing about the page size would have flagged it. A slug reader that keys on the old prefix reports a dead feed rather than a moved href, which is the same failure class as the seconds-keyed stamp reader from the night pass: **a parser is a claim about a page that no longer holds**.

## The queue carried thirty-three filings

`chatmcp/mcpso` issues **#8181 to #8213** in the window, the newest filed at **2026-11-27T02:32:08Z**. The queue host that was **NXDOMAIN** for the midday supplement answered again through the GitHub API, so the outage was a DNS edge condition rather than a lost filing stream, and every filing that accumulated during it is now visible. The distribution is the usual one: remote streamable-HTTP endpoints with a registry name, a fleet of Apify-hosted DirectAPI Labs actors filing six endpoints in four minutes, and local stdio packages.

## Two ships

- [Dealport MCP - 28M US Companies Behind a Free Preview](/hermes/mcp/servers/external/dealport-mcp/) - **41 tools read keyless, six `preview_companies` calls driven, a rate card read as an MCP resource.** 28M+ US private businesses and properties from state registries, UCC filings, CMS cost reports, SEC Form ADV and NYC property records, sized for **$0.00** before a record is bought at **$0.01** and an owner contact at **$0.09**. **The finding that matters is the count:** four filter shapes returned exactly **10,000** with `matching_count_more: true`, including a three-letter name prefix that cannot describe ten thousand companies, while the sample rows visibly narrowed, so the one number the free tier exists to produce cannot compare two buy-boxes. `state: "ZZ"` returns a clean zero with `tam_gate_passed: false` and no error, `industry` is null on two of five sample rows in two states, a bare `naics` filter answers `search_too_broad`, and `remaining_balance_usd` is **null** rather than zero on an unauthenticated call. The paid 40 answer **401** with `resource_metadata` pointing at a protected-resource document, so the wall is discoverable, and `dealport://rate-card` publishes every price before it is spent.
- [GPU Cloud Prices MCP - What an H100 Hour Costs Right Now](/hermes/mcp/servers/external/united-compute-gpu-prices-mcp/) - **4 keyless read tools, eight calls driven across all four**, covering **1,044 offers for 76 GPU models across 59 clouds**, refreshed every fifteen minutes. The cheapest rentable H100 SXM was **$0.55** on Clore.ai in Russia and the cheapest datacenter H100 was **$2.4236** on Fluence, a **4.4x** spread on the same nominal unit, with Vast.ai at **$1.7356**, GPU.ai at **$2.23**, Hyperstack at **$2.50**, and an in-stock list of **20 of 33 offers across 18 providers**. A `min_vram: 48` and `max_price: 1.00` query returned **20** offers led by an L40 at **$0.33**, which is the shape that answers an inference budget. `get_gpu` on `mi300x` returns `cheapest_price_per_hour: null` with `offers_in_stock: 0` and the advertised `$1.00` preserved in `offers_not_available`, **null is not zero**. Four defects recorded: a region filter matches an offer rather than a price (Lium's B200 at $5.50 appears in a Europe query carrying France, Israel and the US in one region list), `reseller` is present on some rows and absent on others, `mi350x-288gb` reports **294** GB of VRAM against the 288 in its own id, and the tracked count of **76** against **71** rentable is a default-flag difference with nothing in the payload saying so.

## Documented, not driven

**Leadscol** (`app.leadscol.com/mcp`, registry `com.leadscol/leadscol`) is the B2B database of Colombia: **3.6 million** active companies, OAuth 2.1, a free account with **50 credits** and no card. `initialize` answered **401** with the Spanish body *"sin autorizar: conecta el servidor con tu cuenta de Leadscol (OAuth) o usa una llave de API de Créditos y plan"*, so every tool sits behind the grant and nothing could be driven this pass. It is the second jurisdiction-scoped company database the catalog has met in a day, after Leadgen's ONRC Romania, and the contrast is the note for its guide: Romania answered keylessly and Colombia answers only inside an account. Held pending a credential rather than on class.

## Held this pass

**SourceMed** is the card worth a line, and not for its content. It reads as a free, source-verified medical evidence library with **9,534** topic shelves and **33,429** evidence cards, which is a clinical audience rather than an operator one, so the hold is on audience and would stand on that alone. **What nearly hid it is a name collision:** a first grep for the slug matched the *SourceMedium* guide and sweep entries from November 10, a different vendor entirely, so a name-based search reported the card as already dispositioned when no page covers it. The slug-versus-name search artefact is a recurring one in this catalog, and this pass adds the near-miss form: two vendors whose names differ by four letters.

**cryptonews-is** (crypto news, 18 tools), **movemate** (consumer gym log) and **busca-para-agentes** (an agent-discoverability endpoint for Next.js sites) are out of scope for a business-answer catalogue and are recorded rather than catalogued.

## What this changes about the method

**Two silent readers failed in one pass and both were caught by a total, not by the code.** The feed parser reported zero cards against a page carrying thirty-six because one href prefix moved, and the name collision reported an unshipped card as shipped because one vendor name contains another. Neither would have raised an error; both were visible only because the page was re-read by hand and the counts were compared. The rule that survives: **when a total disagrees with a listing, the reader is the first suspect**, and a zero from a parser is a measurement of the parser until proven otherwise.
