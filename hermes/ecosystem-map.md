---
title: Hermes Ecosystem Map
description: Visual map of the entire Hermes Agent ecosystem  --  121+ repos, 14 categories, all connections visualized.
---

# Hermes Ecosystem Map

Visual map of the entire Hermes Agent ecosystem  --  every repository, category, and relationship.

## System Architecture

```mermaid
graph TB
    CORE[NousResearch/hermes-agent<br/>⭐195K · Core Framework]

    subgraph OFFICIAL[Official Resources]
        SELF[hermes-agent-self-evolution<br/>⭐4.1K]
        PAPERCLIP[hermes-paperclip-adapter<br/>⭐1.6K]
        AUTONOVEL[autonovel<br/>⭐1.1K]
        NEMO[NVIDIA/NemoClaw<br/>⭐21K]
    end

    subgraph DOCS[Documentation]
        ORANGE[Orange Book<br/>⭐4.4K]
        LEARN[27-Chapter Tutorial<br/>⭐153]
        MUDRI[Community Docs<br/>⭐58]
        OFFICIAL_DOCS[Official Docs<br/>hermes-agent.nousresearch.com]
    end

    subgraph UI[Interfaces]
        WEBUI[hermes-webui<br/>⭐14.5K]
        DESKTOP[hermes-desktop<br/>⭐12K]
        STUDIO[hermes-studio<br/>⭐8K]
        WORKSPACE[hermes-workspace<br/>⭐5.7K]
        CLAWPANEL[clawpanel<br/>⭐2.8K]
        SCARF[scarf macOS<br/>⭐629]
    end

    subgraph MEMORY[Memory Systems]
        CLAUDEMEM[claude-mem<br/>⭐83K]
        GBRAIN[gbrain<br/>⭐23K]
        EVEROS[EverOS<br/>⭐7.5K]
        MNEMOSYNE[mnemosyne<br/>⭐1.2K]
        MEMTRACE[memtrace<br/>⭐193]
    end

    subgraph MCP[MCP & Integrations]
        CORPUSIQ_MCP[CorpusIQ MCP<br/>53 tools · 37+ platforms]
        KINDLY[Kindly Search<br/>⭐345]
        KAGI[Kagi MCP<br/>⭐137]
        ANUBIS[Anubis MCP<br/>⭐147]
        CLAWROUTER[ClawRouter<br/>⭐12]
    end

    subgraph SKILLS[Skills]
        MARKETING[Marketing Skills<br/>45+ skills]
        FACTORY[Skill Factory<br/>⭐381]
        KANBAN[hermes-kanban<br/>⭐252]
        GUARD[skillguard]
        SUPERPOWERS[superpowers-zh<br/>⭐5.5K]
        AGENCY[agency-agents-zh<br/>⭐15K]
    end

    subgraph DEPLOY[Deployment]
        PANEL[1Panel<br/>⭐36K]
        OPERATOR[K8s Operator<br/>⭐13]
        AUTONOMOUS[Autonomous Server<br/>⭐14]
        LANGBOT[LangBot<br/>⭐16K]
    end

    subgraph RESEARCH[Research & Benchmarks]
        PAWBENCH[PawBench<br/>⭐59]
        HERMESBENCH[HermesBench<br/>⭐6]
        METAHARNESS[Meta-Harness]
    end

    subgraph COMMUNITY[Community]
        AWESOME_NYK[awesome-hermes-agent<br/>⭐4K]
        AWESOME_SAMUR[awesome-hermes-agent<br/>⭐1.7K]
        USECASES[awesome-hermes-usecases<br/>⭐101]
        DISCORD[Discord Community<br/>10K+ members]
        REDDIT[r/hermesagent]
    end

    subgraph CORPUSIQ_HUB[CorpusIQ Hermes Hub]
        ECOSYSTEM[Ecosystem Directory<br/>121+ repos]
        ARCHITECTURE[Architecture Guide]
        KNOWLEDGE[Memory Guide]
        CRONS[Cron Reference]
        SETUP[Setup Guide]
        MCP_GUIDE[MCP Guide]
    end

    CORE --> OFFICIAL
    CORE --> DOCS
    CORE --> UI
    CORE --> MEMORY
    CORE --> MCP
    CORE --> SKILLS
    CORE --> DEPLOY
    CORE --> RESEARCH
    CORE --> COMMUNITY

    CORPUSIQ_HUB --> CORE
    CORPUSIQ_HUB --> OFFICIAL
    CORPUSIQ_HUB --> MEMORY
    CORPUSIQ_HUB --> MCP
    CORPUSIQ_HUB --> SKILLS
    CORPUSIQ_HUB --> DEPLOY
    CORPUSIQ_HUB --> RESEARCH
    CORPUSIQ_HUB --> COMMUNITY
```

## Category Distribution

```mermaid
pie title Repos by Category
    "Core & Official" : 5
    "Documentation" : 8
    "Community Lists" : 12
    "UI & Dashboards" : 8
    "Memory & Knowledge" : 12
    "MCP & Integrations" : 8
    "Skills & Plugins" : 15
    "Orchestration" : 8
    "Deployment" : 10
    "Security" : 5
    "Research" : 12
    "Content & Media" : 6
    "Platform-Specific" : 12
    "Specialized" : 8
```

## Star Distribution

```mermaid
xychart-beta
    title "Stars by Category (log scale)"
    x-axis ["Core", "Memory", "UI", "Orch.", "Deploy", "Skills", "Research"]
    y-axis "Stars (log)" 0 --> 200000
    bar [195064, 82700, 14540, 61663, 35898, 15046, 4116]
```

## Master Index

| # | Repository | Stars | Category |
|---|-----------|-------|----------|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 195,064 | Core |
| 2 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 102,447 | Orchestration |
| 3 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 82,700 | Memory |
| 4 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | 65,835 | UI |
| 5 | [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 61,663 | Orchestration |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 50,162 | Specialized |
| 7 | [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | 47,420 | Orchestration |
| 8 | [1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel) | 35,898 | Deployment |
| 9 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | 28,359 | Orchestration |
| 10 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | 22,991 | Memory |

[Full 121+ repo directory →](/hermes/ecosystem.md)

## Data Flow

```mermaid
graph LR
    GITHUB[GitHub API] -->|nightly search| DISCOVER[Discovery Engine]
    DISCOVER -->|score + categorize| SCORE[Scoring System]
    SCORE -->|>=70| AUTO[Auto-Approved]
    SCORE -->|<70| PENDING[Pending Review]

    COMMUNITY_SUBMIT[Community Submissions] -->|issue template| INTAKE[Intake Workflow]
    INTAKE -->|score| SCORE

    AUTO --> APPROVED_DB[(Approved DB)]
    PENDING -->|manual review| APPROVED_DB
    PENDING -->|rejected| REJECTED_DB[(Rejected DB)]

    APPROVED_DB -->|auto-update| ECOSYSTEM_MD[ecosystem.md]
    APPROVED_DB -->|auto-update| CONTRIBUTORS[contributors.md]

    REJECTED_DB -->|log reason| REVIEW_LOG[review_log.json]
```

## How It Works

1. **Nightly Discovery (10 PM - 2 AM AZ):** The discovery engine searches GitHub across 20 query categories for new Hermes-related repos.

2. **Automated Scoring:** Each repo is scored 0-100 on: relevance, quality, activity level, documentation, adoption, and uniqueness.

3. **Auto-Approval:** Repos scoring 70+ are automatically added to the ecosystem.

4. **Manual Review:** Repos scoring 50-69 are prioritized for review. Repos scoring 30-49 enter the review queue.

5. **Community Submissions:** Anyone can submit a repo via the [GitHub issue template](https://github.com/CorpusIQ/corpusiq-docs/issues/new?template=submit-repo.yml). Submissions are scored and processed within 48 hours.

6. **Database Sync:** All additions update the ecosystem.md directory, contributors page, and master index automatically.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
