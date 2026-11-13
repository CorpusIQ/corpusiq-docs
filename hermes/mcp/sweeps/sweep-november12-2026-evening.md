---
title: "MCP Server Discovery - November 12, 2026 (Evening)"
description: "A ten-hour window where the sitemap lost listings without gaining any, the feed carried five cards and the queue twenty-two: one calculator that refuses"
category: "MCP Ecosystem"
last_updated: "2026-11-12"
---

# MCP Server Discovery - November 12, 2026 (Evening)

Fired on the **21:00 MST** tick, nine and a half hours after the midday supplement closed. The delta was not where the schedule usually puts it: the sitemap surface produced **no new key at all**, the feed carried **five** cards above the cutoff and the submission queue **twenty-two** arrivals. One entry earned a guide, and it earned it by refusing to produce a number.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, twelve of them server maps
                                 (priority-servers plus servers/1 to 11)
raw <loc> entries                64,577   against 64,578 at the 17:01Z midday-supplement capture
per-map counts                   priority 299 / 7,588 / 5,948 / 6,518 / 6,744 / 6,952 /
                                 6,756 / 9,351 / 6,589 / 4,031 / 2,606 / 1,195
distinct keys, locale-stripped   19,068   against 20,885 on the 17:01Z capture
additions                        0
keys absent from this capture    1,817
newest lastmod                   2026-11-12T16:16:25Z  (before the 17:05Z cutoff)
lastmod at or after 17:05Z       0
mcp.so /feed                     200 at 145,085 bytes, 36 anchors (29 server, 7 rail),
                                 30 stamped cards in the M/D/YYYY form, 5 above the cutoff
queue #7224 to #7245             22 arrivals, no gaps
```

**The removal count is stated as a composition change and not as 1,817 delistings, because the two readings do not support that claim.** The raw entry count is flat (64,577 against 64,578) while distinct keys fell by 1,817, which means the surviving keys carry more URLs each - **3.39** per key against **3.09** - so the same surface pruned keys and added pages under keys that already existed. A sample of five removed slugs was searched across all twelve maps: `000safah000-ai/blackhawkmcp`, `01-studio/startupkit`, `0ui-labs/coderabbit-mcp-server`, `0x79de/hft-mcp` and `0xTrxz/supabase-mcp` have no trace in today's text. Tail matching softens it slightly - **134** of the 1,817 have their final segment present under a different key form - but the remainder are absent. **Page-level confirmation is not available from this host:** a detail route answers **403** by edge policy (the standing condition since November 4) and the reader proxy answers **401** on bad IP reputation, both re-tested this pass. Zero additions is the load-bearing number for this sweep: the canonical gained no listing key in ten hours.

## The feed, five cards above the cutoff

| Card | Stamped (UTC) | Disposition |
|---|---|---|
| `busabase` | 2026-11-13 03:18Z | Agent database and workspace (MIT) - system-of-record class already carried |
| `hms-x402-data-origins-re-data-refinery-storefront` | 2026-11-13 00:31Z | x402 paid data origins (Ohio property, car rental rates) - x402 class, owner named |
| `lobbystack` | 2026-11-12 21:28Z | Open-source AI receptionist - class owner shipped from this catalog today |
| `porter-metrics` | 2026-11-12 20:36Z | Hosted marketing data, 45 tools - marketing-data class, owners named |
| `textforagents` | 2026-11-12 20:17Z | Prior disposition: publisher family of pay-per-check agent infrastructure |

`rushcrm` at 17:38Z and `hank` at 17:21Z were the midday supplement's own tail, re-served. The stamps are UTC in a 12-hour `M/D/YYYY, HH:MM AM/PM` `title` attribute and were converted before the cutoff was applied.

## 1 catalogued, 1 guide

**[Click Decay MCP - CTR Math That Refuses a Number](/hermes/mcp/servers/external/click-decay-mcp/)** - remote Streamable HTTP at `https://clickdecay.com/mcp`, plain JSON, no session, **keyless**, `initialize` **200** as `clickdecay` **1.0.0** on protocol `2025-06-18` with `tools` as the only capability, registry `com.clickdecay/mcp-server` **1.0.0** active (published 2026-11-12T23:10:41Z), MIT, vendor QQQ OÜ in Tallinn, about 60 requests a minute per connection.

**Four** tools, each annotated `readOnlyHint: true`, `idempotentHint: true`, `openWorldHint: false`. **Eleven calls were driven**, and the arithmetic was reproduced by hand as a control: 3,000 clicks from 100,000 impressions against 3,150 from 125,000 over two 28-day periods returned `clicksAtPriorCtr` **3,750** (`modelled`), an impressions component of **+750** (`calculated`), a CTR component of **-600** (`calculated`) and an observed click delta of **+150** - 125,000 at 3 percent is 3,750, 3,750 minus 3,000 is +750, 3,150 minus 3,750 is -600, and both components add back to the observed delta.

**The finding is the refusal.** Google's own impressions-logging anomaly runs **2025-05-13 to 2026-04-27**. A comparison touching that window returned `value: null` with `nullReason: "GSC_REPORTING_ANOMALY"` on every impressions-dependent figure - both CTRs, the impression delta, the percentage-point change, the relative change, both modelled figures and both components - while `clickDelta` stayed **+200** `observed`, with the anomaly listed in `anomalies` and `sourceUrl` pointing at Google's notice. The same call on dates after the anomaly returns numbers. `check_gsc_reporting_issues` exposes the registry behind it: **two** records at reading, `GSC_IMPRESSIONS_ANOMALY_2025_2026` (`block_ctr_diagnostics`) and `GSC_BULK_EXPORT_MISSING_DAYS_2026` (`warn`).

Three bad inputs were refused with machine-readable codes - `PERIOD_LENGTH_MISMATCH`, `PERIOD_OVERLAP`, `CLICKS_GT_IMPRESSIONS` - all at HTTP **200** with `isError: true` and `structuredContent.errors`, and **no `content` block**, which is the defect recorded in the guide: a client that renders only `content` shows the operator an empty answer. A null value carries a `nullReason` (`ZERO_RATE` for a zero CTR) without setting `isError`, and two observed figures come back unrounded (`ctrChangePp` as `-0.47999999999999987`, `relativeCtrChangePercent` as `-15.999999999999993`).

## Also identified this pass (not catalogued)

The twenty-two queue arrivals were read in one authenticated call and triaged one by one; a directory card is a claim, not a measurement, and the class owners below are named so the next pass does not re-open them blind.

- **porter-metrics** (#7225-adjacent feed card, `https://mcp.portermetrics.com/mcp`, 45 tools, hosted sign-in) is a genuine operator surface and holds anyway: marketing-data aggregation is carried by **Otto MCP** (Meta, GA4 and GSC in one chat), **Manifold MCP** (hosted marketing data for agents) and **Metrinel**, with the semantic-layer owners **Dataddo**, **Catalogian** and **Azquo** one layer below.
- **lobbystack** is an open-source AI receptionist for calls, texts and appointments - the class **Hank MCP** was catalogued into this morning, beside the receptionist group already here.
- **busabase** (MIT database and workspace where agents and people share data) sits on the agent system-of-record class carried by the memory and workspace entries; **hms-x402** is x402 paid data origins, the class owned by **Cred402** and the x402 group.
- **textforagents** is a prior disposition - the pay-per-check agent-infrastructure publisher family, held once already.
- **Traxure** (#7225) is release-liveness monitoring for music catalogues and was measured to its gate: a keyless `initialize` answered **401** with `resource_metadata` and `scope="traxure"`. It holds on the music-catalogue class owned by **[DropCue MCP](/hermes/mcp/servers/external/dropcue-mcp)** - same record set, different question - and the handshake alone does not carry a guide.
- **App Reviews** (#7226), **Competitor Ads** (#7227) and **Shopify App Store Search** (#7228) are three entries filed within one second of each other by the same publisher, scoped to their own Apify Actors. That is the standing Apify-actor distribution ruling: it is a hold class regardless of how business-relevant the data is.
- **MéxicoAPI** (#7233) is official Mexican reference data with sources per answer (INEGI, Banxico, DOF, CNBV, SAT, CONASAMI) and validators for RFC, CURP, CLABE, NSS. The validators are already covered by the catalogued **tlaloc-mcp-server** (CURP against RENAPO, RFC against SAT, postal codes against SEPOMEX, banking against Banxico, SPEI and CEP); the geography and reference data does not close a gap that entry leaves.
- **OpenRecord** (#7238, Epic MyChart portals, 50+ tools, family proxy records, passkey and TOTP) is a personal health record surface that installs locally as a desktop extension - held on the patient-chart class the **last-ehr** disposition established, and on the local-install tier.
- **GlucoBeat** (#7235, Libre glucose diary) and **Hoy Planes** (#7234, twelve Spanish provinces of events) are consumer surfaces in classes already carried - the health-diary group around last-ehr and Pleso, and the local-events group around the two What's On city servers.
- **AgentDrives** (#7240) publishes how far its own agent got signing up, using and paying for a SaaS - interesting enough to read, and a tool directory rather than a data surface, which is the **Agent Demand Registry** precedent. **Fourth Feed** (#7243, AI video tools with prices, traffic and agent-readiness) is the same shape.
- **Agent Guild** (#7241) steers coding-agent terminals on your own machine and is a local install; note the name collision with the **Agent Guild** reputation layer catalogued in June, which is a different product. **Browz** (#7229, fingerprint-protected browser profiles), **bootkey** (#7242, agent hosting), **SynapseOrch** (#7230, workflow automation) and **FigmaMCP** (#7245, a Mac app bridging the Figma desktop plugin) each sit on a class already carried - browser automation, agent hosting, workflow automation and design tooling.
- **Alerta Chart** (#7239, 65 trading tools behind a Pro or Elite plan), **Bitcompare** (#7244, crypto yield and lending rates) and **ResultsZA** (#7232, South African lottery and racing) hold on the markets and consumer-gambling classes; **Geloky** (#7231) on geocoding; **Construct** (#7236) on 3D and CAD validation, the class **VextCAD** was held into; **PokerData** (#7224) on hobby solvers.

## Surfaces read and core listing

Both directory surfaces for the window, the feed twice over (plain and cache-busted), and the queue from #7224 to #7245 in one authenticated call. The core listing check was not re-run this pass because both surfaces were read for the window and neither returned a CorpusIQ result; the standing conditions are unchanged - `mcpservers.org/servers/corpusiq-io` answers **403** by edge policy, the four mcp.so bare slugs answer **404**, and the official registry carries the active `io.corpusiq/multi-source-mcp` records.
