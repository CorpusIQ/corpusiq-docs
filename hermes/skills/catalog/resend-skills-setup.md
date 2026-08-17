---
title: "Resend Agent Skills — Email API, Inboxes, and"
description: Install 5 production-grade Resend email skills (28.8K+ combined installs) for Hermes agents — transactional email API, agent inboxes, React Email templates, CLI operations, and email deliverability best practices.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/resend-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Resend Agent Skills — Setup Guide

**Source:** [resend/resend-skills](https://skills.sh/resend/resend-skills) (28,800+ combined installs)
**Category:** Communication Bots / Platform Integration
**Quality Tier:** 🟢 Production

Resend's official agent skills provide everything Hermes agents need to send, receive, and manage email programmatically. From transactional API calls to agent inboxes that process inbound email, these 5 skills encode Resend's production patterns — idempotency keys, webhook verification, template variable syntax, and deliverability best practices that prevent common production issues.

---

## Installation

```bash
# Install all Resend skills
npx skills add resend/resend-skills

# Or install specific skills
npx skills add resend/resend-skills --skill resend
npx skills add resend/resend-skills --skill agent-email-inbox
npx skills add resend/resend-skills --skill react-email
npx skills add resend/resend-skills --skill email-best-practices
npx skills add resend/resend-skills --skill resend-cli
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **resend** | ~10K | Core Resend API — send transactional emails (single/batch), receive inbound webhooks, manage templates, domains, contacts, broadcasts, automations |
| **agent-email-inbox** | ~7K | Build AI agent inboxes — inbound email processing with security patterns (sender allowlists, content filtering, sandboxed processing) |
| **react-email** | ~5K | Build HTML email templates with React components, visual email editor integration, render to HTML |
| **email-best-practices** | ~4K | Email deliverability — SPF/DKIM/DMARC, compliance (CAN-SPAM, GDPR, CASL), webhooks, accessibility |
| **resend-cli** | ~3K | Terminal operations — send emails, manage domains, contacts, templates, webhooks, API keys from shell/scripts/CI/CD |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Resend account** | Free tier: 100 emails/day. Sign up at [resend.com](https://resend.com) |
| **Resend API key** | Create at resend.com/api-keys — prefix `re_` |
| **Verified domain** | Required for production sending — verify in Resend dashboard |
| **Node.js** | Required for `react-email` and `resend` SDK usage |

---

## Key Capabilities

### Core Email API
The `resend` skill is the primary entry point. It handles idempotency keys (critical for preventing duplicate sends on retry), webhook signature verification, and template variable syntax. Always load this skill when an agent needs to send email — it catches gotchas that cause silent failures in production.

### Agent Inboxes
The `agent-email-inbox` skill is purpose-built for Hermes agents that process inbound email. It enforces sender allowlists, content filtering, and sandboxed processing — preventing untrusted email from controlling agent behavior. Critical for any agent that receives email programmatically.

### React Email Templates
The `react-email` skill enables building email templates as React components — with live preview, visual editing, and HTML rendering. Use for welcome emails, password resets, notifications, order confirmations, and newsletters.

### CLI Operations
The `resend-cli` skill provides full terminal control of the Resend platform. Send emails (including React Email `.tsx` templates via `--react-email` flag), manage domains, contacts, broadcasts — all from shell scripts or CI/CD pipelines.

---

## Quick Start

```bash
# 1. Install the core Resend skill
npx skills add resend/resend-skills --skill resend

# 2. Set API key
export RESEND_API_KEY="re_xxxx"

# 3. Install CLI (optional)
npx skills add resend/resend-skills --skill resend-cli

# 4. Send a test email (via resend-cli skill)
resend email send --from "onboarding@resend.dev" --to "your@email.com" \
  --subject "Hello from Hermes" --text "Email sent via Resend skills."

# 5. Set up agent inbox (if receiving email)
npx skills add resend/resend-skills --skill agent-email-inbox
# Agent will configure webhook endpoint and security rules via the skill
```

---

## Verification

```bash
# Check installed Resend skills
npx skills list | grep resend

# Verify API key works
curl -s -H "Authorization: Bearer $RESEND_API_KEY" \
  https://api.resend.com/domains | jq '.data | length'

# Test CLI
resend domains list
```

---

## Notes

- The `agent-email-inbox` skill's security patterns are **critical** — untrusted email can inject commands into agent workflows if not properly sandboxed
- The `resend` skill's idempotency key pattern prevents duplicate sends on retry — always use it for production email
- React Email templates can be rendered to HTML without a Resend account — useful for any email pipeline
- The free tier (100 emails/day) is sufficient for development and low-volume agent operations
- For high-volume agent email (notifications, reports), upgrade to a paid plan
