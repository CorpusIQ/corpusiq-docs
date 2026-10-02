---
title: "Yocoolab MCP - Visual Feedback to PR Workflow for Agents"
description: "Self-hosted stdio MCP server that connects AI coding agents to Yocoolab's visual feedback platform. Agents list and triage design feedback threads pinned on live web pages, pull thread context with screenshots and element source, reply to designers, mark threads addressed and open GitHub PRs that close out feedback."
category: Productivity
stars: 1 (GitHub)
added: 2026-09-07
source: mcp.so feed
relevance: ★★★
tags: [visual-feedback, design-collaboration, github-pr, feedback-workflow, product-teams, jira, linear, self-hosted]
---

# Yocoolab MCP - Visual Feedback to PR Workflow for Agents

**Local stdio MCP server (npm, JWT token)** - the official MCP package from Yocoolab (yocoolab.com) that exposes feedback threads, design selections and activity events as tools for Claude Code, Cursor, Cline, Roo Code and Windsurf - so an agent can triage visual feedback left on a live web page and turn it into a coded fix without a human re-explaining the problem.

```
Server type: Local stdio (npx @yocoolab/mcp-server@2), calls the Yocoolab cloud API
Auth: JWT token from the Yocoolab Chrome extension or app.yocoolab.com; GitHub token (auto-detected from gh CLI) for PR tools
Endpoint: https://app.yocoolab.com (API base; the MCP server runs locally on your machine)
Tools: 19 (thread triage and replies, selection and element context, activity summaries, AI conversations, deployment previews, optional Pendo analytics)
Pricing: Free forever - no seat fees for collaborators
Category: Productivity
Built by: Yocoolab (github.com/Yocoolab/mcp-server, Apache 2.0)
```

## Why This Matters for Operators

Visual feedback dies in screenshots. A customer or stakeholder pins a comment on a live element, the developer receives it stripped of context, and the first hour of the fix is spent re-finding the button and re-reading the thread. Yocoolab keeps the context attached - the element, its source, the conversation and the business goals - and the MCP server hands all of it to the coding agent in one call.

**The workflow ends in a PR, not a conversation: the agent reads the full thread, proposes options, and the human decides - approve, route to Jira, or let the agent open the pull request.** Teams ship feedback-to-fix loops in minutes with nobody re-explaining anything, and every collaborator (devs, designers, PMs, clients) is free.

## Tools & Capabilities

| Group | Tools | Purpose |
|---|---|---|
| Threads | list_open_threads, get_thread_context, add_thread_message, mark_thread_addressed, create_pr_for_thread | Triages open feedback, pulls thread context (selection, screenshot, conversation, files touched), replies, marks addressed, opens PRs that close out threads |
| Selection / Bridge | get_latest_selection, get_selection_history, get_element_context, find_source_for_selection, ai_analyze_page | Reads selections from the Chrome extension, resolves element source, analyzes the live page |
| Activity | get_recent_events, get_activity_summary, get_files_touched, get_companion_messages, reply_to_companion | Summarizes workspace activity and agent conversations |
| AI | get_ai_conversations | Reads past AI conversations on the workspace |
| Deployment | get_deployment_preview | Previews deployment state |
| Pendo (optional) | pendo_list_guides, pendo_page_analytics, pendo_feature_usage, pendo_track_event | Product analytics inside the agent session |

## Installation

One command installs and configures every supported agent automatically (Claude Code, Cursor, Cline, Roo Code, Windsurf):

```bash
npx -y @yocoolab/mcp-server@2 setup
```

The setup wizard detects installed agents and writes the correct MCP config for each; restart the agent and the yocoolab server appears. Requirements: Node.js 20+, a Yocoolab account with JWT (from the Chrome extension settings), and a GitHub PAT with repo scope only if you want the PR tools (auto-detected when the gh CLI is installed and authenticated).

## Configuration

```json
{
  "mcpServers": {
    "yocoolab": {
      "command": "npx",
      "args": ["-y", "@yocoolab/mcp-server@2"],
      "env": {
        "YOCOOLAB_API_URL": "https://app.yocoolab.com",
        "YOCOOLAB_TOKEN": "<your-yocoolab-jwt>",
        "YOCOOLAB_BRIDGE_PORT": "9800",
        "YOCOOLAB_BRIDGE_WORKSPACE": "/absolute/path/to/your/workspace"
      }
    }
  }
}
```

The JWT comes from the Yocoolab Chrome extension settings or the account at app.yocoolab.com. Without it, thread-feedback tools are disabled but bridge, companion and activity tools still work. GITHUB_TOKEN is only needed for create_pr_for_thread and is auto-detected from an authenticated gh CLI.

## Business Relevance

- **Product teams** close design feedback loops from pin to shipped PR without re-explaining context in tickets.
- **Founders shipping solo** get a free triage layer: customers pin feedback, the agent reads and proposes fixes, the founder approves.
- **Agencies** keep clients inside the review loop with zero seat fees and no file-conversion overhead.
- **Engineering leads** route agent work to Jira, Linear, Slack or GitHub from the same thread the feedback came from.

## Integration with CorpusIQ

Yocoolab turns product feedback into shipped fixes; CorpusIQ turns the business into numbers. A composed workflow: customer feedback pinned in Yocoolab reaches the agent with full element context, and the same agent session reads CorpusIQ's Stripe or Shopify connectors to quantify what the complaint costs in revenue before deciding the fix priority - so the team ships the change that moves money, not just the loudest thread. Both keep humans in the loop: Yocoolab requires a human to approve before routing or PRs, and CorpusIQ connectors stay read-only.

## Limitations

- New listing, small public repo (1 star, created Apr 2026) - track record is short; the npm package has full provenance, SBOMs and CI, which is encouraging for a young project.
- Local stdio server only - the MCP process runs on your machine, not as a hosted endpoint.
- PR creation requires a GitHub personal access token (or gh CLI auth); Jira and Linear are routed through the Yocoolab web app, not MCP tools.
- The Chrome extension is the primary source of selections and the JWT - teams not using Chrome have a thinner toolset.
- Pendo tools are optional and only useful if the workspace connects Pendo product analytics.

## See Also

- [PingRoom MCP - Human Decisions and Notifications for Agents](/hermes/mcp/servers/external/pingroom-mcp)
- [Elium MCP - Enterprise Knowledge Base for Agents](/hermes/mcp/servers/external/elium-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
