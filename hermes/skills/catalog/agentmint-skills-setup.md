---
title: AgentMint Skills Setup Guide
description: Route Hermes delegate_task to persistent AgentMint subagents with cross-call memory — wallet-based agent identity and JSON-RPC agent operations
---

# AgentMint Skills — Setup Guide

**AgentMint Skills** bridge Hermes Agent's `delegate_task` to the [AgentMint](https://agentmint.store) platform, enabling persistent subagents that remember across calls via wallet-based identity.

By [mesutcelik/agentmint-skills](https://github.com/mesutcelik/agentmint-skills).

---

## 1. Prerequisites

- **Hermes Agent** installed and running
- Python 3.10+
- An AgentMint account (create at [agentmint.store](https://agentmint.store))

---

## 2. Install AgentMint Hermes Runner

The Python adapter bridges Hermes' gateway to the AgentMint API:

```bash
pip install agentmint-hermes-runner
```

This installs from [mesutcelik/agentmint-hermes](https://github.com/mesutcelik/agentmint-hermes) (available on PyPI).

---

## 3. Install the Skills

```bash
# Universal AgentMint usage skill
hermes skills install mesutcelik/agentmint-skills/agentmint

# Hermes-specific delegate_task routing skill
hermes skills install mesutcelik/agentmint-skills/hermes-delegate-task
```

---

## 4. Configure Hermes Gateway

Add the AgentMint runner to your Hermes gateway config:

```yaml
# ~/.hermes/config.yaml
gateway:
  plugins:
    agentmint:
      enabled: true
      adapter: agentmint_hermes_runner
      wallet_path: ~/.agentmint/wallet.json
```

---

## 5. Skill Reference

### `agentmint` — Universal Usage

Discovery checklist, wallet matrix, every JSON-RPC method, persona format. Snapshot of the canonical [AgentMint SKILL.md](https://agentmint.store/SKILL.md).

**Use when:** Setting up new AgentMint wallets, exploring available RPC methods, creating agent personas.

### `hermes-delegate-task` — Hermes Subagent Router

Routes `delegate_task(background=True)` calls to named, persistent AgentMint subagents.

**Key difference from native delegate_task:**
- Native `delegate_task`: subagent lives for one call, no memory
- AgentMint `delegate_task`: subagent persists across calls, remembers context
- Subagents have wallet-based identity on the AgentMint platform

---

## 6. CorpusIQ Use Cases

- **Long-running research agents** — Delegate competitive research to persistent subagents that accumulate knowledge across sessions
- **Multi-agent growth ops** — Separate agents for social monitoring, lead capture, and content creation with shared wallet identity
- **Client onboarding** — Persistent per-client subagents that remember integration details

---

## 7. Verification

```bash
# Check skills are loaded
hermes skills list | grep agentmint

# Test AgentMint connectivity
python3 -c "from agentmint_hermes_runner import AgentMintClient; print(AgentMintClient().health())"

# Verify gateway config
hermes config get gateway.plugins.agentmint
```

---

## 8. Troubleshooting

| Issue | Fix |
|-------|-----|
| `agentmint-hermes-runner` not found | Ensure PyPI package is installed: `pip install agentmint-hermes-runner` |
| Wallet not found | Create at [agentmint.store](https://agentmint.store) or run `agentmint wallet create` |
| Subagent doesn't remember | Verify `background=True` is set on `delegate_task` calls |
| Gateway plugin not loading | Check `~/.hermes/config.yaml` syntax and restart Hermes |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [AgentMint Skills Repo](https://github.com/mesutcelik/agentmint-skills) →*
