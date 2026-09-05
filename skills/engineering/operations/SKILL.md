---
name: engineering-operations
description: Progressive disclosure routing hub for root-cause debugging, visual screenshot defect diagnosis, observability, and workspace hygiene.
---

# Engineering Operations Hub

## Purpose

This is the operational stage of the engineering lifecycle. Operations ensures software systems can be systematically diagnosed when failing, observed in production, and maintained cleanly in developer workspaces.

---

## The Operations Flow

```text
debugging / visual-defect-diagnosis (Reproduce, gather evidence, form hypothesis, minimal fix)
         ↓
observability (Structured logging, metrics, failure tracing)
         ↓
workspace-hygiene (Clean temporary artifacts, prune scratch files, maintain repository health)
```

---

## Specialist Workflows

Load the relevant specialist guide on demand using `view_file`:

- **[Debugging (Root Cause Analysis)](./debugging/SKILL.md)**: Systematically diagnose and remediate software defects using evidence, reproduction, and minimal fixes.
- **[Visual Defect Diagnosis](../../visual-defect-diagnosis/SKILL.md)**: Triage UI bugs, compiler crashes, and stack traces presented via screenshots or visual logs.
- **[Observability](./observability/SKILL.md)**: Design structured logging, tracing, metrics, and failure diagnostics.
- **[Workspace Hygiene](./workspace-hygiene/SKILL.md)**: Maintain repository cleanliness, purge temporary agent files, and preserve durable context.

---

## Operational Principle

> **Do not guess. Reproduce, gather evidence, form a hypothesis, test it, then fix.**
