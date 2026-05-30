# CorpusIQ MCP architecture

This page is for developers. It explains what Model Context Protocol is,
how CorpusIQ implements it, and how to connect any MCP-compatible client
to CorpusIQ's live-data layer.

---

## What is MCP?

Model Context Protocol (MCP) is an open standard for connecting AI
assistants to external data sources and tools. It was introduced by
Anthropic and is now supported by Claude, a growing list of third-party
LLM clients, and an ecosystem of server implementations.

The short version: instead of copy-pasting data into a chat window, you
run an MCP server that the AI can call like a function. The AI asks for
data, the server fetches it, the AI gets structured results. No prompt
engineering, no CSV uploads, no stale context.

MCP servers expose **tools** (callable functions with typed inputs and
outputs) and optionally **resources** (documents or data the AI can
read). CorpusIQ exposes tools only — one tool per connector action.

Official spec: https://modelcontextprotocol.io

---

## CorpusIQ's MCP endpoint

```
https://mcp2.corpusiq.io/mcp
```

This is a hosted MCP server. You do not run it locally. You point your
MCP client at this URL and authenticate with your CorpusIQ credentials.
CorpusIQ handles everything behind that endpoint: connector auth, rate
limiting, data normalization, and the skills engine.

**Transport:** HTTP with Server-Sent Events (SSE) for streaming.
**Auth:** Bearer token (your CorpusIQ JWT, obtained after sign-in).

---

## Architecture overview

```
Your LLM client (Claude, ChatGPT, custom agent)
        |
        | MCP protocol (JSON-RPC over HTTP/SSE)
        v
https://mcp2.corpusiq.io/mcp   <-- CorpusIQ MCP server
        |
        +-- Connector layer (31 connectors)
        |       Shopify, QuickBooks, GA4, HubSpot, Meta Ads,
        |       Klaviyo, Stripe, Slack, Gmail, and 20+ more.
        |       Each connector holds an encrypted OAuth token
        |       scoped to your account only.
        |
        +-- Skills engine
        |       Pre-built runbooks that orchestrate multi-connector
        |       queries (e.g. "executive-snapshot" pulls from 6
        |       connectors, joins the data, and returns a unified
        |       business health summary).
        |
        +-- Canonical facts store
                User-declared business facts (pricing, team, decisions)
                that ground AI answers in stable, verified context.
```

---

## The connector layer

Each of CorpusIQ's 31 connectors is an isolated module that:

1. Holds one encrypted OAuth token per user account.
2. Exposes a set of typed MCP tools (e.g. `get_orders`, `list_campaigns`,
   `run_report`).
3. Translates MCP tool calls into vendor API calls, handles pagination,
   and normalizes the response into consistent JSON.

Connectors are **read-only by design**. CorpusIQ requests read scopes
only during OAuth and has no write paths in any connector. This is not
a configuration option — it is an architectural constraint.

When you call a tool like `get_orders`, the flow is:

```
MCP tool call  -->  CorpusIQ connector  -->  Shopify REST API
                                         <--  JSON orders array
       structured result  <--  normalized JSON
```

The LLM never touches vendor credentials. The connector is the only
layer that holds and uses the OAuth token.

---

## The skills engine

Some questions require more than one connector. "What is my true CAC?"
requires every ad platform, GA4, and Shopify or QuickBooks — at minimum
four separate API calls, with a join step.

The skills engine encodes these multi-step workflows as **runbooks**:
ordered sequences of tool calls with join logic and presentation rules.
When an LLM calls `invoke_skill` with a skill name like
`executive-snapshot`, the skills engine:

1. Calls the appropriate connectors in the correct order.
2. Joins the results (e.g. ad spend by date + Shopify revenue by date).
3. Returns a unified, structured result to the LLM.

Skills are the main reason CorpusIQ answers broad business questions
better than a raw tool list. The LLM doesn't have to figure out which
five connectors to call and how to join them — the runbook already knows.

Available skills include:

- `executive-snapshot` — business health across finance, sales, and marketing.
- `ad-spend-truth-report` — cross-platform ROAS from actual revenue data.
- `financial-command-center` — cash, AR, expenses, anomalies.
- `ecommerce-command-center` — store health, LTV, CAC, inventory.
- `email-lifecycle-intel` — email channel health across all ESPs.
- `board-update-drafter` — investor-update format from live actuals.
- `customer-health-scorecard` — per-account health scoring.

Call `invoke_skill` or `list_skills` to discover and run them.

---

## The canonical facts store

CorpusIQ includes a small key-value store for user-declared facts:
pricing, team composition, product positioning, past decisions. These
are written explicitly by the user (not inferred), and the AI reads them
at the start of business questions to ground its answers.

MCP tools: `canonical_context_get`, `canonical_facts_get`,
`canonical_facts_set`, `canonical_decisions_add`.

This is CorpusIQ's answer to the "the AI doesn't know my business"
problem. Instead of embedding documents, you declare facts once and they
persist across sessions.

---

## Security model

- **Read-only everywhere.** No connector has write access. This is
  enforced at the connector layer, not just by policy.
- **Per-user token isolation.** OAuth tokens are stored encrypted and
  scoped per user account. One user's token cannot be used by another.
- **No data retention.** CorpusIQ does not store API responses. Each
  tool call fetches live data from the vendor and returns it directly.
  Nothing is cached on CorpusIQ's servers beyond the OAuth token itself.
- **Revocable at any time.** Disconnect a connector from CorpusIQ's
  settings panel. The token is deleted immediately. You can also revoke
  from the vendor's side (Shopify admin, Google account settings, etc.).

---

## Connecting Claude Desktop

Claude Desktop supports MCP servers natively via `claude_desktop_config.json`.

Add CorpusIQ as a remote server:

```json
{
  "mcpServers": {
    "corpusiq": {
      "type": "sse",
      "url": "https://mcp2.corpusiq.io/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_CORPUSIQ_JWT"
      }
    }
  }
}
```

Replace `YOUR_CORPUSIQ_JWT` with the token from your CorpusIQ account
settings. After saving the file and restarting Claude Desktop, the
CorpusIQ tools will appear in Claude's tool list automatically.

Config file locations:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

---

## Connecting ChatGPT (via Actions or custom GPT)

ChatGPT supports MCP-style integrations through Custom GPT Actions.

1. In the GPT editor, go to **Configure > Actions > Add action**.
2. Import the CorpusIQ OpenAPI schema (available at
   `https://mcp2.corpusiq.io/openapi.json`).
3. Set authentication to **Bearer token** and paste your CorpusIQ JWT.
4. Save and test with a prompt like "list my Shopify orders from last week."

---

## Connecting any MCP client

Any client that implements the MCP specification can connect to
CorpusIQ. The endpoint supports standard MCP over HTTP+SSE.

Example using the TypeScript MCP SDK:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { SSEClientTransport } from "@modelcontextprotocol/sdk/client/sse.js";

const transport = new SSEClientTransport(
  new URL("https://mcp2.corpusiq.io/mcp"),
  {
    requestInit: {
      headers: {
        Authorization: `Bearer ${process.env.CORPUSIQ_JWT}`,
      },
    },
  }
);

const client = new Client({ name: "my-agent", version: "1.0.0" }, {});
await client.connect(transport);

// List available tools
const { tools } = await client.listTools();

// Call a tool
const result = await client.callTool({
  name: "get_orders",
  arguments: { limit: 50 },
});
```

Python MCP SDK example:

```python
from mcp import ClientSession
from mcp.client.sse import sse_client
import os

async with sse_client(
    "https://mcp2.corpusiq.io/mcp",
    headers={"Authorization": f"Bearer {os.environ['CORPUSIQ_JWT']}"}
) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        tools = await session.list_tools()
        result = await session.call_tool("get_orders", {"limit": 50})
```

---

## Tool naming conventions

CorpusIQ tool names follow the pattern `connector_action`:

- `get_orders` — Shopify or Amazon Seller orders.
- `list_campaigns` — Meta Ads or Google Ads campaigns.
- `run_report` — GA4 custom report.
- `get_profit_loss` — QuickBooks P&L.
- `invoke_skill` — run a multi-connector skill by name.
- `resolve_connector` — discover which tools to call for a given intent.

Call `resolve_connector` with a plain-English intent to get back the
exact tool schemas relevant to your question. This is the fastest way
to explore what's available without reading every tool definition.

---

## Rate limits and pagination

CorpusIQ does not impose additional rate limits beyond the underlying
vendor's own limits. Each connector respects the vendor's rate limit
headers and backs off automatically.

All list tools (`get_orders`, `list_campaigns`, etc.) support `limit`
and offset-style pagination (`offset`, `starting_after`, `page_index`
depending on the connector). See each tool's schema for the exact
parameter names.

---

## Further reading

- [Connectors explained](connectors-explained.md) — how OAuth and
  connector auth works.
- [Skills explained](skills-explained.md) — deeper dive on the
  runbook/skills engine.
- [Prompts: MCP developer queries](../prompts/mcp-developer-queries.md)
  — 20+ example prompts for developers.
- [Quickstart](../quickstart/) — fastest path from zero to first answer.
