---
title: vps-server-management Setup Guide
description: Complete setup guide for vps-server-management — manage VPS servers and the AI agents running on them, including Hermes Agent Discord gateway deployments.
---

# vps-server-management Setup Guide

**Skill:** `vps-server-management` · **Installs:** 26 · **Source:** [davidondrej/skills](https://github.com/davidondrej/skills) (2,510 ★)

Manage VPS servers and the AI agents running inside them — connect, deploy, monitor, restart, and operate remote hosts and their agents. Part of davidondrej's 40-skill agent operations toolkit.

---

## Prerequisites

- **SSH access** to target VPS servers (root or sudo user)
- **Hostinger VPS** or any Ubuntu 24.04 server (the skill's reference configuration uses Hostinger + Dokploy/n8n)
- **Agent installed on VPS** — Hermes Agent, OpenClaw, Codex, or Claude Code
- **Infrastructure document** at `~/Documents/code/workspace/library/infrastructure.md` (source of truth for IPs, expirations, access levels)

---

## Installation

```bash
npx skills add davidondrej/skills --skill vps-server-management
```

---

## Capabilities

- **Server inventory management** — Track hostnames, IPs, OS, purpose, and expiration dates
- **SSH agent deployment** — Launch agents directly on VPS for full filesystem/process context
- **Remote monitoring** — Check agent status and health on remote hosts
- **Access level enforcement** — Three tiers: App login, VPS SSH, Hostinger hPanel
- **Multi-server operations** — Manage multiple VPS instances with different purposes (Dokploy, n8n, Discord gateways)

---

## Reference Architecture

The skill's default server layout (adapt to your infrastructure):

| Hostname | Purpose | Agent |
|---|---|---|
| `<server-1>` | Dokploy — personal OpenClaw instance | OpenClaw |
| `<server-2>` | n8n workflow automations (primary) | n8n agents |
| `<server-3>` | **Hermes Agent — Discord gateway** | **Hermes Agent** |

---

## Usage

### Check agent status on a server

```
SSH into <server-3> and check if the Hermes Agent Discord gateway is running
```

The skill instructs the agent to SSH into the box, launch the agent ON the VPS (e.g., `codex --yolo`), and report status.

### Deploy an agent to a new server

```
Set up Hermes Agent on a new VPS at <IP>
```

The skill guides through: SSH access verification → agent installation → gateway configuration → health check.

### Restart a remote agent

```
Restart the OpenClaw agent on <server-1>
```

For short command sequences (updates, config changes, restarts), the skill recommends driving an existing SSH session directly.

---

## CorpusIQ Use Cases

**Hermes Agent Discord gateway management:** Manage the CorpusIQ Discord gateway Hermes Agent deployment — monitor uptime, restart after updates, verify connectivity.

**Multi-agent infrastructure:** Track all CorpusIQ agent deployments across VPS instances with a single inventory document.

**CI/CD for agent updates:** Push Hermes Agent updates to remote VPS instances with rollback capability.

---

## Security Model

| Access Level | Scope | Share With |
|---|---|---|
| **App login** | Build/edit workflows, no server access | Team members |
| **VPS SSH** | Docker, files, system config | Trusted technical staff |
| **Hostinger hPanel** | Billing, reboot, OS reinstall, SSH creds | Admin only |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| SSH connection refused | Verify IP is correct and SSH daemon is running on the VPS |
| Agent not found on VPS | Install the agent first: follow Hermes/OpenClaw setup docs for Ubuntu 24.04 |
| Permission denied | Check access level — app login doesn't grant SSH access |
| cmux agent prefills wrong message | Claude Code cmux note: after Claude finishes, it may prefill a predicted next user message — that draft is Claude, not the user speaking |

---

## Related Skills

- [distribute-skill-to-all-agents](/hermes/skills/catalog/distribute-skill-to-all-agents-setup/) — Sync skills across agent instances (same publisher)
- [browser-harness](/hermes/skills/catalog/browser-harness-setup/) — Browser automation for agents (same publisher)
- [anti-sleep](https://skills.sh/davidondrej/skills) — Keep remote agents alive on VPS
- [setup-help](https://skills.sh/davidondrej/skills) — Agent environment setup assistance

---

*← [Skills Marketplace](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
