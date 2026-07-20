---
title: Yuanbao (元宝) — Tencent Group Chat Integration for Hermes Agents
description: Official Nous Research skill for Tencent Yuanbao group chat integration. @mention users, query group info and members, send direct messages. 550+ installs.
---

# Yuanbao (元宝) — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/NousResearch/hermes-agent) (Official)
**Skill:** `yuanbao` · **Installs:** 550+ · **Category:** Messaging / Chat Integration
**Platform:** Linux, macOS, Windows

Integrate Hermes Agent with Tencent Yuanbao (元宝) group chats. @mention users, query group information and member lists, and send direct messages — all from agent conversations. The gateway automatically converts `@nickname` references in replies into real @mentions.

---

## Installation

```bash
# Install via skills.sh
npx skills add nousresearch/hermes-agent --skill yuanbao -g -y
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ |
| **Yuanbao Gateway** | Configured in `config.yaml` under `gateway.platforms.yuanbao` |
| **Group Access** | The bot must be a member of the target Yuanbao group |

---

## How Messaging Works

**Your text reply IS the message sent to the group/user.** The gateway automatically delivers your response text to the chat. You do NOT need any special "send message" tool — just reply naturally.

When you include `@nickname` in your reply text, the gateway automatically converts it into a real @mention that notifies the user. This is built-in — you have full @mention capability.

---

## Available Tools

| Tool | When to Use |
|------|------------|
| `yb_query_group_info` | Query group name, owner, member count |
| `yb_query_group_members` | Find a user, list bots, list all members, get nickname for @mention |
| `yb_send_dm` | Send a private/direct message (DM / 私信) with optional media files |

---

## @Mention Workflow

When you need to @mention / 艾特 someone:

1. Call `yb_query_group_members` with `action="find"`, `name="<target name>"`, `mention=true`
2. Get the exact nickname from the response
3. Include `@nickname` in your reply text — the gateway handles the rest

**Example:**

```
User: "帮我艾特元宝"

Agent calls: yb_query_group_members({ group_code: "328306697", action: "find", name: "元宝", mention: true })

Agent reply (this gets sent to the group):
@元宝 你好，有人找你！
```

**Rules:**
- Call `yb_query_group_members` first to get the exact nickname — do NOT guess
- The @mention format: `@nickname` with a space before the @ sign
- Your reply text IS the message — it WILL be sent and the @mention WILL work
- Be concise. Do NOT explain how @mention works to the user.

---

## Send DM (Private Message) Workflow

When someone asks to send a private message:

1. Call `yb_send_dm` with `group_code`, `name` (target user's name), and `message`
2. The tool automatically finds the user and sends the DM

**Example — Text DM:**

```json
yb_send_dm({
  "group_code": "535168412",
  "name": "用户aea3",
  "message": "hello"
})
```

**Example — DM with Media:**

```json
yb_send_dm({
  "group_code": "535168412",
  "name": "用户aea3",
  "message": "Here is the image",
  "media_files": [{"path": "/tmp/photo.jpg"}]
})
```

**Supported media**: Images (.jpg/.png/.gif/.webp/.bmp) sent as image messages; other files sent as documents.

---

## Query Group Info

```json
yb_query_group_info({ "group_code": "328306697" })
```

Returns: group name, owner, member count.

---

## Query Members

| Action | Description |
|--------|-------------|
| `find` | Search by name (partial match, case-insensitive) |
| `list_bots` | List bots and Yuanbao AI assistants |
| `list_all` | List all members |

---

## Notes

- `group_code` comes from chat_id: `group:328306697` → `328306697`
- Groups are called "派 (Pai)" in the Yuanbao app
- Member roles: `user`, `yuanbao_ai`, `bot`
- If multiple users match a name, the tool returns candidates — ask the user to clarify

---

## Related Skills

- [Hermes Agent Core](/hermes/skills/catalog/hermes-agent-setup/) — Official core Hermes Agent skill
