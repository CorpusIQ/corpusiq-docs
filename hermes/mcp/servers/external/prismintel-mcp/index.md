---
title: "Prismintel MCP - Four-Bloc Triage of Cached Geopolitical"
description: "A keyless endpoint returning cached four-bloc analysis of a geopolitical topic, with a consensus index, per-bloc tone split and honest archive label."
category: "Content & Research"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-25
source: "mcpservers.org arrival in the November 25 evening window, `servers/1..13` maps; official registry record app.prismintel/triage 1.0.0; keyless initialize, a two-tool tools/list and three tools/call requests driven against https://prismintel.app/api/mcp on 2026-11-25"
relevance: "★★"
tags: [geopolitics, risk, research, media-analysis, trade, supply-chain, keyless, remote-mcp]
last_updated: "2026-11-25"
---

# Prismintel MCP

**Every outlet frames the same event differently, and the framing is the part an operator usually cannot see.** A shipping disruption, a tariff escalation and an export-control change all read as different stories depending on which bloc's press is doing the reporting, and a business decision taken on one bloc's account of an event is a decision taken on a sample of one. Prismintel returns the divergence as data: a share of the corpus per bloc, a tone score, and the omission each bloc makes.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://prismintel.app/api/mcp
Auth:         none, no key and no account
Registry:     app.prismintel/triage 1.0.0
Instructions: "Read-only, zero-cost access to cached PRISMINTEL multi-bloc dossiers."
Tools:        2, read from a keyless tools/list
```

`initialize` answers **200** at protocol **2025-06-18** with `Server: cloudflare` and the single capability `tools`. There is no resource surface, no prompt surface and **no write path of any kind**: the endpoint reads a cache and hands it back.

## The two tools

| Tool | Arguments | What comes back |
| --- | --- | --- |
| `list_monitored_theaters` | none | every cached flashpoint with its consensus index, compile time, expiry stamp, freshness label and a deep link |
| `get_geopolitical_triage` | `topic`, optional `lang` | the BLUF, the consensus index, the per-bloc tone split and a deep link to the terminal |

## What one dossier actually contains

`get_geopolitical_triage` on *"semiconductor export controls"* returned a **51-source** dossier at a **68%** consensus index, compiled **2026-11-24T21:45Z**, with the analysis split three ways rather than into a single verdict:

- **Operational reality** - *"TSMC has closed a prior self-assessment loophole for Chinese chip designs and paused some advanced shipments to China in direct response to tightened US Commerce Department rules issued in mid-November 2026."*
- **The primary narrative fault line** - Western outlets read the controls as a national-security response to a circumvention scheme; Eurasian and state-aligned outlets read the same measures as *"unlawful economic coercion that damages global supply chains"*; regional and Global South outlets lead with *"the practical compliance burden on third-country intermediaries such as Singapore and Malaysia."*
- **Analytical restraint** - *"This evidence base documents reported regulatory tightening, market reaction and divergent bloc framing, but it does not establish coordinated state intent, confirmed physical chokepoint disruption, or an imminent kinetic trajectory in the Taiwan Strait."*

The tone split quantifies the framing rather than describing it:

| Bloc | Corpus share | Tone score | Top omission named |
| --- | --- | --- | --- |
| Western / NATO | **39%** | **-15** | the compliance burden on Southeast Asian intermediaries |
| Regional Actors | **29%** | **-10** | the US legislative push tied to defence spending |
| Eurasian & State-Aligned | **20%** | **-55** | the Huawei criminal conviction on fraud and trade-secret counts |
| Global South / Non-Aligned | **12%** | **+5** | - |

39 + 29 + 20 + 12 = **100%**, and the spread runs from **+5** to **-55** on the same event. **The most useful column is the last one.** A tone score tells a reader that a bloc is hostile; the omission field tells them what a bloc's coverage leaves out, which is the thing that survives a summary. An assistant asked "what is the risk to our chip supply" that reads only the Western 39% is working from the corpus that scores the event at -15 and omits the compliance problem sitting on Singapore and Malaysia, where a distributor's actual exposure lives.

## All nine theaters were expired, and that is the finding

`list_monitored_theaters` returned nine dossiers covering eight distinct topics:

| Consensus | Topic | Compiled | Age at read | Expired |
| --- | --- | --- | --- | --- |
| 68% | Hormuz: tanker attacks, war funding | 2026-11-25T16:30Z | **11.5 h** | yes |
| 62% | Hormuz: same title, second copy | 2026-11-25T16:13Z | **11.8 h** | yes |
| 74% | North American trade realignment, tariffs | 2026-11-24T21:48Z | **30.2 h** | yes |
| 68% | Export controls, Taiwan Strait, chips | 2026-11-24T21:45Z | **30.2 h** | yes |
| 69% | Eastern Europe energy grid, Black Sea | 2026-11-24T21:42Z | **30.3 h** | yes |
| 72% | Red Sea maritime disruptions | 2026-11-24T21:38Z | **30.4 h** | yes |
| 66% | Arctic shipping routes and militarization | 2026-11-24T21:52Z | **30.1 h** | yes |
| 72% | South China Sea code of conduct | 2026-11-24T00:58Z | **51.0 h** | yes |
| 76% | Ukraine maritime reach to Libya | 2026-11-23T19:30Z | **56.5 h** | yes |

**Every row carried `is_expired: true` and `freshness: "archive"` at 21:00 MST on 2026-11-25.** The newest dossier was eleven and a half hours old and the oldest was more than two days old, which makes the endpoint a library rather than a live feed at the moment it was read.

The label is honest and the caller is the problem. The same dossier returns two fields that disagree about freshness:

```text
status:          CACHED_DOSSIER_AVAILABLE
freshness:       archive
is_expired:      true
compiled_at:     2026-11-24T21:45:20.904+00:00
```

**An agent that branches on `status` sees "available" and reports a 30-hour-old analysis as current.** An agent that reads `freshness` or `is_expired` knows to date the answer. The fix is on the client side and it is one line: present the compile time, not the status.

The expiry arithmetic is also inconsistent. Three rows carry a **6-hour** window from compile to expiry and six carry **12 hours**, on the same tool on the same read. Seven of the nine compiled within twenty minutes of each other on the evening of 2026-11-24, which reads like one nightly batch, and only the two Hormuz entries were refreshed the following afternoon.

## Duplicate topics occupy two of the nine rows

The Hormuz dossier appears twice with different compile times and different consensus indexes, **68% at 16:30Z and 62% at 16:13Z**, under an identical title. Two rows, seventeen minutes apart, six points of consensus between them. Whatever the roll-up does, it does not deduplicate by title, so a client listing "the theaters" gets eight subjects and nine rows, and a client averaging consensus indexes across rows double-counts the Hormuz story. Read `compiledAt` and use the newest row per title.

## What the payload points at, and what it does not

Every deep link carries a tracking parameter naming the marketplace: `utm_source=ai_marketplace` on both the theater URLs and `fullDossierUrl`. That is a normal acquisition convention and it is stated here because the link is part of the answer, not advertising in it.

Each dossier also carries a `corpusSnapshotHash` of the form `SHA-256 684e289a1fd9cf08`, which is **16 hex characters, 64 bits**, short of a full SHA-256 digest of 64 hex characters. It is a content fingerprint, not a verifiable digest: an operator should not treat it as an integrity proof of the underlying corpus, which is not exposed.

The `ctaNotice` names what sits behind the paid surface: *"Full 5-Lens Telemetry (Yahoo Finance, OFAC/USAspending, CAIDA IODA, Sentinel-2 GEOINT), full source bibliography, and 16-page TLP:CLEAR PDF export."* None of those five lenses, the bibliography or the export is reachable through the MCP tools. The MCP surface is the BLUF and the tone split; the evidence layer is the product.

## Limits measured this pass

- **Cache only.** The instructions say it never compiles new analysis, and the expiry stamp proves it: nine of nine dossiers were past expiry at read time. A topic that is not cached returns no analysis rather than a fresh one.
- **Nine topics, one language.** Every row returned `language: "en"`, and `lang: "en"` behaved identically to omitting the field, so no second-language corpus was observed.
- **No source list per item.** The BLUF names actors and events, and the bloc split names what each bloc omits, but the individual sources behind a claim are behind the paid surface. Treat the consensus index as a vendor-computed number with no published method, not as a measured agreement rate.
- **Six-hour to twelve-hour staleness is normal, days are not.** Two dossiers were more than two days old with no newer version in the list.
- **Read-only, and nothing to configure.** No account, no key, no scopes, no writes. The whole surface is two tools.

## Where it fits a business-answer system

The pattern worth taking from this server is the **restraint paragraph**. A tool that says what its own evidence does *not* establish, in the same payload as the claim, is doing the verification step that a summarising assistant usually skips. The failure mode it models is the one that costs operators money: a single-bloc account of an event, retold as fact, with the omission invisible.

## See also

- [Financial News MCP](/hermes/mcp/servers/external/financial-news-mcp) for dated market headlines against the same events.
- [APITube News MCP](/hermes/mcp/servers/external/apitube-news-mcp/) for a general news wire rather than a bloc-framed dossier.
- [Klarix Intelligence Engine MCP](/hermes/mcp/servers/external/klarix-intelligence-engine-mcp/) for the B2B competitive-intelligence counterpart.
- [External MCP Server Catalog](/hermes/mcp/servers/external/) for the full index.
