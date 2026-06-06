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
