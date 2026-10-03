---
title: "Steipete Agent Scripts - Portable Agent Skills & Helpers"
description: "Peter Steinberger's shared agent-skills repo: 54 SKILL.md workflows, sync tooling, and dependency-light helpers for Codex/Claude workspaces. 9.5K installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/steipete-agent-scripts-setup/"
robots: "index,follow"
last_updated: "2026-10-02"
tags: ["hermes skill", "agent skill", "skill setup", "codex", "claude", "developer tools", "macos", "swiftui"]
---

# Steipete Agent Scripts - Setup Guide

**Source:** [steipete/agent-scripts](https://github.com/steipete/agent-scripts) (7,198⭐, MIT)
**Skill family:** `steipete/agent-scripts` (54 SKILL.md files in-repo; 61 indexed listings)
**Combined Installs:** ~9,472 across indexed listings (Oct 2, 2026 snapshot)
**Category:** Developer Tooling / macOS / Media Utilities
**Quality Tier:** 🟢 Production-ready source (well-starred, MIT, active maintenance, per-skill front matter and validation tooling)

Peter Steinberger's `agent-scripts` repo is the canonical home for shared agent instructions, skills, and portable helpers he uses across local workspaces. Beyond skills it ships the sync/validation infrastructure other repos borrow: `scripts/sync-skills` (idempotent global discovery across Codex/Claude), `scripts/validate-skills`, and a `hooks/` guardrail layer. The skill roster leans toward macOS/Swift development utilities, media conversion, and GitHub workflow automation.

---

## Installation

Skills are plain `skills/<name>/SKILL.md` entries. Install the collection via the skills.sh installer, or clone and symlink:

```bash
git clone https://github.com/steipete/agent-scripts ~/Projects/agent-scripts

# Idempotent global discovery (run after cloning or adding skills)
~/Projects/agent-scripts/scripts/sync-skills

# Validate all skills
~/Projects/agent-scripts/scripts/validate-skills
```

Discovery rules enforced by `sync-skills`:
- **Codex** scans nested dirs → gets whole-root links.
- **Claude Code** loads only `~/.claude/skills/<name>/SKILL.md` (one level deep; category subfolders are NOT scanned) → gets a flat per-skill link mirror.
- Name collisions resolve `agent-scripts > manager > codex-local`; the script prints skipped duplicates and prunes broken/stale managed links.

## Roster - Top Indexed Skills

| Skill | Installs | What It Does |
|---|---|---|
| video-transcript-downloader | 1,012 | Download and transcribe video sources |
| brave-search | 855 | Brave Search API integration |
| skill-cleaner | 544 | Audit and clean skill directories |
| create-cli | 347 | Scaffold CLI tools |
| markdown-converter | 342 | Convert documents to/from Markdown |
| 1password | 313 | 1Password CLI integration |
| nano-banana-pro | 289 | Image generation workflow |
| codex-first | 269 | Route work to Codex first |
| swiftui-liquid-glass | 262 | SwiftUI Liquid Glass UI work |
| openai-image-gen | 243 | OpenAI image generation |
| native-app-performance | 236 | Native app performance work |
| instruments-profiling | 222 | Instruments profiling on macOS |
| frontend-design | 204 | Frontend design guidance |
| domain-dns-ops | 188 | Domain / DNS operations |
| oracle | 172 | Oracle DB workflows |
| swift-concurrency-expert | 164 | Swift concurrency patterns |
| browser-use | 117 | Browser automation |
| openclaw-relay | 113 | OpenClaw relay integration |
| xurl | 104 | X/Twitter via xurl CLI |
| mac-maintenance | 102 | macOS maintenance routines |

*…plus 41 more indexed skills in the 2–101 install range (github deep-review, cloudflare-registrar, whatsapp, ssh-doctor, wrangler, twilio-sms, reminders, fleet-maintenance, and others).*

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Skill-library hygiene | `skill-cleaner` + the repo's `validate-skills`/`sync-skills` pattern for managing a growing skill library |
| Research & media | `video-transcript-downloader` + `markdown-converter` + `brave-search` for research pipelines |
| Social ops | `xurl` for X posting/search, `release-tweets` for release announcements |
| macOS fleet | `ssh-doctor`, `remote-mac`, `mac-maintenance` for managing the Mac Mini worker |

## Limitations / Verification

- skills.sh indexing verified Oct 2, 2026: 61 indexed listings; 54 SKILL.md files verified via the GitHub trees API on branch `main`.
- Some skills are macOS/Apple-platform specific (`swiftui-*`, `instruments-profiling`, `native-app-performance`, `xcode-sync`) — not portable to Linux agents.
- Several skills mirror third-party CLIs (`1password`/`one-password` appear as duplicates; `xurl`, `wrangler`, `twilio-sms` are wrappers) — the repo is a routing layer, not the upstream tool.
- No live install test performed; install counts are from the Oct 2, 2026 sweep snapshot.
