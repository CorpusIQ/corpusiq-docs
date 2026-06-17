# IMAP Email

## What it unlocks
Not every mailbox is Gmail or Outlook. If you run email on Fastmail, ProtonMail Bridge, your own domain, or a hosted IMAP provider, this connector lets CorpusIQ read your mail the same way it reads Gmail — so search across "all my email" actually means all of it.

## Before you connect
- An email account that supports IMAP
- IMAP host, port, and an app password (most providers require an app-specific password, not your main login password)
- About 3 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find IMAP Email.
2. Click Configure.
3. <!-- screenshot: IMAP credential form in CorpusIQ -->
4. Enter your IMAP host (e.g. `imap.fastmail.com`), port (usually 993), email address, and app password.
5. Click Save. CorpusIQ verifies the connection by listing your folders.

You'll see IMAP change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Folder list and message counts
- Recent messages and full message content
- Keyword search across your mailbox

CorpusIQ never sends mail, deletes messages, or marks anything read.

## Questions you can ask
- "Find the email from my landlord about the lease."
- "Show me unread messages in my Inbox."
- "Search my mail for 'wire transfer'."
- "What folders are in my mailbox?"
- "Read the latest message from accounts@stripe.com."

## Troubleshooting
- **"Authentication failed"** — Most providers (Fastmail, iCloud, Yahoo, Gmail) require an *app password*, not your main account password. Generate one in your provider's security settings.
- **TLS errors** — Use port 993 with SSL, not 143 plain. If your provider uses STARTTLS on 143, switch to 993.
- **Folder list looks short** — Some providers hide certain folders (Trash, Spam) unless subscribed. Subscribe to them in your mail client first.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
