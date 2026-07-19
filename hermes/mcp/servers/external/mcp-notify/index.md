---
title: "MCP Notify — Monitor the MCP Registry for New Servers"
description: "Integration guide for nirholas/mcp-notify. Real-time monitoring of the MCP ecosystem: new/updated/removed servers, notifications via Discord, Slack, Email, Telegram."
category: mcp
tags: [mcp-server, monitoring, notifications, devops, registry, hermes-agent]
last_updated: 2026-07-15
mcp_server: nirholas/mcp-notify
stars: 28
source: mcpservers.org
---

# MCP Notify — Monitor the MCP Registry for New Servers

**Repository:** [nirholas/mcp-notify](https://github.com/nirholas/mcp-notify)
**Stars:** 28 ★
**Category:** DevOps / Monitoring
**License:** MIT
**Last Updated:** 2026-07-14

## What It Does

MCP Notify polls the MCP Registry for changes and sends real-time notifications when servers are added, updated, or removed. Includes a CLI, Go SDK, REST API, and MCP server for AI agents. Supports Discord, Slack, Email, Telegram, Microsoft Teams, Webhooks, and RSS feeds as notification channels.

### Tools Provided

| Tool | Description |
|------|-------------|
| `check_registry` | Poll the MCP registry for changes since last check |
| `get_new_servers` | List newly registered MCP servers |
| `get_updated_servers` | List servers with metadata/code changes |
| `get_removed_servers` | List servers removed from registry |
| `search_servers` | Search registry by keyword, category, stars |
| `subscribe_category` | Subscribe to notifications for a specific server category |
| `configure_notifications` | Set up notification channels (Discord, Slack, Telegram, etc.) |
| `get_registry_stats` | Registry statistics: total servers, growth rate, category breakdown |

## Why This Matters

The MCP ecosystem grows at ~10-15 servers/day. Manually checking mcp.so and mcpservers.org for new servers is unsustainable. MCP Notify automates discovery — it watches the registry and alerts you when relevant servers appear.

For CorpusIQ specifically: new MCP servers in the "business," "marketing," "analytics," and "CRM" categories are competitive signals. Early detection of category entrants allows faster competitive response.

## Setup for Hermes Agent

### Prerequisites

- Go 1.21+ (for CLI/SDK) OR Docker
- Notification channel webhook URL (Discord, Slack, Telegram, etc.)

### Step 1: Clone and Build

```bash
cd ~/mcp-servers
git clone https://github.com/nirholas/mcp-notify.git
cd mcp-notify

# Option A: Go build
go build -o mcp-notify ./cmd/mcp-notify

# Option B: Docker
docker build -t mcp-notify .
```

### Step 2: Configure

Create `~/.mcp-notify/config.yaml`:

```yaml
registry:
  poll_interval_minutes: 60
  sources:
    - https://mcpservers.org
    - https://mcp.so
    - https://smithery.ai

notifications:
  telegram:
    enabled: true
    bot_token: ${TELEGRAM_BOT_TOKEN}
    chat_id: "-1003961538688"  # CorpusIQ Team
    topic_id: 2  # Dev discussion topic
  
  discord:
    enabled: false
    webhook_url: ${DISCORD_WEBHOOK}
  
  email:
    enabled: false
    smtp_host: smtp.gmail.com
    smtp_port: 587
    to: notifications@example.com

filters:
  categories:
    - business
    - marketing
    - analytics
    - crm
    - finance
    - communication
  min_stars: 5
  exclude_keywords:
    - crypto
    - nft
    - blockchain
    - gaming
    - nsfw
```

### Step 3: Initial Scan

```bash
./mcp-notify scan --baseline
# Output: Baselined registry with 9,847 servers. Will alert on changes.
```

### Step 4: Register with Hermes

```bash
hermes mcp add mcp-notify -- ~/mcp-servers/mcp-notify/mcp-notify serve
```

Or via `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  mcp_notify:
    command: /home/hermes/mcp-servers/mcp-notify/mcp-notify
    args:
      - serve
    env:
      MCP_NOTIFY_CONFIG: /home/hermes/.mcp-notify/config.yaml
```

### Step 5: Verify

```bash
hermes mcp list | grep mcp-notify
```

## Integration with CorpusIQ Cron Jobs

Replace the current manual scan cron with MCP Notify:

```bash
# OLD (manual scan)
0 */6 * * * /home/hermes/scripts/scan-mcp-servers.sh

# NEW (auto-notify)
# MCP Notify runs as a daemon with built-in polling
# Just start it once:
hermes mcp start mcp-notify
```

The agent can then query `mcp-notify` during session startup:

```
Agent: "Any new business-category MCP servers since last session?"
MCP Notify: "2 new: QuickBooks MCP (45★), Salesforce MCP (12★)"
```

## Use Cases

1. **Competitive intelligence:** Alert when new servers enter your category
2. **Ecosystem awareness:** Track MCP growth trends and emerging categories
3. **Curated collections:** Automatically build "best of" lists from registry data
4. **Dependency monitoring:** Watch for updates to MCP servers your stack depends on
5. **Market research:** Analyze which categories are growing fastest

## Limitations

- Polling-based (not real-time push) — up to 60-min delay on new server discovery
- Registry sources may have incomplete coverage (not all servers are listed everywhere)
- Category classification relies on source metadata (may be inaccurate)
- Early stage project (28★) — API may change
- No historical trending data (only deltas from baseline)

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `No changes detected` | Registry sources may be down; check `mcp-notify status` |
| `Webhook delivery failed` | Verify webhook URL; check firewall egress rules |
| `Telegram bot not sending` | Verify bot token has `sendMessage` permission in chat |
| `Rate limited by registry` | Increase `poll_interval_minutes` to 120+ |

## Related Guides

- [Scan Results July 15](/hermes/mcp/servers/external/scan-results-2026-07-15/) — Latest manual scan
- [MCP Directory Maintenance](/hermes/mcp/servers/external/) — Keeping our listings current
- [Hermes Ecosystem Discovery](/hermes/mcp/servers/external/) — Nightly ecosystem engine
