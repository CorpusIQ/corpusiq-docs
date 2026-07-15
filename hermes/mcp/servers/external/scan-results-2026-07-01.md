---
title: "MCP Server Scan Results — 2026-07-01"
description: "MCP server discovery scan results for July 1, 2026. Automated scan of new and existing MCP server integrations with availability checks and status updates for the Hermes ecosystem."
---

# MCP Server Directory Scan — July 1, 2026

## SOURCE: GitHub Search (pushed July 1, 2026)

### Methodology
- GitHub API search: `topic:mcp-server` pushed >2026-06-30
- Cross-referenced against existing catalog (index.md, last updated June 30)
- mcp.so unavailable (Cloudflare blocking persists)
- mcpservers.org returned no new servers in SSR payload

---

## NEW BUSINESS-RELEVANT SERVERS

### 1. memo — Local-First AI Memory ★ New
- **Category:** Memory & Knowledge / Privacy
- 100% local persistent semantic memory for AI agents on Apple Silicon (MLX) or Linux/Ubuntu (CPU). Markdown source of truth, sqlite-vec + BM25 hybrid search, codegraph-backed knowledge graph. MCP server + CLI. No cloud, no API keys.
- GitHub: github.com/jagoff/memo
- PyPI: pypi.org/project/mlx-memo/
- **Business relevance:** Privacy-first memory infrastructure for operators who need local-only AI agent memory without cloud dependencies. Essential for regulated industries (HIPAA, GDPR) or operators who refuse cloud-based memory. Competes with Memclaw/axiomseal on the privacy dimension.

### 2. Chia Health MCP — Telehealth Operations ★ New
- **Category:** Healthcare / Compliance
- HIPAA-compliant telehealth operations via MCP — manage patient intake, prescriptions, consent forms, lab orders, and payment (Stripe) through AI agents. Supports GLP-1 weight loss, peptides, anti-aging, longevity clinics.
- GitHub: github.com/Carolaunfading944/chia-mcp
- Topics: telehealth, HIPAA, GLP-1, semaglutide, tirzepatide, peptides, longevity, anti-aging, pharmacy
- **Business relevance:** First healthcare-operations MCP server. Operators in telehealth, weight loss clinics, peptide therapy, longevity medicine can automate patient workflows through AI agents. Massive market (GLP-1 market alone is $100B+). Compliance-sensitive vertical.

### 3. CCHub — Claude Code Config Manager ★ New
- **Category:** Development & Infrastructure / Tooling
- Desktop app (Tauri + React + Rust) for managing Claude Code MCP servers, skills, plugins, hooks, and config profiles in one UI. Multi-profile management for complex setups.
- GitHub: github.com/boxxapp23-pixel/cchub
- Topics: claude-code, claude-mcp, config-manager, desktop-app, developer-tools, mcp, tauri
- **Business relevance:** Developer tooling for operators running complex Claude Code setups across multiple profiles, teams, or environments. Centralizes MCP server + skill + plugin management.

### 4. Bambu Printer MCP — 3D Printing Automation ★ New
- **Category:** Manufacturing / Hardware
- Control Bambu Lab 3D printers, edit STL files, manage 3MF print workflows via MCP. AI agents can start prints, monitor progress, edit models. Compatible with Bambu CLI, Bambu Studio, Klipper, OctoPrint, Moonraker.
- GitHub: github.com/offthehook-implication870/bambu-printer-mcp (⭐2)
- Topics: bambu-lab, 3D printing, STL, 3MF, Klipper, OctoPrint, Blender
- **Business relevance:** Manufacturing and prototyping operators with Bambu Lab 3D printers can automate print workflows through AI agents. Niche but growing — Bambu Lab is the fastest-growing 3D printer brand (consumer + prosumer market).

---

## ALSO NOTED (Lower Priority / Niche)

| Server | Category | Why Not Added |
|--------|----------|---------------|
| mcp-local-school-orchestrator (sheelaghexpensive483) | Education | Very niche (local school data privacy) |
| cc-update-all (alaas4989) | Dev Tools | Commodity (update CLI for Claude Code marketplaces) |
| tidal-cli (robbiek3659, ⭐1) | Media | Personal use (Tidal music CLI) |
| AE-agent (smooth-snarl702) | Content Creation | Niche (After Effects automation) |
| x402-fpl-api (Edwinvi6421) | Entertainment | Zero business relevance (Fantasy Premier League) |
| Research-Agent (Crinolineflexion823) | Content/Research | Alibaba competition entry, no production relevance |
| Firebreak (Nonmigratory-electrolysis990) | Security | Niche (offensive pentesting MCP) |
| mcp-terminal-server (Unfathomable-siren38) | Dev Tools | Commodity (PTY terminal server) |
| my-claude-skills (nariatrip191, ⭐1) | Productivity | Personal skills repo, not a server |
| phpman (chedong/phpman, ⭐1) | Dev Tools | Niche (PHP manual MCP wrapper) |

---

## KEY TRENDS (July 1, 2026)

- **Healthcare MCPs emerging**: Chia Health signals healthcare operations as a new MCP category — HIPAA-compliant telehealth workflows are now automatable through AI agents. Huge market (GLP-1 alone is $100B+).
- **Privacy-first memory infrastructure**: memo (100% local MLX/CPU) shows privacy-conscious operators demanding local-only AI memory without cloud dependencies. Competes with cloud-based Memclaw/axiomseal on privacy axis.
- **Developer tooling maturing**: CCHub (desktop config manager for Claude Code) shows ecosystem tooling is maturing beyond data access into developer UX layer.
- **Hardware automation expanding**: Bambu Printer MCP shows physical hardware (3D printers) becoming MCP-addressable — manufacturing/prototyping workflows can now be AI-driven.

---

*Scan performed July 1, 2026. Source: GitHub API (topic:mcp-server pushed >2026-06-30).*
*Note: mcp.so unavailable (Cloudflare). mcpservers.org SSR payload contained no new servers beyond June 30.*
