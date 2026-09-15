---
title: "AgendaForge MCP - Event Operations for AI Agents"
description: "Official remote MCP for AgendaForge, the AI-native event management platform: 53 tools read and manage events, sessions, speakers, agendas, CFP forms and submissions, sponsors, ticketed attendees and email sends, with every write proposed for a human to approve in-app. OAuth 2.1, nothing to install."
category: Productivity
stars: n/a (hosted)
added: 2026-08-27
source: "mcp.so feed (agendaforge-50742c)"
relevance: ★★
tags: [events, event-management, conferences, cfp, speakers, attendees, remote-mcp]
---

# AgendaForge MCP

**Official hosted remote MCP server (Streamable HTTP, OAuth 2.1) for the AgendaForge event management platform.** AgendaForge's MCP exposes the whole event back office to an AI assistant: organizations and events, sessions and agendas grouped by day and room, speakers and sponsors, CFP forms and submissions, review progress, registration stats, ticketed attendees, email templates and activity, and CRM contacts. Reads are direct; writes - contact imports, notes, speaker reminders and messages - are proposed by the agent and approved by a human inside the product, with a pending-approvals list the assistant can check.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1, nothing to install
Endpoint: https://mcp.agendaforge.app/mcp
Tools: 53
Pricing: Platform feature; see agendaforge.app
Docs: https://agendaforge.app/developers
Category: Productivity
```

## Why This Matters for Operators

Running a conference means living in the event platform: scheduling, speaker wrangling, CFP triage, sponsor updates, attendee counts, email status. AgendaForge MCP moves that back office into the assistant an organizer already uses. **The approval model is the standout: the agent can draft a speaker email, file a contact import or add a CRM note, but nothing goes out until an organizer approves it in-app - and `list_pending_approvals` shows exactly what is waiting.** Schedule conflicts are checkable in bulk (`check_schedule_conflicts` takes up to 20 proposed placements without changing the schedule), and submission content is explicitly treated as untrusted data.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_my_orgs` / `list_events` / `get_event` | Organizations, events, and one event's overview with live counters |
| `list_sessions` / `get_session` / `get_agenda` | Sessions with speaker confirmation state; agenda grouped by day and room |
| `list_forms` / `list_submissions` / `get_review_progress` | CFP forms, submissions with status, review rounds and pending decisions |
| `list_speakers` / `list_sponsors` / `list_speaker_tasks` | Speaker rosters, sponsor tiers and booth flags, portal tasks with due dates |
| `list_attendees` / `get_registration_stats` | Ticketed attendees; registration stats and ticketing rail |
| `get_email_activity` / `list_email_templates` / `draft_email` | Email send status; template names; safe render-without-send previews |
| `search` / `semantic_search` / `search_contacts` | Keyword, metered hybrid vector search, and paged contact search |
| `check_schedule_conflicts` | Bulk conflict check for up to 20 proposed placements |
| `import_contacts` / `add_contact_note` / `send_speaker_reminder` / `send_speaker_message` | Approval-gated writes: nothing executes until an organizer approves |
| `list_pending_approvals` | The coordinator's approval queue with tool name and summary |

53 tools in total; the listing documents the full set at the developers page.

## Installation

```bash
claude mcp add agendaforge --transport http https://mcp.agendaforge.app/mcp
```

Codex, Cursor and VS Code setups follow the same URL. OAuth sign-in happens once per client; permission filtering follows the signed-in user's organization roles.

## Configuration

```json
{
  "mcpServers": {
    "agendaforge": {
      "type": "http",
      "url": "https://mcp.agendaforge.app/mcp"
    }
  }
}
```

## Business Relevance

- **Conference organizers** run scheduling, speaker ops and CFP triage from one assistant
- **Event teams** check conflicts in bulk and approve agent-proposed emails in-app
- **Sponsor and partner managers** keep tiers, booths and custom fields current in conversation
- **Community managers** track attendees, email delivery and CRM notes without the dashboard

## Integration with CorpusIQ

AgendaForge owns the event back office; CorpusIQ owns the business numbers around it. Ticket revenue from AgendaForge's registration stats can be reconciled against Stripe and QuickBooks in CorpusIQ to close the books on an event, while attendee lists feed HubSpot-based follow-up sequences that CorpusIQ tracks through to pipeline. For operators who run conferences as a growth channel, the pair answers "how is the event running" (AgendaForge) and "what is it earning" (CorpusIQ) from the same agent thread.

## Limitations

- New listing - no public adoption track record yet
- Writes are approval-gated by design: the agent proposes, a human approves in-app
- Single-event scoping for some tools; registration counts not yet in get_event stats
- Platform-specific: only useful to teams running events on AgendaForge
- Semantic search is metered

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
