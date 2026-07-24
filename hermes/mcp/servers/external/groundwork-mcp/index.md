---
title: "Groundwork MCP — Company-State Feed for AI Agents"
description: "Tenant-scoped, read-only company-state discovery for MCP-compatible AI agents. Module catalog, dashboard, brand settings, entitlement, and curated skill how-tos."
category: mcp
tags: [mcp, memory, knowledge, company-os, documentation, groundwork, rarefied-earth, hermes-agent]
github: https://github.com/Rarefied-Earth/groundwork
website: https://rarefied.earth/groundwork/
stars: 1
verified: true
source: mcp.so
discovered: 2026-07-24
pricing: Pro $49/mo · Operating $149/mo · Studio $299/mo · 14-day free trial
---

# Groundwork MCP — Company-State Feed for AI Agents

**Groundwork** stops agents from inventing your company. It's a hosted MCP server that gives any MCP-compatible client a tenant-scoped, read-only picture of what is current, what is entitled, and how work is supposed to run.

Think of it as a "company memory" layer that sits between your AI agents and your actual company state — modules, brand settings, dashboards, entitlements, and curated how-tos are all available through structured MCP tools.

## What It Does

- **Company-state feed**: Read-only access to your company's module catalog, dashboard settings, and brand configuration
- **Entitlement awareness**: Agents know what features/tiers you have access to — no inventing capabilities
- **Curated skill how-tos**: Documentation and procedures surfaced through MCP tools
- **Public proof (no account)**: Anyone can test via the public endpoint at `https://connector.rarefied.earth/public/mcp`
- **Tenant-scoped**: Each organization gets its own isolated view

## Key Tools

| Tool | Description |
|------|-------------|
| `groundwork_public_proof` | Verify the MCP connection works — no account required |
| `groundwork_public_status` | Check Groundwork service status |
| `demo_resume` | Example tool demonstrating the resume/company-state workflow |

## Quick Start

### 1. Try Without an Account

```bash
# Public endpoint — no auth required
# Add to your MCP client config:
{
  "mcpServers": {
    "groundwork-public": {
      "url": "https://connector.rarefied.earth/public/mcp"
    }
  }
}
```

Then call `groundwork_public_proof` to verify connectivity.

### 2. Full Setup (Pro Account)

```bash
# 1. Sign up at https://rarefied.earth/groundwork/
# 2. Start 14-day free trial (card required)
# 3. Get your tenant endpoint from the dashboard
# 4. Add to MCP config:
{
  "mcpServers": {
    "groundwork": {
      "url": "https://connector.rarefied.earth/YOUR_TENANT/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

### 3. Install Source (Self-Hosted)

```bash
git clone https://github.com/Rarefied-Earth/groundwork
cd groundwork
npm install
# Configure env vars, then:
npm start
```

## Hermes Agent Integration

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  groundwork:
    url: "https://connector.rarefied.earth/YOUR_TENANT/mcp"
    headers:
      Authorization: "Bearer ${GROUNDWORK_API_KEY}"
```

## Use Cases for Business Operators

1. **Agent onboarding**: New AI agents immediately know your company's stack, brand voice, and approved workflows — no manual context injection
2. **Multi-agent consistency**: All agents across Claude, Cursor, Hermes, and Codex read from the same company-state source
3. **Compliance guardrails**: Agents can check entitlements before suggesting features or workflows you don't have access to
4. **Workspace auditing**: The public proof tool lets you verify agent behavior without an account

## Limitations

- **Read-only**: Groundwork is a state feed, not a write-back system — agents can read company state but can't modify it
- **Source closed**: While docs are public, the core server code is closed source
- **New project**: 1 GitHub star as of July 2026 — early stage, expect API evolution
- **Trial requires card**: 14-day free trial needs payment card at checkout

## Pricing Tiers

| Tier | Price | Best For |
|------|-------|----------|
| **Pro** | $49/mo | Solo operators, single tenant |
| **Operating** | $149/mo | Small teams, multi-agent setups |
| **Studio** | $299/mo | Agencies, multi-tenant, advanced features |

All tiers include the 14-day free trial. Founding rates may apply.

## Category

**Memory & Knowledge** — alongside tools like Context7, Groundwork, and codicil. Groundwork differentiates by focusing on company-specific state rather than general documentation.

---

*Discovered via [mcp.so](https://mcp.so/servers/groundwork) on July 24, 2026. Verified listing. GitHub: [Rarefied-Earth/groundwork](https://github.com/Rarefied-Earth/groundwork).*
