---
title: "Microsoft Planner MCP — Integration Guide"
description: "Connect AI agents to Microsoft Planner for task management in Microsoft 365. Create plans, manage tasks, update buckets, and automate project workflows."
category: mcp
tags: [mcp-server, microsoft-planner, task-management, enterprise, microsoft-365, project-management]
last_updated: 2026-07-03
source: https://mcpservers.org
source_repo: github.com/aixolotl/microsoft-planner-mcp
---

# Microsoft Planner MCP — Integration Guide

**What it does:** Connects AI agents to Microsoft Planner via MCP, enabling task creation, plan management, bucket organization, and workflow automation within Microsoft 365 environments.

**Why it matters:** Microsoft Planner is used by millions of enterprise teams for task tracking within the Microsoft 365 ecosystem. This MCP server lets operators manage projects conversationally — create tasks from meeting notes, reorganize priorities based on shifting deadlines, and generate status reports without opening the Planner UI.

## Quick Info

| Field | Value |
|-------|-------|
| **Transport** | stdio (local) |
| **Authentication** | Microsoft Graph API (OAuth 2.0) |
| **Install** | `npx -y @aixolotl/microsoft-planner-mcp` |
| **Source** | `github.com/aixolotl/microsoft-planner-mcp` |
| **Category** | Task Management & Enterprise |
| **CorpusIQ Verdict** | ★★★★☆ — High value for Microsoft 365 operators |

## Setup

### Prerequisites

1. Microsoft 365 account with Planner license (included in most business plans)
2. Azure AD app registration with Microsoft Graph API permissions:
   - `Tasks.ReadWrite` (delegated)
   - `Group.Read.All` (delegated)
   - `User.Read` (delegated)

### 1. Register Azure AD Application

```bash
# In Azure Portal → App Registrations → New Registration
# Name: MCP-Planner-Integration
# Redirect URI: http://localhost (for device code flow)
# Note: Application (client) ID and Directory (tenant) ID
```

### 2. Configure MCP Client

Add to your `claude_desktop_config.json` or equivalent:

```json
{
  "mcpServers": {
    "microsoft-planner": {
      "command": "npx",
      "args": ["-y", "@aixolotl/microsoft-planner-mcp"],
      "env": {
        "AZURE_CLIENT_ID": "<your-client-id>",
        "AZURE_TENANT_ID": "<your-tenant-id>"
      }
    }
  }
}
```

### 3. Authentication Flow

First run will trigger Microsoft OAuth device code flow:
1. Agent initiates connection
2. Browser opens to `microsoft.com/devicelogin`
3. Enter the displayed code
4. Grant Planner permissions
5. Token cached for subsequent sessions

## Available Tools

| Tool | Description |
|------|-------------|
| `list_plans` | List all Planner plans accessible to the user |
| `get_plan` | Get plan details including buckets and task counts |
| `list_tasks` | List tasks in a plan/bucket with filters (assigned, due, priority) |
| `create_task` | Create a new task with title, due date, assignee, priority, description |
| `update_task` | Update task fields: status, due date, assignee, priority, notes |
| `create_bucket` | Create a new bucket within a plan |
| `get_my_tasks` | Get tasks assigned to the authenticated user across all plans |
| `add_task_checklist` | Add checklist items to a task |
| `add_task_comment` | Add a comment/note to a task |

## Operator Workflows

### Daily Standup Prep

```
Agent: "Show me all my tasks due this week across all plans, sorted by priority"
→ get_my_tasks(filter: {dueBefore: "2026-07-10"}, sort: "priority")
→ Returns prioritized task list ready for standup
```

### Meeting → Task Automation

```
Agent: "Create tasks in the Q3 Launch plan from these meeting notes:
- Finalize pricing page by Friday (assign to Sarah)
- Update API docs by next Wednesday (assign to me)
- Schedule beta demo with Acme Corp by Monday"
→ Creates 3 tasks with proper assignments and due dates
```

### Sprint Retro Prep

```
Agent: "Show me all completed tasks in the Engineering plan from last sprint"
→ list_tasks(plan: "Engineering", status: "completed", completedSince: "2026-06-23")
→ Returns completed task list for retro discussion
```

## Limitations

- Requires Microsoft 365 commercial subscription (not personal/family)
- OAuth flow requires interactive browser first-run
- Microsoft Graph API rate limits apply (10,000 requests/10 min per app)
- Cannot manage Planner premium features (timeline view, goals)
- Read-only for plans shared with the user but not owned

## Alternatives

| Server | Best For |
|--------|----------|
| **Linear MCP** | Startup/product teams (simpler, faster UX) |
| **Atlassian MCP (Jira)** | Enterprise Agile/Scrum teams |
| **ClickUp MCP** | All-in-one project management |
| **Notion MCP** | Flexible project tracking with docs |
| **n8n MCP** | Workflow automation across multiple tools |

## CorpusIQ Assessment

**Strategic Value:** High. Microsoft 365 is the default enterprise stack. Any operator managing teams on Planner can immediately reduce task-management friction by 60-80% through conversational task operations.

**Integration Difficulty:** Medium. Azure AD setup is the primary hurdle. Once configured, the MCP server is standard stdio with cached OAuth.

**Risk:** Low. Microsoft Graph API is mature. Permissions are scoped to Planner data. No PII exposure beyond task metadata.

**Recommendation:** **Catalog and recommend** to Microsoft 365 operators. This fills a clear gap in the enterprise task management MCP ecosystem.
