---
name: engineering-planning
description: Progressive disclosure routing hub for engineering planning, requirements analysis, architecture evaluation, implementation plans, and teamwork orchestration.
---

# Engineering Planning & Architecture Hub

## Purpose

This is the planning stage of the engineering lifecycle. Planning translates user intent into clear boundaries, verifiable acceptance criteria, and structured execution sequences **before any production code is modified**.

---

## The Planning Flow

```text
requirements-analysis (What to build & acceptance criteria)
         ↓
architecture (Boundaries, data ownership & dependencies)
         ↓
implementation-plan (Concrete multi-file diff sequence & test plan)
         ↓ (if multi-agent execution)
teamwork-orchestrator (Swarm task dispatching & step checkpoints)
```

---

## Specialist Workflows

Load the relevant specialist guide on demand using `view_file`:

- **[Requirements Analysis](./requirements-analysis/SKILL.md)**: Translate user requests into testable requirements, edge cases, and acceptance criteria.
- **[Architecture Decisions](./architecture/SKILL.md)**: Evaluate system boundaries, dependency direction, state ownership, and modularity.
- **[Implementation Plan](./implementation-plan/SKILL.md)**: Establish a concise, evidence-based plan before modifying code across multiple files or layers.
- **[Teamwork Orchestrator](../../teamwork-orchestrator/SKILL.md)**: Coordinate multi-agent swarm teams, role matrices, and step-boundary checkpoints for large projects.

---

## Planning Verification

A plan is complete when:
1. Every modified file is identified (`[NEW]`, `[MODIFY]`, `[DELETE]`).
2. Observable acceptance criteria and edge cases are defined.
3. Automated test verification commands are specified.
