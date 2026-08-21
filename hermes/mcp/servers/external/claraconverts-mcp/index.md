---
title: "ClaraConverts MCP — Website Conversion Agent, Provisioned and Managed Over MCP"
description: "MCP server for ClaraConverts, a 24/7 AI conversion agent for websites: 9 tools provision and manage the account — pricing, trial tenant, embed snippet, site knowledge refresh, integration config and upgrades — over Streamable HTTP."
category: Marketing & Conversion
stars: n/a (new listing)
added: 2026-08-21
source: "mcp.so GitHub issue #3675"
relevance: ★★
tags: [conversion, cro, website, lead-capture, ai-agent, provisioning, marketing, remote-mcp]
---

# ClaraConverts MCP

**Provision and manage a website conversion agent entirely through tool calls.** ClaraConverts answers visitor questions, guides decisions and captures leads on any website with a one-line embed. Its MCP server is the account layer: an agent can check pricing, spin up a 14-day trial tenant, fetch the embed snippet, refresh the site knowledge base, configure integrations, list Cal.com event types and generate upgrade links — no dashboard clicking.

```
Server type: Remote (Streamable HTTP)
Auth: None for public tools; Bearer token (issued by create_trial_tenant) for account tools
Endpoint: https://claraconverts.com/mcp
Tools: 9 (pricing, provisioning, embed, settings, integrations)
Pricing: 14-day free trial (no card); plans from $49/mo (Standard $49, Pro $99, Volume $799)
Category: Marketing & Conversion
Built by: ClaraConverts (companion repo: github.com/cognicores/claraconverts-agents)
```

## Why This Matters for Operators

A website conversion agent is only useful once it's live, trained on the site and wired into the tools that book the meetings. That setup is normally a sequence of dashboard steps. **ClaraConverts' MCP makes the agent do its own onboarding**: `create_trial_tenant` mints the account, `get_embed_snippet` returns the one-liner to install, `refresh_site_knowledge` retrains on the site after a redesign, and `configure_integration` wires Cal.com so booked meetings land on your calendar.

The free-to-start model matters too — public tools (pricing, integrations, trial creation) work without credentials, so an agent can evaluate the product before you commit.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_pricing` | Read current plans and pricing |
| `list_integrations` | See what the conversion agent can connect to |
| `create_trial_tenant` | Spin up the free 14-day trial (no card); returns the Bearer token |
| `get_embed_snippet` | Fetch the one-line website install code |
| `update_tenant_settings` | Manage account settings |
| `refresh_site_knowledge` | Retrain the agent on current site content |
| `configure_integration` | Wire integrations (e.g. Cal.com) |
| `list_calcom_event_types` | List bookable event types |
| `get_upgrade_link` | Generate the plan upgrade link |

## Installation

```bash
claude mcp add claraconverts --transport http https://claraconverts.com/mcp
```

Connect without credentials to browse pricing and create a trial; after `create_trial_tenant` returns a Bearer token, attach it for the account-management tools.

## Configuration

```json
{
  "mcpServers": {
    "claraconverts": {
      "type": "http",
      "url": "https://claraconverts.com/mcp"
    }
  }
}
```

Public tools need no auth. Account tools send `Authorization: Bearer <token>` from the trial tenant.

## Business Relevance

- **SMB operators** add a 24/7 site conversion agent and manage it without a developer
- **E-commerce teams** answer visitor questions pre-purchase and capture leads instead of bounced sessions
- **Agencies** provision and configure client tenants programmatically (the Volume plan covers up to 10 sites)
- **Ops teams** keep the agent's knowledge fresh after every site change through `refresh_site_knowledge`

## Integration with CorpusIQ

ClaraConverts captures the leads; CorpusIQ routes and measures them. A composed workflow has the conversion agent qualify visitors on-site while CorpusIQ's CRM connectors (HubSpot, Close) receive the captured leads and GA4 tracks the conversion path that produced them — one session can then answer "how many of this week's site leads came from the ClaraConverts agent, and what did they buy" across both surfaces.

## Limitations

- Backend is closed-source (companion repo only) — you depend on the hosted service
- MCP surface is provisioning and management, not the live conversation data
- Paid plans start at $49/mo after the 14-day trial
- Brand new listing (Aug 2026), no track record yet
- Conversion-agent category is crowded; differentiation is the embed + provisioning loop

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
