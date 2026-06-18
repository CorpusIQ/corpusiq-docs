---
title: Hermes Skills
description: 380+ skills for Hermes agents — 90 native CorpusIQ skills, 290+ marketplace skills from skills.sh. Reusable, executable agent capabilities.
---

# Hermes Skills

**See the [Skills Catalog](/hermes/skills/catalog/) for the complete index of all 380+ skills.**

Skills are reusable agent capabilities — step-by-step workflows with tools, triggers, and verification criteria. They are not static prompts, not text files — they are executable runbooks that Hermes agents read and execute. A skill tells the agent exactly what to do, what tools to use, how to verify each step, and what to do when something goes wrong.

## How Skills Work

Every skill follows a consistent structure:

1. **Trigger** — When the skill activates (keyword match, cron schedule, agent profile, or explicit invocation)
2. **Tool Manifest** — Which tools the skill requires (MCP connectors, terminal access, browser, web extraction)
3. **Execution Steps** — Numbered instructions the agent follows sequentially
4. **Verification Gates** — After each major step, what to check before proceeding
5. **Error Recovery** — What to do when a step fails (retry, escalate, skip, or abort)

A skill loads into the agent's context at runtime. The agent doesn't "remember" the skill from previous sessions — it reads the skill body fresh every time, which means skills can evolve without retraining or redeployment. If a skill has a bug, you fix the skill file and the next invocation picks up the fix immediately.

## Categories

Skills are organized into functional categories that reflect how teams use Hermes in production:

| Category | Count | What It Covers |
|----------|:-----:|----------------|
| **Growth & Engagement** | 13 | Community engagement, social automation, content rotation, go-to-market |
| **Marketing** | 45+ | SEO, CRO, copywriting, ads, content strategy, competitive analysis, cold outreach |
| **Development** | 10 | GitHub workflows, code review, PR management, CI/CD, codebase inspection |
| **Engineering** | 8 | MCP architecture, connector audits, API development, frontend, scheduled jobs |
| **Operations** | 20+ | Email automation, cron management, system audits, lead capture, monitoring |
| **Research & Intelligence** | 6 | Prospect research, competitive analysis, market intelligence |
| **Lead Response & Nurture** | 11 | Inbound classification, response personalization, nurture sequences |
| **Video Production** | 6 | AI avatar video, UGC series, voiceover, multi-platform posting |
| **Agent Infrastructure** | 35+ | Browser automation, orchestration, RAG, Docker, K8s, monitoring |

See the [Skills Catalog](/hermes/skills/catalog/) for the full categorized index.

## Installing Skills

### Native Skills (Auto-Loaded)

Native CorpusIQ skills load automatically when the agent profile matches their trigger conditions. No installation required — if you have a CorpusIQ profile, the skills are already available.

To view loaded skills in your current profile:

```bash
hermes skills list --native
```

### Marketplace Skills (From skills.sh)

Install community skills from [skills.sh](https://skills.sh) using the Hermes CLI:

```bash
# Install a single skill
npx skills add coreyhaines31/marketingskills@seo-audit

# Install a full skill pack (all skills from a repo)
npx skills add coreyhaines31/marketingskills

# Install a Hermes agent variant
npx skills add nousresearch/hermes-agent@dogfood

# List all installed marketplace skills
hermes skills list --marketplace

# Remove a skill
hermes skills remove seo-audit
```

### Verifying Installation

After installing, verify the skill loaded correctly:

```bash
# Check skill metadata
hermes skills inspect seo-audit

# Test the skill with a dry run
hermes skills test seo-audit --dry-run
```

If a skill fails to load, check the Hermes logs for missing dependency errors. Most marketplace skills require specific tools — for example, `seo-audit` requires web extraction (`web_extract`) and terminal access. Install any missing tools before retrying.

## Creating Custom Skills

You can create your own skills for any repeatable workflow. The fastest path is to let Hermes generate the skill from a working session:

```bash
# After completing a task manually, tell Hermes to create a skill from it
"Create a skill from the last task I just did — audit our email automations"

# Hermes will write the skill file and offer to install it
```

To author a skill manually, create a markdown file with this structure:

```markdown
---
trigger_keywords: ["email audit", "automation check"]
required_tools: ["email_connector", "terminal"]
---

# Email Automation Audit

## Step 1: List all active automations
Use email_connector to fetch automation list. Verify count > 0.

## Step 2: Check delivery status
For each automation, verify last run timestamp. Flag any > 24h stale.

## Step 3: Generate report
Output markdown table: automation name, last run, status, issues found.

## Verification
- All automations accounted for
- No stale runs > 24h
- Report includes actionable recommendations
```

Install your custom skill:

```bash
hermes skills install ./my-skills/email-audit.md
```

The skill is now available for any Hermes session in your profile. Invoke it by mentioning the trigger keywords or calling it explicitly:

```
"Run the email automation audit"
```

## Marketplace Discovery

The Hermes community hub includes a curated [Skills Marketplace](/hermes/skills/marketplace/) with 290+ community-contributed skills. New skills are discovered through automated sweeps of skills.sh and added weekly. Browse by category, check install counts to see what's trending, and submit your own skills for inclusion.

### Trending This Week

[🆕 June 16, 2026 — ClawPilot ecosystem: mobile-to-agent bridge →](/hermes/skills/marketplace/new-june16-2026/)

### Recent Discoveries

- [June 15, 2026 — Nous Research Expansion (23 skills)](/hermes/skills/marketplace/new-june15-2026/)
- [June 12, 2026 — OpenClaw Security Suite (13 skills)](/hermes/skills/marketplace/new-june12-2026-update/)
- [June 11, 2026 — Hermes Ecosystem + Platform Bots (38 skills)](/hermes/skills/marketplace/new-june11-2026/)

## Quick Links

| Page | Content |
|------|---------|
| **[Skills Catalog](/hermes/skills/catalog/)** | Every skill, categorized, counts, single source of truth |
| **[Marketplace](/hermes/skills/marketplace/)** | 290+ curated skills with install counts and categories |
| **[Development](/hermes/skills/development/)** | GitHub, code review, issues, CI/CD, testing, PR lifecycle |
| **[Marketing](/hermes/skills/marketing/)** | SEO, CRO, ads, content strategy, cold outreach, community |
| **[Engineering](/hermes/skills/engineering/)** | MCP architecture, connector audits, API dev, frontend, cron |
| **[Operations](/hermes/skills/operations/)** | Email, cron, audit, lead capture, monitoring, governance |
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
