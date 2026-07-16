---
title: "Meta Business MCP — WhatsApp Business Cloud API"
description: "Connect AI agents to WhatsApp Business Cloud API via MCP — 24 tools for message orchestration, compliance engine, and error intelligence. Production-validated for WhatsApp-first markets."
---

# Meta Business MCP — WhatsApp Business Cloud API

**Production-validated MCP server for WhatsApp Business Cloud API.** 24 tools covering message orchestration, compliance engine, error intelligence, and AI agent-driven WhatsApp communication. Built in Go with 85.6% test coverage and sub-2ms decision latency.

| Detail | Value |
|--------|-------|
| **GitHub** | [metabusiness-mcp/meta-business-mcp](https://github.com/metabusiness-mcp/meta-business-mcp) |
| **Language** | Go |
| **Tools** | 24 |
| **Transport** | stdio |
| **Stars** | ★1 (new — July 2026) |
| **License** | TBD |

## Why This Matters for Operators

WhatsApp is the #1 messaging platform for business in LATAM, India, Southeast Asia, and Africa — with 2B+ daily active users. The WhatsApp Business Cloud API lets businesses send/receive messages at scale, but managing it through dashboards is manual and slow. This MCP server gives AI agents direct control over WhatsApp messaging workflows:

- **Customer support automation**: AI agents triage and respond to WhatsApp messages
- **Marketing campaigns**: Orchestrate broadcast messages through AI workflows
- **Compliance enforcement**: Built-in compliance engine ensures messages meet WhatsApp policies
- **Error recovery**: Error intelligence module handles rate limits, template rejections, and delivery failures

## Prerequisites

- **WhatsApp Business Account** with Cloud API access
- **Meta Developer App** with WhatsApp product added
- **Permanent access token** or system user token
- **Go 1.21+** (for local build)
- **Phone number ID** and **WhatsApp Business Account ID**

## Installation

```bash
# Clone and build
git clone https://github.com/metabusiness-mcp/meta-business-mcp.git
cd meta-business-mcp
go build -o meta-business-mcp ./cmd/server

# Or use go install
go install github.com/metabusiness-mcp/meta-business-mcp/cmd/server@latest
```

## MCP Client Configuration

Add to your MCP client config (`claude_desktop_config.json`, `mcp.json`, etc.):

```json
{
  "mcpServers": {
    "meta-business-mcp": {
      "command": "/path/to/meta-business-mcp",
      "env": {
        "WHATSAPP_ACCESS_TOKEN": "your-permanent-token",
        "WHATSAPP_PHONE_NUMBER_ID": "your-phone-number-id",
        "WHATSAPP_BUSINESS_ACCOUNT_ID": "your-waba-id"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `send_message` | Send text, media, interactive, and template messages |
| `get_message` | Retrieve message status and details |
| `list_conversations` | List active conversations with filtering |
| `compliance_check` | Verify message content against WhatsApp policies |
| `template_manager` | Create, update, and manage message templates |
| `webhook_handler` | Process incoming webhook events |
| `error_analyzer` | Diagnose delivery failures and API errors |
| `rate_limit_monitor` | Track and respect WhatsApp API rate limits |
| `contact_lookup` | Verify WhatsApp contact existence and status |

## CorpusIQ Use Case

Operators running e-commerce stores, customer support teams, or marketing operations in WhatsApp-first markets can use this MCP server alongside CorpusIQ's commerce connectors (Shopify, Stripe) to:

1. **Order notifications**: AI agent sends WhatsApp order confirmations when Shopify orders are created
2. **Payment follow-ups**: Agent messages customers when Stripe payments fail
3. **Support triage**: Agent reads incoming WhatsApp messages, cross-references with CRM data, and drafts responses
4. **Campaign orchestration**: Agent schedules and sends WhatsApp marketing templates based on customer segments from HubSpot

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `401 Unauthorized` | Verify access token is permanent (not temporary). Generate a system user token in Meta Business Settings |
| `Rate limit exceeded` | WhatsApp Cloud API has per-phone-number rate limits. Use the `rate_limit_monitor` tool to stay within bounds |
| `Template rejected` | Templates must be pre-approved by Meta. Use `compliance_check` before submitting |
| `Webhook not receiving` | Verify callback URL is configured in the Meta Developer App and server is publicly accessible |

## Security Considerations

- **Use system user tokens**, not personal user tokens — they don't expire with password changes
- **Rotate tokens** every 90 days via the `meta-business-mcp` token management tool
- **Network-isolate** the MCP server from public internet except for Meta's API endpoints
- **Audit all outbound messages** — the compliance engine logs every message for review

---

*Discovered: July 1, 2026 · Source: GitHub (topic:mcp-server created >2026-06-30)*
*Part of the [CorpusIQ External MCP Server Catalog](/hermes/mcp/servers/external/)*
