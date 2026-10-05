---
title: "Sitegoalie MCP - WordPress Operations for Agencies"
description: "Read client WordPress site status from any MCP client and run Safe Updates, client reports and work logs when the workspace allows, with auto-rollback."
category: Business Operations
stars: n/a (hosted platform, sitegoalie.com)
added: 2026-10-05
source: "chatmcp/mcpso issue #4758 (com.sitegoalie/sitegoalie)"
relevance: ★★★
tags: [wordpress, agencies, website-management, monitoring, uptime, updates, remote-mcp]
---

# Sitegoalie MCP

**The maintenance dashboard for agencies that look after WordPress sites, in the conversation.** Sitegoalie is a hosted dashboard for agencies running client WordPress fleets: updates, uptime, PHP errors, broken links, performance, work logs and client reports. Its MCP server exposes 17 tools so an assistant can read that status across sites and, when the workspace allows changes, run a Safe Update, send a client report, run a performance test or log work.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (Claude.ai, ChatGPT connectors) or a Sitegoalie API token
Endpoint: https://app.sitegoalie.com/mcp
Tools: 17 (read-only by default; write tools appear only when the connection may change the site)
Safety: Safe Updates take a backup first, test checkout, forms and wp-admin, and roll back automatically on failure
Pricing: Free plan for one site; the API and MCP server are on paid plans with a 14-day Pro trial
Built by: sitegoalie.com
```

## Why This Matters for Operators

Agencies manage maintenance as a stream of small, risky actions across many sites, and the useful question is rarely "what is the status" alone; it is "what is pending, what is broken, and can I safely push the update". Sitegoalie's read tools answer the first part per site (pending updates, issues, uptime, PHP errors, broken links, performance, work entries, client reports), and its write tools answer the second inside explicit limits: writes only exist when the connection is allowed to make them, and Safe Updates back up first, test checkout, forms and wp-admin, and roll back automatically if something fails.

## Tool Surface

| Tool | Purpose |
|---|---|
| get_account, list_sites, get_site | Account and per-site overview |
| list_pending_updates, list_issues | Update backlog and detected issues |
| get_uptime, list_php_errors, list_broken_links, get_performance | Health readouts |
| list_work_entries, list_client_reports | Work log and client reports |
| get_update_job | Status of an update job |
| run_safe_update | Backup, test, and roll back on failure |
| send_client_report, run_performance_test, log_work_entry, delete_work_entry | Write actions, gated by the workspace |

Owners and admins choose the workspace and whether the connection is read or read-write when connecting; read-only is the default.

## Authentication

Two paths:

- **Claude.ai and ChatGPT**: add the server as a custom connector and sign in with OAuth.
- **Claude Code, Cursor, VS Code**: use an API token from the Sitegoalie dashboard, attached as a bearer credential in the Authorization header, with this connection shape:

```json
{
  "mcpServers": {
    "sitegoalie": {
      "type": "http",
      "url": "https://app.sitegoalie.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_SITEGOALIE_TOKEN"
      }
    }
  }
}
```

The endpoint is published in the official MCP Registry as `com.sitegoalie/sitegoalie`.

## Installation

```bash
claude mcp add --transport http sitegoalie https://app.sitegoalie.com/mcp
```

Then connect a workspace and choose read or read-write access. A Sitegoalie account is required; the free plan covers one site, and the MCP server itself is on paid plans with a 14-day Pro trial.

## Business Relevance

- **Agencies** check every client site's status in one conversation instead of opening each dashboard.
- **Maintenance operators** run Safe Updates with an automatic rollback path instead of doing risky updates by hand.
- **Client reporting** turns the work log into a report that can be sent from the same session.

## Integration with CorpusIQ

Agency operations and client analytics are two halves of the same account review. Sitegoalie reports what is happening on the WordPress side (updates, uptime, performance, work done), while CorpusIQ's connectors read the analytics, search and revenue side, so a monthly client update can pair "what we maintained" with "what it drove" in one pass.

## Limitations

- Requires a Sitegoalie account; the MCP server is not on the free plan (the free plan covers one site in the dashboard).
- Write tools depend on the workspace setting chosen at connect time; a read-only connection cannot run Safe Updates.
- The tool list is vendor-published and stable, but check the connect-time schema for argument details.
- Client reports and work entries are agency-facing records; nothing here publishes to the client site beyond what the workspace permits.

## FAQ

### Do I need write access to be useful?

No. Read-only is the default and covers status, updates, issues, uptime, errors, broken links, performance, work logs and client reports across every site in the workspace.

### What makes a Safe Update safe?

It takes a backup first, tests checkout, forms and wp-admin after updating, and rolls back automatically if the tests fail.

### Which plans include the MCP server?

The dashboard has a free plan for one site; the API and MCP server are on paid plans, and a 14-day Pro trial is available.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [WPPilot MCP - WordPress, Elementor and WooCommerce](/hermes/mcp/servers/external/wppilot-mcp/)
- [Elementor MCP Server - WordPress Website Automation](/hermes/mcp/servers/external/elementor-mcp-server/)
- [Pixelesq MCP - Website Management and SEO for Agents](/hermes/mcp/servers/external/pixelesq-mcp/)
