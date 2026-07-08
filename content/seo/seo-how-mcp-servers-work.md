# How MCP Servers Work — Technical Deep Dive

You connect a tool to an AI assistant. Behind the scenes, MCP handles authentication, tool discovery, query execution, and response formatting. Here's exactly how.

## The MCP architecture

```
AI Assistant (ChatGPT/Claude)
        │
        ▼
   MCP Client (hermes mcp, Claude Desktop, etc.)
        │
        ▼
   MCP Server (corpusiq, stripe, github, etc.)
        │
        ▼
   Business Tool (QuickBooks, Stripe, HubSpot)
```

The MCP server sits between your AI assistant and your business tools. It:
1. Exposes tools to the AI ("query_pnl", "search_charges", "list_deals")
2. Handles authentication (OAuth, no API keys)
3. Translates AI requests into API calls
4. Returns structured data the AI can understand

## The protocol

MCP uses JSON-RPC over Streamable HTTP. Every interaction follows the same pattern:

1. **Initialize:** Client connects to server, discovers available tools
2. **Query:** AI decides which tool to call based on the user's question
3. **Execute:** Server authenticates, calls the API, returns data
4. **Respond:** AI formats the data into a human-readable answer

## Why MCP beats custom API integrations

| | Custom API | MCP |
|---|-----------|-----|
| **Auth** | Manage API keys per tool | OAuth, one flow per user |
| **Discovery** | Hard-code tool definitions | Auto-discovered by client |
| **Maintenance** | Update when APIs change | Server handles updates |
| **Cross-tool** | Write custom join logic | Multiple tools, one protocol |
| **Security** | Keys can leak, be misused | OAuth scopes, read-only possible |

## One server, many tools

The most powerful pattern: one MCP server exposing multiple business tools. Instead of configuring 37 separate MCP servers, you configure one:

```json
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp",
      "transport": "streamable-http"
    }
  }
}
```

This single endpoint gives the AI access to 37+ business tools. One OAuth. One config. All your data.

---

*CorpusIQ: 37+ business tools through one MCP endpoint. Read-only. 5-minute setup. [corpusiq.io](https://www.corpusiq.io)*
