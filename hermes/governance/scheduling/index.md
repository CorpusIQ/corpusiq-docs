# Production Cron Reference Architecture

38 crons run this agent autonomously 24/7. This is the complete reference — every schedule, every purpose, every delivery target.

## Cron Categories

| Category | Count | Core Purpose |
|----------|-------|--------------|
| Email Operations | 4 | Inbox monitoring, lead classification, auto-response, job forwarding |
| Social Publishing | 3 | Cross-platform posting (X, LinkedIn), content rotation, promotion |
| Content Operations | 2 | Daily video generation, cross-platform distribution |
| Community Engagement | 5 | Help-first commenting, GitHub issues, channel scanning, IG monitoring |
| Research & Discovery | 5 | Tech research, MCP servers, skills, GitHub repos, Product Hunt |
| Governance | 6 | Health monitoring, self-improvement, drift prevention, auth checks, directories |
| Memory | 1 | Nightly dream cycle for knowledge consolidation |
| Growth | 2 | Organic discovery, GEO tools |
| Job Search | 1 | Daily executive job search (confidential) |
| GitHub | 2 | Issue polling, auto-acknowledgment |
| Release Monitor | 1 | Hermes Agent version tracking |

---

## Complete Cron Registry

### Email Operations

```
eef64b6eed8e  */15 * * * *     email-monitor           no_agent    Telegram T2
              └─ Check team@ + info@ every 15 min
              └─ 4-tier classification: HIGH_VALUE, QUALIFIED, INTERESTED, SPAM
              └─ HIGH_VALUE → instant Telegram alert → 30min SLA

577abcb19c93  */15 * * * *     forward-handler         no_agent    local
              └─ Forward job replies: team@ → personal inbox

d6c65b56ba64  */30 * * * *     email-responder         AI agent    local
              └─ AI-powered HTML responses to qualified leads
              └─ Loads corpusiq-email-operating-rules + execution-discipline

5497eb2abf2c  */30 * * * *     job-reply-forwarder     no_agent    local
              └─ Backup forward handler for job search replies
```

### Social Publishing

```
16ab362e7ca9  0 6,9,15 * * *   social-posting          AI agent    local
              └─ 3x daily: 6 AM, 9 AM, 3 PM AZ
              └─ X + LinkedIn Page via Postiz on Mac Mini
              └─ Loads social-cadence-engine + execution-discipline

225a69ff30da  0 7,14 * * *     daily-rotation          AI agent    local
              └─ 2 X posts promoting CorpusIQ via Postiz

e9c856a66eca  0 8,16 * * 1-5   github-mcp-promotion    AI agent    local
              └─ Weekdays: 8 AM, 4 PM AZ
              └─ GitHub contributions + natural CorpusIQ mentions
```

### Content Operations

```
8ec41d554bc6  0 6 * * *        video-pipeline          AI agent    local
              └─ Daily 6 AM: UGC video generation
              └─ HeyGen v2 API → FFmpeg → Email for review → Postiz publish
              └─ 10 scenario library, 6-avatar rotation, 14-day no-repeat

fc7d32e3d588  0 8,11,14,17,20  cross-platform-monitor  AI agent    Telegram T2
              └─ 5x daily: Check all platforms for new comments/messages
```

### Community Engagement

```
ddacec4011bd  0 6,8,10,12,15,17 help-first-commenting  AI agent    local
              └─ 6x daily: Find operators asking questions
              └─ Answer helpfully — mention product only if relevant
              └─ Skip banned platforms (Reddit, HN)

079b3604c42e  0 5,7,10,17 * * * github-issue-engagement AI agent   local
              └─ 4x daily: Help-first on high-value issues
              └─ 5 AM, 7 AM, 10 AM, 5 PM AZ

2269fb270a77  0 8 * * *         daily-channel-scan      AI agent    Telegram T2
              └─ Scan all platforms for mentions, comments, engagement

aa2fafce8d80  0 10,15 * * *     ig-comment-monitor      AI agent    Telegram T2
              └─ Instagram comment monitoring + helpful replies
```

### Research & Discovery

```
c3e3df5974f2  0 */6 * * *       tech-research           AI agent    local
              └─ Every 6 hours: Discover new tools, AI developments

834a43fb1148  0 3,11,19 * * *   mcp-server-monitor      AI agent    Telegram T2
              └─ 3x daily: Check mcp.so, mcpservers.org for new servers

48d37f56d35c  0 4,12,20 * * *   skills-monitor          AI agent    Telegram T2
              └─ 3x daily: Check skills.sh for new skills

9ad1f43ff06b  0 9 * * *         github-daily-discovery  AI agent    local
              └─ Find new GitHub directories to submit CorpusIQ to

d3bb38ade338  15 */2 * * *      ph-rss-monitor          no_agent    local
              └─ Every 2 hours: Product Hunt RSS for competitor launches
```

### Governance

```
5ad87b93dc3b  0 22 * * *        system-health-monitor   AI agent    Telegram T2
              └─ 10 PM: Verify all crons, tokens, APIs operational

5a837c3d87f9  0 23 * * *        daily-self-improvement  AI agent    local
              └─ 11 PM: Review mistakes, patch skills, update memory

4c5a50f21ea2  0 1 * * *         drift-prevention        AI agent    Telegram T2
              └─ 1 AM: Governance integrity — registry, skills, memory sync

f44fa8b3b0b1  0 7 * * *         auth-health-check       no_agent    local
              └─ 7 AM: Verify all OAuth tokens and API keys

d87b726f0c7c  0 10 * * *        mcp-directory-check     AI agent    local
              └─ Verify MCP directory listings still live

0de31ae4fd9b  0 * * * *         docs-repo-monitor       no_agent    local
              └─ Hourly: Monitor corpusiq-docs for new PRs/issues
```

### Memory

```
be6ee0113368  0 3 * * *         gbrain-dream            AI agent    local
              └─ 3 AM: Memory consolidation — merge, deduplicate, strengthen
```

### Growth

```
57d13bdb4201  0 7,19 * * *      organic-discovery       AI agent    Telegram T2
              └─ 7 AM + 7 PM: Find organic promotion opportunities

c63dd7058200  0 7 * * *         daily-growth-geo        AI agent    Telegram T2
              └─ 7 AM: Growth tools + GEO directory maintenance
```

### Job Search

```
06f4f056ade8  0 7 * * *         executive-job-search       AI agent    Telegram T2
              └─ 7 AM: Search for executive roles, generate resumes
              └─ CONFIDENTIAL — never mention CorpusIQ
```

### GitHub Automation

```
7a6a4007c834  * * * * *         github-issue-poll       no_agent    Telegram T2
              └─ Every minute: Poll GitHub issues

2d3a157ec92c  0 */6 * * *       auto-ack-issues         no_agent    Telegram T2
              └─ Every 6 hours: Auto-ack enhancement issues (draft)
```

### Hermes Release

```
be2bee6a3f05  0 2,10,18 * * *   hermes-release-monitor  AI agent    Telegram T2
              └─ 3x daily: Check for new Hermes releases
```

---

## Cron Schedule Map (Arizona / MST)

```
Hour  │ Active Crons
──────┼────────────────────────────────────────────────────────
00:00 │
01:00 │ ██ drift-prevention
02:00 │ ██ hermes-release-monitor
03:00 │ ██ gbrain-dream · mcp-server-monitor
04:00 │ ██ skills-monitor
05:00 │ ██ github-issue-engagement (1/4)
06:00 │ ██████ video-pipeline · social-posting (1/3) · help-first (1/6)
07:00 │ ██████████ job-search · auth-health · daily-rotation (1/2) · github-issues (2/4) · growth-geo · organic-discovery (1/2)
08:00 │ ██████ github-promotion (1/2) · help-first (2/6) · channel-scan · cross-platform (1/5)
09:00 │ ██████ social-posting (2/3) · github-discovery
10:00 │ ██████████ help-first (3/6) · ig-monitor (1/2) · mcp-directory · github-issues (3/4) · hermes-release (2/3)
11:00 │ ██ cross-platform (2/5) · mcp-server-monitor (2/3)
12:00 │ ████ help-first (4/6) · skills-monitor (2/3)
13:00 │
14:00 │ ██ daily-rotation (2/2) · cross-platform (3/5)
15:00 │ ████ social-posting (3/3) · help-first (5/6) · ig-monitor (2/2)
16:00 │ ██ github-promotion (2/2)
17:00 │ ████ help-first (6/6) · github-issues (4/4) · cross-platform (4/5)
18:00 │ ████ daily-report · hermes-release (3/3)
19:00 │ ██ mcp-server-monitor (3/3) · organic-discovery (2/2)
20:00 │ ████ skills-monitor (3/3) · cross-platform (5/5)
21:00 │
22:00 │ ██ system-health
23:00 │ ██ self-improvement
```

---

## Cron Patterns

### Pattern 1: AI Agent Cron (complex reasoning)

```bash
hermes cron create \
  --prompt "Your self-contained task prompt here" \
  --skills "skill-one,skill-two" \
  --schedule "0 6 * * *" \
  --deliver "telegram:-100CHATID:TOPICID" \
  --enabled-toolsets "terminal,web,file,skills,send_message"
```

**When to use:** Anything needing reasoning — social posting, email response, research, content generation.

### Pattern 2: No-Agent Script (mechanical tasks)

```bash
hermes cron create \
  --script "email-monitor.py" \
  --schedule "*/15 * * * *" \
  --no-agent true \
  --deliver "telegram:-100CHATID:TOPICID"
```

**When to use:** Mechanical polling — email checks, GitHub polling, RSS monitoring. Faster, cheaper (no LLM), more reliable.

### Pattern 3: Script + Agent Pipeline

```bash
# Job A: Collect data (no-agent script, runs every hour)
hermes cron create \
  --script "collect-metrics.py" \
  --schedule "0 * * * *" \
  --no-agent true \
  --deliver "local"

# Job B: Process data (AI agent, runs after Job A, injects its output)
hermes cron create \
  --prompt "Analyze the metrics collected below and identify anomalies" \
  --schedule "5 * * * *" \
  --context-from "job-a-id"
```

**When to use:** Data collection + analysis pipeline. Saves tokens on collection, uses LLM only for insight.

---

## Health Monitoring

The 10 PM system health monitor checks:

```python
# What it verifies nightly:
check_1 = cronjob_list()                    # All crons running?
check_2 = gmail_token_valid()              # team@ + info@ tokens
check_3 = github_token_valid()             # Classic PAT
check_4 = heygen_token_valid()             # Video pipeline
check_5 = postiz_integrations_alive()      # X + LinkedIn + TikTok + Instagram
check_6 = corpusiq_mcp_connected()         # 53 tools available
check_7 = honcho_connected()               # Peer memory
check_8 = gbrain_indexing()                # Organizational memory
check_9 = disk_space()                     # >10% free
check_10 = memory_usage()                  # <90%
```

Failures are reported to Telegram Topic 2. The 1 AM drift prevention cron does a deeper integrity check.

---

## Creating Your First Cron

```bash
# 1. Start simple — check your email every 15 minutes
hermes cron create \
  --name "my-email-watch" \
  --prompt "Check Gmail for unread messages. Summarize new emails in one sentence each. Be silent if inbox is empty." \
  --schedule "*/15 * * * *" \
  --enabled-toolsets "terminal,web,file,send_message"

# 2. Add a daily report
hermes cron create \
  --name "my-daily-report" \
  --prompt "Generate a bullet-point summary of everything that happened today. What worked? What broke? What should I know for tomorrow?" \
  --schedule "0 18 * * *" \
  --enabled-toolsets "terminal,web,file,send_message"

# 3. Add nightly self-improvement
hermes cron create \
  --name "my-self-improvement" \
  --prompt "Review today's tasks. What could be improved? Update relevant skills with learned patterns." \
  --schedule "0 23 * * *" \
  --enabled-toolsets "terminal,file,skills"
```

---

## Lessons Learned

1. **No-agent scripts for polling** — mechanical tasks don't need LLMs. Save tokens.
2. **Rate limit awareness** — X is limited to ~10/day, LinkedIn Page to 2/day. Build schedules around it.
3. **Error loops kill crons** — if a platform is down, STOP. Don't retry. Log and move on.
4. **Delivery targets matter** — Telegram T2 for human-readable reports, `local` for machine-readable logs.
5. **Context-from is powerful** — chain crons: collect data with a script, analyze with an agent.
6. **Mass pauses are a symptom** — if you pause 15 crons at once, something cascaded. Find the root cause.

---

*Next: [Memory Architecture](/hermes/knowledge/) · [MCP Integration](/hermes/mcp/) · [Deployment Patterns](/hermes/infrastructure/)*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*
