---
title: "BugHerd MCP - Client Feedback Inside the Editor"
description: "Official BugHerd server: an agent lists client tasks with screenshot, CSS selector and console context, then comments, reassigns and closes them."
category: Development / Agency Operations
stars: n/a (BugHerd subscription)
added: 2026-10-27
source: "live probe on mcp.bugherd.com/mcp (initialize 401, OAuth required), the vendor getting-started article and client integration guides, the tool names published on the vendor page, and the mcpservers.org official listing"
relevance: ★★★
tags: [bug-tracking, website-feedback, agency, oauth, kanban, client-portal, qa, triage]
last_updated: "2026-10-27"
---

# BugHerd MCP

**Website feedback arrives as a screenshot and one sentence: this looks wrong on my phone. Everything an agent needs to fix it, the URL, the CSS selector, the browser, the console output, exists in the tool the client used to point at the screen. What was missing was a way for the agent to read it.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.bugherd.com/mcp
Transport:   JSON-RPC over POST
Auth:        OAuth, acting as your BugHerd user
Tools:       read, list, update, comment, create across tasks and
             projects (get_task_details, list_project_tasks,
             list_my_tasks, list_all_tasks, update_task, add_comment,
             create_task, create_project, update_project)
Built by:    BugHerd (bugherd.com), the official server
Clients:     Claude Code, Claude, Cursor, ChatGPT, VS Code with
             Copilot, Windsurf, Codex CLI, Gemini CLI, Zed, Onyx
```

## Why This Matters for Operators

Agencies lose a day a week to context switching between a feedback board and a codebase. Fifteen tasks land over a weekend, each one needs to be read, matched to a file, fixed and answered, and the status has to be updated in two places so the client does not ask about it again.

This is the first server in this catalog that closes an agency feedback loop in one place: the agent reads the task with its captured context, makes the change, comments what it did in the thread the client already watches, and marks it done. The review step stays human, on the board.

## What It Actually Does

`initialize` on `https://mcp.bugherd.com/mcp` returns HTTP 401, which is the correct shape for an account-gated server rather than a stale endpoint. The vendor documents OAuth sign-in, with the selected organization determining which data the client can reach and access always reflecting the user's existing BugHerd permissions. Connected clients can be seen and their tokens revoked.

The published tool surface, grouped by what an operator does with it:

| Job | Tools |
|---|---|
| Read one task in full | `get_task_details` |
| List work by project, by assignee, or everywhere | `list_project_tasks`, `list_my_tasks`, `list_all_tasks` |
| Close the loop | `update_task` for status, assignee, priority, severity and due date |
| Tell the client | `add_comment` for fix summaries, analysis and updates in the task thread |
| Open new work | `create_task`, `create_project`, `update_project` |

What travels with each task is the part that matters: the screenshot or screen recording, the URL, the CSS selector, the client comment, the attachments and the technical details BugHerd captured when the client clicked, plus console logs and replay on the plans that include them.

## The Part That Costs You Something

This server can write to the client-facing surface, and that is the whole risk.

**`add_comment` is a client-facing message.** An agent that posts "fixed, redeployed" before the deploy is live has now told a paying client something untrue in a thread they read. The vendor's own framing is that the human reviews what was done on the board or in the thread, which is the correct default: let the agent read and prepare, and keep the outbound comment behind a person.

**`create_task` and `update_task` change a board a team is working from.** A triage pass that closes tasks is a real change to someone's day, so scope the agent to the projects and statuses you mean it to touch.

## How It Is Contained

- **OAuth as the user, not as the workspace.** Permissions mirror the connecting user's existing BugHerd permissions, so an agent cannot exceed the person who authorised it.
- **Organization-scoped.** The organization chosen at connect time bounds what the client can reach, which makes client separation enforceable at the connection rather than in a prompt.
- **Tokens are revocable.** Connected clients can be reviewed and revoked from the account, so a connection made for one project can be closed when that work ends.
- **Read-only is a choice, not a default.** The read tools are safe on their own; the write tools are separated by name, so a client can be wired to list and detail only.

## Limitations Recorded

- No tool call was executed: every path requires a BugHerd account, so capability groups come from the vendor's published tool names rather than a live `tools/list`.
- Each task shares everything captured with the agent, so what the client attached, recordings included, reaches the assistant. Review what the project captures before connecting.
- Console output and replay depend on the plan and the integration being active on the site.
- BugHerd is a feedback and task system, not a test runner. It tells the agent what a person saw, not what is broken.

## FAQ

### Can the agent close client tasks on its own?
It has the tools to. Whether it should is a policy decision, and the honest default is: let it read, triage and prepare, and let a person mark work done and post the client-facing comment.

### Does it work with ChatGPT and Claude directly?
The vendor lists Claude Code, Claude, Cursor, ChatGPT, VS Code with Copilot, Windsurf, Codex CLI, Gemini CLI, Zed and Onyx as supported clients, with per-client setup articles.

### What should I test first?
Connect one project, ask the agent to list the open tasks and read the three oldest, and check that the context it sees matches what the client actually reported before giving it any write tool.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Directory and agency operations guides](/hermes/mcp/servers/external/)
- [CorpusIQ connectors for project and CRM data](/hermes/mcp/)
