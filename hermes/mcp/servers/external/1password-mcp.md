---
title: "1Password MCP Server ★ Official (Beta)"
description: "Official 1Password MCP server (beta): lets Claude Code, Codex, Cursor and Kiro manage 1Password Environments through secure authorization prompts."
category: mcp
tags: [mcp-server, security, secrets-management, 1password, official, devops, ai-agents]
last_updated: 2026-11-16
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/1password-mcp/"
robots: "index,follow"

---

# 1Password MCP Server ★ Official (Beta) - New July 17

The 1Password MCP server bridges MCP-compatible AI agents (Claude Code, Codex, Cursor, Kiro and any stdio MCP client) to 1Password Environments - letting agents create environments, list variables, and manage secrets without ever reading or exposing the secret values.

This is the first major secrets-management platform to ship an official MCP server, marking a significant milestone in AI agent security infrastructure.

**Source:** mcpservers.org (discovered July 17, 2026)
**Category:** Security / DevOps / Secrets Management
**Author:** 1Password (Official)
**Docs:** https://www.1password.dev/environments/mcp-server
**Status:** Beta (released July 2026)

## Key Innovation: Agent-Managed Secrets Without Exposure

The core design principle is unlike any other MCP server: **the agent never sees the secrets.** The MCP server acts as a secure bridge that:

- **Creates Environments** - provision new 1Password Environments from an MCP client
- **Lists variable names** - enumerate environment variables without revealing values
- **Manages secrets** - update, rotate, and organize secrets through authorized processes
- **Authorizes via prompts** - every sensitive operation triggers a human authorization prompt

Secrets remain in 1Password and are only accessed by authorized processes at runtime. The MCP client (your AI agent) orchestrates secrets management while 1Password enforces the security boundary.

## Requirements

- A 1Password account with Environments access
- The 1Password desktop app, installed and signed in
- An MCP client that supports stdio transport: Claude Code, Codex (Mac and Linux), Cursor, Kiro, or any other stdio MCP client

## Setup

### Step 1: Create an Environment in 1Password

The MCP server reads Environment names and secret names only. Secret values stay in 1Password and are never returned to the client, even when an agent requests them.

### Step 2: Configure Your MCP Client

The server runs locally as the `1password-mcp` command. For Claude Code, install the 1Password Developer Tools plugin, which registers the MCP configuration for you:

```
/plugin marketplace add 1Password/1password-claude-plugin
/plugin install 1password@1password
```

Restart Claude Code, then enter `/mcp` to confirm the 1Password server is connected.

For any other stdio client, add the `1password-mcp` command to its configuration file. JSON config files:

```json
{
  "mcpServers": {
    "1password": {
      "command": "1password-mcp"
    }
  }
}
```

TOML config files:

```toml
[mcp_servers.1password]
command = "1password-mcp"
```

Then restart your client.

## Business Relevance

This is a landmark MCP server for operators running AI agents in production:

1. **Security-first agent operations:** For the first time, you can let AI agents manage infrastructure secrets without granting them read access to those secrets. This solves the fundamental tension between agent autonomy and security.

2. **Auditable agent actions:** Every secrets operation goes through 1Password's authorization prompts, creating an audit trail of what the agent attempted and what was approved.

3. **Enterprise-ready patterns:** 1Password's approach - agent orchestrates, platform enforces - sets the pattern for enterprise MCP integrations. Expect similar designs from AWS Secrets Manager, HashiCorp Vault, and Azure Key Vault.

4. **Environment provisioning at scale:** Operators managing multiple deployment environments can let agents handle the mechanical work of creating and organizing environments while maintaining zero-trust on secret values.

## Use Cases for Business Operators

- **CI/CD pipeline setup:** Agent provisions environment variables for new deployment stages without human copying of secrets
- **Secret rotation automation:** Agent initiates rotation workflows, human approves, secrets update without agent exposure
- **Multi-environment management:** Agent organizes variables across dev/staging/production environments
- **Onboarding automation:** Agent creates environments for new team members or services

## Limitations (Beta)

- Documented client setup covers Claude Code, Codex, Cursor, and Kiro, plus a generic stdio path for any other MCP client. Codex support is Mac and Linux only
- Beta status - API may change before GA
- Requires 1Password Environments (separate from standard 1Password vaults)

---

*Discovered in daily MCP scan July 17, 2026. [← Back to External MCP Catalog](/hermes/mcp/servers/external)*
