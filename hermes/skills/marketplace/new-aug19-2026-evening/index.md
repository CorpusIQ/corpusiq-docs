---
title: "New Skills — August 19, 2026 (Evening)"
description: "skills.sh evening sweep: Hermes Field Kit (asimons81, 122⭐, 16 skills), AtlasOmnia Hermes Custom Pack (48⭐, 60+ skills), Buzz Skills (tonbistudio, 250⭐, Hermes on Nostr) — 3 new publisher clusters, 79+ skills, 3 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug19-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-19"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-19-evening"
new_publishers: 3
new_skills: 79
guides_drafted: 3
---

# New Skills — August 19, 2026 (Evening)

Evening sweep of August 19. Fourteen skills.sh API queries (hermes core, broad, and ecosystem repos) returned 605 unique skills; the cluster-level diff (skill name AND source repo grep against the full hermes/ tree) surfaced three genuinely new Hermes-native publisher clusters that the morning sweep's top-band floor missed. All three sit below the 2,000-install band but clear the cluster-authority bar: cohesive, versioned, Hermes-native suites with real field pedigree.

## New Publisher Clusters — Guided This Sweep

| Cluster | Skills | GitHub | Tier | Guide |
|---|---|---|---|---|
| asimons81/hermes-field-kit | 16 (13 stable + 3 experimental) | 122⭐ | 🟡 | [Hermes Field Kit Setup](/hermes/skills/catalog/hermes-field-kit-setup/) |
| atlasomnia/hermes-custom-pack | 60+ | 48⭐ | 🟡 | [AtlasOmnia Hermes Custom Pack Setup](/hermes/skills/catalog/atlasomnia-hermes-custom-pack-setup/) |
| tonbistudio/buzz-skills | 3 | 250⭐ | 🟡 | [Buzz Skills Setup](/hermes/skills/catalog/buzz-skills-setup/) |

## Method Notes

- 14 queries (nousresearch/hermes-agent, aradotso/hermes-skills, 4 broad hermes queries, garrytan/gbrain, plastic-labs/honcho, aradotso/devtools-skills, sickn33/antigravity-awesome-skills, kcchien/clawpilot, rethinking-studio/clawpilot-skills, varnan-tech/opendirectory, cosmicstack-labs/mercury-agent-skills) → 605 unique skills → 111 name-level NEW flags.
- Cluster-level filtering (source-repo grep) cut 111 to 3 genuine clusters. The four >100-install hits (ux-audit-rethink 716, researchers-tech 169, skill-studio 158, amz-negative-keywords 100) were all rejected as non-Hermes: Claude Code UX audit, Suno music production, Claude Code workflow studio, and Amazon-seller Claude skills respectively.
- asimons81/hermes-field-kit is the standout find: the most disciplined Hermes-native operations suite on the marketplace. SemVer releases, per-skill versioning, a dependency-free repository validator, published skill specification, and an explicit admission rule (solves a real task, used in a real workflow, reproducible by another person). The 16 skills organize as inspect → diagnose → recover → migrate → verify.
- atlasomnia/hermes-custom-pack is the broadest Hermes-ops pack: config editing that works around security guards, context optimization, self-evaluation, session maintenance, Mnemosyne operations, plugin development/evaluation, and a verification family (pre-push gates, publication link audits, source verification) that mirrors CorpusIQ's public-content discipline.
- tonbistudio/buzz-skills opens a genuinely new surface: the first documented path for a Hermes gateway on Nostr via Square/Block's Buzz client, including NIP-OA attestation and native media attachment delivery. The official block/buzz repo's buzz-cli skill (36 installs) is the upstream CLI reference.
- Mac Mini still unreachable — sweep ran entirely from the Spark canonical clone, push auth via gh CLI token.

## Evaluated and Queued

| Cluster | Skills | Installs | Reason parked |
|---|---|---|---|
| mastepanoski/claude-skills (ux-audit-rethink) | 1 | 716 | Claude Code UX audit skill; no Hermes target |
| bitwize-music-studio/claude-ai-music-skills (researchers-tech) | 1 | 169 | Suno music production; not agent tooling |
| glebis/claude-skills (skill-studio) | 1 | 158 | Claude Code workflow studio |
| jaygptpro/amazon-pro-skills (amz-negative-keywords) | 1 | 100 | Amazon-seller Claude skills |
| twexapi-dev/hermes-xapi | 1 | 1 | Hermes X-automation plugin, 0⭐ — parked below bar; watch for growth |
| zelray/hermes-composio-skill | 1 | 1 | Composio integration, 0⭐ — below bar |
| rox1694125-bit/hermes-codex-control-plane | 2 | 1×2 | Codex control-plane pattern, 0⭐ — below bar |
| mah92/hermes-persian-skills | 3 | 1×3 | Persian locale niche (Bale messenger, STT/TTS), 2⭐ |
| alexeyisme/hermes-spotify-skill | 1 | 10 | Spotify novelty, low value for ops |
| redoracle/hermes-ops-kit | 2 | 1×2 | Early-stage ops kit, below cluster bar |

## Notable Signals for CorpusIQ

- **hermes-stack-doctor + hermes-token-audit** are direct upgrades to our own system-auditor and token-health cadences: read-only GREEN/YELLOW/RED verdicts and estimate-vs-billing separation, exactly our verify-before-assertion shape.
- **dont-lie-to-me** encodes evidence discipline (observed vs sourced vs inferred vs unknown) as a loadable skill — the same discipline our public-content guardrails enforce.
- **x-post-writer + x-analytics-import** target our primary social channel directly: claim-verified drafting and private-by-default analytics import.
- **github-pre-push-gates + publication-link-audit** (custom-pack) match our pre-push sanitization and broken-link audit passes one to one.
- **hermes-in-buzz** is worth tracking: if Buzz/Nostr gateways take off, CorpusIQ gains an additional agent-delivery surface with native media attachments.

## Index State After Sweep

- catalog/index.md: +3 entries
- marketplace/index.md: header 903 → 906, footer 954 → 957
- last_updated on both indexes: 2026-08-19
