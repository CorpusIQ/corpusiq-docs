---
title: Google Measurement MCP - GA4, Search Console and Tag Manager
description: The Google measurement stack for AI agents. One MCP server exposes GA4, Search Console and Tag Manager with 15 read tools always on and 9 write tools that stay invisible until explicitly enabled. Publish requires human confirmation and destructive operations do not exist in the codebase. Early v0.1.0.
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★★
tags: [ga4, search-console, tag-manager, analytics, google, oauth, self-hosted]
---

# Google Measurement MCP - GA4, Search Console and Tag Manager

**MCP server (stdio, Google OAuth)** - one self-hosted server that puts the three Google surfaces operators actually use - GA4, Search Console and Tag Manager - behind a single, safety-first tool set: 15 read tools always on, 9 write tools that do not exist in the tool list until the operator passes `--enable-write`, and destructive operations that are not implemented at all. Tag Manager publishing requires an explicit human confirmation, and updates merge instead of replace so a tag cannot be silently unwired.

```
Server type: stdio (self-hosted, Node)
Auth: Google OAuth (user flow or service account)
Endpoint: local (npx / node)
Tools: 24 (15 read always on, 9 opt-in write)
Pricing: free, open source - Google API quotas apply
Category: Data & Analytics
Built by: jabeer4148-ops (github.com/jabeer4148-ops/google-measurement-mcp)
```

## Why This Matters for Operators

Pointing an AI agent at your analytics is low-risk. Pointing one at a live Tag Manager container is not - a bad publish breaks tracking on every page of the site, and the raw GTM API has a trap the vendor verified against the live API: omitting `firingTriggerId` silently empties it, leaving a tag that looks normal in the UI and never fires. Most GTM MCP servers can publish containers and inherit that trap.

**This server makes the dangerous thing hard on purpose: write tools are absent unless explicitly enabled, publish prints the diff of what would go live and refuses without `confirm: true`, and delete, archive and removal operations do not exist in the codebase.** The merge-on-update behavior is the quiet engineering win: an agent changing a tag name carries over everything else, and the response lists `preservedFields` so the operator can see what survived.

It also consolidates what used to be three separate integrations: GA4 reporting, Search Console queries and sitemap inspection, and Tag Manager container reads in one credential.

## Tools & Capabilities

| Group | Tools | What they do |
|---|---|---|
| GA4 - read | `ga4_list_account_summaries`, `ga4_run_report`, `ga4_run_realtime_report`, `ga4_list_custom_dimensions`, `ga4_list_key_events` | Accounts and properties, flat-row reports, last 30 minutes realtime, custom dimensions with scope, key events with counting method |
| Search Console - read | `gsc_list_sites`, `gsc_search_analytics_query`, `gsc_list_sitemaps`, `gsc_inspect_url` | Site list, clicks and impressions with CTR and position, submitted sitemaps with warnings, index status for one URL (2,000/day per property) |
| Tag Manager - read | `gtm_list_accounts`, `gtm_list_containers`, `gtm_list_workspaces`, `gtm_list_tags`, `gtm_list_triggers`, `gtm_list_variables` | Accounts, containers (numeric id vs public GTM id), workspaces, tags with triggers, firing conditions, user-defined variables |
| Write (opt-in) | `ga4_create_custom_dimension`, `ga4_create_key_event`, `ga4_update_key_event`, `gsc_submit_sitemap`, `gtm_create_tag`, `gtm_update_tag`, `gtm_create_trigger`, `gtm_create_version`, `gtm_publish_version` | 9 tools, only present with `--enable-write`; publish requires `confirm: true` and prints the would-go-live diff |

Responses cap at 25 rows by default with a `truncated: true` flag and guidance to narrow the query. Not implemented by design: deleting key events, archiving dimensions, deleting sitemaps, tag/trigger/variable deletion, GSC site add/remove, GA4 property and data-stream mutation.

## Installation

```bash
npm install -g google-measurement-mcp
google-measurement-mcp
```

First run walks through creating a Google Cloud project, enabling the three APIs, configuring the consent screen, publishing the OAuth app (the vendor explicitly warns not to skip this step) and creating an OAuth client. Agencies and CI can use a service-account setup instead of the interactive flow.

## Configuration

```json
{
  "mcpServers": {
    "google-measurement": {
      "command": "google-measurement-mcp",
      "env": {
        "GOOGLE_CLIENT_ID": "your-client-id",
        "GOOGLE_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

Sign in once in the browser to mint the refresh token. To expose the 9 write tools, add `--enable-write` to the command - they are genuinely absent from the tool list until then, so an agent cannot see or attempt them.

## Business Relevance

- **Marketing operators** ask "what changed this week" against GA4 and Search Console in one chat instead of two consoles
- **SEO teams** inspect URLs and submit sitemaps through the assistant with read tools always safe
- **Agencies managing client containers** get publish-with-confirmation and merge semantics instead of raw replace
- **Operators burned by broken tracking** get a server that structurally cannot delete, archive or silently unwire a tag

## Integration with CorpusIQ

Google Measurement MCP extends the analytics surface CorpusIQ already serves: CorpusIQ's GA4 connector reads the same property data through its governed read-only layer, while this server adds Search Console and Tag Manager on the operator's own machine with the write surface explicitly opt-in. A composed workflow: CorpusIQ answers the business question (signups, revenue, cohort behavior) while the agent uses this server to inspect the GTM container that drives attribution, read Search Console visibility for the landing pages that convert, and stage a tag change the operator publishes manually.

## Limitations

- Early release (v0.1.0) - GA4 coverage is narrower than Google's official analytics-mcp, which the vendor recommends for GA4-only read use
- Self-hosted stdio only; no hosted endpoint
- Write tools require explicit opt-in, and publishing always needs human confirmation - deliberately slow
- Google API quotas (especially URL inspection at 2,000/day) apply unchanged
- New listing with no community track record yet

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
