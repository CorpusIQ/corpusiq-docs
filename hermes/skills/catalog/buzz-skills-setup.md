---
title: "Buzz Skills — Hermes Agent on Nostr via Block's Buzz Setup"
description: "tonbistudio/buzz-skills — 3 skills, 250 GitHub stars: connect a Hermes Agent to the Buzz messaging community (block/buzz, Nostr-based) as a native agent with NIP-OA attestation, deliver local media as native Buzz attachments, and self-host a Buzz relay."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/buzz-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-19"
tags: ["hermes skill", "agent skill", "skill setup", "buzz", "nostr", "messaging gateway", "self-hosting", "media delivery"]
---

# Buzz Skills — Setup Guide

**Source:** [tonbistudio/buzz-skills](https://skills.sh/tonbistudio/buzz-skills)
**GitHub:** [tonbistudio/buzz-skills](https://github.com/tonbistudio/buzz-skills)
**Skills:** 3 skills (hermes-in-buzz 3 installs, buzz-media-attachments 3, buzz-self-hosting 2)
**Category:** Messaging Integration
**First Seen:** August 19, 2026 evening sweep
**Quality Tier:** 🟡 Beta — 250 GitHub stars, created July 30, 2026; small, portable, and pinned against the official block/buzz source releases

Buzz is Square/Block's Nostr-based messaging client ([block/buzz](https://github.com/block/buzz)). This pack makes a Hermes Agent a first-class Buzz community member: a dedicated Nostr identity for the agent, owner-only access controls, NIP-OA attestation so the community can verify the agent, gateway configuration, and native media delivery through the Buzz CLI. It is the first documented path for running a Hermes gateway on the Nostr relay network rather than on Telegram/Discord-class adapters.

---

## Installation

The maintained-checkout pattern (recommended — keeps the skills updateable with `git pull`):

```bash
git clone https://github.com/tonbistudio/buzz-skills.git
```

```yaml
# ~/.hermes/config.yaml
skills:
  external_dirs:
    - /absolute/path/to/buzz-skills
```

Or via the skills.sh marketplace:

```bash
npx skills add tonbistudio/buzz-skills
```

The pack includes two helper scripts under `hermes-in-buzz/scripts/`: a cross-platform credential updater (`update_buzz_credentials.py`, reads keys with hidden input and atomically updates the active profile's `.env`) and an optional Rust helper for deriving the agent identity and creating NIP-OA attestations without placing private keys in argv.

## Prerequisites

| Requirement | Details |
|---|---|
| **Buzz CLI** | `buzz` CLI installed per the block/buzz releases (the official repo also publishes a `buzz-cli` skill, 36 installs) |
| **A Buzz community or relay** | Hosted community or the self-hosted `deploy/compose` stack for buzz-self-hosting |
| **Nostr identity** | A separate nsec for the agent — never the owner's identity |
| **Docker (self-hosting only)** | For the relay compose stack |

## What It Provides

| Skill | Purpose |
|---|---|
| hermes-in-buzz | End-to-end setup of a dedicated Hermes Agent as a native Buzz messaging agent: relay connectivity, separate Nostr identity, owner-only access controls, Buzz CLI installation, NIP-OA attestation, gateway configuration, live inbound/outbound verification |
| buzz-media-attachments | Send local media files to the active Buzz conversation through the native `buzz messages send --file` flow when generic `MEDIA:/path` delivery is unavailable; MP4 fast-start and canonical sanitization workflows, GIF fallback |
| buzz-self-hosting | Stand up and debug a self-hosted Buzz relay via `deploy/compose`: env/secrets setup, closed-relay membership, the loopback-hostname 404 footgun (`localhost` vs `127.0.0.1`), community re-keying, agent-response debugging, backups, and hosted-to-self-hosted migration limits |

## Quick Start

1. Clone and register: `git clone https://github.com/tonbistudio/buzz-skills.git` then add the path to `skills.external_dirs` in `~/.hermes/config.yaml`
2. Install the Buzz CLI and generate a dedicated Nostr keypair for the agent
3. Load hermes-in-buzz and say "connect this Hermes gateway to my Buzz community"
4. For reports with attachments, load buzz-media-attachments so media goes out as native Buzz files

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **New gateway surface** | hermes-in-buzz is the first Nostr-native Hermes gateway path — an additional distribution channel for agent reports and community presence beyond Telegram |
| **Native media delivery** | buzz-media-attachments solves the exact class of problem we hit when `MEDIA:` paths fail on a given adapter — native `--file` fallback with fast-start and sanitization |
| **Relay self-hosting playbook** | buzz-self-hosting's compose-stack debugging (loopback footgun, re-keying, backup, migration limits) is a reusable reference for running our own relay infrastructure |
| **Owner-only access controls** | The NIP-OA attestation + owner-only pattern is a reference for agent identity verification on any public relay |

## Limitations / Verification

- Below the 20K install guide bar — drafted on cluster authority: new ecosystem surface (Nostr/Buzz for Hermes gateways), 250 GitHub stars, created July 30, 2026
- Buzz itself is young; the pack is pinned against block/buzz source releases and expects the CLI to be built from the same pinned release as the Rust helper
- buzz-self-hosting targets the `deploy/compose` stack; hosted-community users only need hermes-in-buzz
- The official block/buzz `buzz-cli` skill (36 installs) is the upstream CLI reference — install it before attempting any of the three

```bash
git clone https://github.com/tonbistudio/buzz-skills.git   # verify checkout works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)
- [Hermes Field Kit Setup](/hermes/skills/catalog/hermes-field-kit-setup/)

*Powered by CorpusIQ*
