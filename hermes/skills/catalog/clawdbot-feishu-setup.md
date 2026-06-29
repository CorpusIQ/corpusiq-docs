---
title: "ClawDBot Feishu Suite Setup Guide"
description: "Install and configure the ClawDBot Feishu Suite — 11 skills for the Lark/Feishu enterprise platform covering documents, drive, wiki, messaging, tasks, permissions, and E2E testing."
---

# ClawDBot Feishu Suite Setup Guide

**Published by:** [m1heng](https://github.com/m1heng) | **Repo:** [clawdbot-feishu](https://github.com/m1heng/clawdbot-feishu)
**Skills:** 11 | **Combined installs:** 4,793 | **Compatible with:** Hermes Agent, ClawDBot, OpenClaw

---

## Overview

The ClawDBot Feishu Suite provides complete integration with Feishu (Lark) — ByteDance's enterprise collaboration platform used by 100M+ users across China and Southeast Asia. These 11 skills cover every Feishu API surface: documents, drive, wiki, messaging, task management, permissions, E2E testing, and release workflows.

**Why Feishu matters for Hermes agents:** Feishu is the dominant enterprise platform in the Chinese market, equivalent to Slack + Google Workspace + Notion combined. For Hermes agents operating in international markets or serving Chinese enterprise clients, Feishu integration is essential infrastructure.

### Skills Overview

| Skill | Installs | API Surface | What It Does |
|-------|----------|-------------|--------------|
| feishu-doc | 1,894 | Documents | Create, read, edit Feishu Docs |
| feishu-drive | 871 | Drive | File management, upload, download |
| feishu-wiki | 451 | Wiki | Knowledge base management |
| feishu-perm | 253 | Permissions | Access control management |
| feishu-task | 173 | Tasks | Task creation, assignment, tracking |
| agent-browser | 149 | Browser | Web browsing within Feishu |
| feishu-message | 133 | Messaging | Send/receive messages |
| feishu-e2e-test | 117 | Testing | End-to-end workflow testing |
| release | 107 | Release | App release management |
| feishu-urgent | 90 | Notifications | Urgent message escalation |
| feishu-reaction | 73 | Engagement | Message reactions and emoji |

---

## Prerequisites

- **Feishu/Lark account** — Free at [feishu.cn](https://www.feishu.cn) or [larksuite.com](https://www.larksuite.com)
- **Feishu Developer Console access** — Create an app at [open.feishu.cn](https://open.feishu.cn)
- **App credentials** — App ID and App Secret from the Feishu Developer Console
- Hermes Agent or ClawDBot installed
- `npx` (Node.js) for skills.sh installation

---

## Quick Start

### Step 1: Create a Feishu App

1. Go to [Feishu Developer Console](https://open.feishu.cn/app)
2. Click "Create Custom App"
3. Name your app (e.g., "Hermes Agent")
4. Note the **App ID** and **App Secret**

### Step 2: Configure Permissions

In the Developer Console → Permissions, enable:
- `doc:doc:readonly` — Read documents
- `doc:doc` — Write documents
- `drive:drive:readonly` — Read drive files
- `drive:drive` — Manage drive files
- `im:message` — Send/receive messages
- `im:message:send_as_bot` — Send as bot
- `task:task:readonly` — Read tasks
- `task:task` — Manage tasks
- `wiki:wiki:readonly` — Read wiki
- `wiki:wiki` — Manage wiki

### Step 3: Install Skills

```bash
# Core document and communication skills
npx skills add m1heng/clawdbot-feishu --skill feishu-doc
npx skills add m1heng/clawdbot-feishu --skill feishu-drive
npx skills add m1heng/clawdbot-feishu --skill feishu-message

# Knowledge management
npx skills add m1heng/clawdbot-feishu --skill feishu-wiki

# Task management
npx skills add m1heng/clawdbot-feishu --skill feishu-task

# Permissions and admin
npx skills add m1heng/clawdbot-feishu --skill feishu-perm

# Testing and release
npx skills add m1heng/clawdbot-feishu --skill feishu-e2e-test
npx skills add m1heng/clawdbot-feishu --skill release
```

### Step 4: Set Environment Variables

```bash
export FEISHU_APP_ID=cli_xxxxxxxxxxxx
export FEISHU_APP_SECRET=your_app_secret
export FEISHU_BASE_URL=https://open.feishu.cn  # China
# export FEISHU_BASE_URL=https://open.larksuite.com  # International
```

---

## Key Skills in Detail

### feishu-doc (1,894 installs)
Create, read, and edit Feishu Documents through Hermes agents. Supports rich text formatting, tables, embeds, and collaborative editing.

**Hermes use:** Generate meeting notes, draft proposals, create documentation, sync content between Feishu and other platforms.

```bash
# Agent can now:
# - Create a new doc: "Create a Feishu doc titled 'Q3 Strategy'"
# - Read existing doc: "Read the Feishu doc at https://xxx.feishu.cn/docx/ABC123"
# - Edit collaboratively: "Add a section about AI strategy to the Q3 doc"
```

### feishu-drive (871 installs)
File management within Feishu Drive. Upload, download, organize, and share files through the agent.

**Hermes use:** Store agent-generated reports, manage file hierarchies, share resources with team members.

### feishu-message (133 installs)
Send and receive Feishu messages. Supports text, cards, images, and interactive message components.

**Hermes use:** Agent-to-team communication, alerts and notifications, automated status updates.

```bash
# Agent can:
# - Send to channel: "Post the daily report to #general"
# - Send DM: "DM @Zhang with the updated contract"
# - Receive commands: "Watch #ops channel for deploy commands"
```

### feishu-wiki (451 installs)
Knowledge base management. Create, organize, and search wiki spaces and articles.

**Hermes use:** Maintain team knowledge bases, auto-generate documentation from code, build searchable internal wikis.

### feishu-task (173 installs)
Task management — create, assign, track, and complete tasks. Integrates with Feishu's built-in task system.

**Hermes use:** Project management automation, sprint planning, issue tracking.

---

## International vs. China Deployment

Feishu operates two separate clouds:

| | **Feishu (China)** | **Lark (International)** |
|---|---|---|
| Domain | feishu.cn | larksuite.com |
| API Base | open.feishu.cn | open.larksuite.com |
| Users | China, SEA | Global |
| Compliance | China data laws | GDPR, international |

Set `FEISHU_BASE_URL` to match your deployment region.

---

## CorpusIQ Use Cases

1. **China Market Operations:** For CorpusIQ operators targeting Chinese enterprises, Feishu integration is essential. Use `feishu-doc` + `feishu-message` for client communication and deliverable sharing.

2. **Internal Documentation:** Use `feishu-wiki` to maintain a searchable knowledge base of agent workflows, integration guides, and troubleshooting runbooks.

3. **Task Automation:** Use `feishu-task` for automated task creation from customer requests — new inquiry → task in Feishu → agent processes → status update.

4. **Multi-Platform Sync:** Combine with Google Workspace skills for cross-platform content sync — write in Feishu, mirror to Google Docs.

5. **Release Management:** Use `release` + `feishu-message` for automated release announcements to team channels.

---

## Troubleshooting

### "App not authorized" errors
Run through OAuth flow in Feishu Developer Console → Security Settings → configure redirect URL. Ensure all required permissions are approved.

### Messages not sending
Verify the bot has been added to the target chat/channel. Bots cannot send to chats they haven't been invited to.

### Rate limiting (429 errors)
Feishu API has tiered rate limits:
- 100 req/s for message sending
- 50 req/s for document operations
- 20 req/s for admin operations

Implement exponential backoff for high-volume workflows.

### Token expiration
Feishu uses tenant access tokens with 2-hour expiry. The skill automatically refreshes, but if tokens expire mid-operation, re-running the command will trigger a fresh token fetch.

---

*← [June 28 Update 3 Discovery](/hermes/skills/marketplace/new-june28-2026-update3/) | [Skills Catalog Home](/hermes/skills/catalog/) →*

---

*This guide is part of the Hermes Skills Library, curated by [CorpusIQ](https://www.corpusiq.io) — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
