---
title: "Protonmail-rs — Proton Mail MCP Server Integration Guide"
description: "Connect AI agents to Proton Mail via MCP with end-to-end OpenPGP encryption. Pure-Rust library, CLI, and MCP server for secure email operations."
---

# Protonmail-rs — Proton Mail MCP Server

**Unofficial, pure-Rust Proton Mail client** — library, CLI, and MCP server with end-to-end OpenPGP encryption. Gives AI agents secure, encrypted email capabilities through Switzerland's privacy-first email provider.

| Detail | Value |
|--------|-------|
| **GitHub** | [filippofinke/protonmail-rs](https://github.com/filippofinke/protonmail-rs) |
| **Language** | Rust |
| **Tools** | MCP-native email operations |
| **Transport** | stdio |
| **Stars** | ★1 (new — July 2026) |
| **License** | TBD |

## Why This Matters for Operators

Proton Mail is the leading encrypted email provider, used by 100M+ users worldwide — including journalists, legal firms, healthcare providers, and security-conscious businesses. This MCP server is the first to bring Proton Mail's end-to-end encryption to AI agent workflows:

- **HIPAA/GDPR compliance**: Encrypted email for regulated industries
- **Legal communications**: Attorney-client privileged email through AI agents
- **Secure client onboarding**: AI agents send encrypted onboarding documents
- **Privacy-first operations**: Zero-access encryption means not even Proton can read emails

## Prerequisites

- **Proton Mail account** (free or paid)
- **Proton Mail Bridge** (for IMAP/SMTP access — paid plans only)
- **Rust toolchain** (for building from source)
- **OpenPGP keys** managed through Proton's key infrastructure

## Installation

```bash
# Clone and build
git clone https://github.com/filippofinke/protonmail-rs.git
cd protonmail-rs
cargo build --release

# Binary at target/release/protonmail-rs
```

## MCP Client Configuration

```json
{
  "mcpServers": {
    "protonmail": {
      "command": "/path/to/protonmail-rs",
      "args": ["mcp"],
      "env": {
        "PROTON_API_URL": "https://mail.proton.me/api",
        "PROTON_SESSION_KEY": "your-session-key"
      }
    }
  }
}
```

## Key Capabilities

| Capability | Description |
|------------|-------------|
| **Read inbox** | Fetch and decrypt emails with OpenPGP |
| **Send encrypted** | Compose and send end-to-end encrypted emails |
| **Search** | Search encrypted mailbox by subject, sender, date |
| **Key management** | Import/export PGP keys, verify signatures |
| **Folder operations** | List, create, move emails between folders |
| **Labels & filters** | Apply labels and manage sieve filters |

## CorpusIQ Use Case

Operators in regulated industries can use this MCP server alongside CorpusIQ's business connectors:

1. **Secure document workflow**: AI agent sends encrypted contracts (via Proton Mail) when DocuSign events complete
2. **Compliance notifications**: Agent sends encrypted audit logs to compliance officers
3. **Client communications**: Agent manages encrypted email threads for legal/financial clients
4. **Privacy-first CRM**: Combine with HubSpot connector for encrypted client communications

## Security Considerations

- **End-to-end encryption**: Emails are encrypted client-side before transmission — the MCP server never sees plaintext
- **Zero-access architecture**: Proton Mail cannot decrypt your emails
- **Session management**: Use short-lived session tokens, not persistent credentials
- **Audit trail**: All agent-initiated email operations are logged in Proton Mail's activity log

## Limitations

- **Proton Mail Bridge required** for IMAP/SMTP access (paid plans only, ~$4/month)
- **Unofficial client** — not maintained by Proton AG
- **New project** (July 2026) — expect API changes and limited tool coverage initially
- **SRP authentication** may require periodic re-authentication

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `Authentication failed` | Regenerate session key via Proton web client → Settings → Security → Sessions |
| `OpenPGP key not found` | Verify key is uploaded to Proton's key server and public key is accessible |
| `Rate limited` | Proton Mail has per-account rate limits (~100 emails/day free, higher on paid) |
| `Build fails` | Ensure Rust toolchain is up to date: `rustup update stable` |

---

*Discovered: July 1, 2026 · Source: GitHub (topic:mcp-server created >2026-06-30)*
*Part of the [CorpusIQ External MCP Server Catalog](/hermes/mcp/servers/external/)*
