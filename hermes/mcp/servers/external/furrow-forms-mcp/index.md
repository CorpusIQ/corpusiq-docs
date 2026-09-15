---
title: "Furrow Forms MCP - Agent-Operable Form Backend with Lead Capture"
description: "Hosted form backend whose entire product is operable through MCP: 26 tools covering account registration, form and client CRUD, submission reading, webhooks and Stripe checkout link generation. Streamable HTTP with token or OAuth auth, plus an npm stdio bridge. MIT, official registry record."
category: Marketing
stars: 1
added: 2026-09-03
source: "mcp.so homepage New Arrivals (furrow-forms)"
relevance: ★★
tags: [forms, lead-capture, webhooks, payments, no-code]
---

# Furrow Forms MCP - Agent-Operable Form Backend with Lead Capture

**Hosted MCP server (Streamable HTTP, 26 tools)** - the form backend for vibe-coded websites, designed so an agent can run the whole lifecycle end to end: create forms, read the submissions that come in, wire webhooks, and generate Stripe checkout links. Token or OAuth auth; npm stdio bridge for older clients.

## Spec Block

| Field | Value |
|---|---|
| Server name | furrow-forms |
| Repo | github.com/useburrow/furrow-forms |
| Endpoint | https://api.furrowforms.com/mcp |
| Transport | Streamable HTTP |
| Auth | Bearer token (frw_ prefix, minted in the dashboard) or OAuth sign-in |
| Tools | 26 tools - accounts, projects, forms, clients, submissions, webhooks, upgrade links |
| npm | @furrowforms/mcp (stdio bridge, same 26 tools) |
| Registry | com.furrowforms/furrow-forms |
| License | MIT |
| Examples | 33 tech stacks in the repo |

## Why This Matters for Operators

Form backends are where websites turn visitors into leads and paying customers. Furrow is unusual in that MCP and REST share the same domain logic - there is no drift between what agents and humans can do. An agent can register the account, scaffold the site integration, create the form, monitor submissions as they arrive, and test the webhook end to end, without a human clicking through a dashboard.

## Tools & Capabilities (26 tools)

| Group | Tools |
|---|---|
| Accounts and teams | get_account, update_account, list_teams, update_team |
| Projects and clients | create_project, get_project, update_project, archive_project, create_client, get_client, update_client, archive_client, list_projects, list_clients |
| Forms and embeds | create_form, get_form, update_form, archive_form, list_forms, get_snippet, bootstrap_site |
| Submissions and integrations | list_submissions, get_submission, upsert_project_webhook, test_webhook, create_upgrade_link, claude_desktop_config |

## Installation

Streamable HTTP (recommended): add `https://api.furrowforms.com/mcp` as a remote server. Tokens are minted in the dashboard under Settings → Tokens (the secret is shown exactly once), or the agent can register the account itself. OAuth works by leaving the header off and completing the sign-in prompt.

Stdio (Claude Desktop, older Cursor builds, Zed, Codex CLI):

```bash
claude mcp add furrow-forms -e FURROW_TOKEN=frw_... -- npx -y @furrowforms/mcp
```

## Configuration

Send the token as the bearer Authorization header (tokens use the frw_ prefix). The npm package @furrowforms/mcp bridges stdio clients to the hosted server with the FURROW_TOKEN environment variable. REST and MCP share the same domain logic.

## Business Relevance

For operators shipping marketing sites, landing pages and vibe-coded web apps: capture leads without a developer in the loop, read submissions directly in agent workflows, generate Stripe checkout links for paid offers, and route webhooks into automation. Agent-first form infrastructure means lead capture becomes part of the operations stack, not a separate tool.

## Integration with CorpusIQ

Form submissions are the top of the funnel CorpusIQ connectors report on: push Furrow leads into the CRM, join submission volume against GA4 and Stripe revenue in CorpusIQ reports, and trigger agent workflows on webhooks for immediate lead response.

## Limitations

Brand new (repo created Aug 26, 2026, 1 star). Young hosted service - verify uptime and data residency before production-critical use. Positioning is developer-facing (vibe-coded sites), though the data surface is operator lead capture.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Asyntai MCP - AI Support Agent for Websites](/docs/hermes/mcp/servers/external/asyntai-mcp)
- [Xverum MCP - People Search Across 750M Professional Profiles](/docs/hermes/mcp/servers/external/xverum-mcp)
