---
title: New Skills Discovery — July 1, 2026
description: 12 new OpenClaw and Hermes ecosystem skills discovered in the July 1, 2026 sweep. Includes deployment tooling (systemd, launchd), Alibaba Cloud integration, creative tooling, and desktop security analysis.
last_updated: 2026-07-01
---

# New Skills Discovery — July 1, 2026

**Sweep Date:** July 1, 2026
**Queries:** 18 search terms across 3 rounds
**Skills Checked:** 243 (round 1) + expanded queries (round 2)
**New Found:** 12 (Hermes/OpenClaw ecosystem)
**Install Range:** 19–85 installs

## Summary

This sweep surfaced 12 genuinely new skills not catalogued in any previous marketplace page. The majority come from two new repos: `alphaonedev/openclaw-graph` (creative + deployment tooling for OpenClaw) and `cinience/alicloud-skills` (Alibaba Cloud SLS integration for OpenClaw). Also surfaced: an MCP plugin for OpenClaw and a MetaMask desktop security analysis skill for Hermes.

---

## New Skills

### Deployment & Infrastructure

| Skill | Installs | Source | Description |
|-------|----------|--------|-------------|
| `linux-systemd` | 54 | `alphaonedev/openclaw-graph` | Systemd service management for OpenClaw agent deployment on Linux |
| `macos-launchd` | 53 | `alphaonedev/openclaw-graph` | Launchd plist management for OpenClaw agent deployment on macOS |

Both skills enable running OpenClaw agents as persistent background services with automatic restart on failure — essential for production deployments.

### Cloud Integration

| Skill | Installs | Source | Description |
|-------|----------|--------|-------------|
| `alicloud-observability-openclaw-sls-integration` | 85 | `cinience/alicloud-skills` | Alibaba Cloud SLS observability pipeline for OpenClaw agents — log collection, metric aggregation, alerting |
| `aliyun-sls-openclaw-integration` | 49 | `cinience/alicloud-skills` | Alibaba Cloud Log Service (SLS) integration — structured logging and real-time log analysis for OpenClaw |

### Creative & Development Tooling

| Skill | Installs | Source | Description |
|-------|----------|--------|-------------|
| `procedural-generation` | 48 | `alphaonedev/openclaw-graph` | Procedural content generation via OpenClaw — 3D assets, textures, terrains |
| `arkit-advanced` | 45 | `alphaonedev/openclaw-graph` | Advanced ARKit integration for OpenClaw — spatial computing and AR experiences |
| `testing-integration` | 44 | `alphaonedev/openclaw-graph` | Automated testing harness for OpenClaw skills — unit, integration, and E2E |

> **Note:** `alphaonedev/openclaw-graph` also contains `playwright-scraper` (1,578 installs) which was already catalogued in the June 26 afternoon sweep.

### MCP & Plugin Ecosystem

| Skill | Installs | Source | Description |
|-------|----------|--------|-------------|
| `mcp-integration` | 19 | `lunarpulse/openclaw-mcp-plugin` | MCP server bridge for OpenClaw — connect OpenClaw agents to any MCP-compatible server |

### Security

| Skill | Installs | Source | Description |
|-------|----------|--------|-------------|
| `metamask-openclaw-desktop-security-analysis` | 19 | `aradotso/hermes-skills` | MetaMask wallet security analysis through Hermes — desktop-level Web3 security auditing |

---

## Non-Hermes Skills (Excluded)

The following skills were detected but excluded as they are not Hermes/OpenClaw ecosystem:

- `ruby-mcp-server-generator` (8,463) — `github/awesome-copilot` (Copilot-specific)
- `cloudflare-mcp-server` (254) — `secondsky/claude-skills` (Claude-specific)
- `react-native-expo` (103) — `ovachiever/droid-tings` (generic)
- `add-mcp` / `delete-mcp` / `update-mcp` (31 each) — `berriai/litellm-skills` (LiteLLM-specific)
- `discord-voice` (28) — `avatarneil/discord-voice` (generic)

---

## Installation

To install any of these skills:

```bash
# OpenClaw Graph skills (deployment, creative, testing)
npx skills add alphaonedev/openclaw-graph/linux-systemd
npx skills add alphaonedev/openclaw-graph/macos-launchd
npx skills add alphaonedev/openclaw-graph/procedural-generation
npx skills add alphaonedev/openclaw-graph/arkit-advanced
npx skills add alphaonedev/openclaw-graph/testing-integration

# Alibaba Cloud integration
npx skills add cinience/alicloud-skills/alicloud-observability-openclaw-sls-integration
npx skills add cinience/alicloud-skills/aliyun-sls-openclaw-integration

# MCP plugin
npx skills add lunarpulse/openclaw-mcp-plugin/mcp-integration

# Hermes security
npx skills add aradotso/hermes-skills/metamask-openclaw-desktop-security-analysis
```

---

*Part of the Hermes Skills Library. Discovered July 1, 2026 — 18-query sweep across skills.sh API.*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
