---
title: "Cal.com MCP — Scheduling Automation for AI Agents"
description: "Connect Cal.com scheduling to Hermes Agent. Create, manage, and query bookings, availability, and event types directly from any AI agent. Official MCP from Cal.com."
category: mcp
tags: [mcp-server, calcom, scheduling, calendar, productivity, booking, automation]
last_updated: 2026-07-03
---

# Cal.com MCP Server ★ New (July 3)

## Overview

Cal.com MCP (`calcom-mcp`) brings the leading open-source scheduling platform directly into AI agents. Create event types, check availability, book meetings, and manage your entire scheduling infrastructure — all through natural language. Official MCP server from Cal.com.

**Key advantage**: Eliminate the back-and-forth of scheduling. AI agents can book meetings, check calendars, and manage availability without leaving the conversation.

## Key Features

- **Event type management**: Create, update, and configure meeting types with custom durations, locations, and availability
- **Booking operations**: Check availability in real-time and book meetings directly
- **Calendar sync**: Query connected calendars (Google, Outlook, iCloud) for conflicts
- **Team scheduling**: Manage round-robin, collective, and managed event types for teams
- **Webhook & workflow**: Trigger automations on booking events
- **Hosted endpoint**: Official remote MCP at `mcp.cal.com` — no local installation needed

## Installation

```bash
# Add to Hermes (remote endpoint)
hermes mcp add calcom --url https://mcp.cal.com/mcp

# Authenticate (OAuth flow — opens browser)
hermes mcp auth calcom
# → Authorize Cal.com access
# → Done. Scheduling tools available.
```

## Manual Configuration

```json
{
  "mcpServers": {
    "calcom": {
      "type": "sse",
      "url": "https://mcp.cal.com/mcp",
      "headers": {
        "Authorization": "Bearer ${CALCOM_API_KEY}"
      }
    }
  }
}
```

## Prerequisites

1. **Cal.com Account**: Sign up at [cal.com](https://cal.com) (free tier available)
2. **API Key**: Generate from Settings → Developer → API Keys
3. **Connected Calendar**: At least one calendar connected (Google, Outlook, etc.)

## Business Use Cases

1. **Client Meeting Automation**: AI agents can find mutual availability and book client meetings in one conversation
2. **Sales Scheduling**: Qualify leads → check SDR calendar → book discovery call — all agent-driven
3. **Interview Coordination**: HR agents can schedule multi-participant interviews across interviewer calendars
4. **Service Delivery**: Consultants can expose booking links, check availability, and confirm appointments via agent
5. **Internal Operations**: Team members ask AI agent "when's our next standup free?" and get booked instantly

## Business Relevance

Cal.com is the scheduling backbone for thousands of businesses. Adding MCP support means every AI agent can now participate in scheduling workflows — not just read calendars. This is infrastructure-level: every operator who uses Cal.com gets AI scheduling for free.

## Limitations

- Remote endpoint requires API key authentication (OAuth coming)
- Team features require Cal.com Teams plan
- Calendar sync limited to connected calendars (no arbitrary ICS support yet)
- Rate limits apply per API key tier

## See Also

- Granola MCP — for AI meeting notes integration
- Google Calendar MCP — for direct Google Calendar access
- CorpusIQ MCP — for cross-platform business data (CRM, email, analytics)
