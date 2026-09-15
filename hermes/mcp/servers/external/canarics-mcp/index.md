---
title: "Canarics MCP - AI Call Analysis and Voice Agents for Sales Teams"
description: "Remote MCP server from Canarics that lets a sales team's own AI assistant operate the phone system: minute usage, agent roster, call summaries with scores and sentiment, daily stats, caller history, consent-gated AI callbacks, and keyless signup tools that provision a trial with a demo voice agent generated from the company website."
category: Communication
stars: n/a (new listing)
added: 2026-09-10
source: mcp.so feed
relevance: ★★★
tags: [voice, telephony, call-analytics, sales, ai-voice-agent, remote-mcp, eu-hosted]
---

# Canarics MCP

**Remote MCP server (Streamable HTTP, stateless)** - Canarics runs AI voice agents that answer and make phone calls for sales and service teams, and analyzes every recorded human call: summary, quality score, sentiment, next steps. This MCP server lets a team's own AI assistant operate the phone system directly. EU-hosted, read-only by design: no transcripts, no prompt editing, no cold-call API. Listed in the official MCP registry as `com.canarics/canarics`.

```
Server type: Remote (hosted, Streamable HTTP, stateless)
Auth: Team API key (cnr_..., created in the Canarics dashboard), or keyless signup tools
Endpoint: https://canarics.com/mcp
Registry: com.canarics/canarics (Official MCP Registry)
Docs for agents: https://canarics.com/api-for-ai-assistants.html
```

## Tools

With a team API key:

| Tool | What it returns |
|---|---|
| `get_usage` | Minutes used vs plan this billing cycle, and the hard cap |
| `list_agents` | The team's AI voice agents (number, language, voice, transfer target) |
| `list_calls` | Call log summaries with scores, sentiment, missed/recovered status |
| `list_conversations` | Conversations handled by the AI voice agents |
| `get_daily_call_stats` | Per-day rollups up to 90 days, in your timezone |
| `get_contact` | Cross-call history for one caller |
| `get_upgrade_options` / `create_upgrade_checkout` | Plans and a hosted payment link a human opens |
| `request_callback` | Schedule the team's voice agent to call a known customer back (callbacks-scoped key, outbound plan; consent-gated, never a cold-calling API) |

With no key at all: `start_signup` and `check_signup_status`, so an assistant can set Canarics up for a company with no account yet. The human claims the signup with one link (sign in, verify phone, accept terms); the trial provisions itself with a demo voice agent generated from the company website, and the assistant receives a read-only API key when it is live.

## Connection

```
{
  "mcpServers": {
    "canarics": {
      "type": "http",
      "url": "https://canarics.com/mcp",
      "headers": { "Authorization": "Bearer cnr_YOUR_API_KEY" }
    }
  }
}
```

## Security by Design

- Keys are read-only by default, scoped to one team, revocable in one click, stored only as hashes.
- Responses pass strict field allowlists: no transcripts, no credentials, never another team's data.
- Callbacks only reach numbers with prior call history, capped per day, inside calling hours.
- Everything runs and stays in the EU (Cloud Run, europe-central2).

## Verification (Sep 10, 2026 night sweep)

Endpoint `https://canarics.com/mcp` live-probed over JSON-RPC: keyless initialize answered with server info (canarics v1.0.0), and keyless `tools/list` captured the two signup tools exactly as documented - `start_signup`, `check_signup_status`. Fully live-verified.

## See Also

- [DialNexa MCP - Voice AI Agents and Confirmed Outbound Calls](/docs/hermes/mcp/servers/external/dialnexa-mcp)
- [VoIP.ms MCP - Business Telephony for AI Agents](/docs/hermes/mcp/servers/external/voipms-mcp)
- [VoIPstudio MCP - Call Analytics for QA and Operations](/docs/hermes/mcp/servers/external/voipstudio-mcp)
