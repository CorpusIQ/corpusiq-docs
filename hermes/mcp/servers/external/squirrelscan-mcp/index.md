---
title: "squirrelscan — SEO & Performance Audit MCP for AI Agents"
description: "Audit websites for SEO, performance, security, accessibility, and agent experience. Get exact fixes delivered to your coding agent."
source: github.com/squirrelscan/squirrelscan
stars: 0
language: Unknown
transport: stdio
auth: None
category: SEO & Web Development
last_updated: 2026-07-21
---

# squirrelscan — SEO & Performance Audit MCP for AI Agents

**Website auditing through MCP.** squirrelscan audits websites across SEO, performance, security, accessibility, and "agent experience" — then provides exact fixes your coding agent can implement immediately.

## What It Does for Operators

- **SEO audit** — Meta tags, structured data, content gaps, indexing issues
- **Performance audit** — Core Web Vitals, load times, resource optimization
- **Security audit** — HTTPS, headers, dependency vulnerabilities
- **Accessibility audit** — WCAG compliance, screen reader compatibility
- **Agent Experience audit** — Novel: audits whether your site is agent-friendly (structured data, API discoverability)
- **Actionable fixes** — Not just problems — exact code changes your AI coding agent can apply

## Installation

```bash
git clone https://github.com/squirrelscan/squirrelscan.git
cd squirrelscan
# Follow repo instructions for setup
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "squirrelscan": {
      "command": "node",
      "args": ["path/to/squirrelscan/server.js"]
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `audit_seo` | Full SEO audit with fix recommendations |
| `audit_performance` | Core Web Vitals and load time analysis |
| `audit_security` | Security headers, HTTPS, vulnerability scan |
| `audit_accessibility` | WCAG compliance check |
| `audit_agent_experience` | Agent-friendliness score (structured data, APIs) |
| `get_fixes` | Generate exact code changes for found issues |

*Note: Tool names are approximate. See github.com/squirrelscan/squirrelscan.*

## Operator Use Cases

1. **SaaS Operators** — Weekly automated audit of your landing page + docs site
2. **Agencies** — Audit client sites before delivery. Generate fix tickets for your dev team.
3. **Ecommerce** — Monitor SEO health across product pages and category templates
4. **AI-Native Companies** — The "agent experience" audit ensures your site is discoverable by AI agents

## CorpusIQ Angle

squirrelscan's "agent experience" audit is forward-looking. As AI agents become a significant traffic source, websites need to be machine-readable. Operators using CorpusIQ for business intelligence can use squirrelscan to ensure their public-facing properties are optimized for both human visitors AND AI agents.

## Limitations

- Early-stage project — audit thoroughness TBD
- Requires coding agent to apply fixes (not one-click)
- "Agent experience" audit category is experimental
- May overlap with established tools like Lighthouse, Ahrefs
