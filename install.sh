#!/bin/bash
# CorpusIQ AI Agent Installer — one command, everything you need.
# curl -sL https://corpusiq.io/install | bash

set -e

echo "🤖 CorpusIQ AI Agent Installer"
echo "================================"
echo ""

# 1. Install agency-agents (232 AI personalities)
if [ ! -d "$HOME/agency-agents" ]; then
    echo "📦 Installing agency-agents (232 agents, 16 divisions)..."
    git clone --depth 1 https://github.com/msitarzewski/agency-agents.git "$HOME/agency-agents" 2>/dev/null
    echo "   ✅ agency-agents installed to $HOME/agency-agents"
else
    echo "   ✅ agency-agents already installed"
fi

# 2. Install Hermes ecosystem (341+ repos)
if [ ! -d "$HOME/corpusiq-docs" ]; then
    echo "📦 Installing CorpusIQ Hermes ecosystem (341+ repos)..."
    git clone --depth 1 https://github.com/CorpusIQ/corpusiq-docs.git "$HOME/corpusiq-docs" 2>/dev/null
    echo "   ✅ CorpusIQ ecosystem installed to $HOME/corpusiq-docs"
else
    echo "   ✅ CorpusIQ ecosystem already installed"
fi

# 3. Run agency-agents install script if available
if [ -f "$HOME/agency-agents/scripts/install.sh" ]; then
    echo ""
    echo "🔧 Detected agency-agents installer. Run:"
    echo "   cd $HOME/agency-agents && ./scripts/install.sh"
fi

echo ""
echo "================================"
echo "✅ Installation complete!"
echo ""
echo "📁 agency-agents:  $HOME/agency-agents  (232 agents)"
echo "📁 corpusiq-docs:  $HOME/corpusiq-docs  (341+ repos)"
echo ""
echo "🔗 Connect agents to your real data:"
echo "   https://corpusiq.io/register"
echo ""
echo "📖 Agent marketplace:"
echo "   https://corpusiq.io/docs/hermes/agent-marketplace/"
