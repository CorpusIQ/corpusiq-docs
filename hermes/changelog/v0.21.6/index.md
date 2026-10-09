---
title: Hermes Agent v0.21.6 Patch Release
description: Hermes Agent v0.21.6 patch release - 2,106 PRs, first cut from the new stable pipeline, plus auth and sender hardening.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.21.6/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes agent", "ai agent", "nous research"]
---

# Hermes Agent v0.21.6

**Release Date:** October 8, 2026
**Since v0.21.5:** 8,867 non-merge commits · 8,342 changed files (+772,490 / -225,600) · 2,106 merged PRs · 3,027 closed issues

> Patch release. This tag rolls up the ~2,100 PRs merged since v0.21.5 into a stable tagged release for Docker and Hermes Cloud. Full curated notes for this window ship with v0.22.0.

---

## Highlights

- **First release cut by the new stable release pipeline** - one attempt ref, a tested Docker image, and a receipt tag at publish
- **Ships the tag, the GitHub release, and the Docker image.** The desktop app, Termux packages, and the Microsoft Store stay on their current build and move with the next bundled release
- **Also in this window, documented in full with v0.22.0:** live transcription while you speak on CLI/TUI/Desktop (`stt.streaming`); spoken voice turns routed to their own model (`auxiliary.voice_chat`); third-party plugins in a per-profile plugin host (`plugins.isolation: host`); favorite and pinned models in the Desktop picker with a usage chip before a subscription hits its wall; local models in `hermes model` plus llama.cpp CUDA on Linux x64 and arm64; layered language packs; summary-first `hermes status` (`--short`, `--full`); a review-pane diff scope selector and keep-awake that follows the turn; cron/`doctor`/home-channel warnings when the cron store goes unwritable; a Discord setup that checks the bot token and prints the invite link; GPT-6.1 Sol and Claude Sonnet 5.5 / Haiku 5.5 in the catalogs; and dozens of new community plugins

---

## Security Fixes

**Dashboard authentication hardening**

- Spoofed `X-Forwarded-For` headers could reset the password-login rate limit and get around the per-IP cap on native sign-in (#133367)
- Unauthenticated login requests could write unbounded values to the auth audit log (#133369)
- The public `/auth/` routes had no request-body size limit (#133370)
- Native sign-in could send login codes to a non-loopback redirect, which allowed session takeover (#130685)

Thanks to Tenable Research for reporting all four issues (TRA-725, TRA-726, TRA-727, TRA-728). The native sign-in redirect issue was also reported independently and fixed by @Froraut. The `X-Forwarded-For` fix builds on community work by @hinotoi-agent and @BearHuddleston (#40285).

**Repository git filter hardening**

- Automatic git calls (session workspace snapshot, subagent worktrees, kanban, worktree cleanup, `hermes -w`) could run `clean`/`smudge`/`process` filter programs defined by an untrusted repository's own config, before the first prompt (#130661)

Thanks to 燕涛 for reporting this privately. It was also reported and fixed publicly by @jonpol01 (#126017, #126019) and @JoaoMarcos44 (#126075).

**Email gateway sender hardening**

- A quoted display name in the `From` header (e.g. `"Victim <victim@example.com>" <attacker@evil.test>`) could make an attacker's message pass the email allowlist as an allowed sender (#125212)

Thanks to Daniel Steele (@keeltrace) for reporting this and writing the fix (#124322).

---

## Updating

- Docker / Hermes Cloud: `nousresearch/hermes-agent:stable` (or `:latest`)
- CLI (git installs): `hermes update`, or re-run the installer one-liner
- Desktop app and Termux: no change in this release; they update with the next bundled release

**Full Changelog**: [v2026.9.24...v0.21.6](https://github.com/NousResearch/hermes-agent/compare/v2026.9.24...v0.21.6)

---

*← [v0.21.5 - Patch Release](/hermes/changelog/v0.21.5) | [Changelog Home](/hermes/changelog) →*

*↑ [Changelog Home](/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
