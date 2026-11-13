---
title: "MCP Server Discovery - November 13, 2026 (Night)"
description: "A window where keys the last pass read as absent came back, nine ad-platform cards landed in one hour, and two tools earned guides"
category: "MCP Ecosystem"
last_updated: "2026-11-13"
---

# MCP Server Discovery - November 13, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the evening sweep closed at 04:06Z. The first thing this window did was contradict the last one: the canonical that the evening pass read as having lost **1,817 keys** came back with those keys present and **246** raw entries more than it had before. Two servers were catalogued, both of them driven rather than read.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, twelve of them server maps
                                 (priority-servers plus servers/1 to 11)
raw <loc> entries                64,823   against 64,577 stated at the 04:06Z evening capture
per-map counts                   priority 299 / 7,588 / 5,948 / 6,518 / 6,744 / 6,952 /
                                 6,756 / 9,351 / 6,589 / 4,031 / 2,606 / 1,443
                                 (every map held except servers/11, 1,195 -> 1,443)
distinct keys, locale-stripped   21,125   against 20,885 at the 17:01Z midday capture
additions                        +240 keys, +246 raw entries
newest lastmod                   2026-11-13T07:36:23Z  (usezn/zn)
lastmod at or after 04:06Z       243 rows, collapsing to 84 distinct listings
mcp.so /feed                     200 at 144,476 bytes, 36 anchors, 30 stamped cards
                                 in the M/D/YYYY form, 15 above the cutoff
submission queue #7246 to #7261  16 arrivals, no gaps
```

## The 1,817 absent keys were a capture artifact, and the proof is five slugs

The evening pass said the surface had pruned **1,817 keys** while holding its raw entry count flat, called it a composition change rather than a delisting count, and named five removed slugs it had searched across all twelve maps with no trace: `000safah000-ai/blackhawkmcp`, `01-studio/startupkit`, `0ui-labs/coderabbit-mcp-server`, `0x79de/hft-mcp` and `0xTrxz/supabase-mcp`.

**All five are present in today's capture.** Each was grepped against the locale-stripped key set built from today's twelve maps and each returned exactly one match. That is not a resurrection: it is the same surface serving a different slice of its own index between two reads, which is the reading the last pass could not corroborate because the detail routes answer **403** by edge policy and the reader proxy **401** on bad IP reputation - both re-tested this pass.

The load-bearing conclusion for future passes: **on this surface a key absent at one capture is not a removal, and a key present is not an arrival, unless the per-map counts moved.** Between the midday and this morning the only map that moved is `servers/11`, by **248** raw entries, and the raw total moved by **246** against the stated figure - a two-entry difference that is inside the prior pass's own per-map sum (64,575 against a stated 64,577). Report the per-map counts, not the key set, when the question is whether anything arrived.

The 243 stamps at or after the cutoff collapse to **84 distinct listings**, and most of them are re-indexes of established repositories - `jlowin/fastmcp`, `clickhouse/loom`, `trycua/cua`, `elie222/inbox-zero`, `mediar-ai/screenpipe`, `MCPJam/inspector`, `Couchbase-Ecosystem/mcp-server-couchbase`, `heygen-com/hyperframes`, `nottelabs/notte-mcp`, `oomol-lab/open-connector`, `metabase-mcp-server`. The genuinely new material in the stamp window is a **07:16Z to 07:17Z** cluster of vendor-domain slugs (`www-regdatalab-com-mcp`, `live-web-data-mcp`, `tavimi-mcp`, `signal-lab-mcp`, `toolbox-pod-mcp`, `taste-match-mcp`, `dealai-mcp`, `regiabi-mcp`, `aisecuritywarden-mcp`, `htristram/trustydata-mcp-server`), one publisher's indexing run rather than ten discoveries, and every one of them a single-purpose wrapper in a class this catalog already carries.

## The feed, fifteen cards above the cutoff

| Card | Stamped (UTC) | Disposition |
|---|---|---|
| `x-ads-mcp-server-by-adkit` | 2026-11-13 09:56Z | AdKit fleet - one product, nine listings, see below |
| `meta-ads-mcp-server-by-adkit` | 2026-11-13 09:23Z | AdKit fleet |
| `tiktok-ads-mcp-server-by-adkit` | 2026-11-13 09:10Z | AdKit fleet |
| `reddit-ads-mcp-server-by-adkit` | 2026-11-13 09:10Z | AdKit fleet |
| `pinterest-ads-mcp-server-by-adkit` | 2026-11-13 09:10Z | AdKit fleet |
| `microsoft-ads-mcp-server-by-adkit` | 2026-11-13 09:10Z | AdKit fleet |
| `linkedin-ads-mcp-server-by-adkit` | 2026-11-13 09:09Z | AdKit fleet |
| `google-ads-mcp-8a9893` | 2026-11-13 09:08Z | AdKit fleet |
| `ads-mcp-server-by-adkit` | 2026-11-13 09:07Z | AdKit fleet (hub listing) |
| `sportsgameodds-mcp` | 2026-11-13 08:47Z | Sports odds data - no registry record found under any name form; unresolved |
| `escro` | 2026-11-13 07:29Z | Escrow/payments - no registry record under `escro`; the two nearest records are a sanctions-screening escrow and an Amazon price-search product, neither is this card |
| `splera` | 2026-11-13 06:29Z | A/B testing for agents (`io.github.sohaibt/splera` 0.1.1) - experimentation class already carried |
| `agentmsgr-95aef4` | 2026-11-13 06:22Z | Agent group chat, `com.agentmsgr/agentmsgr` 1.3.0, 11 tools, remote 401 - held, see below |
| `galatic-ai-15efb7` | 2026-11-13 04:32Z | AI video, image, music and voice generation (`ai.galatic/galatic` 1.0.1) - media-generation class saturated |
| `galatic-ai` | 2026-11-13 04:25Z | Same product, second card |

`dash` at 02:40Z was in the previous window's read and is carried here as undispositioned rather than new: it is a remote dashboard product whose card arrived after the evening pass listed its five, and it is held on the BI-dashboard class owned by [Tableau](/hermes/mcp/servers/external/tableau-mcp/), [Metabase](/hermes/mcp/servers/external/metabase-mcp/) and [Muvia BI](/hermes/mcp/servers/external/muvia-bi-mcp/).

## 2 catalogued, 2 guides

**[DocQuery MCP - Spreadsheet and PDFs, One Queryable Table](/hermes/mcp/servers/external/docquery-mcp/)** - remote Streamable HTTP at `https://docquery.io/api/v1/mcp`, JSON-RPC 2.0, no session header issued, `initialize` **200** as `docquery-mcp` **1.0.0** on protocol `2025-06-18` with **tools, resources and prompts** as capabilities, registry `io.docquery/docquery` **1.0.0** and **1.0.1**. The public demo key `dq_demo_readonly` - printed on the vendor's own homepage - drove **eight `tools/call` requests** against a linked workspace: **four** tools, all `readOnlyHint: true`, **three** resources (`docquery://tables/...`, `docquery://schema`) and **three** prompts. `list_tables` returned two tables (4 customers, 6 invoices), `list_relations` returned one `many_to_one` link, `query_table` returned 6 rows with `total` and `returned` reported separately, and `related_rows` resolved invoice `customer_id 2` to a single customer row in one hop. Two things earned the guide: an invoice carrying **`total: 0`** and status `paid` (a real zero, not a missing field), and a defect - calling a valid tool with a **missing** required argument returns HTTP 200, `isError: true`, and the text **`Unknown tool: query_table`**, which sends an agent looking for a different tool instead of a missing key.

**[CalcBloc MCP - Payroll Numbers With a Source Attached](/hermes/mcp/servers/external/calcbloc-mcp/)** - local stdio, npm `calcbloc-mcp` **0.1.1**, `initialize` as `calcbloc-mcp` **0.1.1** on protocol `2025-06-18` with `tools` only, registry `io.github.itmarkerz/calcbloc-mcp` **0.1.0** and **0.1.1**, MIT code and CC BY 4.0 data. **Five** tools, **nine calls driven**. `$100,000` in California came back as take-home **72,319.60** with deductions itemised to federal **13,170.04**, Social Security **6,200.00**, Medicare **1,450.00**, state **5,560.36** and CA SDI **1,300.00**, plus four official sources with their check dates. The federal figure was **reproduced by hand** from the 2026 single brackets the tool itself returns: taxable income 83,900 against the 16,100 standard deduction gives exactly **13,170.00**, and the four cents the tool reports is `506.54 x 26` - the biweekly rounding, not an error. Coverage is stated three ways across the vendor's own surfaces (npm and registry *37 countries*, `list_countries` **37 tax tables / 12 calculators**, the developers page *13 countries*) and the guide names the tool as the honest one. Three defects recorded: a per-country requirement (`region` for the US) that the tool schema cannot express, an enum that hyphenates (`income-tax`) where the prose does not, and a keyless ceiling of **5 requests a minute and 50 a day** that a real session hits inside five minutes.

## Also identified this pass (not catalogued)

Sixteen queue arrivals were read in one authenticated call with their bodies, and the feed's fifteen cards were triaged against the official registry.

- **The AdKit fleet** (#7246-adjacent feed cluster, nine cards inside **49** minutes) is **one product, not nine**: `io.github.adkit/ads` answers the registry at 1.0.1 through **1.0.4**, all declaring the same remote `https://mcp.adkit.so`. A keyless `initialize` against it answers **401** with `Authorization header with Bearer token required` and **no** `WWW-Authenticate` and no protected-resource document - a static token gate, the weakest evidence tier in the catalog. Campaign creation across Google, Meta, TikTok, Reddit, LinkedIn and X is a real operator surface, and it holds here for one reason: the product cannot be measured past its gate from this host, and the catalog does not ship guides on a marketing card plus a 401.
- **`agentmsgr`** (`com.agentmsgr/agentmsgr` **1.3.0**, **11** tools, remote at `app.agentmsgr.com/mcp` plus a `/shared` endpoint) is the closest call of the window: an agent group chat with messages, replies, approvals, wake links and join requests. It holds on the agent-coordination class carried by the catalog's own agent-messaging entries and on the same 401 tier without a document.
- **AISend, CVPosh, GrowFast, Bugsly, SEOBolt, RemixViral** (#7246 to #7251) were filed by **one account inside eight seconds**, all remote Streamable HTTP, all registry-listed, all with private source and three public client-config repositories each (`-claude-plugin`, `-gemini-extension`, `-cursor-kit`). That is one publisher shipping a connector per product; the six are dispositoned as a fleet, and **SEOBolt** stays covered by the SEO-audit class this catalog already carries in depth.
- **Runner** (`io.github.runtheworldai/runner`, "an AI growth team for your business", OAuth with your own account) holds on the AI-marketing-agent class owned by **Marsell** and **Crevio**.
- **Ironflow** (Hyperliquid trades, candles, funding, open interest, liquidations, read-only SQL over every fill since 25 May 2025) is a strong data surface and holds on the market-data class carried by **TradingData** (48 tools) and **TradingAgentStack**.
- **Festapp** and **vstupenky.online** (#7255, #7256) were filed two seconds apart by one submitter and are the same event-ticketing product for two Czech brands; the event-ops class is carried by **Nowistay** and the venue group.
- **OpenDocKit** (local stdio, 19 document formats including the Korean HWP/HWPX, tables preserved) is very close to the shipped **DocQuery** guide's subject and is named in its See-also block rather than duplicated.
- **Alloy** (open-source physics engine for robot learning), **Pyfio Router** (a five-tool demo with no hosted endpoint), **Manulyx** (LaTeX editor for researchers) and **`calculate_placements`-style local utilities** are outside the operator catalog's scope or self-declared demos.
- **`sportsgameodds`** and **`escro`** are recorded as **unresolved** rather than absent: neither term returns a record from the official registry under any of the name forms tried, and neither detail route would answer from this host.

## Method notes

The feed's relative-time stamps again read `M/D/YYYY, HH:MM AM/PM` in the `title` attribute and are **UTC** - converted before the cutoff was applied, which is why a 03:00 MST run compares against a 04:06Z stamp and not a 04:06 local one. The submission queue was read through `GET /repos/chatmcp/mcpso/issues?state=all&sort=created&direction=desc` with bodies included, one call for the sixteen-entry window.

The catalog figures were updated in the same pass: **1,162** guide directories and **1,307** entries.
