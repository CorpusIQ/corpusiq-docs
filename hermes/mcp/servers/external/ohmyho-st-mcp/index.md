---
title: "ohmyho.st MCP - Hosting, Postgres and Email for Agents"
description: "ohmyho.st is an all-in-one Vercel, Supabase and Resend alternative your coding agent operates: deploy a GitHub app, run managed Postgres, send email and manage domains from one MCP server."
category: "DevOps"
stars: n/a (new listing)
added: 2026-09-28
source: "mcp.so server page (docs.ohmyho.st)"
relevance: ★★★
tags: [deployment, hosting, postgres, transactional-email, domains, devops, stdio-mcp]
---

# ohmyho.st MCP

**Deploy, database and email your agent operates as one platform.** ohmyho.st bundles what most operators buy as three separate services: Vercel-style hosting, Supabase-style managed Postgres and Resend-style transactional email. The MCP server gives Codex, Claude Code, Cursor, Hermes or OpenClaw the tools to host a GitHub app, run its database, send mail and manage domains and budgets, all from one prompt and one credit balance.

```
Server type: Local stdio (npm binary, Node 22+)
Auth: Browser sign-in (ohmyhost login --json); you keep your own auth provider
Install: npm install --global @amerged/ohmyhost-cli @amerged/ohmyhost-mcp
Registry name: io.github.amerged-org/ohmyhost-mcp (Apache-2.0 client)
Tools: deployment, database, email, domain and budget tools with built-in agent skills
Pricing: one credit balance covers hosting, database and email; sign-up is open
Category: DevOps / Hosting, Database and Email platform
Built by: Amerged (ohmyho.st)
```

## Why This Matters for Operators

Small operators who build with AI-assisted tools typically stack three vendors, three bills and three sets of credentials: hosting, database and email. ohmyho.st collapses that into a single platform the agent already operates, which means the agent can go from "deploy this GitHub project" to a live app with a working database, a sender domain and a spend budget without the operator leaving the conversation.

The MCP server also ships task guides the agent reads before acting, so deployment steps follow the vendor's own playbook instead of improvising. That is the same governance pattern CorpusIQ recommends for any agentic workflow: give the agent tools, but make the procedure explicit.

## Tools & Capabilities

| Capability area | What the agent can do |
|---|---|
| Deploy from GitHub | Host Vite, TanStack Start and Next.js apps, with a protected Dev address and a separate Prod |
| Managed Postgres | Run queries, check size and compute, plan Dev-to-Prod schema migrations, export encrypted SQL backups |
| Transactional email | Send and receive through your own sender domain |
| Custom domains | Manage DNS records, HTTPS and readiness checks |
| Usage and budgets | Read credit usage and set spending limits per project |
| Built-in Skills | Task guides the agent reads before acting |
| Support receipts | Bug reports return a receipt ID you can follow up on |

The mcp.so listing publishes no tool table for this server, so capability names above come from the vendor docs (docs.ohmyho.st). Fetch the live tool list from the running server before scripting against specific tool names.

## Installation

```bash
npm install --global @amerged/ohmyhost-cli @amerged/ohmyhost-mcp
ohmyhost login --json
claude mcp add --transport stdio --scope user --env OHMYHOST_ENVIRONMENT=production ohmyho -- ohmyhost-mcp
```

Setup commands for Codex, Cursor, Hermes and OpenClaw are in the vendor's MCP setup guide at docs.ohmyho.st/agents/mcp.

## Configuration

```json
{
  "mcpServers": {
    "ohmyho": {
      "command": "ohmyhost-mcp",
      "env": {
        "OHMYHOST_ENVIRONMENT": "production"
      }
    }
  }
}
```

## Business Relevance

- **Indie founders and operators** replace Vercel + Supabase + Resend with one service the agent runs
- **AI-builder teams** deploy Lovable, Bolt or Cursor-built apps from GitHub without leaving the editor
- **Cost controllers** get one credit balance with per-project spending limits instead of three vendor bills
- **Agent-ops teams** get built-in skills and support receipts, so agent actions are guided and followable

## Integration with CorpusIQ

ohmyho.st handles the build-and-run layer while CorpusIQ handles the business-data layer. Deploy the app with ohmyho.st, then connect its Postgres to the CorpusIQ analytics and CRM connectors so the agent can answer "which project used the most credits?" alongside revenue and pipeline questions in one conversation. For email, pair ohmyho.st transactional mail with a CorpusIQ email connector workflow so outbound messages and inbox threads stay inside the same agent session.

## Limitations

- New listing with no track record yet
- The npm client is Apache-2.0, but the hosted platform itself is not open source
- Requires Node 22+ for the stdio binary
- Listing publishes no tool table; verify live tools against the vendor docs
- You keep your own authentication provider, so auth is your responsibility

## FAQ

### Does it replace my auth provider?

No. You keep your own authentication provider; ohmyho.st supplies hosting, database, email and domains, not user identity.

### Is the platform open source?

The npm client (Apache-2.0) is open source, but the hosted platform is not. The client source ships inside the package.

### Can an agent run the whole stack hands-free?

Yes for deploys, database work, email and domain management within the budgets you set. Sign-in happens once in your browser, after which the agent operates the account through the MCP tools.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
