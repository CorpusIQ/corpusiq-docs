---
title: "Hermes Agent Changelog - CorpusIQ Docs"
description: Version history and release notes for NousResearch Hermes Agent. Track new features, breaking changes, and upgrades.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent Changelog

Track every Hermes Agent release. New versions are auto-detected and documented within 24 hours of publication.

## Releases

| Version | Date | Name | Highlights |
|---------|------|------|------------|
| [v0.21.5](/hermes/changelog/v0.21.5) | September 24, 2026 | Patch Release | 460 PRs: Desktop plugin SDK wave, Simple/Advanced interface mode, Connectors page replacing the MCP tab, French/German/Spanish catalogs, per-profile lifecycle controls |
| [v0.21.4](/hermes/changelog/v0.21.4) | September 21, 2026 | Patch Release | 1,812 PRs: host-wide gateway singleton lock, `--format stream-json` CLI, `skills.auto_load`, session_search bounds, LTX 2.5 + Kling O3 video catalogs, plugin and author pages |
| [v0.21.3](/hermes/changelog/v0.21.3) | September 14, 2026 | Patch Release | Remote dashboard refresh-token coalescing and state.db writer-handle dedup for remote Desktop and Cloud users |
| [v0.21.2](/hermes/changelog/v0.21.2) | September 11, 2026 | The state.db Patch Release | Six-PR reliability campaign: no more second writers, healthy databases no longer reported corrupt, safe `doctor --fix` |
| [v0.21.1](/hermes/changelog/v0.21.1) | September 7, 2026 | Patch Release | 632 PRs: codebase modularization, startup performance, provider and model updates, MCP authorization, cron delivery fixes |
| [v0.21.0](/hermes/changelog/v0.21.0) | August 31, 2026 | The Pantheon Release | Bot Mode agent society, cron memory and continuity, live subagent steering, MCP command center, desktop browser driving, six new providers |
| [v0.20.1](/hermes/changelog/v0.20.1) | August 13, 2026 | Patch Release | 1,444 commits, ~656 PRs: stabilization across desktop app, gateway platforms, installers, tool system, provider catalogs |
| [v0.20.0](/hermes/changelog/v0.20.0) | August 3, 2026 | The Herald Release | Streaming conversational voice, A2A v1.0, grounded citations, desktop artifacts + plugin SDK, CLI power commands, tool self-recovery, smarter compression - 3,650 commits, 647 contributors |
| [v0.19.1](/hermes/changelog/v0.19.1) | July 30, 2026 | Patch Release | ~3,087 commits: gateway stability, voice fixes, Telegram media, FLUX3 video, Buzz/Nostr, installer patches |
| [v0.19.0](/hermes/changelog/v0.19.0) | July 20, 2026 | The Quicksilver Release | ~80% first-token speed improvement, terminal billing, Bitwarden/1Password secrets, smart approvals, durable delivery ledger, live subagent transcripts, GPT-5.6/grok-4.5/kimi-k3, 450+ contributors |
| [v0.18.2](/hermes/changelog/v0.18.2) | July 7, 2026 | WhatsApp Baileys Fix | Unpins WhatsApp Baileys bridge from git commit to published npm 7.0.0-rc13, fixing Docker builds |
| [v0.18.1](/hermes/changelog/v0.18.1) | July 7, 2026 | Infrastructure Patch | ~660 PR roll-up since v0.18.0: installer self-healing, dashboard/gateway fixes, WhatsApp pairing, MCP/provider fixes, stability hardening |
| [v0.18.0](/hermes/changelog/v0.18.0) | July 1, 2026 | The Judgment Release | P0/P1 clean sweep (100% resolved), Mixture-of-Agents as first-class model, verification & completion contracts, `/learn` skill distillation, `/journey` learning timeline, desktop coding Projects, background fan-out, scale-to-zero gateway, Google Vertex AI, security hardening |
| [v0.17.0](/hermes/changelog/v0.17.0) | June 19, 2026 | The Reach Release | iMessage via Photon, Raft agent network, background subagents, image editing, Automation Blueprints, desktop overhaul, Skills Hub rehaul, WhatsApp, Telegram rich text |
| [v0.16.0](/hermes/changelog/v0.16.0) | June 5, 2026 | The Surface Release | Desktop app, remote gateway, web admin panel, fuzzy model picker, `/undo`, 简体中文, leaner skills, NVIDIA/skills tap |

---

## How Updates Are Detected

Three crons monitor Hermes Agent releases:
| Cron | Schedule | Action |
|------|----------|--------|
| `hermes-release-monitor` | 02:00, 10:00, 18:00 UTC | Check GitHub releases for new versions |

When a new release is detected, a changelog page is drafted, committed to `CorpusIQ/corpusiq-docs`, and reported via Telegram.
---

## FAQ

### What is the latest Hermes Agent version?

v0.21.5, published September 24, 2026. It rolls up roughly 460 PRs since v0.21.4, headlined by the Desktop plugin SDK wave and the new Connectors page.

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
        "text": "v0.21.5, published September 24, 2026. It rolls up roughly 460 PRs since v0.21.4, headlined by the Desktop plugin SDK wave and the new Connectors page."
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
