---
title: "Connect Asana to Claude via MCP - Tasks and Milestones"
description: "Connect Asana to Claude through CorpusIQ MCP. Ask which tasks are overdue, what is blocked and who owns what, with cited read-only answers."
category: Claude Integrations
tags: ["connect Asana to Claude", "Asana Claude integration", "MCP Asana connector", "Asana data to Claude", "AI for Asana", "CorpusIQ MCP"]
last_updated: "2026-11-04"
canonical: https://www.corpusiq.io/docs/connect-asana-to-claude
robots: index,follow
---

# How to Connect Asana to Claude with CorpusIQ MCP

Asana tells you what is on a board. It is slower at telling you what is late, what is blocked, and who is carrying more than their share across four projects at once. Those answers mean opening each project, filtering, and reading the list.

Connecting Asana to Claude through CorpusIQ MCP replaces that with a question. You ask in plain language, Claude reads your live workspace, and the answer names the project, the task, and the owner it used.

### Why Connect Asana to Claude?

- **Overdue work, across every project.** "Show me all overdue tasks across my projects." One question instead of four filtered views.
- **Blocked items.** "Which tasks are blocked and waiting on someone else?" That list is usually the real status of a project.
- **Workload.** "Who has the most open tasks this week?" Useful before a planning call, not after.
- **Milestones.** "Which milestones are coming up this month, and which were missed?" The second half is the part nobody reports.
- **Custom fields as answers.** "Show me every task tagged Client Review" works because custom fields are readable, not just the built-in ones.
- **Cross-source context.** Pair the task list with the email thread, the CRM record, or the support queue in one conversation, so the commitment and the work line up.

### How It Works

1. **Connect Asana to CorpusIQ** through OAuth and authorize read-only access to the workspace.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ retrieves** projects, tasks, sections, assignees, due dates, custom fields, and milestones, handling pagination and field expansion behind the scenes.
4. **Claude answers** from that retrieved content, with the projects and tasks it used named.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Asana**.
3. Sign in to Asana and approve the read-only scopes for the workspace you want to read.
4. Copy the MCP config block shown under **Settings, Integrations, Claude Desktop**.

**In Claude Desktop**

5. Open **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
6. Add the CorpusIQ entry:

```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://mcp2.corpusiq.io/mcp"
      ]
    }
  }
}
```

7. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
8. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Tasks**

- "What tasks are assigned to me this week?"
- "Show me all overdue tasks across my projects."
- "Which tasks are blocked and waiting on someone else?"
- "Which tasks have no assignee?"

**Projects**

- "What is the completion percentage for the launch project?"
- "Which projects are behind schedule?"
- "Show me every active project and its status."

**Milestones and fields**

- "What milestones are coming up this month?"
- "Which milestones were missed?"
- "Show me every task tagged Client Review across all projects."
- "List the high-priority tasks in the current sprint."

**People and cross-source**

- "Who has the most open tasks?"
- "Which overdue tasks belong to customers with an open support ticket?" (requires the support or CRM connector)
- "Which deliverables promised in email this month have no Asana task?" (requires the email connector)

### Security

- **Read-only by scope.** The connection requests read access to projects, tasks, sections, assignees, custom fields, and milestones. It cannot create tasks, reassign work, change due dates, or modify a project.
- **Enforced in two places.** The OAuth scope and the MCP tool set both refuse writes, so a write attempt fails rather than silently succeeding.
- **Revocable at any time.** Removing the CorpusIQ application in Asana ends the connection.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Asana, CorpusIQ, and Claude.

### Comparison: Asana Views vs Asana Through Claude

| Aspect | Asana boards and search | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Filters per project | A question in plain language |
| Across projects | One project at a time | Every project in one answer |
| Overdue and blocked work | A filtered list you build | Asked directly |
| Custom fields | Column-by-column reading | Referenced by name in the question |
| Mixing sources | Export and join elsewhere | Tasks plus email, CRM, or support in one answer |
| Write access | Yes, by you | None, read-only |

Boards are the right tool when you want to run the work. Claude is the right tool when you want to know the state of it.

### FAQ: Common Questions

<details>
<summary><strong>Does Claude see every workspace?</strong></summary>

Only the workspace you authorize. Access follows the account that approves the consent screen, so a workspace the account cannot open in Asana is not reachable from Claude either.
</details>

<details>
<summary><strong>Can Claude create or reassign a task?</strong></summary>

No. Every Asana tool exposed to Claude is read-only. Creating, assigning, completing, and editing tasks are not available through this connection.
</details>

<details>
<summary><strong>Are custom fields included?</strong></summary>

Yes. Custom fields come back with each task and can be named in a question, which is what makes answers such as "every task tagged Client Review" possible.
</details>

<details>
<summary><strong>Does it read subtasks and comments?</strong></summary>

Task detail includes the fields Asana exposes for the task, so subtask relationships and the descriptive fields come through. The connection is for reading work state, not for transcribing discussion threads.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Every question is answered against the workspace at the moment you ask. There is no nightly copy of your projects behind the answers.
</details>

<details>
<summary><strong>Can I connect Asana and Jira at the same time?</strong></summary>

Yes. Each connector authorizes independently, so a question can compare delivery work across both systems without either one being the source of truth for the other.
</details>

---

**Next steps:** [Connect Asana to Claude now](https://www.corpusiq.io/connectors)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
