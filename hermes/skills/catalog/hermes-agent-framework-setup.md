---
title: "Hermes Agent Framework — Core Nous Research Agent Framework Setup"
description: "176+ installs. Guide to Nous Research's Hermes Agent framework with self-improving learning loops, three-layer memory, and automatic Skill creation. Setup guide for Hermes agents."
---

# Hermes Agent Framework — Setup Guide

**Source:** [aradotso/ai-agent-skills](https://skills.sh/aradotso/ai-agent-skills/hermes-agent-framework) (176+ installs)
**Category:** Hermes Agent / Core Framework
**Quality Tier:** 🟡 Beta

Expert knowledge for working with Hermes Agent, the open-source AI Agent framework by Nous Research featuring built-in self-improving learning loops, three-layer memory system (episodic, semantic, procedural), and automatic Skill creation and evolution. Differs from traditional agents (OpenClaw/Claude Code) by implementing learning-as-a-first-class-feature.

---

## Installation

```bash
npx skills add aradotso/ai-agent-skills --skill hermes-agent-framework
```

### Core Hermes Agent Setup

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | 3.10+ |
| **API Key** | OpenAI, Anthropic, or compatible provider |
| **Memory Path** | `~/.hermes/memory` (auto-created) |
| **Skills Path** | `~/.hermes/skills` (auto-created) |

---

## Key Capabilities

### Three-Layer Memory System
- **Episodic**: Conversation history — stores user/agent interactions with retrieval
- **Semantic**: Knowledge base — searchable vector store for facts, patterns, and domain knowledge
- **Procedural**: Skills — reusable procedures that auto-evolve based on usage and feedback

### Self-Improving Learning Loop
Configure automatic learning: reflection interval (every N interactions), skill creation threshold (after N similar tasks), and feedback sensitivity. Agent detects patterns, creates Skills for repeated tasks, and improves existing Skills based on human feedback.

### Automatic Skill Creation
Skills are generated from repeated interaction patterns. Define via Python SDK or YAML files. Includes versioning, usage tracking, and auto-improvement toggles.

### Multi-Agent Orchestration
`AgentOrchestrator` supports sequential, parallel, and hierarchical coordination strategies. Create specialized agents (code expert, reviewer, doc writer) and dispatch complex workflows.

### Extensible Tool System
Built-in tools: WebSearch, CodeExecutor, FileSystem, APICaller. Custom tools defined via `Tool` base class with parameter validation.

---

## Quick Start

```python
from hermes_agent import HermesAgent, MemoryConfig, LearningConfig

agent = HermesAgent(
    model="gpt-4-turbo",
    memory_config=MemoryConfig(
        episodic_enabled=True,
        semantic_enabled=True,
        procedural_enabled=True,
        memory_path="~/.hermes/memory"
    ),
    learning_config=LearningConfig(
        enable_auto_learning=True,
        reflection_interval=5,
        skill_creation_threshold=3
    )
)

response = agent.chat("Help me analyze this Python code")
```

### CLI Usage

```bash
hermes chat "What's the weather today?"
hermes chat --skill code-reviewer "Review my Python script"
hermes memory list
hermes skills list
```

---

## Verification

```bash
# Verify installation
python -c "from hermes_agent import HermesAgent; print('OK')"

# Start interactive mode
python -m hermes_agent

# Check memory stats
python -c "from hermes_agent import HermesAgent; a = HermesAgent(model='gpt-4-turbo'); print(a.memory.stats())"
```

---

## Notes

- Start with conservative learning settings — higher thresholds prevent over-generalization
- Provide feedback regularly — the learning loop improves proportionally with human input quality
- Review auto-generated Skills before heavy use — inspect and refine before production reliance
- Monitor token usage — learning loops can increase API calls
- Version control your Skills in git for reproducibility
- Separate agents by role using orchestration for complex workflows

---
