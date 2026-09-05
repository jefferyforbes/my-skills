---
name: code-context
description: Build a focused understanding of the existing codebase before making requested code changes. Use when a code change requires understanding surrounding architecture, dependencies, data flow, conventions, state ownership, callers, tests, or existing implementations before deciding how to modify the code.
---

# Code Context & Navigation

## Purpose

Build enough context around a requested code change to make an informed implementation decision **before modifying code**.

The goal is not to understand the entire repository, but the **smallest relevant system surrounding the requested change**.

---

## Core Principle

> **Understand before modifying. Do not immediately edit the first file that appears relevant.**

---

## When to Use
- Implementing a new feature in an existing codebase.
- Modifying existing behavior or fixing non-trivial bugs.
- Refactoring, changing APIs, or adjusting state management.
- Working in an unfamiliar repository or evaluating cross-module impact.

---

## Context Workflow

```text
1. Parse Request (Desired vs actual behavior, explicit constraints)
       ↓
2. Locate Entry Point (Screen, Composable, Class, API, or Repository)
       ↓
3. Trace Callers & Dependencies (Determine consumers and upstream contracts)
       ↓
4. Inspect Existing Patterns (Match conventions and tests)
       ↓
5. Form Minimal Change Hypothesis (Smallest correct modification)
```

---

## Progressive Disclosure Routing

For deep tracing techniques and impact checklists, load via `view_file`:
- **[Code Exploration Guide](./references/code-exploration-guide.md)**: Detailed caller tracing workflows, Level 1–4 depth expansion, and cross-module impact matrices.

---

## Context Output Checklist
Before modifying code, establish:
- **Current Behavior**: What currently happens and where.
- **Key Files**: Exact paths of entry points and dependencies.
- **Existing Pattern**: Conventions to follow.
- **Target Change Location**: The minimal correct file and symbol.
- **Risks**: Potential breakage for callers or state.
