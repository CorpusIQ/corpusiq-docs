---
title: Telegram CLI — Native Telegram Client for Hermes Agents
description: Full-featured Telegram CLI for reading, searching, sending messages, managing groups, and syncing chat history. 425 installs. Fast native MTProto client — no bot API limitations.
---

# Telegram CLI — Setup Guide

**Source:** [skillhq/telegram](https://skills.sh/skillhq/telegram) (425 installs)
**Category:** Communication / Messaging
**Quality Tier:** 🔵 Community

A native Telegram CLI using the MTProto protocol — not the Bot API. This means full access to your Telegram account: read messages, search across all chats, send DMs and group messages, manage group members, mute chats, export history, and organize folders. Much more powerful than bot-only access for Hermes agents that need full Telegram account capabilities.

---

## Installation

```bash
npm install -g @skillhq/telegram
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Telegram Account** | A registered Telegram account (phone number) |
| **API Credentials** | Get `api_id` and `api_hash` from [my.telegram.org/apps](https://my.telegram.org/apps) |

---

## Key Capabilities

### Authentication

```bash
telegram auth                    # First-time login (prompts for api_id, api_hash, phone, code)
telegram check                   # Verify session is valid
telegram whoami                  # Show logged-in account
telegram whoami --json           # Account info as JSON
telegram logout                  # Clear saved session
```

### Reading Messages

```bash
telegram inbox                   # Unread messages summary
telegram chats                   # List all chats
telegram chats --type group      # Filter: user, group, supergroup, channel
telegram read "ChatName" -n 50   # Read last 50 messages
telegram read "ChatName" --since "1h"  # Messages from last hour
telegram read @username -n 20    # Read DM with user
```

### Searching

```bash
telegram search "query" --chat "ChatName"   # Search within a specific chat
telegram search "query" --all               # Search all chats globally
telegram search "query" -n 20               # Limit results
```

### Sending Messages

```bash
telegram send @username "Hello"             # Send DM
telegram send "GroupName" "Message"         # Send to group
telegram reply "ChatName" 12345 "Response"  # Reply to specific message ID
```

### Group Management

```bash
telegram members "GroupName"                # List members
telegram members "GroupName" -n 500         # Fetch up to 500 members
telegram admins "GroupName"                 # List admins only
telegram mute "GroupName"                   # Mute noisy group
telegram unmute "GroupName"                 # Unmute
telegram kick "GroupName" @user             # Remove user
telegram promote "GroupName" @user          # Promote to admin
```

### Contacts & History

```bash
telegram contact @username                  # Get contact info
telegram export "ChatName" --format json    # Export chat history
telegram folders                            # List chat folders
```

---

## Quick Start — Hermes Agent

```bash
# Install
npm install -g @skillhq/telegram

# First-time setup (requires api_id + api_hash from my.telegram.org)
telegram auth

# Verify
telegram whoami

# Check unread
telegram inbox

# Monitor CorpusIQ Team topic
telegram read "CorpusIQ Team" -n 10
```

---

## Verification

```bash
telegram check && echo "Telegram CLI: OK"
telegram whoami --json | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'Logged in as: {d.get(\"first_name\",\"?\")}')"
```

---

## Notes

- **MTProto, not Bot API**: Full account access — read all chats, send as yourself, manage groups. Much more powerful than bot-only Telegram access
- **First-time auth**: Requires API credentials from my.telegram.org (one-time setup per account)
- **Session persistence**: Session saved locally after `telegram auth` — no re-authentication needed
- **Use case for CorpusIQ**: Monitor CorpusIQ Team forum, read Topic 2 messages programmatically, send alerts, export chat history for analysis
- **Pitfall**: Not for bot accounts — use Telegram Bot API for @corpusiq_bot. This is for human account access
- **Related skills**: telegram-bot-builder (if using bot API), corpusiq-inbound-communication-monitoring
