---
title: "MCP Server Discovery - November 15, 2026 (Night)"
description: "A directory that moved by one duplicate URL and thirteen queue submissions, where the two ships are a drawing server and a fee calculator and both are decided by arithmetic."
category: "MCP Ecosystem"
last_updated: "2026-11-15"
---

# MCP Server Discovery - November 15, 2026 (Night)

Fired on the **03:00 MST** tick, five hours after the evening sweep closed at 21:02 MST. The directory moved by **one raw URL entry** that is a duplicate of a listing it already carried, the feed carried nothing above the cutoff stamp for the first time this week, and the submission queue carried **thirteen** arrivals. Two servers ship, and neither ships on a feature list: one is decided by FIPS codes that come back correct, the other by **32** cost rows that recompute to the cent.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, twelve of them server maps
raw <loc> entries, maps 1-11     65,045   against 65,044 at the 21:02Z capture (+1)
per-map counts                   7,588 / 5,949 / 6,518 / 6,744 / 6,952 / 6,756 /
                                 9,351 / 6,590 / 4,030 / 2,607 / 1,960
per-map movement                 servers/2 5,948 to 5,949, the other ten held exactly
distinct keys, locale-stripped   21,325   against 21,325 = identical
priority-servers.xml             200 with 299 entries and 34 distinct keys
union of both maps               21,359 = the retained canonical exactly
set diff                         0 additions, 0 removals
URLs per surviving key           3.05
newest lastmod                   2026-11-15T08:30:32Z (trycua/cua)
lastmod at or after 04:02Z       191 rows, 67 distinct listings, all already present
mcp.so /feed                     200 at 156,327 bytes, 36 anchors, 30 stamped cards
                                 newest stamp 11/15/2026 03:03 AM UTC, 0 above 04:02Z
submission queue #7374 to #7387  13 arrivals, #7380 returns 404
```

## One raw entry, and it is not an arrival

The eleven numbered maps returned **65,045** raw `<loc>` entries against the **65,044** those same eleven carried at the 21:02 capture. The whole movement sits in `servers/2`, from **5,948** to **5,949**, and the ten other maps are identical to the entry, including the `servers/9` correction at **4,030** and the `servers/11` wave at **1,960** that the previous two passes read.

That single entry did not add a key. The distinct locale-stripped key set reads **21,325** on both captures, which is exactly what the evening pass reported, so the added `<loc>` is a second URL form for a listing already in the index. The two-map union closes the arithmetic: `priority-servers.xml` answered **200** with **299** entries and **34** distinct keys at `/sitemaps/priority-servers.xml`, which is where the index no longer routes it, and the union of the eleven numbered maps with that priority map is **21,359** keys, the exact size of the canonical retained from the evening pass. **Zero additions, zero removals** on the basis that counts, with nothing left over to explain.

The **34** keys that are absent from the eleven-map basis and present in the canonical are all thirty-four of the priority map, verified one by one in this pass rather than assumed from the prior pass's note. A key missing from a slice of the index is a slice, not a delisting, and this is the arithmetic that says so.

**The stamps were busy and carried no arrivals.** **191** `lastmod` rows sit at or after the **04:02Z** cutoff, collapsing to **67** distinct listings, and every one of the 67 was already in the canonical set. The newest is **2026-11-15T08:30:32Z** on `trycua/cua`, which is a re-index of a repository this catalog has read before. A stamp on this surface remains a description of when the page was re-read, and reading it as a discovery is how a quiet window becomes a false claim.

## The feed, nothing above the stamp

Read at **156,327** bytes with **36** card anchors, **30** cards carrying a stamp in the `M/D/YYYY, HH:MM AM/PM` UTC form and **27** distinct stamps, because three slugs are stamped twice. The newest stamp is **11/15/2026, 03:03 AM** on `cartesian-ecu`, which is the card the evening pass dispositioned, and **zero** cards sit above the **04:02Z** cutoff. The five cards at the top of the feed are the same five products the 21:00 sweep held: `cartesian-ecu`, `facet`, `social-fetch-d3f5b8`, `naturepedia-canonical-discovery-mcp-server` and `hiapi-remote-mcp-73ef07`. No new card, no re-stamp, nothing to re-open.

## The queue, thirteen arrivals

Read from **#7374** to **#7387** with bodies in one authenticated call. **#7380** answers **404** on the API and is recorded absent rather than skipped.

**Shipped - ChartAnt** (`#7374`). Charts and maps as hosted images. Keyless, stateless, `ChartAnt` **0.4.0**, **51** tools, **nine** driven. The pass that earns a guide here is not the chart count but the two place tools underneath the maps: `match_places` returned **3 of 3** German states as `Bavaria (DE-BY)`, `Baden-Württemberg (DE-BW)` and `Saxony (DE-SN)`, **3 of 3** Georgia counties as **13121**, **13089** and **13135**, and `locate_points` resolved three coordinates to Paris **FR-75**, Fulton County **13121** and New South Wales **AU-NSW**. Correct geography is what makes a choropleth a document rather than decoration. The world map came back as a **1920 by 1080** PNG of **187,175** bytes and was inspected rather than trusted: Natural Earth boundaries, the United States darkest and labelled **88K EUR**, a stepped legend from **15K** to **88K**, every uncoloured country grey under a `No data` swatch. Every response also carries an editable PowerPoint chart and an Excel workbook, both fetched at the right MIME types. **The limit that matters is a clock:** keyless links expire in an hour by the server's own note, and `create_living_chart` without an account answers *NOT SAVED* and draws a one-off anyway.

**Shipped - CryptoExchangeIn** (`#7386`). All-in trading cost by mode plus a per-country regulatory matrix. Keyless, `cryptoexchangein` **1.0.0**, **six** tools, five driven. **32** cost rows at a 10,000 dollar amount recomputed as `rate_pct x amount / 100` and matched to the cent, with the ranking strictly ascending in all four modes. **The finding is the mode, not the venue:** the same OKX trade costs **$10.00** as a spot taker and **$165.00** as an instant card buy, a factor of **16.5**, and Coinbase Advanced is the most expensive line in every mode at **0.60%**, **0.40%**, **0.10%** and **3.55%**. India came back with **FIU-IND under PMLA**, **30%** flat under Sec 115BBH plus **1%** TDS under Sec 194S, INR IMPS and NEFT on domestic venues, and a matrix where every service is `conditional` with its own guide URL. **Two defects recorded:** the `country` argument wants a slug and fails silently on an ISO code, so `IN` is echoed as `in` and returns **0** ranked rows where `india` returns **4**; and every row carries a referral code, a direct referral URL and a `go_url` stamped `utm_source=mcp`, with `list_providers` carrying a `we_get` field that names the commission - the sort is on cost, proven by CoinDCX ranking second on instant buy with no referral at all, but the reader should see the economics.

**Held, with the owner named.**

**SEO Rank Fixer** (`#7381`) holds twice over. Its endpoint measures the gate first: `initialize` at `https://seorankfixer.com/api/mcp` answered **401**, which is the OAuth tier with nothing driven beyond it. And the class is owned here in the strongest sense available: Search Console and Bing analytics, SEO fixes ranked by estimated clicks and AI-answer citation checks is the ground [Geolint](/hermes/mcp/servers/external/geolint-mcp), [LogNorm](/hermes/mcp/servers/external/lognorm-mcp), [CiteRank](/hermes/mcp/servers/external/citerank-mcp), [AEO Engine](/hermes/mcp/servers/external/aeo-engine-mcp), [Creavores AEO](/hermes/mcp/servers/external/creavores-aeo-mcp), [HarborRank](/hermes/mcp/servers/external/harborrank-mcp) and [SEO Audit Console](/hermes/mcp/servers/external/seo-audit-console-mcp) occupy, and it is also the ground CorpusIQ itself sells on.

**The Veil Press** (`#7387`, `com.theveilpress.www/veilpress` **2.0.0**) is the closest call of the window and the strongest hold. Keyless, **five** tools, driven through `search_stories`: the query `sanctions` returned **8** results, each with a `cite_as` line of the form *The Veil Press, \<headline\>, \<url\>*, and the top summary does the thing this catalog keeps asking for - it reports that the Treasury Secretary said Iran's economy is *collapsing* and then states that Treasury's own releases from 15 and 21 October call it *failing*, and that **neither** says collapsing. That is a fact-check inside a news feed. It holds anyway on the **news class**, already carried by [APITube News](/hermes/mcp/servers/external/apitube-news-mcp), [Financial News](/hermes/mcp/servers/external/financial-news-mcp), [NewsMind](/hermes/mcp/servers/external/newsmind-mcp) and [Webz News Search](/hermes/mcp/servers/external/webz-news-search). The promotion test is recorded: this earns a file the moment the catalog needs an *original reporting with numbered primary sources* owner rather than a news search owner, because the citation discipline is the differentiator and not the headlines.

**No Stairs Please** (`#7385`) is keyless with **eight** tools and it answers: `search_venues` for jazz in Washington returned **7** venues with room capacity, step-free load-in, note counts and dated show history (Dimitriou's Jazz Alley at **350** capacity with **73** show days logged). It holds on two grounds. The fields an operator would pay for are metered: `reveal_venue` unlocks booking contacts and music days for **7** days against a credit balance, and the anonymous tier showed **4 of 4** free reveals remaining. And the class is a single-vertical directory, sitting beside the venue and events surfaces already carried rather than opening a new capability.

**Towerwatch** (`#7376`), **Yield Desk** (`#7377`) and **Precio Real** (`#7378`) are one publisher's three listings and all three measured to the same gate: `initialize` answered **401** with error code **-32001** and the body *missing or unknown key: send Authorization: Bearer (get a key in the bot)*. Two of them are the same data under two names - Mexico City sale ads ranked by estimated Airbnb net yield, explicitly *Same data and server as Towerwatch* - which makes the pair one product with two front doors, and both are credit-metered per tool call through a Telegram bot. No keyed session exists here, so nothing beyond the handshake is measurable and the guide would be a description of three marketing pages.

**Held without an endpoint to probe, each by its own reason.** **Syncky Health** (`#7375`) is local stdio over `npx -y @syncky/agent` and reads Apple Health through a paired iPhone app, so the data source is a phone that is not here. **Dinoctor** (`#7379`) exposes its MCP server as a flag on a desktop application binary (`Dinoctor --mcp`), macOS or Windows installed, which is the unlocked-desktop-app disposition recorded before. **Stratos** (`#7383`) runs a local Streamable HTTP endpoint on `127.0.0.1:9921` inside a proprietary macOS PHP environment, with the runtime inspection and execution tools behind a Pro tier. **Punchcutter** (`#7384`) is a pip install from git with a Studio app beside it, in the design tooling class. **nogpu** (`#7382`) is a developer-laptop measurement utility that wants a JSONL corpus of past model decisions uploaded before it can say anything, and sells the kept model for **$99**; it is tooling for choosing a model, not a data surface for a business. All five are recorded so the next pass does not re-open them blind.

## What the window says

The directory contributed **zero keys and zero products**, and this time it did it while adding a URL, which is the cleanest demonstration available that a raw entry count describes an index rather than a market. The feed contributed nothing above its cutoff for the first time in this week's passes. Everything that shipped came out of the submission queue, and everything that shipped was decided by a computation somebody could repeat: FIPS codes and ISO subdivisions for one, a thirty-two row cost table for the other.

Both guides also carry the same warning in different clothes. ChartAnt's images expire in an hour without an account, and CryptoExchangeIn's ranking sits inside an affiliate payload that states its own commission. A tool that is useful and also selling something is normal in this ecosystem; the catalog's job is to print the price tag next to the capability, not to pretend the price tag is not there.

## 🆕 November 15, 2026 - Night (2 New, 2 Guides)

A five-hour window in which the canonical added one duplicate URL, the feed added no card, and thirteen queue arrivals produced two ships decided by arithmetic rather than by claims.
