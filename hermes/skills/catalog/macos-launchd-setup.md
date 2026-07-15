---
title: macOS Launchd Agent Deployment — Setup Guide
description: Deploy OpenClaw/Hermes agents as macOS launchd services with KeepAlive, log routing, and environment variable management.
---

# macOS Launchd Agent Deployment — Setup Guide

## Prerequisites
- **macOS 12+** (Monterey or later)
- **OpenClaw / Clawdbot / Hermes** agent installed
- **Terminal** access

## Capabilities

| Capability | Description |
|-----------|-------------|
| **Plist Generation** | Create LaunchAgent `.plist` files for agent processes |
| **KeepAlive** | Auto-restart agents that exit or crash |
| **RunAtLoad** | Start agent immediately when plist is loaded |
| **Log Routing** | StandardOutPath / StandardErrorPath for file-based logging |
| **Environment Variables** | Inject API keys and config paths via EnvironmentVariables dict |
| **launchctl Management** | bootstrap, bootout, list, print — full lifecycle control |

## Installation

```bash
npx skills add alphaonedev/openclaw-graph/macos-launchd
```

## Quick Start

Create `~/Library/LaunchAgents/com.corpusiq.hermes-gateway.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.corpusiq.hermes-gateway</string>

    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/hermes</string>
        <string>gateway</string>
        <string>run</string>
        <string>--profile</string>
        <string>corpusiq</string>
    </array>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <dict>
        <key>SuccessfulExit</key>
        <false/>
    </dict>

    <key>EnvironmentVariables</key>
    <dict>
        <key>HERMES_HOME</key>
        <string>/Users/media/.hermes/profiles/corpusiq</string>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
    </dict>

    <key>StandardOutPath</key>
    <string>/Users/media/.hermes/logs/gateway-stdout.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/media/.hermes/logs/gateway-stderr.log</string>

    <key>WorkingDirectory</key>
    <string>/Users/media</string>
</dict>
</plist>
```

Load and start:

```bash
# Load the plist (registers with launchd)
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.corpusiq.hermes-gateway.plist

# Verify it's running
launchctl list | grep com.corpusiq.hermes-gateway

# Check logs
tail -f ~/.hermes/logs/gateway-stdout.log
```

Stop and unload:

```bash
launchctl bootout gui/$(id -u)/com.corpusiq.hermes-gateway
```

## Key Configuration Patterns

### KeepAlive Options

| Option | Behavior |
|--------|----------|
| `<true/>` | Always restart (equivalent to systemd `Restart=always`) |
| `SuccessfulExit: false` | Only restart on crash/non-zero exit (equivalent to `Restart=on-failure`) |
| `Crashed: true` | Only restart on signal/crash |
| `NetworkState: true` | Restart when network changes |

### Environment Variable Injection

```xml
<key>EnvironmentVariables</key>
<dict>
    <key>OPENAI_API_KEY</key>
    <string>sk-...</string>
    <key>ANTHROPIC_API_KEY</key>
    <string>sk-ant-...</string>
</dict>
```

### Log File Management

```bash
# Rotate logs (launchd doesn't auto-rotate)
mv ~/.hermes/logs/gateway-stdout.log ~/.hermes/logs/gateway-stdout.log.1
# Reload the agent to pick up new log file
launchctl kickstart gui/$(id -u)/com.corpusiq.hermes-gateway
```

## CorpusIQ Use Cases

1. **Mac Mini Worker:** The Mac Mini runs Hermes processes for video generation, email monitoring, and docs management. Launchd provides proper process supervision — agents restart on crash, logs are captured to files, and environment variables are managed centrally.

2. **Multi-Profile Management:** Each Hermes profile gets its own LaunchAgent plist with isolated environment variables and log files.

3. **Cron Replacement:** Long-running monitor workers (social media, email, GitHub) can run as LaunchAgents instead of cron — better logging, crash recovery, and process visibility.

## macOS vs Linux Comparison

| Feature | macOS (launchd) | Linux (systemd) |
|---------|-----------------|-----------------|
| Config format | XML `.plist` | INI `.service` |
| Load command | `launchctl bootstrap` | `systemctl enable` |
| Start command | `launchctl kickstart` | `systemctl start` |
| Logs | File-based (StdoutPath) | journald |
| Resource limits | Not natively supported | MemoryMax, CPUQuota |
| User scope | `gui/<uid>` domain | `systemctl --user` |

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `launchctl bootstrap` fails with "Already loaded" | Plist already registered | `launchctl bootout` first, then bootstrap |
| Agent not auto-restarting | KeepAlive not configured | Set `KeepAlive: SuccessfulExit: false` |
| "Service cannot load in requested session" | Wrong domain | Use `gui/<uid>` for GUI agents, `user/<uid>` for background |
| Agent runs but no logs | Log directory doesn't exist | `mkdir -p ~/.hermes/logs/` |
| Environment variables not taking effect | Plist cached | `launchctl bootout` + `bootstrap` to reload |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Home](/hermes/skills/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
