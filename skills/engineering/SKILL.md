---
name: engineering
description: Foundational software engineering operating model and routing hub. Use as the base capability for implementation, planning, architecture, refactoring, debugging, testing, code review, security, and cleanup.
---

# Engineering Core & Routing Hub

## Purpose

This is the foundational engineering skill.

The root `AGENTS.md` defines the global agent operating model. This skill defines how engineering work is routed into specialised workflows.

**Do not duplicate the root engineering principles here.**

The operating hierarchy is:

```text
AGENTS.md
    ↓
Engineering operating model
    ↓
Specialist engineering skill
    ↓
Domain/platform skill
    ↓
Reference material
```

More specific guidance may add constraints or procedures, but should not silently contradict the root operating model.

---

# Engineering Lifecycle

Use the following lifecycle for non-trivial engineering work:

```text
Understand
    ↓
Discover
    ↓
Define outcome
    ↓
Decompose
    ↓
Plan
    ↓
Implement
    ↓
Verify
    ↓
Review
    ↓
Report
```

If verification fails:

```text
Failure
   ↓
Diagnose
   ↓
Update hypothesis / plan
   ↓
Implement
   ↓
Verify
```

Do not repeatedly retry an unchanged approach.

---

# Skill Routing

Read the smallest relevant specialist skill set needed for the task.

When executing specific engineering tasks, **read the relevant specialist guide on demand by calling `view_file` on the relative path**.

## Planning & Analysis

Use when the task requires understanding requirements, architecture, or implementation sequencing:

- **[Requirements Analysis](./planning/requirements-analysis/SKILL.md)**: Translate requests into unambiguous acceptance criteria, constraints, and testable boundaries.
- **[Implementation Plan](./planning/implementation-plan/SKILL.md)**: Establish a concise, evidence-based plan before making non-trivial changes across multiple files or layers.
- **[Architecture Decisions](./planning/architecture/SKILL.md)**: Evaluate boundaries, ownership, dependencies, and state flow.

Typical flow:
```text
requirements-analysis
        ↓
architecture (when required)
        ↓
implementation-plan
```
Do not invoke all three automatically for small changes.

---

## Execution

Use when exploring, modifying, or restructuring code:

- **[Code Context & Navigation](./execution/code-context/SKILL.md)**: Build a focused understanding of entry points, callers, and data flows before modifying code.
- **[Refactoring](./execution/refactoring/SKILL.md)**: Safely improve structure and maintainability without altering observable behaviour.
- **[Code Path Cleanup](./execution/code-path-cleanup/SKILL.md)**: Identify and remove obsolete code paths, orphaned functions, and unnecessary compatibility layers.

Use refactoring or cleanup only when the requested work actually requires it.

---

## Validation

Use when proving correctness or assessing quality:

- **[Testing (Strategy & Levels)](./validation/testing/SKILL.md)**: Select the smallest appropriate test level (unit, integration, UI, screenshot) to protect meaningful behaviour.
- **[Code Review](./validation/code-review/SKILL.md)**: Multi-dimensional review focusing on correctness, safety, architecture, testability, and edge cases.
- **[Security](./validation/security/SKILL.md)**: Threat modeling, trust boundaries, injection prevention, and credential protection.

Validation should be selected according to risk rather than mechanically running every validation workflow.

---

## Operations

Use when diagnosing, observing, or operating existing systems:

- **[Debugging (Root Cause Analysis)](./operations/debugging/SKILL.md)**: Systematic diagnosis using reproduction, evidence, hypothesis testing, and minimal fixes.
- **[Observability](./operations/observability/SKILL.md)**: Structured logging, tracing, metrics, and failure diagnostics.
- **[Workspace Hygiene](./operations/workspace-hygiene/SKILL.md)**: Maintaining repository cleanliness, purging `.agent/tmp/`, and preserving durable context.

---

# Composition Rules

Skills should compose rather than duplicate one another.

For example:

```text
Feature request
    ↓
requirements-analysis
    ↓
implementation-plan
    ↓
code-context
    ↓
implementation
    ↓
testing
    ↓
code-review
```

A debugging task may instead use:

```text
code-context
    ↓
debugging
    ↓
testing
    ↓
code-review
```

A refactor may use:

```text
code-context
    ↓
refactoring
    ↓
testing
    ↓
code-review
```

The exact combination should follow the task rather than a fixed ceremony.

---

# Context Discipline

Specialist skills should:

- Keep core instructions concise.
- Move deep reference material into `references/`.
- Avoid repeating global engineering principles.
- Avoid repeating instructions already provided by parent skills.
- Load detailed knowledge only when relevant.
- Prefer reusable procedures over long explanations.

When two skills contain the same rule, determine whether it belongs at a higher level instead of maintaining duplicate copies.

---

# Evidence Contract

Specialist skills must distinguish between:

- **Observed** — directly established from code, tooling, runtime behaviour, or documentation.
- **Inferred** — conclusion supported by available evidence.
- **Assumed** — necessary assumption not yet established.
- **Unable to verify** — evidence could not be obtained.

Do not report assumptions as facts.

---

# Verification Contract

Every implementation-oriented skill should define:

1. What behaviour should be verified.
2. Which verification level is appropriate.
3. What evidence constitutes success.
4. What should happen if verification fails.

Compilation alone is never sufficient proof when behaviour requires stronger evidence.

---

# Scope Contract

Specialist skills should not expand task scope unless the expansion is necessary to:

- preserve correctness,
- resolve a blocking issue,
- satisfy the requested outcome,
- protect an important architectural boundary, or
- prevent a clear regression.

Optional improvements should be surfaced rather than silently implemented.

---

# Completion Contract

A specialist workflow should finish with:

- What changed.
- What was verified.
- Important architectural decisions.
- Remaining uncertainty.
- Any follow-up work that is genuinely necessary.

Do not claim verification that was not performed.

---

# Principles & Learning

When the user needs an explanation of an engineering concept, trade-off, or surprising behaviour, or when authoring skills, load the shared principle documents via `view_file`:

- **[Learning & Decision Narration](../shared/principles/learning/SKILL.md)**: Guidelines for explaining non-obvious engineering decisions and trade-offs.
- **[Shared Principles Router](../shared/principles/SKILL.md)**: Catalog of shared architectural standards and authoring rules.

Keep explanations decision-oriented rather than narrating implementation mechanics.
