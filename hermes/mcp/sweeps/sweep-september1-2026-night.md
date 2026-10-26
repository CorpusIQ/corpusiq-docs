---
title: "MCP Server Discovery - September 1, 2026 (Night Sweep)"
description: "Night cron sweep over chatmcp/mcpso issues #3877-#3885 plus mcp.so and mcpservers.org homepages - 7 new business-relevant MCP servers catalogued with guides, 4 live-probed."
category: mcp
tags: [mcp-servers, daily-scan, night-sweep, september-2026]
last_updated: 2026-10-19
---

# MCP Server Discovery - September 1, 2026 (Night Sweep)

**Source:** chatmcp/mcpso GitHub issues #3877-#3885, mcp.so homepage recentServers, mcpservers.org homepage latest list, mcpservers.org /all JSON-LD page 1 cross-ref
**Method:** GitHub issues API + parse-homepages.py + extract-mcpservers-jsonld.py + live JSON-RPC probes (batch-probe.py) + registry checks
**Cutoff:** issues past #3876 (midday sweep cutoff); run at 19:01 MST Sep 1 / 02:01 UTC Sep 2

## Summary

- Issues evaluated: 6 fresh (#3877, #3879, #3881, #3883, #3884, #3885)
- Homepage candidates evaluated: 12 (mcp.so recentServers 4 fresh, mcpservers.org homepage 5 fresh slugs)
- Catalogued with guides: 7
- Skipped: 8 fresh + all /all page 1 repeats (prior dispositions)

## New Business-Relevant Servers Catalogued (7 guides)

| Server | Source | Verification | Category |
|--------|--------|--------------|----------|
| Zetesis | issue #3879 | 4 tools live-probed keyless at api.zetesis.science/mcp; registry v0.2.0 active | Research |
| Hesper Atlas Evidence | issue #3877 | 15 tools live-probed at hesperatlas.com/mcp; registry v1.6.0 active | Finance |
| Done Bear | issue #3883 | 35 tools live-probed at mcp.donebear.com/mcp; registry v1.0.0 active | Productivity |
| AdTest.AI | issue #3884 | npm adtest-mcp v1.1.0 published verified; stdio | Marketing |
| Layers Growth MCP | mcp.so recentServers | endpoint mcp.layers.com/mcp 401-verified live; repo layers/mcp MIT | Marketing |
| QuickBooks Connector by Meridian | mcpservers.org homepage | endpoint qbo-connector.meridian.pilot.com/mcp 401-verified live; Pilot.com | Finance |
| AI Crawler Index (Pathwren) | mcpservers.org homepage | 7 tools live-probed keyless at www.pathwren.workers.dev/mcp | SEO |

## Verification Notes

- Zetesis: initialize 200 no auth, serverInfo zetesis v1.28.1, tools evaluate_claim / zetesis_scope / zetesis_evidence / verify_attestation. Hard identifiers (PMID/DOI/NCT/grant) on every source, year-fenced retrieval.
- Hesper Atlas: initialize 200, 15 tools = 9 account-free evidence tools + 6 OAuth subscriber tools (signals:read scope). No raw market data, no trading.
- Done Bear: initialize 200, serverInfo donebear v0.7.0, 35 tools. Submission's GitHub link 404s (Nomos precedent: registry name + live endpoint beat repo availability).
- AdTest: single tool analyze_advert, 13 dimensions, async video flow, 1 credit per analysis, free account via app.adtest.ai.
- Layers: anonymous initialize returns 401 AUTH_REQUIRED (expected bearer-session gate); CLI setup writes .mcp.json + skill, session in OS credential store; every charge quoted, posting/spending/billing human-gated.
- Meridian QBO: GET /mcp returns 401 on anonymous probe (OAuth gate; /api/mcp 404s so /mcp is the endpoint). Free, multi-client, journal-entry writes. Pilot.com Inc.
- Pathwren: 7 tools captured; operator prefixes remirrored every 6 hours; 8 robots.txt stances; no vendor repo found.

## Skipped (not catalogued)

- Signadot (#3885) - ephemeral-environment Kubernetes sandboxes and traffic routing: dev infrastructure class.
- Aperture Wallet Knowledge (#3881) - official read-only product knowledge for a consumer crypto wallet: consumer product-docs class.
- Mantis Immersive Commerce (mcp.so recentServers) - showroom MCP whose core business tools are still mocked; the working surface is SDK codegen utilities: premature per the Krimskrams rule.
- Novu (mcp.so recentServers) - notification infrastructure: dev infra class.
- Backblaze B2 (mcp.so recentServers) - cloud storage operations: cloud infra class.
- ComputeSage StackBench (mcpservers.org homepage) - GPU/LLM benchmarks and hardware recommendations: dev infrastructure class.
- AmanChain x402 Marketplace (mcpservers.org homepage) - crypto agent-to-agent payment marketplace: x402 plumbing class.
- Sauna Guide Quotes (/all) - consumer home-sauna project briefs and quote requests: consumer niche class.
- mcpservers.org /all page 1 repeats and homepage slugs: all prior-sweep dispositions (CordFind, Vaanzari, Firefly III, Onchain Diary, SigVest, GridCarbon, urdigitalau family incl. WordPress/Clarity/Bing Webmaster/Cloudflare, Seedance, Wan 3.0, local-gpu-imagegen, LinkUpAPI, chat-recall, Perception, GridNews, mlab.sh, IMS Creators, DAST flight data, Symvanta, 3D-Agent, famous-name re-indexes; Atomic Mail, CarChat, file2markdown, BiGapi repeats).

## Trends

- Verification-first submissions continue: three of six fresh issues shipped citation-ready, read-only, no-auth or narrow-scope surfaces with published registry records (Zetesis, Hesper, Done Bear, Aperture) - the "evidence and provenance" pattern from Edgrapi/Trooth/VulX Watch is consolidating into a product class.
- Accounting and AEO both surfaced from directory homepages this sweep (Meridian QBO, AI Crawler Index), confirming homepage slug cross-refs still produce the catch-up yield the /all page no longer does.
- The human-in-the-loop growth server pattern (Layers: quoted charges, human-gated posting/spending) is the same governance shape ErzyCall brought to voice - approval-gated autonomous execution is becoming the standard architecture for commercial agent servers.

## Actions Taken

- 7 integration guides written to hermes/mcp/servers/external/<slug>/index.md
- index.md updated: top sweep section, last-updated line, docs-links tail block
- validate-guides.py: 7/7 PASS; See Also dir + label checks run; seomely label corrected to index label
- Committed and pushed to main with full-hash verification
