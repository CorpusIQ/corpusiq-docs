---
title: "Commander Common Sense Gate - CorpusIQ Docs"
description: "Setup and usage guide for Commander Common Sense Gate. Part of the Hermes resource directory. judgment verification layer that inspects every proposed acti."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/commander/"
robots: "index,follow"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Commander Common Sense Gate

Commander is a judgment and verification layer that inspects every proposed Hermes action before execution. It identifies missing context, predicts consequences, and decides whether to approve, modify, clarify, escalate, or block.

## Architecture

Commander runs as the master controller. Every task enters through Commander first. Commander owns the decision. Hermes executes only what Commander approves.

## 10-Step Judgment Gate

1. What is the exact objective
2. What facts are confirmed
3. What information is missing
4. What assumptions are being made
5. What real-world constraints apply
6. What could fail
7. What damage could failure create
8. What evidence proves completion
9. Is the action reversible
10. Should the action be approved, modified, clarified, escalated, or blocked

## Hard Rules

16 hard rules run on every action. Pattern-matched in milliseconds:

- No em dashes in public content
- No internal analytics data in posts
- No AI buzzwords
- Content formula enforcement
- No posting to personal LinkedIn
- URL verification required
- Check [INTERNAL] folder before INBOX
- No NousResearch URLs in Hermes links
- Read entire message before acting
- No branches on CorpusIQ repos
- Browser-verify all LinkedIn posts
- Search knowledge stores before asking the team
- Check both email accounts
- No CID-embedded images in emails

## Failure Dataset

239 structured records from real Hermes mistakes. Each record maps to one or more of 12 capability categories: completeness, causal reasoning, physical reality, temporal reasoning, social reasoning, scope control, risk judgment, evidence discipline, memory application, uncertainty, resource judgment, security judgment.

## Training Loop

Commander improves with every decision. The cycle: submit, review, approve/block, execute, verify, learn.
