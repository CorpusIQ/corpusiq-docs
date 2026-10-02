---
title: "Done Bear MCP - GTD Task Manager for Agents"
description: "Hosted OAuth 2.1 MCP for the Done Bear task manager: create, edit and complete tasks, projects and checklists, plus comments, attachments, labels, teams and bulk edits across 35 live-verified tools. Local-first GTD workflow with inbox, today, upcoming, anytime and someday views."
category: Productivity
stars: "n/a (hosted service)"
added: 2026-09-01
source: "chatmcp/mcpso issue #3883 (Sep 1, 2026 night sweep)"
relevance: ★★
tags: [mcp-server, task-management, gtd, productivity, projects, checklists, oauth, remote-mcp]
---

# Done Bear MCP

**A GTD task manager an agent can actually drive.** Done Bear is a local-first task manager with a hosted MCP surface: tasks, projects, checklists, comments, attachments, labels and teams, with bulk operations and GTD views (inbox, today, upcoming, anytime, someday). Live-probed Sep 1, 2026: all 35 tools captured from the endpoint (serverInfo: donebear v0.7.0), OAuth-gated for writes.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://mcp.donebear.com/mcp
Auth: OAuth 2.1
Tools: 35 (live-probed Sep 1, 2026)
Registry: com.donebear/donebear v1.0.0 (active, updated Aug 16, 2026)
Also listed: Smithery (donebear/donebear)
Website: donebear.com
```

## Why This Matters for Operators

Most task managers expose a read-only "AI view" or none at all. Done Bear's MCP is the full workspace: the agent can create, plan and complete real work, not just summarize it.

First, **write-side GTD.** `task_add` routes new tasks into inbox, today, upcoming, anytime or someday views, so agent-created work lands in the same system the human already runs on.

Second, **bulk operations with confirmation semantics.** `task_bulk_edit` and `task_bulk_done` move up to 50 tasks per call, and the tool descriptions themselves instruct the agent to confirm the number list with the user first.

Third, **full collaboration context.** Comments, attachments (server-side fetch and storage, never raw file bytes through the model), labels and team assignment make the workspace a shared surface between the agent and the team rather than a private agent log.

## Tools and Capabilities

All 35 tools captured live Sep 1, 2026; grouped by surface.

| Surface | Tools |
|---------|-------|
| Workspace context | `guide`, `get_context`, `search` - per-topic product guides, workspace snapshot, ranked lexical search |
| Tasks | `task_list`, `task_show`, `task_add`, `task_edit`, `task_done`, `task_reopen`, `task_archive`, `task_bulk_edit`, `task_bulk_done`, `task_assign` |
| Projects | `project_list`, `project_add`, `project_join`, `project_leave`, `project_edit` |
| Checklists | `checklist_list`, `checklist_add`, `checklist_done`, `checklist_edit`, `checklist_remove` |
| Comments | `comment_list`, `comment_add`, `comment_edit`, `comment_remove` |
| Attachments | `task_attachment_list`, `task_attach`, `task_attachment_remove` |
| Labels and teams | `label_list`, `label_create`, `label_add`, `label_remove`, `team_list` |

## Installation

```bash
claude mcp add --transport http donebear https://mcp.donebear.com/mcp
```

First connection opens OAuth sign-in to your Done Bear workspace. The hosted endpoint is POST-only Streamable HTTP; follow the vendor's get-started guide at donebear.com/docs/mcp/get-started for client-specific steps.

## Configuration

```json
{
  "mcpServers": {
    "donebear": {
      "type": "http",
      "url": "https://mcp.donebear.com/mcp"
    }
  }
}
```

The grant scopes the agent to the connected workspace. Comments are attributed to the connected user and are visible to the whole workspace, so the agent writes as a teammate.

## Business Relevance

- **Founders and solo operators** hand the agent their inbox and today lists, letting it triage, schedule and complete GTD-state changes directly.
- **Small teams** use one workspace where agent-created tasks, comments and attachments sit alongside human work with attribution.
- **Agency PMs** use bulk edits to sweep 50 stale tasks at once and team assignment to route agent findings to the right owner.
- **Workflow builders** attach generated files to tasks by URL, so reports and exports land on the task they belong to.

## Integration with CorpusIQ

Done Bear composes with CorpusIQ as the execution ledger for agent work. A CorpusIQ workflow that flags anomalies in Stripe, HubSpot or Google Ads can create the follow-up task in Done Bear with the full context attached, assign it to the owner, and check the task off when the metric recovers. The operator keeps one governance point: Done Bear holds the plan and the history of who did what, while CorpusIQ supplies the business data that decides what goes on the list. The bulk-done tool's explicit confirm-first semantics match the operator's control expectations.

## Limitations

- Brand new listing; the submission's GitHub link (github.com/donebear/donebear) is not yet publicly accessible - registry name and live endpoint verified instead.
- Writes require OAuth sign-in; no anonymous or API-key mode.
- Comments and task assignment are workspace-visible, so agent activity is attributed and reviewable rather than silent.
- Hosted service only; no self-host option documented.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Taskfolk MCP - Project Management for Teams and AI Agents](/hermes/mcp/servers/external/taskfolk-mcp)
- [Laver MCP - Kanban Boards, Sprints and Team Wiki for Agents](/hermes/mcp/servers/external/laver-mcp)
