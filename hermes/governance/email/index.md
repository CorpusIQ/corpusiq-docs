---
title: Email Operations
description: Autonomous email management for dual-account operations. Monitoring, send checklist, HTML templates, response standards.
---

# Email Operations

CorpusIQ agents manage multiple email accounts autonomously — monitoring, responding, and sending with strict quality gates.

## Dual Account Architecture

```
team@example.com (primary)
  ├─ Growth operations
  ├─ Inbound lead responses
  ├─ Outbound cold email
  └─ Daily reports

info@example.com (secondary)
  ├─ General inquiries
  ├─ Partnership requests
  └─ Forwarded to team@ for processing

personal@example.com (personal)
  ├─ Job applications (confidential)
  └─ Never in daily reports
```

## Monitoring

A master monitor checks both accounts every 30 minutes:

```python
# Dual-account monitor
accounts = ["team@example.com", "info@example.com"]
for account in accounts:
    new_messages = check_inbox(account, since=last_check)
    for msg in new_messages:
        classify_and_respond(msg)
```

## Send Checklist (HARD GATE)

Before ANY outbound email, verify:
1. ✅ Correct from address (team@ for business, personal@ for personal)
2. ✅ Correct signature and phone number policy
3. ✅ HTML formatting validates
4. ✅ No emdashes (—) — use hyphens only
5. ✅ No AI buzzwords or detectable patterns
6. ✅ Links are live and correct
7. ✅ Recipient domain verified (not a competitor)
8. ✅ Not on do-not-contact list

## Response Standards

| Priority | Response Time | Example |
|----------|--------------|---------|
| Lead inquiry | 15 minutes | "Interested in CorpusIQ" |
| Partnership | 1 hour | "Let's collaborate" |
| Support | 4 hours | "How do I..." |
| General | 24 hours | "Hey, cool product" |

## HTML Templates

All outbound email uses professional HTML templates:
- Responsive design (mobile + desktop)
- CorpusIQ branding
- Clear CTA buttons
- Plain-text fallback
- Tracking pixel for open rates

## Forwarding Rules

```
info@example.com → forwards unclear replies to team@
team@example.com → agent processes directly
personal@example.com → NEVER forwarded, confidential
```

## Common Operations

| Operation | Command |
|-----------|---------|
| Check inbox | `get_gmail_message` / `search_gmail` |
| Send email | Via corpusiq-email-send-checklist skill |
| Search history | `search_gmail` with Gmail search syntax |
| Read thread | `get_gmail_message` with message_id |

## Security Rules

1. Never expose phone numbers in email
2. Never forward personal account messages
3. Always verify sender before responding
4. Log all outbound messages to activity-log.jsonl
5. Token refresh: Google OAuth tokens persist via headless automation

---

*← [Monitoring](/hermes/governance/monitoring/) | [Registry](/hermes/governance/registry/) →*
*↑ [Governance](/hermes/governance/)*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
