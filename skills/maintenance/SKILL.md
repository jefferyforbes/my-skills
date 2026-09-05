---
name: maintenance
description: Agent system maintenance and self-evaluation harness. Inspect, audit, test, refactor, and optimize agent skills, instructions, and workflows under strict evidence constraints.
---

# Agent Maintenance Subsystem & Routing Hub

## Purpose

The `maintenance` skill is the discoverable top-level routing hub for the agent self-maintaining harness. It provides the capabilities and governance required to evaluate, test, refactor, and optimize the agent operating system itself (instructions, skills, workflows, references, and tool definitions).

---

## Operating Mandate

> **Maintenance skills may inspect and propose changes to the agent system itself, but must use evidence and regression validation before modifying foundational instructions.**

Never modify agent instructions, skills, or workflows based solely on a single isolated failure or speculative convenience. All modifications must pass through the formal maintenance change gate.

---

## The Formal Maintenance Change Gate

All proposed modifications to the agent system must follow this strict 5-stage lifecycle:

```text
┌─────────────────┐
│   agent-audit   │  1. System evaluation & finding discovery
└────────┬────────┘
         │ findings
         ▼
┌─────────────────┐
│  agent-testing  │  2. Establish baseline tests capturing observed defects
└────────┬────────┘
         │ baseline proven
         ▼
┌─────────────────┐
│skill-maintenance│  3. Execute minimal, safe structural repairs or
│skill-optimise   │     extract deep references to reduce context
└────────┬────────┘
         │ modification complete
         ▼
┌─────────────────┐
│  agent-testing  │  4. Run regression suite to prove fix without regression
└────────┬────────┘
         │ regression passed
         ▼
┌─────────────────┐
│      adopt      │  5. Promote changes into production configuration
└─────────────────┘
```

---

# Maintenance Capabilities Catalog

When performing agent maintenance, **read the relevant specialist guide on demand by calling `view_file` on the relative path**:

## 1. System-Wide Health & Diagnostics
- **[Agent System Audit](./agent-audit/SKILL.md)**: Perform a full evaluation of system health, discoverability, context efficiency, link integrity, and architectural consistency across all skills and configurations.

## 2. Proving & Regression Testing
- **[Agent Testing](./agent-testing/SKILL.md)**: Concrete scenario and regression testing suite to prove that proposed improvements actually work and prevent regressions in routing, discovery, and execution. Automated runner available at `maintenance/scripts/run_regression.py`.

## 3. Safe Structural Repairs
- **[Skill Maintenance](./skill-maintenance/SKILL.md)**: Safe refactoring runbook for repairing broken routes, updating script references, reconciling paths, and enforcing the "Fix Before You Delete" principle.

## 4. Context Budgeting & Compression
- **[Skill Optimization](./skill-optimization/SKILL.md)**: Measure actual context cost versus inference cost, separate operational rules from deep references, and extract bulky knowledge without losing capability.

---

# Verification & Completion Contract

Any agent execution within the `maintenance` domain must conclude with:
1. What was inspected or modified.
2. The before-and-after baseline evidence from `agent-testing`.
3. Verification that zero capabilities were degraded or unintentionally removed.
4. Any remaining uncertainties surfaced to the user.
