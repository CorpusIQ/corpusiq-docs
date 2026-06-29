---
title: Hermes WhatsApp Secretary — Setup Guide
description: Install and configure the WhatsApp secretary skill for Hermes Agent — read, summarize, draft-and-confirm replies, and schedule messages via WhatsApp.
---

# Hermes WhatsApp Secretary — Setup Guide

**Source:** [ricktechmecha/hermes-whatsapp-secretary](https://github.com/ricktechmecha/hermes-whatsapp-secretary)
**Category:** Communication Bots / Productivity
**License:** MIT · **Published:** June 27, 2026

A personal WhatsApp secretary skill for Hermes Agent. It reads incoming WhatsApp messages, summarizes threads, drafts replies for your approval, and can schedule messages — all through the Hermes agent interface. Never miss an important WhatsApp message while working, and never type a reply you didn't approve.

---

## Key Capabilities

| Capability | How It Works |
|-----------|---------------|
| **Read messages** | Retrieves unread WhatsApp messages across chats |
| **Summarize threads** | Condenses long chat threads into key points |
| **Draft replies** | Generates suggested responses for your approval |
| **Confirm-before-send** | No message is sent without explicit user confirmation |
| **Schedule messages** | Queue messages for future delivery |
| **Priority filtering** | Flags urgent messages based on sender/content |

---

## Installation

```bash
npx skills add ricktechmecha/hermes-whatsapp-secretary
```

### Prerequisites

| Requirement | Details |
|-------------|---------|
| **WhatsApp account** | Active WhatsApp with WhatsApp Web capability |
| **whatsapp-web.js** or **Baileys** | WhatsApp Web API library (installed automatically) |
| **Hermes Agent** | v0.16.0+ |
| **QR scan** | One-time WhatsApp Web QR authentication |

### Configuration

```bash
# In ~/.hermes/config.yaml
skills:
  whatsapp-secretary:
    auto_summarize: true
    draft_replies: true
    require_confirmation: true
    priority_senders:
      - "+1234567890"  # Boss
      - "+1987654321"  # Partner
    quiet_hours:
      start: "22:00"
      end: "07:00"
```

---

## Usage with Hermes Agent

### Daily Workflow

```
"Check my WhatsApp messages"
"Summarize the family group chat"
"Draft a reply to Sarah about the meeting time"
"Schedule a WhatsApp message to the team for tomorrow 9am"
```

### Reply Flow

1. Hermes reads the message
2. Drafts a suggested reply
3. Shows you the draft → **you approve or edit**
4. Only then does it send

```
Hermes: "Sarah asks: 'Can we move the meeting to 3pm?'"

Draft reply: 'Sure Sarah, 3pm works for me. See you then!'

[Approve] [Edit] [Skip]
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Customer WhatsApp inquiries | Auto-draft responses for common questions |
| Team coordination | Summarize group chats, flag action items |
| Personal productivity | Batch-process WhatsApp during focused work time |
| Lead response | Draft first replies to inbound business inquiries |

---

## Security Notes

- WhatsApp Web session must be re-authenticated periodically
- Store WhatsApp auth state securely — it grants full message access
- `require_confirmation: true` is strongly recommended for production use
- Messages are processed locally — no third-party server involved

---

*This guide is part of the [Hermes Skills Catalog](/hermes/skills/catalog/). Discovered June 29, 2026. Powered by CorpusIQ.*
