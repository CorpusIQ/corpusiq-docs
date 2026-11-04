---
title: "MCP Server Discovery - November 3, 2026 (Evening)"
description: "Evening sweep: a mandate gate driven four ways and a hosted ETL surface, with 27 submissions and 12 endpoints dispositioned."
last_updated: 2026-11-03
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november3-2026-evening"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 3, 2026 (Evening Sweep)

## Summary

Eleven hours after the midday pass, and the delta moved again. The mcp.so `/feed` carried ten cards above the midday stamp and nine of them were inside operator scope for the first time in three passes, the submission window carried **27** submissions between **#6680** at `17:37:35Z` and **#6706** at `03:22:45Z`, and the mcpservers.org `/all` newest page moved its counter by three entries across twenty-seven slugs, which is a page-1 composition change rather than a new cohort.

Two arrivals earned guides and they sit at opposite evidence tiers. **HANRIA Agent Mandate Check MCP** was driven end to end with no credential at all: a three-clause mandate validated to a digest, then four actions checked to `permit`, `escalate`, `deny` and `escalate`, each with a signed receipt. **Integrate.io MCP Server** answered a measured **401** with OAuth protected-resource metadata and is documented from the vendor's parameter-level reference, because its tools need an account.

The reading rule that matters this pass is the one about class precedents and their limits. Agent governance is already in the catalogue, so a new gate has to beat a specific neighbour rather than the category. HANRIA does, on the one axis the cabinet was missing, which is the operator-authored document itself.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included, one call | **27** submissions **#6680** to **#6706**, none read by the midday pass |
| mcp.so `/feed` | r.jina.ai reader, relative timestamps | **25** cards parsed, newest **54 minutes** old, ten above the midday stamp: Simple Inventory Management, NPILayer, APIXO, Integrate.io, Kurodyne, MyDesigns, Homesage.ai, assign2me, Machina, DeFi Quant |
| mcpservers.org `/all` | r.jina.ai, cache-busted | counter **19,148** against **19,145** at midday, **27** unique slugs on page one, seven of them unledgered vendor-domain slugs |
| Endpoint probes | keyless `initialize` plus `tools/list` | **12** endpoints: **6** answered **200** (hanria-check **0.7.4**, npilayer **1.0.0**, etfiq **0.4.0** re-check, plus priors) and **6** answered **401** (GoKuna with `scope="tasks"`, simpleinventorymanagement with `scope="inventory.access"`, assign2me, integrate.io, and two priors) |

## New Servers Catalogued

### HANRIA Agent Mandate Check MCP - Written Consent Gates

Relevance: HIGH. **Tier 1, driven** (`initialize` **200** as `hanria-check` **0.7.4**, `tools/list` returning **2** tools, both called, **5** mandate templates read as resources).

The operator writes a mandate: a `purpose`, a `default` for anything no clause covers, and an ordered clause list where each clause carries an `effect` of `permit`, `deny` or `escalate` and a `match` over the proposed operation. The agent passes that mandate plus the action to `check_action`. The first matching clause decides, and the answer names the clause that decided it.

Driven: a three-clause publisher mandate validated to `valid: true` with a `mandate_digest` of `2efbcf8d...` and the reason that the default for anything uncovered is `escalate`. Then four actions. A `network` `post` to a `https://api.github.com/repos/CorpusIQ/` prefix returned `permit` on `permit-docs-publish`. The same verb to an unrelated organisation returned `escalate` with no clause matched and the closest clause named and explained. A `transaction` `pay` returned `deny` on `deny-transactions`. An `administrative` `grant` returned `escalate` on `escalate-admin`. Every answer carried a `hanria-receipt-v1` receipt with the mandate digest, the action digest, an issue time, a fifteen-minute window and a signature.

`validate_mandate` is the other half and it is not a schema linter: it reports clauses that can never run because an earlier clause already decides them, unbounded prefixes, credential material inside a mandate, and expiry. Driving it proved the strictness. A first attempt used `kind` values of `payment` and `access` and a free-text `reason` on each clause; the server refused with `outcome: error` naming the offending field and the accepted taxonomy of `file`, `process`, `package`, `network`, `device`, `credential_use`, `transaction` and `administrative`, which the client is instructed to treat as a deny.

It earns a guide because the governance cabinet holds four different pieces and none of them is a mandate. [AgenticRail Gate MCP](/hermes/mcp/servers/external/agenticrail-gate-mcp/) enforces deterministic step order and verifies a hash-chained receipt chain, [AgentLedger MCP](/hermes/mcp/servers/external/agentledger-mcp/) caps and records spend, [agent-bom MCP](/hermes/mcp/servers/external/agent-bom-mcp/) maps an AI supply chain's blast radius, and [glc PromptGuard MCP](/hermes/mcp/servers/external/glc-promptguard-mcp/) scores prompts and tool outputs. The operator-authored authorisation document, with clause ordering and a third `escalate` outcome, is the piece that was missing.

Guide: [HANRIA Agent Mandate Check MCP](/hermes/mcp/servers/external/hanria-mandate-check-mcp/)

### Integrate.io MCP Server - ETL Pipelines by Description

Relevance: HIGH. **Tier 2, documented** (keyless `POST` to `https://api.xplenty.com/0/api/mcp` returned **HTTP 401** with `Bearer error="invalid_token"` and `resource_metadata` at `api.xplenty.com/0/.well-known/oauth-protected-resource`; no tool called, because the surface needs an account).

A hosted server on the account path `https://api.xplenty.com/YOUR_ACCOUNT_ID/api/mcp`, one JSON-RPC message per request, batch requests refused, OAuth 2.1 or a Personal Access Token. The vendor documents **46** tools across reading, authoring and jobs while the directory card says **44**, and tells clients to run `tools/list` against their own account for the exact set.

The jobs half is where an operator lives: `list_runs`, `get_run`, `get_run_summary` for records read per source and written per destination, and `explain_job_failure` for the primary error, the detected patterns and the log tail. The authoring half builds a package from a description, edits components and edges, manages variables, saves a draft and rolls back a version. The reading half inspects connections without credentials, previews data and transformations, profiles columns and re-answers from the live documentation through `ask_docs`.

The containment statements are unusually direct and they are the part a buyer should read first. Mutating tools take effect immediately and there is no sandbox. Mutation-base subclasses accept a `dry_run`. `create_schedule` creates a schedule disabled by default. `create_cluster` provisions billed infrastructure. Package edits are versioned and roll back, and every change lands in the account's audit history. `list_runs` defaults to root runs only, so child retries are excluded, and `validate_package` writes the workflow script to S3 even though it alters nothing. The token default is a **ten year** Personal Access Token, which is the one setting to shorten on an account that can start billed clusters.

It earns a guide because there is no ETL entry in **1,094** guides. The warehouse neighbours read data that something else has to move: [SaturnSQL MCP](/hermes/mcp/servers/external/saturnsql-mcp/), [Snowflake MCP](/hermes/mcp/servers/external/snowflake-mcp/) and [SQL Server MCP](/hermes/mcp/servers/external/sql-server-mcp/).

Guide: [Integrate.io MCP Server](/hermes/mcp/servers/external/integrate-io-mcp/)

## Read and Held

**Two holds taken on a class whose entry already exists, with the difference recorded.** Simple Inventory Management (mcp.so, 54 minutes before the read) answered a keyless `POST` with **HTTP 401** and `scope="inventory.access"` on `simpleinventorymanagement.com/mcp`, **31** tools per its detail page covering items, suppliers, reorder suggestions, purchase orders, custom fields and product photos. It is held on the inventory class carried by [Spark Inventory MCP](/hermes/mcp/servers/external/spark-inventory-mcp/), which reasons forward into a draft purchase order from a forecast, where this is a fuller record-keeping surface with no forecast in it. MyDesigns answered with a print-on-demand surface that publishes to Shopify, WooCommerce, TikTok Shop and Etsy, held on the class carried by [MarketPrint MCP](/hermes/mcp/servers/external/marketprint-print-on-demand/).

**Held on the vertical rule.** NPILayer is a keyless **200** as `npilayer` **1.0.0** with **3** read-only tools over the CMS NPPES provider file, `lookup_npi`, `search_providers` and `providers_near`, and it is honest about its own limits in the instructions, since an NPI does not indicate licensure, credentialing or current practice. It is held as a healthcare vertical beside the TMSClinics, SleepStudies and test-well holdings. Homesage.ai answers on `api.homesage.ai/mcp` over 160 million US properties and is held on the property class carried by [Fonciq MCP](/hermes/mcp/servers/external/fonciq-mcp/), [HeritageDeed MCP](/hermes/mcp/servers/external/heritagedeed-mcp/) and [RealtyPad MCP](/hermes/mcp/servers/external/realtypad-mcp/). OnlineTherapy.me prices services and therapist pay across 68 platforms and is the healthcare vertical again. GameGene, EPW.tools and Kurodyne are game design, energy-simulation weather files and a digital-product marketplace.

**Held with the probe that produced the ruling.** GoKuna answered **401** with `Bearer resource_metadata` and `scope="tasks"` plus `API_KEY_REQUIRED`, **10** tools that post a real-world task for an ID-checked person to execute with photo or video proof, and payment only for accepted work. It is the first complete version of a surface the October 21 night pass held as incomplete, so the hold carries a promotion test rather than a dismissal: drive `post_task` and `review_submission` with a task under a dollar, and if the proof and the acceptance step behave, the slice is empty and it should be catalogued. PlaceCall answered through the same vendor, a real outbound call to a US business with a transcript returned, held on the voice class. VOYGR Prospecting is 16 million US places with people enrichment and an attribute described in plain English, held on the lead-generation class carried by [Leadbay MCP](/hermes/mcp/servers/external/leadbay-mcp/), [Vibe Prospecting MCP](/hermes/mcp/servers/external/vibe-prospecting-mcp/) and [GoodLeads](/hermes/mcp/servers/external/goodleads-mcp/). FoxReach is **89** cold-email tools over campaigns, replies, sequences, warmup and lead verification, held on the outbound class carried by Warmerly and Sendsets. GSCPAP joins Search Console, Analytics 4, PageSpeed and live SERPs across **38** tools with an archive past Google's 16 month limit, held on the twenty-guide SEO class. MemCell is persistent agent memory, assign2me is task management, Machina is an x402 utility aggregator, anon.li is email aliases and encrypted drops, Documarium is a docs-site publisher with versioning, rtfx.pro publishes artifacts to a private link with view statistics, ElfHosted is hosting, ParalonCloud rents GPUs by the minute, and Handsy AI drives an iPhone through an ESP32 board.

**Already catalogued, re-confirmed rather than re-triaged.** ETFIQ submitted in this window, and a guide directory for it already exists from November 2 with the same endpoint `https://mcp.etfiq.com/mcp`. A live re-probe answered `initialize` **200** as `etfiq` **0.4.0** with the instructions line naming nightly recomputation from public filings, so the entry stands and nothing new was written.

**Outside operator scope, named so the next pass does not re-triage them.** TickerMint and Valo.IA are trading cards, TickerMint across 6 games and Valo across 14. Touchline Wire is Premier League and Fantasy Premier League analytics. Queenstown Tourism is regional travel. IMPOSSIBREW is a UK alcohol-free beer finder. SimoraGo is travel eSIM plans. Khavion reviews Terraform, CloudFormation and Kubernetes against cited cloud practices. LogoAPI returns company logos and favicons. Homing Pigeon texts the developer's own phone. AgentForge simulates EVM transactions and rug-checks tokens. EPW.tools produces EnergyPlus weather files. GameGene collects game-design precedents. The rest of the window is single-purpose calculators and developer utilities.

**On the mcpservers.org page one.** The counter moved **19,145** to **19,148** with **27** unique slugs, and seven had no prior disposition under either their slug or their spaced product name: `mapsdata-mcp`, `jasonarend`, `shisunxia`, `farzadnadiri`, `dima-xd`, `lightcube-labs` and `jeonghun917`. Six of the seven are vendor-domain or author-handle slugs from the developer submission wave the night pass grouped, and the seventh is a web-scraping vendor already visible in the page's sponsor rail. None carries an operator data surface, and the composition change rather than a new cohort is what the three-entry counter move describes.

## Core Listing Verification

| Surface | Result (measured this pass) |
| --- | --- |
| mcpservers.org | live, `/servers/corpusiq-io` served through the reader proxy with the CorpusIQ MCP Server title; the direct fetch is a Cloudflare 403, unchanged from prior passes |
| mcp.so | still not listed: `/server/corpusiq`, `/server/corpusiq-io`, `/server/corpusiq-mcp` and `/server/io.corpusiq` all **404** |
| Glama | live, `/mcp/connectors/io.corpusiq/multi-source-mcp` answered **200** |
| Official registry | active, `io.corpusiq/multi-source-mcp` **1.0.0** with the `mcp2.corpusiq.io/mcp` remote and a description still reading **30+** business systems against 40+ on the site |
| Smithery | not re-probed this pass; the registry API returned vendor-side **HTTP 500** at the midday pass and was last confirmed live on October 31 |

## Verification

Both guides pass the local per-guide validator: YAML frontmatter parses, all eight keys present, titles at **54** characters against a **60** cap, descriptions inside the **100** to **155** band, no em or en dashes, no redaction markers, an FAQ section with question headings, and every See Also target resolving to a real directory. The catalogue counts move from **1,094** guide directories to **1,096**.

**Counts.** Guide tree **1,094** directories before this pass and **1,096** after. Twelve endpoint probes, **6** answering **200** and **6** answering **401**. mcp.so **25** cards parsed with the newest **54** minutes old. mcpservers.org `/all` at **19,148** against **19,145**. Submission window **#6680** to **#6706**.
