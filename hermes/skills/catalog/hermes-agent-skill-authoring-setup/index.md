---
title: Hermes Agent Skill Authoring — Official Guide for Writing SKILL.md
description: Official Nous Research guide for writing high-quality SKILL.md files for the Hermes Agent ecosystem. Templates, best practices, validation, and publishing workflow. 230+ installs.
---

# Hermes Agent Skill Authoring — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/NousResearch/hermes-agent) (Official)
**Skill:** `hermes-agent-skill-authoring` · **Installs:** 230+ · **Category:** Development / Skill Creation
**Platform:** Linux, macOS, Windows

The official guide for writing SKILL.md files for the Hermes Agent ecosystem. Learn the metadata format, content structure conventions, best practices for skill quality, validation tools, and the publishing workflow to get your skill listed on skills.sh.

---

## Installation

```bash
# Install via skills.sh
npx skills add nousresearch/hermes-agent --skill hermes-agent-skill-authoring -g -y
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ |
| **Text Editor** | Any — VS Code recommended for YAML frontmatter validation |
| **GitHub Account** | For publishing to skills.sh marketplace |

---

## SKILL.md Format

Every skill is a single `SKILL.md` file with YAML frontmatter and Markdown body:

```yaml
---
name: my-skill-name
description: "Clear, concise description of what the skill does."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [category, keywords]
    related_skills: [other-skill-name]
---

# Skill Title

## Overview
What the skill does and when to use it.

## Prerequisites
What's needed before using this skill.

## Workflow
Step-by-step instructions.

## Pitfalls
Common issues and how to avoid them.

## Verification
How to confirm the skill worked correctly.
```

---

## Frontmatter Fields

| Field | Required | Description |
|-------|:--------:|-------------|
| `name` | ✅ | Lowercase, hyphens only, max 64 chars. Must match directory name. |
| `description` | ✅ | 1-2 sentences. Appears in skills list and marketplace search. |
| `version` | ✅ | SemVer. Bump when changing workflow significantly. |
| `platforms` | — | Array: `linux`, `macos`, `windows`. Omit if cross-platform. |
| `metadata.hermes.tags` | — | Keywords for skill search. |
| `metadata.hermes.related_skills` | — | Skill names this skill works with or extends. |

---

## Content Structure Best Practices

### 1. Overview Section

Answer three questions in the first paragraph:
- **What** does it do?
- **When** should an agent load it?
- **Why** use this instead of general knowledge?

### 2. Prerequisites Section

Be specific. Don't say "need API access" — say "OpenAI API key with `gpt-4` model access, set as `OPENAI_API_KEY` environment variable."

### 3. Workflow Section

Numbered steps with exact commands. Every command should be copy-paste runnable:

```bash
# Good — exact, runnable
python3 scripts/validate.py --input config.yaml

# Bad — vague
validate the configuration file
```

### 4. Pitfalls Section

Document what WILL go wrong and how to fix it:

```
PITFALL: The API returns 401 if the token was generated more than 24 hours ago.
SOLUTION: Regenerate the token and update the environment variable.
```

### 5. Verification Section

How to confirm the skill worked:

```bash
# Check output file exists and is non-empty
test -s output/report.md && echo "PASS" || echo "FAIL"
```

---

## Skill Quality Checklist

Before publishing, verify:

- [ ] YAML frontmatter is valid (no syntax errors)
- [ ] `name` matches the directory name
- [ ] Description is under 200 characters
- [ ] All commands are copy-paste runnable
- [ ] Prerequisites list every dependency
- [ ] Workflow has numbered steps
- [ ] Pitfalls section covers at least 2 common issues
- [ ] Verification section has at least 1 test
- [ ] No hardcoded secrets (use environment variables)
- [ ] Platforms list is accurate

---

## Publishing to skills.sh

1. Create a public GitHub repo with your `SKILL.md`
2. Tag the repo with `hermes-agent` topic on GitHub
3. skills.sh auto-discovers repos with agent-skill topics
4. Your skill appears on the marketplace within 24 hours

```bash
# Example: publishing a skill
git init my-hermes-skill
cd my-hermes-skill
# Create SKILL.md with proper frontmatter
git add SKILL.md
git commit -m "Initial skill: my-hermes-skill"
gh repo create my-hermes-skill --public --push
gh repo edit --add-topic hermes-agent
```

---

## Skill Directory Structure

```
my-skill/
├── SKILL.md              # Required — the skill definition
├── references/           # Optional — detailed reference docs
│   └── api.md
├── templates/            # Optional — output templates
│   └── report.md
├── scripts/              # Optional — helper scripts
│   └── validate.py
└── assets/               # Optional — images, configs
    └── logo.png
```

---

## Related Skills

- [Hermes Agent Core](/hermes/skills/catalog/hermes-agent-setup/) — Official core skill
- [Skill Creator](/hermes/skills/catalog/skill-creator-setup/) — Community skill creation workflow
- [Skill Repo Manager](/hermes/skills/catalog/skill-repo-manager-setup/) — Managing multi-skill repos
