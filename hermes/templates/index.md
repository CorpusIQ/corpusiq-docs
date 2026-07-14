---
title: Templates
description: Ready-to-use templates for Hermes Agent configurations, skills, and deployment patterns. Part of the Hermes Skills Library.
---

# Templates

Ready-to-use templates for Hermes Agent and CorpusIQ setups.

## Available Templates

| Template | Description |
|---|---|
| [Trial Onboarding Email](/hermes/templates/trial-onboarding-email.html) | HTML email template for SaaS trial onboarding flows |
| [Hermes Skill Template](#skill-template) | Standard SKILL.md template with frontmatter, triggers, and pitfalls |
| [Hermes Config Template](#config-template) | Minimal config.yaml template for getting started |
| [Cron Job Template](#cron-template) | Template for scheduling recurring agent tasks |

## Skill Template

Create a `SKILL.md` file with this structure:

```markdown
---
name: your-skill-name
title: Your Skill Title
description: One-line description of what this skill does
triggers:
  - When the user asks about X
  - When working with Y
category: your-category
---

# Your Skill Title

Brief overview of what this skill covers.

## Prerequisites

- Tool or dependency required
- API keys needed

## Steps

1. First step with exact command
2. Second step with verification

## Pitfalls

- Common mistake and how to avoid it
- Another pitfall to watch for

## Verification

How to confirm everything works:

```bash
your-verification-command
```
```

## Config Template

Minimal `config.yaml` for a new Hermes Agent setup:

```yaml
model: sonnet
provider: anthropic

tools:
  - shell
  - web_search
  - web_extract
  - read_file
  - write_file
  - patch

cron:
  enabled: true

memory:
  backend: sqlite
```

## Cron Template

Schedule recurring tasks with `cronjob`:

```bash
# Daily at 9 AM
hermes cron create \\
  --name "daily-report" \\
  --schedule "0 9 * * *" \\
  --prompt "Generate the daily activity report and email it" \\
  --deliver email:reports@example.com \\
  --profile default
```

---

*More templates are added regularly from the Hermes community.*

*← [Hermes Home](/hermes/) | [Scripts](/hermes/scripts/) →*

*↑ [Templates Home](/hermes/templates/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
