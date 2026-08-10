---
title: "FlowyTeam OKR MCP — Integration Guide"
description: "Native OKR/KPI MCP server — connect Claude, ChatGPT, or any MCP client to your OKRs, KPIs, tasks, projects, and team management. 33 tools, one connection."
category: mcp
tags: [mcp-server, okr, kpi, performance-management, project-management, business-operations, hermes-agent]
last_updated: 2026-08-10
---

# FlowyTeam OKR MCP Server — OKR & Performance Management for AI Agents

**Rating:** ★★ | **Category:** Business Operations | **Transport:** Streamable HTTP

## What It Does

FlowyTeam is a native OKR MCP server that connects Claude, ChatGPT, Claude Code, or n8n to your organization's OKRs, KPIs, tasks, projects, employees, attendance, leave, tickets, clients, leads, and invoicing. **33 tools, one connection.** Your agent can read every objective and key result, post check-ins, move key-result progress, track KPIs, and generate reports — all in plain language without opening a dashboard.

## Why Business Operators Need This

OKR tracking is high-friction: most teams set quarterly OKRs, check them twice, and forget them. FlowyTeam makes OKR management conversational — ask "How are we tracking against Q3 objectives?" and get a real-time answer with specific key-result progress. The 33-tool surface goes beyond OKRs to cover the full operational stack (tasks, projects, attendance, leave, clients, leads, invoicing), making it a unified business operations MCP server rather than a point solution.

**Competitive landscape:** Most MCP servers in the productivity space are developer tools (ATLAS, task management for coding agents). FlowyTeam is the first MCP server purpose-built for business performance management — OKRs, KPIs, and team operations. The OAuth gateway with public onboarding tools (no token required for account creation) removes setup friction.

## Quick Start

### Connection Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (Remote) |
| **OAuth Endpoint** | `https://flowyteam.com/api/mcp/cloud/rpc` (Claude Desktop, ChatGPT) |
| **CLI Endpoint** | `https://flowyteam.com/api/v2/mcp/rpc` (Claude Code, Cursor, VS Code) |
| **Gateway Endpoint** | `https://flowyteam.com/api/mcp/gateway` (no token — onboarding only) |
| **Authentication** | OAuth 2.0 with PKCE (desktop/web) or Bearer token (CLI) |
| **Tools** | 33 |
| **GitHub** | `flowy-team/okr-mcp-server` (0★, created Aug 7, 2026) |

> ⚠️ The OAuth endpoint (`/api/mcp/cloud/rpc`) and CLI endpoint (`/api/v2/mcp/rpc`) are **not interchangeable**. Use the correct one for your client.

### Claude Desktop / ChatGPT (OAuth)

No API token needed. Authorize once per app.

```
URL: https://flowyteam.com/api/mcp/cloud/rpc
```

**Claude:** Settings → Connectors → Add custom connector → paste URL → Log in → Authorize.

**ChatGPT:** Settings → Connectors → add the same URL and authorize.

Uses OAuth 2.0 with PKCE. Tools respect your existing FlowyTeam role and permissions.

### Claude Code / Cursor / VS Code (Bearer Token)

Get your API token from FlowyTeam → **Settings → MCP & AI Integration**.

```bash
claude mcp add --transport http flowyteam \
  https://flowyteam.com/api/v2/mcp/rpc \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

```json
{
  "mcpServers": {
    "flowyteam": {
      "transport": "http",
      "url": "https://flowyteam.com/api/v2/mcp/rpc",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

### No Account Yet? Use the Gateway

The public gateway exposes three onboarding tools with **no token required** — an agent can create and activate an account conversationally:

```bash
claude mcp add --transport http flowyteam https://flowyteam.com/api/mcp/gateway
```

## Key Tools (33 Total)

| Category | Tools | Description |
|----------|-------|-------------|
| **OKRs** | Read objectives, read key results, post check-ins, update KR progress | Full OKR lifecycle management |
| **KPIs** | Read KPIs, update KPI values, generate KPI reports | Performance metric tracking |
| **Tasks** | List, create, update, assign, complete tasks | Task management across projects |
| **Projects** | List projects, read project details, track milestones | Project portfolio visibility |
| **Employees** | Directory, attendance, leave requests, approvals | Team management |
| **Tickets** | Support ticket read/write | Help desk integration |
| **CRM** | Clients, leads, opportunities | Lightweight CRM |
| **Finance** | Invoices, payments | Basic financial tracking |
| **Reports** | Generate OKR, KPI, and performance reports | Automated reporting |

## Example Usage

### OKR Check-In

Ask your agent: *"How are we tracking against Q3 objectives?"*

The agent reads all Q3 objectives and key results, returns a status summary with progress percentages, and highlights at-risk items.

### Post a Check-In

Ask your agent: *"Update KR-3.2 to 65% — we shipped the API integration this week."*

The agent posts a check-in with the progress update and your note.

### Team Capacity Check

Ask your agent: *"Who's out this week and how does that affect our sprint commitments?"*

The agent checks attendance/leave, cross-references with assigned tasks, and flags at-risk deliverables.

### Generate Monthly Report

Ask your agent: *"Generate the August OKR report for the leadership team."*

The agent pulls OKR progress, KPI trends, and team activity into a structured report.

## Pricing

FlowyTeam requires a subscription. Check [flowyteam.com](https://flowyteam.com) for current plans. The OAuth gateway includes free onboarding tools for account creation.

## Repository & Resources

| Resource | URL |
|----------|-----|
| **GitHub** | [github.com/flowy-team/okr-mcp-server](https://github.com/flowy-team/okr-mcp-server) |
| **Website** | [flowyteam.com](https://flowyteam.com) |
| **Setup Guide** | [flowyteam.com/get/mcp-server](https://flowyteam.com/get/mcp-server) |
| **API Reference** | [flowyteam.com/get/mcp-docs](https://flowyteam.com/get/mcp-docs) |
| **OAuth Docs** | [flowyteam.com/mcp-docs](https://flowyteam.com/mcp-docs) |

## Verdict: ★★ — Strong for Teams Already Using OKRs

FlowyTeam is the first MCP server to bring OKR and KPI management to AI agents. The 33-tool surface covering the full operational stack (not just OKRs) makes it a unified business operations MCP rather than a point solution. The OAuth gateway with no-token onboarding tools is clever — reduces setup friction to near zero.

**Strengths:** 33 tools covering OKRs + KPIs + tasks + team + CRM + invoicing, OAuth with PKCE for desktop/web, public gateway for no-token onboarding, role-based permissions respected, hosted (no self-hosting).

**Limitations:** Brand new (0 stars, created Aug 7, 2026), requires FlowyTeam subscription, hosted-only (no self-hosting option), separate endpoints for OAuth vs CLI clients can confuse, documentation split across three URLs.

**Best for:** Teams already using or adopting OKR frameworks who want performance management integrated into their AI agent workflows. Particularly strong for operations teams that need visibility across OKRs, projects, and team capacity in one agent connection.
