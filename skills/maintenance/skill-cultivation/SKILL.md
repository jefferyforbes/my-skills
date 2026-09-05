---
name: skill-cultivation
description: Discovers, analyzes, and synthesizes new candidate skills by mining residual session artifacts, interaction transcripts, user corrections, recurring workflows, and frontier research via Firecrawl.
---

# Skill Cultivation & Pattern Mining

## Purpose

`skill-cultivation` is the generative discovery engine of the **Formal Maintenance Change Gate**:

$$\mathbf{skill\text{-}cultivation} \longrightarrow \text{agent-audit} \longrightarrow \text{agent-testing} \longrightarrow \text{adopt}$$

While `agent-audit` inspects existing skills for duplication and decay, `skill-cultivation` discovers reusable improvements by:
1. **Mining Internal Residual Artifacts**: Inspecting past session transcripts, implementation plans, walkthroughs, and developer corrections.
2. **Conducting External Frontier Research**: Querying scientific research papers, GitHub repositories, and upstream technical documentation via Firecrawl.

---

## The Cultivation Lifecycle

```text
┌─────────────────────────────────┐
│ 1. Harvest Residual Artifacts   │  Inspect session logs, brain artifacts, user prompts
│    & Frontier Research          │  Query papers, GitHub, and upstream docs via Firecrawl
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│ 2. Cluster Recurring Patterns   │  Identify repetitive manual workflows or repeated guidance
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│ 3. Evaluate Cultivation Value   │  Assess frequency, toil reduction, and scope boundaries
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│ 4. Draft Candidate Skill        │  Enforce Router Hub (<600 words) + references/ structure
└────────────────┬────────────────┘
                 │ candidate ready
                 ▼
┌─────────────────────────────────┐
│ 5. Submit to agent-audit Gate   │  Verify no overlap with existing catalog before adoption
└─────────────────────────────────┘
```

---

## 1. Harvesting Residual Artifacts & Research

### Internal Session Harvesting
Antigravity creates durable session records under `~/.gemini/antigravity/brain/<session-id>/`:
- **Transcripts (`transcript.jsonl`)**: Chronological history of requests, reasoning, and tool calls.
- **Architectural Artifacts**: Plans, walkthroughs, diagrams, and reports.
- Query the lightweight interaction ledger:
  ```bash
  python3 ~/.gemini/config/skills/maintenance/skill-cultivation/scripts/harvest_sessions.py
  ```

### External Frontier Research with Firecrawl
When researching new agent capabilities, architectural paradigms, or upstream API changes, use the [`firecrawl`](../../firecrawl/SKILL.md) skill:
- **Scientific Papers**: `firecrawl research search-papers "<topic>"`
- **GitHub Discussions & PRs**: `firecrawl research search-github "<topic>"`
- **Upstream Documentation**: `firecrawl search` and `firecrawl scrape`

---

## 2. Pattern Mining Heuristics

Evaluate potential skills against three core signals:
1. **Repeated Multi-Step Workflows (Procedural Toil)**: Frequent identical setups across sessions.
2. **Recurring User Corrections (Behavioral Misalignment)**: Persistent developer corrections.
3. **Emergent Domain Stacks (New Project Primitives)**: New SDKs or external tooling patterns.

---

## 3. Skill Candidate Architecture: The Triad Standard

Candidate skill drafts must never be monolithic text dumps. They must be structured as:
- **Root `SKILL.md` (Precise & Well-Connected)**: <600 words, purpose, triggers, behavioral constraints, and router links.
- **`references/` Directory (Thorough)**: Comprehensive implementation recipes, deep schemas, checklists, and edge cases.

---

## Deep References

Load on-demand via `view_file`:
- **[Cultivation Patterns & Mining Guide](./references/cultivation-guide.md)**: Querying the ledger, scoring models, and Firecrawl research patterns.

---

## 4. Verification & Change Gate Handoff

Never adopt a cultivated skill directly into production:
1. **`agent-audit`**: Ensure zero overlap with existing skills and proper parent-child routing.
2. **`agent-testing`**: Verify links, discoverability, reachability, and syntax with `run_regression.py`.
3. **`update-ai-data`**: Synchronize to durable external repositories.
