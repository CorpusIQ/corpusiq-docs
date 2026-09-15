---
title: Vaultwarden MCP - Self-Hosted Password Vault Access
description: Connects Claude or any MCP client to a self-hosted Vaultwarden or Bitwarden password vault through the official Bitwarden CLI. 15 tools search logins, generate passwords and prepare edits that only save when you confirm. Secrets never enter the conversation unless explicitly approved.
category: Security
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★
tags: [passwords, secrets, bitwarden, vaultwarden, security, claude, self-hosted]
---

# Vaultwarden MCP - Self-Hosted Password Vault Access

**MCP server (stdio, desktop-window approvals)** - gives Claude or any MCP client access to a self-hosted Vaultwarden or Bitwarden vault by driving the official Bitwarden CLI. Search logins, look them up, add new ones and edit them from a chat window, with a card UI that keeps passwords hidden behind dots and a copy button. Claude never receives a password without an explicit per-request desktop approval, and nothing changes until the human presses Save. Not affiliated with Bitwarden or Vaultwarden - a personal project that drives the published CLI.

```
Server type: stdio (local)
Auth: Bitwarden CLI session (desktop window for master password)
Endpoint: local process - fixed to your vault instance at install time
Tools: 15 (vault CRUD, search, generation, approval gates)
Pricing: free, open source - requires a Vaultwarden or Bitwarden server
Category: Security
Built by: ShadowsDistant (github.com/ShadowsDistant/Vaultwarden-MCP)
```

## Why This Matters for Operators

Operators accumulate credentials across dozens of services, and the two available failure modes are both bad: sharing a vault password with an agent defeats the vault entirely, and pasting secrets into chat logs leaks them into transcripts. This server splits the difference with a card-based approval model: the agent can search the vault, see item names and usernames, generate passwords and prepare edits - but a secret is only released into the conversation when the human approves it in a desktop window, once per request.

**The design constraint is explicit: Claude cannot create, edit or trash anything until you press Save or Confirm in the card, deletes go to the trash where the vault keeps them 30 days, and the vault server address is fixed at install time so an agent cannot redirect it.** The one-time code, notes and passwords stay behind the card's copy buttons, and the clipboard clears itself after 30 seconds by default.

For a solo operator or small team that self-hosts Vaultwarden, this is the difference between an agent that helps with logins and an agent that can exfiltrate them.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `vault_status` | Whether the vault is signed in, locked or unlocked, and which instance it uses |
| `vault_login` | Sign in, in a window on your desktop |
| `vault_unlock` | Unlock, in a desktop window, then show the vault |
| `vault_lock` | Lock immediately and forget the session key |
| `vault_sync` | Pull the latest contents from the server |
| `vault_search` | Find items by name, site or folder (names and hosts only, no usernames in bulk) |
| `vault_get_item` | One item in full, minus every secret |
| `vault_list_folders` | Folders with the ids used to file or filter |
| `vault_generate_password` | Generate a password or passphrase into the card, not the conversation |
| `vault_create_login` | Prepare a new login for you to save |
| `vault_edit_item` | Prepare a change for you to confirm, shown as before-and-after |
| `vault_trash_item` | Prepare to move an item to the trash, for you to confirm |
| `vault_restore_item` | Bring an item back out of the trash |
| `vault_reveal_secret` | Ask you, in a desktop window, to release one secret into the conversation |

A second set of card-only tools (read secret on click, copy to clipboard, save draft) is app-only and stays unregistered unless the client declares MCP Apps support at startup - on any other host those tools do not exist and nothing can call them.

## Installation

```bash
npm install -g vaultwarden-mcp
vaultwarden-mcp
```

For Claude Desktop, install from a release or from source; for Claude Code, add the server to `.mcp.json`; any other MCP client can run the stdio binary. The bundled Bitwarden CLI must survive the install - if it does not, re-run `npm install --legacy-peer-deps` and `npm run build`. On Linux, `zenity` or `kdialog` provides the approval windows.

## Configuration

```json
{
  "mcpServers": {
    "vaultwarden": {
      "command": "vaultwarden-mcp",
      "env": {
        "VW_MCP_CLIPBOARD_CLEAR_SECONDS": "30"
      }
    }
  }
}
```

Sign in once in the desktop window; on a machine with no desktop, unlock the CLI yourself and pass the session as `BW_SESSION`. A custom CA bundle can be pointed to with `VW_MCP_CA_FILE` for private certificate authorities.

## Business Relevance

- **Solo operators** get vault search and password generation inside their agent without pasting secrets into transcripts
- **Small teams on Vaultwarden** let agents prepare credential changes that a human always saves
- **Security-conscious operators** keep the master password out of the conversation entirely - it is typed into a desktop window
- **Audit-minded teams** get trash-not-delete semantics (30-day retention) on every item change

## Integration with CorpusIQ

Vaultwarden MCP covers the credential layer that CorpusIQ deliberately does not: CorpusIQ connects to business systems through its own OAuth flow and never handles third-party account passwords, while this server manages the operator's personal and team logins on a self-hosted vault. A composed workflow: an agent working a support ticket in CorpusIQ's HubSpot or Stripe connectors asks Vaultwarden which login belongs to the vendor in question, prepares a credential rotation with a generated password, and the operator saves it from the card - no secret ever lands in the agent transcript or the business-data session.

## Limitations

- Personal project, not affiliated with Bitwarden or Vaultwarden - read the vendor's SECURITY.md before pointing it at a vault that matters
- Local stdio only; the vault instance address is fixed at install time
- Secret release requires a desktop approval window per request, which rules out headless servers
- New listing (September 2026) - no long community track record
- Depends on the Bitwarden CLI being installed and healthy on the host

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
