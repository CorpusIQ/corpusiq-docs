---
title: "MCP Server Discovery - October 14, 2026 (Evening Sweep)"
description: "Evening sweep cataloguing a Mitsubishi PLC workbench, an agent-native Delaware C-corp formation rail, and free UK Corporation Tax calculators."
last_updated: 2026-10-14
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october14-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 14, 2026 (Evening Sweep)

Evening sweep about 13 hours after the October 14 midday sweep and about 12 hours after its 11:00 MST supplement. This cycle re-ran the 21:00 MST evening dispatch after the original execution was interrupted by a worker restart; a pre-run check confirmed zero side effects (no evening commits, stamps or activity-log entries) before the sweep re-executed. Surfaces: the mcp.so `/feed` (30 server links via the direct TanStack fetch), mcpservers.org `/all` pages 1-5 through the r.jina.ai reader proxy (150 slugs; the newest-30 page fully rotated by the evening ingestion wave while pages 2-5 moved by two to three slugs), the fresh chatmcp/mcpso issue window #5396-#5427 (32 numbers; 31 live, #5410 absent), and a fresh twelve-sitemap canonical refresh (r120: 15,619 server URLs; 143 additions and one re-key against the r119 capture), with vendor docs, evidence checks and class-precedent passes for every candidate. Three new business-relevant entries, each catalogued with a guide: a Mitsubishi PLC engineering workbench, an agent-native Delaware C-corp formation rail, and free UK Corporation Tax calculators.

## New Servers Catalogued

### GX Works Agent MCP - Mitsubishi PLC Engineering

A Windows MCP runtime and optional browser workbench for Mitsubishi PLC engineering: the agent reads a project's CPU and current program, retrieves CPU-scoped instruction facts and manual excerpts as evidence, builds Ladder, ST and FBD candidates, saves versioned artifacts (Ladder JSON, IR, SVG, ST derived from IR, GX import CSVs) and delivers the current Ladder version into GX Works2 with operator-configured execution consent. Two independent packages (MCP zip and Web zip); no Python required; interface MPL-2.0, runtime free for internal commercial use. This is the Mitsubishi counterpart to TiaLink (catalogued this afternoon for Siemens TIA Portal) and the second member of the industrial-PLC-authoring class.

Relevance: MEDIUM. **Repo and release verified** (github.com/Arienax/gxworks-agent, v0.1.0 released October 13 2026; no hosted endpoint to probe - the runtime is local by design).

### Corply MCP - Delaware C-Corp Formation from Chat

The formation and company-operations rail for agent-native incorporation: the founder works with their assistant through company intake, review, signing and payment, and the same MCP connection then manages equity, corporate actions and compliance on the live entity. Every Delaware filing is human-reviewed by Corply. Hosted Streamable HTTP with native OAuth sign-in; `whoami` verifies the connected account. Slots beside Pitch Protocol (funding rail) and Corpus Law (legal search) in the catalog.

Relevance: HIGH. **Endpoint live** (initialize returns `AUTH_REQUIRED` for the native OAuth flow; the agent-readable guide at corply.dev/skills.md verified).

### Taxley MCP - Free UK Corporation Tax Calculations

Seventeen free UK Corporation Tax tools modeled on the rules published on GOV.UK: CT estimates (small profits rate, main rate, marginal relief, associated companies, short periods, periods straddling 1 April), payment and filing deadlines, late-filing penalties and interest, director's loan s455 tax, capital allowances, chargeable gains with indexation, micro-entity and small company size checks, long-period splits, company car and van benefits, mileage, homeworking, trivial benefits, dividend reserves, salary vs dividends, sole trader vs limited, and pension contributions. Keyless and free; every answer links back to the worked result on taxley.co.uk.

Relevance: HIGH. **Endpoint verified** (keyless initialize 200 as `taxley` v1.0.0; `tools/list` returns all 17 tools).

## Sources

- mcp.so /feed (30 server links, direct TanStack fetch; three cards fresh past the midday-supplement capture: litshrine, Ranla and CardsNearby)
- mcpservers.org /all pages 1-5 via the r.jina.ai reader proxy (150 slugs; page 1 fully churned against the midday-supplement capture on the evening ingestion wave; pages 2-5 stable with two to three movers each; a second page-1 fetch confirmed the rotation is stable, not a render artifact)
- chatmcp/mcpso issues #5396-#5427 (32 numbers; 31 live, #5410 absent; submission bodies carried endpoints and auth modes in one authed call)
- Fresh twelve-sitemap canonical refresh (r120: 15,619 server URLs after locale-prefix stripping; 143 additions and one re-key against the r119 capture - the evening ingestion wave; the additions resolved to prior dispositions, class holds and the three catalogued entries)
- Vendor docs and evidence checks for every candidate (Taxley keyless initialize 200 with all 17 tools; Corply initialize `AUTH_REQUIRED` for its native OAuth flow plus the skills.md agent guide; LiveCRM 401 invalid_token; GX Works Agent verified via the public repo, release artifacts and README - the runtime is local by design)

## Also Identified (Not Catalogued)

**mcp.so feed (three fresh cards):** litshrine (a ritual novelty - "a quiet place for agents to make wishes, light a daily lamp, and receive a reviewed oracle"; Verified and Featured on mcp.so with a remote endpoint, but a novelty surface, not business data) and CardsNearby (find local US card shops and card shows - sports, Pokemon, Magic, TCG; consumer hobby class), both held on the consumer and novelty rule; Ranla (an AI growth agent for software businesses - pages that rank, AI-answer mentions, Reddit replies and lifecycle email; a single-vendor growth platform whose SEO, social and email slices sit inside the saturated marketing and email-infrastructure classes per OperStack, tinysend and SendPulse) held. The three cards that rolled off the feed (pixel-art-generator-sprite-fusion, everbary-certified-translations, ship) all carry prior dispositions.

**mcpservers.org /all pages 1-5 plus the 143 canonical additions (the evening ingestion wave):** evaluated and held, with the named anchors. LiveCRM (typed, audited Salesforce and HubSpot cleanup with reversible writes; the sales-CRM operations class per the Kasar, TeamShift and Boardroom holds - the strongest hold of the cycle), RiskModels (US equity factor risk, return attribution and ETF hedge ratios; the finance-data saturation per the catalogued PairBook plus the stock-research rule), CiteLadder (AI search visibility records; saturated per geolint, LogNorm and the Cite42 disposition), Zenning (AI-employee platform connector), JobSpidey (job search, resumes and application tracking; the career-workflow utility rule - jobs DATA catalogues, career-workflow utilities hold), ValuationMCP (wealth-management valuations; the wealth-operations class per Milemarker and X1 Wealth with the valuation math surface covered by Valuation API MCP), SemanticHub (news-source monitoring and article clustering), Tasks by thetasks.app (task-workspace class per Notion and Monday), Mailcycle (an inbox per agent, sealed on arrival; agent-email saturation per Voidmail) and SadaSend (scoped email sending with allowlists and provenance; email infrastructure per tinysend and SendPulse), ScreenVerb (screenshot library search; utility class per CurlShot), SendFromChat and Waply (WhatsApp automation density per Gambot and Neuron), Tessio (age-verification statistics; compliance and KYC density per bynn), OpenBtoB (shipment records, HS codes and buyer screening; customs per Customs MCP and EximAgent with the sanctions slice covered), Deadlatch (a pre-trade latch for trading agents; the pre-action guard class per Sentinel Shield and fineprint), 402xAgent x402-spotcheck (x402 payment-guard infrastructure class), ScreensDesign (mobile app design research; the design-tooling holds), Notestack (a write-to-podcast notebook; the NotebookLM prior disposition), Fenestra (architectural rendering; the architecture vertical per the AEC holds plus media generation), Agent Data Co (daily AI-ecosystem data; meta-directory classes per Agora and Agent Discovery Board) and AgentAtlas (coding-agent setup directory; same meta class), the saifs-ai five-server family (lead scoring, customer tiering, marketing, inventory and synthetic data; the family carries its thin-docs Marketing disposition), the CloudCorpRecords four-tool fleet (greenlight, claimcheck, gatefile, prwatch - open-source contributor workflow utilities), Agent Letter Desk (physical letters; opening soon and invite-only), AgentRXI (x402 LLM access and wallet checks; x402 infrastructure plus agent-verification density), PRRO Cloud (Ukrainian fiscal cash registers; regional fintech), Vythos and Khive (workspace platform connectors; thin at capture), Chatley (AI voice-agent platform; call-agent density per DialNexa and KaiCalls), Ecco Board (agent task board; the CLAIM and AgentBoard holds), Elfsight AI Chatbot (chatbot platform class), InsightSocial (25-platform social data; the social-data density per fastsocial and EnvoAPI), Udora and PlayableGift (gifting consumer), GrazieChef (restaurant menu and cost utilities), Outcometick (Polymarket tick-data strategy SDK; crypto and quant classes), EasySociable (social carousel production; the social-creative class), Memocore (shared agent memory; the memory density per knowsme and Memwyre), Bumiatlas (Indonesian land parcel lookup; regional property), Spicrawl (web scraping to Markdown; the scraping-infrastructure class per Plainport), Zeptap (mirror a real iPhone for agents; device-automation class per FlashDesk and Ghost), SubmitCheck (directory data over x402; meta and x402 classes), Flexreport (equity live events; finance saturation), and the group-ledger residuals recorded by the night sweep and the midday supplement (SQLX, the LVL skill market, the LOTS suite, HONO, Yui agent rooms, Oh My Phone Use, Timexxs, Sheets MCP, and the mambabuilt job-change trio).

**chatmcp/mcpso issue window #5396-#5427 (32 numbers; 31 live):** held in full. Zinc (the official Amazon, Walmart and Target shopping rail; agent-commerce class per the Is Agentic and Stockpile Market holds), RealtyCrawl (real-estate observations; property-data density per the Placestack hold), Public Data MCP twice over (recalls, government contracts, ZIP income and leads; Apify-actor distribution class per Metqo with the public-record slices covered), JustClip and FastClip (video clipping; the Reelhouse clip-repurposing hold), SuperLocalMemory and skillmem (agent memory density), BountyRadar (prior disposition), the MistifyTea trio (Cheapest-LLM Router, Free and Cheap Tokens, BountyRadar; model-routing and token-catalogue tooling plus one DEBUG test issue), Vitkilabs Anvil, hexvero, RealRun, Kaleto, Heard, SaltCrate Oracle, NexaLayer, Convertlyft, LaTeX-Agent, TANDIU AI Infrastructure Data, japan-price-alert, korea-mcp, magento.watch, Preventionlabs, Affitor and the Agent Output Verifier (dev, ops, regional and consumer singles), plus #5418 (a pricing question about mcp.so's submission paths; not a server).

**Consumer and regional remainder (held):** Agent Maddegen art hub, Bandmixr, Best Asia Hotels, Callejear, Desert Road Catholic, Atlas of Plantbased, Sickle, TastePix, Yacht Specs, HutchDB, Cartographer, Portsmith, MakeVideo, PM Wallets, Web3Juice, App Factory and similar dev, crypto and consumer singles from the wave.

## Core Listing Verification

- mcpservers.org: LISTED (detail proxy 200; title exact this cycle)
- glama: LISTED (canonical server page 200)
- smithery: LISTED (registry query returns `Cprusiq` as the first result)
- mcp.so: NOT LISTED (four-slug direct probe all 404; quarantine holds, no resubmit)

No changes to the CorpusIQ listing state this cycle.

## Result

Catalog moved from 925 servers (+811 guides) to 928 servers (+814 guides).
