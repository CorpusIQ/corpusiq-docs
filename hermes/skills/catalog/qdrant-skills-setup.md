---
title: "Qdrant Skills - Vector Search, Retrieval and Memory Setup"
description: "Qdrant's official agent skills: 14.4K combined installs across 34 listings. Retrieval quality, scaling, monitoring, and hybrid search guidance."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/qdrant-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "qdrant", "vector search", "rag", "embeddings"]
---

# Qdrant Skills - Setup Guide

**Source:** [qdrant/skills](https://www.skills.sh/qdrant/skills) via skills.sh - 14.4K combined installs across 34 indexed listings; snapshot 2026-10-27 (Oct 27 sweep)

**GitHub:** [qdrant/skills](https://github.com/qdrant/skills) - 265 stars, Apache-2.0, branch main, not archived, 34 `SKILL.md` files: 33 under `skills/` nested up to four levels deep, plus the `qdrant-advisor` meta-skill under `meta/`

**Category:** Vector search, retrieval and agent memory infrastructure

**Quality Tier:** 🟡 Beta - first-party Qdrant repository under Apache-2.0 with 265 stars, and all 34 indexed listings have a matching `SKILL.md` in the current tree, but the README carries its own active development disclaimer

Qdrant maintains this repository as the official agent skill set for the vector database it ships. It is not a general purpose collection. Every skill covers a decision that determines whether retrieval works: quantization and memory tiers, shard and replica counts, tenant isolation, hybrid fusion, embedding model migration, upgrade order. The layout is a hierarchy rather than a flat list. A hub skill such as `qdrant-scaling` names its own sub-skills and links to them, a leaf skill ends with a `What NOT to Do` section, and the README states the philosophy plainly: skills answer "when?" and "why?", documentation answers "how?".

For agents the retrieval angle is the practical one. Vector search is usually the layer under an agent's memory: a collection stores the embeddings the agent writes and reads back, and the quality of that round trip decides whether recalled context is relevant or merely similar. These skills treat that as an engineering problem with measurable inputs. `qdrant-search-quality` diagnoses bad results, scores recall against a golden set, and only then recommends hybrid search, fusion or reranking. `qdrant-sizing` and `qdrant-performance-optimization` size RAM, disk and shards before provisioning instead of after an out of memory crash.

Two properties matter for a self-hosted agent stack. Qdrant is Apache-2.0 and runs locally, in Docker, on your own Kubernetes, or as an embedded in-process shard through Qdrant Edge, so this skill set is usable with no Qdrant Cloud account and no database API key at all. `qdrant-deployment-options` exists specifically to make that choice explicit rather than defaulting to a hosted cluster.

## Installation

The README documents a single-skill path, a bundle path, a Claude Code plugin path and a clone path. The recommended one installs only the advisor, a meta-skill with no static content that loads the relevant guidance from `skills.qdrant.tech` at request time:

```bash
npx skills add qdrant/skills/meta/qdrant-advisor
```

The advisor is not part of the bundle, so the two commands are alternatives, not steps in a sequence. The full offline set:

```bash
npx skills add qdrant/skills
```

Claude Code adds the repository as a marketplace and installs the single plugin it declares:

```
/plugin marketplace add qdrant/skills
/plugin install qdrant@qdrant
```

The marketplace name and plugin name both read `qdrant`, which matches `.claude-plugin/marketplace.json` in the repository. Cursor installs from the Cursor Marketplace, or adds `qdrant/skills` manually as a Remote Rule (GitHub).

For Hermes and any other agent, clone and copy the directories you need:

```bash
git clone --depth 1 https://github.com/qdrant/skills.git
cp -R skills/qdrant-search-quality ~/.hermes/skills/qdrant-search-quality
cp -R skills/qdrant-scaling ~/.hermes/skills/qdrant-scaling
cp -R meta/qdrant-advisor ~/.hermes/skills/qdrant-advisor
```

Copy sub-skill directories along with their hub. Hub `SKILL.md` files navigate by relative link, so `qdrant-scaling/scaling-data-volume/vertical-scaling` only resolves if that directory came with it. The README's own agent table names `~/.claude/skills/` for Claude Code, `.cursor/skills/` for Cursor, `~/.config/opencode/skill/` for OpenCode, `~/.codex/skills/` for Codex and `~/.pi/agent/skills/` for Pi; Hermes uses its own skills directory and otherwise follows the same copy pattern.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| qdrant-search-quality | 1,793 | Diagnosing irrelevant or missing results: embedding model choice, search strategies, hybrid search and fusion, reranking, relevance feedback, and scoring recall against a golden set. |
| qdrant-clients-sdk | 1,792 | Client setup and snippet search across the Python, TypeScript, Rust, Go, .NET and Java SDKs. |
| qdrant-performance-optimization | 1,689 | Proactive tuning hub that routes to search speed, indexing performance or memory usage work based on the constraint you name. |
| qdrant-monitoring | 1,539 | Metrics and health: Prometheus scraping, Grafana, health probes, optimizer and cluster debugging, alerting and log centralization. |
| qdrant-scaling | 1,474 | Scaling decisions across data volume, QPS, latency and query volume, including horizontal versus vertical and retention windows. |
| qdrant-deployment-options | 1,456 | Choosing between local mode, Docker, self-hosted, Qdrant Cloud, Hybrid Cloud and the embedded Edge shard. |
| qdrant-model-migration | 1,443 | Switching embedding models without downtime, including dimension changes and running two models side by side for comparison. |
| qdrant-version-upgrade | 1,403 | Upgrade paths and compatibility guarantees: rolling upgrades, client versus server order, and what to check before jumping versions. |
| qdrant-advisor | 693 | A meta-skill with no static content that searches skills.qdrant.tech live and walks the skill hierarchy from the symptom you describe. |
| qdrant-edge | 283 | Building on the embedded shard: server sync, on-device BM25, snapshots, and what Edge ships versus what you implement yourself. |
| qdrant-multitenancy | 252 | Tenant isolation: payload partitioning, tiered multitenancy, and region-based data isolation through custom sharding. |

The remaining 23 indexed listings range from 5 to 176 installs: `qdrant-sizing` (176), `qdrant-migration-tool` (92), `qdrant-hybrid-cloud-setup` (76), `qdrant-minimize-latency` (41), `qdrant-managed-cloud-quickstart` (14), then the leaves of the four hub families at 10 to 13 installs each, and `qdrant-relevance-feedback` at 5. The leaves are the specific guidance the hubs point at: `qdrant-search-quality/diagnosis`, `qdrant-monitoring/debugging`, `qdrant-performance-optimization/memory-usage-optimization`, `qdrant-scaling/scaling-data-volume/tenant-scaling` and similar.

## Why This Matters for Hermes Agents

Retrieval failures do not raise errors. An agent with a badly configured collection returns confident answers built on weak matches, and nothing in the response signals that the recall was poor. `qdrant-search-quality` addresses that directly: it separates a diagnosis branch from a strategy branch, and it asks for a golden set and recall@k before accepting any tuning change as an improvement.

The sizing and performance skills close the other silent failure. `qdrant-sizing` opens by rejecting the shorthand estimate of points times dimensions times four bytes, then walks the components that actually consume memory, including the quantized copy stored alongside the original vectors, HNSW indexes, sparse vectors and payload indexes, plus roughly 20 percent headroom. An agent that skips this step provisions a cluster that is undersized on day one.

Trigger design is unusually good here. Descriptions are written as `Use when` plus the exact phrases a user says, such as "memory keeps climbing", "optimizer stuck" or "results are not relevant", which is what makes the right skill fire without a router. The hierarchy then keeps context small: the hub carries routing and the leaf carries the endpoints, metrics and thresholds.

For memory work specifically, the practical pairing is a self-hosted collection for what the agent stores and recalls, `qdrant-multitenancy` for isolation between users or tenants, and `qdrant-monitoring` for the metrics that reveal a growing footprint before a crash. None of that requires a cloud account.

## Usage

| You say | What happens |
|---|---|
| "Search results are irrelevant, what do I change first" | qdrant-search-quality routes to its diagnosis branch, checks model and chunk fit before any tuning, then proposes a golden set and recall@k measurement. |
| "How much RAM do I need for 50 million 1536-dimension vectors" | qdrant-sizing sizes each component separately, adds about 20 percent headroom, derives node count, and checks shard count against future growth. |
| "Queries got slow after a bulk upload" | qdrant-monitoring routes to its debugging leaf, which checks optimizer status and segment health before blaming search latency. |
| "We need to switch from OpenAI embeddings to another model with no downtime" | qdrant-model-migration describes the dual-vector path so old and new embeddings coexist during re-embedding. |
| "One customer's data is drowning the others" | qdrant-multitenancy picks payload partitioning, tiered multitenancy or custom sharding from the isolation and residency requirement. |
| "Can I jump from 1.15 to 1.18 and can we do it live" | qdrant-version-upgrade covers the upgrade path, rolling upgrade procedure and client versus server order. |
| "Get Qdrant running locally with no cloud account" | qdrant-deployment-options compares local mode, Docker and the embedded shard, and names the tradeoffs of each. |

## Verification

Every URL in this section returned HTTP 200 on 2026-10-27. Fetch the skill files before installing them and read the frontmatter and the leaf sections:

```bash
for p in skills/qdrant-search-quality/SKILL.md \
         skills/qdrant-scaling/SKILL.md \
         skills/qdrant-sizing/SKILL.md \
         skills/qdrant-multitenancy/SKILL.md \
         skills/qdrant-performance-optimization/SKILL.md \
         meta/qdrant-advisor/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/qdrant/skills/main/$p"
done
```

The ones worth reading in full before install, because they touch credentials, exposure or residency:

- https://raw.githubusercontent.com/qdrant/skills/main/meta/qdrant-advisor/SKILL.md (fetches remote guidance every session)
- https://raw.githubusercontent.com/qdrant/skills/main/skills/qdrant-managed-cloud-quickstart/SKILL.md (database API keys, strict mode, irreversible choices)
- https://raw.githubusercontent.com/qdrant/skills/main/skills/qdrant-multitenancy/SKILL.md (region pinning and data residency)

After install, confirm the layout rather than the count:

```bash
ls ~/.hermes/skills | grep qdrant
head -4 ~/.hermes/skills/qdrant-scaling/SKILL.md
```

Each directory should hold a `SKILL.md` whose frontmatter has `name` and `description`, and hub skills should also carry an `allowed-tools` line. A hub whose relative links 404 means the sub-skill directories were not copied with it. The public site at https://skills.qdrant.tech mirrors the same tree, so a page that exists there and not in your copy is a copy problem, not a missing skill.

## Security

skills.sh verdicts for the Gen Agent Trust Hub, Socket and Snyk auditors were not sampled for this fire, so every cell below reads Not checked. Open each skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| qdrant-search-quality | Not checked | Not checked | Not checked |
| qdrant-clients-sdk | Not checked | Not checked | Not checked |
| qdrant-performance-optimization | Not checked | Not checked | Not checked |
| qdrant-monitoring | Not checked | Not checked | Not checked |
| qdrant-scaling | Not checked | Not checked | Not checked |
| qdrant-deployment-options | Not checked | Not checked | Not checked |
| qdrant-model-migration | Not checked | Not checked | Not checked |
| qdrant-version-upgrade | Not checked | Not checked | Not checked |
| qdrant-advisor | Not checked | Not checked | Not checked |
| qdrant-edge | Not checked | Not checked | Not checked |
| qdrant-multitenancy | Not checked | Not checked | Not checked |

The risk that matters here is infrastructure access, not code execution. The skills are markdown with references, but they instruct an agent to operate a live database. Four observations from the files themselves:

- **Credentials.** `qdrant-managed-cloud-quickstart` states that every REST and gRPC request to Managed Cloud carries a database API key, that each key works only on the cluster it was created in and is shown once at creation, and that keys expire after 90 days by default unless an empty expiration is set. It also warns that keys keep working after their creator is removed from the account unless they are revoked. An agent following this skill can create and hold cluster credentials, so treat the key as a secret and revoke on offboarding.
- **Network exposure.** `qdrant-hybrid-cloud-setup` records that the default `ClusterIP` service is internal only with no API key, that exposing it through LoadBalancer, NodePort or Ingress requires configuring an API key as a Kubernetes secret, and that internal node-to-node gRPC on port 6335 is never protected by API key or TLS and must never be publicly reachable. Exposing a cluster without a key and leaving 6335 reachable are both on that skill's `What NOT to Do` list.
- **Irreversible and destructive operations.** The cloud quickstart's own framing is that some cluster choices cannot be undone, that free clusters are suspended after a week idle and deleted after four weeks, and that changing a collection's replication factor on Cloud causes shards to be replicated or dropped automatically, which is why manual replica changes are listed as a thing not to do. Backup and snapshot steps belong in the plan before any of these run.
- **Data residency.** `qdrant-multitenancy` states that geographic residency follows only if the cluster's nodes are actually in the target regions, and that Qdrant Cloud deploys a cluster in a single region with no managed multi-region. The quickstart adds that free Cloud Inference models run in the US even for EU-region clusters, so an EU residency requirement needs a paid model or embeddings computed before upload.

One more, specific to the advisor: it instructs the agent to fetch `skills.qdrant.tech` fresh every session and to ground its answer in what came back, and it explicitly tells the agent not to answer from memory. That is the correct posture for accuracy, and it also means remote text enters the agent's context on every Qdrant request. Treat fetched pages as reference data, not as instructions, and note the README caveat that the claude.ai web app cannot fetch the site on its own, so the URL has to be passed in the prompt there.

## Limitations

- Snapshot data, verified 2026-10-27: 14,404 combined installs across 34 indexed listings; 265 GitHub stars; Apache-2.0; branch main. Counts drift over time.
- The 34 indexed listings and the 34 `SKILL.md` files in the tree match one to one, but the shape is a hierarchy: 33 files under `skills/` (most of them sub-skills, not top-level directories) and one under `meta/`. Installing "the suite" installs a tree, not 34 independent tools.
- The README's Skills table documents 14 of the 34 listings. The other 20, including every leaf named in the table above, appear in the install index and in their own `SKILL.md` frontmatter; the use descriptions for those rows come from those files rather than the README.
- `qdrant-advisor` is deliberately excluded from the `npx skills add qdrant/skills` bundle, so the bundle and the advisor are separate installs with different update behaviour: the bundle goes stale, the advisor refetches from the site each session.
- The README carries its own disclaimer that the skills are under active development and that content and structure may change between versions. Pin a commit or copy into your own skills directory if you need reproducible behaviour.
- Hub `SKILL.md` files navigate by relative link only, so partial copies break. `qdrant-monitoring` splits into `setup/` and `debugging/`, and `qdrant-scaling/scaling-data-volume` splits into four further directories; copy the parent with its children.
- These skills are passive knowledge. The README points at two separate MCP servers for tool-level work, `mcp-code-snippets` for documentation and code search and `mcp-server-qdrant` for storing memories and managing collections, and neither is part of this repository.

## Related

- [LangChain Agent Skills - Memory, RAG, Persistence & Middleware Setup](/hermes/skills/catalog/langchain-skills-setup)
- [Hermes Memory Stack Setup](/hermes/skills/catalog/hermes-memory-stack-setup)
- [Context Forge Rag Setup](/hermes/skills/catalog/context-forge-rag-setup)
- [Pydantic Skills - Logfire and Pydantic AI Suite Setup](/hermes/skills/catalog/pydantic-skills-setup)

## Pro Tips

- Install the advisor first and the bundle second. The advisor routes from a symptom and stays current; the bundle is what gives you offline and deterministic behaviour once you know which branches you use.
- Name the symptom, not the subsystem. "Memory keeps climbing" and "results are not relevant" are the trigger phrases these descriptions are written against; "help me with Qdrant configuration" is not.
- Ask for the golden set before accepting a quality change. `qdrant-search-quality` will propose tuning, and without a recall@k measurement you cannot tell an improvement from noise.
- Size before you provision, and size for twelve months out. `qdrant-sizing` is explicit that the point count to plan against is the one you expect later, not today's.
- If you only ever run a self-hosted collection for agent memory, start with `qdrant-deployment-options`, `qdrant-sizing`, `qdrant-multitenancy` and `qdrant-monitoring`. That is four directories covering the decisions that are expensive to change later.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
