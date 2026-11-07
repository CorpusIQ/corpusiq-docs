---
title: "MCP Server Discovery - November 6, 2026 (Evening Sweep)"
description: "First canonical wave in four passes: 126 new server URLs, two guides, an Excel engine that audits formulas and a carbon credit registry index."
last_updated: 2026-11-06
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november6-2026-evening"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 6, 2026 (Evening Sweep)

## Summary

This pass fired on the **21:00 MST** tick, ten hours after the midday supplement, and the sitemap that had been flat for four passes finally moved. The twelve-sitemap canonical came back with **126** server URLs that were not there at the 04:32 capture and **zero** removals, taking the universe from **19,733** to **19,859**. The mcp.so feed and the submission queue were quiet by comparison: **2** cards above the midday-supplement stamp and **16** new issues.

**Two servers were catalogued**, and they came from opposite surfaces. One arrived in the submission queue and the other only in the sitemap, which is the argument for reading all three surfaces on every pass rather than the one that moved last time.

| Surface | Read | Result |
| --- | --- | --- |
| mcpservers.org twelve-sitemap canonical | all 15 documents, plain urllib, locale prefixes stripped, diffed against the 04:32 capture | **19,859** server URLs against **19,733**: **+126**, **-0** |
| mcpservers.org `/all` | direct fetch with a browser user agent | **403** for the sixth consecutive pass, a standing condition |
| mcp.so homepage | direct fetch plus a cache-busted second read | **132** card objects, **109** distinct stamps, newest `2026-11-07T02:31:44.172Z` on both reads, **2** cards above the midday-supplement stamp |
| chatmcp/mcpso submission queue | authenticated API, `per_page=40` | **16** numbers from `#6862` to `#6877`, every one an arrival |
| Endpoint probes | keyless `initialize` and `tools/list` | `https://api.basis1.tech/mcp` answers **200** twice and **401** on a tool call; `https://carbonmeld.com/api/v1/mcp` answers **401** with a protected-resource document |

## The counting note the canonical needs

The raw sitemap union now reads **29,197** URLs, and only **19,859** of them are server pages. The rest is the `static.xml` map that carries the marketing surface: `/topics/*`, `/submit`, `/webmcp` and a long tail of vendor help pages that were indexed as `/servers/...` paths without being server records. The filter that makes the diff honest is the `/servers/` prefix applied after stripping the inline locale prefixes, and both steps are required: a naive union over-reports by roughly **9,300** URLs per pass, and a naive diff without the locale strip reads the same server in twelve languages as twelve additions.

One addition is worth naming because it looks like a duplicate and is not: `mcpservers.org/servers/corpusiq/corpusiq-docs` is the documentation repository listed as its own entry, which means our own tail now appears in the directory twice under two different slugs while the canonical still carries `/servers/corpusiq-io` as the product page.

## New Servers Catalogued

### [Basis MCP - The Excel Engine an Agent Can Audit](/hermes/mcp/servers/external/basis-mcp/)

From the queue (`#6864`). Hosted remote server at `https://api.basis1.tech/mcp`, Streamable HTTP with an API key as a bearer, plus an npm stdio package (`npx -y @basis1/mcp`). A keyless `initialize` answers **200** as `basis-mcp` **0.0.1** on protocol `2025-06-18`, and a keyless `tools/list` returns all **25** tools with annotations and schemas, so the surface is the server's own contract. A keyless `tools/call` answers `401 unauthorized`, and the parse semantics are read from the vendor's machine-readable references, so the tier is **documented with the schema read live**, not driven.

It earns a guide because nothing else here can check a workbook's arithmetic. The parser turns an `.xlsx` into a typed cell graph, a formula dependency edge list, cell-anchored images and an audit record; the audit re-runs every formula against the value Excel itself cached and reports divergences by coordinate; and the findings name hard-coded plugs found by bytecode-program identity rather than by heuristic, broken references and their dependents, circularity with the workbook's own iterative-calculation setting taken into account, and links to workbooks that are not there. On the vendor's public corpora, **43.2%** of substantial models (**1,000** formulas or more) across the Enron spreadsheets and the FUSE corpus carry at least one plug, and **97.31%** of **3,344** FUSE workbooks under 1 MB recompute with zero mismatches over **4,033,846** formulas compared. Pricing is free during early access with **1,000** requests, **2 GB** in and **50,000,000** cells out per key per month, **402** `quota_exceeded` when a dimension runs out, in-memory jobs with a **15-minute** TTL and no SLA, all stated by the vendor rather than implied.

### [CarbonMeld MCP - Carbon Credits From Their Documents](/hermes/mcp/servers/external/carbonmeld-mcp/)

From the sitemap only. Remote server at `https://carbonmeld.com/api/v1/mcp`, JSON-RPC over POST, **15** read-only tools behind either an OAuth sign-in with dynamic client registration or an API key. A keyless `initialize` answers **401** with `{"error":"Missing or invalid API key."}` and a `WWW-Authenticate` header naming `https://carbonmeld.com/.well-known/oauth-protected-resource/api/v1/mcp`, whose own body confirms one scope `carbonmeld.read` and a header bearer. **Documented, not driven**, because the records past the public summary need a Premium account.

It earns a guide because the catalogue could account for carbon and could not buy it. **GreenCalculus** answers how much a company emits, with sourced factors and pinned data versions, and that was the whole of the subject here. CarbonMeld indexes **34,421** projects across **30** registries and **12** marketplaces, scores them from their registry documents under a published method (v2.2, every rule queryable by id through `get_method`), and serves the search, the record, the red flags, the vintages, the marketplace listings, the CORSIA labels, the ICVCM CCP tracker, a buyer's public retirement records and an offer check that compares a broker's pasted text against the recorded registration. Premium is **EUR 9 + VAT** a month for **30** different projects a day and **300** API requests, Pro **EUR 49** for **300** and **1,000**, shared across the site, the PDF reports, REST and MCP, with a **120**-requests-a-minute burst limit and a **00:00 UTC** reset.

## Held, With the Class Named

**From the queue (14 arrivals held):**

- **US Business Verification** (`ai.greyridgesignals/business-verification-mcp`, state registries for NY, CO and CT plus an OFAC SDN screen downloaded per call, a scored `match_confidence` instead of a string match) on the business-identity and sanctions classes already carried by Synorb, FinzData, SimilarLabs and Velarion, and by ScreenVerity, QoreNext Trade Screening and Atlas Verified. The Colorado UCC-lien profile is the one field that is genuinely new, and it is a capability improvement inside a class with an owner, which is the BACKLNK ruling applied again.
- **AdRails** (`dev.adrails/adrails` **0.6.2**, Google Ads, Local Services Ads and ChatGPT Ads with plan, validate-only, commit, spending caps the agent cannot edit, human activation and a hash-chained audit log) on the ads-execution class, and specifically behind the approval-gate precedent set by **lookfirst**, which already binds an approval to a call's own arguments with a per-call HMAC. A second approval mechanism is a mechanism, not a class. Note the name collision: `adrails.ai` is already catalogued as a Shopify revenue-reconciliation server, and this is a different product on `adrails.dev`.
- **LinkJolt** (`io.linkjolt/linkjolt`, affiliate program setup with commission benchmarks drawn from real SaaS programs, Stripe/Paddle/Polar/Creem tracking, affiliate approval, and no ability to move money) as marketing operations adjacent to the revenue-attribution entries. Held on a keyless-free but account-gated surface with no driven session, not on class.
- **Global Law** (`lexifina/global-law`, local stdio, 208 jurisdictions and 714 corpora read from local git histories, `world_on_date`, `who_wrote`, `compare_dates`, `provision_history`, no network calls) on the legal class carried by LegalCode, Patsnap and the Taiwan and corpus-law entries. The point-in-time mechanism is the strongest in that class this month and it is still a local corpus of public law rather than a business system.
- **Basis** catalogued; **musterd** (`io.musterd/musterd`, local daemon, roster and lanes with acceptance before done) as agent coordination, the class this documentation set covers in prose rather than in the catalog; **PairOnce** as a device bridge for agent-to-phone file transfer; **CheckMyApp** as post-deploy journey testing beside the QA and browser-automation entries; **CutClip.one** on media generation; **Schedchie** on social scheduling across 13 networks; **ChefBear** as a consumer recipe app with an OAuth approval in its own iPhone app; **GAMES.GG** as a consumer games vertical; **The Wyze Blog** as a UK letting-agent content surface; **Highwire** and **kdraigo** on the crypto and trading class beside PairBook and the perpetuals entries; **Agent Field Trip** outside operator scope as a public-domain art museum for agents.

**From the sitemap (126 additions):**

Three cohorts account for most of the wave and each is dispositioned once. A **documentation-mirror fleet** of about 20 slugs reads `-docs`, `-docs-mcp`, `-agents`, `-llms-txt` or `/help/` in the path, which is a product documentation route rather than a business surface, and the ruling stands from earlier passes. A **marketing-page cohort** of about 25 `www-` and `-agents` slugs is the same vendors' landing pages indexed as servers, including GAMES.GG, ChefBear, Schedchie, Purple8, FirstAISearch, PropertyIndex, Soundlink, Invio and Xero in one path. And **eight `shunshi-ai` servers** (bazi, kangxi, liuyao, naming, tarot, zeri, ziwei, astro) are one author's fleet, held as a single line under the single-author rule.

The business-relevant remainder, each held on a class with an owner: **Tariffs API** (`tariffsapi.com`, US import duty by HTS code with Chapter 99 resolved, Section 301, 232 and 338 stacked) behind **tariff-monitor-mcp**, which already stacks MFN, 301 and 232 over 19,856 HTS lines and prices the exposure; **TrackCVE** (every public CVE with exploitation signals, free and open) on the vulnerability class beside VulX Watch and the x402 security entries; **AdSpends** (Meta ad library intelligence at the advertorial level) on ads intelligence; **GapCite** (GEO and AEO visibility tracking) on the visibility class with seven owners, the BACKLNK ruling unchanged; **KafDesk** (native Kafka client with a built-in MCP server) on developer tooling; **Context Engine** (one memory shared by agents and a team) on agent memory beside Konshus, Azquo, Agentic Memory and SPM; **AI BIM Tool** and **uCAD** on design tooling; **Tokfluence** (18M TikTok creators) on influencer analytics beside IQfluence, Viral Manager and UGC Chart; **SyncWith** on spreadsheet data import; **Seqora** on database clients; **Kanal** on WhatsApp commerce for Shopify; **Marian** as a pre-launch consumer mortgage waitlist; **Hea** as a consumer health companion; **Tulina** as an automation platform; **GLO case search** on legal research; **InboxSim** as email testing; **Adspends** and **AI Agent Search Optimization** as prior dispositions in this week's prose; **Sellfy**, **LoadOptimizer**, **PatentRef**, **Sanctionlistcheck**, **PastCharts**, **Odds-API**, **PuraSIM**, **PepBank**, **Flavo** and **ManaWG** already catalogued or held earlier this week. **Bosco Labs** did not resolve a hostname and was not judged.

## Core Listing Check

- **mcpservers.org** - `/servers/corpusiq-io` is present in the freshly fetched canonical (one occurrence, and a second entry now carries the docs repository at `/servers/corpusiq/corpusiq-docs`). The detail page answers the standing **403**, and `/all` answers **403** as well.
- **mcp.so** - still not listed. All four direct slugs (`corpusiq`, `corpusiq-io`, `multi-source-mcp`, `corpusiq-mcp`) return **404**.
- **Glama** - **200** on `/mcp/connectors/io.corpusiq/multi-source-mcp`.
- **Official MCP registry** - four active records, **1.0.3** the newest at `2026-10-24T04:07:42Z` and `isLatest: true`. Its description reads **40+** business systems, which is the correction earlier passes carried as drift against a 30+ catalog: the drift is closed at the registry.

## Counts

- Canonical: **19,733** to **19,859** server URLs, **+126** and **-0**, from **29,197** raw URLs across 15 sitemap documents with the locale prefixes stripped before the diff.
- mcp.so: **132** card objects and **109** distinct stamps on both reads, newest `2026-11-07T02:31:44.172Z`, **2** cards above the midday-supplement stamp.
- Submission queue: **16** numbers, `#6862` to `#6877`, all arrivals.
- Candidates evaluated: **144** (**126** sitemap additions, **16** queue arrivals, **2** feed cards). Catalogued **2**, held **142**.
- Guide tree: **1,109** directories before this pass, **1,111** after. **1,252** entries counting single-file guides before, **1,254** after.
- Endpoint probes: **3**. `api.basis1.tech/mcp` **200** on `initialize` and `tools/list`, **401** on `tools/call`; `carbonmeld.com/api/v1/mcp` **401** with a protected-resource document; `carbonmeld.com/.well-known/oauth-protected-resource/api/v1/mcp` **200**.
