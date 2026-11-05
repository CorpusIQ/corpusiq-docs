---
title: "Connect Jira to Claude via MCP - Sprints, No JQL"
description: "Connect Jira to Claude through CorpusIQ MCP. Ask about sprints, blockers and velocity in plain English and get cited answers, read-only."
category: Claude Integrations
tags: ["connect Jira to Claude", "Jira Claude integration", "MCP Jira connector", "Jira data to Claude", "AI for Jira", "CorpusIQ MCP"]
last_updated: "2026-11-04"
canonical: https://www.corpusiq.io/docs/connect-jira-to-claude
robots: index,follow
---

# How to Connect Jira to Claude with CorpusIQ MCP

Jira answers one question well: what is in this board right now. It answers the harder questions badly. How much did we finish this sprint compared with the last five. Which issue has been sitting in review longer than the rest of the queue. Why the release slipped. Getting those answers means building a filter, choosing fields, and squinting at a chart.

Connecting Jira to Claude through CorpusIQ MCP replaces the filter builder with a question. You ask in plain language, Claude reads your live Jira instance, and the answer comes back with the project, the sprint, and the issues it used named in the reply. No JQL. No export.

### Why Connect Jira to Claude?

Jira is where engineering work is recorded, and it is the system least read by the people who pay for it. Claude gives you a way to read it without learning the query language.

- **Sprint status without a dashboard.** "What is still open in the current sprint, and who owns each item?" One question instead of a board filter.
- **Velocity over time.** "How many story points did we complete in each of the last five sprints?" Claude reads the closed sprints and returns the numbers side by side.
- **Aging work.** "Which issues have been in review for more than five days?" The queue is usually the answer to why a date slipped.
- **Release readiness.** "Which issues targeted at the next release are still unresolved, and what is the highest priority among them?"
- **Workload distribution.** "Who has the most open issues this sprint?" Useful before a planning meeting, not after.
- **Cross-source context.** Pair the Jira answer with the pull request, the incident note, or the customer ticket in the same conversation, so the delivery story and the record agree.

### How It Works

1. **Connect Jira to CorpusIQ.** Authorize read-only access to your instance, either through OAuth for Jira Cloud or a personal access token for Jira Data Center.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into Jira searches, handles pagination and field mapping, and retrieves the matching issues, sprints, and projects.
4. **Claude answers** from that retrieved content, with the issues it used attached to the answer.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Jira**.
3. Authorize read-only access. On Jira Cloud this is an OAuth consent screen. On Data Center it is a personal access token bound to the account you want read.
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

**Sprint and planning**

- "What is still open in the current sprint?"
- "How many story points have we completed this sprint, and what is our velocity over the last five sprints?"
- "Show me unresolved issues in the current sprint sorted by priority."
- "Which issues moved to done since Monday?"

**Board hygiene**

- "Which issues have been in In Progress for more than five days?"
- "Show me issues with no assignee in the active sprint."
- "Which bugs were reopened more than once?"

**Epics and releases**

- "What is the status of the authentication epic?"
- "Which issues targeted at the next release are still unresolved?"
- "How many open bugs belong to the current release?"

**People and workload**

- "Who has the most open issues this sprint?"
- "Show me issue distribution by assignee."
- "Which issues are blocked, and what are they waiting on?"

**Cross-source**

- "Which open Jira issues correspond to customers who reported a problem this week?" (requires the CRM or email connector)
- "Show me issues that shipped after the incident was opened." (requires the incident or monitoring source)

### Security

- **Read-only by permission.** The connection requests read access to projects, issues, sprints, and reports. There is no path for Claude to create an issue, transition a status, assign work, or comment.
- **Enforced in two places.** The Jira permission scope and the MCP tool set both refuse writes, so a write attempt fails rather than silently succeeding.
- **Revocable at any time.** Removing the CorpusIQ application in Jira, or revoking the personal access token, ends the connection immediately.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Jira, CorpusIQ, and Claude.

### Comparison: JQL and Dashboards vs Jira Through Claude

| Aspect | Jira boards and JQL | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Filters, JQL, saved searches | A question in plain language |
| Setup per question | Choose project, fields, date range | None |
| Cross-sprint view | A separate report or dashboard | Asked directly, returned as text |
| Reading history | You open each issue | Claude reads the issues and summarizes |
| Mixing sources | Export and join elsewhere | Jira plus CRM, code, or incidents in one answer |
| Write access | Yes, by you | None, read-only |

Filters are the right tool when you know exactly which issues you want. Claude is the right tool when you know the question and not the query.

### FAQ: Common Questions

<details>
<summary><strong>Does this work with Jira Data Center, or only Cloud?</strong></summary>

Both. Jira Cloud authorizes through OAuth. Data Center authorizes with a personal access token issued to the account you want read. In both cases the access is read-only.
</details>

<details>
<summary><strong>Do I need to know JQL?</strong></summary>

No. Ask in plain language and CorpusIQ builds the underlying search. If you already know JQL, you can paste a query into your question and it is used directly.
</details>

<details>
<summary><strong>Can Claude change an issue status or assign work?</strong></summary>

No. Every Jira tool exposed to Claude is read-only. Creating issues, transitioning statuses, assigning, commenting, and editing fields are not available through this connection.
</details>

<details>
<summary><strong>Which Jira projects can Claude see?</strong></summary>

Only the projects the authorizing account can already see in Jira. Permissions are inherited from the account, so Claude cannot reach a project that the human who connected it could not open.
</details>

<details>
<summary><strong>Are custom fields available?</strong></summary>

Yes. Standard fields come back with each issue, and custom fields can be referenced by name in your question. Story point fields, team fields, and internal priority fields all work.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Every question is answered against the instance at the moment you ask. There is no nightly copy of your Jira project behind the answers.
</details>

---

**Next steps:** [Connect Jira to Claude now](https://www.corpusiq.io/connectors)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
