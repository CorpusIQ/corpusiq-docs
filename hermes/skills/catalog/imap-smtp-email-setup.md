---
title: IMAP/SMTP Email — OpenClaw Email Integration Setup Guide
description: Setup guide for the imap-smtp-email skill — bring email reading and sending capabilities to your OpenClaw agent. IMAP for inbox access, SMTP for sending.
last_updated: 2026-07-08
---

# IMAP/SMTP Email — OpenClaw Email Integration

**Publisher:** [boomsystel-code](https://skills.sh/boomsystel-code/openclaw-workspace) | **Installs:** 1,207 | **Category:** Email

Gives your OpenClaw agent full email capabilities — read inboxes via IMAP, send messages via SMTP. Works with Gmail, Outlook, custom mail servers, and any provider supporting standard IMAP/SMTP protocols.

## Prerequisites

- OpenClaw installed and running
- Node.js 18+
- Email account with IMAP/SMTP access enabled
- For Gmail: [App Password](https://support.google.com/accounts/answer/185833) or OAuth2 setup
- `npx` available (comes with Node.js)

## Installation

```bash
npx skills add boomsystel-code/openclaw-workspace/imap-smtp-email
```

Verify installation:

```bash
npx skills list | grep imap-smtp-email
```

## Configuration

Create or update your OpenClaw config with email credentials:

```json
{
  "email": {
    "imap": {
      "host": "imap.gmail.com",
      "port": 993,
      "tls": true,
      "user": "your-email@gmail.com",
      "password": "${IMAP_PASSWORD}"
    },
    "smtp": {
      "host": "smtp.gmail.com",
      "port": 587,
      "tls": true,
      "user": "your-email@gmail.com",
      "password": "${SMTP_PASSWORD}"
    }
  }
}
```

**⚠️ Security:** Never hardcode passwords in config files. Use environment variables:

```bash
export IMAP_PASSWORD="your-app-password"
export SMTP_PASSWORD="your-app-password"
```

## Capabilities

### Read Emails

The agent can:
- List recent emails from inbox
- Search emails by subject, sender, date range
- Read full email bodies (plain text and HTML)
- Download attachments
- Mark emails as read/unread

### Send Emails

The agent can:
- Compose and send new emails
- Reply to existing threads
- CC/BCC recipients
- Attach files
- Set custom headers

### Email Management

- Move emails between folders
- Flag/star important messages
- Delete/archive emails
- Search across all folders

## CLI Reference

Once installed, the skill adds these commands to your agent's toolset:

```
Command                    Description
─────────────────────────────────────────────
list_inbox [limit]         List recent inbox messages
search_emails <query>      Search emails by criteria
read_email <id>            Read full email content
send_email <to> <subject>  Compose and send email
reply_to <id>              Reply to an email thread
get_attachments <id>       Download email attachments
move_email <id> <folder>   Move email to folder
```

## CorpusIQ Use Cases

- **Lead response automation:** Agent monitors inbox, identifies qualified leads, drafts contextual responses
- **Email campaign tracking:** Monitor campaign replies, extract metrics, update dashboards
- **Support ticket routing:** Read support emails, classify urgency, route to appropriate team
- **Invoice/receipt processing:** Extract attachment data from vendor emails for bookkeeping

## Troubleshooting

### Connection refused

```bash
# Verify IMAP is accessible
openssl s_client -connect imap.gmail.com:993 -crlf

# Verify SMTP is accessible  
openssl s_client -connect smtp.gmail.com:587 -starttls smtp -crlf
```

### Authentication failed

- Gmail: Ensure "Less secure app access" is off and you're using an App Password
- Outlook/Hotmail: Enable IMAP in settings, use app-specific password
- Custom servers: Verify TLS certificate is valid

### Emails not appearing

- Check IMAP folder path prefix (some servers use `INBOX.` prefix)
- Verify the agent has read permissions on the folder
- Check spam/junk folders if expected emails are missing

---

*← [IMAP/SMTP Setup Guide](/hermes/skills/catalog/imap-smtp-email-setup/) | [Discovery Page](/hermes/skills/marketplace/new-june28-2026/) →*

*↑ [Skills Catalog](/hermes/skills/catalog/)*

---

*Part of the Hermes Skills Library — curated by CorpusIQ. Content remains attributed to original authors and repositories. [CorpusIQ](https://corpusiq.io) — one MCP endpoint, all your business tools.*
