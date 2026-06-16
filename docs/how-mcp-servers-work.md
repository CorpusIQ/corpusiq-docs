---
title: "How MCP Servers Work: Technical Deep Dive into Transport, Tools, and Authentication | CorpusIQ"
description: "A technical deep dive into how MCP servers operate: transport layers, tool discovery, resource management, prompt templates, authentication flows, and the JSON-RPC protocol that powers AI-to-data connections."
category: MCP Education
tags: [MCP Server, Model Context Protocol, JSON-RPC, Transport Layer, AI Architecture, Tool Discovery]
last_updated: 2026-06-16
canonical: https://www.corpusiq.io/docs/how-mcp-servers-work
robots: index,follow
---

# How MCP Servers Work: A Technical Deep Dive

Understanding the internals of an MCP server reveals why this architecture represents such a significant leap over traditional API integrations. This guide walks through every layer of the MCP stack — from the transport mechanism that moves bytes between client and server, to the tool discovery system that lets AI models navigate data sources they've never seen before, to the authentication model that keeps business data secure.

## The MCP Protocol Stack

MCP is built on a layered architecture that separates concerns cleanly:

**Layer 1: Transport** — How bytes move between client and server. MCP supports two transport mechanisms: stdio (standard input/output for subprocess communication) and HTTP with Server-Sent Events (for networked deployments).

**Layer 2: JSON-RPC 2.0** — The message format. Every MCP message is a JSON-RPC 2.0 request, response, or notification. This is the same remote procedure call protocol used by Ethereum nodes, VS Code's language server protocol, and countless other systems.

**Layer 3: MCP Primitives** — The domain objects. Tools, resources, prompts, and sampling. These are the abstractions that make MCP useful for AI integration rather than just another RPC framework.

**Layer 4: Application Logic** — The actual data connectors. This is where CorpusIQ's 30+ business integrations live — the code that translates MCP tool calls into QuickBooks API requests, Shopify GraphQL queries, or Google Analytics reports.

## Transport Layer in Detail

### stdio Transport

In stdio mode, the MCP client launches the MCP server as a child process. All communication flows over stdin and stdout as newline-delimited JSON-RPC messages. The client writes requests to the server's stdin and reads responses from the server's stdout.

```
Client (Host Application)
    |
    | spawns subprocess
    v
MCP Server Process
    | writes JSON-RPC to stdout
    | reads JSON-RPC from stdin
```

Advantages of stdio transport:
- **Simplicity** — no network configuration, no port management, no TLS certificates
- **Security** — communication never leaves the local machine
- **Lifecycle management** — when the host exits, the server process exits automatically

Limitations:
- **Single-machine only** — can't distribute across hosts
- **One client per server** — no connection sharing
- **Process overhead** — each client connection requires a separate server process

### HTTP Transport with SSE

In HTTP mode, the MCP server runs as a standalone HTTP service. The client connects over the network and communicates via HTTP POST for requests and Server-Sent Events for streaming responses and server-initiated notifications.

```
Client (Host Application)
    |
    | HTTP POST (JSON-RPC requests)
    | SSE stream (responses + notifications)
    v
MCP Server (HTTP Service)
```

Advantages of HTTP transport:
- **Network accessibility** — clients and servers can run on different machines
- **Connection sharing** — multiple clients can connect to one server instance
- **Standard infrastructure** — works with load balancers, reverse proxies, and cloud deployment

CorpusIQ uses HTTP transport for its cloud deployment, enabling thousands of concurrent client connections through standard load-balanced infrastructure.

## The JSON-RPC 2.0 Message Format

Every MCP message conforms to JSON-RPC 2.0. A request looks like this:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "list_shopify_orders",
    "arguments": {
      "status": "open",
      "limit": 50
    }
  }
}
```

A successful response:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Found 23 open orders totaling $47,230.15..."
      }
    ]
  }
}
```

The key MCP methods defined by the protocol:

| Method | Purpose |
|--------|---------|
| `initialize` | Handshake: client and server exchange capabilities |
| `tools/list` | Discover available tools |
| `tools/call` | Execute a tool with arguments |
| `resources/list` | Discover available resources |
| `resources/read` | Read a resource's content |
| `prompts/list` | Discover available prompt templates |
| `prompts/get` | Retrieve a prompt template |

## Tool Discovery: How AI Models Navigate Unknown Systems

Tool discovery is the MCP feature that most distinguishes it from traditional APIs. Here's how it works in practice:

**1. Initialization Handshake.** When a client connects to a server, it sends an `initialize` request. The server responds with its capabilities — which protocol features it supports, which MCP version it implements, and instructions for subsequent setup.

**2. Tool Enumeration.** The client calls `tools/list`. The server returns an array of tool definitions, each containing:

```json
{
  "name": "list_shopify_orders",
  "description": "List Shopify orders with optional status and date filters. Returns order ID, total price, customer name, and fulfillment status.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "status": {
        "type": "string",
        "enum": ["open", "closed", "cancelled", "any"],
        "description": "Filter orders by status. Default: 'any'."
      },
      "limit": {
        "type": "integer",
        "description": "Maximum orders to return. Default: 50."
      },
      "created_at_min": {
        "type": "string",
        "description": "ISO 8601 date string for earliest creation date."
      }
    }
  }
}
```

**3. AI Reasoning.** The AI model receives these tool definitions as part of its context. When the user asks "how many unfulfilled orders do we have from this week?", the model:
- Reads the `list_shopify_orders` description: "List Shopify orders with optional status and date filters"
- Maps "unfulfilled" to the fulfillment status concept
- Maps "this week" to appropriate date parameters
- Constructs the appropriate `tools/call` request

**4. Execution and Response.** The server processes the tool call against the live API, returns structured data, and the AI model synthesizes a natural language answer.

This is fundamentally different from how traditional API integrations work. In a traditional setup, a developer must anticipate every possible question, write code to handle each one, and hard-code the mapping between user intent and API endpoints. With MCP, the AI model does this mapping dynamically based on the tool descriptions.

## Resources: Structured Data Access

Resources are MCP's mechanism for exposing static or semi-static data that the AI model might want to reference. Unlike tools, which execute operations, resources represent data objects that can be read directly.

Examples of resources:
- Database schemas (table definitions, column types)
- API documentation (endpoint descriptions, parameter formats)
- Configuration files (feature flags, environment settings)
- Reference data (product catalogs, price lists, tax rates)

Resources are identified by URIs and can contain either text or binary data. The `resources/list` method returns available resources, and `resources/read` retrieves their content.

In CorpusIQ's implementation, resources include canonical business facts — user-declared definitions that ensure consistency across queries. When a user declares "MRR is calculated as the sum of active subscription plan amounts," that definition becomes a resource the AI model can reference in any relevant query.

## Prompts: Reusable Interaction Templates

Prompts are pre-built conversation templates that guide the AI model toward producing structured, consistent outputs. They're defined server-side and can include arguments for customization.

A prompt definition looks like:

```json
{
  "name": "monthly_revenue_report",
  "description": "Generate a monthly revenue report with breakdown by product category",
  "arguments": [
    {
      "name": "month",
      "description": "Month to report on (YYYY-MM format)",
      "required": true
    }
  ]
}
```

When a user asks for a report, the AI model can discover this prompt template, fill in the arguments, and produce a consistently structured output. This is particularly valuable for recurring business reports where format consistency matters.

## Authentication and Security

MCP itself doesn't mandate a specific authentication scheme — it's a transport-level concern that each implementation handles. However, the protocol provides a standard pattern for authentication through the `initialize` response, where servers can advertise their authentication requirements.

CorpusIQ's authentication model:

**OAuth 2.0 for cloud services.** Each business platform (Shopify, QuickBooks, HubSpot, etc.) is connected through OAuth 2.0. Users authorize CorpusIQ to access their data with explicitly scoped permissions. Tokens are stored encrypted at rest and rotated automatically.

**Read-only by default.** Every connector defaults to read-only access. Write operations require explicit opt-in at both the OAuth scope level and the MCP server configuration level. This dual-gate approach prevents accidental data modification.

**Token isolation.** Each user's OAuth tokens are cryptographically isolated. No user can access another user's data, even within the same CorpusIQ organization.

**Audit logging.** Every tool call is logged with timestamp, user identity, tool name, and parameters. This creates a complete audit trail for compliance and debugging.

## How CorpusIQ Extends the MCP Standard

While the base MCP protocol provides the foundation, CorpusIQ adds several enterprise-grade features:

**Unified server architecture.** Instead of running separate MCP server processes for each data source, CorpusIQ runs a single MCP server that manages 30+ connectors. This reduces operational complexity and enables cross-source queries.

**Cross-source orchestration.** When a user asks a question that spans multiple data sources — like "compare ad spend from Meta with revenue from Shopify" — CorpusIQ orchestrates multiple tool calls, normalizes the responses, and presents unified results to the AI model.

**Canonical context.** CorpusIQ maintains user-declared business definitions (canonical facts) that the AI model can reference. This ensures that terms like "active customer" or "monthly recurring revenue" are interpreted consistently across all queries.

**Metric specifications.** Users can declare how key metrics should be computed, and CorpusIQ enforces those definitions. When the AI model asks "what's our MRR?", it gets the MRR computed according to the user's definition — not whatever interpretation the model happens to apply.

**Truth sources.** Users can designate authoritative documents (spreadsheets, PDFs, database tables) as the source of truth for specific questions. When the AI model encounters a question that matches a truth source, it consults the designated document rather than computing from raw data.

## Performance Characteristics

MCP server performance depends primarily on the underlying data source APIs. The protocol overhead itself is minimal — JSON serialization and deserialization account for milliseconds of latency.

CorpusIQ's performance optimizations:

**Connection pooling.** HTTP connections to data source APIs are pooled and reused, eliminating TCP handshake overhead on repeated calls.

**Parallel execution.** When a query requires multiple tool calls against independent data sources, CorpusIQ executes them concurrently rather than sequentially.

**Response streaming.** Large result sets are streamed rather than buffered completely in memory, enabling queries against datasets of any size.

**Intelligent caching of metadata.** API schemas, tool definitions, and other metadata that changes infrequently are cached to avoid redundant API calls.

## Frequently Asked Questions

**Q: Can I build my own MCP server?**
A: Yes. MCP is an open protocol with SDKs available in Python, TypeScript, and other languages. The protocol specification is publicly documented. Building a custom MCP server lets you expose proprietary systems to any MCP-compatible AI client.

**Q: How does MCP handle errors?**
A: MCP uses standard JSON-RPC error codes. Tool execution errors return structured error objects with machine-readable codes and human-readable messages. The AI model can interpret these errors and adjust its approach — for example, retrying with different parameters or asking the user for clarification.

**Q: What happens if a data source is unavailable?**
A: The MCP server returns an error to the client, which the AI model can communicate to the user in natural language. CorpusIQ includes timeout handling and retry logic for transient failures.

**Q: How are rate limits handled?**
A: CorpusIQ's MCP server tracks rate limits for each connected platform and implements backpressure. If a query would exceed rate limits, the server throttles requests and communicates the delay to the client.

**Q: Can MCP servers stream partial results?**
A: Yes. Through the HTTP+SSE transport, servers can stream partial results as they become available. This is particularly useful for large reports or long-running queries.

**Q: Is MCP suitable for real-time applications?**
A: MCP queries execute against live data and typically return in seconds. While not suitable for sub-second latency requirements (like trading systems), it's more than fast enough for business intelligence, reporting, and operational queries.

**Q: How does MCP compare to GraphQL?**
A: GraphQL is a query language for APIs — you write queries to request specific fields. MCP is a protocol for AI agents to discover and use tools. They solve different problems. MCP could use GraphQL as the underlying transport for some data sources.

**Q: Does MCP support webhooks or event-driven patterns?**
A: The base MCP protocol is request-response oriented. However, the HTTP+SSE transport supports server-initiated notifications, which could be used for event-driven patterns. This area of the protocol is actively evolving.

## Internal Links

- [What Is an MCP Server? Complete Introduction](/docs/what-is-an-mcp-server)
- [MCP vs Zapier: Real-Time vs Polling](/docs/mcp-vs-zapier)
- [MCP vs API Integrations: AI-Native Interface](/docs/mcp-vs-api-integrations)
- [MCP Security Best Practices](/docs/mcp-security-best-practices)
- [Benefits of MCP for Business](/docs/benefits-of-mcp-for-business)
- [MCP for Enterprise: Scale and Compliance](/docs/mcp-for-enterprise)
- [MCP for Operations: Workflow Automation](/docs/mcp-for-operations)

## Schema Markup Suggestions

```json
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "How MCP Servers Work: Technical Deep Dive into Transport, Tools, and Authentication",
  "description": "A technical deep dive into how MCP servers operate: transport layers, tool discovery, resource management, prompt templates, and authentication flows.",
  "author": {
    "@type": "Organization",
    "name": "CorpusIQ"
  },
  "datePublished": "2026-06-16",
  "proficiencyLevel": "Intermediate",
  "about": {
    "@type": "Thing",
    "name": "Model Context Protocol"
  }
}
```

---

**Suggested URL:** `https://www.corpusiq.io/docs/how-mcp-servers-work`

**Meta Title:** How MCP Servers Work: Technical Deep Dive | CorpusIQ

**Meta Description:** Technical deep dive into MCP server architecture: transport layers, JSON-RPC protocol, tool discovery, resource management, prompt templates, and authentication.

**H1:** How MCP Servers Work: A Technical Deep Dive
