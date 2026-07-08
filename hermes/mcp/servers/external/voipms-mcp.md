---
title: "VoIP.ms MCP — Business Telephony for AI Agents"
description: "Manage business phone numbers, send/receive SMS, handle voicemail, configure call flows, and access billing — all from AI agents. Complete VoIP.ms platform operations over MCP."
category: mcp
tags: [mcp-server, voip, telephony, sms, communication, phone-numbers, call-flows, business-phone]
last_updated: 2026-07-08
---

# VoIP.ms MCP Server ★ New (July 2 PM)

## Overview

VoIP.ms MCP (`voipms-mcp.ecliptical.io`) is the first business telephony MCP server, exposing the full VoIP.ms platform to AI agents. Manage phone numbers (DIDs), send and receive SMS, check voicemail, configure call flows and IVRs, query billing and usage — all from any MCP-compatible client. Business operators can now delegate phone system management, SMS communications, and telephony operations to AI agents without logging into the VoIP.ms portal.

**Key advantage**: Full VoIP.ms API surface over MCP — phone numbers, SMS, voicemail, call routing, billing, all in one server.

## Key Features

- **Phone number management**: Search, purchase, configure, and release DIDs across 60+ countries
- **SMS**: Send SMS, receive SMS, query message history, manage SMS-enabled DIDs
- **Voicemail**: Check voicemail messages, configure voicemail-to-email, manage greetings
- **Call flows**: Create and modify IVR menus, call forwarding rules, time-based routing, ring groups
- **Billing**: Query account balance, retrieve call detail records (CDRs), check usage
- **Sub-accounts**: Manage reseller sub-accounts — create, configure, bill

## Installation

```bash
# Remote SSE — no local install needed
hermes mcp add voipms --url https://voipms-mcp.ecliptical.io
```

## Configuration

```json
{
  "mcpServers": {
    "voipms": {
      "url": "https://voipms-mcp.ecliptical.io",
      "transport": "sse"
    }
  }
}
```

API credentials are configured through the VoIP.ms account — the MCP server handles authentication transparently.

## Business Relevance

- **Customer Support**: AI agents can provision phone numbers for new customers, route calls to support teams, and send SMS notifications — all programmatically
- **Sales Outreach**: Automate SMS follow-ups and call tracking for lead nurturing campaigns
- **Operations**: Monitor call volumes, track CDR costs, and alert on unusual usage patterns through AI-driven observability
- **Reseller Management**: VoIP resellers can manage sub-accounts, provision numbers, and handle billing through AI agents
- **IVR Automation**: Deploy and modify call flows and IVR menus via natural language — "route after-hours calls to voicemail and send a transcript via email"

## Integration with CorpusIQ

VoIP.ms MCP adds telephony to CorpusIQ's communication stack, complementing existing email (Gmail/Outlook via PortEden and HimAlaya), WhatsApp (Meta Business MCP, Neuron), and physical mail (PostAgent). Together, operators get an omnichannel communication layer:

- **Unified Communications**: AI agents manage email, WhatsApp, SMS, and voice from a single orchestration point
- **Lead Response**: Inbound calls → AI agent checks CRM (Attio/OnePageCRM) → sends personalized SMS follow-up → logs interaction
- **Alerting**: Combine VoIP.ms call data with Drumbeats monitoring — "if uptime monitor fails, call the on-call engineer and send SMS to the team"

The remote SSE transport pattern aligns with CorpusIQ's existing MCP integrations for zero-friction deployment.

## Limitations

- VoIP.ms-specific — requires a VoIP.ms account
- Remote-hosted — depends on `voipms-mcp.ecliptical.io` uptime
- No WebRTC/softphone — call control only, not real-time audio streaming
- Pricing and number availability determined by VoIP.ms platform

## See Also

- [Meta Business MCP — WhatsApp Business Cloud API](/hermes/mcp/servers/external/meta-business-mcp/)
- [KaiCalls — AI Phone Secretary](/hermes/mcp/servers/external/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
