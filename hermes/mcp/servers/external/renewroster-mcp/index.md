---
title: "RenewRoster MCP - Domain and SSL Renewal Roster"
description: "Remote MCP that tracks domain and SSL expiry across agency clients, with reminder schedules, alert channels, per-asset cost and a monthly renewal report."
category: Business Operations
stars: n/a (A2 Ventures product, 24 tools, API key)
added: 2026-10-31
source: "The mcpservers.org /all newest page on 2026-10-31 under the slug renewroster-com-docs-mcp, plus a keyless JSON-RPC tools/list probe on https://app.renewroster.com/mcp answering HTTP 401 with an invalid or missing API key message, the official MCP registry entry com.renewroster/renewroster at version 1.0.0 declaring a streamable-http remote, HTTP 200 reads on renewroster.com, renewroster.com/pricing and app.renewroster.com/login, and the repository github.com/raghuchinnannan/renewroster-mcp"
relevance: ★★★
tags: [domains, ssl, expiry-monitoring, agency, clients, renewals, alerting, webhooks, api-key, remote-mcp]
last_updated: "2026-10-31"
---

# RenewRoster MCP

**Every agency owns a list of things that expire, and the list lives in a spreadsheet that nobody opens until a client says their site is down. RenewRoster turns that list into a read surface an assistant can answer from, and it carries the one field the spreadsheet never has, who pays.**

```
Server type: Remote (Streamable HTTP, stateless)
Endpoint:    https://app.renewroster.com/mcp
Auth:        Authorization: Bearer rr_live_... (read-only or read + write key)
Limits:      60 requests/min on free, 300/min on paid
Tools:       24, write tools only present on a read + write key
Registry:    com.renewroster/renewroster 1.0.0 in the official MCP registry
Repo:        github.com/raghuchinnannan/renewroster-mcp
Built by:    A2 Ventures
```

A keyless `tools/list` answers **HTTP 401** with `invalid or missing API key or OAuth access token`, which is the expected state for a connector bound to an account, and the client configuration is one line:

```json
{
  "mcpServers": {
    "renewroster": {
      "type": "http",
      "url": "https://app.renewroster.com/mcp",
      "headers": { "Authorization": "Bearer rr_live_your_key" }
    }
  }
}
```

Claude Code takes the same thing as `claude mcp add --transport http renewroster https://app.renewroster.com/mcp --header "Authorization: Bearer ..."`, and the vendor publishes the config for Cursor, VS Code, Windsurf and Claude Desktop, the last through `mcp-remote` because a desktop config cannot send a header on its own.

## What it does

The surface splits into what an assistant can look up for free and what it can change on your behalf:

- **Lookups that touch nothing stored**: `lookup_domain` runs a live RDAP or WHOIS query on any domain, `lookup_cert` performs a live TLS check on a public host, and `lookup_ct` reads the latest certificate for a hostname from Certificate Transparency logs. None of the three saves anything, so an assistant can answer a one-off question without polluting the roster.
- **The roster reads**: `list_expiring` returns domains and certificates expiring within N days, expired ones included, defaulting to thirty; `list_assets` filters the whole tracked set by type, client, status and expiry window; `get_asset` returns one asset with its recent check history, and `get_asset_history` returns that history directly.
- **The agency view**: `list_clients` with asset counts, `get_agency` for plan, usage against limits and the API rate limit, `list_members` for team roles, `get_reminders` for the reminder schedule and `get_report` for a monthly renewal report by period.
- **Writes**: `add_domain`, `add_ssl_host`, `add_client`, `import_assets` for bulk work up to a thousand assets with a refusal if the import would pass the plan limit, `check_now` to force a re-check, `update_asset` to change client, who pays, auto-renew, cost, per-asset reminder days or the name, `delete_asset` marked destructive so clients that ask will ask, plus `set_reminders` and the alert channel and webhook tools down to `test_alert_channel`, which sends a real sample alert five times an hour at most.

## The field that makes this an operator surface

A generic expiry monitor already exists, and the catalogue carries one in [WatchCron MCP](/hermes/mcp/servers/external/watchcron-mcp/), which watches whether a job reports rather than whether a registration lapses. What separates this entry is the per-asset commercial data: `who pays`, `cost`, `auto-renew` and a client assignment, which is the difference between knowing that a certificate expires in nine days and knowing whether that expiry is your problem or a client's, what it costs, and whether anyone has been given the bill. `get_report` closes the loop with a monthly renewal report by period, which is the artefact an agency actually sends.

That is also why the write scoping matters more than usual here. An assistant holding a read + write key can add a thousand assets in one call and change what every asset costs, and the vendor's answer is a key type chosen at creation and a dashboard-only list that keeps billing, plan changes, checkout, member invitations, role changes and key creation out of the API entirely. The separation is correct and it is the first thing to test: whether a read-only key genuinely refuses `add_domain` rather than merely hiding the tool from the list.

## Where it sits beside the registrar and the certificate log

Three entries in this catalogue now touch the same object from three sides and none of them replaces another. [EuroDNS MCP](/hermes/mcp/servers/external/eurodns-mcp/) is a registrar API, so it acts on domains and certificates rather than watching them. [CTlogs.io MCP](/hermes/mcp/servers/external/ctlogs-mcp/) reads Certificate Transparency for subdomain discovery and certificate history, which is the security question. RenewRoster is the roster and the calendar, answering what expires, for which client, at whose expense, with reminders already scheduled. An operator with all three can ask a question none of them answers alone, and a careful one will notice that the registrar is where a renewal actually happens, so a roster that flags expiry still ends in a purchase somewhere else.

## What this pass did not establish

The endpoint is live and the credential contract is a bearer key, and that is the whole of what was driven: `tools/list` needs a key, so the tool names, the read and write split and the dashboard-only list are the vendor's published position and not a list this pass measured. Four things a trial should settle: whether the read-only key enforces read-only server-side, whether `import_assets` reports which rows were rejected rather than only failing the batch, whether the reminder schedule is per agency or per client, and what the free plan's asset ceiling is, since `get_agency` reads usage against a limit whose number the documentation does not state.

## FAQ

### Does it need a RenewRoster account?
Yes. An API key is created in the dashboard API tab and shown once, and the key type decides whether the assistant can only look or also change the roster.

### Which clients work?
Any client that speaks remote Streamable HTTP, which covers Claude Code, Claude Desktop through `mcp-remote`, Cursor, VS Code and Windsurf. The vendor publishes a config for each.

### Can the assistant delete a tracked domain?
Yes, with a read + write key, through `delete_asset`, which is marked destructive so clients that ask before destructive calls will prompt first.

### Does it renew anything?
No. It tracks expiry, checks live, schedules reminders and reports; the renewal itself happens at the registrar.

## See Also

- [EuroDNS MCP - Domain, DNS and SSL Registrar Operations](/hermes/mcp/servers/external/eurodns-mcp/) - the registrar where a flagged renewal is actually bought
- [CTlogs.io MCP - Certificate Transparency Search for Agents](/hermes/mcp/servers/external/ctlogs-mcp/) - the certificate history question beside the expiry question
- [WatchCron MCP - Know When a Job Stops Reporting](/hermes/mcp/servers/external/watchcron-mcp/) - monitoring silent failure rather than silent expiry
