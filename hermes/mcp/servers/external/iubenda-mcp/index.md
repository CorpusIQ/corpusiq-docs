---
title: "iubenda MCP - Website Legal Compliance for Agents"
description: "Handle website legal compliance end to end: generate privacy and cookie policies, set up consent banners, draft terms and conditions, and run cookie scans through natural-language chat."
category: Compliance
stars: n/a (no public repo)
added: 2026-09-03
source: mcp.so
relevance: ★★★
tags: [compliance, gdpr, privacy, cookie-consent, legal, terms-and-conditions, remote-mcp]
---

# iubenda MCP

**Remote MCP server (Streamable HTTP, no auth)** - iubenda lets an AI assistant handle website legal compliance from start to finish: create and manage sites, generate privacy and cookie policies tailored to the services used, add data-processing services from iubenda's catalog, set up consent banners, draft terms and conditions, and run cookie scans to detect trackers.

```
Server type: Remote (Streamable HTTP)
Auth: None (per mcp.so listing FAQ)
Endpoint: https://mcp-server.iubenda.com/mcp
Tools: capability set served from the endpoint (live tool list not yet indexed)
Pricing: iubenda platform plans (trusted by 150,000+ businesses)
Category: Compliance
Built by: iubenda
```

## Why This Matters for Operators

Legal compliance is the highest-friction recurring task on a founder's plate: every new marketing pixel, third-party tool or site section changes what the policies must say, and getting it wrong carries GDPR and ePrivacy exposure. Most operators handle it with copy-paste templates that drift out of date within weeks.

**The mechanism is the value:** the agent can run cookie scans, detect what trackers actually load, and update the policies to match, keeping the legal layer in sync with the real site instead of a one-time snapshot. The same tools legal teams use (Consent Database, Compliance Monitor) back what the agent sets up.

## Tools & Capabilities

The live tool list is served from the endpoint; the listing documents these capability areas:

| Capability | Purpose |
|---|---|
| Site management | Create and manage sites under the iubenda account |
| Policy generation | Generate privacy and cookie policies from the services in use |
| Service catalog | Add data-processing services to the policy from iubenda's catalog |
| Consent setup | Configure cookie consent banners and CMP behavior |
| Terms drafting | Draft terms and conditions through natural language |
| Cookie scans | Detect trackers, then update policies as the site changes |

## Installation

```bash
claude mcp add iubenda --transport http https://mcp-server.iubenda.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "iubenda": {
      "type": "http",
      "url": "https://mcp-server.iubenda.com/mcp"
    }
  }
}
```

Coverage targets GDPR, ePrivacy, US state privacy laws and cross-market requirements. Account-level configuration happens in the iubenda dashboard; the MCP server operates against the connected account.

## Business Relevance

- **Founders** ship compliant privacy and cookie layers without manual policy maintenance
- **Agencies** manage compliance across client sites from chat
- **Developers** keep cookie consent in sync with what the code actually loads

## Integration with CorpusIQ

iubenda covers the legal layer that CorpusIQ's business-data connectors deliberately do not touch: CorpusIQ reads revenue, spend and customers, while iubenda keeps the site's consent and policy layer compliant. A composed workflow: a new marketing integration gets added in the stack, iubenda's agent-side cookie scan detects the new tracker, policies update, and CorpusIQ's connectors continue reading clean, consented data. For agencies running client portfolios, the two cover operations and compliance from one assistant.

## Limitations

- Capability list from listing prose; verify the live tools after connecting
- Commercial platform - policy generation is tied to iubenda plans
- No self-host option; the legal layer lives in iubenda's cloud
- Auth model listed as none, which may change as the endpoint matures

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [PolicyForge MCP - Legal Policies Generated and Audited from Your Codebase](/hermes/mcp/servers/external/policyforge-mcp)
- [mcp-sanctions - Watchlist Screening for KYC and AML](/hermes/mcp/servers/external/mcp-sanctions)
- [Fallax MCP - Phishing Simulation Results for Audit Evidence](/hermes/mcp/servers/external/fallax-mcp)
