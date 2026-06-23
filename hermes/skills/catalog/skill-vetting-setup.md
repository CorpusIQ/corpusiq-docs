---
title: Skill Vetting Setup Guide
description: Install NVIDIA SkillSpector-based security vetting for Hermes skills  --  scan-before-install, risk gating, marketplace catalog, and weekly re-audits
---

# Skill Vetting  --  Setup Guide

**Skill Vetting** automatically vets external AI agent skills with [NVIDIA SkillSpector](https://github.com/NVIDIA/skillspector) before installation. Scan for vulnerabilities, gate on risk score, maintain a catalog of vetted skills, and run weekly re-audits.

By [SoCalStreet/skill-vetting](https://github.com/SoCalStreet/skill-vetting).

---

## 1. Prerequisites

- **Hermes Agent** installed and running
- **Python 3.12+** with `uv` package manager
- Git

---

## 2. Install NVIDIA SkillSpector

SkillSpector is the vulnerability scanning engine. Install it first:

```bash
git clone https://github.com/NVIDIA/skillspector.git ~/skillspector
cd ~/skillspector
uv venv .venv --python 3.12 && source .venv/bin/activate
make install

# Make available system-wide
sudo bash -c 'cat > /usr/local/bin/skillspector << '"'"'EOF'"'"'
#!/bin/bash
exec ~/skillspector/.venv/bin/skillspector "$@"
EOF'
sudo chmod +x /usr/local/bin/skillspector
```

Verify:

```bash
skillspector --version
```

---

## 3. Install Skill Vetting

### Option A: Via Hermes skills CLI

```bash
hermes skills install https://github.com/SoCalStreet/skill-vetting/SKILL.md
```

### Option B: Manual clone

```bash
git clone https://github.com/SoCalStreet/skill-vetting.git ~/.hermes/skills/security/skill-vetting
```

---

## 4. Set Up Weekly Audit Cron (Optional)

Automatically re-scan all installed skills every Monday at noon:

```bash
hermes cron create "0 12 * * 1" \
  --prompt "Run the skill-vetting periodic audit: scan all installed skills at ~/.hermes/skills/ and report new findings to Telegram" \
  --skill skill-vetting \
  --toolsets terminal
```

---

## 5. Capabilities

- **Scan-before-install enforcement**  --  The skill intercepts `hermes skills install` and runs SkillSpector first
- **64 vulnerability patterns** across 16 categories (static analysis)
- **Risk gating**  --  Auto-proceed on low scores, require approval on medium, refuse on high
- **External marketplace catalog**  --  5 marketplaces mapped (SkillsLLM, mcpservers.org, VoltAgent, +2)
- **Weekly audit cron**  --  Re-scans all installed skills, alerts on new findings
- **Vetting log**  --  Every scan logged to JSONL for audit trail

---

## 6. CorpusIQ Use Cases

- **Skills catalog curation**  --  Vet every new skill before adding to the CorpusIQ marketplace
- **Cron safety**  --  Ensure automated discovery skills don't introduce vulnerabilities
- **Client deployments**  --  Verify skills before installing in customer Hermes environments

---

## 7. Verification

After installation:

```bash
# Check skill is loaded
hermes skills list | grep skill-vetting

# Run a manual scan on a skill directory
skillspector scan ~/.hermes/skills/some-skill/
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Skill Vetting Repo](https://github.com/SoCalStreet/skill-vetting) →*
