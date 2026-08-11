---
title: Hermes Nextcloud Integration Setup Guide
description: Install and configure adnw-vinc/hermes-nextcloud — Nextcloud files, notes, calendar, and contacts bridge for Hermes Agent.
category: integration
publisher: adnw-vinc
maturity: beta
source: https://github.com/adnw-vinc/hermes-nextcloud
---

# Hermes Nextcloud Integration — Setup Guide

Nextcloud integration for Hermes Agent by [adnw-vinc](https://github.com/adnw-vinc/hermes-nextcloud). Bridges Nextcloud's file storage, notes, calendar, and contacts into Hermes — enabling agents to operate on self-hosted cloud data without third-party services.

## What It Provides

- **File operations** — browse, read, write, and share files via WebDAV
- **Notes** — create/edit Nextcloud Notes with Markdown support
- **Calendar** — read/create/modify events via CalDAV
- **Contacts** — search and manage contacts via CardDAV
- **Talk** — send messages via Nextcloud Talk API
- **Share links** — create and manage public/private share links

## Installation

```bash
# Install via skills.sh
npx skills add https://github.com/adnw-vinc/hermes-nextcloud

# Manual clone
git clone https://github.com/adnw-vinc/hermes-nextcloud.git ~/.hermes/skills/hermes-nextcloud
```

## Configuration

```yaml
nextcloud:
  base_url: "https://cloud.yourdomain.com"
  username: "${NEXTCLOUD_USER}"
  password: "${NEXTCLOUD_APP_PASSWORD}"   # Use app password, not main password
  verify_ssl: true
  services:
    files: true       # WebDAV
    notes: true       # Notes API
    calendar: true    # CalDAV
    contacts: true    # CardDAV
    talk: false       # Talk API (optional)
```

**Recommended**: Use a Nextcloud app password (generated in Settings → Security → Devices & sessions) rather than your main account password. This limits the agent's scope and allows easy revocation.

## Key Workflows

### File operations

```
List files in my Nextcloud "Projects/CorpusIQ/" folder.
Upload the latest daily report to Nextcloud.
```

### Notes management

```
Create a meeting note in Nextcloud Notes for today's standup.
Search my Nextcloud Notes for "Q3 roadmap".
```

### Calendar integration

```
What's on my Nextcloud calendar today?
Create a "Product Review" event for Friday 2-3 PM.
```

### Contact search

```
Find the contact for "Brandon Belot" in my Nextcloud contacts.
```

## Verification

```bash
# Test connection
hermes chat -q "List the root folder contents of my Nextcloud at https://cloud.yourdomain.com"

# Test notes
hermes chat -q "List my Nextcloud notes"
```

## Pitfalls

- **App password required**: Nextcloud's main password may not work with WebDAV if 2FA is enabled. Always generate an app password.
- **Self-signed certificates**: If using a self-signed cert, set `verify_ssl: false` — but only for internal/development deployments.
- **WebDAV rate limiting**: Nextcloud may throttle rapid file operations. Use batch operations where possible.
- **CalDAV timezone**: Ensure the Nextcloud server and Hermes host are in the same timezone or timezone-aware.
- **File locking**: WebDAV locks are not automatically released on session timeout. Implement a lock timeout.

## See Also

- [adnw-vinc/hermes-nextcloud repo](https://github.com/adnw-vinc/hermes-nextcloud)
- [Nextcloud Developer Docs](https://docs.nextcloud.com/server/latest/developer_manual/)
- [Apple Calendar Setup](/hermes/skills/catalog/apple-calendar-setup/)
- [Google Workspace Setup](/hermes/skills/catalog/google-workspace/)

---

*Setup guide by CorpusIQ. Source: [adnw-vinc/hermes-nextcloud](https://github.com/adnw-vinc/hermes-nextcloud).*
