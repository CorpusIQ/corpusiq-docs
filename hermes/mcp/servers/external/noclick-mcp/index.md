---
title: "NoClick MCP - Workflow Automation for AI Assistants"
description: "Hosted MCP server that lets an AI assistant build, edit, run, and debug NoClick workflows through 47 tools - workflows, checkpoints, node configuration, executions, credentials, and skills - plus a visual builder that turns 150+ apps into a hosted MCP server."
category: Productivity
stars: n/a (new listing, github.com/noclickapp/noclick)
added: 2026-08-29
source: "mcp.so GitHub issue #3816"
relevance: ★★
tags: [mcp-server, automation, workflow, no-code, ai-agents, integration, productivity, remote-mcp]
---

# NoClick MCP

**A hosted MCP server that lets AI assistants create, configure, and run NoClick workflows without leaving the editor - 47 tools over workflows, checkpoints, nodes, executions, credentials, and skills - on top of a platform that also turns 150+ connected apps into a hosted MCP server with no code.** NoClick is an automation platform (workflows, nodes, edges, runs, credentials, credits, organizations) with an AI builder that assembles workflows from plain-language descriptions. Works with Claude, Claude Code, ChatGPT, Cursor, Windsurf, and OpenAI Codex through OAuth 2.1 with PKCE.

```
Server type: Remote (Streamable HTTP), hosted
Auth: OAuth 2.1 with PKCE (bearer tokens also accepted)
Endpoint: https://api.noclick.io/mcp
Tools: 47 (workflows, checkpoints, nodes, execution, credentials, workspace, interface, skills, debugging)
Pricing: Free, Plus, Pro, and Enterprise plans (credit-based)
Category: Productivity / Workflow Automation
Built by: NoClick (noclick.com); repo github.com/noclickapp/noclick
```

## Why This Matters for Operators

Operators collect an automation backlog they never get to: the report that should post to Slack, the form that should write to the CRM, the webhook that should notify the team. NoClick MCP puts an assistant on that backlog directly - describe the automation, and the assistant builds the workflow with the node catalog, validates it, runs it, and inspects the output, with checkpoints to snapshot state before risky batches of edits.

Two surfaces matter to operators. The workflow tools let an assistant build and debug automations in conversation, with the AI builder pausing to ask for anything only you know (account connections, values). The hosted MCP builder goes the other direction: pick apps (Gmail, Slack, HubSpot, Salesforce, Notion, Shopify, and 150 more), choose which operations to expose, and get a hosted MCP server URL your assistant can call - no code, nothing to deploy.

**Automation backlogs become conversational work, and any app stack can be exposed as an MCP server in minutes.**

## Tools & Capabilities

All 47 tool names verified from the vendor's public tools page.

| Group | Tools |
|---|---|
| Workflows | list_workflows, create_workflow, get_workflow, update_workflow_metadata, delete_workflow, save_template_draft, get_current_workflow, open_workflow |
| Checkpoints | create_checkpoint, list_checkpoints, restore_checkpoint |
| Nodes | get_available_node_types, search_operations, get_node_operations, get_node_configs, update_workflow, validate_workflow, autofill_node, get_node, get_selected_node, load_value |
| Execution | run_workflow, run_nodes, get_execution_status, list_executions, get_node_output, get_node_output_history, get_node_statuses, list_tool_calls |
| Credentials | search_credentials, connect_credential, list_credential_requests, load_options |
| Workspace | get_workflow_folders, update_folders, list_workspaces, switch_workspace |
| Interface | update_interface, eval_interface, validate_interface |
| Skills | list_skills, load_skill |
| Debugging and feedback | get_console_logs, get_sdk_logs, get_health, report_bug, request_feature |

## Installation

```bash
claude mcp add --transport http noclick https://api.noclick.io/mcp
```

On first use the browser opens for OAuth authorization and the token is saved automatically. Keep the client session running while you approve in the browser - closing the terminal or approving from an old tab breaks the localhost hand-off; just re-run the authenticate step.

## Configuration

```json
{
  "mcpServers": {
    "noclick": {
      "type": "http",
      "url": "https://api.noclick.io/mcp"
    }
  }
}
```

Project-scoped config (.mcp.json) is recommended so a team shares the same setup through version control.

## Business Relevance

- **Operations leads** clear the automation backlog by describing workflows instead of building them by hand.
- **Teams on SaaS stacks** expose Gmail, Slack, HubSpot, Notion, or Salesforce operations to their assistants as a hosted MCP server.
- **Engineers** hand the assistant the workflow layer (nodes, runs, checkpoints, console logs) while keeping credentials managed in NoClick.
- **Agencies** clone template drafts and iterate them with the AI builder before publishing to the template library.

## Integration with CorpusIQ

NoClick complements CorpusIQ's connector architecture from both directions. CorpusIQ already ships 40+ built-in connectors; NoClick's hosted MCP builder covers the long tail of apps (150+) that CorpusIQ workflows need occasionally, exposed as tools without code. A CorpusIQ-driven workflow can use NoClick MCP to build a Slack-notification automation for lead alerts, run it, and read get_node_output for verification - the same done-only reporting discipline CorpusIQ applies to its own crons. Checkpoints give CorpusIQ's automation work a rollback rail that matches its audit-first doctrine for external actions.

## Limitations

- Commercial platform - real automations consume credits on the Free/Plus/Pro/Enterprise plans.
- Workflows run in NoClick's cloud; heavy self-hosting teams may prefer n8n for on-prem.
- The 47-tool MCP surface is for building workflows, not for querying business data from your apps (that is the separate hosted MCP builder).
- Brand-new listing (repo fresh, no star history) - the platform itself predates the MCP surface.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [n8n MCP Server - Workflow Automation](/docs/hermes/mcp/servers/external/n8n-mcp)
- [Browserless MCP - Browser Automation for Agents](/docs/hermes/mcp/servers/external/browserless-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
