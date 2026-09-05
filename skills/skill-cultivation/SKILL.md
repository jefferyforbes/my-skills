---
name: skill-cultivation
description: Discovers, analyzes, and synthesizes new candidate skills by mining residual session artifacts, interaction transcripts, user corrections, and recurring workflows.
---

# Skill Cultivation & Pattern Mining

## Purpose

`skill-cultivation` is the generative discovery engine of the **Formal Maintenance Change Gate**:

$$\mathbf{skill\text{-}cultivation} \longrightarrow \text{agent-audit} \longrightarrow \text{agent-testing} \longrightarrow \text{adopt}$$

While `agent-audit` inspects existing skills for duplication and decay, `skill-cultivation` looks backward across **residual artifacts** (session transcripts, implementation plans, walkthroughs, generated code, and developer corrections) to identify repeated patterns and synthesize new, high-value, reusable skills adhering to the **Core Skill Triad** (Well-Connected, Thorough, Precise).

---

## The Cultivation Lifecycle

```text
┌─────────────────────────────────┐
│ 1. Harvest Residual Artifacts   │  Inspect session logs, brain artifacts, user prompts
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

## 1. Harvesting Residual Artifacts

Antigravity creates durable session records under `~/.gemini/antigravity/brain/<session-id>/`:
- **Transcripts (`transcript.jsonl`)**: Chronological history of user requests, model reasoning, and tool calls.
- **Architectural Artifacts**: `implementation_plan.md`, `walkthrough.md`, diagrams, and reports.
- **Scratch Files**: Code snippets and temporary investigation scripts.

### Lightweight Interaction Ledger

To avoid scanning raw multi-megabyte transcripts repeatedly, maintain and query the lightweight interaction ledger:

```bash
python3 ~/.gemini/config/skills/maintenance/skill-cultivation/scripts/harvest_sessions.py
```

This updates `ledger.jsonl`, providing a compact index of session IDs, user intents, tools executed, and deliverables.

---

## 2. Pattern Mining Heuristics

When reviewing harvested interactions, evaluate against three key signals:
1. **Repeated Multi-Step Workflows (Procedural Toil)**: Frequent identical setups or pipelines across distinct sessions.
2. **Recurring User Corrections (Behavioral Misalignment)**: Persistent developer corrections (e.g. constraints, flags, custom scripts).
3. **Emergent Domain Stacks (New Project Primitives)**: New SDKs or architectures requiring repetitive codebase navigation.

---

## 3. Skill Candidate Architecture: The Triad Standard

Candidate skill drafts must never be monolithic text dumps. They must be structured as:
- **Root `SKILL.md` (Precise & Well-Connected)**: <600 words, purpose, triggers, behavioral constraints, and router links.
- **`references/` Directory (Thorough)**: Comprehensive implementation recipes, deep schemas, checklists, and edge cases.

---

## Deep References

Load on-demand via `view_file`:
- **[Cultivation Patterns & Mining Guide](./references/cultivation-guide.md)**: Querying the ledger, clustering algorithms, and proposal evaluation scoring.

---

## 4. Verification & Change Gate Handoff

Never adopt a cultivated skill directly into production:
1. **`agent-audit`**: Ensure zero overlap with existing skills and proper parent-child routing.
2. **`agent-testing`**: Verify links, discoverability, reachability, and syntax with `run_regression.py`.
3. **`update-ai-data`**: Synchronize to durable external repositories.
