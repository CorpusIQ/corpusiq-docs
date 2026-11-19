---
title: "Connect Asana to Perplexity via MCP"
description: "Connect Asana to Perplexity through CorpusIQ MCP. Ask what is overdue, who is overloaded and which milestones slipped, across every project."
category: Perplexity Integrations
tags: ["connect Asana to Perplexity", "Asana Perplexity integration", "MCP Asana connector", "Asana project questions", "overdue tasks across projects", "CorpusIQ MCP"]
last_updated: "2026-11-19"
canonical: "https://www.corpusiq.io/docs/connect-asana-to-perplexity"
robots: "index,follow"
---

# How to Connect Asana to Perplexity with CorpusIQ MCP

Asana knows the state of the work and shows it one project at a time. The question that matters is rarely about one project: who is carrying too much this week, what is overdue across everything, which milestone is about to slip. Building that view means a portfolio report, a filter and a spreadsheet, every time. **Connecting Asana to Perplexity through CorpusIQ MCP** turns it into a question.

Perplexity is strong on the public record and blind to your workspaces. Once Asana is connected, Perplexity reads projects, tasks, sections, assignees, custom fields, dependencies and milestones through CorpusIQ, and answers with the task or project named.

### Why Connect Asana to Perplexity?

- **Workload.** "Who has the most open tasks this week, and is anything assigned that has no due date?"
- **Overdue work.** "Show me all overdue tasks across my projects, with the assignee and the section each sits in."
- **Blocked work.** "Which tasks are blocked and what is blocking them?"
- **Milestones.** "Which milestones are due this month, and which have already slipped?"
- **Custom fields.** "Show me every task where Story Points is above 8 that is still open."
- **Read-only by capability.** The retrieval tools documented on this page return project and task data to the assistant. They never create a task, reassign work or change a due date.

### How It Works

1. **Connect Asana to CorpusIQ.** Approve the consent screen for the workspace you want visible. The connection covers projects, tasks, sections and the metadata around them.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **Ask a work question.** CorpusIQ searches tasks and projects across the workspace, follows pagination and expands the fields the question needs.
4. **Perplexity answers** with the task, project and section named, so the number can be checked in Asana itself.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Asana** and click Connect.
3. Sign in to Asana and choose the workspace to authorise.
4. Approve the consent screen and wait for the connector to turn green.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

Then ask something the workspace can answer, for example what is due this week. Which workspaces are reachable is decided by the authorisation you approved; nothing outside it is read.

### Example Perplexity Questions

**Workload and priority**

- "Who has the most open tasks this week?"
- "Which high-priority tasks have no owner and a due date inside seven days?"
- "Show me tasks assigned to the design team that are also blocking something."

**Status and slippage**

- "Which projects are behind schedule, and by how much?"
- "What is the completion percentage for each active project?"
- "Show me every task that was due last week and is still incomplete."

**Structure**

- "Which milestones are coming up this month?"
- "Which sections hold the most unfinished work?"
- "List tasks where the custom field Sprint equals the current sprint."

**Cross-source**

- "Show me Asana tasks for the accounts that close this month in the CRM." (requires a CRM connector)
- "Which overdue Asana tasks belong to clients who emailed this week?" (requires a mail connector)
- "Compare Asana project completion with what the team reported in Slack." (requires a messaging connector)

### Security

- **Retrieval tools only.** The tools documented on this page read projects, tasks, sections, assignees, custom fields, dependencies, milestones and workspace metadata.
- **The workspace is not modified.** No task is created, reassigned, rescheduled or completed, and no project setting changes through these tools.
- **Asana authorisation stays yours.** CorpusIQ holds the encrypted grant; revoking it from Asana ends the connection's reach.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Asana, CorpusIQ and Perplexity.

### Comparison: Asana reporting and a work question

| Aspect | Asana reporting and portfolios | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A saved report or a filter you build first | A question asked in the thread |
| Scope | One project or one portfolio | Every project the workspace carries |
| Ad-hoc questions | Rebuild the filter each time | Follow-up changes the question, not the setup |
| Custom fields | Filterable inside a project view | Grouped and compared across projects |
| Cross-system | Copy the list into another tool | Asked beside CRM, mail or finance |
| Write access | Yes, by your users in Asana | None through the retrieval tools |

Asana reports answer the question the report was built for. The operating question changes every week.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity create or reassign tasks?</strong></summary>

No. The retrieval tools documented on this page read project and task data. Creating, assigning, rescheduling, commenting and completing happen in Asana.
</details>

<details>
<summary><strong>Does it read custom fields?</strong></summary>

Yes. Priority, effort, sprint, client name and any other custom field can be filtered and grouped, which is usually how the real question is phrased.
</details>

<details>
<summary><strong>Can it see task dependencies?</strong></summary>

Yes. Dependency information is readable, so blocked work and blocking work can be listed together instead of clicked through one task at a time.
</details>

<details>
<summary><strong>Does it cover every workspace?</strong></summary>

It covers the workspaces you authorised at connect time. A second workspace needs its own authorisation.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Read live at question time. A task edited a moment ago appears in the next answer.
</details>

<details>
<summary><strong>Does this work in ChatGPT or Claude too?</strong></summary>

Yes. Asana is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

### See Also

- [Connect Asana to ChatGPT](connect-asana-to-chatgpt.md) - the same project questions, asked in ChatGPT
- [Connect Monday.com to Perplexity](connect-monday-com-to-perplexity.md) - the same questions on the other board
- [Connect Jira to Perplexity](connect-jira-to-perplexity.md) - the engineering side of the same work
- [Connect Slack to Perplexity](connect-slack-to-perplexity.md) - what was decided, and where it was said
- [Browse all CorpusIQ connectors](connectors.md) - the full list

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*

