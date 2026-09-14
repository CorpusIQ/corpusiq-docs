---
title: "Day Off MCP - PTO and Time Tracking for Agents"
description: "Remote MCP server for Day Off, the PTO and time-tracking platform used by more than 50,000 companies. Assistants reach leave requests, balances, approvals, attendance, timesheets and team availability over OAuth at mcp.day-off.app/mcp, alongside the platform's Slack, Teams and calendar integrations."
category: Business Operations
stars: n/a (new listing)
added: 2026-09-14
source: "mcp.so feed (day-off) + vendor listing text"
relevance: ★★
tags: [hr, pto, time-tracking, workforce, leave-management, attendance, oauth, remote-mcp]
---

# Day Off MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the agent interface for Day Off, an AI-powered PTO and time-tracking platform trusted by more than 50,000 companies. The workforce questions that normally mean a dashboard trip - who is off today, whose leave request is waiting, how many days a teammate has left - become assistant questions, answered from the same system the company already runs its leave and attendance in. The endpoint answers an anonymous initialize with HTTP 401, confirming a live, auth-gated server.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first connect)
Endpoint: https://mcp.day-off.app/mcp
Tools: capability set documented (leave, attendance, timesheets, approvals, reports); live tool list served from the endpoint
Pricing: Day Off account required; plan details at day-off.app
Category: Business Operations
Built by: Day Off (day-off.app)
```

## Why This Matters for Operators

HR admin is a stream of small, constant questions that interrupt everyone: approvals sit in a queue, balances get checked one employee at a time, and "who is off today" needs a calendar view before a planning call. Day Off MCP collapses that into conversation. An ops lead can ask for the state of next week's coverage before a launch, a manager can walk through pending approvals in a chat thread, and a founder can check balances and attendance patterns without learning the admin UI. The platform already models the hard parts - accrual, carryover, expiry, blockout dates, multi-step approvals, roles and permissions - so the answers respect the company's actual policies.

## Tools & Capabilities

| Area | Coverage |
|---|---|
| Leave management | requests, single or multi-step approvals, balances and allowances, custom policies per team and location, accrual, carryover and expiry rules, blockout dates |
| Attendance and time | time and attendance tracking, timesheets, working-hours management, time across tasks and projects |
| Scheduling | fixed, flexible, rotating and remote schedules; public holidays; multiple locations and time zones |
| Team visibility | "Who's Off Today" calendar, team availability, role-based visibility settings |
| Reporting | advanced time-tracking and leave-management reports |
| Admin | bulk operations for large teams, multiple teams, sub-teams, policies and approvers; SSO and MFA |

The live tool list is served from the connected endpoint; the MCP listing documents the capability set above.

## Installation

```bash
claude mcp add day-off --transport http https://mcp.day-off.app/mcp
```

Add the endpoint as a custom connector in Claude, Cursor, VS Code or any MCP-compatible client and complete the OAuth sign-in. Day Off also ships employee and admin mobile apps (Apple App Store, Google Play) and integrates with Slack, Microsoft Teams, Google Calendar and Outlook Calendar on the platform side. The app supports English, Spanish, French and German.

## Configuration

```json
{
  "mcpServers": {
    "day-off": {
      "type": "http",
      "url": "https://mcp.day-off.app/mcp"
    }
  }
}
```

## Business Relevance

- **Founders and ops leads** check coverage and pending approvals before planning sprints, launches or holidays.
- **HR managers** answer balance, policy and attendance questions without opening the admin console.
- **Team leads** see availability and schedules for their own people, scoped by the roles already configured.
- **Finance and payroll prep** pulls timesheet and attendance summaries in the same session as other business data.

## Integration with CorpusIQ

Day Off answers the workforce side of a review; CorpusIQ answers the business side. A CorpusIQ agent can pull revenue, pipeline and operations data (Stripe, QuickBooks, HubSpot, Google Workspace, Slack) and, in the same session, ask Day Off who is out, whose approval is pending and how the team's hours landed - so a Monday operating review covers people and numbers together. Because both systems scope access by role, the composed answer respects each platform's permissions.

## Limitations

- Brand new listing: no third-party track record and no public repo for the server itself.
- Tool names are not published on the listing; the live list is served from the authorized connection.
- Commercial SaaS only, with no self-hosted option through the MCP server.
- Workforce scope only: leave, attendance and time - payroll execution stays in the payroll system.
- The 50,000-company figure is the vendor's own platform claim.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [ConnectMachine MCP - Digital Business Cards and Contact CRM for Agents](/hermes/mcp/servers/external/connectmachine-mcp/)
- [Taskade MCP - Official AI Workspace Connector](/hermes/mcp/servers/external/taskade-mcp/)
