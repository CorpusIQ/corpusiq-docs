---
title: "MCP Server Discovery - November 7, 2026 (Night)"
description: "Flat canonical six hours after the evening pass, 15 queue arrivals, and one server catalogued: a document engine that edits the real xlsm."
last_updated: 2026-11-07
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november7-2026-night"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 7, 2026 (Night)

## Summary

This pass fired on the **03:00 MST** tick, six hours after the November 6 evening sweep, and the sitemap was flat: **19,859** server URLs against **19,859** at the evening capture, **zero additions and zero removals**. The window came from the two surfaces that move independently of it - **2** cards above the evening stamp on the mcp.so homepage and **15** arrivals in the submission queue from `#6878` to `#6892` - plus the two entries the evening pass shipped, which were re-probed here rather than taken on trust.

**One server was catalogued.** It arrived as `#6890` in the queue and it is the first surface in this catalog that edits the file a business already runs on and hands it back with its macro project intact.

## Provenance note: a stale clone nearly duplicated the last pass

The catalogue clone used for this pass was three commits behind `origin/main`, which already carried the November 6 evening sweep and its two guides for **Basis MCP** and **CarbonMeld MCP**. The crossref therefore ran against a ledger missing the newest pass, and both servers were independently researched, probed and written up as new before the duplicate was caught at the branch step: the fetch that created the working branch refused to check out, because `basis-mcp` and `carbonmeld-mcp` already existed on the remote.

Both duplicate drafts were discarded rather than merged. What survives from that work is the independent confirmation of the evening pass's two probes, which is worth recording: **Basis** answered a keyless `initialize` **200** as `basis-mcp` **0.0.1** and `tools/list` returned all **25** tools while `tools/call` answered **401** `missing or invalid bearer token`; **CarbonMeld** answered a keyless `initialize` **401** with `WWW-Authenticate` naming `https://carbonmeld.com/.well-known/oauth-protected-resource/api/v1/mcp` and `scope="carbonmeld.read"`. Both match what the evening pass reported. The operational lesson is in the procedure, not in the products: pull the catalogue clone before the crossref, because a six-hour gap is enough for a sibling pass to fill the ledger.

## Sources Swept

| Surface | Read | Result |
| --- | --- | --- |
| mcpservers.org twelve-sitemap canonical | 12 server maps (`servers/1` to `servers/10`, `priority-servers`, `remote-mcp-servers`) fetched fresh, plain urllib, inline locale prefixes stripped, `/servers/` subset only | **63,180** raw `<loc>` entries, **19,859** server URLs. Against the November 5 capture of **19,513**: **346** additions, **0** removals, and all 346 are the November 6 passes' own additions, so nothing entered in this window |
| mcpservers.org `/all` | direct fetch with a browser user agent, then the r.jina.ai reader proxy | **403** `Just a moment`, then **401 03** bad IP reputation, the standing condition since November 4 |
| mcp.so homepage | direct fetch with a browser user agent, then a cache-busted second read | **188** `createdAt` occurrences parsing to **172** slug/stamp pairs across **145** distinct cards; newest `2026-11-07T08:00:01.000Z` on both reads; **2** cards above the evening stamp `2026-11-07T02:31:44.172Z` |
| chatmcp/mcpso submission queue | authenticated `gh api`, 60 issues in one call | **15** arrivals from `#6878` The AI Record to `#6892` CrakSEO skills, none a listing update |
| Endpoint probes | keyless `initialize`, then `tools/list`, then a `tools/call` where the server allowed it | **3**: `sumoffice-document` **0.3.0** keyless **200** with **21** tools, driven on the read path; `basis-mcp` **0.0.1** keyless **200** with **25** tools and **401** on the call; `carbonmeld` **401** with a protected-resource document |
| Official MCP registry | `registry.modelcontextprotocol.io` searches per candidate | `com.sumoffice/office`, `com.chef-bear/chefbear`, `gg.games/games-gg`, `com.the-ai-record/archive`, `com.openrobotkits/openrobotkits`, `ai.imagera/imagera`, `com.sugusite/sugusite`, `dev.hotskills/hotskills` and others resolved |
| Core listing check | canonical grep, Glama, registry, four mcp.so slugs | Unchanged: carried in the canonical, Glama **200**, registry **1.0.3** reading **40+ business systems**, mcp.so **404** on all four |

## The proof that the canonical was flat

A count is not a diff. The argument here is arithmetic and it is checkable: this pass fetched **19,859** distinct server URLs; the last capture on record is **19,513**; the two November 6 passes added **220** (night and midday) and then **126** (evening), which is **346**; and the diff against 19,513 returned exactly **346** additions and **0** removals. A single new server in the six-hour window would have made that 347. Every one of the 346 also matched a ledger surface - **3** an on-disk guide directory, **25** a prior sweep under a compact token, **205** a ledger token, and the rest the documentation-mirror and product-respelling families the earlier passes dispositioned.

The two false clears worth naming from that token pass: `getfund-space-en-help-mcp` matched the string `getfundamentals` inside a tool description, and `lulubox-store` matched the bare word `store`. A short token tested against the concatenated ledger matches something almost every time, which is why the context slice decides the disposition and not the boolean.

## The window that did move

**mcp.so** put two cards above the evening stamp: **Przypominamy.com SMS** at `2026-11-07T06:34:38.685Z`, a Polish SMS reminder service held as a single-market source, and **Zynlex** at `2026-11-07T08:00:01.000Z`, a Windows browser for local web development with a built-in MCP server, held as developer tooling.

The **submission queue** carried 15 arrivals and one of them was worth a guide.

## Catalogued: SumOffice MCP

`https://view.sumoffice.com/mcp`, registered as `com.sumoffice/office`, `sumoffice-document` **0.3.0**, **21** tools, **no account and no key**, plus the same server as a Docker image over stdio for teams that cannot send files out. It opens a real `.docx`, `.xlsx` or `.xlsm` up to 50 MB in a private editor cabin for the session, reads cells and formulas, the VBA project with its entry points and blockers, the Power Query steps and load targets, the paragraphs, comments and tracked changes, proposes a change, applies it only on approval, and hands back a copy as a 24-hour download link.

**Driven on the read path.** The `cashflow` demo opened as a genuine `.xlsm`: three sheets (`Cash flow` A1:I33, `Bank export` A1:F61, `Monthly from bank` A1:F13), `workbook_inspect` reporting `vba_project: true`, `vba_signature: false`, two tables, one query table, one connection, `data_mashup: true` and zero external links. `sheet_read` returned values and formulas side by side (`D28` carrying `=B28-C28` with its computed `-57,200`). `macro_list` returned `Module1.FlagCashGaps` user-runnable on the **native** route with no blockers and `Sheet1.Worksheet_Change` on the **excel-bridge** route blocked as an event-or-document module at line 12, without executing anything. `query_list` returned `MonthlyCashflow` with its load target, background refresh and refreshed version 6, and **the M body withheld by engine policy with only its sha256 exposed** - the right call for the string that carries a connection credential.

**The round trip is the argument.** The vendor's published proof, dated **20 September 2026**: an agent opened an Enron workbook with a VBA project and a dynamic-array UDF, proposed a formula, applied it and saved a copy; Excel 16 opened it with no repair dialog and `xl/vbaProject.bin` was byte-identical. Byte-identical macros are where document tooling normally fails, and they are the reason an operator can let an agent touch a finance file at all.

**The write path refused twice here, and both refusals are in the guide.** `unsupported-cell-preview-edits` for plain numeric inputs, where the preview accepts only formatting, formulas or drag-fill; then `busy: all 5 editor cabins are in use`, the documented concurrency ceiling of the hosted server, with no close-cabin tool among the 21. Recorded as a limit rather than smoothed over.

## Held, with the class owner named

- **E-signature and contract flow:** **Layers** (`#6889`, `md.layers/workspace`, contracts, tasks, pages, forms and Drive, with a link the other side can sign and sign-in through a Layers account). The nearest catalogued name is **Signatoro**, which reads as an e-signature surface but serves an email signature block, so this is the closest thing to a first-of-class in the window and the description is one line with no tool list. Held pending a driven session rather than shipped on a paragraph.
- **App administration:** **VibeAdmin** (`#6886`) exposes a SaaS app's users, support actions, growth and retention, segments, feature flags and email behind a scoped API key with an audit log. Real, and product analytics is a carried class.
- **MCP security tooling:** **mcpsteward** (`#6888`) inventories configured MCP servers, flags credentials in client configs and grades a server against the 2026-07-28 spec with a citation per finding. Agent infrastructure rather than a business data surface, and the class is carried.
- **SEO:** **Docket SEO** (`#6880`) does free read-only page audits, AI crawler access and redirect tracing, on a class with twenty guides.
- **AI-use research:** **The AI Record** (`#6878`) is a cited archive of verbatim statements about how organisations use AI, with evidence grades. Interesting, and not a business system a connector reads.
- **Regional and single-market:** **ru-marketplace-mcp** (`#6891`, 12 Russian and Chinese marketplaces with cross-marketplace price comparison, keyless, the strongest of the regional group), **明乐智保** (`#6882`, Chinese mainland life insurance disclosures with RFC 9728 metadata), **GCC Domestic** (1,700 licensed domestic-worker agencies across six GCC countries) and **Przypominamy.com SMS**. Each needs a driven session before a guide is worth writing.
- **Consumer and vertical:** **ChefBear** (`#6862`), **GAMES.GG** (`#6863`), **Ask Garçon**, **CoKarTa**, **BeautySpark**, **Hea**, **TimeZero**, **Agent Field Trip** (`#6877`), **OpenRobotKits** (`#6879`) and **Geppetto Robot Directory**.
- **Generation, speech and devices:** **Imagera** (`#6883`), **CutClip.one** (`#6868`), **Vidaro Studio**, **Arumi**, **NanoPic**, **Murmur** (`#6881`, macOS on-device TTS), **SecretVoice**, **Zynlex** (`#6884`), **Snaggy** (`#6885`, local Mac bookmarks), **PairOnce** (`#6876`).
- **Publishing and delivery:** **Sugusite** (`#6887`) as a Japanese static host with OAuth, **host0** and **HotCodePush** as app publishing and OTA delivery, **Layers** above on documents.
- **Coordination and revenue:** **Botsesh**, **LinkGents**, **LinkJolt** (`#6865`) on affiliate administration beside Cello, GrowSurf and Ambassly, **GetKanal** (`#6869`) on WhatsApp marketing for Shopify, **Tulina** on revenue operations, **RealAI** on property data, **Invio Xero** on geo-niche accounting, **Highwire** (`#6871`) and **kdraigo** (`#6872`) on crypto trading and backtesting, **US Business Verification** (`#6870`) and **Entitylight** on the KYB class carried by Company Identity Resolver, registry-mcp, Prometiam Risk, honest-vies, contix, ScreenVerity, QoreNext Trade Screening and Atlas Verified, **TamingDNS** on email authentication where how.is answers with 17 checks, **Tokfluence** on creator analytics, **CheckMyApp** on post-deploy site QA beside SiteGoalie and SquirrelScan, **Schedchie** (`#6873`) on the saturated social scheduling class, and **CrakSEO** (`#6892`) as agent skills over an already-carried SEO class.

## Core listing check

Measured in this pass rather than inherited:

| Surface | Result |
| --- | --- |
| mcpservers.org canonical | `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs` both present in the fresh capture |
| mcpservers.org detail | `/servers/corpusiq-io` answers **403**, the same condition that refuses `/all` |
| Glama | `/mcp/connectors/io.corpusiq/multi-source-mcp` answers **200** |
| Official MCP registry | four records for `io.corpusiq/multi-source-mcp`, **1.0.0** to **1.0.3**, the newest published `2026-10-24T04:07:42Z` and reading "One governed MCP endpoint for **40+ business systems**" |
| mcp.so | not listed: `/server/corpusiq`, `/server/corpusiq-io`, `/server/corpusiq-mcp` and `/server/io.corpusiq` all **404** |

## Counts

- Canonical **19,859** against **19,859**, **0** additions and **0** removals; the **346** returned against the November 5 capture are the November 6 passes' own arrivals, **233** of them matched a ledger surface and **114** were unledgered slugs, **57** registry-resolved.
- mcp.so **188** `createdAt` occurrences, **172** slug/stamp pairs, **145** distinct cards, newest `2026-11-07T08:00:01.000Z` on both reads, **2** cards above the evening stamp.
- Submission window **15** numbers, `#6878` to `#6892`, all arrivals.
- Endpoint probes **3**: **2** keyless **200** (`sumoffice-document` **0.3.0** with **21** tools, `basis-mcp` **0.0.1** with **25**), **1** **401** with protected-resource metadata and scope `carbonmeld.read`.
- Guide tree **1,111** directories before this pass and **1,112** after; **143** single-file guides unchanged; **1,254** entries before and **1,255** after.
- **1** catalogued, **1** guide, **14** window candidates held with their class named, and two duplicate drafts discarded at the branch step.
