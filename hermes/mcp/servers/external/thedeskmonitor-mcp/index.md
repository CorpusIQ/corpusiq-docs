---
title: "TheDeskMonitor MCP - Workforce Analytics from Chat"
description: "Ask who is clocked in, where hours go and what work costs - 24 live workforce tools over MCP, with a no-account demo mode."
category: Operations
stars: n/a (hosted platform, thedeskmonitor.com)
added: 2026-10-05
source: "mcpservers.org /all"
relevance: ★★
tags: [workforce, time-tracking, productivity, teams, operations, demo-mode, api-key, remote-mcp]
---

# TheDeskMonitor MCP

**"Who is clocked in?" is a question now answered in the chat box.** TheDeskMonitor is workforce productivity and cost intelligence for small teams: automatic time tracking, workload views and dashboards, with a native MCP server of 24 live tools. An assistant can read the dashboard, employees, timesheets, approvals, activity and analytics, and run the operational basics (clock in, clock out, invite staff) with confirmation. Setup claims under five minutes, and a public demo key lets anyone explore a synthetic company with no account at all.

```
Server type: Remote (Streamable HTTP; mcp-remote bridge for stdio-only clients)
Auth: API key - dm_demo_public for the synthetic demo, dm_live_ keys for your tenant
Endpoint: https://api.thedeskmonitor.com/api/mcp/v1/
Tools: 24 (dashboards, employees, timesheets, approvals, alerts, analytics, attendance)
Scope: Tenant-scoped - employees see their own records, managers their team, admins the tenant
Built by: TheDeskMonitor
```

## Why This Matters for Operators

Workforce questions are constant and small: who is working right now, who is overloaded, where last week's hours went, which approvals are waiting. Each one traditionally costs a dashboard login. With the MCP tools, the same questions are typed or spoken to whatever assistant the manager already uses, and the answers come from the live tenant data rather than a stale export. The cost-intelligence angle matters too: hours are the largest controllable cost in most service businesses, and seeing them next to workload and projects is where the decisions are.

**Try before you buy, literally.** The demo key `dm_demo_public` works with no account against a synthetic 8-person company, so an operator can test the whole surface, then swap in a `dm_live_` key from Settings, API Keys to see their own tenant. Write actions (clock in, clock out, invite staff) are flagged for confirmation in clients that support it.

## Tools

24 tools, including:

| Tool | What it does |
|---|---|
| `get_dashboard_summary` | The workforce overview: who is in, load, recent activity |
| `list_employees`, `get_employee_details` | The team roster and one person's details |
| `list_my_timesheet` | Your own time entries |
| `list_pending_approvals` | Approvals waiting on a decision |
| `list_recent_activity` | What happened lately across the tenant |
| `get_workload_alerts` | Who is overloaded or underused |
| `get_productivity_overview` | Productivity read for the team |
| `summarize_team_hours` | Team hours summarized for a period |
| `clock_in`, `clock_out` | Attendance actions, confirmation-flagged |
| `invite_staff` | Invite a person into the tenant, confirmation-flagged |
| `get_capabilities` | What this key and account may do |
| `get_pricing_and_plans`, `start_free_trial` | Plan details and a trial start link |
| `get_data_dictionary`, `get_demo_scenarios`, `get_analytics_questions` | How the data is shaped, demo tasks, and questions to try |
| `get_analytics_overview`, `get_analytics_feature_usage` | Usage and feature analytics |

Analytics and discovery tools are active in demo mode; live mode adds the full set including attendance writes.

## Installation

Claude Desktop uses the mcp-remote bridge:

```json
{
  "mcpServers": {
    "deskmonitor": {
      "command": "npx",
      "args": ["-y", "mcp-remote@latest",
        "https://api.thedeskmonitor.com/api/mcp/v1/",
        "--header", "Authorization: Bearer dm_demo_public"]
    }
  }
}
```

Swap `dm_demo_public` for your `dm_live_` key to reach real data. Cursor, Windsurf and Claude Code take the remote URL directly; the vendor also ships a connector installer that auto-configures supported clients, and the first live-key connection shows one consent screen.

## Business Relevance

- **Founders and managers** get "who is working, who is overloaded" answers without opening another dashboard.
- **Agencies** check timesheets and pending approvals between meetings, by chat.
- **Ops leads** watch productivity and workload trends against projects to spot resourcing problems early.
- **Anyone evaluating** tests the whole thing with the public demo key before creating an account.

## Integration with CorpusIQ

Workforce data answers "what did it cost in time"; CorpusIQ answers "what did it earn". CorpusIQ reads the financial and marketing systems (Stripe, QuickBooks, GA4, ads) while TheDeskMonitor reads the team's hours and load. Together an operator can look at a project's hours from one side and its revenue and acquisition cost from the other, each read-only from the agent's side, with the comparison happening in the answer.

## Limitations

- Live mode requires a TheDeskMonitor account and a `dm_live_` key; the demo is synthetic and read-only.
- The demo key is public and shared: treat its data as a sandbox, never for real reporting.
- Write actions are limited (attendance, invites) and confirmation-flagged; deeper HR actions stay in the app.
- Claude Desktop needs the mcp-remote bridge and Node.js 18+.
- Data is tenant-scoped by key; the same scoping limits any single connection's view.

## FAQ

### Can I try it without an account?

Yes. Use the public demo key `dm_demo_public` against a synthetic 8-person company; analytics and discovery tools are active and no registration is needed.

### How do I connect my real team?

Create a free account, open Settings, API Keys, generate a `dm_live_` key, and put it in the client config in place of the demo key. The first connection shows a consent screen.

### What can the assistant change?

Clock in, clock out and invite staff, all flagged for confirmation in clients that support it. Everything else on the tool list is read-only, and employee-level scoping applies.

### How current is the data?

Questions like "who is clocked in?" return live tenant state; dashboards and analytics reflect the same records the app shows.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Staffic MCP - Team Time Tracking and Monitoring](/hermes/mcp/servers/external/staffic-mcp/)
- [Hourtick MCP - Time Tracking, Tasks and Billing](/hermes/mcp/servers/external/hourtick-mcp/)
- [ZenSched MCP - Field Workforce Scheduling for Agents](/hermes/mcp/servers/external/zensched-mcp/)
