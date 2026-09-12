---
title: "MCP Server Discovery - September 11, 2026 (Evening Sweep)"
description: "Evening sweep over the mcp.so feed, mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy and chatmcp/mcpso issues #4072-#4079. 9 new business-relevant servers catalogued with guides, 7 endpoints live-probed over JSON-RPC."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-11
---

# MCP Server Discovery - September 11, 2026 (Evening Sweep)

**Source:** mcp.so feed (30 server blocks, curl + regex), mcpservers.org /all pages 1-2 (r.jina.ai reader proxy, 43 slugs batch-classified), chatmcp/mcpso issues #4072-#4079 (the fresh window past the midday cutoff at #4070)
**Method:** GitHub issues API, /all slug extraction via reader proxy, JSON-RPC initialize + tools/list probes
**Date:** September 11, 2026 ~19:00 MST (Sep 12 02:00 UTC)

## Summary

| Metric | Count |
|---|---|
| New GitHub issues evaluated | 8 (#4072-#4079) |
| mcpservers.org /all slugs batch-classified | 43 (page 1 renders 13 via the proxy; page 2 full 30) |
| New servers catalogued | 9 |
| Integration guides written | 9 |
| Skipped (not catalogued) | 40+ names across prior dispositions, niche classes and shells |

## New Business-Relevant Servers (9 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| GoodLeads MCP | goodleads-mcp | Formation-grade lead intelligence - state-filing leads priced per record, human-completed Stripe checkout | Live-probed: keyless tools/list returned all 13 tools with full schemas |
| Recordwire MCP | recordwire-mcp | US business-registry data and change events across 7 states | Live-probed: keyless tools/list returned all 8 tools; calls require the rk_live_ bearer key |
| MentionAgent MCP | mentionagent-mcp | Publisher outreach and backlink placements from the agent | Live-probed: 401 invalid_token on anonymous initialize, bearer auth as documented |
| iHatePosting MCP | ihateposting-mcp | Official social scheduler MCP, validate-before-create, 14 platforms | Live-probed: initialize returned serverInfo v0.3.0; stateless tools/list returned all 6 tools |
| LocationLists MCP | locationlists-mcp | 725 US business-location datasets, search to Stripe checkout | Live-probed: keyless tools/list returned tools with schemas; catalog.json confirms 14.2M locations |
| ClauseAI MCP | clauseai-mcp | Keyless startup legal documents - 12 CC0 templates | Live-verified: session-gated JSON-RPC endpoint; template API returned all 12 live |
| VerifyAPI MCP | verifyapi-mcp | Fact-checking with Ed25519-signed JWS receipts | npm @verify-api/mcp v0.1.9 metadata + GitHub README contract verified |
| Unicorn Screener MCP | unicorn-screener-mcp | Startup scores out of 100 and public research memos | Live-probed: keyless tools/list returned all 5 tools |
| Mobile Text Alerts MCP | mobile-text-alerts-mcp | Official SMS - send/schedule, subscribers, groups, carrier registration | Live-probed: 401 Unauthorized on anonymous initialize, auth-gated as documented |

## Findings

- **GoodLeads MCP**: hosted at mcp.goodleads.club/mcp (Streamable HTTP, no auth, stateless). 13 tools: interpret_list, list_starters, browse_leads, list_filterable_fields, explain_concept, quote_list, list_live_states, list_products, find_lead_by_glid, data_quality_scorecard, describe_surface, checkout_list, create_checkout. $0.25 per record (name + mailing address), $0.50 (plus verified phone or email), $0.70 (both); no minimums. Only the two checkout tools write, and neither touches money - payment is human-completed on Stripe's hosted page. Listed in the Anthropic Connectors Directory.
- **Recordwire MCP**: hosted at api.recordwirehq.com/mcp (Streamable HTTP, bearer rk_live_ key shared with REST). 8 tools: search_businesses, get_business, get_business_events, search_events, list_sources, create_subscription, list_subscriptions, delete_subscription. Coverage: Florida, New York, Colorado, Pennsylvania, Virginia, Connecticut, Oregon; per-state key restrictions return 403 outside the subscription. Plans from $200/month.
- **MentionAgent MCP**: hosted at mentionagent.ai/mcp (Streamable HTTP, bearer header - OAuth explicitly not supported yet). 10 tools: get_status, list_inbox, get_thread, draft_reply, send_reply, mark_deal, list_pending_drafts, edit_draft, approve_batch, set_sending. send_reply has no recipient field - emails only ever go back to the thread's existing person. draft_reply crawls the publisher's site and picks the page and paragraph to ask for.
- **iHatePosting MCP**: hosted at ihateposting.com/mcp (Streamable HTTP, API key, stateless - no session header). 6 tools: whoami, get_platform_rules, validate_post, create_post, list_posts, list_accounts. validate_post runs the same checks the publisher runs seconds before posting. 90 days free, no credit card required.
- **LocationLists MCP**: hosted at locationlists.com/mcp (Streamable HTTP, keyless). 5 tools: search_datasets, get_dataset, get_sample, get_quote, create_checkout. 725 datasets + 1 bundle, 14,248,853 US business locations, one-time $9-$199 per dataset. Registry io.github.kylehawke-stack/locationlists. Read-only ChatGPT profile at /mcp/chatgpt.
- **ClauseAI MCP**: hosted at clauseai.exe.xyz/mcp (Streamable HTTP, no account). 12 templates from General Legal (CC0): mutual-nda, one-way-nda, master-services-agreement, dpa-global, dpa-us, privacy-policy-gdpr, privacy-policy-us, terms-of-use, cookie-notice, employee-offer-letter, advisor-agreement, business-associate-agreement. PDF, ODT or Markdown download. Agent skill via npx skills add wasauce/clauseai.
- **VerifyAPI MCP**: npm @verify-api/mcp v0.1.9 (stdio). One tool: verify_claim with verdicts supported/contradicted/unverifiable, source URL, exact quote, confidence, and an Ed25519 JWS receipt (JWKS at api.verify-api.dev/.well-known/jwks.json). Free trial 3 calls/IP/24h keyless; $0.02 per verified claim, fresh-fetch $0.05; unverifiable calls free.
- **Unicorn Screener MCP**: hosted at unicornscreener.vc/api/mcp (Streamable HTTP, keyless). 5 tools: search_startups, lookup_startup, request_startup_memo, get_screening_status, read_startup_memo. Free lookups on existing results; new screenings consume a free allowance. OpenAPI at /openapi.json, llms.txt published.
- **Mobile Text Alerts MCP**: hosted at mcp.mobile-text-alerts.com/mcp (Streamable HTTP, bearer). Official vendor submission (verified + featured badges). Capabilities from the listing: send and schedule SMS, manage subscribers and groups, complete carrier registration. Tool list account-gated; vendor main site has no public /mcp docs page (404).

## Skipped (Not Catalogued)

PipesHub #4078 (permission-aware enterprise RAG - remote per-instance MCP, tool names unpublished, npm README is a client-connection guide only), MCP Selection Lab #4072 (metadata-only MCP tool-selection benchmarks from AgentTrustLab - benchmark infra class), England Works Watch #4073 / CQC Provider #4074 / UK Taxi PHV #4075 (ChanghuLiu UK regulatory decision-layer family - UK Premises Licence already disposed Sep 6; UK geo-niche family), SimFuse eSIM Storefront (travel consumer), SomaCheck Vibecheck (consumer novelty), prior-sweep dispositions respected (UmmahAPI, Midpoint Card Prices, Tribeunal, TruVerifAI, Theyond, Reach, Airside Labs, OpenZiti pair, Nova Data, Canarics, Orthogonal, VenuNite, toll402, Loadster, priostack, pulse-verity, Prove AI, Resell Pro HOLD, TERM, DeliverKit), HasData per-connector listings (HasData 57-API family guide covers them), ilyautov Russian marketplace family (marketplaces-mcp-ru + WB/Ozon guides cover them), Playgama, snapInsta, Briefing Service, Open Task Relay, redfox pair, LEGAION Verifier, bussin-mcp, Qotien, ProofCore Notary, Windframe, Keeper.sh, Vectorize, TheQRCode.io, offgen.ai, Agent Control Agent Meter, Nimo, pdf2md, Open Economics, Browser Forest, Heliograph, knowledgeforagents.com, Shipi18n, infinitebacklog, AgentTrustLab, Zambo, orbylon readiness, kolourr/midpoint-mcp, plus nav-only and author shells (jinmojing, felipegambettadesouza6-jpg, abdullahhasan42, dbhq-uk, zambodotdev).

## Directory Status (core maintenance)

- **mcpservers.org:** LISTED - reader proxy 200 on /all; direct curl 403 CF wall unchanged.
- **glama.ai:** not re-checked this cycle (no change signals).
- **mcp.so:** CorpusIQ remains NOT LISTED (moderation quarantine, no resubmit).
- **PulseMCP / smithery.ai:** no change signals this cycle.
