# Neuron — WhatsApp MCP Integration Guide

## Overview
Neuron provides 120+ MCP tools for WhatsApp automation: AI chatbots, broadcast campaigns, contact management, knowledge bases, and newsletters. First MCP-native WhatsApp marketing platform.

**Website:** https://neuron.ng  
**Category:** Communication / Marketing Automation  
**Transport:** Streamable HTTP  

## Business Use Cases
- **Customer support chatbots**: Deploy AI agents that respond to WhatsApp messages
- **Broadcast campaigns**: Send bulk WhatsApp messages to contact lists
- **Contact management**: Sync and manage WhatsApp contacts via AI agents
- **Newsletter automation**: Schedule and send WhatsApp newsletters
- **Knowledge base Q&A**: AI agents answer customer questions from your knowledge base

## Setup

### Prerequisites
- A Neuron account (sign up at neuron.ng)
- Neuron API credentials

### MCP Client Configuration

```json
{
  "mcpServers": {
    "neuron": {
      "url": "https://api.neuron.ng/mcp",
      "transport": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_NEURON_API_KEY"
      }
    }
  }
}
```

### For Claude Desktop
Add the above configuration to your `claude_desktop_config.json`.

### For Cursor / VS Code
Add to your MCP configuration in settings.

### For Hermes
```json
{
  "mcpServers": {
    "neuron": {
      "url": "https://api.neuron.ng/mcp",
      "transport": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_NEURON_API_KEY"
      }
    }
  }
}
```

## Key Tools (120+ total)

| Tool Category | Examples |
|--------------|----------|
| **Chatbots** | Create, deploy, manage WhatsApp chatbots |
| **Broadcasts** | Send bulk messages, schedule campaigns |
| **Contacts** | Import, segment, manage contact lists |
| **Knowledge Base** | Upload docs, manage Q&A pairs |
| **Newsletters** | Create, schedule, track WhatsApp newsletters |
| **Analytics** | Message delivery, open rates, response tracking |

## Why This Matters for Operators

WhatsApp has 2B+ users and is the #1 business messaging platform in:
- **LATAM** (Brazil, Mexico, Colombia)
- **India** (500M+ users)
- **Southeast Asia** (Indonesia, Philippines)
- **Africa** (Nigeria, South Africa, Kenya)

If you do business in these markets, WhatsApp is not optional — it's where your customers are. Neuron brings WhatsApp automation into your AI agent workflow for the first time.

## Pricing
Check neuron.ng for current pricing. Platform typically offers tiered plans based on message volume and feature set.

## Alternatives
- **Official WhatsApp Business API**: Direct Meta integration (requires business verification, more complex setup)
- **Twilio MCP** (if available): Broader communication platform, WhatsApp is one channel
- **Custom webhook bots**: Build your own, but lose the 120+ pre-built tools

## Security Notes
- API keys provide full account access — store securely
- WhatsApp has strict anti-spam policies — use broadcasts responsibly
- Consider read-only mode for initial testing
- Review Neuron's data handling and privacy policy before connecting production data

---

*Guide created June 28, 2026. Check neuron.ng/docs for latest setup instructions.*
