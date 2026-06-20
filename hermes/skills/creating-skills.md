---
title: Creating Custom Skills for Hermes Agent — Complete Step-by-Step Guide
description: Complete guide to creating custom Hermes Agent skills. SKILL.md anatomy, trigger patterns, verification steps, error recovery, testing methodology, and publishing. Build reusable AI agent workflows step by step.
category: skills
tags: [hermes-agent, skills, custom-skills, skill-development, triggers, testing, publishing, reusable-workflows]
last_updated: 2026-06-16
---

# Creating Custom Skills — A Complete Step-by-Step Guide

## Before You Start: The Rule of Three

Before creating a skill, you should have performed the task manually at least three times. The first time teaches you what's needed. The second time refines your approach. By the third time, you know the pattern well enough to encode it as a skill. Skills created before the third manual run are often over-engineered or miss key edge cases.

Ask yourself:
- Do I understand every tool call in the workflow and what can go wrong with each one?
- Have I handled errors at least once during manual execution?
- Can I explain this workflow to a teammate in under two minutes?

If yes to all three, you're ready.

## SKILL.md Anatomy

Every skill lives in a directory with a `SKILL.md` file at its root. Here is the complete anatomy:

```markdown
---
name: my-skill-name
description: A one-sentence description of what this skill does
version: 1.0.0
author: your-handle
tags: [tag1, tag2, category]
required_connectors: [connector-a, connector-b]
quality_tier: beta
---

# Skill Name

## What This Skill Does
A clear 2-3 sentence description. Someone browsing the catalog should
understand the use case immediately.

## When to Use This Skill
Describe the scenarios where this skill is useful. Include example
trigger phrases that should activate it.

## Required Setup
- Connector A: [what permissions are needed and why]
- Connector B: [what permissions are needed and why]
- Environment variables: [any required config]

## Workflow
Each step is a discrete action with tool calls, validation, and error handling.

### Step 1: Gather Context
Tool: summary_of_what_you_call
What it does: description
Error handling: what happens if this fails

### Step 2: Process Data
...

### Step 3: Present Results
...

## Example Output
Show what the user should expect to see. Use realistic placeholder data.

## Troubleshooting
Common issues and how to resolve them.

## Changelog
- 1.0.0: Initial release
```

Don't skip the metadata block. The `required_connectors` field lets Hermes verify everything is available before starting. The `tags` field makes your skill discoverable.

## Trigger Patterns

Trigger patterns determine when your skill activates. They should be specific enough to avoid false positives but broad enough to catch real user intent.

**Good trigger patterns:**
- "Check our marketing performance this week"
- "How are our ads doing?"
- "Show me campaign ROI"
- "Marketing health check"

**Bad trigger patterns:**
- "marketing" (too broad — fires on any mention of marketing)
- "Check our marketing performance this week including Facebook Ads and Google Analytics" (too specific — won't match natural variations)

Write 5-10 trigger patterns covering different ways a user might ask for your skill. Include variations in formality ("Show me our ad performance" vs. "I'd like to review advertising metrics"), time windows ("this week" vs. "last 7 days"), and specificity ("campaigns" vs. "Facebook campaigns").

## Verification Steps

Between major workflow steps, verify the data you received:

**Schema verification.** Does the response have the expected shape? Required fields present? Data types correct? If a tool returns an error instead of data, your skill should catch that immediately.

**Completeness verification.** Did you get everything you asked for? If you requested 200 records and got 47, it's either a pagination issue or a problem. Log the discrepancy.

**Freshness verification.** Is this data current? If a timestamp is older than expected, surface a caveat. "Last synced 3 days ago" is different from "real-time data."

**Business rule verification.** Are values within expected ranges? If average order value suddenly tripled, something might be wrong with the data — not necessarily your skill, but worth flagging.

## Error Recovery Patterns

Every tool call can fail. Your skill should handle these failure modes explicitly:

**Transient errors** (network timeout, rate limit, temporary API error): Retry with backoff. Start at 1 second, double each retry, cap at 3 attempts. Include jitter to avoid thundering-herd problems.

**Authentication errors** (expired token, insufficient permissions): Don't retry — these won't self-resolve. Return a clear message: "Connector X needs re-authentication. Visit [link] to reconnect."

**Data errors** (no results found, invalid parameters, upstream validation failure): Return what you can with clear caveats. "No orders found for the specified date range. If you expected results, verify the date range and try again."

**Partial failures** (batch processing, some records failed): Return successes with a summary of failures. "Processed 47 of 50 records. 3 failed: [IDs with error reasons]. The failed records have been logged for review."

**Unknown errors**: Catch-all that logs the full error and returns a user-friendly message. "Something went wrong during step X. The error has been logged. Try again or check your connector configuration."

## Testing Methodology

Test your skill systematically before sharing it:

### Unit-Level Testing
Test each step in isolation by providing mock inputs. Does step 3 produce correct output when given the expected format from step 2? If you can't test steps independently, refactor until you can.

### Happy Path Testing
Run the full skill end-to-end with known-good data. Does it complete without errors? Is the output formatted correctly? Does it finish in a reasonable time?

### Edge Case Testing
Run your skill with:
- **Empty data:** What happens when there are no results?
- **Maximum data:** What happens with 10,000 records instead of 50?
- **Missing optional fields:** What if the API omits fields that are usually present?
- **Special characters:** What if names contain Unicode, emoji, or SQL-like strings?
- **Date boundaries:** What happens at month end, year end, DST transitions?

### Error Injection Testing
Deliberately break things and verify recovery:
- Disconnect a connector mid-skill
- Return malformed data from a mock tool
- Exceed a rate limit
- Provide invalid parameters

### Regression Testing
After any change to your skill, re-run the full test suite. Skills that depend on external APIs can break when those APIs change. Schedule a weekly automated smoke test for production skills.

## Example: A Complete Skill Walkthrough

Let's build a "Customer Insight" skill. This skill looks up a customer across CRM, billing, and support systems to give a unified view.

**SKILL.md (abbreviated):**

```markdown
---
name: customer-insight
description: Generates a unified customer profile from CRM, billing, and support data
version: 1.0.0
author: community
tags: [customer, crm, support, billing]
required_connectors: [crm, quickbooks, email]
quality_tier: beta
---

# Customer Insight

## What This Skill Does
Given a customer name or email, produces a unified profile combining CRM
contact data, recent billing activity, open support tickets, and last
communication summary.

## Workflow

### Step 1: Find the Customer
Search CRM by name or email. If multiple matches, present options for user
to select.

Error: No match → "No customer found with that name/email."
Error: Multiple matches → Present a numbered list for user selection.
Error: CRM unavailable → "CRM connector is not responding. Try again or
check your connection."

### Step 2: Gather Profile Data
Fetch the selected customer's full CRM record.

Error: Record deleted between search and fetch → Retry search to confirm.

### Step 3: Gather Billing Data
Query billing system for recent invoices and payment status.

Error: Billing system unavailable → Show CRM data with note: "Billing data
unavailable — QuickBooks connector not responding."

### Step 4: Gather Support Data
Check for open support tickets and recent resolved tickets.

Error: No support connector → Skip, present profile without support data.

### Step 5: Present Unified Profile
Format into sections: Contact, Billing, Support, Recent Activity.
```

This skill demonstrates the key pattern: each step has explicit error handling, partial results are better than total failure, and the user always knows which data sources contributed to the output.

## Publishing Your Skill

When your skill is tested and documented:

1. Verify it works with example.com placeholder data (no real credentials or data)
2. Choose the appropriate quality tier based on your testing
3. Submit to your preferred marketplace with the skill directory
4. Respond to community feedback and update as needed

See the [Skill Marketplaces guide](skill-marketplaces.md) for publishing instructions for each marketplace.

## Maintaining Your Skill

Skills need maintenance. Plan to:

- **Check monthly:** Do the API endpoints still work the same way?
- **Update on connector changes:** If a connector adds required parameters or changes response format, update your skill.
- **Respond to issues:** Community users will find edge cases you didn't. Fix them.
- **Deprecate gracefully:** If you stop maintaining a skill, mark it deprecated with a notice and migration suggestion.

A well-maintained skill compounds in value. Every fix benefits every user.

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
