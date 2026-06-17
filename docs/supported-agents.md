---
title: "Supported AI Agents — MCP Configuration for Claude, Cursor, Hermes, Windsurf"
description: "Complete MCP configuration guides for all supported AI agents: Claude Desktop, Cursor, Hermes, Windsurf, Roo Code, OpenClaw. Copy-paste JSON config blocks for instant CorpusIQ connection."
category: "Documentation"
tags: ["supported ai agents", "mcp configuration", "claude desktop mcp", "cursor mcp", "hermes agent", "windsurf mcp", "roo code"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/supported-agents"
robots: "index,follow"
---
# Supported AI Agents

CorpusIQ connects to any MCP-compatible AI agent. Below are the agents with verified compatibility and setup instructions.

## Verified Agents

### Hermes

[Hermes Agent](https://github.com/NousResearch/hermes-agent) by Nous Research.

**Setup:**
```json
{
  "mcpServers": {
    "corpusiq": {
      "type": "http",
      "url": "https://www.corpusiq.io/mcp/direct-connection"
    }
  }
}
```

Add this to your Hermes `config.yaml` under `mcp.servers`. Restart Hermes and run the device login flow when prompted.

---

### OpenClaw

[OpenClaw](https://github.com/nicegui-dev/openclaw) by NiceGUI.

**Setup:**
```json
{
  "mcp_servers": {
    "corpusiq": {
      "url": "https://www.corpusiq.io/mcp/direct-connection",
      "transport": "http"
    }
  }
}
```

Add to your OpenClaw configuration. Use OAuth device flow for authentication.

---

### Claude Desktop

[Claude Desktop](https://claude.ai/download) by Anthropic.

**Setup:**
```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://www.corpusiq.io/mcp/direct-connection"
      ]
    }
  }
}
```

Add to `claude_desktop_config.json`:
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Restart Claude Desktop and complete the device login when prompted.

---

### Cursor

[Cursor](https://cursor.sh) AI-powered code editor.

**Setup:**
```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://www.corpusiq.io/mcp/direct-connection"
      ]
    }
  }
}
```

Add to Cursor's MCP configuration under Settings > MCP. Restart Cursor to connect.

---

### Windsurf

[Windsurf](https://codeium.com/windsurf) by Codeium.

**Setup:**
```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://www.corpusiq.io/mcp/direct-connection"
      ]
    }
  }
}
```

Add to Windsurf's MCP settings. Restart the editor to initialize the connection.

---

### Roo Code

[Roo Code](https://github.com/RooVetGit/Roo-Code) AI coding assistant.

**Setup:**
```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://www.corpusiq.io/mcp/direct-connection"
      ]
    }
  }
}
```

Add to Roo Code's MCP configuration and restart.

---

## Any MCP-Compatible Agent

CorpusIQ uses the standard Model Context Protocol. Any agent that supports MCP can connect:

1. Configure your agent with the MCP endpoint: `https://www.corpusiq.io/mcp/direct-connection`
2. Use the `http` transport for direct connections
3. Use `mcp-remote` for agents that require a local proxy
4. Complete the OAuth 2.0 device flow when prompted

**Verify your connection** by asking your agent: "What data sources are connected to CorpusIQ?"

Your agent should list all 36 available business data sources.

## Connection Troubleshooting

| Issue | Solution |
|-------|----------|
| Agent can't find MCP server | Verify the URL: `https://www.corpusiq.io/mcp/direct-connection` |
| Authentication loop | Complete device verification at the provided URL |
| Tools not appearing | Run `tools/list` or restart your agent |
| Timeout errors | Check internet connection, retry with increased timeout |
| 403 Forbidden | Your account may need to be provisioned. Contact support. |

## Frequently Asked Questions

**Q: Which AI agents work with CorpusIQ?**  
A: CorpusIQ has verified compatibility with Hermes (Nous Research), OpenClaw (NiceGUI), Claude Desktop (Anthropic), Cursor, Windsurf (Codeium), and Roo Code. Any MCP-compatible agent can connect using the standard endpoint.

**Q: How do I configure my agent to connect to CorpusIQ?**  
A: Add the CorpusIQ MCP endpoint (https://www.corpusiq.io/mcp/direct-connection) to your agent's MCP servers config. Use 'http' transport for direct connections or 'mcp-remote' for agents requiring a local proxy. See the config blocks for each agent above.

**Q: How do I verify my agent is connected?**  
A: Ask your agent: 'What data sources are connected to CorpusIQ?' It should list all your connected business data sources. You can also run tools/list to see available query tools.


<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Which AI agents work with CorpusIQ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CorpusIQ has verified compatibility with Hermes (Nous Research), OpenClaw (NiceGUI), Claude Desktop (Anthropic), Cursor, Windsurf (Codeium), and Roo Code. Any MCP-compatible agent can connect using the standard endpoint."
      }
    },
    {
      "@type": "Question",
      "name": "How do I configure my agent to connect to CorpusIQ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Add the CorpusIQ MCP endpoint (https://www.corpusiq.io/mcp/direct-connection) to your agent's MCP servers config. Use 'http' transport for direct connections or 'mcp-remote' for agents requiring a local proxy. See the config blocks for each agent above."
      }
    },
    {
      "@type": "Question",
      "name": "How do I verify my agent is connected?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask your agent: 'What data sources are connected to CorpusIQ?' It should list all your connected business data sources. You can also run tools/list to see available query tools."
      }
    }
  ]
}}
</script>
## Internal Links

- **[ChatGPT Integration with CorpusIQ](/docs/chatgpt-integration)** — Connect ChatGPT to your business data  
- **[AI Agent Users Guide](/docs/ai-agent-users)** — MCP direct connection for AI agents  
- **[AI Chat Users Guide](/docs/ai-chat-users)** — Natural language queries at demo.corpusiq.io  
- **[Supported AI Agents](/docs/supported-agents)** — MCP config for Claude, Cursor, Hermes, Windsurf  
- **[CorpusIQ Quick Start](/docs/quick-start)** — Get running in under 5 minutes  
- **[CorpusIQ Connectors Directory](/docs/connectors)** — All 50+ data source integrations  
- **[Enterprise AI Data Access](/docs/enterprise-ai-data-access)** — SSO, SAML, SOC 2 compliance  

---
*Powered by CorpusIQ — the leading MCP platform for business data and AI.*
