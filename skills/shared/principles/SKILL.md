---
name: shared-principles
description: Internal progressive-disclosure routing hub for shared cross-domain agent principles, architecture contracts, and authoring guidelines.
---

# Shared Principles Router

## Purpose

This is an **internal progressive-disclosure router** for cross-domain engineering and agent principles. 

It is not mounted as an independent discoverable skill at the harness root; instead, discoverable domain skills (such as `engineering`, `android`, or `maintenance`) route to these principles when cross-domain alignment, learning, or authoring rules are required.

---

# Architecture & Principles Catalog

Use `view_file` on the relative paths below to inspect the appropriate principle document:

## 1. Skill System Architecture & Discovery Contract
- **[Skill System Architecture](./skill-system.md)**: Layered ownership model, the Host Harness Discovery Contract, and the capability hierarchy (`Discoverable Skill -> Routed Workflow -> Reference`).

## 2. Skill Authoring & Context Discipline
- **[Skill Authoring Guidelines](./skill-authoring/SKILL.md)**: Rules for creating composable, maintainable skills, managing context budgets, and moving bulky knowledge into references.

## 3. Principles & Learning Workflow
- **[Learning & Decision Narration](./learning/SKILL.md)**: Guidelines for explaining non-obvious engineering decisions, trade-offs, and educational insights without narrating mechanical keystrokes.

## 4. Repository Overview
- **[Shared Directory Overview](../README.md)**: Architectural purpose of unmounted shared principles.
