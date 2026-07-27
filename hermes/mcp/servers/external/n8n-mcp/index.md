# n8n MCP Server ★★★

**Source:** mcpservers.org · **Last updated:** July 26, 2026 (evening sweep)  
**GitHub:** [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)  
**Endpoint:** Local stdio (`npx n8n-mcp`) or remote deployment  
**Auth:** None required (read-only documentation access)  
**Category:** Workflow Automation / Developer Tools

---

## Overview

The **n8n MCP server** bridges n8n's workflow automation platform with AI models. It gives AI assistants structured access to n8n's complete node ecosystem — 2,175 nodes (827 core + 1,348 community) with documentation, properties, operations, and real-world examples. AI coding agents can now understand, recommend, and scaffold n8n workflows directly.

## Key Capabilities

| Resource | Coverage |
|----------|----------|
| **Core nodes** | 827 — full properties and operations |
| **Community nodes** | 1,348 (1,195 verified) — with source filters |
| **Node properties** | 99% coverage with detailed schemas |
| **Node operations** | 63.6% coverage of available actions |
| **Documentation** | 87% coverage from official n8n docs (including AI nodes) |
| **AI tools** | 265 AI-capable tool variants detected with full documentation |
| **Templates** | 2,352 workflow templates with 99.96% AI metadata coverage |
| **Real-world examples** | 156 ranked configurations from popular templates |

## What Agents Can Do

- **Discover nodes** — Search 2,175 nodes by name, category, or capability
- **Read documentation** — Get full node docs, properties, and input/output schemas
- **Recommend workflows** — Given a business requirement, suggest appropriate n8n nodes and template workflows
- **Validate configurations** — Check node parameters against their schemas before deployment
- **Scaffold workflows** — Generate n8n workflow JSON from natural language descriptions
- **Search templates** — Find matching templates for common automation patterns

## Integration

### 1. Claude Desktop

```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": ["n8n-mcp"]
    }
  }
}
```

### 2. Hermes Agent (config.yaml)

```yaml
mcp:
  servers:
    n8n:
      command: npx
      args: ["n8n-mcp"]
```

### 3. Cursor / VS Code

Add to your MCP configuration file with the stdio transport using `npx n8n-mcp`.

## Business Operator Use Cases

1. **Workflow Discovery** — "What nodes can I use to connect my PostgreSQL database to Slack?" — agent finds the right nodes and shows wiring
2. **Automation Scaffolding** — "Build me a workflow that monitors Stripe for failed payments and posts to a Slack channel" — agent generates the workflow JSON
3. **Template Matching** — "I need to sync HubSpot deals to Google Sheets" — agent finds the closest template from 2,352 options
4. **Node Documentation Lookup** — "What parameters does the HTTP Request node accept for OAuth2?" — agent retrieves the complete schema
5. **AI Pipeline Design** — Agent recommends the 265 AI-capable nodes for building LLM-powered automation pipelines

## Pricing

- **n8n MCP server:** Free (open source, community-maintained)
- **n8n itself:** Free (self-hosted) or n8n Cloud from €20/month
- No API keys required for read-only documentation access

## Community & Support

- 22.4K+ GitHub stars on n8n main repo
- Active community-maintained MCP server
- Sponsorship available for the MCP server maintainer

## Verdict

★★★★★ — Essential for any business operator running n8n. Turns your AI coding agent into an n8n workflow expert that can recommend, validate, and scaffold automations from 2,175 nodes across 2,352 templates. The documentation coverage (87%) and template metadata (99.96%) make this a production-ready knowledge layer for AI-assisted workflow automation.
