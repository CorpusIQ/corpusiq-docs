# Example: Add CorpusIQ MCP to Claude Desktop

**Type:** Configuration
**Applies to:** Claude Desktop (macOS and Windows)
**Prerequisite:** Active CorpusIQ account with at least one connector configured

---

## What This Does

Adds the CorpusIQ MCP server to your Claude Desktop configuration so you can
query your connected data sources directly from Claude. Once configured, Claude
can access your CorpusIQ connectors (Shopify, GA4, HubSpot, etc.) in real time
during conversations.

---

## Prerequisites

1. Claude Desktop installed (download at https://claude.ai/download)
2. CorpusIQ account at https://app.corpusiq.io
3. Your CorpusIQ API key (Settings → API Keys → Create Key)
4. At least one connector configured and authorized in CorpusIQ

---

## Step 1: Locate the Claude Desktop Config File

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

If the file does not exist, create it. If it exists, you'll merge into it.

---

## Step 2: Add CorpusIQ to the Config

Open `claude_desktop_config.json` in a text editor and add the CorpusIQ server
entry under `mcpServers`. Replace `YOUR_API_KEY` with your actual CorpusIQ API key.

```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y",
        "@corpusiq/mcp-server"
      ],
      "env": {
        "CORPUSIQ_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

If you already have other MCP servers in your config, add `corpusiq` as an
additional entry alongside them:

```json
{
  "mcpServers": {
    "existing-server": {
      "command": "...",
      "args": ["..."]
    },
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y",
        "@corpusiq/mcp-server"
      ],
      "env": {
        "CORPUSIQ_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

---

## Step 3: Restart Claude Desktop

Quit Claude Desktop completely and reopen it. On macOS, use Cmd+Q to ensure
it fully quits rather than just closing the window.

---

## Step 4: Verify the Connection

In a new Claude conversation, type:

```
What CorpusIQ connectors do I have connected?
```

Claude should respond with a list of your configured connectors. If it does,
the MCP server is working.

---

## Expected Output

```
You have the following CorpusIQ connectors configured:
- Shopify (connected, last sync: 2 minutes ago)
- Google Analytics 4 (connected, last sync: 5 minutes ago)
- HubSpot (connected, last sync: 1 minute ago)

You can ask me to query any of these sources directly.
```

---

## Troubleshooting

**Claude doesn't show CorpusIQ tools:**
- Confirm the JSON is valid (no trailing commas, properly nested)
- Verify your API key is correct (no extra spaces)
- Check that `npx` is available in your terminal: `npx --version`
- On macOS, if npx isn't found, add your Node path to the config:
  ```json
  "env": {
    "CORPUSIQ_API_KEY": "YOUR_API_KEY",
    "PATH": "/usr/local/bin:/usr/bin:/bin"
  }
  ```

**Authentication error from CorpusIQ:**
- Regenerate your API key in CorpusIQ Settings → API Keys
- Ensure the key has not been scoped to specific connectors only

**Connector shows as disconnected:**
- Re-authorize the connector in CorpusIQ app at https://app.corpusiq.io/connectors
- OAuth tokens expire — reconnecting takes under 30 seconds

---

## Next Steps

Once connected, try a cross-source query:

```
Pull last week's Shopify revenue and compare it to my GA4 paid traffic sessions.
What was the revenue per paid session?
```

See the [recipes/](../recipes/) directory for more query patterns.
