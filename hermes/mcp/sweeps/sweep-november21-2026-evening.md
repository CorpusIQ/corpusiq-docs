---
title: "MCP Server Discovery - November 21, 2026 (Evening)"
description: "A ten-hour window in which the sitemaps re-sharded without adding a key, and the queue carried both products worth a guide."
category: "MCP Ecosystem"
last_updated: "2026-11-21"
---

# MCP Server Discovery - November 21, 2026 (Evening)

Fired on the **21:00 MST** tick, ten hours after the midday supplement closed on the capture stamped **17:00Z**. The canonical gained no key and lost none, the sitemaps re-sharded their locale forms while holding the same **23,220** distinct listings, and the seventeen queue arrivals carried both finds: an astrology surface whose charts reproduce against an ephemeris, and a dependency-outage surface that names which AI provider is down right now.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          37,102   against 36,971 (different map distribution)
  servers/1  ..... 4,147     servers/7  ..... 5,935     sums to 37,102 exactly
  servers/2  ..... 2,505     servers/8  ..... 2,698
  servers/3  ..... 2,989     servers/9  ..... 2,611
  servers/4  ..... 3,196     servers/10 ..... 2,615
  servers/5  ..... 3,390     servers/11 ..... 2,531
  servers/6  ..... 2,900     servers/12 ..... 1,585
distinct keys, maps 1-12      23,220   against 23,220         (0 / 0)
URLs per key                   1.60   against 1.59
priority-servers.xml            258 raw,  34 distinct keys (against 262 raw)
remote-mcp-servers.xml           15 raw,  one slug in fifteen locale forms
lastmod, server maps           173 rows at or after 17:00Z, 110 distinct keys,
                               every one of them already in the key set
mcp.so /feed                  200, 156,635 bytes, 34 anchors, 30 stamps
                              FOUR fresh products plus two prior cards
submission queue              #7775 to #7791, seventeen arrivals
```

The diff basis is the capture stored at **11:31Z**, and the elapsed time is read from that file's modification stamp rather than from the slot label. The two passes inside the window already proved the surface flat at **17:00Z** and again an hour later, so the whole material of this pass came from the push surfaces.

## A re-shard, not an arrival

**131 more raw rows and exactly the same number of products.** The twelve numbered maps returned **37,102** `<loc>` entries against **36,971**, distributed differently across the maps, while the distinct locale-stripped key set read **23,220** on both sides at **1.60** URLs per key against **1.59**.

Three readings agree that nothing arrived:

1. **The key set is identical** at 23,220 on the twelve-map basis, with the union diff returning one addition (`remote-mcp-servers/clockwise`, a slug in its remote form) and zero removals.
2. **Every one of the 173 `lastmod` rows** at or after the **17:00Z** cutoff, collapsing to **110** distinct keys, is a stamp on a listing that was already in the set.
3. **The per-map counts changed shape without changing the total population**, which is what a re-shard looks like and what a purge does not. The lesson of the day applies again: a raw delta is a rumour until the key set agrees with it.

## Catalogued with guides: two

### Asteria (#7791) - a natal chart that reproduces

`https://askasteria.com/mcp`, server `asteria 1.0.0+d43752a50483`, keyless, **thirteen** tools, registry `com.askasteria/asteria` to **1.0.2**. The catalog's first astrology entry, and the reason it earns a guide is that the chart half is checkable: a chart for **2026-03-20 15:00 UTC** returns the Sun at **0.0097 degrees Aries**, fourteen minutes after the equinox at 14:46 UTC; the Sun's longitude for **2000-01-01 12:00 UTC** reads **280.369 degrees**, the published position; the full Moon of **2026-01-03** is returned at **10:02:59Z** with a lit fraction of **0.99990**; and a sunrise chart puts the Ascendant at **271.650 degrees** against a Sun at **280.369**, the expected lead at that latitude. Two tarot draws of three cards returned entirely different cards, `psalm 23` came back in six King James verses with its Latin number **22** beside it, and `ritual` refused *"new job"* with its own enum. The reading half is the vendor's interpretation and the guide says so.

### WhatsDownNow (#7786) - which dependency is broken

`https://whatsdownnow.com/mcp`, server `whatsdownnow 1.6.0`, keyless reads, **thirteen** tools, registry `io.github.jacobpmiller/whatsdownnow` to **1.4.0**. **250** services in **13** categories holding **27** AI providers, each answering with three separate readings: the vendor's official status line, an HTTP probe from this service, and user reports. `get_status openai` resolved to the `chatgpt` slug and returned *"all systems operational"* with a **200 in 103ms** probe at **03:56:26Z**; `get_status stripe` returned verdict up with *"no public status feed"* and a **401 in 97ms** recorded as *"reachable; API answered and asked for a key, as expected"*; `check_stack` over six dependencies returned `ready: true`; `list_incidents cloudflare` returned the ORD incident from **00:32:59Z** to **01:11:58Z** with its own incident URL; and `get_ai_fallback` read **13 of 14** healthy with the board at **degraded** because of one provider, Mistral, quoting *"Vibe Work issues with GLM 5.3 Short"* beside a **403** probe. It is the dependency half of the monitoring story the catalog already owns for a business's own properties.

## Held, with the class or the gate named

Seventeen queue arrivals were read with bodies in one authenticated call; fifteen were not catalogued.

```text
ShareHTML        #7790  OAuth 2.1 with PKCE; class covered by Hushdrop
                        (66 tools publishing agent pages as private links)
Clic'n Done PDF  #7789  Office and PDF class (paperoffice, sumoffice,
                        ifillpdf, relaypdf already catalogued)
Tsoden x2        #7788  SEO and AEO visibility class, saturated before them
                 #7787  (one tool belongs to the other listing's surface)
Ania             #7785  avatar and lip-sync media generation; class carried
                        by PixVerse, MiniMax and Draftless
Datapika         #7784  Apify actor distribution, an established hold class
TemPolor         #7783  useapi.net media family, held on the same class
Runway           #7781  useapi.net media family
Hyperliquid      #7782  trading infrastructure class (TradingData, Kote
                        Charts, Pitbi)
openajar         #7780  agent VM and sandbox class (Homemade, kosa8)
Mrrlin           #7779  model-routing pool over several providers; local
                        stdio with no endpoint measurable from here
RBAi Scholar     #7778  biomedical literature; class covered by Paper Search
                        MCP (20+ academic sources including PubMed)
Draftless        #7777  media generation plus social publishing, saturated
BrainChain       #7776  crypto change feed; class owned by Protocol Change
                        Feed MCP
Formation Lane   #7775  UNRESOLVED, not decided: the host returned
                        TLSV1_ALERT_ACCESS_DENIED to every request from this
                        machine and curl produced no HTTP status at all
```

Four fresh feed products were also disposed of without a guide:

```text
gravel-host     20:27Z  game-server management behind OAuth 2.1, scope
                        servers:read servers:control, with a protected-
                        resource document. NOT the catalogued WeGravel
                        despite the name: this is game hosting, that is
                        delivered gravel pricing. Held on the gate.
rentcast-api    19:45Z  four tools that are an API gateway (list-endpoints,
                        get-endpoint, search-endpoints, execute-request) in
                        front of the RentCast API. Held on the API-proxy
                        class; execute-request needs a key nobody here holds.
clearmetric     23:20Z  401 invalid_token with no WWW-Authenticate, eighteen
                        tools never listed. Held on the static-token tier
                        plus the custom-business-app class.
garita-labs     00:02Z  thirty agent-security analysis tools, no callable
                        endpoint published on the card read here. Recorded
                        unresolved rather than decided.
```

The two remaining fresh cards are prior dispositions: `squish` at **17:47Z** and **17:29Z** (one product re-stamped, held last pass on the hosting console class) and `see-sight-tours` at **17:12Z**, which shipped as a guide in the midday supplement.

## Listings

Not re-measured this pass. The five surfaces were read on the **10:00 MST** midday pass, and nothing in this window touches them. The catalog's own position is unchanged: mcpservers.org live, mcp.so not listed on four slugs, glama and smithery listed, the Anthropic directory unchanged.

## What the window taught

- **A raw rise can still be a flat population.** 131 more `<loc>` entries with an identical key set is a re-shard, and the per-map distribution is the tell, not the total.
- **A `lastmod` stamp is a candidate generator, never an arrivals count.** 173 rows and 110 keys produced zero additions because every stamped key was already in the set.
- **The category you think you are cataloguing may be a computation.** Astrology reads like a lifestyle prompt wrapper until the chart returns a longitude that matches an ephemeris to the arcminute, and then it is a data surface with written commentary attached.
- **A verdict field can be more confident than its evidence.** A 401 probe scored as `up` is defensible for reachability and misleading for function, and the difference lives in the summary line rather than the verdict.
- **An unreachable host is neither a hold nor a ship.** Formation Lane answered TLS access denied to every request, so it is recorded unresolved with the exact error instead of being folded into a class it was never measured against.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Asteria MCP](/hermes/mcp/servers/external/asteria-mcp)
- [WhatsDownNow MCP](/hermes/mcp/servers/external/whatsdownnow-mcp)
- [MCP Server Discovery - November 21, 2026 (Midday Supplement)](sweep-november21-2026-midday-supplement)
