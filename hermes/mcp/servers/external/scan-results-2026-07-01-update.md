---
title: "MCP Server Scan Results — 2026-07-01 (PM Update)"
description: "Afternoon update to the July 1 MCP server discovery scan. 2 new business-relevant servers found after the morning scan."
---

# MCP Server Directory Scan — July 1, 2026 (PM Update)

## SOURCE: GitHub API (created >2026-06-30)

### Methodology
- GitHub API search: `topic:mcp-server created:>2026-06-30`
- Cross-referenced against existing catalog (index.md, morning scan results)
- Morning scan used `pushed:>2026-06-30` — this PM update uses `created` to catch repos that were created today but may have been pushed slightly earlier
- 10 repos created on July 1, 2026. 2 passed business-relevance filter.

---

## NEW BUSINESS-RELEVANT SERVERS

### 1. Meta Business MCP — WhatsApp Business Cloud API ★ New
- **Category:** Communication / Commerce
- Production-validated MCP server for WhatsApp Business Cloud API — compliance engine, error intelligence & message orchestration for AI agents. 24 tools, sub-2ms decisions, 85.6% test coverage. Built in Go.
- GitHub: github.com/metabusiness-mcp/meta-business-mcp (⭐1)
- Topics: whatsapp, whatsapp-business-api, mcp-server, messaging-api, chatbot, claude, meta-api
- **Business relevance:** WhatsApp is the #1 business messaging platform globally (2B+ users). This server gives AI agents direct access to Meta's official WhatsApp Business Cloud API — transactional messaging, customer support, compliance enforcement. Unlike Neuron (marketing-focused), this targets the raw API for production messaging workflows. Essential for operators in WhatsApp-first markets (LATAM, India, SEA, Africa) needing AI-driven WhatsApp communication.

### 2. Protonmail-rs — Proton Mail MCP ★ New
- **Category:** Communication / Security
- Pure-Rust Proton Mail client — library, CLI, and MCP server with end-to-end OpenPGP encryption. First MCP server for Proton Mail (100M+ users globally).
- GitHub: github.com/filippofinke/protonmail-rs (⭐1)
- Topics: protonmail, openpgp, e2e-encryption, mcp-server, rust, email
- **Business relevance:** First MCP server for Proton Mail — the leading encrypted email provider. Operators in regulated industries (HIPAA, legal, finance) can now have AI agents handle encrypted email while maintaining end-to-end encryption. Proton's zero-access architecture means even Proton cannot decrypt emails — critical for attorney-client privilege, healthcare communications, and financial compliance.

---

## ALSO NOTED (Lower Priority / Niche)

| Server | Category | Why Not Added |
|--------|----------|---------------|
| CRThu/CarrotContext | Enterprise KM | Chinese-market enterprise knowledge management. Niche regional use case. |
| pipeworx-io/mcp-crontab | Dev Tools | Commodity (crontab expression parser) |
| pipeworx-io/mcp-mime | Dev Tools | Commodity (MIME type lookup) |
| pipeworx-io/mcp-csv | Dev Tools | Commodity (CSV/JSON converter) |
| pipeworx-io/mcp-color | Dev Tools | Commodity (color utilities) |
| pipeworx-io/mcp-geohash | Dev Tools | Commodity (geohash encoder) |
| rzere/mcpexplorer-docs | Meta / Docs | Documentation only, not an MCP server |
| Kuberwastaken/awesome-claude-mcp-servers | Meta / Curation | Curated list, not an MCP server |

---

## KEY TRENDS (July 1 PM Update)

- **WhatsApp MCP ecosystem expanding**: Two WhatsApp MCP servers now exist — Neuron (marketing/broadcasts, 120+ tools) and Meta Business MCP (raw API, compliance-focused, 24 tools). WhatsApp is becoming a distinct MCP category.
- **Encrypted communication goes MCP**: Protonmail-rs brings end-to-end encrypted email to AI agents. This opens regulated industries (legal, healthcare, finance) to AI-driven communication workflows where privacy is non-negotiable.
- **Commodity utilities still flowing**: The pipeworx-io suite (crontab, MIME, CSV, color, geohash) represents the "long tail" of MCP development — small, single-purpose utilities. These won't be catalogued individually but signal a maturing ecosystem where even minor developer tools get MCP interfaces.

---

## ACTIONS TAKEN

- ✅ Added 2 new servers to `index.md` catalog
- ✅ Created integration guide: Meta Business MCP (`meta-business-mcp.md`)
- ✅ Created integration guide: Protonmail-rs (`protonmail-rs.md`)
- ✅ Updated "last updated" timestamp
- ⬜ Push to GitHub

---

*Scan performed July 1, 2026 PM. Source: GitHub API (topic:mcp-server created >2026-06-30).*
*Morning scan covered pushed >2026-06-30. This PM update uses created date to catch repos the morning scan may have missed.*
