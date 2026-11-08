---
title: "Templates - CorpusIQ Docs"
description: Ready-to-use templates for Hermes Agent configurations, skills, and deployment patterns. Part of the Hermes Skills Library.
canonical: "https://www.corpusiq.io/docs/hermes/templates/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes template", "agent template", "skill template"]

---

# Templates

Ready-to-use templates for Hermes Agent and CorpusIQ setups.

## Available Templates

| Template | Description |
|---|---|
| [Trial Onboarding Email](https://github.com/CorpusIQ/corpusiq-docs/blob/main/hermes/templates/trial-onboarding-email.html) | HTML email template for SaaS trial onboarding flows |
| [Hermes Skill Template](#skill-template) | Standard SKILL.md template with frontmatter, triggers, and pitfalls |
| [Hermes Config Template](#config-template) | Minimal config.yaml template for getting started |
| [Cron Job Template](#cron-template) | Template for scheduling recurring agent tasks |

## Skill Template

Create a `SKILL.md` file with this structure:

```markdown
---
name: your-skill-name
description: Use when X happens. One line, 60 characters or fewer.
version: 1.0.0
platforms: [macos, linux]

metadata:
  hermes:
    tags: [your-tag, another-tag]
    category: your-category
---

# Your Skill Title

Brief overview of what this skill covers.

## When to Use

- When the user asks about X
- When working with Y

## Procedure

1. First step with exact command
2. Second step with verification

## Pitfalls

- Common mistake and how to avoid it
- Another pitfall to watch for

## Verification

- Command that proves the step worked
```

## Verification

How to confirm everything works:

```bash
your-verification-command
```

## Config Template

Minimal `config.yaml` for a new Hermes Agent setup:

```yaml
model:
  default: anthropic/claude-sonnet-5.5
  provider: openrouter

platform_toolsets:
  cli: [hermes-cli]

memory:
  memory_enabled: true
  user_profile_enabled: true
```

`platform_toolsets` picks the tool surface per platform: a preset like `hermes-cli`, or your own list of toolsets (`cli: [web, terminal, file, skills, todo]`). `hermes tools enable` and `hermes tools disable` write this key for you.

## Cron Template

Schedule recurring tasks with `hermes cron create`. The schedule and the prompt are positional arguments, not flags:

```bash
# Daily at 9 AM
hermes cron create "0 9 * * *" \
  "Generate the daily activity report and email it" \
  --name "daily-report" \
  --deliver local
```

`--deliver` accepts `origin`, `local`, `telegram`, `discord`, `signal`, `platform:chat_id`, `bot-chat[:profile]`, or `room:<room_id>[@profile]`. To run the job under a different profile, set the profile for that invocation with `HERMES_PROFILE=default hermes cron create ...`, or change the sticky default with `hermes profile use default`. Add `--skill <name>` (repeatable) to attach skills, or `--script <file> --no-agent` for a script-only job that never wakes the model.

---

*More templates are added regularly from the Hermes community.*

*← [Hermes Home](/hermes) | [Scripts](/hermes/scripts) →*

*↑ [Templates Home](/hermes/templates)*

---

*Curated by CorpusIQ - one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
