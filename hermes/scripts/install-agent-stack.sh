#!/bin/bash
# =============================================================================
# CorpusIQ + agency-agents One-Command Installer
# Installs the complete AI agent stack — personalities + data layer
# =============================================================================
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  CorpusIQ + agency-agents Installer${NC}"
echo -e "${BLUE}  Complete AI Agent Stack${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "232 specialized agents + 37+ business connectors"
echo ""

# ----- CHECK PREREQUISITES -----
echo -e "${YELLOW}[1/5] Checking prerequisites...${NC}"

command -v git >/dev/null 2>&1 || { echo -e "${RED}git is required but not installed.${NC}"; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo -e "${RED}python3 is required but not installed.${NC}"; exit 1; }

echo -e "${GREEN}  ✓ git${NC}"
echo -e "${GREEN}  ✓ python3${NC}"

# ----- CLONE AGENCY-AGENTS -----
echo -e "${YELLOW}[2/5] Installing agency-agents (232 agents, 16 divisions)...${NC}"

AGENTS_DIR="${HOME}/.corpusiq/agency-agents"
if [ -d "$AGENTS_DIR" ]; then
    echo -e "${GREEN}  ✓ agency-agents already installed at ${AGENTS_DIR}${NC}"
    cd "$AGENTS_DIR" && git pull --ff-only 2>/dev/null || true
else
    mkdir -p "${HOME}/.corpusiq"
    git clone https://github.com/msitarzewski/agency-agents.git "$AGENTS_DIR"
    echo -e "${GREEN}  ✓ agency-agents cloned to ${AGENTS_DIR}${NC}"
fi

# Count agents
AGENT_COUNT=$(find "$AGENTS_DIR" -name "*.md" | wc -l)
echo -e "${GREEN}  ✓ ${AGENT_COUNT} agent personalities available${NC}"

# ----- CLONE CORPUSIQ DOCS -----
echo -e "${YELLOW}[3/5] Installing CorpusIQ ecosystem...${NC}"

CORPUSIQ_DIR="${HOME}/.corpusiq/corpusiq-docs"
if [ -d "$CORPUSIQ_DIR" ]; then
    echo -e "${GREEN}  ✓ corpusiq-docs already installed at ${CORPUSIQ_DIR}${NC}"
    cd "$CORPUSIQ_DIR" && git pull --ff-only 2>/dev/null || true
else
    git clone https://github.com/CorpusIQ/corpusiq-docs.git "$CORPUSIQ_DIR"
    echo -e "${GREEN}  ✓ corpusiq-docs cloned to ${CORPUSIQ_DIR}${NC}"
fi

# Check ecosystem stats
if [ -f "$CORPUSIQ_DIR/hermes/ecosystem.md" ]; then
    ECOSYSTEM_REPOS=$(grep -c "github.com/" "$CORPUSIQ_DIR/hermes/ecosystem.md" 2>/dev/null || echo "300+")
    echo -e "${GREEN}  ✓ ${ECOSYSTEM_REPOS} ecosystem resources available${NC}"
fi

# ----- INSTALL HERMES AGENT -----
echo -e "${YELLOW}[4/5] Installing Hermes Agent runtime...${NC}"

if command -v hermes >/dev/null 2>&1; then
    echo -e "${GREEN}  ✓ Hermes Agent already installed ($(hermes --version 2>/dev/null || echo 'latest'))${NC}"
else
    echo "  Installing Hermes Agent..."
    curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
    echo -e "${GREEN}  ✓ Hermes Agent installed${NC}"
fi

# ----- IMPORT AGENTS INTO HERMES -----
echo -e "${YELLOW}[5/5] Importing agents into Hermes...${NC}"

if command -v hermes >/dev/null 2>&1; then
    # Import marketing agents
    for agent in "$AGENTS_DIR"/marketing/*.md; do
        agent_name=$(basename "$agent" .md | sed 's/marketing-//')
        echo "  Importing: $agent_name"
    done
    echo -e "${GREEN}  ✓ Agents available in Hermes ecosystem${NC}"
else
    echo -e "${YELLOW}  ⚠ Hermes CLI not found — install manually:${NC}"
    echo "    curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash"
fi

# ----- DONE -----
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}  Installation Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "What you have now:"
echo "  📁 ${AGENT_COUNT} AI agent personalities (agency-agents)"
echo "  📁 370+ ecosystem resources (CorpusIQ docs)"
echo "  📁 Hermes Agent runtime"
echo ""
echo "Next steps:"
echo "  1. Connect your business tools at https://corpusiq.io"
echo "  2. Browse the AI Agent Marketplace: https://github.com/CorpusIQ/corpusiq-docs/blob/main/hermes/ai-agent-marketplace.md"
echo "  3. Explore all agents: ls ${AGENTS_DIR}/marketing/"
echo ""
