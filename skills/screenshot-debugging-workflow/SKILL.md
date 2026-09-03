---
name: screenshot-debugging-workflow
description: >-
  Standard 7-stage workflow for diagnosing UI/server screenshot errors, conducting
  architectural context analysis, creating implementation plans, delegating to subagents,
  and executing code reviews.
---

# Screenshot Error Debugging & Execution Workflow

Use this skill when presented with a screenshot error, stack trace, or complex prompt requesting debugging, architectural analysis, implementation planning, multi-agent execution, and review.

## Workflow Stages

1. **Diagnosis & Context Building (`/debugging`, `/code-context`)**
   - Extract exact stack trace, symbols, line numbers, and error details.
   - Trace upstream caller logic and database/API schemas.

2. **Domain Architecture & Gradle Analysis (`/android-architecture`, `/android-gradle-logic`)**
   - Evaluate boundary contracts across Presentation, Domain, Data Storage, and Remote API layers.
   - Inspect Gradle module structure and dependencies.

3. **Technical Analysis Document**
   - Write a structured Markdown report detailing root cause analysis and remediation strategies.

4. **Implementation Plan Artifact (`/implementation-plan`)**
   - Create `implementation_plan.md` with breaking changes, proposed edits (`[NEW]`, `[MODIFY]`, `[DELETE]`), and automated test verification plans.

5. **Execution & Subagent Delegation (`/boost`, `/teamwork-preview`)**
   - Delegate scoped component tasks to `DeepCoder` or `self` subagents.

6. **Code Review & Quality Check (`/code-review`)**
   - Review code for correctness, security, performance, and testability.

7. **Walkthrough & Verification (`walkthrough.md`)**
   - Run verification builds and update `walkthrough.md`.
