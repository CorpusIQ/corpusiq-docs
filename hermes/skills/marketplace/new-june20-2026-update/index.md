---
title: New Hermes Skills — June 20, 2026 Update
description: 4 newly discovered Hermes Agent skill repos — scope-first interactive planning, neckbeard minimalism, skill safety audit, YouTube audio converter, and grill requirements interrogation
---

# New Skills: June 20, 2026 (Update)

**Discovered:** June 20, 2026 (evening sweep) via GitHub API search (`hermes+skill+created:>2026-06-18`)
**New repos:** 4 | **New skills/tools:** 5

---

## Category 1: Operational Discipline Skills (2 repos)

### MahdiHedhli/skills — scope-first + neckbeard (0⭐)

**Two operational discipline skills** that enforce planning-first and minimalism-first code generation.

| Skill | Description |
|-------|-------------|
| **scope-first** | Interactive planning via `clarify` tool — asks one decision at a time (target directory, approach, v1 scope) with button choices before delegating builds. Bypassed only with "yolo" / "skip planning" |
| **neckbeard** | Minimalism ladder for code generation: YAGNI → stdlib → platform → installed dep → one line → minimum that works. Never prunes security/observability/audit-logging. Vendored from Ponytail (MIT) |

**Scope-first workflow:**
```
User: "build me a dashboard"
Agent: clarify("Where should this live?", ["~/projects/dashboard", "./dashboard", "current dir"])
Agent: clarify("What framework?", ["Next.js", "Plain HTML/JS", "Flask"])
Agent: [builds exactly what was scoped]
```

**Repo:** [MahdiHedhli/skills](https://github.com/MahdiHedhli/skills) | **Stars:** 0 | **Created:** June 20, 2026
**Install:** `git clone` → copy `skills/scope-first/` + `skills/neckbeard/` to `~/.hermes/skills/`
**Setup Guide:** [scope-first-setup](/hermes/skills/catalog/scope-first-setup/)

---

### SoCalStreet/hermes-grill-skill — grill (0⭐)

**Requirements interrogation skill** — before building anything, grills the user with sharp, specific questions to prevent misalignment. Borrowed from Matt Pocock's grill concept: nobody knows exactly what they want, so interrogate first, build once.

| Feature | Details |
|---------|---------|
| Trigger | User says "build", "create", "implement", "fix", "I want to…" |
| Approach | Sharp questions, not clarify buttons — more conversational |
| Scope | Non-trivial builds only; skips simple lookups and unambiguous edits |
| Goal | Prevent the #1 cause of agent rework: misalignment |

**Repo:** [SoCalStreet/hermes-grill-skill](https://github.com/SoCalStreet/hermes-grill-skill) | **Stars:** 0 | **Created:** June 20, 2026
**Install:** `git clone` → copy `SKILL.md` to `~/.hermes/skills/hermes-grill/`

---

## Category 2: Developer Tooling (1 repo)

### fxsc2011/skill-audit — Skill Safety Audit (0⭐)

**Skill security auditor** — scans SKILL.md and `scripts/` for malicious code, dangerous commands, suspicious imports, and file-boundary violations. Chinese-language (中文), but the Python scripts work universally.

| Feature | Details |
|---------|---------|
| Single audit | `python3 audit.py ~/.hermes/skills/<category>/<skill>/` |
| Full audit | Batch scan all installed skills |
| JSON output | `--json` flag for programmatic processing |
| Batch fix | `batch-fix-frontmatter.py` — auto-fills missing `trigger` fields |
| Checks | Malicious code, dangerous shell commands, suspicious Python imports, file path boundaries |

**Repo:** [fxsc2011/skill-audit](https://github.com/fxsc2011/skill-audit) | **Stars:** 0 | **Created:** June 20, 2026
**Install:** `git clone` → copy to `~/.hermes/skills/devops/skill-audit/`
**Note:** Chinese-language documentation but Python scripts work with any locale

---

## Category 3: Media Tools (1 repo)

### ksdok/hermes-skills — youtube-audio-converter (0⭐)

**YouTube audio extraction skill** — wraps `youtube-to-mp3` CLI (yt-dlp + ffmpeg) for downloading audio from YouTube videos, playlists, or URL files.

| Feature | Details |
|---------|---------|
| Formats | MP3, M4A, WAV, FLAC, Opus, AAC, Vorbis, ALAC |
| Batch | URL file support for bulk conversion |
| Dry run | Preview before downloading |
| Dedup | Skips already-processed videos |
| Requires | `youtube-to-mp3` CLI (`yt-dlp` + `ffmpeg`) |

**Repo:** [ksdok/hermes-skills](https://github.com/ksdok/hermes-skills) | **Stars:** 0 | **Created:** June 19, 2026
**Install:** `git clone` → copy `youtube-audio-converter/` to `~/.hermes/skills/`

---

## Also Discovered (lower value)

| Repo | Description | Why skipped |
|------|-------------|-------------|
| Modichen/Hermesagent | Skill list | Previously catalogued |
| darraappen2/herman-skill-playbook | 8 execution skills by Herman | Previously catalogued |
| wilmerarredondozavala-jpg/odysseus-skills | Skills export for Odysseus IA | Previously catalogued |
| qq250113397-dotcom/skill-shell | Chinese skill manager for Codex/Claude Code/Hermes | Previously catalogued |
| tensakulabs/hermes-ponytail | Ponytail lazy-senior-dev skills | Previously catalogued |

---

## Stats

- **Total new repos catalogued:** 4
- **New skills/tools:** 5 (scope-first, neckbeard, grill, skill-audit, youtube-audio-converter)
- **Setup guides drafted:** 1 (scope-first)
- **Hermes-native:** 4 repos

---

*← [Marketplace Home](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Powered by CorpusIQ — June 20, 2026*
