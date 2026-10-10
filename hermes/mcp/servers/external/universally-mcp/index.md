---
title: "Universally MCP - Site Translation Management"
description: "Manage WordPress and Astro translations from your assistant: strings, languages, glossary rules and analytics, role-checked."
category: Business Operations
stars: n/a (new listing)
added: 2026-10-09
source: "mcpservers.org /all (October 9, 2026 evening sweep)"
relevance: ★★
tags: [translation, localization, wordpress, astro, glossary, multilingual, oauth, remote-mcp]
---

# Universally MCP

**Official MCP server for the Universally translation platform** - search strings and their translations, add or switch languages, manage glossary rules and read translation analytics, from any assistant. Read-only until you explicitly allow changes.

```
Server type: Remote (Streamable HTTP at https://mcp.universally.com/platform)
Auth: OAuth sign-in per workspace (or an X-API-Key header for scripted clients)
Tools: workspace and plan reads; sites; languages; translations; glossary; analytics
Safety: read-only by default - changes require ticking Allow changes at sign-in; no tool can delete anything; every call is checked against your workspace role
Category: Business Operations
Built by: Universally (universally.com)
```

## Why This Matters for Operators

A multilingual site accumulates translation work the way a garage accumulates boxes: strings waiting for review, languages switched on for a campaign and never cleaned up, a glossary that only one person knows. The operational questions - what is untranslated, what did the machine translate, what is actually being requested - normally take a dashboard tour.

Universally puts those questions in the assistant. **"Which strings in the German site are still untranslated" or "switch French on for this site" is now a sentence**, and the analytics read shows what visitors request in the last 24 hours. The permission model carries over from the platform: the assistant acts as you, within your role, and refuses changes unless you opted in at connection time.

## Tools & Capabilities

| Area | What the assistant can do |
|---|---|
| Workspace | Read the workspace name, settings, plan, its limits and usage |
| Sites | List sites, read one site, create a site, read install steps for its platform |
| Languages | List a site's languages, add a language, switch one on or off |
| Translations | Search strings, read all translations for a string, edit, approve or unapprove, machine-translate |
| Glossary | List glossary rules; create or edit a rule |
| Analytics | Read requests, translation activity and most requested URLs for the last 24 hours |

## Installation

```bash
claude mcp add --transport http universally https://mcp.universally.com/platform
```

Works with Claude (web and desktop), ChatGPT (developer mode), Cursor and VS Code; step-by-step guides are in the Universally docs. For scripted clients, create a workspace API key and send it as `X-API-Key`.

## Configuration and Safety

- Each connection is tied to one workspace, chosen at sign-in; add a second connection for a second workspace.
- Leave Allow changes unticked for read-only, or tick it so the assistant can also edit; without it every write tool is refused regardless of role.
- The assistant cannot delete anything and never sees private API keys.
- Machine-translating a string replaces its current translation (including a human-written one) and consumes prepaid words; edits go live as cached pages refresh.

## Business Relevance

- **Localization owners** see what is untranslated and what is being requested without dashboard tours.
- **Marketing teams** switch languages on for a launch and off afterwards from chat.
- **Site operators** keep glossary rules consistent by editing them where the discussion happens.
- **Agencies** run translation triage for client sites with role-scoped access.

## Integration with CorpusIQ

Translation work only pays off if the market is arriving. Universally manages the strings; CorpusIQ reports the traffic, queries and conversions by market from GA4 and Search Console, so "is the German site earning its keep" gets answered with both halves: what was translated and what it did. Business numbers from Stripe or Shopify complete the picture per region.

## Limitations

- Tied to the Universally platform and its plan limits (sites, prepaid words); it manages translations, it does not perform professional translation review.
- Machine translation replaces the current translation and is metered against prepaid words.
- Write access is opt-in per connection and constrained by workspace role.
- Newer connector; the tool set is young and evolving.

## FAQ

### Can the assistant make changes without my permission?

No. A connection is read-only by default; write tools stay refused until you tick Allow changes at sign-in, and even then they are checked against your workspace role.

### Does it work with WordPress and Astro sites?

Yes. The docs describe WordPress and Astro setups, and the assistant reads the install steps for a site's platform when you create one.

### Can the assistant delete a language or a translation?

No. There is no delete tool; deletion stays in the Universally dashboard.

## See Also

- [WPPilot MCP - WordPress, Elementor and WooCommerce](/hermes/mcp/servers/external/wppilot-mcp/)
- [Elementor MCP Server - WordPress Website Automation](/hermes/mcp/servers/external/elementor-mcp-server/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
