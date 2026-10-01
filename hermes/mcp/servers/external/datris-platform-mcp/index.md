---
title: "Datris Data Platform MCP - Governed Data for Agents"
description: "Open-source Datris exposes 73 capabilities over one MCP server so agents can acquire, validate and land data with provenance, without holding your keys."
category: Data & Analytics
stars: n/a (open-source platform, datris.ai; AGPL-3.0)
added: 2026-10-01
source: "mcp.so server page (datris-platform-oss)"
relevance: ★★★
tags: [data-platform, data-engineering, etl, mcp, self-hosted, open-source, provenance, credentials, agents]
---

# Datris Data Platform MCP

**A governed control plane for the data your agents move.** Datris sits beside your warehouse and lake rather than replacing them, and puts data acquisition, validation and loading behind one MCP surface. Agents ask Datris for data; Datris finds it, acquires it, validates it, lands it in the stores you already run, and returns it with provenance, over MCP, without ever holding your keys.

```
Server type: Remote (HTTP/SSE) or local stdio bridge
Auth: none by default (USE_API_KEYS=false); x-api-key when auth is enabled
Endpoint: http://localhost:3000/sse (self-hosted) via npx mcp-remote
Tools: 73 capabilities behind one MCP server
Pricing: free and open source (AGPL-3.0); self-hosted
Category: Data & Analytics
Built by: datris.ai
```

## Why This Matters for Operators

Every agent stack reaches the point where the agent needs real data from somewhere other than the chat. Without a control plane, each agent hand-rolls its own taps, holds its own credentials, validates inconsistently, and leaves no record of what it did. Datris moves that work behind a single governed surface: one interface instead of seventy-three integrations, credentials referenced by name rather than pasted into a prompt, and a recorded run for every job.

The credential model is the design decision worth noting. The agent references a secret by name and never holds a key, and agent-generated code runs in an isolated container with no keys inside it. For operators letting agents touch production data stores, that split is the difference between a pilot and something you can run unattended.

## Tools & Capabilities

Datris organizes work as an operating loop rather than a flat tool list:

| Stage | What it covers |
|---|---|
| Acquire | AI-generated data taps |
| Validate | Plain-English validation rules |
| Land | Multi-destination pipelines |
| Observe | Provenance and job state per run |
| Explain & Repair | AI error explanation |

The platform exposes **73 capabilities** behind a single MCP server. The public listing does not enumerate every tool identifier, so the surfaces are described by stage above rather than by exact tool name. Durable state, pipelines and sync bookmarks live in the platform rather than in the conversation, so regenerating a script does not lose a pipeline's place, and every generated script version is tracked in git.

## Installation

The stack runs on Docker. The installer pulls pre-built images and starts everything into `./datris`:

```bash
curl -fsSL https://get.datris.ai/install.sh | sh
```

A laptop-friendly minimal install runs eight small containers with no model download by setting three values in `.env`: `TEI_ENABLED=0`, `EMBEDDING_PROVIDER=openai`, and optionally `POSTGRES_ENABLED=0`. There is also a single-file Compose option that works natively in PowerShell on Windows.

From a git clone:

```bash
git clone https://github.com/datris/datris-platform-oss.git
cd datris-platform-oss
cp .env.example .env   # add ANTHROPIC_API_KEY and/or OPENAI_API_KEY
docker compose up -d
```

UI on `http://localhost:4200`, API on `http://localhost:8080`.

## Configuration

Connect an MCP client to the bundled server on port 3000 through the `mcp-remote` stdio bridge. The client then appears in the Datris UI Agent Monitor with live tool-call streaming:

```json
{
  "mcpServers": {
    "datris": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://localhost:3000/sse", "--transport", "sse-only"]
    }
  }
}
```

No API key is required when `USE_API_KEYS=false` (the OSS default). If your instance enables auth, append `"--header", "x-api-key:<your key>"` to the `args` array. Requires Node.js on your `PATH`. A CLI is also available:

```bash
brew tap datris/tap
brew install datris
datris ingest data.csv --dest postgres
```

## Business Relevance

- **Data and analytics engineers** put agent-driven ingestion behind one governed surface with provenance for every run
- **Operations teams** validate incoming data against plain-English rules before it lands in the warehouse
- **Security-conscious operators** let agents work on production stores while credentials stay brokered and out of the agent's reach
- **Platform teams** self-host on-prem, in any cloud, or on a laptop with open-source infrastructure (MinIO, PostgreSQL, MongoDB, Kafka, Vault)

## Integration with CorpusIQ

Data landing and revenue reporting belong together. A composed workflow: Datris governs how agent-acquired data reaches the warehouse, and CorpusIQ supplies the business metrics that sit on top of it from its GA4, Stripe, Shopify and QuickBooks connectors, so an operator can trace an ingested dataset through to the revenue it explains. For operators running both, the data-moving question and the business-outcome question sit in one session.

## Limitations

- **Self-hosting is required.** Datris OSS is not a managed service; you run the Docker stack and own its operation.
- **An LLM key is needed for AI-generated taps.** The stack expects at least one of `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, or the Azure OpenAI variables, or `AI_PROVIDER=bedrock`.
- **The public listing does not expose a fetchable tool list**, so this guide describes capabilities by stage rather than by exact tool identifier.
- **License is AGPL-3.0**, which carries source-availability obligations for network use; review it against your own distribution model before embedding.

## FAQ

### Do I need the full ten-container stack?

No. Three `.env` settings (`TEI_ENABLED=0`, `EMBEDDING_PROVIDER=openai`, `POSTGRES_ENABLED=0`) cut it to eight small containers with no model download and roughly 3.5 GB of memory.

### Does the agent hold my credentials?

No. The agent references a secret by name and never holds a key, and agent-written code runs in an isolated container with no keys inside it.

### Is it a hosted service?

No. Datris OSS self-hosts; the installer and Compose files run on your own machine, cloud, or on-prem.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Settra MCP - Governed Tabular Data for Agents](/hermes/mcp/servers/external/settra-mcp/)
- [Databar MCP - 100+ Provider Enrichment](/hermes/mcp/servers/external/databar-mcp/)
