---
title: Slack + GitHub Integration for Hermes Agent  --  Automated Dev Workflow Notifications
description: Connect Slack and GitHub to Hermes Agent for automated PR notifications, issue triage, deployment status alerts, and daily standup digests. MCP server setup, webhook configuration, and cron patterns for development teams.
category: integrations
tags: [hermes-agent, integration, slack, github, pr-notifications, issue-tracking, deployment, devops, webhooks]
last_updated: 2026-06-16
---

# Slack + GitHub Integration  --  Automated Dev Workflow Notifications

## Architecture Overview

```
GitHub (Events) → Hermes Agent (Process) → Slack (Notifications)
        ↑                                        ↓
        └────── Slack Commands ←────────────────┘
```

The integration works in two directions:
- **Push:** GitHub webhooks or polling triggers Hermes to post updates in Slack.
- **Pull:** Slack slash commands or bot mentions trigger Hermes to query GitHub.

## Prerequisites

- A Slack workspace with permissions to create apps and install bots
- A GitHub repository (or organization) with webhook admin access
- Hermes Agent configured with Slack and GitHub MCP tools

## MCP Server Setup

### GitHub Tools

Configure your Hermes environment with a GitHub personal access token:

```bash
export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"
```

Required scopes: `repo` (private repos), `read:org` (organization access), `notifications` (for polling).

The key tools you'll use:
- Search for PRs by state, author, label, or branch
- List issues with filters for assignee, milestone, or label
- Get deployment statuses and workflow run results
- Read commit history and diffs

### Slack Tools

Configure a Slack bot token:

```bash
export SLACK_BOT_TOKEN="xoxb-xxxxxxxxxxxx"
```

Required scopes: `chat:write`, `channels:read`, `channels:history`, `users:read`.

Key tools:
- Post messages to channels or threads
- Search for existing messages (to avoid duplicates)
- List channels and users

## Core Automations

### Pull Request Notifications

**Goal:** Notify a Slack channel when PRs need attention.

**Cron Schedule:** Every 15 minutes during working hours (`*/15 9-17 * * 1-5`)

**Logic:**
1. Query GitHub for open PRs with no reviews or requested changes
2. For each PR found, check if a Slack notification was already sent (search channel history for PR number)
3. If new, post a notification with: PR title, author, branch, lines changed, link, and time open
4. If aging (>24 hours without review), escalate with @channel mention

**Hermes Prompt:**
```
Check GitHub for open pull requests in [ORG/REPO]. For each PR that hasn't been reviewed within [HOURS], post a notification to Slack #[CHANNEL]. Skip PRs we've already notified about. Format: PR title, author, link, lines changed, hours since creation. Escalate PRs older than 24h.
```

### Issue Triage Assistant

**Goal:** Route new GitHub issues to the right Slack channel based on labels.

**Cron Schedule:** Every 5 minutes

**Logic:**
1. Query GitHub for issues created or updated in the last 5 minutes
2. Read issue body, title, and labels
3. Determine destination channel based on label mapping (bug → #engineering-alerts, feature-request → #product, question → #support)
4. Post summary with priority assessment
5. If unlabeled, post to a triage channel with suggestion for appropriate label

**Label-to-Channel Mapping:**
```
bug, critical, security → #eng-alerts
enhancement, feature-request → #product-feedback
documentation → #docs
question, help-wanted → #community-support
```

### Deployment Status Monitor

**Goal:** Track deployment progress and alert on failures.

**Cron Schedule:** Every 2 minutes during active deployment windows

**Logic:**
1. Query GitHub Actions or deployment API for currently running workflows
2. Post deployment start to Slack with link to workflow run
3. Poll until completion (success or failure)
4. On success: post summary (duration, what changed, link to release)
5. On failure: post error details, failing step, and @ the last committer
6. Track deployment frequency and success rate over time in a thread summary

### Daily Standup Digest

**Goal:** Prepare a morning digest for standup meetings.

**Cron Schedule:** 8:45 AM daily (`45 8 * * 1-5`)

**Logic:**
1. Query merged PRs in the last 24 hours
2. Query opened/closed issues in the last 24 hours
3. Query deployment events in the last 24 hours
4. Compile into a structured digest and post to #standup channel
5. Format: "Yesterday's Shipments" with merged PRs, "Open Items" with new and blocked issues, "What's Deployed" with environment status

## Setting Up Webhooks (Alternative to Polling)

For real-time notifications instead of cron polling, configure GitHub webhooks:

1. Go to repository Settings → Webhooks → Add webhook
2. Payload URL: your Hermes webhook endpoint
3. Content type: `application/json`
4. Events: "Pull requests," "Issues," "Deployments," "Workflow runs"
5. Secret: generate a random string, store in `GITHUB_WEBHOOK_SECRET`

Webhooks eliminate polling latency but require your Hermes instance to be reachable from the internet. For internal/private deployments, cron polling is simpler and sufficient for most use cases.

## Best Practices

- **Deduplicate notifications.** Always search Slack history for the PR/issue number before posting. Use a consistent format (e.g., `[PR #1234]` in the message) so search is reliable.
- **Use threads.** Post follow-up comments as thread replies rather than new messages. This keeps channels clean.
- **Rate yourself.** Track how many notifications you send per day. If it exceeds ~20 in a single channel, aggregate more aggressively.
- **Respect working hours.** Route urgent issues (security, production incidents) 24/7. Route everything else only during working hours.
- **Test in a sandbox channel first.** Set up a #bot-testing channel and direct all notifications there until you've tuned the signal-to-noise ratio.

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
