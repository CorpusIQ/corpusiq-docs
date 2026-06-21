---
title: Scope-First Skill — Setup Guide
description: Interactive planning discipline for Hermes agents — use the clarify tool to scope builds one decision at a time before delegating or writing code
---

# Scope-First: Interactive Planning for Hermes Agents

**Skill:** `scope-first` | **Author:** MahdiHedhli | **Version:** 1.2.0
**Repo:** [MahdiHedhli/skills](https://github.com/MahdiHedhli/skills)

---

## 1. What It Does

Scope-first is a **plan-first discipline** that intercepts build/feature requests. Before writing a single line of code or delegating to a subagent, it scopes the task **interactively** using Hermes' `clarify` tool — one decision at a time, with button choices.

The core insight: a wall of questions the user can't act on is the failure mode. `clarify` renders each question as a blocking, button-based prompt. Users click, don't type.

---

## 2. Prerequisites

- Hermes Agent v0.14.0+ (for `clarify` tool support)
- The `clarify` tool must be enabled in your toolset
- Linux, macOS, or Windows

---

## 3. Installation

```bash
# Clone the repo
git clone https://github.com/MahdiHedhli/skills.git /tmp/mahdihedhli-skills

# Copy only the scope-first skill
cp -r /tmp/mahdihedhli-skills/skills/scope-first ~/.hermes/skills/

# Reload Hermes skills
hermes skills reload

# Verify
hermes skills list | grep scope-first
```

Optionally install neckbeard (companion minimalism skill):

```bash
cp -r /tmp/mahdihedhli-skills/skills/neckbeard ~/.hermes/skills/
hermes skills reload
```

---

## 4. How It Works

### Trigger

Activates when the user says: **"build," "implement," "create," "add," "scaffold," "set up"** — any request that will write files or spawn a worker.

Does NOT activate for: questions, read-only investigation, or requests the user already scoped precisely.

### The Clarify Pattern

The skill uses `clarify()` for every decision, one at a time:

```python
clarify(
    question="Where should this live?",
    choices=["~/projects/html5-chess", "./html5-chess", "the current directory"]
)
```

Each decision gets a blocking prompt with clickable buttons. The user picks one, or types a custom answer via the auto-appended "Other" row.

### Decisions Worth Clarifying (in order)

1. **Target directory** — propose a concrete path before any file is written
2. **Approach/stack** — framework, language, library choices with trade-offs
3. **V1 scope** — what's in vs. out for the first iteration

Stop as soon as you know enough to build. For low-stakes details (file names, minor config), pick a sensible default and state it.

### Bypass

The user can skip the planning gate with explicit bypass phrases:
- "yolo"
- "skip planning"
- "just build it"
- "don't plan, just code"

---

## 5. CLI Reference

Scope-first is a skill, not a CLI. It integrates into Hermes' skill system and activates automatically when the trigger conditions match.

```bash
# Check if installed
hermes skills list | grep scope-first

# View skill details
hermes skills info scope-first

# Disable temporarily
hermes skills disable scope-first

# Re-enable
hermes skills enable scope-first
```

---

## 6. CorpusIQ Use Cases

| Use Case | How Scope-First Helps |
|----------|----------------------|
| **Feature development** | Prevents scope creep — user picks v1 scope explicitly before build starts |
| **Subagent delegation** | Ensures workers get scoped tasks with concrete target directories |
| **Multi-profile setups** | Confirms which Hermes profile/directory receives new files |
| **Client-facing builds** | Interactive scoping creates an audit trail of decisions |
| **New tool integration** | Clarifies install location, dependencies, and integration approach |

---

## 7. Troubleshooting

### "clarify tool not found"

The `clarify` tool must be enabled in your Hermes toolset. Check:

```bash
hermes config get toolsets
```

Ensure `clarify` appears in the enabled list. Add it if missing:

```bash
hermes config set toolsets '["terminal", "file", "web", "clarify", ...]'
```

### "scope-first not triggering"

The skill uses Hermes' trigger system. Verify the trigger keywords match your request pattern:

- Triggers: build, implement, create, add, scaffold, set up
- Non-triggers: what is, how do I, explain, find, search

### "Too many clarify prompts"

If scope-first asks too many questions, the request may genuinely be under-specified. Provide more detail upfront: "build me a Next.js dashboard in `~/projects/dash` with a dark theme and 3 charts" — the skill will detect this is already scoped and skip most prompts.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace →](/hermes/skills/marketplace/)*
*Powered by CorpusIQ — June 20, 2026*
