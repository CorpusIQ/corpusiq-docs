---
title: ClawPilot Ecosystem — Full Setup Guide for Hermes Agents
description: Install, configure, and use the ClawPilot ecosystem (clawpilot, clawpilot-pair, clawpilot-send, clawpilot-config, clawpilot-doctor) to connect PocketClaw mobile app to Hermes Agent hosts.
---

# ClawPilot Ecosystem — Setup Guide

**Source:** [kcchien/clawpilot](https://skills.sh/kcchien/clawpilot) (241 installs) + [rethinking-studio/clawpilot-skills](https://skills.sh/rethinking-studio/clawpilot-skills) (29/22/21/20 installs)
**Category:** Mobile Agent Interface, Infrastructure

ClawPilot bridges PocketClaw (iOS/macOS mobile app) to AI agent runtimes — including **Hermes Agent**. Once paired, operators can chat with their Hermes agents, send files, receive reports, run diagnostics, and manage configuration — all from their phone.

---

## Installation

### Install All ClawPilot Skills

```bash
# Main ClawPilot skill (OpenClaw expert + security tools)
npx skills add kcchien/clawpilot

# PocketClaw pairing + runtime support
npx skills add rethinking-studio/clawpilot-skills --skill clawpilot-pair
npx skills add rethinking-studio/clawpilot-skills --skill clawpilot-send
npx skills add rethinking-studio/clawpilot-skills --skill clawpilot-config
npx skills add rethinking-studio/clawpilot-skills --skill clawpilot-doctor
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **PocketClaw iOS app** | Install from App Store on iPhone/iPad |
| **Hermes Agent** | v0.16.0+ with API server enabled |
| **API server key** | Set in `~/.hermes/.env`: `API_SERVER_ENABLED=true`, `API_SERVER_KEY=<your-key>` |
| **Network** | Host and phone on same local network, or use Tailscale for remote access |

Enable the Hermes API server:

```bash
# In ~/.hermes/.env
API_SERVER_ENABLED=true
API_SERVER_KEY=$(openssl rand -hex 32)
API_SERVER_PORT=8888
```

---

## Key Capabilities

### Skill-Specific Capabilities

| Skill | Capability | How to Trigger |
|---|---|---|
| **clawpilot-pair** | Generate pairing code for PocketClaw | "Pair my phone with Hermes" or "Set up PocketClaw" |
| **clawpilot-send** | Send files from host to mobile | "Send this report to my phone" |
| **clawpilot-config** | Validate host config for pairing | "Check if my Hermes is ready for PocketClaw" |
| **clawpilot-doctor** | Diagnose pairing/connection issues | "Why can't my phone connect to Hermes?" |
| **clawpilot** | Security audit, config inspect, session scan | "Audit my agent gateway security" |

### Pairing Workflow

1. Enable Hermes API server (see Prerequisites)
2. Load `clawpilot-pair` skill
3. Agent verifies host readiness
4. Agent generates a pairing code
5. Enter code in PocketClaw iOS app
6. Connection established — chat from mobile

### Sending Files to Mobile

When a PocketClaw conversation is active, the agent can:
1. Generate or locate the file
2. Use `clawpilot send` to route it to mobile
3. File appears in PocketClaw app

Supports: reports, screenshots, generated images, log files, data exports.

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Mobile agent check-in** | Load `clawpilot-pair`, pair phone, chat with CorpusIQ agent from anywhere |
| **Receive daily reports on mobile** | Agent generates report, uses `clawpilot-send` to deliver to PocketClaw |
| **Remote diagnostics** | Load `clawpilot-doctor` when agent goes unresponsive — diagnose from phone |
| **Config validation before pairing** | Load `clawpilot-config` to verify Hermes API server before attempting pairing |
| **Security audit on demand** | Load `clawpilot` to run security audit against OpenClaw gateway from mobile |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| "API server not found" | Verify `API_SERVER_ENABLED=true` in `~/.hermes/.env` and restart Hermes |
| "Connection refused" | Check firewall allows port 8888; verify host and phone on same network or Tailscale active |
| "Invalid pairing code" | Regenerate code with `clawpilot-pair`; codes are single-use and expire |
| "Runtime not detected" | Run `clawpilot-config` to validate; ensure Hermes is running with `hermes status` |
| File send fails | Verify file path exists; check PocketClaw app is open and paired |

## Verification

```bash
# Verify all ClawPilot skills installed
hermes skills list | grep -E "clawpilot|clawpilot-pair|clawpilot-send|clawpilot-config|clawpilot-doctor"

# Check Hermes API server is running
curl -s http://localhost:8888/health -H "Authorization: Bearer $(grep API_SERVER_KEY ~/.hermes/.env | cut -d= -f2)"

# Test pairing readiness (loads clawpilot-config)
hermes --skills clawpilot-config "Check if this host is ready for PocketClaw pairing"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-june16-2026/) →*

*Powered by CorpusIQ*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
