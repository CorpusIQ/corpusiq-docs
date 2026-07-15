---
title: "AGEL-Comp Safety Framework — Setup Guide"
description: "Install and configure the AGEL-Comp neuro-symbolic safety layer for Hermes Agent. Automatic blocking, causal learning, and queryable world model."
skill_name: hermes-agel-comp
category: Security
source_repo: lesterppo/hermes-agel-comp
stars: 0
language: Python
platforms: [Linux, macOS]
---

# AGEL-Comp Safety Framework — Full Setup Guide

A neuro-symbolic safety layer for [Hermes Agent](https://github.com/NousResearch/hermes-agent) based on the AGEL-Comp framework (Shahid & Rothe, 2026). Works transparently through Hermes plugin hooks — **zero agent compliance needed.**

---

## What It Does

### Automatic safety blocking

The `agel-safety` plugin intercepts tool calls **before execution**:

| Tool | Blocked when |
|------|-------------|
| `read_file` | Path matches secret-file pattern (`.env`, `credentials.json`, `api_key.*`, …) |
| `terminal` | Command matches destructive pattern (`rm -rf`, `git reset --hard`, `DROP TABLE`, …) |
| `write_file` | Target path matches secret-file pattern |

The agent sees the block reason and can ask for user approval — it doesn't silently fail.

### Causal learning from mistakes

When a tool call returns an error, the plugin runs the **MCS+ILP pipeline**:

1. **MCS (Minimal Contrastive Search)** — isolates the causal factor
2. **ILP (Inductive Logic Programming)** — generalizes to a reusable rule
3. **CPG world model** is updated — the agent won't make the same mistake twice

**Example:** Agent reads `passwords.txt` and gets "Permission denied" → learns `requires_approval(X) :- contains_secrets(X)` and `contains_secrets(passwords_txt)` → next time, any file reading triggers an NTP check and is blocked if secrets are suspected.

### Queryable world model

The `agel_comp` Hermes tool provides 10 actions for querying and extending the Causal Program Graph:

```
agel_comp(action="bootstrap")          # Load foundational knowledge
agel_comp(action="prove", head="...")   # NTP verification of safety rules
agel_comp(action="learn_from", ...)     # Run MCS+ILP learning from an error
agel_comp(action="list_rules")          # Show all CPG rules
agel_comp(action="query_rule", id=...)  # Inspect a specific rule
agel_comp(action="status")             # CPG statistics and health
agel_comp(action="export")             # Export rules to JSON
agel_comp(action="import", ...)        # Import rules from JSON
agel_comp(action="reset")              # Clear all learned rules
agel_comp(action="explain", id=...)    # Explain a rule's derivation
```

---

## Prerequisites

- **Hermes Agent** running with plugin support
- **Python 3.10+**
- Write access to `$HERMES_HOME` (for persisting the CPG)

---

## Install

### Quick install

```bash
git clone https://github.com/lesterppo/hermes-agel-comp.git
cd hermes-agel-comp
./install.sh
```

Restart Hermes. The safety layer is active immediately.

### Manual install

```bash
# 1. Clone
git clone https://github.com/lesterppo/hermes-agel-comp.git
cd hermes-agel-comp

# 2. Install the plugin
mkdir -p $HERMES_HOME/plugins/agel-comp
cp -r agel_safety $HERMES_HOME/plugins/agel-comp/
cp agel_comp_tool.py $HERMES_HOME/plugins/agel-comp/

# 3. Register in Hermes config
# Add to $HERMES_HOME/config.yaml:
# plugins:
#   agel-comp:
#     enabled: true
#     path: plugins/agel-comp

# 4. Restart Hermes
```

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│                  Hermes Agent                    │
│  ┌───────────────────────────────────────────┐  │
│  │         agel-safety plugin                │  │
│  │  pre_tool_call  ──→ NTP verification      │  │
│  │  post_tool_call ──→ MCS+ILP learning      │  │
│  └──────────────┬────────────────────────────┘  │
│                 │                                │
│  ┌──────────────▼────────────────────────────┐  │
│  │           Causal Program Graph            │  │
│  │  W = (V, E)  —  Horn clauses as rules    │  │
│  │  Persists to $HERMES_HOME/agel_comp/     │  │
│  └──────────────────────────────────────────┘  │
│                                                 │
│  ┌──────────────────────────────────────────┐  │
│  │         agel_comp tool (10 actions)       │  │
│  │  bootstrap · prove · learn_from · query  │  │
│  │  list_rules · status · export · import   │  │
│  │  reset · explain                          │  │
│  └──────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

### Pre-tool-call hook (NTP verification)

Before every tool call, the plugin:
1. Extracts the tool name and arguments
2. Checks against the CPG for matching rules
3. Runs **NTP (Neural Theorem Proving)** verification
4. Returns `allow`, `block`, or `warn`

### Post-tool-call hook (MCS+ILP learning)

After every tool call that returns an error:
1. **MCS** isolates the causal factor from the error
2. **ILP** generalizes it into a reusable Horn clause rule
3. The rule is added to the CPG
4. Future calls matching the rule pattern are pre-blocked

---

## Configuration

### Default safety rules (built-in)

```prolog
% Secret file patterns
block_read(X) :- matches_pattern(X, ".env").
block_read(X) :- matches_pattern(X, "credentials.json").
block_read(X) :- matches_pattern(X, "api_key.*").
block_read(X) :- matches_pattern(X, "*.pem").
block_read(X) :- matches_pattern(X, "id_rsa*").

% Destructive commands
block_exec(X) :- contains_substring(X, "rm -rf /").
block_exec(X) :- contains_substring(X, "git reset --hard").
block_exec(X) :- contains_substring(X, "DROP TABLE").
block_exec(X) :- contains_substring(X, "shutdown -h now").

% Write protection
block_write(X) :- matches_pattern(X, "/etc/*").
block_write(X) :- matches_pattern(X, "~/.ssh/*").
```

### Adding custom rules

Use the `agel_comp` tool from within a Hermes session:

```
agel_comp(action="learn_from",
          tool="terminal",
          error="Permission denied: cannot delete /etc/hosts",
          context="Agent attempted to modify system file")

# Or import from JSON
agel_comp(action="import",
          rules='[{"head": "block_exec(X)", "body": "matches_pattern(X, \\"sudo rm\\")"}]')
```

---

## Usage Examples

### Bootstrap the safety layer

```
agel_comp(action="bootstrap")
```
Loads foundational safety knowledge into the CPG. Run once after install.

### Check safety status

```
agel_comp(action="status")
```
Returns:
```
CPG Status:
  Rules: 47 (12 built-in, 35 learned)
  Blocked calls today: 23
  Learned rules today: 3
  False positives: 0
  Storage: $HERMES_HOME/agel_comp/cpg.db (1.2 MB)
```

### List all rules

```
agel_comp(action="list_rules")
```
Returns all active Horn clause rules with their derivation source (built-in, learned, imported).

### Verify a proposed action

```
agel_comp(action="prove", head="block_exec(rm -rf /tmp/cache)")
```
Returns `true` (blocked) or `false` (allowed) with the matched rule.

### Learn from a mistake

```
agel_comp(action="learn_from",
          tool="read_file",
          error="Permission denied: /home/user/.aws/credentials",
          context="Agent attempted to read AWS credentials file")
```
The MCS+ILP pipeline runs and adds: `block_read(X) :- matches_pattern(X, ".aws/credentials")`.

### Export rules for sharing

```
agel_comp(action="export")
```
Returns a JSON array of all rules that can be imported into another Hermes instance.

---

## Troubleshooting

### Plugin not loading

```bash
# Check Hermes logs for plugin errors
tail -100 $HERMES_HOME/logs/hermes.log | grep agel

# Verify plugin files exist
ls -la $HERMES_HOME/plugins/agel-comp/

# Check config.yaml
grep -A5 "agel-comp" $HERMES_HOME/config.yaml
```

### CPG not persisting

The CPG is stored at `$HERMES_HOME/agel_comp/cpg.db`. Ensure the directory is writable:

```bash
mkdir -p $HERMES_HOME/agel_comp
chmod 755 $HERMES_HOME/agel_comp
```

### Too many false positives

If the safety layer is blocking legitimate operations:

```
# Review recent blocks
agel_comp(action="list_rules")

# Remove an over-aggressive rule
agel_comp(action="query_rule", id=12)
# If it's a learned rule →
agel_comp(action="reset", rule_id=12)
```

### Agent bypassing the safety layer

AGEL-Comp works through Hermes plugin hooks — the agent cannot disable it. If the agent appears to be bypassing blocks, check:

1. Plugin is loaded: `hermes plugins list | grep agel`
2. Hook is registered: check logs for `agel-safety: pre_tool_call registered`
3. CPG is loaded: `agel_comp(action="status")` shows rules > 0

---

## Related Tools

- [hermes-doctor](https://github.com/503496348-ops/hermes-doctor) — Self-diagnosis and self-healing plugin
- [agent-supervision-skills](https://github.com/drippy-passport968/agent-supervision-skills) — Delegate tasks with verification gates
- [hermes-flight-recorder](https://github.com/zwright8/hermes-flight-recorder) — Trace-based autonomy evals

---

## References

- Shahid, A. & Rothe, C. (2026). *AGEL-Comp: A Neuro-Symbolic Framework for Safe Autonomous Agent Deployment.*
- [Hermes Agent Plugin Documentation](#repo-unavailable)

---

*Powered by CorpusIQ*
