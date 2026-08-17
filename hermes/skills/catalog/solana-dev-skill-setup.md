---
title: "Solana Dev Skill — Official Blockchain Development"
description: "solana-foundation/solana-dev-skill — 58.4K installs. The Solana Foundation's official agent skill for building on Solana: program development, tokens, and ecosystem tooling."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/solana-dev-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup", "blockchain"]
---

# Solana Dev Skill — Setup Guide

**Source:** [skills.sh](https://www.skills.sh/solana-foundation/solana-dev-skill) (58.4K installs)
**GitHub:** [solana-foundation/solana-dev-skill](https://github.com/solana-foundation/solana-dev-skill)
**Category:** Blockchain Development
**First Seen:** August 13, 2026 sweep
**Quality Tier:** 🟢 Production (official foundation skill)

A single-purpose, official skill from the Solana Foundation. It encodes current Solana development practice for agents: program (smart contract) development with Anchor, token standards (SPL, Token-2022), RPC patterns, and ecosystem tooling. One of the few first-party blockchain skills on skills.sh — and the highest-installed one.

---

## Installation

```bash
npx skills add solana-foundation/solana-dev-skill
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| solana-dev | 58.4K | Solana development — programs, tokens, RPC, tooling |

## Prerequisites

- Rust toolchain for Anchor programs (or TypeScript for client-side)
- Solana CLI: `sh -c "$(curl -sSfL https://release.solana.com/stable/install)"`
- RPC endpoint (public devnet works for testing)

## CorpusIQ Use Cases

- **Web3 connector research** — Solana data patterns (RPC, account indexing) inform future payment/chain connector designs
- **Crypto OSINT pairing** — combines with `follow-the-crypto` from the OSINT skill set for on-chain investigation workflows

## Limitations / Verification

- Devnet-first: production programs need audit before mainnet deploy — the skill encodes development practice, not audit standards
- Verify: `solana --version` after CLI install, then `anchor build` on a sample program

## Related

- [OSINT Skills — Open-Source Intelligence Investigation Setup](/hermes/skills/catalog/osint-skills-setup/)
- [Solana Docs](https://solana.com/docs)
