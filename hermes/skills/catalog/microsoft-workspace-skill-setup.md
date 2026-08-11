---
title: Microsoft Workspace Skill Setup Guide
description: Install and configure Andrew-Girgis/microsoft-workspace-skill — Outlook email, calendar, and Microsoft 365 Graph API access for Hermes Agent.
category: integration
publisher: Andrew-Girgis
maturity: beta
source: https://github.com/Andrew-Girgis/microsoft-workspace-skill
---

# Microsoft Workspace Skill — Setup Guide

Microsoft 365 integration for Hermes Agent by [Andrew-Girgis](https://github.com/Andrew-Girgis/microsoft-workspace-skill). Provides Outlook email/calendar, Microsoft Graph API access, and Teams integration — essential for enterprise Hermes deployments in Microsoft shops.

## What It Provides

- **Outlook Email** — read, send, search, and organize emails via Microsoft Graph
- **Outlook Calendar** — create, read, update, and delete events
- **Contacts** — search and manage Outlook/Exchange contacts
- **Teams** — send messages to Teams channels (read-only for threads)
- **OneDrive/SharePoint** — file operations via Microsoft Graph
- **To Do** — task management via Microsoft To Do API

## Installation

```bash
# Install via skills.sh
npx skills add https://github.com/Andrew-Girgis/microsoft-workspace-skill

# Manual clone
git clone https://github.com/Andrew-Girgis/microsoft-workspace-skill.git ~/.hermes/skills/microsoft-workspace
```

## Authentication Setup

This skill requires Microsoft Graph API access via OAuth 2.0:

### Step 1: Register an Azure AD Application

1. Go to [Azure Portal → App Registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
2. Click "New registration"
3. Name: "Hermes Agent Integration"
4. Redirect URI: `http://localhost:8080/callback` (for device auth)
5. Click "Register"

### Step 2: Configure API Permissions

Add these delegated permissions under "API Permissions":
- `Mail.ReadWrite`
- `Calendars.ReadWrite`
- `Contacts.ReadWrite`
- `Files.ReadWrite`
- `Tasks.ReadWrite`
- `User.Read` (for profile)

### Step 3: Create Client Secret

1. Go to "Certificates & secrets"
2. Create "New client secret"
3. Save the secret value immediately (it won't be shown again)

### Step 4: Configure the Skill

```yaml
microsoft_workspace:
  client_id: "${MS_CLIENT_ID}"
  client_secret: "${MS_CLIENT_SECRET}"
  tenant_id: "${MS_TENANT_ID}"          # or "common" for multi-tenant
  redirect_uri: "http://localhost:8080/callback"
  scopes:
    - "Mail.ReadWrite"
    - "Calendars.ReadWrite"
    - "Contacts.ReadWrite"
    - "Files.ReadWrite"
    - "Tasks.ReadWrite"
```

### Step 5: First Authentication

```bash
# The first time, Hermes will open a browser for OAuth consent
hermes chat -q "Check my Outlook inbox for unread emails"
# Follow the browser prompt to authorize
```

The access and refresh tokens are stored securely in `~/.hermes/secrets/microsoft-workspace.json`.

## Key Workflows

### Email operations

```
Check my Outlook inbox for unread emails from @corpusiq.io.
Send an email to brandon.b@corpusiq.io with subject "Q3 Planning Update".
```

### Calendar

```
What meetings do I have tomorrow?
Schedule a 30-minute sync with the dev team on Friday at 10 AM.
```

### Teams

```
Send a message to the "Product" Teams channel: "New skills sweep published — 31 new Hermes skills discovered."
```

### File search

```
Find all PowerPoint files in my OneDrive modified this week.
```

## Verification

```bash
# Test authentication
hermes chat -q "List my Outlook folders"

# Test calendar
hermes chat -q "Show today's calendar events"
```

## Pitfalls

- **⚠️ Admin consent**: Some organizations require admin consent for Graph API permissions. If you see "Need admin approval," contact your Azure AD admin.
- **Token refresh**: Access tokens expire in 1 hour. The skill auto-refreshes using the refresh token. If refresh fails, re-auth is required.
- **Throttling**: Microsoft Graph has rate limits (~10K requests/day for most endpoints). Heavy email scanning can trigger throttling.
- **Shared mailboxes**: Accessing shared mailboxes requires additional permissions (`Mail.ReadWrite.Shared`). Not included by default.
- **S/MIME encrypted emails**: Cannot be read by the agent. The skill will skip encrypted messages and log a warning.
- **Government clouds**: If using GCC/GCC-High/DoD tenants, use the appropriate Graph endpoint (`graph.microsoft.us`, not `graph.microsoft.com`).

## See Also

- [Andrew-Girgis/microsoft-workspace-skill repo](https://github.com/Andrew-Girgis/microsoft-workspace-skill)
- [Microsoft Graph API Docs](https://learn.microsoft.com/en-us/graph/)
- [Google Workspace Setup](/hermes/skills/catalog/google-workspace/)
- [IMAP SMTP Email Setup](/hermes/skills/catalog/imap-smtp-email-setup/)

---

*Setup guide by CorpusIQ. Source: [Andrew-Girgis/microsoft-workspace-skill](https://github.com/Andrew-Girgis/microsoft-workspace-skill).*
