# GTD Brain MCP — GTD Task Manager for AI Agents

**Priority:** HIGH | **Category:** Productivity / Operations  
**Transport:** Remote Streamable HTTP | **Auth:** OAuth 2.1 PKCE  
**Website:** https://gtdbrain.com  
**MCP Registry:** `com.gtdbrain/gtd-brain`  
**Discovered:** July 27, 2026 (chatmcp/mcpso #3315)

## What It Does for Operators

GTD Brain exposes a full Getting-Things-Done board to any MCP client. Capture, organize, and work through inbox items, next actions, projects, and waiting-for lists — all through natural language. This is the first dedicated GTD-methodology MCP server, filling a gap for operators who use GTD as their core operating system.

**Why this matters:** Most task-management MCP servers are generic CRUD wrappers around Notion or Todoist. GTD Brain is purpose-built for the GTD workflow with context-appropriate tools (capture goes to inbox, next actions are distinct from projects, waiting-for has its own list).

## Installation

```bash
# Remote endpoint, no local install
# Auth: OAuth 2.1 PKCE with passwordless email login
# Free month trial for new users
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "gtd-brain": {
      "url": "https://mcp.gtdbrain.com/api/gtdbrain/v1/mcp",
      "transport": "streamable-http"
    }
  }
}
```

## Tools (12)

| Tool | Description |
|------|-------------|
| `capture` | Dump anything into inbox for later processing |
| `list_next_actions` | What needs doing now, by context |
| `list_projects` | All active projects with outcomes |
| `list_waiting_for` | Delegated items awaiting response |
| `list_cards` | All cards in a column/view |
| `search_cards` | Full-text search across the board |
| `get_card` / `create_card` / `update_card` | CRUD operations |
| `move_card` | Move between columns (e.g., inbox → next actions) |
| `archive_card` | Clean up completed items |

## Operator Use Cases

1. **Daily review automation:** Agent pulls `list_next_actions` + `list_waiting_for` each morning, surfaces the 3 highest-leverage items, and drafts follow-ups for overdue waiting-for items
2. **Project status reporting:** Agent pulls `list_projects`, reads project cards, and generates a weekly stakeholder update automatically
3. **Inbox triage:** Operator brain-dumps ideas to `capture` throughout the day — agent processes the inbox during weekly review, categorizing each item into next action, project, reference, or trash
4. **Delegation tracking:** When an operator delegates work, the agent logs it to `waiting_for` with a reminder date — follows up automatically if no response by deadline
5. **Meeting prep:** Agent pulls relevant projects + next actions before a meeting, giving the operator a pre-built agenda

## CorpusIQ Angle

**Integratable.** CorpusIQ could pull operational metrics (revenue, support tickets, deal pipeline) and create GTD tasks from them — e.g., "Follow up on deal #4321 → waiting-for" when a HubSpot deal stalls. The GTD Brain MCP provides the task-execution layer that CorpusIQ's data layer can feed.

## Limitations

- Requires active GTD Brain subscription (free month on signup)
- Single-user focused (no team board support mentioned)
- OAuth flow requires initial browser login for token grant
- GTD-methodology specific — users on other systems (Kanban, Scrum) may find less value
