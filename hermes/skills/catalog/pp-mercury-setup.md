---
title: "pp-mercury - Mercury Banking CLI Setup Guide for Hermes Agents"
description: "mvanhorn/printing-press-library - pp-mercury skill, 124 installs: drive the Mercury banking API from a Hermes agent - accounts, transactions, transfers, cards, treasury, AR invoicing, webhooks - with a read-only payment-plan approval workflow before any money moves."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pp-mercury-setup/"
robots: "index,follow"
last_updated: "2026-08-27"
tags: ["hermes skill", "agent skill", "skill setup", "banking", "fintech", "mercury", "payments", "cli"]
---

# pp-mercury - Setup Guide

**Source:** [mvanhorn/printing-press-library](https://skills.sh/mvanhorn/printing-press-library/pp-mercury)
**GitHub:** [mvanhorn/printing-press-library](https://github.com/mvanhorn/printing-press-library) (Apache-2.0, CLI Printing Press catalog - 472 CLIs across 22 categories)
**Skill:** `pp-mercury`, 124 installs
**Category:** Developer Tools / Finance & Banking
**First Seen:** Catalogued in the Aug 21, 2026 sweep; **re-evaluated Aug 27, 2026** - publisher README now documents first-class Hermes install paths (`hermes skills install`), invalidating the earlier "OpenClaw-targeted" rejection
**Quality Tier:** 🟡 Beta - explicit Hermes install support and a verified live install path, but Snyk audit is Fail-level (see Security Audit Status)

pp-mercury wraps the full Mercury banking API behind one agent-native CLI, `mercury-pp-cli`. Instead of an agent fumbling raw REST calls (pagination, idempotency keys, webhook registration), the CLI gives muscle-memory commands for every banking surface - accounts, transactions, transfers, cards, treasury, AR invoicing, journal entries, SAFE requests, statements, and webhooks. Its standout capability is `workflow payment-plan`: a **read-only approval plan** for any payment or transfer that emits the exact dry-run and execute commands before a single write happens - an agent can prepare a $25 transfer and stop for human approval with zero money moved.

The skill itself is harness-agnostic: any agent with Bash access can drive the Go binary. The publisher's README lists Hermes install commands alongside OpenClaw, Claude Code, Codex, and Cursor.

---

## Installation

### 1. Install the CLI binary (required - the skill drives this binary)

```bash
# Preferred: Printing Press npm installer (defaults to ~/.local/bin on macOS/Linux)
npx -y @mvanhorn/printing-press-library install mercury --cli-only
```

Verify before proceeding:

```bash
mercury-pp-cli --version
```

If `--version` reports "command not found", add `~/.local/bin` to `$PATH` for the agent runtime. Go-install fallback (requires Go 1.26.6+):

```bash
go install github.com/mvanhorn/printing-press-library/library/payments/mercury/cmd/mercury-pp-cli@latest
```

### 2. Install the skill for Hermes

```bash
hermes skills install mvanhorn/printing-press-library/cli-skills/pp-mercury
```

From inside the Hermes chat TUI:

```text
/skills install mvanhorn/printing-press-library/cli-skills/pp-mercury
```

For Vercel Agent Skills-compatible harnesses (verified live Aug 27, 2026 - the skills.sh installer clones the repo and discovers the skill tree):

```bash
npx skills add mvanhorn/printing-press-library/cli-skills/pp-mercury -g -y
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Mercury account** | A Mercury organization account (mercury.com) - production or sandbox |
| **Mercury API token** | `mercury-pp-cli auth set-token <TOKEN>` or export `MERCURY_BEARER_AUTH` |
| **Go 1.26.6+** | Only for the `go install` fallback path (npm installer needs only Node) |
| **`$PATH` coverage** | `~/.local/bin` must be on the agent runtime's `$PATH` |

## Core Skill

| Skill | Installs | Use For |
|---|---|---|
| pp-mercury | 124 | Mercury banking API - account management, transaction processing, balance tracking, payment handling. Triggers: "mercury account balance", "mercury transactions", "send a Mercury payment" |

## Command Reference

| Group | Example | Purpose |
|---|---|---|
| `accounts` / `account` | `mercury-pp-cli accounts` | Paginated account list / single account by ID |
| `transactions` / `transaction` | `mercury-pp-cli transactions --since 2026-08-01` | Transaction history with date-range filters, notes, categories |
| `transfer` | `mercury-pp-cli transfer ...` | Move funds between accounts in the same organization |
| `cards` | `mercury-pp-cli cards create` | Issue virtual cards, set limits, manage card details |
| `treasury` | `mercury-pp-cli treasury` | Treasury accounts and balances |
| `ar` | `mercury-pp-cli ar create-invoice` | Invoices, customers, attachments, PDFs (receivables) |
| `books` | `mercury-pp-cli books get-journal-entries` | Journal entries and Chart of Accounts templates |
| `safes` | `mercury-pp-cli safes get-requests` | SAFE (equity) requests for fundraising ops |
| `statements` | `mercury-pp-cli statements ...` | Download account statements |
| `webhooks` | `mercury-pp-cli webhooks create` | Register/manage webhook endpoints for event notifications |
| `organization` | `mercury-pp-cli organization` | EIN, legal business name, DBAs |
| `which` | `mercury-pp-cli which "pay a contractor"` | Natural-language command resolution (exit 2 = no confident match) |
| `agent-context` | `mercury-pp-cli agent-context --agent` | Machine-readable command metadata for agent/MCP hosts |
| `workflow payment-plan` | `mercury-pp-cli workflow payment-plan --kind transfer --source-account-id acct_src --destination-account-id acct_dst --amount 25 --agent` | **Read-only approval plan** with body, idempotency key, dry-run command, and execute command |
| `workflow archive` | `mercury-pp-cli workflow archive --agent` | Sync Mercury resources into a local SQLite store for offline search |

## Security Audit Status (skills.sh, verified Aug 27, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pp-mercury | Pass | Warn | Fail |

Snyk Fail is the reason for the 🟡 Beta tier rather than 🟢. The skill is a thin SKILL.md over a Go CLI; review the Snyk findings on the [skills.sh security page](https://skills.sh/mvanhorn/printing-press-library/pp-mercury/security/snyk) before wiring it to a production token.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent-safe payments** | `workflow payment-plan` produces a read-only plan with dry-run before any transfer - the autonomous-spend budget gets a hard approval gate for money movement |
| **Finance ops automation** | Balance checks, transaction categorization, and statement pulls become single CLI calls instead of manual Mercury dashboard work |
| **Client AR operations** | Invoice creation/retrieval and PDF downloads for billing workflows (`ar create-invoice`, `ar get-invoice-pdf`) |
| **Runway monitoring** | `treasury` + `accounts` + `transactions` compose into a daily runway snapshot job |
| **Event-driven alerts** | Register webhooks for transaction events feeding internal notification channels |

## Limitations / Verification

- Requires a Mercury API token with appropriate scopes - the CLI does not bypass Mercury's permission model; sandbox testing is strongly advised for write commands.
- `workflow payment-plan` plans are read-only; the execute step is a separate explicit command - keep the two steps separated in any agent workflow.
- Publisher author field in SKILL.md frontmatter reads "Cathryn Lavery" while the repo is maintained under mvanhorn - cosmetic, but noted for attribution checks.
- Install counts are modest (124) relative to the catalog's breadth; the underlying discovery skill (`printing-press-library`) has far more installs.

Verification after install:

```bash
hermes skills list | grep pp-mercury
mercury-pp-cli --version
mercury-pp-cli which "account balance"   # exit 0 = command resolved
```

## Related

- [Printing Press Library - 472-CLI Agent Tool Catalog Setup](/docs/hermes/skills/catalog/printing-press-library-setup) - the parent catalog and its discovery skill
- [Skills Marketplace](/docs/hermes/skills/marketplace) - more discovery batches
