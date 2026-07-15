---
title: Three-Agent Bridge Protocol Setup Guide
description: Install and configure airbrushbones-afk/hermes-skills/three-agent-bridge — real-time sync protocol for multi-agent Hermes deployments across separate machines
---

# Three-Agent Bridge Protocol Setup

**Source:** [airbrushbones-afk/hermes-skills](#repo-unavailable)
**Package:** `three-agent-bridge` subdirectory
**Stars:** 0 ⭐ | **License:** MIT
**Created:** June 24, 2026
**Category:** Multi-Agent / DevOps / Coordination

---

## 1. What It Is

A real-time synchronization protocol for three Hermes agents: **Human + Desktop Hermes + VPS Hermes**. Uses a shared JSONL bridge file as the common communication channel — solving the fundamental problem that Hermes bots can't join Telegram group chats and two agents in separate DMs can't see each other's conversations.

### Architecture

```
┌─────────────┐      Telegram DM      ┌─────────────┐
│   Desktop   │◄─────────────────────►│     VPS     │
│   Hermes    │                        │   Hermes    │
│ (Lancelot)  │                        │ (Watchtower)│
└──────┬──────┘                        └──────┬──────┘
       │                                      │
       │         bridge-chat.jsonl            │
       └──────────── shared file ─────────────┘
                         │
                         │ Telegram DM
                         ▼
                 ┌───────────────┐
                 │    Human      │
                 │   (Bones)     │
                 └───────────────┘
```

## 2. Prerequisites

- Two Hermes agents on separate machines (or same machine with different profiles)
- Shared filesystem access (NFS, SMB, SSH, or Syncthing) between the two agent machines
- SSH access (for VPS-hosted bridge pattern)
- Telegram gateway configured on both agents

## 3. Installation

```bash
git clone #repo-unavailable.git
cp -r hermes-skills/three-agent-bridge ~/.hermes/skills/three-agent-bridge
```

### Verify

```bash
ls ~/.hermes/skills/three-agent-bridge/
# Should show: SKILL.md
```

## 4. Configuration

### Option A: Same Filesystem (NFS/SMB)

Both agents share a mounted filesystem:

```yaml
# In ~/.hermes/config.yaml on BOTH agents
three_agent_bridge:
  bridge_path: /mnt/shared/hermes/bridge-chat.jsonl
  poll_interval: 2  # seconds
  my_name: "desktop"  # unique per agent: "desktop" or "vps"
```

### Option B: VPS-Hosted (SSH Polling)

Desktop polls VPS via SSH:

```yaml
# Desktop agent config
three_agent_bridge:
  ssh_host: user@vps-ip
  bridge_path: /root/.hermes/shared/bridge-chat.jsonl
  polling_script: |
    ssh user@vps "tail -20 /root/.hermes/shared/bridge-chat.jsonl" > /tmp/bridge-snapshot.jsonl
  poll_interval: 2
```

```bash
# Start polling as background process
while true; do
  ssh user@vps "tail -20 /root/.hermes/shared/bridge-chat.jsonl" > /tmp/bridge-snapshot.jsonl
  sleep 2
done
```

### Option C: Syncthing (File Sync)

Syncthing provides real-time file sync between machines without SSH overhead:

```bash
# Install Syncthing on both machines
sudo apt install syncthing  # or brew install syncthing

# Create shared directory
mkdir -p ~/hermes-bridge

# Configure in Syncthing UI (http://localhost:8384):
# - Add ~/hermes-bridge to both devices
# - Enable "Send & Accept" on both sides
# - Set to "File Versioning: Trash Can File Versioning"

# Both agents write/read from ~/hermes-bridge/bridge-chat.jsonl
```

## 5. Bridge File Protocol

### Message Format

Each line in `bridge-chat.jsonl` is a JSON object:

```json
{"sender": "desktop", "level": 10, "text": "Starting deployment pipeline...", "ts": "2026-06-24T14:30:00Z"}
{"sender": "vps", "level": 20, "text": "Pipeline received. Executing step 1...", "ts": "2026-06-24T14:30:02Z"}
{"sender": "human", "level": 5, "text": "Hold deployment — I need to review the config first", "ts": "2026-06-24T14:30:05Z"}
```

### Priority Levels

| Level | Meaning | Example |
|:-----:|---------|---------|
| 0-9 | Normal | Routine work, progress updates |
| 10-19 | Important | Pipeline events, state changes |
| 20-29 | Critical | Failures, blockers, escalations |
| 30+ | Human override | Direct human instruction |

### Conversation Mirroring

Each agent mirrors its Telegram conversation to the bridge:

```python
# Pseudocode for conversation mirroring
def on_telegram_message(msg):
    bridge_entry = {
        "sender": AGENT_NAME,
        "level": infer_priority(msg),
        "text": msg.text,
        "ts": current_timestamp()
    }
    append_to_bridge(bridge_entry)
```

The other agent polls the bridge file and reacts accordingly.

## 6. Usage

```bash
# Load the skill and configure bridge
hermes -s three-agent-bridge "Set up bridge at /mnt/shared/hermes/bridge-chat.jsonl as desktop agent"

# Send a message to the other agent
hermes -s three-agent-bridge "Send to vps: deploy the latest release candidate"

# Check bridge for pending messages from the other agent
hermes -s three-agent-bridge "Check bridge for messages since last read"
```

## 7. CorpusIQ Use Cases

| Use Case | Why This Protocol |
|----------|-------------------|
| **Mac Mini + Hermes server coordination** | Desktop Hermes (Mac Mini) syncs with VPS Hermes (cloud) — CorpusIQ's exact architecture |
| **Multi-profile state sharing** | CorpusIQ growth agent profile shares state with other profiles via bridge |
| **Cron job coordination** | Prevent two agents running the same cron simultaneously |
| **Escalation chain** | Desktop escalates to VPS agent, VPS escalates to human via priority levels |
| **Session handoff** | Bridge file serves as shared context between agent profiles |

## 8. Pitfalls (From Real-World Deployment)

- **Symlinked bridge files:** If the bridge is a symlink, `tail` follows it but `cp` replaces it — use `cp -a` to preserve.
- **SSH key expiry:** SSH-based polling breaks when keys expire. Use certificate-based auth or keychain.
- **Polling vs push:** 2-second polling on SSH creates ~43K SSH connections/day. Consider Syncthing for lower overhead.
- **File locking:** Simultaneous writes can corrupt the JSONL file. Use atomic writes (write to temp, rename) on both sides.
- **Message ordering:** Two agents writing concurrently can interleave messages. Accept near-real-time, not perfect ordering.
- **Bridge file growth:** No built-in rotation. Add a cron to archive and rotate when file exceeds 10MB.

## 9. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Bridge file not updating | Filesystem permissions | Ensure both agents can write; check `ls -la` on the bridge file |
| Agent sees old messages | Polling interval too slow | Reduce `poll_interval` from 2s to 1s |
| SSH polling drops connection | SSH timeout or network blip | Add `ServerAliveInterval 5` to SSH config |
| Syncthing not syncing | Device not connected | Check Syncthing UI for device status; restart syncthing |
| Duplicate responses | Both agents respond to same bridge entry | Add `acknowledged_by` field to prevent double-handling |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 24 Discovery](/hermes/skills/marketplace/new-june24-2026/) →*
