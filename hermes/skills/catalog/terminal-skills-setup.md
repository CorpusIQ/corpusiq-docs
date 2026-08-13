---
title: Terminal Skills — System Administration Skill Pack for Hermes Agents
description: Collection of terminal-focused skills (cron, systemd, network-tools, VPN) with 2.4K+ combined installs. Gives Hermes agents structured knowledge for Linux system administration, cron job management, and network operations.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/terminal-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Terminal Skills — Setup Guide

**Source:** [chaterm/terminal-skills](https://skills.sh/chaterm/terminal-skills) (2.4K+ combined installs)
**Category:** Engineering / System Administration
**Quality Tier:** 🟡 Beta

A collection of terminal and system administration skills from chaterm that give Hermes agents structured, reusable knowledge for managing Linux systems — cron job scheduling, systemd service management, network diagnostics, and VPN configuration. While Hermes agents already have terminal access, these skills provide best-practice templates and troubleshooting patterns.

---

## Installation

```bash
npx skills add chaterm/terminal-skills --skill cron
npx skills add chaterm/terminal-skills --skill system-admin
npx skills add chaterm/terminal-skills --skill systemd
npx skills add chaterm/terminal-skills --skill network-tools
npx skills add chaterm/terminal-skills --skill vpn
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **cron** | 1.3K | Cron job scheduling, log monitoring, and troubleshooting |
| **system-admin** | 478 | General Linux system administration tasks |
| **systemd** | 222 | systemd service management and unit file authoring |
| **network-tools** | 181 | Network diagnostics, port scanning, firewall rules |
| **vpn** | 170 | VPN client configuration and troubleshooting |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Linux** | Skills are Linux-specific (Debian/Ubuntu focus) |
| **Root/sudo** | Some operations require elevated privileges |
| **Language** | Primary documentation is in Chinese (zh-CN); commands are universal |

---

## Key Capabilities

### Cron — Scheduled Task Management
```bash
# View current crontab
crontab -l

# Edit crontab
crontab -e

# Common schedules
0 * * * * command       # Hourly at minute 0
*/15 * * * * command    # Every 15 minutes
0 9-17 * * * command    # Business hours, hourly
0 0 * * 1-5 command     # Weekdays at midnight
```
Ideal for creating and debugging Hermes cron jobs, understanding schedule syntax, and monitoring cron logs for failures.

### Systemd — Service Management
```bash
# Service lifecycle
systemctl status <service>
systemctl start/stop/restart <service>
systemctl enable/disable <service>

# Log inspection
journalctl -u <service> --no-pager -n 50
```
Directly applicable to managing the Hermes gateway service, debugging death loops, and authoring systemd unit files.

### Network Tools — Diagnostics
```bash
# Connectivity checks
ping -c 4 <host>
traceroute <host>

# Port scanning
ss -tlnp                    # Listening ports
nmap -sT <host>             # TCP port scan

# DNS
dig <domain>
nslookup <domain>
```
Useful for debugging Telegram API connectivity, MCP server reachability, and API endpoint health.

### System Admin — General Operations
Disk usage, process management, user management, package installation, and log rotation patterns for day-to-day Hermes system maintenance.

---

## Quick Start for Hermes Agents

```bash
# 1. Verify installation
npx skills list | grep terminal-skills

# 2. Inspect current cron jobs (using cron skill knowledge)
crontab -l 2>/dev/null || echo "No user crontab"

# 3. Check Hermes gateway service status (using systemd skill knowledge)
systemctl --user status hermes-gateway-corpusiq.service --no-pager

# 4. Network health check (using network-tools skill knowledge)
ss -tlnp | grep -E '11434|8080|3000'
```

---

## Verification

```bash
# Check skills are installed
npx skills list 2>&1 | grep -E 'cron|system-admin|systemd|network-tools|vpn'

# Verify cron knowledge is accessible
npx skills use chaterm/terminal-skills@cron 2>&1 | head -20

# Verify systemd knowledge
npx skills use chaterm/terminal-skills@systemd 2>&1 | head -20
```

---

## Notes

- **Language**: Primary documentation is in Chinese (zh-CN). Commands, paths, and syntax are universal. Use with translation tools if needed.
- **Hermes integration**: These skills complement but don't replace Hermes' built-in terminal access. They provide structured knowledge for recurring administration patterns.
- **Overlap with existing skills**: The `linux-systemd` and `cron-design-workflow` skills in the CorpusIQ catalog cover similar ground with English documentation. These terminal-skills provide additional patterns and Chinese-language alternatives.
- **VPN skill**: Useful when Hermes needs to connect through VPNs for geo-restricted API access or testing.
