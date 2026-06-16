# Cloud VPS — Always-On Budget Deployment

Run Hermes 24/7 on a $5–20/month cloud VPS. No hardware to maintain, no electricity bill to worry about, and it stays online even when your laptop is off. Perfect for email monitoring, cron jobs, and lightweight autonomous agents.

## Provider Comparison

| Provider | Cheapest Plan | RAM | CPU | Best For |
|---|---|---|---|---|
| **Hetzner** | €4.51/mo (CX22) | 4GB | 2 vCPU | Best value in Europe |
| **DigitalOcean** | $6/mo (Basic) | 1GB | 1 vCPU | Good docs, global regions |
| **AWS Lightsail** | $5/mo | 1GB | 1 vCPU | AWS ecosystem integration |
| **Vultr** | $6/mo | 1GB | 1 vCPU | Many regions, hourly billing |
| **Linode** | $5/mo | 1GB | 1 vCPU | Simple, reliable |

**Recommendation:** Hetzner CX22 (4GB RAM, €4.51/mo) gives you enough memory for Hermes + memory stack without swapping. For lightweight cron-only usage, a 1GB droplet works.

## Step 1: Provision the VPS

All commands assume Ubuntu 24.04 LTS.

```bash
# After creating your VPS, SSH in
ssh root@your-server-ip

# Create a non-root user
adduser hermes
usermod -aG sudo hermes
su - hermes
```

## Step 2: Install Dependencies

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nodejs npm git curl

# Node 20+ (for MCP servers)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

node --version  # Should be 20+
```

## Step 3: Install Hermes

```bash
pip install hermes-agent

hermes profile create cloud-agent
hermes profile use cloud-agent
```

## Step 4: Configure Cloud Models

VPS instances don't have GPUs. Use API-based models exclusively.

```bash
# OpenRouter — access to 200+ models
hermes config set providers.openrouter.api_key "your-key"

# Set primary model (cost-effective)
hermes config set model.default openrouter/qwen/qwen3-235b-a22b:free

# Set fallback for harder tasks
hermes config set model.fallback openrouter/anthropic/claude-sonnet-4
```

**Note:** `qwen/qwen3-235b-a22b:free` on OpenRouter costs $0.000/token — effectively free for light usage. Claude via OpenRouter runs ~$3/million input tokens.

## Step 5: Docker Option (Alternative)

For a fully containerized VPS deployment:

```bash
# Install Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker hermes

# Run Hermes in Docker
docker run -d --name hermes-agent \
  -v ~/.hermes:/home/hermes/.hermes \
  -e OPENROUTER_API_KEY="your-key" \
  --restart unless-stopped \
  nousresearch/hermes-agent:latest
```

For a full Docker setup with compose, [see the Docker guide](docker.md).

## Step 6: Systemd Service

Make Hermes survive reboots:

```bash
sudo tee /etc/systemd/system/hermes-gateway.service << 'EOF'
[Unit]
Description=Hermes Agent Gateway
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=hermes
ExecStart=/home/hermes/.local/bin/hermes gateway run
Restart=always
RestartSec=10
Environment=HOME=/home/hermes

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now hermes-gateway
sudo systemctl status hermes-gateway
```

## Step 7: Cron Persistence

Your VPS is always on — make it work 24/7:

```bash
# Email monitoring
hermes cron create \
  --name "email-watch" \
  --prompt "Check inbox for unread messages. Summarize. Silent if empty." \
  --schedule "*/15 * * * *"

# Daily health check
hermes cron create \
  --name "health-check" \
  --prompt "Verify all services are running. Check disk space. Report issues." \
  --schedule "0 8 * * *"

# Nightly cleanup
hermes cron create \
  --name "nightly-cleanup" \
  --prompt "Archive old logs. Clean temp files. Report disk usage." \
  --schedule "0 2 * * *"
```

## Step 8: Security Hardening

```bash
# Firewall — only allow SSH
sudo ufw allow 22/tcp
sudo ufw enable

# SSH key-only auth
# On your local machine:
ssh-copy-id hermes@your-server-ip

# Then on the VPS, disable password auth:
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart sshd

# Enable unattended security updates
sudo apt install unattended-upgrades
sudo dpkg-reconfigure unattended-upgrades
```

## Cost Breakdown

| Item | Monthly Cost |
|---|---|
| Hetzner CX22 (4GB RAM) | €4.51 |
| OpenRouter API (free models) | $0 |
| Honcho (free tier) | $0 |
| **Total** | **~$5/month** |

For heavier usage with Claude-level models: ~$15–25/month total.

## Monitoring

```bash
# Check Hermes status
hermes gateway status

# Check resource usage
htop
df -h

# View logs
journalctl -u hermes-gateway -f
```

---

*Next: [Docker Setup](docker.md) · [Production Cron Reference](/hermes/governance/scheduling/)*
