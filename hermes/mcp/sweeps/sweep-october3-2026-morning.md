---
title: "MCP Server Discovery - October 3, 2026 (Morning)"
description: "Morning MCP sweep: 5 new business-relevant servers catalogued, from voice AI and predication markets to a multi-agent backlog."
last_updated: 2026-10-03
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october3-2026-morning"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 3, 2026 (Morning Sweep)

Morning sweep over the mcp.so `/servers` listing (29 slugs from the feed) and mcpservers.org `/all` (30 slugs), both fetched through the r.jina.ai reader proxy. Every candidate was cross-referenced against the catalog ledger and guide directories, then fetched through its detail page and, where keyless, probed with a live `tools/list` before cataloguing.

## New Servers Catalogued

### PredictionMarketsPicks MCP - Kalshi and Polymarket Data

Free, read-only Kalshi and Polymarket data for AI agents: NFL prop prices across venues, strike ladders and win probability, cross-venue price gaps, Fed and 2026 Senate odds, the Kalshi 15-minute and perpetual boards, plus EV, Kelly and Bayes calculators.

- Endpoint: `https://predictionmarketspicks.com/api/mcp/mcp` (remote Streamable HTTP, keyless)
- Surface: 34 tools verified through a live unauthenticated `tools/list` (`fed_rate_odds`, `senate_map`, `nfl_prop_board`, `find_arbitrage`, `calculate_ev`, `kelly_size`, `bayes_update`, and more)
- Model: read-only by design; focused servers split out for draft, weather and commodities

### Cartesia MCP - Voice AI for Agents

The official remote MCP server for Cartesia, the low-latency voice AI platform, giving any MCP-compatible agent access to text to speech, voice cloning and the audio layer behind voice agents and phone calls.

- Endpoint: `https://mcp.cartesia.ai/mcp` (remote Streamable HTTP, API key)
- Surface: Cartesia speech and voice tools (live list via the server endpoint)
- Provenance: first-party, published by Cartesia (the `cartesia-ai` GitHub org), verified and featured on the directory

### My Fordyce MCP - Shared Backlog for Agent Teams

A control plane over one shared backlog, built for the case where more than one AI agent works the same queue. Every work hand-out is a lease, concurrency is refused by design, and the attempt record survives so the next holder never re-runs blind.

- Endpoint: `https://myfordyce.fordycecg.com/mcp` (remote Streamable HTTP, OAuth or API key)
- Surface: `request_work`, `claim`, `heartbeat`, `add_evidence`, `release`; lifecycle `available → claimed → in_use → awaiting_review → done`
- Model: whole-ticket versioning (a write carries the version it read), lazy reclaim, presented identity via `agent_id`

### OpenAdLibrary MCP - Ad Library Data for Agents

Exposes a public ad corpus to any MCP client so an agent can pull live and historical ad creative for competitor and market research without a browser session.

- Endpoint: `https://mcp.openadlibrary.com/mcp` (remote Streamable HTTP, public-data key)
- Surface: ad search and retrieval over the public ad corpus
- Auth: key as `Authorization: Bearer` or `x-api-key` header, or OAuth; refused with an authentication error without one

### AgentTrust MCP - Trust Decisions for Agent Endpoints

Sits between finding an agent and calling it: an endpoint URL goes in, observed monitoring, reliability and ownership evidence is read, and a machine-readable trust decision comes out, without contacting the endpoint itself.

- Endpoint: `https://getagenttrust.com/api/mcp` (remote Streamable HTTP)
- Surface: `check_agent_trust` returns a `trustDecision` with health, reliability score, evidence freshness and ownership
- Rule: recommended when healthy and score ≥ 50, confidence banded high at ≥ 90 and medium at ≥ 50 when verified; explicitly not a community rating or security guarantee

## Held / Not Catalogued

The mcp.so feed was dominated by prior dispositions this cycle (Aayat AI, AgentGrid.io, allcams.fm, BulkTranscripts, Common Paper, Daski, Desearch, esimoa, FlatHunt, Genchi, Generate Greetings, GTM API, IBM ELM, Manifold, mcp-db-wizard, PixelDojo, Povver, prodready, SayLive, SocialAPIs, Sooveryn, Stele, TATUAT.RO, Treza, Uplika, Zyte). On mcpservers.org, the remaining slugs resolved to prior sweeps or dispositions (TidyTools, Talpy Aya, Fazy, Meniscus, clexo, Clayre Skills, IureOCR, IureTranscribe, Prompt God, Account Niche Finder, Skillfully, Jotter, Very Simple Notes, pmndrs docs, AgentTrust's own listing, memeswap, ssap self-learning-agent-setup).

## Notes

- mcp.so `/servers` fed 29 digestible slugs through the reader proxy; its `/feed` block carried no genuinely new entries this cycle.
- PredictionMarketsPicks was the highest-yield find: keyless, 34 tools, verified live with no auth.
- Cartesia is notable as an official first-party voice server, echoing the pattern of platform vendors publishing their own MCP surface.
