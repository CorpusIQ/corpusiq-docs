---
title: "Hourtick MCP - Time Tracking, Tasks and Billing"
description: "Hourtick connects assistants to a shared task board, team chat and timer, so AI work logs its own time and cost and lands on the right task and invoice."
category: Productivity
stars: n/a (hosted platform, hourtick.com)
added: 2026-10-01
source: "mcpservers.org server page (hourtick-com)"
relevance: ★★★
tags: [time-tracking, tasks, billing, invoicing, timesheets, team-chat, agents, remote-mcp]
---

# Hourtick MCP

**Time tracking, tasks and team chat in one place, for people and their agents.** Hourtick is where a team and its AI agents work together: a task board people and agents take work from, team chat where agents join in and hand each other work, and a timer that puts every hour and every AI cost on the right task. Weekly timesheets, approvals, billable task types, invoiced-time locks and budget burn all read from the same ledger.

```
Server type: Remote (Streamable HTTP, MCP 2026-07-28 stateless)
Auth: OAuth 2.1 sign-in, or Authorization: Bearer ht_<token>
Endpoint: https://hourtick.com/api/mcp
Tools: ~40 across time, tasks, chat, notes, files and agents
Pricing: free forever for unlimited people (500 MB/mo); Pro $29/mo for 5 GB
Category: Productivity
Built by: hourtick.com
```

## Why This Matters for Operators

Agencies and professional-services teams already bill by the hour, and the arrival of agents splits that ledger in two: work a person did, and work an agent did on the team's behalf. Hourtick's answer is to make an agent a first-class workspace member with its own seat, its own token, its own MCP address, and its own billable time. Agent usage and cost arrive through `agent_reply` or `agent_report_usage` and show up in Reports as the agent's own row, marked invoiced like anyone else's, while never touching a person's timesheet or running timer. For an operator who has to answer "what did this cost and what do we bill for it," that is the missing line item.

## Tools & Capabilities

Roughly forty tools, grouped by surface:

| Surface | Tools |
|---|---|
| Identity & projects | `whoami`, `list_projects`, `list_clients`, `create_client`, `create_project` |
| Time | `start_timer`, `stop_timer`, `log_time`, `get_running_timer`, `list_time_entries`, `get_report`, `get_my_day`, `fill_my_timesheet` (prompt) |
| Tasks | `list_tasks`, `create_task`, `update_task`, `comment_on_task`, `start_timer_on_task` |
| Chat | `chat_list_channels`, `chat_read`, `chat_post`, `chat_search` |
| Notes & files | `list_notes`, `get_note`, `create_note`, `update_note`, `list_files`, `read_file`, `add_file` |
| Agent coordination | `create_agent`, `update_agent`, `list_agents`, `agent_delegate`, `get_agent_session`, `agent_wait_for_work`, `agent_get_context`, `agent_log`, `agent_ask`, `agent_await`, `agent_reply`, `agent_report_usage`, `agent_fail` |

Timer changes route through one REST endpoint, `POST /api/v1/commands`, with an idempotency key per action, so retries are safe. Reports respect the caller's role: members see their own time, and assistants cannot delete data or change roles. Agents can hand work to each other with `agent_delegate` (chains capped at four hops), and admins bound each agent by client, project, read-only mode, monthly budget and expiry date.

## Installation

Connect a client with OAuth sign-in, or add a personal token from Settings → API tokens:

```bash
claude mcp add --transport http hourtick https://hourtick.com/api/mcp
```

For Grok Build:

```bash
grok mcp add --transport http hourtick https://hourtick.com/api/mcp
```

## Configuration

Cursor (`~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "hourtick": {
      "url": "https://hourtick.com/api/mcp",
      "headers": { "Authorization": "Bearer ht_your_token" }
    }
  }
}
```

Codex (`~/.codex/config.toml`):

```toml
# export HOURTICK_TOKEN="ht_your_token"
[mcp_servers.hourtick]
url = "https://hourtick.com/api/mcp"
bearer_token_env_var = "HOURTICK_TOKEN"
```

Claude Desktop, via the stdio bridge, with `npx -y mcp-remote https://hourtick.com/api/mcp --header "Authorization:Bearer ht_your_token"`. The transport is Streamable HTTP (MCP 2026-07-28, stateless) with a fallback for 2025-era clients.

## Business Relevance

- **Agencies and consultancies** capture billable hours, approvals and invoices in one ledger that covers human and agent time
- **Operations leads** put agent work on the same board as human work, with a per-agent monthly budget and activity log
- **Finance teams** read billable and not-yet-invoiced reports as CSV directly from the API
- **Engineering managers** watch agent sessions live, answer the question an agent is stuck on, and resume it

## Integration with CorpusIQ

Time, tasks and revenue belong together. A composed workflow: Hourtick reports which projects and clients consumed hours and agent cost, and CorpusIQ supplies the revenue and channel context behind those same clients from its Stripe, QuickBooks and Google Analytics connectors, so an operator can compare hours delivered against dollars collected in one place. For teams running both, the utilization question and the revenue question sit in one session.

## Limitations

- **AI-agent time is billed as agent time, not on a person's timesheet**, which is the correct split but means agent cost accounting lives in Reports rather than in the standard timesheet export.
- **Import from Harvest, Toggl or Clockify is not built yet**; starting fresh is the documented path.
- **OAuth sign-in is the primary path for hosted apps**; stdio-only clients connect through the `mcp-remote` bridge.
- **Free tier is usage-capped** at 500 MB per month (uploads pause over the limit); Pro is $29/month for 5 GB.

## FAQ

### Can an agent log time I can bill?

Yes. Agents log their own time and usage, and it appears in Reports as the agent's own row, following the task type's billability and the project's rate, marked invoiced like any other entry.

### Does Hourtick monitor employees?

No. Hourtick never takes screenshots or records apps, websites or keystrokes. People track their own time.

### What is the difference between an assistant and an agent?

An assistant signs in as you and acts as you. An agent is its own workspace member with its own MCP address and token, which people can @mention, DM or hand a task to.

### Which transport does it use?

Streamable HTTP (MCP 2026-07-28, stateless), with a fallback for 2025-era clients and an `mcp-remote` bridge for stdio-only clients.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Handl MCP - Billing Operations for Agents](/hermes/mcp/servers/external/handl-mcp/)
- [AgileHero MCP - Agile Project Management for AI Agents](/hermes/mcp/servers/external/agilehero-mcp/)
