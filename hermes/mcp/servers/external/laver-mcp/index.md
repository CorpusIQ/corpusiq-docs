---
title: "Laver MCP - Kanban Boards, Sprints and Team Wiki for Agents"
description: "Official MCP server from Laver (laver.app): 59 typed tools that read and drive kanban boards, tickets, sprints, attachments and the team wiki with versioned writes so an agent and a person can work the same board at once. stdio via npx @laver/mcp, MIT."
category: Productivity
stars: "n/a (new listing, Developyn/laver-mcp)"
added: 2026-08-30
source: "mcp.so GitHub issue #3835"
relevance: ★★
tags: [mcp-server, project-management, kanban, tickets, wiki, team, stdio, npm]
last_updated: "2026-10-19"
---

# Laver MCP

**Official MCP server from Laver, a project management tool for small teams.** 59 typed tools read and drive kanban boards, tickets, sprints, attachments and the workspace wiki through the same public REST API the web app uses. The headline design decision is versioned writes: every mutation that can collide carries the record's `version`, and a stale write is refused with a 409 returning the current value, so an agent and a person can work the same board at once without one silently overwriting the other.

```
Server type: Local (stdio via npx)
Auth: workspace-scoped API key (Admin > API keys); the key acts as the person who created it
API host: https://api.laver.app (override with LAVER_API_URL, https only except localhost)
Tools: 59 over boards, tickets, comments, subtasks, labels, custom fields, attachments, wiki pages, automations and published links
Registry: io.github.Developyn/laver-mcp v0.5.0 (official MCP registry)
Pricing: Free (one workspace, up to 3 billable people, no card) · Pro £2.99/person/month or £23.99/person/year
License: MIT · Repo: github.com/Developyn/laver-mcp (created Aug 13, 2026)
Built by: Laver (laver.app)
```

```json
{
  "mcpServers": {
    "laver": {
      "command": "npx",
      "args": ["-y", "@laver/mcp"],
      "env": { "LAVER_API_KEY": "your key here" }
    }
  }
}
```

## Why This Matters for Operators

Laver is one of the few team project management tools whose MCP surface is built for a human and an agent working the same board simultaneously. Three design decisions stand out.

First, **versioned writes with a 409 contract.** Ticket updates, moves, status reorders, wiki replacements and automation edits all take the record's `version`; a conflict comes back as 409 with the current version instead of an overwrite, so the agent re-reads and retries. Comments are deliberately not versioned (last edit wins) and only the author may edit or delete one.

Second, **the key acts as the person.** A workspace-scoped API key created under Admin > API keys inherits exactly its creator's permissions and is revocable without touching the account. Refusals come back verbatim from the same REST API the web app uses, so an agent can act on a real error ("409, re-read and retry") instead of a generic failure.

Third, **context-budget tooling.** Structural reads on busy boards returned 119-180 kB each; the server ships opt-in narrowing parameters (`get_board` with `include_tasks: false`, `get_wiki_tree` with `depth: 1`, `list_tickets` with `include_descriptions: false`) that cut those payloads by 75-99 percent, which matters when an agent polls a board in a loop.

## Tool Groups (59 tools)

- **Reading (11):** `list_workspaces`, `list_boards`, `get_board`, `list_tickets`, `list_workspace_tickets`, `get_ticket`, `get_ticket_comments`, `get_ticket_flow`, `list_custom_fields`, `list_labels`, `search`
- **Writing (15):** `create_ticket`, `update_ticket`, `move_ticket`, `comment_on_ticket`, `update_comment`, `delete_comment`, `mark_comments_read`, `add_subtask`, `update_subtask`, `delete_subtask`, `archive_ticket`, `delete_ticket`, `create_board` (templates: crm, sales-leads), `link_tickets`, `unlink_tickets`
- **Board structure (10):** `create_status`, `update_status`, `reorder_statuses`, `delete_status`, `create_group`, `reorder_groups`, `delete_group`, `create_custom_field`, `update_custom_field`, `delete_custom_field`
- **Labels (4):** `list_labels`, `create_label`, `update_label` (renames everywhere), `delete_label`
- **Attachments (4):** `list_ticket_attachments`, `get_ticket_attachment`, `upload_ticket_attachment`, `delete_ticket_attachment`
- **Wiki (9):** `list_wikis`, `search_wiki`, `get_wiki_tree`, `get_wiki_page`, `get_wiki_page_version`, `append_wiki_page`, `update_wiki_page`, `create_wiki_page`, `restore_wiki`
- **Automations (6):** `list_automations`, `get_automation`, `list_automation_runs`, `create_automation`, `update_automation`, `delete_automation`
- **Published links (1):** `list_published_links` (owner or admin only; taking a link down is deliberately not a tool)

`list_workspace_tickets` is the stand-up read: it answers "what is late" and "what does nobody own" without walking every board. `get_ticket_flow` derives per-column cycle times from ticket history; read the `visits` field rather than summing `by_status` totals across tickets.

## Verification (Aug 30, 2026)

- npm registry: @laver/mcp v0.5.0 published, description matches the submission
- Official MCP registry: listed at v0.5.0 under io.github.Developyn/laver-mcp
- GitHub repo live (MIT, created Aug 13, 2026); README enumerates every tool group with error semantics and a route-coverage file

## Notes and Caveats

- stdio only: no hosted remote endpoint; the server runs where the client starts it (npx) and calls api.laver.app
- New listing: the repo has no stars yet and the vendor is small; treat as early-adopter tooling
- Automations are standing grants: a rule runs as the key's user until disabled or deleted; stop a misbehaving rule with `update_automation` (enabled: false) before deleting, since deletion destroys its run history
- Attachments over 4 MB, or non-text/image files, are written via `save_to` to a path on the machine running the server rather than passed through context
- The REST API is larger than the 59 tools; the difference is tracked in the repo's mcp/route-coverage.js
