---
title: "MCP Server Sweep — July 20, 2026"
description: "8 new business-operator-relevant MCP servers discovered from awesome-mcp-servers (punkpeye/awesome-mcp-servers) since last sweep on July 19. Headline finds: mcp-sam-gov (150-tool government contracting), openInvest (63⭐ multi-agent investment engine), Orbiads GAM (200+ tool Google Ad Manager), camt053/pacs008 (ISO 20022 banking suite)."
category: mcp
tags: [mcp-servers, discovery, sweep, catalog, 2026]
last_updated: 2026-07-20
---

# MCP Server Sweep — July 20, 2026

Discovered 8 new business-operator-relevant MCP servers from recent PRs merged into the [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) list on July 19-20, 2026.

**Source:** punkpeye/awesome-mcp-servers (recent merged PRs)
**Previous sweep:** July 19, 2026 (20 servers)
**This sweep:** 8 operator-relevant servers (+ more niche/consumer servers identified but not cataloged)

## Headline Finds

| Server | Category | Why It Matters |
|--------|----------|----------------|
| **mcp-sam-gov** ★★★ | Government/Procurement | 150 tools for US federal + state/local government contracting, spending, regulation & partner vetting — SAM.gov, USAspending, Grants.gov, OFAC, FDIC, EPA + 45 more. Keyless. **First government contracting MCP server.** |
| **openInvest** ★★★ | Finance | Research-grade investment decision engine — isolated multi-agent committee, auditable verdicts, backtests with lookahead protection. 63⭐. Python. |
| **Orbiads GAM MCP** ★★ | Marketing/AdTech | Google Ad Manager hosted MCP — 200+ tools across campaign management, line items, creatives, reporting, and ad-ops compliance audits. |
| **camt053-mcp** ★★ | Finance/Banking | ISO 20022 camt.053 bank-to-customer statement parsing & reconciliation — 19 tools, CBPR+/HVPS+ readiness, SLSA-L3 provenance. Part of the ISO 20022 MCP Suite. |
| **pacs008-mcp** ★★ | Finance/Banking | ISO 20022 pacs.008 credit transfer generation, validation, parsing & audit — 10 tools, scheme-aware (CBPR+/HVPS+/Fedwire/CHAPS/T2/SCT-Inst). |
| **skillselion-mcp** ★ | Aggregators | Search Skillselion's curated directory of Claude Code skills, MCP servers & plugin marketplaces, ranked by installs and GitHub stars. |
| **ai-footprints-mcp** ★ | Knowledge & Memory | Agent-first bookmark & knowledge manager — let AI agents manage your digital footprints (Chinese: AI 足迹). |
| **bug-bounty-intelligence-mcp** ★ | Security | AI-powered smart contract security analysis trained on 27,681 real Sherlock/Code4rena findings. USDC/scan via x402 on Base. |

## Full Discovery List

| # | Server | Category | Repo | Stars |
|---|--------|----------|------|-------|
| 1 | mcp-sam-gov | Government/Procurement | cliwant/mcp-sam-gov | 4 |
| 2 | openInvest | Finance & Fintech | longsizhuo/openInvest | 63 |
| 3 | Orbiads GAM MCP | Marketing/AdTech | OrbiAds/Orbiads-GAM-MCP | 3 |
| 4 | camt053-mcp | Finance & Fintech | sebastienrousseau/camt053-mcp | 1 |
| 5 | pacs008-mcp | Finance & Fintech | sebastienrousseau/pacs008-mcp | 0 |
| 6 | skillselion-mcp | Aggregators | skillselion/skillselion-mcp | 0 |
| 7 | ai-footprints-mcp | Knowledge & Memory | Piccolo123/ai-footprints-mcp | 0 |
| 8 | bug-bounty-intelligence-mcp | Security | holistis/bug-bounty-intelligence-mcp | 0 |

## Additional Servers Identified (Not Cataloged)

These were found in the PR queue but are consumer/niche — included here for completeness but no integration guides drafted:

- **tgboard** — Telegram directory MCP
- **llm-video-mcp** — Token-budgeted video understanding for coding agents
- **Nippy** — Cloud platform (nippy.host)
- **ariadne** — Affected-test selection for Kotlin/Android
- **knowmind** — AI agent memory & knowledge graph (repo not found)
- **financialdatapi/mcp** — Finance & Fintech (repo not found)
- **Routara** — LLM Gateway MCP server
- **gotcosy/mcp** — Travel & Transportation
- **slnmap** — Developer Tools (EMahmoudNabil/slnmap)
- **LseKit-SequentialThinking** — Structured thinking MCP with 26 tools + dual MoA reasoning
- **ValueScope** — DCF valuation engine (A-shares/HK/US/JP stocks)
- **Obsidian Everywhere** — Obsidian integration
- **PPN Hub** — Aggregators
- **Ace-Context-MCP** — Knowledge & Memory
- **DeepPane** — MCP server
- **VectorFree** — MCP server
- **memory-arbiter-mcp** — Knowledge & Memory
- **Lumify** — Sports intelligence
- **Posthive** — Social Media
- **Logospell** — Misc
- **Immersive Commons** — Aggregators (Floor 10 SF)
- **Swath API** — Radar-verified storm detection & property intel

## Integration Guides Created

Detailed setup guides drafted for all 8 headline servers. Each covers:
- What the server does for operators
- Installation (npm/uvx/pip)
- Claude Desktop / Hermes config
- Key tools and their use cases
- Authentication requirements

## CorpusIQ Angle

Several of these servers are directly relevant to CorpusIQ's operator audience:

- **mcp-sam-gov** — Government contracting is a massive operator workflow. 150 tools covering federal + state procurement. Complementary to CorpusIQ's business data connectors. If an operator runs a government contracting business, this is essential.
- **openInvest** — Multi-agent investment committee with auditable verdicts. 63⭐ signals real adoption. Potential partnership for financial operators using CorpusIQ.
- **Orbiads GAM** — Google Ad Manager MCP fills a gap in the marketing/adtech MCP ecosystem. Operators running ad operations can now manage GAM from AI agents.
- **camt053/pacs008** — ISO 20022 is the global standard for financial messaging. These MCP servers let operators parse bank statements and generate credit transfers from AI agents — directly relevant to CorpusIQ's finance vertical.

## See Also

- [[servers/external/sam-gov-mcp]]
- [[servers/external/openinvest-mcp]]
- [[servers/external/orbiads-gam-mcp]]
- [[servers/external/camt053-mcp]]
- [[servers/external/pacs008-mcp]]
- [[servers/external/skillselion-mcp]]
- [[sweeps/sweep-july19-2026]]
- [[index]]
