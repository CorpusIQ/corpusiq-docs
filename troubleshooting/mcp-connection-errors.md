# MCP Connection Errors — Troubleshooting Guide

The most common issues when connecting CorpusIQ to Claude Desktop, ChatGPT, Cursor, or any MCP client. Start here before escalating to support.

## Symptom: "MCP server not found" or "Connection refused"

**What it means:** Your MCP client cannot reach the CorpusIQ server.

**Check these first:**

1. **Is the URL correct?** The CorpusIQ MCP server URL is:
   ```
   https://mcp2.corpusiq.io/mcp
   ```
   Not `mcp.corpusiq.io` or `api.corpusiq.io`. Verify the exact URL in your config.

2. **Is your internet working?** Run this from your terminal:
   ```bash
   curl -I https://mcp2.corpusiq.io/mcp
   ```
   You should see `HTTP/2 200`. If you get a timeout or connection refused, check your firewall or VPN.

3. **Is your MCP client config correct?** For Claude Desktop, the config file lives at:
   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

   The correct format:
   ```json
   {
     "mcpServers": {
       "corpusiq": {
         "url": "https://mcp2.corpusiq.io/mcp",
         "headers": {
           "Authorization": "Bearer YOUR_API_KEY"
         }
       }
     }
   }
   ```

## Symptom: "401 Unauthorized" or "Authentication failed"

**What it means:** Your API key is missing, expired, or wrong.

**Fix:**
1. Go to [corpusiq.io/settings/api](https://corpusiq.io/settings/api) and copy your API key
2. Verify the key starts with `ciq_`
3. In your MCP config, make sure the header name is exactly `Authorization` and the value is `Bearer YOUR_KEY` (with the word "Bearer" followed by a space)
4. After updating the config, restart your MCP client completely (quit and reopen, not just reload)

## Symptom: "MCP Server requires OAuth" or "Device login required"

**What it means:** You are connecting with a device or CLI tool that needs OAuth authentication instead of an API key.

**Fix:**
1. Use the device authorization flow: run your MCP client, it will display a URL and a code
2. Open the URL in a browser, enter the code
3. Log in with your CorpusIQ account
4. The MCP client will automatically receive a token

For CLI tools using device login, the config looks like:
```json
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp",
      "auth": "oauth"
    }
  }
}
```

## Symptom: "Tool not found" or "No tools available"

**What it means:** Authentication worked but CorpusIQ isn't exposing any tools to your client.

**Common causes:**
1. **No connectors configured.** Log into corpusiq.io and connect at least one data source (Shopify, QuickBooks, HubSpot, etc.). CorpusIQ only exposes tools for connected sources.
2. **Client caching.** Restart your MCP client completely. Some clients cache the tool list and won't pick up changes until restarted.
3. **Trial expired.** Check your account status at corpusiq.io/settings/billing. Expired trials cannot access tools.

## Symptom: "Timeout" or "Request took too long"

**What it means:** Your query is taking longer than the MCP client's timeout limit.

**Fix:**
1. For complex cross-source queries, try breaking them into smaller questions
2. Check if one of your connectors is slow. Disconnect and reconnect the slowest one
3. Increase the timeout in your MCP client if it supports custom timeouts

## Symptom: "Rate limit exceeded" or "429 Too Many Requests"

**What it means:** You're making too many requests too quickly.

**Fix:**
1. Wait 60 seconds and try again. CorpusIQ rate limits reset every minute
2. Spread your queries out instead of firing them rapidly
3. If you consistently hit rate limits, upgrade your plan at [corpusiq.io/pricing](https://corpusiq.io/pricing)

## Still stuck?

If none of these fixes your issue, email support with:
- The exact error message (copy and paste, don't paraphrase)
- Which MCP client you're using (Claude Desktop, Cursor, ChatGPT, etc.)
- Your operating system
- What connector(s) you're trying to use
- The query you ran when the error occurred
