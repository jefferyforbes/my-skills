---
name: teamwork-orchestrator
description: Orchestrate multi-agent swarm teams, specialized subagents, milestone task dispatches, and step-boundary checkpoints for complex projects.
---

# Teamwork Orchestration & Multi-Agent Swarms

## Purpose

Coordinate complex engineering projects across autonomous, specialized subagent teams. Enforces disciplined role separation, task handoffs, checkpointing, and adversarial verification.

Use this skill when:
- Executing large, multi-phase architectural features or refactors.
- Dispatching parallel tasks to specialized subagents (`invoke_subagent`, `send_message`).
- The user requests `/teamwork-preview` or a swarm workflow.

---

## 1. Swarm Persona Matrix

When dividing complex work, instantiate specialized personas with bounded scopes:

```text
┌────────────────────────────────────────────────────────┐
│                  Project Orchestrator                  │
│   Maintains plan.md, progress.md, dispatches & monitors│
└───────────┬────────────────────────────────┬───────────┘
            │                                │
            ▼                                ▼
┌──────────────────────┐          ┌──────────────────────┐
│  Explorer / Miner    │          │Implementation Worker │
│  Read-only mapping   │          │Scoped code & tests   │
└───────────┬──────────┘          └──────────┬───────────┘
            │                                │
            ▼                                ▼
┌──────────────────────┐          ┌──────────────────────┐
│  Reviewer / Sentinel │          │Adversarial Challenger│
│  Security & quality  │          │Stress-tests boundaries│
└───────────┬──────────┘          └──────────┬───────────┘
            │                                │
            └────────────────┬───────────────┘
                             ▼
                  ┌──────────────────────┐
                  │   Victory Auditor    │
                  │   Independent proof  │
                  └──────────────────────┘
```

---

## 2. Orchestrator Dispatch Protocol

The **Project Orchestrator** must maintain project state in a designated coordination directory (typically `.agents/orchestrator/` or `.agents/teamwork/`):

1. **`ORIGINAL_REQUEST.md`**: Immutable copy of user instructions and acceptance criteria.
2. **`PROJECT.md` / `plan.md`**: Milestone breakdown, dependency graph, and assigned roles.
3. **`progress.md`**: Real-time status tracker updated after each milestone handoff.

### Dispatching Subagents
When dispatching a task via `invoke_subagent`:
- Pass a structured prompt specifying:
  - Exact Role and Persona.
  - Working directory (`.agents/<role_name>/`).
  - Mandatory inputs to read (`ORIGINAL_REQUEST.md`, upstream handoffs).
  - Concrete deliverable path (`.agents/<role_name>/handoff.md`).
  - Required completion message back to parent.

---

## 3. Step-Boundary Checkpointing

To ensure resilience against crashes or session truncation:
- Save state to disk at each step boundary.
- Context metadata (e.g. completed milestones, active branch names, verified test results) should be persisted in checkpoint files.
- Before starting a new phase, the orchestrator verifies the preceding checkpoint.

---

## 4. Adversarial Verification & Victory Audit

Never conclude a multi-agent project solely on an implementation worker's report:
1. **Adversarial Challenger**: Explicitly seeks out edge cases, empty inputs, timeout behavior, and concurrency races.
2. **Victory Auditor**: An independent, fresh agent instance with no confirmation bias that:
   - Reads the original acceptance criteria.
   - Executes the automated test suite independently.
   - Confirms that deliverables match every requirement before reporting completion.

---

## Deep References
Load on-demand using `view_file`:
- **[Swarm Persona Prompts & Handoff Schemas](./references/swarm-persona-prompts.md)**: Production-ready prompts for Explorers, Workers, Challengers, and Victory Auditors.
