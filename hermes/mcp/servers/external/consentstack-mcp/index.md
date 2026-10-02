---
title: ConsentStack MCP - Agent-Managed Cookie Consent
description: "Hosted MCP server from ConsentStack with 22 tools for GDPR/CCPA cookie consent end to end - create sites, stage and publish banners, run compliance scans and categorize trackers with OAuth 2.1 sign-in at app.consentstack.io/api/mcp."
category: Compliance
stars: "n/a (official hosted service)"
added: 2026-08-31
source: "mcpservers.org homepage latest (Aug 31, 2026 evening sweep)"
relevance: ★★★
tags: [mcp-server, consent-management, gdpr, ccpa, privacy, compliance, cookies, remote]
---

# ConsentStack MCP

**Hosted MCP server from the ConsentStack consent management platform - 22 tools that let an AI agent set up and run cookie consent end to end.** Create a site, stage banner configuration as drafts, publish after approval, get the install snippet, run compliance scans and categorize the trackers they find - all from the agent that built the site, through OAuth sign-in with the same account used for the dashboard.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://app.consentstack.io/api/mcp
Auth: OAuth 2.1 (sign in with a ConsentStack account; no API keys)
Registry: io.consentstack/cookie-consent (listed in the MCP Registry)
Homepage: consentstack.io
Tools: 22 (site creation, banner configuration and publishing, install snippet, compliance scans, tracker categorization)
Pricing: free signup with a free Basic tier; paid plans beyond
```

## Why This Matters for Operators

Cookie compliance is the highest-touch paperwork every website carries. The rules change per jurisdiction, the trackers multiply every release, and a stale banner is a real fine risk under GDPR and CCPA.

First, **the same agent that builds the site can make it compliant.** ConsentStack's hosted MCP is explicitly designed for AI-built sites: the agent that generated the pages can create the consent setup, stage the banner as a draft, get the three install tags with the real site key, and publish only after you approve the changes in conversation.

Second, **jurisdiction handling is built in, not configured by hand.** The platform's compliance engine covers 195+ regulations and auto-detects each visitor's jurisdiction, serving opt-in for GDPR, opt-out for CCPA, and the right model for LGPD, PIPEDA, POPIA and PDPA - so the banner behavior stays correct as traffic geography changes.

Third, **drafts never touch the live site.** Banner appearance, text and compliance settings are staged as drafts; publish_config is the only path to production. An agent can prepare a full consent redesign while the current banner keeps serving.

## Tools and Capabilities

Per the mcpservers.org listing and ConsentStack's documentation, the server's 22 tools cover the whole consent lifecycle:

| Capability | What it does |
|-----------|-------------|
| Site management | Create and register the domains the consent setup runs on (manage_domains) |
| Setup guide | get_setup_guide returns the three install tags with your real site key for the agent to add to the site head |
| Banner configuration | Stage banner appearance, text and compliance settings as drafts |
| Publishing | publish_config pushes approved changes to the live site |
| Compliance scan | Scan the site and categorize the trackers it finds |
| Tracker management | Categorize and manage detected trackers against consent purposes |

## Installation

Connect any MCP client that supports remote servers over Streamable HTTP with OAuth:

```json
{
  "mcpServers": {
    "consentstack": {
      "url": "https://app.consentstack.io/api/mcp"
    }
  }
}
```

On first connect the client opens a browser window where you sign in with the same account used for the ConsentStack dashboard. There are no API keys to create or paste; a free account is enough to start.

## Configuration

No static configuration beyond the URL. The server is endpoint-verified (an unauthenticated initialize returns a clean 401 invalid_token, confirming the OAuth gate is enforced). After sign-in, the agent reads the account's sites and works against the live ConsentStack dashboard state.

## Business Relevance

- **Site owners and operators** get a compliant consent setup installed by the same agent that builds or maintains the site, with human approval required before anything publishes.
- **Agencies managing many client sites** stage banner changes as drafts across accounts and publish after client sign-off, per domain.
- **Compliance officers** run scans and tracker categorization from chat instead of logging into yet another dashboard.
- **Growth teams** keep consent analytics and banner behavior aligned with campaign pages without a developer ticket.

## Integration with CorpusIQ

ConsentStack pairs with CorpusIQ as the compliance layer beside the analytics layer. CorpusIQ's GA4 connector reports traffic and conversion; ConsentStack's MCP reports what consent state those visitors were under and which trackers are categorizing correctly - so an operator can ask whether a traffic drop tracks with a banner change, in one conversation. The Cookie Free Analytics MCP composes on the measurement side for cookieless GDPR-first reporting, and PolicyForge MCP covers the legal policy documents that sit alongside the consent setup.

## Limitations

- OAuth-only authentication - no static API keys, so unattended server-to-server use requires an OAuth session.
- New to the MCP Registry (io.consentstack/cookie-consent); tool-by-tool docs beyond the listing are thin.
- Hosted platform only - no self-host option.
- Free Basic tier covers entry-level use; higher traffic and multi-site needs move to paid plans.
- Compliance jurisdiction depth is the vendor's claim; verify against your counsel for regulated markets.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Cookie Free Analytics MCP - Cookieless GDPR-First Web Analytics](/hermes/mcp/servers/external/cookiefreeanalytics-mcp)
- [PolicyForge MCP - Legal Policies Generated and Audited from Your Codebase](/hermes/mcp/servers/external/policyforge-mcp)
