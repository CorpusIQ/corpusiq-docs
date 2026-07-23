---
title: Outside Agent MCP Server
subtitle: Build and publish production-ready AI agents for web, SMS, and phone
source: mcpservers.org
github: https://github.com/santasailab/outside-agent-claude-plugin
created: 2026-07-15
category: AI Agents
stars: 0
tags: [agent-deployment, sms, web, phone, communication, production]
---

# Outside Agent MCP Server

Remote MCP server for **building and publishing production-ready AI agents** that operate on web, SMS, and phone channels. Connect from any coding agent (Claude Code, Cursor, Codex) and deploy agents directly to production channels.

## What It Does

- **Agent Deployment** — Build AI agents in your IDE and deploy to web/SMS/phone
- **Multi-Channel** — Same agent logic serves web chat, SMS text, and phone calls
- **Remote MCP** — No local server needed — connect to hosted endpoint
- **Production-Grade** — Built for production deployment, not just prototyping

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **Customer Support Agent** | Deploy an FAQ agent that answers via web chat + SMS |
| **Phone Answering Agent** | AI agent that answers business calls and routes inquiries |
| **SMS Notifications** | Agent-initiated SMS alerts for order updates, appointments |
| **Multi-Channel Consistency** | Same agent personality across web, SMS, and phone |

## Installation

Remote MCP server — add directly to your MCP client config:

```json
{
  "mcpServers": {
    "outside-agent": {
      "type": "url",
      "url": "https://mcp.outsideagent.io/mcp",
      "env": {
        "OUTSIDE_AGENT_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Auth

API key authentication. Create an account at the Outside Agent platform and generate an API key.

## Tools Provided

- `create_agent` — Define agent persona, knowledge base, and channel configuration
- `deploy_agent` — Deploy agent to specified channels (web, SMS, phone)
- `list_agents` — View all deployed agents and their status
- `get_conversation_logs` — Review agent interactions across channels

## Limitations

- **0 stars, brand new** — Created July 15, 2026. Early stage.
- **SaaS platform dependency** — Agents run on Outside Agent infrastructure, not self-hosted.
- **Pricing unknown** — No public pricing for the platform.
- **Vendor lock-in** — Agent definitions and conversation data live on their platform.

## Operator Verdict

★★ **Useful for rapid deployment but evaluate vendor risk.** The multi-channel deployment (web+SMS+phone from one agent definition) is genuinely valuable. However, the platform dependency means you're betting on Outside Agent's longevity. Good for MVPs and prototypes. For mission-critical agents, prefer self-hosted MCP servers with direct Twilio/WebSocket integration.
