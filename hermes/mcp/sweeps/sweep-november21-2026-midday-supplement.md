---
title: "MCP Server Discovery - November 21, 2026 (Midday Supplement)"
description: "An hour in which the directory did not move at all, and both push surfaces still carried two products worth a guide."
category: "MCP Ecosystem"
last_updated: "2026-11-21"
---

# MCP Server Discovery - November 21, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday sweep closed on the capture it stamped **17:00Z**. The canonical came back flat on every reading, so the whole hour was the two push surfaces: three cards above the cutoff that resolve to two products, and one queue arrival that turned out to be one of them.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          36,971   IDENTICAL map for map to the 17:00Z capture
  servers/1  ..... 4,153     servers/7  ..... 5,878     sums to 36,971 exactly
  servers/2  ..... 2,526     servers/8  ..... 2,716
  servers/3  ..... 2,995     servers/9  ..... 2,609
  servers/4  ..... 3,172     servers/10 ..... 2,592
  servers/5  ..... 3,367     servers/11 ..... 2,539
  servers/6  ..... 2,879     servers/12 ..... 1,545
distinct keys, maps 1-12      23,220   against 23,220         (0 / 0)
URLs per key                   1.59   against 1.59
priority-servers.xml            262 raw,  34 distinct keys
remote-mcp-servers.xml           15 raw,   0 server slugs (one slug in fifteen forms)
lastmod, server maps          33,411 stamped pairs; ZERO rows at or after 17:00Z
mcp.so /feed                  200, 156,533 bytes, 34 anchors, 30 stamps
                              THREE cards above the cutoff, TWO products
submission queue              #7774 only
```

## A flat hour, proved three ways

Three readings agree, and none of them is a narrative:

1. **36,971** raw `<loc>` entries across the twelve numbered server maps, identical map for map to the midday capture and summing exactly to the stated total.
2. **23,220** distinct locale-stripped keys on both sides, at the same **1.59** URLs per key, for **0 additions** and **0 removals** on the twelve-map plus priority basis and on the union.
3. **Zero** `lastmod` rows at or after the **17:00Z** cutoff across **33,411** stamped pairs in the server maps.

The remote map again misreads if the bases are mixed: `remote-mcp-servers/<slug>` appears under fifteen locale prefixes for one slug, so a naive union against a twelve-map baseline reports fifteen additions that are fifteen URL forms.

The `/all` pages were not re-read: the surface has answered **403** by edge policy since 4 November.

## Where the material came from

**Feed.** 200 at **156,533** bytes, 34 server anchors, 30 stamps. Three cards above the cutoff: `squish` at **17:29Z** and again at **17:47Z** (one product re-stamped, one anchor between the two stamps), and `see-sight-tours` at **17:12Z**.

**Queue.** `chatmcp/mcpso` carried **#7774** only, filed at **17:58:51Z**: Fuzzzy Law.

One product arrived on both surfaces within four minutes of each other: the registry published `com.fuzzzycore.law/georgian-law` at **17:57:58Z**, the queue issue named the same endpoint fifty-three seconds later. That is a vendor doing the listing work properly, and it is worth saying that the registry record and the submission agreeing is what makes the endpoint identity certain.

## Shipped: two, both keyless and both driven

### Fuzzzy Law - the first Georgian law surface

Submission **#7774**, `https://law-api.fuzzzycore.com/mcp`, registry `com.fuzzzycore.law/georgian-law` **1.0.0**, twelve read-only tools, no auth. Fifteen `tools/call` requests were driven.

The measurement that justifies the guide: **24** codes and laws holding **6,517** articles, every response stamped `data_current_as_of: 2026-11-21`, and **8,473** published decisions - **8,116** Supreme Court (to **2026-06-16**), **328** Constitutional Court (to **2026-06-24**) and **29** Grand Chamber (to **2017-03-02**). Labour code article 12 came back whole, with version date **2026-09-16** and the `matsne.gov.ge` link to the paragraph.

The honesty is the story. `verify_citation` on a fabricated notary clause returned the real article and a `lexical_check` counting **5 of 6** claim terms, with the sentence *"The article exists. Compare the claim with the text before relying on it."* and its own label - *"Word and number overlap only. This is not a legal judgement; read the text."* A citation to `მუხლი 9999` returned `exists: false` and the instruction not to cite it. Search in English returned nothing and asked for Georgian terms, which is a limit the guide states rather than smooths.

### See Sight Tours - the first guided-tours booking surface

Feed card at **17:12Z**, registry `com.seesight-tours/booking` **1.0.0** published **2026-11-18T00:58:15Z**, eight tools, no auth, all driven keyless.

`search_products` on Toronto returned **31** products from **237 CAD** down to **110 CAD** per adult. `check_availability` on the Niagara Falls day tour for **2026-12-05**, two adults, returned one departure at **07:00 America/Toronto** with **4 seats left** and **726.00 CAD** for the party, expiring **2026-11-21T18:17:13Z** with its own price basis - per-person tickets, taxes and fees as shown at checkout, before any promo code. `get_checkout_link` on the returned `quote_id` produced a `state: prepared` URL on `/checkout/handoff/` expiring **19:02:18Z**, and `check_checkout_link` on it answered that the link is ready while stating that whether the guest paid is visible only to the guest and to the operator's support. A fabricated checkout URL was refused by name; an unknown product id returned `NOT_FOUND`.

Travel was already carried here by hotel booking and rental cars, so the guide argues the distinct slice: activities with live seats and a payment handoff that no agent can complete.

## Held, with the class or the gate named

One, from the third feed card:

```text
squish   domains, DNS, hosting, backups, uptime behind OAuth 2.1
         (401 with a protected-resource document, no keyless read)
         held on the hosting-and-registrar console class already
         carried by Domain MCP (Dynadot) and EuroDNS
```

The second `squish` card at **17:47Z** is the same product re-stamped eighteen minutes after the first, not two listings.

## Listings

Not re-measured this hour. The five surfaces were read on the **10:00 MST** midday pass, one hour before this window, and nothing in this hour's evidence touches them: mcpservers.org live at `servers/corpusiq-io`, mcp.so not listed on four slugs, glama and smithery listed, the Anthropic directory unchanged.

## What the window taught

- **A flat canonical is a precondition, not a verdict.** The directory did not move by a single row, and the hour still shipped two guides, because the arrivals moved on the feed and in the queue.
- **One product can appear twice on one surface.** Two `squish` stamps eighteen minutes apart on a 30-card feed is a re-stamp, and counting stamps rather than slugs turns it into two discoveries.
- **The registry and the queue agreeing is the strongest identity evidence available.** A vendor that publishes the record and files the submission in the same minute removes the guesswork about which endpoint belongs to which product.
- **A tool that declines to judge is more useful than one that pretends to.** `verify_citation` ships the text, the version date and a word-overlap count, and says in its own words that this is not a legal judgement.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Fuzzzy Law MCP](/hermes/mcp/servers/external/fuzzzy-law-mcp)
- [See Sight Tours MCP](/hermes/mcp/servers/external/see-sight-tours-mcp)
