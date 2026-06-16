---
title: New Skills — June 16, 2026 — Native Hermes Media Skill
description: Skills.sh sweep discovered youtube-content (160 installs) — a native Hermes Agent skill for YouTube transcript extraction and content transformation. Previously undocumented in the skills catalog.
---

# June 16, 2026 — Skills Discovery

**Sweep:** REST API queries against skills.sh (`q=hermes`, `q=nousresearch/hermes-agent`, `q=aradotso/hermes-skills`) + GitHub repo search for new hermes-skills repos.

## New Skills Documented

| Skill | Source | Installs | Status |
|---|---|---|---|
| [youtube-content](/hermes/skills/catalog/youtube-content-setup/) | nousresearch/hermes-agent | 160 | **New setup guide created** |

## Already Catalogued (Cross-Reference Verified)

All other 50 results from `q=hermes`, all 43 from `q=nousresearch/hermes-agent`, and all 50 from `q=aradotso/hermes-skills` were already documented in:
- `hermes/skills/catalog/index.md` (native + marketplace catalog)
- `hermes/skills/development/index.md` (GitHub workflow skills)
- Individual setup guides in `hermes/skills/catalog/`

### Notable: 6 Native GitHub Skills Confirmed

The nousresearch query surfaced 6 GitHub workflow skills (138-144 installs each) that are native Hermes built-ins:
- `github-auth`, `github-issues`, `github-pr-workflow`, `github-code-review`, `github-repo-management`, `codebase-inspection`

These are already documented in `hermes/skills/development/index.md` under native skills.

## GitHub Repo Discovery

New hermes-skills repos created June 14-16, 2026:

| Repo | Stars | Created | Notes |
|---|---|---|---|
| [cobibean/soul-grader-skill](https://github.com/cobibean/soul-grader-skill) | 28⭐ | Jun 14 | Already catalogued (`soul-grader-setup.md`) |
| [zapprosite/hermes-community-skills](https://github.com/zapprosite/hermes-community-skills) | 1⭐ | Jun 16 | Claims 25+ skills — monitor for growth |
| [zapprosite/hermes-skills-pack](https://github.com/zapprosite/hermes-skills-pack) | 1⭐ | Jun 16 | Refrimix + social-media + business skills |
| [Ow1onp/hermes-agent-skills](https://github.com/Ow1onp/hermes-agent-skills) | 1⭐ | Jun 14 | Production-grade skills, self-evolving |
| [PeterCha90/link-bookmark](https://github.com/PeterCha90/link-bookmark) | 2⭐ | Jun 16 | Unread link bookmarks from chat |

**Verdict:** All low-star (<30) except soul-grader (already catalogued). No new high-value skills.sh entries from these repos yet. Monitor zapprosite repos — if they publish to skills.sh and gain installs, re-evaluate.

## What Changed

- **New setup guide:** `hermes/skills/catalog/youtube-content-setup.md` — 7-section guide with CLI reference, CorpusIQ use cases, troubleshooting
- **No catalog index changes needed** — `youtube-content` is a native skill, catalogued under media tools

---

*← [June 13, 2026 — Update 3](/hermes/skills/marketplace/new-june13-2026-update3/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Powered by CorpusIQ*
