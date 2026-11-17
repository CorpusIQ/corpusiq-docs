---
title: "MCP Server Discovery - November 17, 2026 (Midday Supplement)"
description: "The sitemap surface was flat to the key, one feed card carried an agent phone line, and one queue entry needed a Mac it cannot have."
category: "MCP Ecosystem"
last_updated: "2026-11-17"
---

# MCP Server Discovery - November 17, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday sweep closed. Both directory surfaces were read and the cheaper proof is that they came back identical: the twelve numbered server maps returned the same **65,989** raw `<loc>` entries, map for map, and the distinct key set stood at **22,113** on both captures. Nothing new arrived from that surface. The mcp.so feed carried **one** card above the midday stamp and the submission queue carried **one** arrival. **One** server ships.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          65,989   against 65,989 at the 17:00Z midday capture
  servers/1  ..... 7,588   held    servers/7  ..... 9,351   held
  servers/2  ..... 5,949   held    servers/8  ..... 6,590   held
  servers/3  ..... 6,518   held    servers/9  ..... 4,024   held
  servers/4  ..... 6,744   held    servers/10 ..... 2,608   held
  servers/5  ..... 6,954   held    servers/11 ..... 2,636   held
  servers/6  ..... 6,756   held    servers/12 ..... 271     held
priority-servers.xml          299 raw, 34 distinct keys   held
static.xml                    822 raw, 102 distinct keys  held
remote-mcp-servers.xml        15 raw,   1 distinct key   held
distinct keys, twelve maps    22,113 against 22,113  = 0 additions, 0 removals
distinct keys, union w static 22,250 (same basis on both sides)
lastmod rows at or after cutoff  0
mcp.so /feed                  200 at 156,358 bytes, 44 anchors, 30 stamped cards
submission queue #7522        1 arrival, body read
```

Three independent readings agree. The raw count did not move, the per-map counts did not move, the distinct key set did not move, and a `lastmod` scan for rows stamped at or after the midday cutoff returned **zero**. A one hour gap on this surface is a flat instrument, and this pass reports it as flat rather than finding something to say about it.

The feeds are where the hour moved.

## The one feed card

| Stamp (UTC) | Slug | Disposition |
|---|---|---|
| 17:27 | `meisim` | **Ships.** New class: US phone lines an agent can own |

The card sits **34 minutes** old at the read, and it is the only stamp above the midday's newest, `romeoseo` at 15:38Z. The feed stamp text now reads `Submitted N minutes ago` rather than `Added N hours ago`, so the pairing rule still holds: read the `M/D/YYYY, HH:MM AM/PM` title attribute in UTC and bind it to the nearest preceding `/servers/<slug>` anchor.

The listing page answered **200** at the bare slug route, carried the Verified and Featured marks, and gave the config block, the MIT licence and the author. It also says *Tool list not available yet*, which is a directory limitation rather than a property of the server: the live endpoint lists **sixteen** tools to a keyless caller.

## The one queue arrival

**#7522**, filed **2026-11-17T17:47:52Z**, reads *Submit MCP Server: Netutilus (network diagnostics on Mac)*. Body read in one authenticated call.

- **Held.** `github.com/elpofigisto/netutilus-mcp` is a **local stdio** binary that ships inside a macOS App Store app, needs **macOS 14.6** or later and a **Netutilus Pro** licence, and is invoked as `/Applications/Netutilus.app/Contents/Helpers/netutilus-mcp`. There is no remote endpoint to probe and no way to reach it from this host, so neither its tools nor its behaviour can be measured here. The product itself is real and the tool list is useful (ping, traceroute, MTR, bufferbloat, Wi-Fi and LAN scan, DNS, SPF, DKIM and DMARC checks), which is exactly why it is recorded with its reason rather than dropped: a catalogue entry with no measurement is a listing, and this catalogue does not count listings.

## What ships, and at which evidence tier

**MeiSIM** ships at the driven tier with a measured boundary. `initialize` answered **200** keyless with **meisimusa-mcp 0.3.5** on protocol **2025-06-18**, and no session id was issued. Sixteen tool schemas came back, every one carrying a title, an output schema, annotations and an `execution.taskSupport` field, which is more of the current spec than most entries here declare.

Twelve `tools/call` requests followed. **Six answered with live data** and no credential:

- `get_ai_line_offer` priced the product in one response: **35** dollars a month per line for texts, **45** with voice, dropping to **32** and **42** at 10 lines, **29** and **39** at 50, **25** and **35** at 200, on a **two month** minimum paid up front.
- `search_us_numbers` returned **28** prepaid plans across five carriers from **7.50** to **288**, every row carrying `includes_us_number: true`, and the price ceiling held at both bounds tested (**10** returned two plans topping out at **10.00**, **25** returned nine topping out at **21.00**), with no duplicate plan ids or carrier and title pairs.
- `search_plans` returned **58** Japan, **80** France and **86** United States eSIM plans from several suppliers (Airalo, Sparks, 3, Bouygues, NextLink, RoamVault, IIJ and MeiSIM), cheapest at **5.99**, **4.70** and **5.99**, and an empty list with no error for a country with no coverage.
- `get_quote` returned its own breakdown, **7.50** subtotal with zero tax and zero fees, and a `quote_expires_at` **15 minutes** out, measured twice.
- `topup_lookup` returned an empty result with a hint naming the three fields that would find an order, which is the one account side tool that answers without a key.

**Six answered with the server's own refusal**, all at HTTP **200** with `isError: true`: *This tool needs a MeiSIM API key. Remote: send it as "Authorization: Bearer ..." on the connection. Local: set MEISIMUSA_API_KEY*, followed by the sentence that decides how an operator plans around this server: *A person opens the account... An AI agent cannot open the account by itself.* The sign-up carries a robot check and the ID step needs a government ID and a phone camera.

Three defects are recorded rather than smoothed: `purchase` declares `payment_method` as a **required object** whose own description says it is **not used**, `search_plans` refuses a call that omits `duration_days` while presenting `data_gb` as the optional filter, and a `purchase` validation failure arrives as two failures concatenated into one message with no field separator. Detail in the guide.

## Counts

Canonical **65,989** against **65,989** with **0 additions and 0 removals** on the twelve-map basis, **0** `lastmod` rows above the cutoff, feed **156,358** bytes with **30** stamped cards and **1** above the cutoff, **1** queue arrival with **0** shipped from it, **2** candidates evaluated with **1** catalogued and **1** held with its reason named, guide tree **1,343** directories before this pass and **1,344** after, `hermes/mcp` Markdown **1,643** to **1,645**.
