---
title: "Cronitor MCP - Cron and Uptime Monitoring from Chat"
description: "The official hosted Cronitor MCP server: create, update, pause and inspect heartbeat, job and HTTP checks, and read a failing-monitor rollup from chat."
category: Business Operations
stars: ★★ (official vendor, OAuth gate, tools documented not driven)
added: 2026-11-02
source: "the chatmcp/mcpso submission #6648 filed 2026-11-03T03:30:19Z, a keyless probe of https://cronitor.io/mcp answering HTTP 401 with protected-resource metadata at https://cronitor.io/.well-known/oauth-protected-resource/mcp, the vendor tool reference at cronitor.io/docs/mcp-server, and the official registry listing io.cronitor/cronitor recorded there as publication pending"
relevance: ★★★
tags: [monitoring, cron, heartbeat, uptime, status-pages, incidents, alerts, oauth, official, remote-mcp]
last_updated: "2026-11-02"
---

# Cronitor MCP

**A scheduled job fails quietly. Nothing throws, nothing pages, and the first person to notice is the customer looking at last week's numbers. The only defence is a deadline someone else is holding, and the second problem is that the deadline usually lives in a dashboard nobody opens until something breaks.**

```
Server type:  Remote (Streamable HTTP, JSON responses)
Endpoint:     https://cronitor.io/mcp
Auth:         OAuth 2.1, authorization code with PKCE
Client ID:    Client ID Metadata Document (CIMD), no dynamic registration
Fallback:     Cronitor SDK Integration key as a Bearer token
Sessions:     none, the server never issues Mcp-Session-Id
Tools:        71 per the vendor tool reference
Published:    MCP Server Card at /mcp/server-card, catalog at /.well-known/ai-catalog.json
Registry:     io.cronitor/cronitor, recorded as publication pending
```

## What it does

The hosted server is a control plane over the Cronitor account an operator already has. It creates monitors, reads their state, pauses alerting, triages issues and manages status pages and components, notification lists, groups and environments.

The tools fall into three groups, as the vendor documents them:

| Group | What it covers |
| --- | --- |
| Task-oriented tools | `setup_monitor`, `get_status`, `get_setup_context`, `list_failing_monitors`, `pause_monitor`, `unpause_monitor` |
| Discovery tools | `describe_monitor_assertions`, `describe_site_query`, `list_issue_assignees` |
| Resource operations | 64 operations that mirror the CronitorCLI resource tree: monitors, status pages and components, issues, notification lists, groups, environments and read-only metrics |

The vendor states **71** tools in total and each input schema declares `additionalProperties: false`, so an unknown field is rejected rather than ignored. Read the live `tools/list` for the exact inventory in the account you connect, since the page's own category counts and its named tool list do not add up to the same number.

`setup_monitor` is the one that changes how an agent works with a schedule. It takes a stable `key`, a `type` of `heartbeat`, `job` or `check`, a cron expression or an interval such as `every 30 minutes`, an IANA `timezone`, notification destinations and, for heartbeats and jobs, a `grace_seconds` allowance after the expected time. Repeating the same call updates the monitor instead of creating a second one, which is what makes it safe to put in a runbook: the agent converges the account on the description rather than accumulating duplicates. Every monitor it creates is tagged `via:mcp`, so the ones an agent made are separable from the ones a human made.

`get_status` with no key returns the account rollup, `{total, healthy, failing, paused, failing_monitors}`, with at most 25 failing monitors named. `list_failing_monitors` returns key, name, type, tags, `failing_since` and `latest_alert_reason` for one environment, and it distinguishes an empty account from a healthy one in a message rather than returning a bare zero.

`get_setup_context` takes no arguments and returns what an agent needs before it configures anything: the organization, the plan with its monitor allowance and minimum check interval, the default environment, notification list and timezone, the telemetry URL base and the name of the environment variable holding the SDK key. It never returns the key itself.

## The line the vendor draws, and it is the right one

Telemetry does not travel through MCP. The vendor's documents are explicit: the MCP server configures and inspects, and the workload reports its own state through CronitorCLI, an SDK, or a direct call to the returned `ping_url`. Sending a heartbeat from the MCP connection would mean the monitor goes quiet exactly when the agent does, which is the failure mode it exists to catch.

For a bounded job the same rule applies with more detail: report the lifecycle, `run` then `complete` or `fail`, not one successful request. An agent that reports "done" through the same channel that scheduled the work has not built a monitor, it has built a mirror.

The one exception in the tool set is instructive: `type=check` inverted the direction. Cronitor probes the target, so `setup_monitor` returns a `monitor_url` and probe instructions instead of a ping URL, and the assertion syntax can be discovered with `describe_monitor_assertions`. The vendor publishes a recipe for monitoring an MCP server itself by POSTing `tools/list` as an HTTP check with assertions on the response, which is the neatest thing in the documentation: an agent can watch the MCP servers it depends on with the same tool it uses to watch crons.

## What this pass measured, and what it did not

A keyless `initialize` against `https://cronitor.io/mcp` returned **HTTP 401** with `WWW-Authenticate: Bearer resource_metadata="https://cronitor.io/.well-known/oauth-protected-resource/mcp"`, which is a live, auth-gated server rather than a parked domain. No tool was called, because the connection needs an account. Everything in this guide about behaviour comes from the vendor's own tool reference, and it is labelled that way rather than written as a driven session.

The operational details that reference carries, and that matter before you connect:

- **OAuth without dynamic registration.** The authorization server supports authorization code with PKCE and identifies clients by a Client ID Metadata Document. Dynamic client registration is **not** enabled, so a client that only knows how to self-register will fail here and a client that speaks CIMD will work. The vendor calls other standards-compliant clients best-effort.
- **No sessions.** The server never issues `Mcp-Session-Id`, and it supports the `2026-07-28` stateless revision alongside `2025-03-26`, `2025-06-18` and `2025-11-25`.
- **Permissions follow the human, not a scope.** An OAuth token carries no scope selection: every request receives exactly what that user's Cronitor role allows, capped at the SDK Integration bundle. OAuth never grants API key, team, billing or administration permissions, and it does not add a ping tool. Role changes, removal from the organization and disabling MCP for the organization all take effect on the next request rather than at token expiry.
- **Redaction is on by default.** Monitor request headers, cookies and bodies are omitted from MCP results, and credential-bearing monitor URLs are replaced with `[REDACTED URL]`, including inside YAML exports. `update_monitor` preserves omitted nested request fields and rejects an edited redaction marker, so a read-then-write loop cannot silently blank a credential, and changing a URL's origin requires replacing or clearing the populated credentials explicitly.
- **Plan limits are errors, not silent downgrades.** A monitor over the account's quota is saved but disabled, with `monitor_quota` in the response, and a plan-limit violation returns `code`, `message` and `upgrade_url` so the agent can show the human the upgrade path instead of retrying.
- **Rate limits are per account, split read and write.** The error carries `limit`, `window_seconds` and `retry_after_seconds`, and the vendor's own instruction is to wait the stated time rather than retry, because the counter resets at the window boundary. Permission errors carry `required_scope`; protocol header mismatches return `-32020` and unsupported versions `-32022`.

## Two servers, and a third that is not this one

Cronitor ships **two** MCP servers and they do different jobs. The hosted one at `cronitor.io/mcp` manages account resources from anywhere and cannot see the machine's crontab. The **local CronitorCLI MCP server** runs on the host, can read and edit that host's crontabs, and syncs those local jobs into Cronitor. An operator who wants an agent to change a schedule on the box needs the local one; the hosted one will not do it, and it does not pretend to.

There is also a third-party wrapper in the official registry, `io.usefulapi/cronitor` at `cronitor.usefulapi.io/mcp`, which is not the vendor's server. The vendor's own entry is `io.cronitor/cronitor`, recorded on its documentation page as publication pending at the time of this pass. Match on the endpoint, not on the name.

## Where this sits in the catalog

Four catalogued servers watch jobs and none of them can change one. [WatchCron MCP](/hermes/mcp/servers/external/watchcron-mcp/) watches cron schedules, [healthchecks MCP](/hermes/mcp/servers/external/healthchecks-mcp/) is the dead man's switch for a heartbeat, [RealUptime MCP](/hermes/mcp/servers/external/realuptime-mcp/) covers uptime, status pages and outage checks, and [HostTracker MCP](/hermes/mcp/servers/external/hosttracker-mcp/) watches hosts. The November 2 midday pass held a submission, `norc`, against exactly that class and noted that the group monitors jobs rather than editing them, so a server that creates and configures monitors from chat was worth a second look.

This is that second look, with a caveat stated plainly: the hosted server configures the monitoring account, not the crontab. It is the official vendor surface for the platform, it is OAuth-gated behind the operator's own login, and the 71-tool resource tree means an agent can manage environments, groups and status pages as well as monitors. What it does not do is change what runs on the box. That is the local CronitorCLI server's job, and it is a separate connection.

## Connect it

OAuth on an interactive client, so the operator approves access in a browser and no key is pasted into a chat.

```json
{
  "mcpServers": {
    "cronitor": {
      "type": "http",
      "url": "https://cronitor.io/mcp"
    }
  }
}
```

Claude Code, as the vendor documents it:

```bash
claude mcp add --transport http --scope user cronitor https://cronitor.io/mcp
```

For a headless client, the fallback is the account's existing **SDK Integration** key sent as a Bearer token in an environment variable. That credential is organization-wide and long-lived, and rotating it interrupts every CronitorCLI and SDK installation still holding the old value, so update the consumers together rather than treating it as an MCP-only key. The vendor states there is no dedicated MCP key type.

The vendor also publishes an agent skill that teaches an agent to audit, add and investigate monitoring: `npx skills add cronitorio/agent-skills`, from the MIT repository `github.com/cronitorio/agent-skills`.

## Do not use it as

- **A telemetry channel.** Never report a job's completion through MCP. Use the ping URL or the CLI, so the deadline survives the agent.
- **A monitor for the thing that runs the monitor.** The agent's own availability is a separate problem; the hosted server going quiet is not an alert you will receive from inside it.
- **A read of the machine's crontab.** Only the local CronitorCLI server can do that.
- **An expansion of what a user can do.** The token carries the user's role and nothing more, by design.

## FAQ

### Is there a free plan?
Cronitor has a free tier and the tool set reports the account's plan and limits in `get_setup_context`, so an agent can check before it creates anything.

### Can an agent read my secrets through this?
The documentation states that request headers, cookies and bodies are omitted and credential-bearing request URLs are redacted, including in YAML exports and in error payloads. Event messages, captured command output and status-page configuration can still carry customer data, so the vendor's advice is to request expanded fields only with the human's approval.

### Why did my client fail to connect?
Most likely dynamic client registration. The authorization server identifies clients by Client ID Metadata Document and does not enable DCR.

### Does the OAuth token expire mid-run?
Role and organization changes apply immediately, ahead of token expiry. For a long-running automation, plan for the token to be re-authorized the same way any other OAuth client is.

### Can it monitor another MCP server?
Yes, and the vendor documents the recipe: an HTTP check that POSTs a `tools/list` request with assertions on the response.
