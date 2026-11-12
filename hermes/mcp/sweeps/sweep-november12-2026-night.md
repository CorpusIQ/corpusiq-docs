---
title: "MCP Server Discovery - November 12, 2026 (Night)"
description: "A flat canonical proven by three numbers, and four entries that came from the feed and the queue - signup checks, portfolio borrowing, splits and analytics"
category: MCP Ecosystem
added: 2026-11-12
last_updated: 2026-11-12
source: "the mcpservers.org sitemap index re-read at 2026-11-12T10:03Z with the twelve server maps fetched individually and every lastmod compared against the 05:03Z capture, the mcp.so feed re-read cache-busted at 143,129 bytes and parsed card by card from the M/D/YYYY stamp in the title attribute, the chatmcp submission queue read from #7163 to #7192 in one authenticated call, the official MCP registry queried for twelve candidates by product name and by namespace, and live sessions on this host: three keyless endpoints driven to tools/list and eleven tools/call requests between them, and one endpoint measured to both OAuth metadata documents"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 12, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the night pass read the same surfaces. The canonical was flat, and this pass can prove it three ways rather than assert it. Every product that shipped came from somewhere else: two from the submission queue, two from the feed.

```text
Surfaces:   /sitemap.xml 200, fifteen maps named, twelve carrying /servers/ URLs
            64,573 raw <loc> entries in those twelve, against 64,570 at 05:03Z
            per-map: priority 299 (held), 1 7,588 (held), 2 5,948 (held), 3 6,518 (held),
            4 6,744 (held), 5 6,952 (held), 6 6,756 (held), 7 9,351 (held), 8 6,589 (held),
            9 4,031 (held), 10 2,606 (held), 11 1,191  (+3 raw)
            distinct locale-stripped keys 20,885 = 20,885, 0 additions / 0 removals
            lastmod at or after 05:03Z: 0 rows
Feed:       143,129 bytes, 30 stamped cards, 35 anchors, 3 above the cut-off + 1 unstamped
Queue:      #7163 - #7192 in one call, 12 created at or after the night read
Catalogued: 4 servers, 4 guides   Held: 20+ with the class owner named
Crossref:   12 candidates through the registry, by name and by namespace
```

## The window: three entries more and no key more

The sitemap index answered **200** and named fifteen maps: `static.xml` (822) and `skills.xml` (12,579) are counted but are not servers, `remote-mcp-servers.xml` carries 15, and the twelve maps that carry `/servers/` URLs are the universe. Eleven of the twelve returned exactly their 05:03Z counts and `priority-servers` held at 299. Only `servers/11` moved, from **1,188** to **1,191**.

The count and the set disagree, and the disagreement is the finding:

```text
raw entries        64,573   (+3)
distinct keys      20,885   (=  , 0 additions / 0 removals)
lastmod >= 05:03   0
```

Three raw entries arrived and no new key did, which means the entries are re-served under locale or fragment forms that normalise onto keys already counted. A `lastmod` scan across all twelve maps returned **nothing** at or after the cut-off, so nothing was published on this surface in the window. The three numbers together are a stronger statement than the entry count alone: an arrival would have had to produce a stamp, and there is no stamp.

## The feed: three fresh cards and one that is not stamped yet

The mcp.so feed answered **200** at **143,129** bytes - less than half the night pass's 289,791, which is a shorter page rather than a quieter one - with **30** stamped time spans and **35** card anchors. Three cards sit above the 05:03Z cut-off:

```text
11/12/2026, 08:40 AM   tracwell                        catalogued
11/12/2026, 06:32 AM   internal-ballistics-calculator   held, hobby calculator
11/12/2026, 06:29 AM   twinr-mcp-server-59fa64          held, app-builder class
(no stamp)             billdog-io                       held, OAuth-gated
```

The first card carries no relative-time span at all, which is what a listing looks like between publication and the first stamp refresh; it was triaged as **billdog-io**, whose endpoint at `https://api.billdog.io/mcp` answers a keyless `initialize` with **401**, JSON-RPC `-32001 Bearer token required` and `WWW-Authenticate` naming `/\.well-known/oauth-protected-resource/mcp`. The next card below the cut-off, `trainrec` at **04:41Z**, landed after the night pass read the surface at 04:01Z and before its 05:03Z capture, so it belongs to that pass's tail; it was triaged as a consumer workout log and held.

## The queue: twelve arrivals, and the fleet that keeps coming back

The submission queue was read from **#7163** to **#7192** in one authenticated call. Twelve were created at or after the night read, and they decompose into three groups of one, one fleet of five, and the rest class-covered. The fleet is the `mambalabsdev` set at **#7181** to **#7185**: Semrush domain metrics, a YouTube channel email finder, property-owner records, Ticketmaster event prices and an Eventbrite scraper - the fourth wave of the same one-tool-per-actor pattern this catalog has held since October 7, now **43** across four waves. The rest are named in the catalog's also-identified paragraph with the class owner beside each.

One queue entry deserves its own line because it is the strongest vendor of the window and it was not catalogued: **Diffbot**, `io.github.diffbot/diffbot-mcp` at `https://mcp.diffbot.com/mcp`, a long-established web-data extraction vendor with a real remote server, held because tool use needs a free Diffbot token and no token was provisioned for this pass. The hold is on evidence, not on merit, and it is the first target of the next pass.

## Shipped: four entries, three of them driven

**Vetto** answers the signup question before the account exists. Four keyless tools, six calls driven, and one rule that only shows itself when two answers are read together: `billing@mailinator.com` blocks for `role` and `disposable` while `team+1@googlemail.com` allows with `role` recorded, so a role address alone is not a verdict. `check_email` on `jdoe@gmail.co` returned the typo suggestion that saves the customer rather than a rejection, and `how_to_block` returned a server-side recipe that ends with the instruction to fail open on timeout.

**Haven Financing** answers the borrowing question with arithmetic: a **200,000** draw against **1,000,000** on the 12-month term costs **10,600.20** a year against **17,000** at 8.5 percent, with LTV, the **70 percent** cap, the **50,000** minimum and the collateral required all in the same response. The finding is that the published sheet carries `asOf: 2026-11-03T20:50:09Z`, nine days stale against the probe, and its rates sit 5 to 18 basis points under the table on the vendor's own page the same day.

**SplitScanner** is the discovery-open, execution-gated tier done well: **24** read-only tools listed keyless, `tools/call` answering **401**, and a tool surface that includes split authority with an expiry filter and exchange listing standards beside SEC filing and in-text search. The answers are the vendor's and are labelled as such; the surface is measured.

**Tracwell** is the OAuth tier done well: four scopes where reading analytics is one of them and the two write scopes touch definitions and site configuration rather than events, dynamic registration, `S256` only, both metadata documents read, and a published plan ladder from **9** to **149** USD a month with **API and MCP access included at every allowance**.

## What the next pass should pick up

**Diffbot** with a token, **Aalto** and **Toolbox POD** with a driven session, **billdog-io** once an account exists, and the freshness question on any rate or price surface: quote the `asOf`, not the number.

### Was anything removed from the canonical this window?

No. The distinct set is identical at **20,885** on both captures, so there are **0 removals** and no normalisation pairs to explain - the three raw entries are duplicates of counted keys.

### Is the feed a reliable arrival signal on its own?

Not at this cadence. Three of 30 stamped cards were inside a six-hour window and one card had no stamp yet; the queue carried the rest of the window's material, which is why both surfaces are read on every pass.
