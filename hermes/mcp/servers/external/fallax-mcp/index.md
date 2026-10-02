---
title: "Fallax MCP - Phishing Simulation Results for Audit Evidence"
description: "Hosted MCP server for phishing simulation and security awareness results: programme summaries, resilience trends, department breakdowns, campaign detail and the per-person evidence trail ISO 27001 and SOC 2 auditors ask for. Twelve tools, ten read-only, OAuth 2.1 with workspace-scoped URLs."
category: Security
stars: "n/a (hosted, closed source)"
added: 2026-09-02
source: "mcp.so GitHub issue #3899"
relevance: ★★★
tags: [security, phishing, awareness-training, iso-27001, soc-2, audit]
---

# Fallax MCP - Phishing Simulation Results for Audit Evidence

**Hosted Streamable HTTP MCP server** - reads one workspace's phishing-simulation and security-awareness results: programme summaries, resilience trends, department breakdowns, campaign detail and the per-person evidence an ISO 27001 or SOC 2 auditor asks for. Ten of twelve tools only read; nothing can create, launch or schedule a simulation.

## Spec Block

| Field | Value |
|---|---|
| Server name | Fallax |
| Registry | io.fallax/fallax |
| Endpoint | https://app.fallax.io/mcp/{workspace-slug} |
| Transport | Streamable HTTP, JSON, no session state |
| Auth | OAuth 2.1 with dynamic client registration (Google or Microsoft sign-in) |
| Protocol | 2025-06-18, 2025-03-26 and 2024-11-05 accepted |
| Docs | https://fallax.io/docs/mcp |
| Repo | none public (closed source) |

## Why This Matters for Operators

Security reports normally have to be written by logging into a dashboard and copy-pasting numbers. Fallax's MCP server lets an assistant answer "how did last quarter go" from the workspace's own results and draft the awareness section of an ISO 27001 report from campaigns that actually ran, with every claim citable to the campaign record. Verification: anonymous initialize returned 401 Unauthorized (endpoint live, OAuth-gated).

## Tools & Capabilities (12 tools)

| Tool | Access | Description |
|---|---|---|
| get_program_summary | Read | Headline open, click, credential-submit and report rates versus the previous period |
| get_resilience_trend | Read | Rates over time, bucketed weekly (30d/90d) or monthly (12m/all-time) |
| get_breakdowns | Read | Period cut by department, template, send language and campaign |
| list_campaigns | Read | Every campaign, newest first, with status and funnel |
| get_campaign | Read | One campaign in full: template, audience, domain, schedule, funnel |
| list_discovered_apps | Read | SaaS apps the tenant's users actually use, with lure availability |
| get_setup_status | Read | What is and is not configured before a simulation can run |
| get_programme_status | Read | Whether the continuous programme is running and its queue |
| get_evidence_bundle | Read, person-level | The ISO 27001 A.6.3 audit trail: one row per person per campaign |
| explain_send | Read, person-level | Why one person received the simulation they got, from planning-time records |
| pause_programme | Write | Stop the continuous programme and drop its queue (owner/admin) |
| exclude_person | Write | Take one person out of the programme permanently (owner/admin) |

## Installation

Connect once from the app: enable assistant access in Fallax Settings, then add the workspace URL to Claude as a custom connector, to ChatGPT as a developer-mode connector, or to any MCP client as a remote server. The URL is the whole configuration: no API key to mint, copy or rotate. The first call opens an OAuth flow with your existing Google or Microsoft account. Workspace membership is rechecked on every call, not captured at connect time.

## Configuration

- One URL per workspace: https://app.fallax.io/mcp/{workspace-slug}
- Person-level tools stay hidden until the workspace enables person-level access
- Restarting a paused programme or re-adding an excluded person happens in the Fallax app, not over MCP

## Business Relevance

Useful for: security and compliance teams preparing ISO 27001 (A.6.3) and SOC 2 evidence, MSSPs reporting across customer workspaces, and executives who want a plain-language answer on whether click rates are falling without opening the dashboard.

## Integration with CorpusIQ

Combine with CorpusIQ's compliance and document workflows: pull Fallax evidence into agent-generated audit reports alongside other compliance data an organization tracks in one place.

## Limitations

Read-only by design: nothing can send a simulation. Person-level data is opt-in per workspace. No public repository. Requires an active Fallax subscription with assistant access enabled.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [VulX Watch MCP - Independent Security Review for AI-Built Apps](/hermes/mcp/servers/external/vulx-watch-mcp)
- [Trooth Network MCP - Witnessed Company Trust Records](/hermes/mcp/servers/external/trooth-mcp)
