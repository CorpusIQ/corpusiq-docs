---
title: "Connect Jira to Perplexity via MCP - Sprints, No JQL"
description: "Connect Jira to Perplexity through CorpusIQ MCP. Ask about sprints, blockers and velocity in plain English and get cited answers, read-only."
category: Perplexity Integrations
tags: ["connect Jira to Perplexity", "Jira Perplexity integration", "MCP Jira connector", "Jira data to AI", "ask Jira in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-18"
canonical: "https://www.corpusiq.io/docs/connect-jira-to-perplexity"
robots: "index,follow"
---

# How to Connect Jira to Perplexity with CorpusIQ MCP

Jira answers one question well: what is in this board right now. It answers the harder questions badly. How much did we finish this sprint compared with the last five. Which issue has been sitting in review longest. Why the release slipped.

Getting those answers means building a filter, choosing fields, and reading a chart. Or writing JQL if you happen to know it.

Connecting Jira through CorpusIQ MCP replaces the filter builder with a question. Perplexity reads your live instance, read-only, and names the project, the sprint and the issues it used.

### Why Connect Jira to Perplexity?

- **Sprint status without a dashboard.** "What is still open in the current sprint, and who owns each item?"
- **Velocity over time.** "How many story points did we complete in each of the last five sprints?"
- **Aging work.** "Which issues have been in review for more than five days?"
- **Release readiness.** "Which issues targeted at the next release are still unresolved, and what is the highest priority among them?"
- **Workload distribution.** "Who has the most open issues this sprint?"
- **Read-only by capability.** The retrieval tools documented on this page are read-only, and the access granted is read access: an OAuth consent on Jira Cloud or a read-scoped personal access token on Data Center.

### How It Works

1. **Connect Jira to CorpusIQ.** Authorise read-only access to your instance, either through OAuth for Jira Cloud or a personal access token for Jira Data Center.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into Jira searches, handles pagination and field mapping, and retrieves the matching issues, sprints and projects.
4. **Perplexity answers** from that retrieved content, with the issues it used attached to the answer.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Jira**.
3. Authorize read-only access. On Jira Cloud this is an OAuth consent screen. On Data Center it is a personal access token bound to the account you want read.
4. The connector turns green and the issue and sprint tools become available.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

7. Connect and approve the CorpusIQ authorization page once. Then start a new thread and ask about a board, a sprint or a release.

A Jira token reads what its account can read. On Data Center, the account you issue the token for is the boundary; on Cloud, the consent screen lists the projects the authorising user can already open.

### Example Perplexity Questions

**Sprint and board**

- "What is still open in the current sprint, and who owns each item?"
- "Which issues moved to Done this week, grouped by assignee?"
- "What is in the ready-for-qa column right now?"

**Delivery health**

- "How many story points did we complete in each of the last five sprints?"
- "Which issues have been in review for more than five days?"
- "What is our average cycle time this quarter against last quarter?"

**Release and scope**

- "Which issues targeted at the next release are unresolved?"
- "What was added to this release after the scope freeze?"
- "Which epics have no issue in progress?"

**Cross-source**

- "Do the epics closed in Jira match the projects marked done in Notion?" (requires the Notion connector)
- "Which Jira incidents have a matching thread in Slack?" (requires the Slack connector)
- "Compare the sprint commitment with the hours logged in the sheet." (requires Google Sheets)

### Security

- **Read-only retrieval tools.** The tools documented on this page search and read issues, sprints and projects. They do not create, transition, assign or comment on an issue.
- **Scoped credentials.** Cloud access is an OAuth consent for the authorising user; Data Center access is a personal access token you can revoke on its own.
- **No stored credentials on your side.** CorpusIQ holds the encrypted token, and revocation takes effect on the next call.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Jira, CorpusIQ and Perplexity.

### Comparison: Jira filters, dashboards and JQL

| Aspect | Jira filters, dashboards and JQL | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A filter builder, or a JQL query | A question in plain language |
| Skill needed | Know the fields and the operators | None |
| Across time | Build a report per sprint | Asked across the last five sprints |
| Outside context | Open a second tab | Same thread, same answer |
| Cross-system | Export to a sheet | Asked across connectors |
| Write access | Yes, by your users | None through the retrieval tools |

A board shows the current state. The question is usually about the trend.

### FAQ: Common Questions

<details>
<summary><strong>Do I need to know JQL?</strong></summary>

No. You ask in plain language and CorpusIQ builds the searches. JQL is not part of the path.
</details>

<details>
<summary><strong>Can Perplexity change an issue?</strong></summary>

No. The retrieval tools documented on this page read issues, sprints and projects. No create, transition or comment path exists on them.
</details>

<details>
<summary><strong>Does it work with Jira Data Center?</strong></summary>

Yes. Cloud connects through an OAuth consent screen, and Data Center through a personal access token.
</details>

<details>
<summary><strong>Which projects can it see?</strong></summary>

The projects the authorising account can already open. Nothing wider is reachable.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Each question reads Jira as it stands, so an issue moved a minute ago shows in the next answer.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Jira is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

### See Also

- [Connect Jira to ChatGPT](connect-jira-to-chatgpt.md) - the same sprint and velocity questions, asked from ChatGPT
- [Connect Jira to Claude](connect-jira-to-claude.md) - the same questions with the Claude Desktop config block
- [Connect Monday.com to Perplexity](connect-monday-com-to-perplexity.md) - work management boards read the same way

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
