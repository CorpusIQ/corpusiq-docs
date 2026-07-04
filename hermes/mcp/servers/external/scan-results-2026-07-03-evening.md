---
title: "MCP Server Discovery — July 3, 2026 (Evening Supplement)"
description: "Late-day supplemental scan of mcpservers.org and mcp.so. 3 new business-relevant MCP servers across task management, product design, and design-to-code categories."
category: mcp
tags: [mcp-servers, daily-scan, july-2026]
last_updated: 2026-07-03
---

# MCP Server Discovery — July 3, 2026 (Evening Supplement)

**Source:** mcpservers.org (sitemap delta), mcp.so, GitHub API
**Method:** Sitemap diff against morning scan + GitHub topic:mcp-server recent pushes
**Date:** July 3, 2026 (evening)
**Prior scan:** [July 3 morning](/hermes/mcp/servers/external/scan-results-2026-07-03/)

## Summary

| Metric | Count |
|--------|-------|
| New servers in mcpservers.org sitemap delta | ~200 (since morning) |
| Already catalogued or developer-only | ~197 |
| **New business-relevant** | **3** |
| **Full integration guides created** | **2** |

## Priority Servers — Full Integration Guides Created

| # | Server | Category | Description | Source |
|---|--------|----------|-------------|--------|
| 1 | **Microsoft Planner MCP** | Task Management & Enterprise | AI-powered Microsoft Planner interaction via MCP. Create plans, manage tasks, update buckets, and automate project workflows in Microsoft 365 environments. Essential for enterprise operators on the Microsoft stack. | mcpservers.org |
| 2 | **Mowgli** | Product Design & UX | Intelligent product canvas with context and taste. Connect coding agents to iterate on product design — from sweeping new flows to surgical tweaks — and sync back to code. Built for product teams who want AI-driven design iteration. | mcpservers.org |

## Additional Notable Servers (Indexed, No Individual Guide)

| Server | Category | Description | Source |
|--------|----------|-------------|--------|
| **Design Context Bridge** | Design & Development | Turns AI agents into frontend developers who can read Figma files — not guess from screenshots. Identifies components, reads colors/type scale, infers routes, exports icons. Faithful design-to-code, not approximation. | mcpservers.org |
| **AgentMetal** | DevOps & Infrastructure | Rent a real Linux VPS as an AI agent. Pay USDC (x402 on Base) or card, SSH in under 60s, no signup. Provision, exec, firewall, and storage. For operators who need disposable cloud infrastructure for agent workflows. | mcpservers.org |
| **Odoo Pulse** | ERP & Business Operations | AI business analyst for Odoo ERP. Query business data, generate reports, and analyze operations through natural language. Companion to the existing odoo-mcp server — focused on business intelligence rather than administration. | mcpservers.org |
| **TrackingTime MCP** | Time Tracking & Productivity | Professional time tracking via MCP. Log hours, manage projects/tasks, generate timesheets, and analyze productivity patterns. For operators billing by the hour or tracking team utilization. | mcpservers.org |
| **Scouter MCP** | APM & Monitoring | Query Scouter APM (objects, counters, XLog transactions) over stdio. For operators monitoring application performance in production environments. | mcpservers.org |

## GitHub API Results

GitHub search for `topic:mcp-server pushed:>2026-07-03T12:00:00Z` returned several new repositories. Notable business-relevant finds:

| Server | Description | Stars |
|--------|-------------|-------|
| **IT Glue MCP** (selic/mcp-itglue) | MCP server for IT Glue — semantic search, documents, and flexible assets for MSPs. | 0 (new) |
| **SeekStone** (shaqmughal/seekstone) | Obsidian MCP server for Claude — filesystem-direct, 575× smaller payloads. | 7 |
| **Agentify** (harindukavishka/agentify) | Convert OpenAPI specs into nine standard AI agent interfaces. | 4 |

## Trends

- **Microsoft ecosystem opens up**: Microsoft Planner MCP marks growing enterprise MCP adoption. With Outlook MCP, Teams MCP, and now Planner MCP, the Microsoft 365 suite is becoming agent-accessible.
- **Design tools go MCP-native**: Mowgli and Design Context Bridge represent a new category — design tools that don't just show designs but let AI agents read, modify, and sync them.
- **Infrastructure-as-API**: AgentMetal's "rent a VPS via MCP" pattern signals a shift toward disposable, agent-provisioned infrastructure — no dashboards, no signups, just API calls.
- **ERP doubles down**: Odoo Pulse (business intelligence) joins the existing odoo-mcp (administration) — ERP platforms are building layered MCP access, not just one connector.

## Actions Taken

- 2 full integration guides created for priority servers:
  - `microsoft-planner-mcp.md`
  - `mowgli-mcp.md`
- 5 additional servers noted (indexed, no individual guide — niche or early-stage)
- Index.md update queued

## Non-Business Servers (Not Catalogued)

- Creed Space — AI safety guardrails (infrastructure-layer)
- Various cybersecurity/compliance MCPs (csoai-org/*) — compliance infrastructure
- Various developer tools (OpenAPI generators, code scanners, etc.)
- Temp/crypto/blockchain servers — speculative/niche
