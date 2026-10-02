---
title: AdPlug LinkedIn Ads MCP - B2B Campaign Control for Agents
description: Hosted LinkedIn Ads connector for B2B demand-gen teams. Full read and guarded write across campaigns, campaign groups, creatives, saved audiences, lead forms and conversions, with multi-account support, audience-size estimation before targeting commits, 5,000-event conversion batches hashed server-side, and a preview step before every mutation. OAuth 2.1.
category: Marketing
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★★
tags: [linkedin-ads, ppc, demand-gen, b2b-marketing, campaign-management, conversions, ad-platforms, remote-mcp]
---

# AdPlug LinkedIn Ads MCP - B2B Campaign Control for Agents

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - a hosted LinkedIn Ads connector from AdPlug (adplug.app) built for B2B teams watching CPL closely: an agent reads campaigns, audiences, creatives, lead-gen forms and conversions across every ad account the operator can touch, diagnoses what changed, and prepares updates through a preview step before anything runs. Secure LinkedIn sign-in, platform tokens encrypted at rest, and an audit trail of every change.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (LinkedIn sign-in, tokens encrypted at rest; URL-token mode also available)
Endpoint: https://api.adplug.app/mcp
Tools: Read plus guarded write across campaigns, audiences, creatives, lead forms, conversions and account discovery (multi-account)
Pricing: Free to start via adplug.app signup, then paid plans (pricing page at adplug.app)
Category: Marketing
Built by: AdPlug (adplug.app)
```

## Why This Matters for Operators

LinkedIn is where B2B teams spend serious money to reach specific buyers, and where campaigns drift the fastest - analysis takes too long, so budgets run against burnt-out audiences. AdPlug's connector removes that lag: the agent reads the last 90 days of audiences, creatives and conversions and produces the first pass while the problem is still fresh, from one question instead of a Campaign Manager session.

**The safety model is preview-first: every mutation - new campaign groups, campaigns, creatives, saved audiences, budget and targeting changes - renders as a reviewable API call before it executes, and every action lands in an audit trail with user, account, outcome and timestamp.** Multi-account is the default rather than an enterprise add-on, so agencies get every client account in one surface. Targeting research estimates audience size before a campaign commits, catching the tiny audience before the budget does. The conversion tool batches up to 5,000 events per call, hashes PII server-side, and posts to LinkedIn's Conversions API - offline and CRM-sourced events included.

AdPlug runs the same connector architecture for Google Ads, so teams can compare LinkedIn cost per lead against paid search for the same offer from one chat.

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Account discovery | Lists every LinkedIn ad account where the operator has admin or campaign manager access |
| Unified analytics | Pulls performance for any pivot - campaign, creative, daily, conversion, lead-gen, audience, reach |
| Browse entities | Lists or gets campaigns, creatives, campaign groups, conversions, lead forms, saved and targeting audiences in plain English |
| Targeting research | Searches targeting options and estimates audience size before saving |
| Campaign building | Creates campaign groups, campaigns, creatives and saved audiences; every change previewed before it runs |
| Updates | Pauses, edits and adjusts budgets or targeting with a preview step before anything touches the account |
| Conversion events | Sends up to 5,000 conversion events at once via LinkedIn CAPI; sensitive fields protected before they reach LinkedIn |
| Audit trail | Records user, account, action, outcome and timestamp for client reporting |

## Installation

Connect through the AdPlug app at adplug.app/signup (LinkedIn OAuth sign-in), then add the endpoint to any MCP client. Claude, Claude Code, ChatGPT, Codex, Cursor, VS Code, GitHub Copilot, Windsurf and Antigravity are all supported per the vendor docs.

```bash
claude mcp add --transport http adplug-linkedin https://api.adplug.app/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "adplug-linkedin": {
      "type": "http",
      "url": "https://api.adplug.app/mcp"
    }
  }
}
```

The endpoint requires OAuth 2.1 bearer auth or a per-connection URL token; the browser sign-in against AdPlug (which holds the encrypted LinkedIn platform token) completes on first use.

## Business Relevance

- **Demand-gen teams** get CPL movement explained by job seniority, audience fatigue spotted by engagement decline, and preview-gated updates without Campaign Manager.
- **PPC agencies** run every client account from one multi-account surface with an audit trail ready for the day a client asks what changed.
- **Marketing operations** batch offline and CRM-sourced conversions with server-side PII hashing instead of manual uploads.
- **Founders running their own LinkedIn spend** get senior-level first-pass analysis and safe, reviewable changes.

## Integration with CorpusIQ

AdPlug reads and edits the paid-acquisition surface; CorpusIQ reads the business those campaigns feed. A composed workflow: the agent pulls revenue and pipeline evidence from CorpusIQ's HubSpot or Salesforce connectors, then asks AdPlug's LinkedIn connector for cost per lead by audience and creative over the same window - paid spend and downstream revenue in one comparison, instead of a marketer pasting exports together. For lead-gen campaigns, CorpusIQ's Stripe and QuickBooks connectors show which converted leads became revenue, feeding the audience and creative decisions the agent proposes through AdPlug's preview step. Both systems keep the human as approver: AdPlug previews every write, CorpusIQ stays read-only.

## Limitations

- Brand new to this catalog (mcpservers.org listing, no public repo or star history to assess).
- Commercial cloud service - no self-hosting; credentials flow through AdPlug's platform.
- Free to start with paid plans beyond; enterprise features (team seats, MCC reporting) are positioned for the paid tiers.
- LinkedIn's API access reviews are handled by AdPlug, but campaign changes still carry platform-side approval and review limits.
- Tool names are not published in vendor docs; the live tool list is served from the endpoint after sign-in.

## See Also

- [Ryze Meta Ads MCP - Hosted Facebook Ads for Agents](/hermes/mcp/servers/external/ryze-meta-ads-mcp)
- [Ryze Google Ads MCP - Hosted Ads Reporting for Agents](/hermes/mcp/servers/external/ryze-google-ads-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
