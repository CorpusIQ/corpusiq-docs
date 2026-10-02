---
title: LandLens One MCP - Tamil Nadu Property Due Diligence
description: "Remote MCP server from Verified.RealEstate for Indian property due diligence. Agents query Tamil Nadu land records with cited legal answers, run automated verification checks (encumbrance certificates, ownership, zone restrictions), read 25 years of registered transaction prices, calculate development potential, track property changes and manage deal documents. Live API-key/OAuth endpoint at verified.realestate/mcp."
category: Real Estate Data
stars: n/a (new listing)
added: 2026-09-12
source: mcp.so feed (landlens-one)
relevance: ★★
tags: [real-estate, property-due-diligence, land-records, india, legal-verification, remote-mcp]
---

# LandLens One MCP

**Remote MCP server (Streamable HTTP, API key or OAuth token)** - property due diligence for Tamil Nadu from Verified.RealEstate, the Chennai real-estate platform. LandLens One is the agent interface to the vendor's 35+ verification tools: questions about land answered from the law and cited to source records, 30-check verification reports, 25 years of registered transaction prices, build-scope calculations and property-change tracking. Operators use it to verify before buying instead of trusting a seller's paperwork.

```
Server type: Remote (Streamable HTTP)
Auth: LandLens API key or OAuth token (bearer credential)
Endpoint: https://verified.realestate/mcp
Tools: Not published; account-gated surface (see capabilities below)
Coverage: Tamil Nadu, India (vendor HQ Chennai; RERA TN/Agent/0181/2024)
Pricing: Verify My Land bundles (2 / 25 / 250 checks); sign up at verified.realestate
Category: Real Estate Data
Built by: Verified.RealEstate
```

## Tools & Capabilities

The live tool list is account-gated; this surface is prose-derived from the vendor's LandLens product pages and mcp.so listing.

| Capability | Purpose |
|---|---|
| Ask Veritas (LandLens One) | Questions about Tamil Nadu land answered from the law, cited to the page, with actions taken on the records |
| Verify My Land | 30 automated legal checks in one report: encumbrance certificate fetch, ownership verification, zone restrictions |
| PriceMap | 25 years of registered property prices - actual transaction values, not just guideline rates |
| Build Scope | Development potential calculator: FSI, setbacks, height limits, parking |
| Property Tracker | Monitoring with alerts on new registrations, EC updates and ownership changes |
| Deal Room | Secure transaction workspace: document sharing, e-signatures, milestone tracking from offer to registration |

The underlying 35+ tool suite includes EC lookup, certified copies, Patta applications, CRZ zone checks, legal opinions, land surveys and completion/occupancy certificates - the records the agent answers against.

## Connection

1. Create an account on verified.realestate and request a LandLens API key (or use the OAuth flow).
2. Point an MCP client at `https://verified.realestate/mcp`.
3. Attach the key as the bearer credential. Unauthenticated calls return a JSON-RPC -32001 error ("A valid LandLens API key or OAuth token is required"), so the credential must be present from the start.

## Verification (Sep 12, 2026 morning sweep)

Endpoint live-probed over JSON-RPC initialize: HTTP 401 with an OAuth bearer challenge (realm LandLens) and protected-resource metadata at verified.realestate/.well-known/oauth-protected-resource - definitive evidence of a live auth-gated endpoint (the AdPlug pattern). The mcp.so listing tagline names the same endpoint. Tool names are not published; the capability surface above is prose-derived from the vendor's LandLens product pages.

## See Also

- [Austin MLS MCP - Live Austin Real Estate Listings for AI Assistants](/hermes/mcp/servers/external/austin-mls-mcp)
- [AskRentAI MCP - Property Portfolio Intelligence for Rent Manager Operators](/hermes/mcp/servers/external/askrentai-mcp)
- [DealMachine MCP - Real Estate Prospecting for Agents](/hermes/mcp/servers/external/dealmachine-mcp)
- [Hermes Changelog](/hermes/changelog)  --  Latest agent releases and features
- [Skills Marketplace](/hermes/skills/marketplace)  --  946+ community skills
