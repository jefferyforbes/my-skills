---
name: engineering
description: Foundational software engineering principles, decision workflows, verification standards, and quality reviews. Use as a base capability across implementation, refactoring, code review, debugging, and architecture tasks.
---

# Engineering Core & Routing Hub

## Purpose
Define unified software engineering standards across all modification, refactoring, review, testing, and debugging workflows. 
The baseline rules are strictly enforced by the global `<RULE[user_global]>`.

When executing specific engineering tasks, **you must read the relevant deep-dive reference manuals** listed below by calling `view_file` on the corresponding path.

---

# Engineering Reference Manuals

## 1. Planning & Analysis
When defining architectures, establishing plans, or analyzing complex requirements:
- **Implementation Plan:** `~/.gemini/config/skills/engineering/planning/implementation-plan/SKILL.md`
- **Architecture Decisions:** `~/.gemini/config/skills/engineering/planning/architecture/SKILL.md`
- **Requirements Analysis:** `~/.gemini/config/skills/engineering/planning/requirements-analysis/SKILL.md`

## 2. Execution & Refactoring
When executing non-trivial code modifications, deep refactoring, or codebase context gathering:
- **Code Context & Navigation:** `~/.gemini/config/skills/engineering/execution/code-context/SKILL.md`
- **Refactoring:** `~/.gemini/config/skills/engineering/execution/refactoring/SKILL.md`
- **Code Path Cleanup:** `~/.gemini/config/skills/engineering/execution/code-path-cleanup/SKILL.md`

## 3. Validation & Testing
When validating features, reviewing code, writing tests, or securing applications:
- **Testing (Strategy & Levels):** `~/.gemini/config/skills/engineering/validation/testing/SKILL.md`
- **Code Review:** `~/.gemini/config/skills/engineering/validation/code-review/SKILL.md`
- **Security:** `~/.gemini/config/skills/engineering/validation/security/SKILL.md`

## 4. Operations & Debugging
When diagnosing bugs, tracking issues, or monitoring applications:
- **Debugging (Root Cause Analysis):** `~/.gemini/config/skills/engineering/operations/debugging/SKILL.md`
- **Observability (Logging/Tracing):** `~/.gemini/config/skills/engineering/operations/observability/SKILL.md`
- **Cleanup:** `~/.gemini/config/skills/engineering/operations/cleanup/SKILL.md`

## 5. Principles & Learning
- **Learning & Explanations:** `~/.gemini/config/skills/shared/principles/learning/SKILL.md`

*(Note: These reference documents contain detailed checklists, workflows, and anti-patterns for their respective domains. View them when their domain is central to your current task.)*
