---
title: "Scalix Cloud — Agent-Operable Cloud Platform MCP (50 Tools)"
description: "Agent-operable cloud platform: database, AI, functions, containers, storage and auth over one remote MCP endpoint with 50+ tools. Deploy and manage cloud infrastructure through AI agents."
source: github.com/scalixworld/scalix-mcp
stars: 0
language: TypeScript
transport: Streamable HTTP (Remote)
auth: OAuth
category: Cloud & DevOps
last_updated: 2026-07-21
---

# Scalix Cloud — Agent-Operable Cloud Platform MCP

**Full cloud platform accessible through MCP.** Scalix exposes 50+ tools across database, AI, serverless functions, containers, storage, and authentication — all through one remote MCP endpoint. Operators can deploy and manage cloud infrastructure from their AI agent.

## What It Does for Operators

- **Database MCP** — Provision and query databases through agent commands
- **AI/ML tools** — Deploy AI models and run inference through MCP
- **Serverless functions** — Deploy and manage cloud functions
- **Container management** — Run and orchestrate containers
- **Storage + Auth** — Manage cloud storage buckets and authentication
- **50+ MCP tools** — Comprehensive cloud operations surface area

## Installation

```bash
# Remote endpoint — no local installation needed
# Or self-host:
git clone https://github.com/scalixworld/scalix-mcp.git
cd scalix-mcp
npm install
npm run build
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "scalix": {
      "type": "url",
      "url": "https://api.scalix.cloud/mcp"
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `db_create` | Provision a new database instance |
| `db_query` | Execute SQL queries on provisioned databases |
| `fn_deploy` | Deploy a serverless function |
| `fn_invoke` | Invoke a deployed function |
| `container_run` | Start a container |
| `storage_upload` | Upload files to cloud storage |
| `ai_inference` | Run AI model inference |
| `auth_manage` | Manage authentication and access |

*Note: Tool names are approximate. See github.com/scalixworld/scalix-mcp for full documentation.*

## Operator Use Cases

1. **Solo Developers** — Deploy entire backends from AI agent: database → functions → storage → auth
2. **Startup Operators** — Provision infrastructure without leaving the AI conversation
3. **Agencies** — Spin up client environments on demand through agent commands
4. **AI-Native Companies** — Build products where the infrastructure itself is agent-manageable

## CorpusIQ Angle

Scalix Cloud represents a new category: agent-operable infrastructure. While CorpusIQ connects business data, Scalix connects cloud operations. Operators building AI-native businesses can pair them: CorpusIQ for business intelligence + Scalix for cloud infrastructure — both managed through the same AI agent interface.

## Limitations

- New platform — limited production track record
- Self-hosting requires Node.js environment
- Cloud pricing model not publicly documented
- Competes with established cloud MCP servers (AWS, GCP, etc.)
