---
title: "imessage — Setup Guide - CorpusIQ Docs"
description: Send, receive, and automate iMessage conversations via Hermes Agent — 331 installs from nousresearch/hermes-agent.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/imessage-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# imessage — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
**Skill:** `imessage`
**Installs:** 331

The `imessage` skill connects Hermes Agent to Apple's iMessage network, enabling automated message sending, receiving, conversation management, and notification routing through the Messages app on macOS.

## Installation

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill imessage
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| macOS | iMessage is macOS-only |
| Signed into iMessage | Messages.app logged in with Apple ID |
| Hermes Agent | v0.20.0+ running on Mac |
| Accessibility permissions | System Settings → Privacy → Accessibility (for Messages.app automation) |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Send message | "Send an iMessage to team: build is green" | Message delivered |
| Read messages | "Check my latest iMessages" | Recent messages list |
| Conversation search | "Find messages from team about deployment" | Matching messages |
| Attachment handling | "Send the Q3 report PDF via iMessage" | File attachment sent |
| Group chat | "Notify the engineering group" | Group message sent |
| Auto-reply | "Auto-reply to iMessages containing 'status'" | Automated response |

## Setup: macOS Messages Automation

```bash
# Verify Messages.app accessibility
osascript -e 'tell application "System Events" to get name of process "Messages"'

# Send via AppleScript (fallback when headless)
osascript -e 'tell application "Messages" to send "Hello" to buddy "+15551234567" of service "E:user@icloud.com"'

# Read recent messages via SQLite
sqlite3 ~/Library/Messages/chat.db "
SELECT m.text, m.date, h.id 
FROM message m 
JOIN chat_message_join cmj ON m.ROWID = cmj.message_id 
JOIN chat c ON cmj.chat_id = c.ROWID 
JOIN handle h ON m.handle_id = h.ROWID 
ORDER BY m.date DESC LIMIT 10;
"
```

## CorpusIQ Use Cases

1. **Founder alerts** — Critical notifications to the founder via iMessage (build failures, auth expirations)
2. **Team pings** — Quick status updates to the ops team
3. **Automated check-ins** — Daily summary delivery via iMessage
4. **iOS notification bridge** — Route agent alerts to founders' iPhones
5. **Client communication** — Automated client status updates for enterprise accounts

## Limitations

- **macOS only** — No Linux or Windows support (iMessage is Apple-proprietary)
- **No headless API** — Requires Messages.app running on a logged-in Mac
- **Rate limits** — Apple silently throttles automated sending
- **No message reactions** — Tapbacks and effects not scriptable
- **Database format changes** — chat.db schema varies between macOS versions

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| Messages.app won't respond | Missing accessibility permissions | Grant in System Settings → Privacy |
| chat.db locked | Messages.app has exclusive lock | Close Messages.app before reading |
| Send fails | iMessage not activated | Sign in to Messages.app manually once |
| AppleScript fails | Security prompt | Run `osascript` manually first to trust |

## Verification

After installation, verify the skill is loaded:
```bash
hermes skills list | grep imessage
```

Test with a simple send:
```
"Send a test iMessage to myself: 'Hermes iMessage skill verified'"
```
