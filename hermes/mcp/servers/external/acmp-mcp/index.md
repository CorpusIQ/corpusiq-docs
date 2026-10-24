---
title: "ACMP MCP - On-Prem IT Management with Approval Gate"
description: "MIT MCP server for Aagon ACMP: 118 tools over clients, CVEs, updates, assets and helpdesk."
category: Business Operations
stars: 1
added: 2026-10-19
source: "mcpservers.org /all page 1 (herzog-gmbh/acmp-mcp)"
relevance: ★★
tags: [it-asset-management, endpoint-management, helpdesk, patch-management, cve, approvals, self-hosted, on-prem, dach]
---

# ACMP MCP

**Self-hosted MCP server for Aagon ACMP, the German client and asset management platform, built around a four-eyes approval gate** - one Windows executable on your own ACMP server that turns the ACMP Public API, the ACMP database and the kiosk into 118 MCP tools, where reads run immediately and anything that writes, executes or deletes freezes as a request until a person approves it in a browser.

```
Server type: Self-hosted (Streamable HTTP, JSON-RPC 2.0, protocol 2025-06-18)
Endpoint: http://<HOST>:8765/ on your own ACMP server (binds 127.0.0.1 by default)
Auth: One personal API key per operator (Bearer), optionally bound to that person's own ACMP identity
Approvals: read = immediate; write = 1 named approver; execute/delete = 2 different approvers
Tools: 118 across 10 areas, plus acmp_call for all 167 Public API commands
Requirements: ACMP 6.9 or 6.10 with AESB/SICS and the Public API enabled; Windows Server with .NET Framework 4.8
License: MIT (github.com/Herzog-GmbH/acmp-mcp). Not an official Aagon product; ACMP and AESB are Aagon trademarks
Pricing: The server is free; you still need an ACMP licence
```

## Why This Matters for Operators

Everyone else is putting a chatbot in front of a SaaS app. This one puts an agent in front of the machines on your network - and then refuses to let it act alone. IT questions arrive in plain language ("which computers have not checked in for 30 days", "where is 7-Zip installed", "which clients are missing last month's Windows updates") and the answer comes from the same inventory your IT team already maintains. The interesting part is the governance: a write request is not an action. It is a frozen request with the PowerShell shown in clear text, the requester, the target machine and a plain-language explanation, and it runs only after the required number of *different* people click approve outside the model.

For operators, that is the difference between "the AI can do things" and "the AI can be pointed at production". It is also the honest answer to the question every business owner asks about agents touching infrastructure: what stops it.

## Tools & Capabilities

118 tools in ten areas. Each tool carries a default approval level, adjustable per tool in `/settings`.

| Area | Tools | What the agent can do |
|---|---|---|
| System and general | 11 | server version, the operator's own rights (`acmp_whoami`), list and describe all 167 Public API commands, status of an approval request, plus read-only database discovery of tables and columns |
| Clients and inventory | 12 | list clients, find one by name or MAC, OS and last logged-on user, CPU/RAM/disks/services/serial, clients offline for X days, agent version spread, drives short on space, a registry value read through a fixed script |
| Software and security | 12 | installed software per machine, search ("where is 7-Zip"), outdated software, missing and failed Windows updates, CVEs with score and last scan time, Defender health ("where is real-time protection off"), BitLocker status per drive, licence over- and under-deployment |
| Jobs and execution | 6 | available client commands, job history and results, script history, starting a client command (1 approver), arbitrary PowerShell as SYSTEM on a client (2 approvers) |
| Client commands (optional) | 15 | decode a command into plain-text steps, catalog of step types, folder tree, create and update drafts, attach or remove install files with SHA-256, new version of an existing command, release drafts, move and folder management |
| Kiosk (optional) | 12 | kiosk tree with visibility filters, existing icons, add or update entries, move and rename, set AD-group/OU/user filters, upload icons, restore from automatic backup |
| Containers | 5 | container membership both ways, create and change, delete (2 approvers) |
| Assets and master data | 25 | assets and asset types, create and update, lend and return, contacts, companies, locations, departments, cost centres, contracts and contracts expiring soon, custom fields |
| Helpdesk | 18 | read tickets including saved queries, ticket history, work time, costs, linked tickets, assignees, templates, categories, resolutions, create and update tickets, close and reopen, add comments |
| Remote support | 2 | TeamViewer IDs for all clients, and a connection link for a machine or a username |

Every tool accepts `format: "json"`. New native commands are added declaratively in `api-tools.json` and new SQL reports in `db-tools.json` without recompiling.

## Installation

On the ACMP server, clone the repository and run the PowerShell assistant:

```powershell
.\install.ps1
```

Nine steps, each explained before it runs: prerequisite check (SICS, port 3950, .NET, free port), the Public API toggle in the ACMP console, install to `C:\ProgramData\AcmpMcp`, the SICS user, the service and a login test, your admin and approver account, optional ACMP identity binding, optional features, then the LAN binding. `.\install.ps1 -CheckOnly` verifies without changing anything; `.\install.ps1 -NonInteractive` runs unattended with the password in `$env:ACMP_SICS_PASSWORD`.

Connect a client:

```bash
claude mcp add --transport http acmp http://<HOST>:8765/ --header "Authorization: Bearer <personal-api-key>"
```

Claude Desktop has a packaged `.mcpb` extension (`mcpb-v1.0.0`, published October 18, 2026). Clients that only speak stdio bridge through `mcp-remote`. Configurations for Claude Code, Claude Desktop, Codex CLI, VS Code/GitHub Copilot, Cursor and Gemini CLI are in `docs/CLIENTS.md`.

## Configuration

| Key | Meaning |
|---|---|
| `sics.username` / `password` | the SICS/AESB base connection to ACMP |
| `sics.virtualRouter` / `wssPort` | default `VCMN` / `3950` |
| `mcp.bindAddress` / `httpPort` | default `127.0.0.1` / `8765`; LAN exposure through `set-network-admin.ps1 -BindAddress <IP>` |
| `approval.*` | approval thresholds, SMTP notification |
| `db.connectionString` | optional, read-only; enables the database report tools |
| `runPowershell.clientCommandId` | optional; enables `acmp_run_powershell` and `acmp_read_registry` |
| `ccWriter.*` / `kioskWriter.*` | optional, off by default; write client commands and kiosk entries directly to the ACMP database |
| `helpdesk.createdStateId` | optional; the ticket state new tickets get |

Add colleagues with `.\add-user.ps1` or the `/onboarding` page. Approval logins use their own token per approver and are independent of the ACMP and MCP keys, so a leaked API key does not confer approval rights.

## Business Relevance

- **IT and MSP teams:** answer fleet questions from the chat window instead of the console, and let the agent prepare remediation while a human keeps the decision.
- **Regulated and mid-size environments:** the two-person rule for destructive actions is a control you can describe to an auditor, and every request keeps requester, intent and the exact script.
- **Asset and contract work:** lend and return hardware, keep contacts, locations and cost centres current, and surface contracts expiring soon without a spreadsheet.
- **Helpdesk:** "open a ticket, printer on the second floor is not printing" becomes a real ACMP ticket with a category, an assignee and a comment trail.
- **Licence and update hygiene:** over- and under-deployment per title, missing and failed updates per machine, CVEs with score, BitLocker and Defender state per drive.

## Integration with CorpusIQ

CorpusIQ reads the business systems - accounting, CRM, analytics - and keeps the numbers consistent across AI clients. ACMP covers the estate those numbers are produced on: ask CorpusIQ what the licence line costs, ask ACMP which machines are actually running the software, in the same conversation. The approval gate is the same idea CorpusIQ applies to answers: the system proposes, and a named human remains accountable for the action.

## Limitations

- **You must already run ACMP.** It is an add-on for a licensed, on-premises system, not a hosted service anyone can connect to. ACMP 6.9 or 6.10 with AESB/SICS and the Public API enabled, on Windows Server with .NET Framework 4.8.
- **The documentation is in German.** The README, installation guide, usage cheat sheet and client configs are German because the ACMP user base is DACH; issues in English are accepted.
- **No TLS is built in.** It binds to localhost by default and refuses LAN mode without an API key, but across network boundaries you need a TLS proxy or VPN in front, plus firewall rules by source subnet.
- **Wide blast radius.** The vendor says plainly that the server grants full ACMP access including command execution on every endpoint; treat each API key like an admin password. `acmp_run_powershell` runs as SYSTEM.
- **The optional writers bypass ACMP's own rights check.** Client-command and kiosk writing goes to the database with a dedicated SQL login rather than through the Public API, so ACMP does not verify the operator's ACMP permissions for those tools. They are off by default, restricted to an allowed-requester list, and still require an approver.
- **Very new.** Repository created October 11, 2026, one release, one star, no third-party track record. Pin the release, test on a lab ACMP instance, and start with the read-only tools.

## FAQ

### Does the agent act on its own?

No for anything that changes state. Reads run immediately. A write becomes a request on the approval page and waits for one approver; execute and delete wait for two different people. The approval happens outside the model, in a browser, with the script shown in full.

### Can every operator do everything?

No. Each operator has their own API key, and can optionally be bound to their own ACMP identity, in which case ACMP checks that person's real rights. What an operator may *request* in the optional writer tools is a separate allow-list (`ccWriter.allowedRequesters`).

### What happens after an ACMP update?

Before writing anything through the optional writers, the server checks the ACMP version, tables, triggers and the write login's rights, and test-unpacks and re-packs the 50 newest commands. If anything differs, it writes nothing. The vendor tested against ACMP 6.10.

### Is it free?

The server is MIT-licensed and free. ACMP itself is a commercial product you license from Aagon, and the server is not an official Aagon product.

## See Also

- [Security Recipes MCP - CVE Intelligence and Remediation](/hermes/mcp/servers/external/security-recipes-mcp)
- [A4B CMMS MCP - Asset & Maintenance Management](/hermes/mcp/servers/external/a4b-cmms-mcp)
- [Tenable MSSP MCP - Managed Security Tenants](/hermes/mcp/servers/external/tenable-mssp-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
