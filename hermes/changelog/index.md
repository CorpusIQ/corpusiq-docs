---
title: "Hermes Agent Changelog - CorpusIQ Docs"
description: Version history and release notes for NousResearch Hermes Agent. Track new features, breaking changes, and upgrades.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/"
robots: "index,follow"
last_updated: "2026-10-13"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent Changelog

Track every Hermes Agent release. New versions are auto-detected and documented within 24 hours of publication.

## Releases

| Version | Date | Name | Highlights |
|---------|------|------|------------|
| [v0.21.7](/hermes/changelog/v0.21.7) | October 12, 2026 | Patch Release | Patch release. This tag rolls up the ~204 PRs merged since v0.21.6 into a stable release for the desktop app (macOS Apple silicon, Windows), the Microsoft Store and MSIX, the installer, Docker and Hermes... |
| [v0.21.6](/hermes/changelog/v0.21.6) | October 8, 2026 | Patch Release | 2,106 PRs: first release from the new stable pipeline (tested Docker image, receipt tag), plus dashboard auth, git filter, and email gateway sender hardening |
| [v0.21.5](/hermes/changelog/v0.21.5) | September 24, 2026 | Patch Release | 460 PRs: Desktop plugin SDK wave, Simple/Advanced interface mode, Connectors page replacing the MCP tab, French/German/Spanish catalogs, per-profile lifecycle controls |
| [v0.21.4](/hermes/changelog/v0.21.4) | September 21, 2026 | Patch Release | 1,812 PRs: host-wide gateway singleton lock, `--format stream-json` CLI, `skills.auto_load`, session_search bounds, LTX 2.5 + Kling O3 video catalogs, plugin and author pages |
| [v0.21.3](/hermes/changelog/v0.21.3) | September 14, 2026 | Patch Release | Remote dashboard refresh-token coalescing and state.db writer-handle dedup for remote Desktop and Cloud users |
| [v0.21.2](/hermes/changelog/v0.21.2) | September 11, 2026 | The state.db Patch Release | Six-PR reliability campaign: no more second writers, healthy databases no longer reported corrupt, safe `doctor --fix` |
| [v0.21.1](/hermes/changelog/v0.21.1) | September 7, 2026 | Patch Release | 632 PRs: codebase modularization, startup performance, provider and model updates, MCP authorization, cron delivery fixes |
| [v0.21.0](/hermes/changelog/v0.21.0) | August 31, 2026 | The Pantheon Release | Bot Mode agent society, cron memory and continuity, live subagent steering, MCP command center, desktop browser driving, six new providers |
| [v0.20.6](/hermes/changelog/v0.20.6) | August 27, 2026 | Patch Release | Patch release. This tag rolls up the ~525 PRs merged since v0.20.5 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs). |
| [v0.20.5](/hermes/changelog/v0.20.5) | August 21, 2026 | Patch Release | Patch release. This tag rolls up the ~323 PRs merged since v0.20.4 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs). |
| [v0.20.4](/hermes/changelog/v0.20.4) | August 18, 2026 | Patch Release | Patch release. This tag rolls up the ~74 PRs merged since v0.20.3 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs). |
| [v0.20.3](/hermes/changelog/v0.20.3) | August 17, 2026 | Patch Release | Patch release. This tag rolls up the ~125 PRs merged since v0.20.2 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs). |
| [v0.20.2](/hermes/changelog/v0.20.2) | August 16, 2026 | Patch Release | Patch release. This tag rolls up the ~397 PRs merged since v0.20.1 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs). |
| [v0.20.1](/hermes/changelog/v0.20.1) | August 13, 2026 | Patch Release | 1,444 commits, ~656 PRs: stabilization across desktop app, gateway platforms, installers, tool system, provider catalogs |
| [v0.20.0](/hermes/changelog/v0.20.0) | August 3, 2026 | The Herald Release | Streaming conversational voice, A2A v1.0, grounded citations, desktop artifacts + plugin SDK, CLI power commands, tool self-recovery, smarter compression - 3,650 commits, 647 contributors |
| [v0.19.1](/hermes/changelog/v0.19.1) | July 30, 2026 | Patch Release | ~3,087 commits: gateway stability, voice fixes, Telegram media, FLUX3 video, Buzz/Nostr, installer patches |
| [v0.19.0](/hermes/changelog/v0.19.0) | July 20, 2026 | The Quicksilver Release | ~80% first-token speed improvement, terminal billing, Bitwarden/1Password secrets, smart approvals, durable delivery ledger, live subagent transcripts, GPT-5.6/grok-4.5/kimi-k3, 450+ contributors |
| [v0.18.2](/hermes/changelog/v0.18.2) | July 7, 2026 | WhatsApp Baileys Fix | Unpins WhatsApp Baileys bridge from git commit to published npm 7.0.0-rc13, fixing Docker builds |
| [v0.18.1](/hermes/changelog/v0.18.1) | July 7, 2026 | Infrastructure Patch | ~660 PR roll-up since v0.18.0: installer self-healing, dashboard/gateway fixes, WhatsApp pairing, MCP/provider fixes, stability hardening |
| [v0.18.0](/hermes/changelog/v0.18.0) | July 1, 2026 | The Judgment Release | P0/P1 clean sweep (100% resolved), Mixture-of-Agents as first-class model, verification & completion contracts, `/learn` skill distillation, `/journey` learning timeline, desktop coding Projects, background fan-out, scale-to-zero gateway, Google Vertex AI, security hardening |
| [v0.17.0](/hermes/changelog/v0.17.0) | June 19, 2026 | The Reach Release | iMessage via Photon, Raft agent network, background subagents, image editing, Automation Blueprints, desktop overhaul, Skills Hub rehaul, WhatsApp, Telegram rich text |
| [v0.16.0](/hermes/changelog/v0.16.0) | June 5, 2026 | The Surface Release | Desktop app, remote gateway, web admin panel, fuzzy model picker, `/undo`, 简体中文, leaner skills, NVIDIA/skills tap |
| [v0.15.2](/hermes/changelog/v0.15.2) | May 29, 2026 | Patch Release | Ships bundled plugin.yaml manifests in wheel and sdist ([`827f7f07`](https://github.com/NousResearch/hermes-agent/commit/827f7f07825be57108cbea18325e8f5e9fb5d2f2)) |
| [v0.15.1](/hermes/changelog/v0.15.1) | May 29, 2026 | Patch Release | > **The Patch Release.** A same-day hotfix for v0.15.0. Headline fix: the dashboard infinite-reload loop that hit anyone running v0.15.0 in loopback mode (Docker, hosted Hermes, fresh installs). A handful of... |
| [v0.15.0](/hermes/changelog/v0.15.0) | May 28, 2026 | Patch Release | > **The Velocity Release.** Hermes gets dramatically faster  -  to start, to run, to ship work, and to grow. The 16,083-line `run_agent.py` collapses to 3,821 (-76%) across 14 cohesive `agent/*` modules. Kanban... |
| [v0.14.0](/hermes/changelog/v0.14.0) | May 16, 2026 | Patch Release | > The Foundation Release  -  Hermes installs and runs anywhere, ships with the things you actually want to use, and stops shipping the things you don't. xAI Grok lands as a SuperGrok OAuth provider with grok-4.3... |
| [v0.13.0](/hermes/changelog/v0.13.0) | May 7, 2026 | Patch Release | > The Tenacity Release  -  Hermes Agent now finishes what it starts. Kanban ships as a durable multi-agent board (heartbeat, reclaim, zombie detection, auto-block on incomplete exit, per-task retries... |
| [v0.12.0](/hermes/changelog/v0.12.0) | April 30, 2026 | Patch Release | > The Curator release  -  Hermes Agent now maintains itself. An autonomous background Curator grades, prunes, and consolidates your skill library on its own schedule. The self-improvement loop that reviews what... |
| [v0.11.0](/hermes/changelog/v0.11.0) | April 23, 2026 | Patch Release | > The Interface release  -  a full React/Ink rewrite of the interactive CLI, a pluggable transport architecture underneath every provider, native AWS Bedrock support, five new inference paths, a 17th messaging... |
| [v0.10.0](/hermes/changelog/v0.10.0) | April 16, 2026 | Patch Release | > The Tool Gateway release  -  paid Nous Portal subscribers can now use web search, image generation, text-to-speech, and browser automation through their existing subscription with zero additional API keys. |
| [v0.9.0](/hermes/changelog/v0.9.0) | April 13, 2026 | Patch Release | > The everywhere release  -  Hermes goes mobile with Termux/Android, adds iMessage and WeChat, ships Fast Mode for OpenAI and Anthropic, introduces background process monitoring, launches a local web dashboard... |
| [v0.8.0](/hermes/changelog/v0.8.0) | April 8, 2026 | Patch Release | > The intelligence release  -  background task auto-notifications, free MiMo v2 Pro on Nous Portal, live model switching across all platforms, self-optimized GPT/Codex guidance, native Google AI Studio, smart... |
| [v0.7.0](/hermes/changelog/v0.7.0) | April 3, 2026 | Patch Release | > The resilience release  -  pluggable memory providers, credential pool rotation, Camofox anti-detection browser, inline diff previews, gateway hardening across race conditions and approval routing, and deep... |
| [v0.6.0](/hermes/changelog/v0.6.0) | March 30, 2026 | Patch Release | > The multi-instance release  -  Profiles for running isolated agent instances, MCP server mode, Docker container, fallback provider chains, two new messaging platforms (Feishu/Lark and WeCom), Telegram webhook... |
| [v0.5.0](/hermes/changelog/v0.5.0) | March 28, 2026 | Patch Release | > The hardening release  -  Hugging Face provider, /model command overhaul, Telegram Private Chat Topics, native Modal SDK, plugin lifecycle hooks, tool-use enforcement for GPT models, Nix flake, 50+ security... |
| [v0.4.0](/hermes/changelog/v0.4.0) | March 24, 2026 | Patch Release | > The platform expansion release  -  OpenAI-compatible API server, 6 new messaging adapters, 4 new inference providers, MCP server management with OAuth 2.1, @ context references, gateway prompt caching... |
| [v0.3.0](/hermes/changelog/v0.3.0) | March 17, 2026 | Patch Release | > The streaming, plugins, and provider release  -  unified real-time token delivery, first-class plugin architecture, rebuilt provider system with Vercel AI Gateway, native Anthropic provider, smart approvals... |
| [v0.2.0](/hermes/changelog/v0.2.0) | March 12, 2026 | Patch Release | > First tagged release since v0.1.0 (the initial pre-public foundation). In just over two weeks, Hermes Agent went from a small internal project to a full-featured AI agent platform  -  thanks to an explosion of... |

---

## How Updates Are Detected

Three release checks a day compare the newest Hermes Agent GitHub release against the version documented here:

| Check | Schedule | Action |
|------|----------|--------|
| `hermes-release-monitor` | 02:00, 10:00, 18:00 UTC | Poll GitHub releases; draft and publish the changelog page for any new tag |

When a new release is detected, a changelog page is generated, committed to `CorpusIQ/corpusiq-docs`, deployed, and reported by email.
---

## FAQ

### What is the latest Hermes Agent version?

v0.21.7, published October 12, 2026. See the release notes for the full changes.

### How often is the Hermes changelog updated?

New versions are detected automatically by release monitors that poll the Hermes Agent GitHub repository three times a day, and a changelog page for each release is published within 24 hours of the tag going live.

### How do I update Hermes Agent?

Run `hermes update` from the terminal, or install fresh with the official installer script at hermes-agent.nousresearch.com/install.sh. Managed and hosted deployments update through their deployment tooling using the latest release tag.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the latest Hermes Agent version?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "v0.21.7, published October 12, 2026. See the release notes for the full changes."
      }
    },
    {
      "@type": "Question",
      "name": "How often is the Hermes changelog updated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "New versions are detected automatically by release monitors that poll the Hermes Agent GitHub repository three times a day, and a changelog page for each release is published within 24 hours of the tag going live."
      }
    },
    {
      "@type": "Question",
      "name": "How do I update Hermes Agent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Run hermes update from the terminal, or install fresh with the official installer script at hermes-agent.nousresearch.com/install.sh. Managed and hosted deployments update through their deployment tooling using the latest release tag."
      }
    }
  ]
}
</script>

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
