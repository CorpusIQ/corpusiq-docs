---
name: gws-gmail
description: Read, search, and send Gmail from the terminal. Full Gmail API access for AI agents to manage email workflows, search inboxes, and send messages programmatically. 34.9K installs.
triggers:
  - "check my email"
  - "search gmail"
  - "send email from terminal"
  - "gmail automation"
  - "read inbox"
source: googleworkspace/cli
installs: 34900
---

# GWS Gmail

Full Gmail access from the terminal via Google Workspace CLI. Enables Hermes agents to read, search, and send emails programmatically.

## Setup

```bash
npx skills add googleworkspace/cli@gws-gmail
gws login
```

Requires Google OAuth. After authentication, the Gmail tools become available to the agent.

## Core Capabilities

- List and search inbox messages with Gmail search syntax
- Read full message content including attachments
- Send emails with HTML formatting
- Manage labels and threads
- Archive, trash, and modify message state

## Hermes Integration

Auto-registers as agent tools. Use in prompts: "Check my inbox for unread messages from the last 24 hours" or "Search for emails about the Q3 report."

## Pitfalls

- OAuth tokens expire after 1 hour. Use refresh token flow for persistent access.
- Large attachments require base64 decoding.
- Gmail API quotas: 250 quota units per user per second for reads.


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*
