---
title: skill-creator — Anthropic's Skill Creation Framework for Hermes
description: Install and use anthropics/skills@skill-creator (317K installs) to author production-quality Hermes agent skills. Workflow scoping, YAML frontmatter, error handling patterns, verification gates, and marketplace publishing.
---

# skill-creator — Setup Guide

**Source:** [anthropics/skills](https://github.com/anthropics/skills) (317,700 installs)
**Category:** Skill Development
**Languages:** Python

Anthropic's official skill creation framework. Guides agents through the complete skill authoring lifecycle: scoping the workflow, writing SKILL.md with correct YAML frontmatter, testing with dry runs, handling error paths, and publishing to marketplaces. The same framework used internally by Anthropic for their 60+ published skills.

---

## Installation

```bash
npx skills add anthropics/skills@skill-creator
```

Verify:
```bash
npx skills list | grep skill-creator
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version |
| **Text editor** | Any — skill files are Markdown |
| **Git** | For version control and publishing |
| **GitHub account** | For publishing to skills.sh marketplace |

---

## Skill Creation Workflow

The framework guides agents through 7 stages:

### Stage 1: Scope the Workflow

```bash
skill-creator scope "Automatically check all social media platforms for new comments and reply helpfully"
```

The scoping phase identifies:
- **Inputs:** What triggers the skill, what data it receives
- **Outputs:** What the skill produces, success criteria
- **Tools needed:** MCP connectors, terminal access, browser, APIs
- **Error surface:** What can fail, how to handle each failure
- **Granularity check:** Is this one skill or should it be split?

### Stage 2: Generate SKILL.md Skeleton

```bash
skill-creator generate --name "social-comment-monitor" --category "social-media"
```

Generates a complete SKILL.md template with all required sections:
```markdown
---
name: social-comment-monitor
description: Monitor and respond to social media comments across platforms
trigger: When checking for new social media engagement
category: social-media
---

# Social Comment Monitor

## Prerequisites
...

## Execution Steps
1. ...
2. ...

## Verification Gates
...

## Error Recovery
...
```

### Stage 3: Define Tool Manifest

The tool manifest declares every tool, API, and connector the skill requires:

```yaml
# In SKILL.md frontmatter
tools:
  - name: terminal
    required: true
  - name: web_extract
    required: false
    fallback: curl
  - name: xurl
    required: true
    version: ">=2.0"
```

### Stage 4: Write Error Recovery Patterns

The framework includes a pattern library for common failures:

| Failure Type | Pattern | Example |
|---|---|---|
| **Timeout** | Exponential backoff, max 3 retries | API call >30s |
| **Rate limit (429)** | Wait for `Retry-After` header, then retry once | Instagram feedback_required |
| **Auth expired (401)** | Refresh token, retry once; if still fails, escalate | Gmail OAuth |
| **Missing data** | Continue with partial results, flag gaps | API returns empty array |
| **Network error** | Retry 3x with 2s delay, then skip and report | Connection reset |

### Stage 5: Add Verification Gates

Every major step gets a verification gate:

```markdown
## Verification Gates

### After Step 2: Platform Connection
- [ ] xurl whoami returns valid user ID
- [ ] Instagram session loads without LoginRequired
- [ ] Postiz posts:list returns non-empty response

### After Step 4: Comment Collection
- [ ] Comment count > 0 for at least one platform
- [ ] No platform returned error on all comment calls
- [ ] Spam filter processed all comments
```

### Stage 6: Dry Run Testing

```bash
skill-creator test social-comment-monitor --dry-run
```

The dry run:
1. Validates YAML frontmatter
2. Checks all declared tools are available
3. Simulates execution with mock tool responses
4. Verifies error paths are handled
5. Reports missing verification gates

### Stage 7: Publish to Marketplace

```bash
skill-creator publish social-comment-monitor --marketplace skills.sh
```

Publishing handles:
- Git tag and version bump
- Marketplace metadata formatting
- GitHub release creation
- skills.sh registry submission

---

## Hermes/CorpusIQ Relevance

**Quality Standardization:** Replaces ad-hoc skill authoring with a structured framework. Every CorpusIQ skill now follows the same 7-stage creation process, ensuring consistency across 133+ skills.

**Error Handling:** The pattern library alone prevents the "skill breaks silently in production" failures. Instead of discovering error paths through production incidents, skills are tested against every failure type before deployment.

**Autonomous Skill Creation:** Hermes agents can create new skills autonomously — scope the workflow, generate the skeleton, write error handling, run dry tests, and publish — all without human intervention. The verification gates ensure quality.

**Integration with find-skills:** After publishing, use `find-skills` to verify the skill appears correctly in marketplaces and track install counts.

---

## See Also

- [find-skills](/hermes/skills/catalog/find-skills-setup/) — Skill discovery tool
- [Creating Custom Skills](/hermes/skills/creating-skills/) — Hermes-native skill authoring
- [Skills Catalog](/hermes/skills/catalog/) — Browse all documented skills
