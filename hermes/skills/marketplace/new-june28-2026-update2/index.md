---
title: "New Skills Discovered — June 28, 2026 (Update 2)"
description: "9 new skills discovered — sundial-org OpenClaw collection (news-summary, ffmpeg-video-editor, Jina Reader, reminders, proactive agent, topic monitor, financial analysis), plus aradotso marketing skill and prompt-security audit watchdog."
last_updated: 2026-07-08
---

# New Skills Discovered — June 28, 2026 (Update 2)

Sweep date: **June 28, 2026 (evening)** | Source: [skills.sh API](https://skills.sh) | Method: 14-term query sweep → precise cross-reference against all existing catalog

**Summary:** 9 new skills discovered — complements the [morning sweep](/hermes/skills/marketplace/new-june28-2026/) (3 skills) and [afternoon update](/hermes/skills/marketplace/new-june28-2026-update/) (17 skills). This sweep covers the **sundial-org/awesome-openclaw-skills** collection (7 skills), plus an aradotso marketing automation skill and a prompt-security audit watchdog.

---

## Top Find: sundial-org/awesome-openclaw-skills (7 skills)

The `sundial-org/awesome-openclaw-skills` repo was only partially catalogued (2 skills in the June 26 sweep). This sweep completes the coverage with 7 new skills spanning news, video, search, reminders, proactive monitoring, and financial analysis.

| Skill | Installs | Category |
|-------|----------|----------|
| [news-summary](https://skills.sh/sundial-org/awesome-openclaw-skills/news-summary) | 1,245 | News & Content |
| [ffmpeg-video-editor](https://skills.sh/sundial-org/awesome-openclaw-skills/ffmpeg-video-editor) | 1,208 | Video / Media |
| [jina-reader](https://skills.sh/sundial-org/awesome-openclaw-skills/jina-reader) | 982 | Search & Extraction |
| [remind-me](https://skills.sh/sundial-org/awesome-openclaw-skills/remind-me) | 879 | Productivity |
| [proactive-agent](https://skills.sh/sundial-org/awesome-openclaw-skills/proactive-agent) | 599 | Agent Automation |
| [topic-monitor](https://skills.sh/sundial-org/awesome-openclaw-skills/topic-monitor) | 581 | Monitoring |
| [financial-market-analysis](https://skills.sh/sundial-org/awesome-openclaw-skills/financial-market-analysis) | 524 | Finance |

**Install all sundial-org skills:**
```bash
npx skills add sundial-org/awesome-openclaw-skills
```

### News Summary (1,245 installs)

Automated news aggregation and summarization for Hermes agents. Pulls from configurable sources, summarizes with LLM, and delivers formatted digests.

```bash
npx skills add sundial-org/awesome-openclaw-skills --skill news-summary
```

### FFmpeg Video Editor (1,208 installs)

Video editing via FFmpeg from Hermes agents. Trim, concatenate, resize, add watermarks, transcode — all via skill commands.

```bash
npx skills add sundial-org/awesome-openclaw-skills --skill ffmpeg-video-editor
```

**Why it matters for CorpusIQ:** CorpusIQ generates UGC videos daily. This skill enables Hermes agents to post-process videos (trim, watermark, resize for platform specs) without external tools.

### Jina Reader (982 installs)

Web content extraction via Jina AI's Reader API. Extracts clean markdown from any URL — bypasses paywalls, handles JS-rendered content.

```bash
npx skills add sundial-org/awesome-openclaw-skills --skill jina-reader
```

### Remind-Me (879 installs)

Task and reminder management for Hermes agents. Schedule reminders, set recurring tasks, track deadlines.

```bash
npx skills add sundial-org/awesome-openclaw-skills --skill remind-me
```

### Proactive Agent (599 installs)

Self-triggering agent skill — the agent proactively monitors conditions and takes action without being asked. Useful for monitoring pipelines, cron health, and alert conditions.

```bash
npx skills add sundial-org/awesome-openclaw-skills --skill proactive-agent
```

**Why it matters for CorpusIQ:** CorpusIQ runs 15+ cron-driven agents. A proactive monitoring agent that checks pipeline health and alerts on failures could replace several manual monitoring tasks.

### Topic Monitor (581 installs)

Monitors specified topics across web sources (news, blogs, social) and alerts when new content matches.

```bash
npx skills add sundial-org/awesome-openclaw-skills --skill topic-monitor
```

### Financial Market Analysis (524 installs)

Real-time financial data analysis — stock prices, market trends, portfolio tracking.

```bash
npx skills add sundial-org/awesome-openclaw-skills --skill financial-market-analysis
```

---

## Additional Finds

### OpenClaw Marketing Skills (714 installs)

**Publisher:** [aradotso/marketing-skills](https://skills.sh/aradotso/marketing-skills) | **Installs:** 714

Marketing automation for OpenClaw/Hermes agents — campaign management, audience targeting, content scheduling. From the same publisher behind the hermes-skills ecosystem (50+ Hermes-native skills).

```bash
npx skills add aradotso/marketing-skills --skill openclaw-marketing-skills
```

> See [full setup guide →](/hermes/skills/catalog/openclaw-marketing-skills-setup/)

### OpenClaw Audit Watchdog (665 installs)

**Publisher:** [prompt-security/clawsec](https://skills.sh/prompt-security/clawsec) | **Installs:** 665

Security auditing and monitoring for OpenClaw/Hermes agent deployments. Detects misconfigurations, monitors for suspicious activity, and generates security reports.

```bash
npx skills add prompt-security/clawsec --skill openclaw-audit-watchdog
```

> See [full setup guide →](/hermes/skills/catalog/openclaw-audit-watchdog-setup/)

---

*This page is part of the [Hermes Skills Marketplace](/hermes/skills/marketplace/). See also: [morning sweep](/hermes/skills/marketplace/new-june28-2026/) and [afternoon update](/hermes/skills/marketplace/new-june28-2026-update/).*

*← [Previous Update](/hermes/skills/marketplace/new-june28-2026-update/) | [Marketplace Home](/hermes/skills/marketplace/) →*
