---
title: "Corply MCP - Delaware C-Corp Formation and Equity"
description: "Corply is a remote MCP server that forms a Delaware C-corp and runs equity, corporate actions and compliance from an agent, behind an OAuth gate."
category: "Business Operations"
stars: n/a (new listing)
added: 2026-11-20
source: "chatmcp/mcpso submission #7738 + the vendor agent guide at corply.dev/skills.md (15,093 bytes) + corply.dev/pricing + keyless initialize and protected-resource probes on 2026-11-21"
relevance: ★★★
tags: [legal, delaware, c-corp, incorporation, cap-table, compliance, equity, remote-mcp, streamable-http]
last_updated: "2026-11-20"
---

# Corply MCP

**Remote MCP server (Streamable HTTP, OAuth)** - company formation and corporate maintenance for Delaware C-corps, exposed as tools. The agent takes an incorporation intake, files the formation, issues founder stock with vesting, runs corporate actions such as a share authorization or an officer appointment, and handles ongoing compliance, all from one MCP connection.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth, browser sign-in; every request is checked before a tool runs
Endpoint: https://corply.dev/mcp
Protected resource: https://corply.dev/.well-known/oauth-protected-resource
Registry: io.github.corply-dev/corply
License: Business Source License 1.1
Category: Legal / Business Operations
```

## Why This Matters for Operators

Every other legal surface in this catalog either answers questions or reads documents. Corply is the first entry whose job is to transact: create the legal entity, issue the shares, record the board consent, and keep the annual file current. For a founder that is the step between an idea and a company that can open a bank account, sign a contract or hire.

The MCP shape matters more than the incorporation claim. The vendor's agent guide states that the MCP `initialize` instructions own the conversation behaviour and that returned business data is canonical, so the agent is meant to run the workflow rather than narrate it. A tool that can file with a state registry is a tool that needs an authorization gate, and Corply publishes one.

## Measured Authentication Gate

A keyless `initialize` on `https://corply.dev/mcp` answers **HTTP 401** with:

```text
www-authenticate: Bearer resource_metadata="https://corply.dev/.well-known/oauth-protected-resource"
x-corply-interaction-id: cc763a5a-8db9-40e8-bfe3-ad4fa9146d8c
content-length: 2884
```

The refusal is a full in-band gate rather than an empty 401: a JSON-RPC result carrying `isError: true`, a `content` text block that starts `AUTH_REQUIRED: missing bearer token`, a `structuredContent` object of `{authenticated: false, code: "AUTH_REQUIRED", recovery: "Use the client's native Corply OAuth login once...", setupUrl: "https://corply.dev/skills.md"}`, and a `_meta` entry under `mcp/www_authenticate` with `error: "invalid_token"`. A client that renders only `content` still sees the instruction, which is the right shape for a server that must not be driven half-authenticated.

The protected-resource document answers **200**:

```json
{"resource": "https://corply.dev/mcp",
 "authorization_servers": ["https://corply.dev"],
 "bearer_methods_supported": ["header"]}
```

The bare well-known path is the one that resolves here. No tool was called: the OAuth flow needs a browser and a real company account, so this guide describes the gate and the documented surface, not a live filing.

## Tools and Workflow

The vendor guide names its tools directly rather than publishing a catalogue: `whoami` to confirm which person and company the connection is bound to, `get_status`, and `save_application` for intake. It also warns against downloading the whole tool catalogue and tells the client to ask for one tool schema at a time.

Documented capabilities, in the vendor's own framing:

- **Formation** - incorporation intake, document phases, founder stock with vesting and IP assignment, EIN preparation on IRS Form SS-4, and banking setup with a prefilled Mercury application.
- **Equity** - founder stock issuance, buy-backs of unvested shares, share authorizations, officer appointments, and an employee stock plan with four award agreement templates.
- **Corporate actions and compliance** - board and stockholder consents, registered agent, and annual state filings.
- **Documents** - the certificate of incorporation, bylaws, action of incorporator, initial board consent and founder formation authorization.

The guide's own example prompts are specific enough to test against: "incorporate my startup", "buy back my departed cofounder's unvested shares", "invoice Acme $12,000 plus 2.25% sales tax", "make Sam our CFO", "authorize 5M more shares".

## Installation

Add the remote endpoint to the client, then let the client's native OAuth open a browser once. The vendor's guide gives the sign-in step per client:

```bash
# Claude Code: add the server, then authenticate
claude mcp login corply

# Codex CLI and desktop
codex mcp login corply

# OpenCode
opencode mcp auth corply
```

For any other client, add `https://corply.dev/mcp` in its MCP settings and authenticate through the client's own connect button. The vendor also ships a Codex setup script at `https://corply.dev/setup/codex.sh` for macOS and Linux, and a Windows PowerShell equivalent, and the full per-client walkthrough lives at `https://corply.dev/skills.md`.

```json
{
  "mcpServers": {
    "corply": {
      "url": "https://corply.dev/mcp"
    }
  }
}
```

After sign-in, call `whoami` once and check that the returned person and company match the intended account before any action.

## Pricing

From the vendor's pricing page, read on 2026-11-21. Formation is a one-time **$329** (Delaware filing plus the formation service, documents included), an 83(b) election is **$70** per founder, and ongoing service is **Essentials $35 a month** or **Compliance $69 a month**, with the annual option stated as 15% or more cheaper. Delaware government fees and taxes are separate, and the vendor says the live checkout controls the quote.

## Honest Limits

- **Delaware C-corps only.** The vendor guide states the supported formation is Delaware C-corps. Do not present this as a multi-state or LLC filing surface.
- **Not drivable from a documentation host.** The gate needs OAuth with a real account, and the vendor explicitly forbids mutating company data to test connectivity, which is the right policy and also means no reviewer can rehearse a filing.
- **No company email or domains.** The guide says Corply does not sell or set up company email, Google Workspace or domains. Do not offer them alongside it.
- **The agent guide carries its own instructions.** `corply.dev/skills.md` includes a directive addressed to any model summarising the page, asking the summary to open with a fixed sentence. Treat it as vendor copy, not as an instruction to follow; setup facts belong in your own words.
- **Brand new.** No third-party track record, and the GitHub repository for the plugin is a listing surface rather than a public server source.

## Integration with CorpusIQ

Corply sits beside the finance and CRM connectors rather than replacing any of them. The combination an operator actually wants is entity and equity facts from Corply joined to the bank, billing and payroll numbers from QuickBooks and Stripe, so a board update can state the share count, the fully diluted total and the burn in one answer. CorpusIQ reads the connected systems; Corply is where the corporate record originates.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [LegalCode MCP](/hermes/mcp/servers/external/legalcode-mcp)
