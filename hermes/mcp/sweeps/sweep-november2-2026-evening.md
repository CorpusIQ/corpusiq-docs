---
title: "MCP Server Discovery - November 2, 2026 (Evening)"
description: "Evening pass ten hours after the midday supplement: zero churn on the directory page, 27 new submissions, and four servers earning guides."
last_updated: 2026-11-02
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november2-2026-evening"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 2, 2026 (Evening Sweep)

## Summary

Ten hours after the midday supplement and eighteen after the night pass. This is the first evening read of the day where one of the three source surfaces produced **nothing at all**: the mcpservers.org `/all` newest page returned **18,887** on both reads with the same thirty slugs the supplement had already dispositioned, so the page had not turned over between 11:00 MST and 21:00 MST. That is worth recording rather than glossing, because the previous four passes all saw churn on that page and a zero-churn read is what proves the other two surfaces are doing the work.

They were. The submission window carried **27** submissions between **#6624** and **#6650** and the mcp.so homepage carried **108** distinct cards with three above the supplement's newest stamp. Four arrivals earned a guide, and two of the four were driven end to end with every tool called.

The two driven finds are the strongest of the day. **AICTIONBOT Werkbank MCP** answers seven procurement questions with a verdict and a number rather than a summary, including a supplier price increase benchmarked against the German producer price index: a 12 percent request against a 4.8 percent market move came back with a counter-offer ceiling. **Context Pill MCP** publishes the claims it has already checked, each labelled with how it was checked and with the trust score of the source that made it, which is a source scorecard rather than a fact checker. **Cronitor MCP** is the official vendor's hosted control plane over an account an operator already has, probed to a **401** with protected-resource metadata and documented rather than driven. **WISEPIM Commerce Reference MCP** fills a hard gap: three offline tools including green-claims screening against Directive (EU) 2024/825, a directive no guide in this catalog mentioned before.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| chatmcp/mcpso submission window | one authenticated call, bodies included | **#6624** at `18:15:08Z` to **#6650** at `03:39:52Z`, **27** submissions, **26** distinct after `FitCard` was filed twice twenty-four seconds apart |
| mcp.so homepage `recentServers` | direct, `--compressed`, TanStack block | **132** raw matches collapsed to **108** distinct cards; newest `2026-11-03T03:04:06Z`, three above the supplement stamp of `2026-11-02T14:39:24Z` |
| mcpservers.org `/all` | r.jina.ai, read twice with different cache busters and user agents | **18,887** on both reads, thirty slugs identical to the midday supplement's page, **zero churn** |
| Endpoint probes | keyless JSON-RPC | **200** on `aictionbot-werkbank` (**7** tools, all called), `context-pill` (**3** tools, all called), `stophy` (**3**), `webarm24` (**61** declared), `green-screen-memes` (**7**), `jaybird-website` (**8**); **401** on `goanyapi` (`mcp:invoke`), `cronitor`, `pocketarchive` (`archive:read`, `archive:write`) |
| Listing surfaces | direct and registry | mcp.so four CorpusIQ slugs **404**; official registry `io.corpusiq/multi-source-mcp` active on `https://mcp2.corpusiq.io/mcp`; the Web, Glama and Smithery reads carried from the midday pass and re-stated below |

## New Servers Catalogued

### AICTIONBOT Werkbank MCP - Procurement Checks That Return a Verdict

Relevance: HIGH. **Tier 1, driven** (keyless `initialize` **200** as `aictionbot-werkbank` **1.2.0**, `tools/list` returning **7** tools, and all seven called live).

The product is seven deterministic checks for a purchasing or accounts payable desk, by KULIC Advisory of Cologne, with no model inside any of them and nothing stored. The one that carries the weight compares a supplier's requested increase against the official Eurostat producer price index for the category, from the month of the last agreed price. Category **C17** paper and packaging with a last agreement of **2024-01** and a **12** percent request returned a market change of **4.8** percent over the observation to **2026-09**, a gap of **7.2** percentage points, a verdict of `hoch` and a counter-offer ceiling of **4.8**. That is a negotiating position with an index date attached, not an opinion.

The other six checks each answer one question with a verdict. A sanctions screen returned **8** possible matches with list, entity type, programme and similarity, followed by the read date of every list. A renewal calculator turned contract start, initial term, renewal and notice period into a last notice day and a days-remaining count. A discount radar priced the discounts expiring inside the next payment runs and the ones already lost, with the last payment run that still catches the live one. An approval matrix check returned a stop on a departed approver still named in the matrix and a check on the missing deputy beside it. A pre-payment check returned `stopp` when the invoice's bank account stood in no vendor record, which is the fraud pattern that costs small businesses the most.

It earns a guide because the neighbours are all single-purpose. Sanctions Screening MCP and mcp-sanctions screen a name. Monitly serves the Eurostat series as a searchable dataset. Invoice Parser and byondr Receipts read a document. Gov Contract Radar finds tenders. None of them returns in-line, check or stop on an invoice, a renewal or a price request.

Two defects go into the guide because driving the server found them. The free-text item arrays (`matrix`, `people`, `open_items`, `vendor_master`) declare no properties, so a people row keyed `name` produced "not in the list" for a person who was in the list while the same row keyed `person` produced the correct departure stop. And `language: "en"` switches only the summary sentence: every finding underneath stays German, as do all structured keys.

Guide: [AICTIONBOT Werkbank MCP](/hermes/mcp/servers/external/aictionbot-werkbank-mcp/)

### Context Pill MCP - The Source Scorecard Behind an AI Claim

Relevance: HIGH. **Tier 1, driven** (keyless `initialize` **200** as `context-pill` **0.1.0**, **3** tools listed and all three called).

A daily feed of AI releases where every item carries four things a feed normally drops: how it was checked, the source's trust score with a conservative lower bound, the evidence link for the primary source, and the date it will be re-checked. The drop read here covered **2026-11-02** on scanner day **18** with **11** checked claims from **10** items, and the item listed as not verified was excluded from the answer rather than mixed in.

The catalogue point is the source table. `list_sources` returned **20** sources, each starting from a neutral Beta(2,2) prior of **0.50** and moving only when a claim is re-checked fourteen days after publication. Anthropic stood at **0.799** with a lower bound of **0.630** over **7** resolved re-checks, Latent Space at **0.761** and **0.586** over **8**, Google DeepMind at **0.692** over **4**, OpenAI at **0.636** over **2**. Twelve of the twenty were still on the prior, which the guide states plainly: most scores are a starting position, not a verdict.

`search_claims` answered **11** matches for a model name out of **121** claims in the ledger, each carrying its status at publication, its current state and its re-check date.

It earns a guide because VerifyAPI checks the claim you bring and signs a receipt, Factanker is the evidence layer for company numbers, and the news surfaces carry no verification label or source score at all. This is the other direction: it publishes what it has already checked, with the check attached.

Guide: [Context Pill MCP](/hermes/mcp/servers/external/context-pill-mcp/)

### Cronitor MCP - The Watchers Cannot Change a Monitor

Relevance: HIGH. **Tier 2** (keyless probe **401** with `WWW-Authenticate: Bearer resource_metadata="https://cronitor.io/.well-known/oauth-protected-resource/mcp"`, tools documented in the vendor reference, **no tool called**).

The official hosted server at `https://cronitor.io/mcp` is a control plane over a Cronitor account: monitors, status pages and components, issues, notification lists, groups, environments and read-only metrics, **71** tools by the vendor's count with `additionalProperties: false` on every schema.

Three details make it usable rather than merely present. `setup_monitor` is an idempotent upsert on a stable key, so a runbook converges the account instead of accumulating duplicates, and every monitor it creates is tagged `via:mcp`. `get_setup_context` returns the plan limits, the default environment and timezone, and the name of the key variable, but never the key. And the vendor draws the boundary in the right place: telemetry never travels through MCP, because a monitor reported through the agent goes quiet exactly when the agent does.

The authorization shape needs to be read before connecting. OAuth 2.1 with PKCE through a **Client ID Metadata Document** and **no dynamic client registration**, which means some clients will fail to connect. No `Mcp-Session-Id` is ever issued. The permission set is the signed-in user's role, capped at the SDK Integration bundle, and role or organization changes take effect on the next request rather than at token expiry.

It earns a guide because of a note the midday pass left. That pass held a submission called `norc` on the cron and uptime class carried by WatchCron, healthchecks, RealUptime and HostTracker, and observed that the group monitors jobs rather than editing them, so a server which configures from chat was worth a second look. This is that second look, with the caveat stated: the hosted server configures the monitoring account, not the crontab. Only the local CronitorCLI server can read or edit the host's crontab, and it is a separate connection.

Guide: [Cronitor MCP](/hermes/mcp/servers/external/cronitor-mcp/)

### WISEPIM Commerce Reference MCP - The Rulebook Beside the Catalog

Relevance: HIGH for ecommerce operators selling into the EU. **Tier 3** (release package and README inspected, no hosted endpoint, **no tool called**).

Three offline read-only tools in a pinned v1.0.0 tarball from GitHub Releases: EU Combined Nomenclature 2026 heading lookup with the chapter and four-digit heading candidates for review, published field checklists across **12** marketplaces and commerce channels, and a phrase scanner for green claims in English, Dutch, German and French against Directive (EU) 2024/825.

The class test is the reason it ships. A grep across every guide for Directive 2024/825, green claims and greenwashing returned **nothing**, so this is a genuinely new surface rather than a crowded one. The commerce entries in this catalog read a store: Mamba profiles a platform, Shopify Speed Check audits a storefront. This reads a rulebook.

Two properties are worth stating because they are checkable rather than claimed. The install points at a versioned release tarball rather than a floating npm range, so the version audited is the version that runs. And the package is described as taking no credentials and making no outbound requests, which is the only sensible design for a local reference table and also the reason it needs no terms negotiation to try.

Guide: [WISEPIM Commerce Reference MCP](/hermes/mcp/servers/external/wisepim-commerce-reference-mcp/)

## Also Identified (Not Catalogued)

Every submission in the window was read with its body, and every card above the stamp was probed. The holds below are measured where a measurement was possible.

`Fetch Router` (`#6626`) bills only on success, detects block and challenge pages and falls back to a headless browser, held on the fetch and scrape class carried by Browserless, PubCrawl, LiteScrape and Ultimate Web Scraper. `Stophy` (`#6625`) answered keyless with **3** meta-tools that discover and then call endpoints across search, places, products, jobs and homes at $1.50 per thousand calls, held on the saturated web search class. `WebArm24` (`#6629`) answered a keyless `initialize` **200** as `webarm24` with a pipeline, cron, cloud browser and step library for its n8n-style platform, held on the workflow automation class carried by n8n MCP and DocsAutomator. `GoAnyAPI` (`#6644`) is **38** read-only SEO, SERP, backlink, domain rating, traffic, ads transparency and trends tools behind OAuth with the `mcp:invoke` scope and protected-resource metadata on its **401**, held on the SEO class, which carries twenty guides including the official Ahrefs MCP.

`Pocket Archive` (`#6639`) is the strongest hold and the one worth revisiting. A private document archive for receipts, bills, contracts, warranties and tax records with OCR text page by page, search by keyword, vendor, date or amount, upload and download of originals, and deadline tracking, behind OAuth with `archive:read` and `archive:write` scopes. It is held on the document retrieval class carried by byondr Receipts, Invoice Parser and Pocket Invoice, with one difference recorded rather than ignored: it is the only one of those that is a persistent store an agent writes into, which is a different risk shape from reading a document once, and it deserves a probe through a real account before it is either catalogued or dismissed.

`NovAI Prices` (`#6624`) lists live prices for **111** Chinese AI models keylessly and read-only, held on the catalogued Chinese model price index `llm-prices-cn`. `Meridian Dispatch` (`#6632`) plans trips into an iPhone app with citable travel guides and OAuth on the plan tools, held on the trip planning class carried by TripleLedger and Maqami Travel. `AgentAlarm` (`#6634`) rings an iPhone through Silent mode and `Homing Pigeon` (`#6635`) sends a text from code, both held on the notification class carried by Mobile Text Alerts. `proton-mail-mcp` (`#6637`) works a Proton Mail Bridge with drafts, previews, a single-use token and undo, held on the saturated email class. `playwright-e2e-mcp` (`#6638`) is the relocated `trajectiq-ai/E2E` entry and developer test tooling.

`Herald` (`#6641`) is a local MCP router that serves scoped groups of servers to several clients, `mcp-jail` (`#6633`) is a policy proxy that runs a server inside a jail rather than being a server itself, and `UGT` (`#6640`) gets a GitHub project running in a private engine, all three developer infrastructure rather than operator surfaces. `Cutscene` (`#6630`) assembles motion-design launch films and `Magion` (`#6647`) generates fashion product photography, both on the saturated media generation class, and the term "saturated" is doing real work for Magion: the media entries already number in the dozens. `Crypto Pulse` (`#6642`) prices crypto calls through x402 and runs a prediction arena with USDC prizes, held on the crypto market data class. `socialwtf-mcp` (`#6643`) is an Ed25519 agent registry with challenge-response registration and direct messages, held on the agent identity class.

`gnomancer` (`#6627`) analyses a consumer DNA file locally, `Footalytics` (`#6631`) grades football predictions, `Go Bananas` (`#6645`) builds browser games, `Joinable` (`#6646`) adds multiplayer to a web game and `FitCard` (`#6649`, `#6650`) sizes a shirt against shirts you own. All five sit outside the operator scope. `FitCard` also shows the resubmission pattern: the identical body filed twice, twenty-five seconds apart, which is one arrival rather than two.

The two feed cards not covered above were probed rather than grouped. `Green Screen Memes` answered a keyless `initialize` **200** as `green-screen-memes` **1.0.0** with **7** tools over a library of about **2,000** chroma-key clips and ready-to-run ffmpeg commands, held on the media class and separately on its own terms page, which forbids identifiable people in clips used in paid ads, sponsored posts or endorsements. `Jaybird Digital` answered a keyless `initialize` **200** as `jaybird-website` **1.3.0** with **8** tools that start a website, write and save its files, list sites and search domains, with drafts expiring after seven days unless kept, held on the site builder class.

## Core Listing Verification

| Surface | Result |
| --- | --- |
| mcp.so four direct slugs | **404** on `/server/corpusiq`, `/server/corpusiq-io`, `/server/corpusiq-mcp` and `/server/io.corpusiq`, unchanged |
| Official MCP registry | `io.corpusiq/multi-source-mcp` active, several published versions, remote `https://mcp2.corpusiq.io/mcp` |
| mcpservers.org `/servers/corpusiq-io` | live, carried from the midday pass, where a direct fetch answered **403** to a plain client and the reader proxy answered the page |
| Glama | live as the connector `io.corpusiq/multi-source-mcp` on the `/mcp/connectors/` route, carried from the midday pass |
| Smithery | registry API live at `qualifiedName` `Cprusiq` with `displayName` CorpusIQ; the HTML server route **404s** because the web directory migrated to an Arcade-powered directory, a recorded migration rather than a delisting, carried from the midday pass |

## Counts

- mcp.so `recentServers`: **108** distinct cards, newest `2026-11-03T03:04:06Z`, three above the **14:39:24Z** midday stamp
- mcpservers.org `/all`: **18,887** on both reads, thirty slugs unchanged, zero churn
- Submission window: **#6624** to **#6650**, **27** submissions, **26** distinct
- Guide tree: **1,086** entries before this pass, **1,090** after
