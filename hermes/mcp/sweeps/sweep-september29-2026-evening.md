---
title: "MCP Server Discovery - September 29, 2026 (Evening Sweep)"
description: "Evening sweep over the mcp.so /feed (29 server blocks, direct fetch) and mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy, with 9 detail pages fetched and 2 live endpoint probes. 7 new business-relevant servers catalogued with guides: OpenGATE MCP, Redacta MCP, PubCrawl MCP, Applyra MCP, Neleto CMS MCP, Yungle MCP and GAIP Agents MCP."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-29
---

# MCP Server Discovery - September 29, 2026 (Evening Sweep)

**Source:** mcp.so /feed (29 server blocks, direct fetch) + mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy + 8 mcpservers.org detail pages via the reader proxy + 1 mcp.so detail page via the reader proxy + 2 live endpoint probes (GAIP initialize, Yungle initialize)
**Method:** feed slug/name pairing with createdAt timestamps, /all slug extraction, two-round token-probe cross-reference against the 738-server catalog plus all disposal prose (sweep reports, .last-sweep files, index.md), targeted context greps for generic-token hits, detail-page enrichment for endpoint/auth/tools, keyless JSON-RPC probes where the listing offered no tool list, guide validation (8 frontmatter fields, em-dash scan, title length, FAQ question headings)
**Date:** September 29, 2026 10:20-11:10 MST (17:20-18:10 UTC)

## Summary

| Metric | Count |
|---|---|
| Feed blocks parsed | 29 server blocks (15 unique) |
| /all entries classified | 60 (pages 1-2 via r.jina.ai proxy) |
| Detail pages fetched | 9 via the reader proxy |
| Endpoint probes | 2 (GAIP HTTP 200 JSON-RPC, Yungle HTTP 401 OAuth wall) |
| Candidates cross-referenced | 37 names and slugs against the 738-server catalog plus disposal prose |
| New business-relevant servers | 7 |
| Integration guides written | 7 |
| Guide validation | 7/7 PASS |

## New Servers Catalogued (7)

**Compliance**
1. **OpenGATE MCP** - deterministic grounding verification for AI systems that must justify answers from source material. 7 scorer families (citation-detection, claim-extraction, verdict-accuracy, redaction, simplification, retrieval, grounding), no LLM judge, reproducible scorecards stamped with the git SHA, regression gate with --ci. Surfaces: MCP server (npx @pharmatools/opengate-mcp), GitHub Action, Python package (opengate-grounding), Docker image. Free, MIT, 2 GitHub stars, built by PharmaTools.AI. Proven in production across four PharmaTools products (halved passage hallucination 5.8% to 2.4%).

2. **Redacta MCP** - clinical pseudonymisation at the privacy boundary. Replaces patient identifiers (NHS numbers with Modulus-11 validation, NI numbers, DOB, postcodes, MRNs, US SSN and ZIP) with labelled tokens, keeps the reversal map out of agent context, HIPAA Safe Harbor mode, self-check pass, reinstate round trip. Local stdio (npx -y redacta-mcp) plus a self-hosted HTTP gateway with a plain-YAML Kubernetes deployment. Free, MIT-0, 9 GitHub stars, built by PharmaTools.AI. Also ships as an iOS app, agent skill, TS/Python libraries, CLI and FigJam plugin.

**Analytics & BI**
3. **PubCrawl MCP** - 14 tools over PubMed, Europe PMC (with preprints), FDA and UK drug labelling (openFDA/DailyMed and eMC) and ClinicalTrials.gov, every result citing its PMID, NCT ID or DOI. Unique compare_labels tool maps US Indications and Usage against UK SmPC section 4.1 side by side. No API keys (optional free NCBI key raises limits). Local stdio (npx -y @pharmatools/pubcrawl), free, MIT, 15 GitHub stars, built by PharmaTools.AI.

**Marketing**
4. **Applyra MCP** - 25 App Store Optimization tools across the App Store and Google Play: rank tracking, keyword difficulty and traffic, listing audits, metadata simulation, competitor visibility, autocomplete mining, niche clustering and top charts. Local stdio (npx -y @applyra/mcp-server) with an APPLYRA_API_KEY; requires the Applyra Unlimited plan. MIT, 0 GitHub stars, built by Applyra (applyra.io).

**Business Operations**
5. **Neleto CMS MCP** - every Neleto site ships a native MCP server at /api/mcp with 57 tools: pages, posts, events, components, layouts, files, settings, languages and meta tags, with template checks and live-page verification. OAuth 2.1 (Claude apps) or API token (coding agents); role-scoped access mirroring the admin. EU-hosted, registry name io.neleto/cms, built by Triple-A Software.

**Productivity**
6. **Yungle MCP** - private, resumable file delivery from AI assistants. Remote MCP at yungle.co/mcp (HTTP 401 invalid_token probe confirmed live OAuth wall), approval on every emailed send, download receipts, expiring links, webhooks with HMAC signatures. EU (Germany) hosting. CLI, TS and Python SDKs and a GitHub Action over the same OpenAPI 3.1 REST API. 1 GitHub star, built by Hein De Wilde.

**Compliance**
7. **GAIP Agents MCP** - read-only evidence about AI agents and MCP servers before and after delegated calls. Remote MCP at gaipagents.com/mcp, free and keyless; initialize probe returned HTTP 200 with a valid JSON-RPC session (server gaip-broker v1.6.1). Four core tools live-verified: gaip_check (working, reachable, valid, changed), gaip_watch (change watching with webhook alerts), gaip_diagnose (failure diagnosis with repair plan), gaip_verify (claims and citation accuracy). Product suites: Agent Observatory and Conformance, Supplier Reliability, Delivery Assurance, Evidence Ledger. No public repo.

## Identified, Not Catalogued

- **StudyDiff** - explains why two scientific papers disagree, with verbatim grounding and a measured blind benchmark. Bench science class.
- **Genomics MCP (rewire-bio)** - EGA, ENA, ENCODE, GEO and NCBI region reads with provenance for computational biologists. Research tool class.
- **Filesystem MCP (j0hanz)** - secure filesystem read/write/search/diff/patch server. Dev utility class (generic, saturated category).

## Non-Business Servers (Not Catalogued)

The GenPark single-author burst (8 entries: financial audit, voice VAD, OCR table, barge in, clause references, jitter buffer, voice latency, chart coordinates by alpha-park) excluded wholesale per the single-author burst precedent. Feed and /all repeats already disposed by the Sep 29 morning and midday sweeps and prior sweep ledgers: EQIQs and Uxia (catalogued Sep 28), PaperOffice AI (catalogued Sep 28), Collide MCP (Sep 9 disposition), Screen Browser, SnapDeploy MCP, Laso Finance, TinyFish, CUQU, Metabind demo, trip1, AQL PropertyCheck, plus the full morning and midday disposition sets (consumer, crypto, geo-niche, dev-utility and communication-saturation classes).

## Directory Listing Status Check

Carried forward from the Sep 29 midday sweep, not re-verified this cycle: glama.ai listed, mcpservers.org listed, smithery listed (Cprusiq), mcp.so not listed (moderation deletion state), PulseMCP listed.

## Verification Notes

- Both clones (Spark and Mac Mini) were at identical HEAD ea3291183 before this sweep; all work ran on the Spark clone with the Mac Mini resynced after push.
- web_extract was unavailable (Firecrawl unconfigured); all discovery used the proven curl plus regex fallbacks documented in the skill.
- GAIP tool names were recovered from a live keyless tools/list probe - zero invented tool names in the guide.
- Yungle endpoint verified via HTTP 401 invalid_token, confirming the OAuth wall documented on the listing.
