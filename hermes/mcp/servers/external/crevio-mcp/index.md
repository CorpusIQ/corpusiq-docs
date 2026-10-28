---
title: "Crevio MCP - Delegate Business Work to an Agent"
description: "A hosted agent for products, orders, customers, email and sites, exposed as 20 MCP tools with a script runner over 3,000 connected apps."
category: Operations / Business Automation
stars: n/a (free plan, OAuth)
added: 2026-10-28
source: "live JSON-RPC probes on https://mcp.crevio.co/mcp answering initialize as crevio-api 2.0.0 on protocol 2025-06-18 with tools, resources and the skills, events and tasks extensions, the twenty tool names returned by tools/list, and the vendor documentation at crevio.co/docs/developer/mcp"
relevance: ★★★
tags: [business-operations, orders, customers, email, script-runner, approvals, audit-log, oauth, streamable-http]
last_updated: "2026-10-28"
---

# Crevio MCP

**The complaint about most business MCP servers is that they read and cannot act. Crevio is the opposite shape: it is an agent that already runs the shop, and the MCP server is the door into it rather than a read-only mirror of an API.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.crevio.co/mcp
Auth:        OAuth 2.1 with dynamic client registration
Tools:       20 (ask_crevio, run_script, resolve_approvals,
             list_audit_events, list_runs, get_run, ...)
Reach:       products, orders, customers, email, sites, marketing
Integrations: 3,000+ connected apps behind tools.<namespace>
Plans:       OAuth works on Free; API tokens need Business
```

## Why This Matters for Operators

There is a difference between an assistant that can answer a question about the shop and one that can do the work inside it. The first is a search box with better grammar. The second is the thing an owner actually wants at 11pm when a batch of orders has the wrong address and 40 customers are waiting.

Crevio's server is built around that second shape. `ask_crevio` hands a job to a separate agent that works the account through the Crevio API and the connected apps, then reports back with a result. `run_script` is the harder edge: it runs JavaScript with bun on the account's own computer, so a sequence of hundreds of calls happens in one step with no agent turn in between, and the script's return value becomes the answer.

The part that makes this safe enough to leave connected is the approval surface. A run that reaches a write it is not authorised for pauses in `needs_input` with pending approval ids, and `resolve_approvals` is the only way forward. Every account action also lands in `list_audit_events`, newest first, with API key use and tool calls at full capture.

## What It Returns, Verified

`initialize` answered HTTP 200 without credentials as `crevio-api` 2.0.0 on protocol `2025-06-18`, advertising tools, resources and three extensions: skills, events and tasks. `tools/list` returned twenty tools:

- **Delegation:** `ask_crevio` (job in, result out), `start_chat` (queue without waiting), `wait_for_run`, `get_run`, `cancel_run`, `resolve_approvals`
- **Scripting:** `run_script`, `wait_for_script_run`, `get_script_run`, `cancel_script_run`
- **Discovery:** `whoami`, `list_integrations`, `list_integration_tools`
- **History:** `list_chats`, `get_chat`, `send_message`, `list_messages`, `list_runs`, `list_audit_events`
- **Files:** `get_file_download_url`

Each tool carries read-only and destructive hints, so a client can gate the writes before they are attempted.

The script path is documented precisely enough to plan against: a script calls `tools.<namespace>.<function>(args)`, every call returns its result and throws on failure, top-level await works, and the last expression is the result. A run writes artifacts into `outputDir` (20 files at most, 50 MB each) which come back as `artifacts` and are exchanged for a download link with `get_file_download_url`, valid for 15 minutes.

Two operational details worth knowing before you lean on it: at most four script runs are in flight per user, and run ids do not expire. If a wait ends first the reply carries `wait_timed_out: true` and the run id, and calling `run_script` again runs it twice unless you reuse the `idempotency_key`. That is the one failure mode that costs money, so the pattern is always wait, then `wait_for_script_run` with the id.

## Limits Worth Recording

- **The OAuth surface is the free one.** OAuth 2.1 with dynamic client registration works on any plan including Free. API tokens (`Authorization: Bearer` or `X-Api-Key`) require the Business plan, so a script that pastes a key is a paid-path decision.
- **Tool discovery is anonymous, account work is not.** `tools/list` answered without credentials because it is static; a call against an account needs the OAuth session, so a keyless probe proves the server exists and says nothing about permissions.
- **The agent is a separate system.** `ask_crevio` runs Crevio's own agent, which means the quality of the outcome depends on that agent's judgement, not on the calling model. Treat it as delegating to a colleague with account access.
- **Approval is a setting, not a guarantee.** Writes pause by default, but the account can grant more autonomy, and once granted the pause does not occur.
- **Files are exchangeable, not stable.** An artifact link expires after 15 minutes. Anything that matters has to be downloaded or moved, not linked into a report.

## Wiring It Up

```json
{"type": "streamable-http", "url": "https://mcp.crevio.co/mcp"}
```

```bash
claude mcp add --transport http crevio https://mcp.crevio.co/mcp
```

Then call `whoami` first. It returns the account, the user, the credential behind the connection, the plan, credit balance and rate limits, which is the fastest way to tell a wrong-account connection from a broken one before blaming the tools.

## FAQ

### Does it need a paid Crevio plan?

No. OAuth 2.1 works on the Free plan. The paid path only appears if you want to authenticate with an API token instead of a browser session, which needs the Business plan.

### Can the agent change my store without asking?

By default a run pauses on writes with pending approvals, and `resolve_approvals` decides them. If the account has been granted more autonomy, the pause does not happen, so the setting is the control.

### What is the difference between ask_crevio and run_script?

`ask_crevio` delegates a job that needs judgement and writing, and can take minutes. `run_script` runs JavaScript deterministically against the API and every connected app in one step, which is the right tool for a data transformation or a bulk read.

### Can I see what it did afterwards?

Yes. `list_audit_events` returns access and configuration changes, approvals, API key use and, at full capture level, the agent's tool calls, newest first.
