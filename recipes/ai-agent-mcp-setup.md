# Recipe: Connect CorpusIQ to AI Coding Agents (Claude Code, Cursor, Hermes)

AI coding agents like Claude Code, Cursor, and Hermes can query your business data directly through CorpusIQ. This recipe shows you how to set it up so your agent can answer questions about revenue, customers, campaigns, and operations while you work.

## Why Connect Your Business Data to a Coding Agent

AI coding agents already help you write code, review PRs, and manage infrastructure. With CorpusIQ connected, they can also:

- Answer "how many customers signed up last week" without leaving the terminal
- Pull real revenue numbers into a PR description
- Check campaign performance before deploying marketing changes
- Verify inventory levels when building e-commerce features
- Pull actual customer counts when writing database migrations

## Setup: Claude Code (Anthropic)

Claude Code supports MCP servers natively. Add CorpusIQ to your Claude Code MCP config.

**Config file location:** `~/.claude/claude_desktop_config.json` or use `claude mcp add`.

```bash
# Add CorpusIQ as an MCP server
claude mcp add corpusiq \
  --url https://mcp2.corpusiq.io/mcp \
  --header "Authorization: Bearer YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your key from [corpusiq.io/settings/api](https://corpusiq.io/settings/api).

**Verify it works:**
```
> What's our total Shopify revenue this month?
```
Claude Code will call the CorpusIQ Shopify tool and return live data.

## Setup: Cursor

Cursor supports MCP servers through its settings. Add CorpusIQ to your Cursor MCP configuration.

1. Open Cursor Settings → MCP → Add New MCP Server
2. Enter:
   - **Name:** CorpusIQ
   - **URL:** `https://mcp2.corpusiq.io/mcp`
   - **Auth Header:** `Bearer YOUR_API_KEY`

Or add it directly to `~/.cursor/mcp.json`:
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

Restart Cursor after adding the config.

## Setup: Hermes Agent (Nous Research)

Hermes supports MCP servers via its config.yaml. Add CorpusIQ under the `mcp_servers` section.

**Config file:** `~/.hermes/config.yaml`

```yaml
mcp_servers:
  corpusiq:
    url: https://mcp2.corpusiq.io/mcp
    headers:
      Authorization: "Bearer YOUR_API_KEY"
```

Then restart Hermes:
```bash
hermes restart
```

Verify with:
```
hermes: which tools do you have from corpusiq?
```

## Setup: Windsurf

Add to `~/.codeium/windsurf/mcp_config.json`:
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

## Useful Agent Prompts

Once connected, try these prompts with your agent:

**Revenue & Finance**
- "Pull our Shopify revenue by product category for Q2"
- "Compare this month's QuickBooks profit to last month"
- "Which customers have unpaid invoices over 30 days?"

**Marketing & Growth**
- "What's our Meta Ads ROAS this week vs last week?"
- "Show me our top 5 Google Ads campaigns by conversion rate"
- "Which email campaigns in Klaviyo drove the most revenue?"

**Operations**
- "How many support tickets are open in HubSpot right now?"
- "What's our inventory level for the top 10 Shopify SKUs?"
- "Show me this week's Stripe refunds over $100"

**Development**
- "Before I deploy this pricing change, what's our current average order value?"
- "Pull actual customer counts by plan tier for this migration PR"
- "What's our API error rate from PostHog for the last 24 hours?"

## Troubleshooting

If your agent says it can't find the CorpusIQ tools:

1. **Restart the agent.** Most MCP clients cache tool lists on startup
2. **Check your API key.** Make sure it hasn't expired at corpusiq.io/settings/api
3. **Verify connectors.** CorpusIQ only exposes tools for connected data sources. Log into corpusiq.io and make sure at least one connector is active
4. **Check the URL.** It must be exactly `https://mcp2.corpusiq.io/mcp`

## Security Note

Your API key grants access to all your connected business data. Store it securely:
- Use environment variables where possible
- Never commit the key to a public repository
- Rotate keys regularly from the CorpusIQ dashboard
- Use different API keys for development and production agents
