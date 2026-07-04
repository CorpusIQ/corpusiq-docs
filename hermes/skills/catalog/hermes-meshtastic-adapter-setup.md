---
title: "Hermes Meshtastic Adapter — LoRa Mesh Integration Setup"
description: "Set up the Hermes Meshtastic Adapter (4⭐) to connect your Hermes agent to a Meshtastic LoRa mesh network for off-grid communication."
skill_name: hermes-meshtastic-adapter
category: iot-hardware
difficulty: Medium
platforms: [Linux]
hardware_required: true
---

# Hermes Meshtastic Adapter — Full Setup Guide

**Repo:** [amscotti/hermes-meshtastic-adapter](https://github.com/amscotti/hermes-meshtastic-adapter) | ⭐ 4
**Author:** amscotti | **Language:** Python
**License:** MIT

The Hermes Meshtastic Adapter is a Hermes Agent plugin that bridges your agent to a Meshtastic LoRa mesh network. It receives plain-text messages from the mesh and can send responses back — enabling Hermes interaction over long-range, low-power radio networks that operate without cell towers or WiFi.

---

## Prerequisites

### Hardware
- Meshtastic-compatible device (LilyGo T-Beam, Heltec LoRa 32, RAK Wireless, etc.)
- USB connection to your Hermes host machine

### Software
- Python 3.11+
- Hermes Agent
- Meshtastic Python library

---

## Installation

```bash
git clone https://github.com/amscotti/hermes-meshtastic-adapter.git
cd hermes-meshtastic-adapter
pip install -r requirements.txt
```

---

## Hardware Setup

### 1. Flash Meshtastic Firmware

Follow the [Meshtastic Flashing Guide](https://meshtastic.org/docs/getting-started/flashing-firmware/) for your device.

### 2. Connect Device

Connect your Meshtastic device via USB. Verify it's detected:

```bash
ls /dev/ttyUSB*    # Linux
ls /dev/cu.*       # macOS
```

### 3. Configure Meshtastic

Using the Meshtastic Python CLI:

```bash
pip install meshtastic
meshtastic --info    # Verify connection

# Set a short name for your node
meshtastic --set-owner "Hermes-Node"

# Configure channel (must match your mesh)
meshtastic --setchan name "HermesMesh" --setchan psk "base64:your-preshared-key"
```

---

## Configuration

### Adapter Config

Edit `config.yaml`:

```yaml
meshtastic:
  port: "/dev/ttyUSB0"          # Serial port for device
  # or use TCP for network-connected devices:
  # host: "192.168.1.100"
  
hermes:
  message_format: "plain"        # "plain" or "json"
  respond_to_all: false          # Only respond to messages prefixed with "Hermes:"
  response_prefix: "🤖 "        # Prefix for all bot responses
  max_message_length: 200        # Meshtastic has message size limits
  
filters:
  allowed_nodes: []              # Empty = respond to all. List node IDs to restrict.
  blocked_nodes: []              # Never respond to these nodes
  require_prefix: "Hermes:"      # Messages must start with this to trigger response
  
logging:
  file: "meshtastic_adapter.log"
  level: "INFO"
```

### Hermes Integration

Register as a Hermes plugin:

```yaml
# In ~/.hermes/config.yaml
plugins:
  meshtastic:
    path: "/path/to/hermes-meshtastic-adapter"
    enabled: true
    config:
      port: "/dev/ttyUSB0"
```

---

## Usage

### Running Standalone

```bash
# Start the adapter
python3 adapter.py

# Output:
# [INFO] Connected to Meshtastic device on /dev/ttyUSB0
# [INFO] Listening for messages on channel 'HermesMesh'
# [INFO] Node ID: !a1b2c3d4
```

### Message Flow

1. User sends a text message from their Meshtastic device
2. Adapter receives it via the mesh
3. If message matches prefix filter, it's forwarded to Hermes
4. Hermes processes and responds
5. Adapter sends response back over the mesh

```
User (LoRa Device) --[radio]--> Mesh --[radio]--> Your Node --[USB]--> Adapter --> Hermes Agent
                                                                              |
User (LoRa Device) <--[radio]-- Mesh <--[radio]-- Your Node <--[USB]-- Adapter <--+
```

### Example Interaction

**User (on Meshtastic device):**
```
Hermes: What's the weather forecast for tomorrow?
```

**Hermes (response over mesh):**
```
🤖 Tomorrow: Partly cloudy, high of 72°F, low of 55°F. 15% chance of rain.
```

---

## Integration with Hermes Agent

### As a Plugin

The adapter registers with Hermes as a plugin, making it available as a tool:

```python
# From within Hermes:
# The adapter exposes these tools:
# - meshtastic_send(message, node_id=None)
# - meshtastic_broadcast(message)
# - meshtastic_status()
```

### Use Cases

| Use Case | Description |
|----------|-------------|
| Off-grid assistant | Query your Hermes agent from remote locations without cell service |
| Field research | Send observations, get analysis back over mesh |
| Emergency comms | Agent can relay information during network outages |
| Sensor monitoring | Mesh-connected sensors report to Hermes for analysis |
| Community mesh | Shared Hermes access for a local mesh network |

---

## Troubleshooting

### "Device not found on /dev/ttyUSB0"

```bash
# Check connected USB devices
lsusb
dmesg | grep -i usb

# Try different port
meshtastic --port /dev/ttyACM0 --info
```

### "No messages received"

1. Verify channel name and PSK match your mesh
2. Check that your node is in range of at least one other node
3. Ensure the region/frequency matches (US: 915MHz, EU: 868MHz)

### "Messages are truncated"

Meshtastic has a ~200 byte payload limit. The adapter splits long messages automatically, but very long Hermes responses will be trimmed:
```yaml
hermes:
  max_message_length: 180  # Leave room for prefix + metadata
```

### "Response prefix not working"

Check the exact prefix in config — it's case-sensitive:
```yaml
filters:
  require_prefix: "Hermes:"  # Must match exactly
```

---

## Range & Performance

| Environment | Typical Range |
|-------------|:------------:|
| Urban (buildings) | 1-3 km |
| Suburban | 3-8 km |
| Rural / open | 10-20 km |
| Elevated / line-of-sight | 50+ km |

Factors affecting range: antenna quality, elevation, terrain, weather, interference.

---

## Alternatives

| Tool | Range | Power | Notes |
|------|:-----:|:-----:|-------|
| Meshtastic LoRa | 1-50km | Battery | Off-grid, no infrastructure |
| WiFi | 50m | Wall power | Requires network |
| Bluetooth | 10m | Battery | Short range, low power |
| Satellite (Iridium) | Global | Battery | Expensive, high latency |

---

*Guide last updated: July 4, 2026 | [Repo](https://github.com/amscotti/hermes-meshtastic-adapter) | [Report issue](https://github.com/CorpusIQ/corpusiq-docs/issues)*
