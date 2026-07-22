---
title: "MCP Server Sweep — July 22, 2026 (Evening)"
description: "GitHub API sweep — 47 net-new MCP servers created July 22. 6 integration guides drafted for business-operator-relevant servers. Headline finds: Collibra Data Governance, Sanctions Screening (OFAC/EU/UK/UN), EU VAT VIES, SAP CAP/CDS (Capforge), SAP ECC (abapilot), General Liquidity."
category: mcp
tags: [mcp-servers, discovery, sweep, catalog, 2026, github]
last_updated: 2026-07-22
---

# MCP Server Sweep — July 22, 2026 (Evening)

Evening sweep via GitHub API. 341 total repositories created July 22 with "mcp server" in metadata — filtered to 47 net-new business-relevant servers not already in our catalog. 6 integration guides drafted for the highest-value operator servers.

**Source:** GitHub API (`created:>2026-07-21`)
**Previous sweep:** July 22, 2026 morning (8 servers from mcp.so)
**This sweep:** 47 net-new, 6 high-value guides created
**Total catalog:** 113+ servers now tracked

## Headline Finds (★ = operator relevance)

| Server | Category | Why It Matters |
|--------|----------|----------------|
| **Collibra MCP** ★★★ | Data Governance | Collibra Core REST API 2.0 — access enterprise data catalog assets, attributes, and relations. Pairs with Power BI MCP for semantic model lineage. First dedicated data governance MCP. |
| **Sanctions Screening MCP** ★★★ | Compliance | OFAC, EU, UK, UN sanctions screening as MCP tools. Hosted on MCPize. Essential for fintech AML/KYC workflows. |
| **EU VAT VIES MCP** ★★★ | Finance/Tax | EU VAT number validation with consultation number for legal audit proof. Part of the Honest MCP suite (Polish ecosystem). |
| **Capforge (SAP CAP/CDS)** ★★★ | Enterprise/SAP | SAP CAP/CDS + UI5 scaffolding with validation against `cds compile`. First SAP development MCP. |
| **abapilot-mcp (SAP ECC)** ★★★ | Enterprise/SAP | In-system ABAP for SAP ECC and on-premise S/4HANA. No BTP, no ADT, no RISE required. |
| **General Liquidity MCP** ★★★ | Fintech/Payments | Machine economy API: resolve, pay, verify, disclose as agent tools. |
| **Universal Commerce Protocol MCP** ★★ | Commerce | Google's Universal Commerce Protocol — AI assistants can shop/search products. |
| **Subcue MCP** ★★ | Pricing Intel | Live pricing & version data for AI agents. JSON-RPC 2.0, no auth required. |
| **Confluence MCP** ★★ | Productivity | Atlassian Confluence MCP server. |
| **OneNote MCP** ★★ | Productivity | Microsoft OneNote with device-code authentication. |

## Full Discovery — Business-Relevant (47 Servers)

### Enterprise / SAP (2)
| # | Server | Stars | Guide |
|---|--------|-------|-------|
| 1 | automatizatodo/capforge | 0★ | ✅ |
| 2 | NicoHern/abapilot-mcp | 0★ | ✅ |

### Finance / Compliance (5)
| # | Server | Stars | Guide |
|---|--------|-------|-------|
| 3 | apifymcpfactory-droid/sanctions-screening-mcp | 0★ | ✅ |
| 4 | bartosz-kuc/honest-vies-mcp | 0★ | ✅ |
| 5 | general-liquidity/general-liquidity-mcp | 0★ | ✅ |
| 6 | bartosz-kuc/nbp-mcp (Polish FX rates) | 0★ | ❌ |
| 7 | dwain-barnes/fuel-prices-mcp (UK) | 0★ | ❌ |

### Data Governance / Analytics (3)
| # | Server | Stars | Guide |
|---|--------|-------|-------|
| 8 | rajivdatta/mcp-collibra | 0★ | ✅ |
| 9 | api-evangelist/apstal (web analytics) | 0★ | ❌ |
| 10 | Subcue/subcue-mcp (pricing data) | 1★ | ❌ |

### Commerce / Business Data (4)
| # | Server | Stars | Guide |
|---|--------|-------|-------|
| 11 | aratan/ucp-mcp-server | 0★ | ❌ |
| 12 | bartosz-kuc/nip-krs-mcp (Polish company registry) | 0★ | ❌ |
| 13 | bartosz-kuc/stat-gov-mcp (Polish statistics) | 0★ | ❌ |
| 14 | nadeemsangrasi/Shovels-MCP-Server | 0★ | ❌ |

### Productivity / Communication (6)
| # | Server | Stars | Guide |
|---|--------|-------|-------|
| 15 | jsalamanc/mcp-confluence | 0★ | ❌ |
| 16 | seanGSISG/onenote-mcp | 0★ | ❌ |
| 17 | kevlasher/todoist-mcp | 0★ | ❌ |
| 18 | bartosz-kuc/honest-gmail-mcp | 0★ | ❌ |
| 19 | bartosz-kuc/honest-drive-mcp | 0★ | ❌ |
| 20 | bartosz-kuc/honest-calendar-mcp | 1★ | ❌ |

### Industry / Niche (8)
| # | Server | Stars | Guide |
|---|--------|-------|-------|
| 21 | JoostKiens/gfw-mcp-server (fishing) | 0★ | ❌ |
| 22 | alikup-ai/otgate (industrial OPC UA) | 0★ | ❌ |
| 23 | zaxarovcom/thisispaper-mcp (architecture) | 0★ | ❌ |
| 24 | mpasternak/dspace-mcp (academic repos) | 0★ | ❌ |
| 25 | bartosz-kuc/imgw-mcp (Polish weather) | 0★ | ❌ |
| 26 | bartosz-kuc/gios-air-mcp (Polish air quality) | 0★ | ❌ |
| 27 | bartosz-kuc/nfz-mcp (Polish healthcare) | 0★ | ❌ |
| 28 | bartosz-kuc/mbank-parser-mcp (Polish bank) | 0★ | ❌ |

### Developer / Infrastructure (19 additional)
Remaining 19 servers are developer-tool-focused: agent memory (senior-code-mcp, rag-mcp), MCP infrastructure (nextjs-mcp-kit, harness-mcp, mcp-upgrade), special-purpose (GPTImage, browser-agent, gemini-cortex-mcp, reuse-before-generate), and platform-specific (Planoda, Ax-Platform, libre-devops Azure). Not individually listed but tracked.

## Integration Guides Created (6)

1. **Collibra MCP** — Enterprise data governance. Collibra Core REST API 2.0 through MCP.
2. **Sanctions Screening MCP** — OFAC/EU/UK/UN compliance screening. Hosted on MCPize.
3. **EU VAT VIES MCP** — EU VAT number validation with legal audit trail.
4. **Capforge (SAP CAP/CDS)** — SAP development MCP with cds compile validation.
5. **abapilot-mcp (SAP ECC)** — In-system ABAP for SAP ECC/S4HANA.
6. **General Liquidity MCP** — Machine economy: resolve, pay, verify, disclose.

## Key Observations

1. **SAP ecosystem awakening** — Two SAP MCP servers in one day (Capforge + abapilot). SAP's 400K+ enterprise customers have been underserved by MCP. This is the first wave.
2. **Polish MCP ecosystem** — bartosz-kuc shipped 12 MCP servers today (part of "Honest MCP" suite). All local, offline-first. Interesting pattern: regional public data MCPs.
3. **Compliance MCPs emerging** — Sanctions screening + VAT validation signal MCP moving into regulated workflows. Audit trails and legal proof features are differentiating.
4. **MCPize hosting emerges** — Sanctions Screening MCP hosted on MCPize. Managed MCP hosting is becoming a distribution channel.
5. **Zero stars, high potential** — Most servers today are 0-star brand-new repos. Early-mover catalog advantage.
