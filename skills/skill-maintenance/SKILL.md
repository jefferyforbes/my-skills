---
name: skill-maintenance
description: Safe structural refactoring and repair runbook for agent skills and workflows. Fixes severed routes, reconciles relative paths, updates script dependencies, and enforces the "Fix Before You Delete" principle.
---

# Skill Maintenance & Structural Repairs

## Purpose

`skill-maintenance` is the execution arm for structural repairs within the **Formal Maintenance Change Gate**:

$$\\text{agent-audit} \\longrightarrow \\text{agent-testing (baseline)} \\longrightarrow \\mathbf{skill-maintenance} \\longrightarrow \\text{agent-testing (regression)} \\longrightarrow \\text{adopt}$$

Its primary responsibility is to execute **safe, verifiable structural refactorings** across skills, manifests, references, and executable scripts.

---

# Core Principles

## 1. Fix Before You Delete
Never delete a skill, workflow, script, or configuration solely because it contains broken links, missing scripts, or malformed syntax.
Always investigate:
1. Does a replacement exist elsewhere in the repository?
2. Did a directory move break relative link paths?
3. Can the missing script or toolchain call be restored?
4. Is it an unexpanded template placeholder?
Only mark a capability for deletion when confirmed genuinely obsolete.

## 2. Preserving Capability Over Compaction
Refactoring must never sacrifice operational capability, constraint rules, safety guards, or edge-case handling for the sake of brevity.

## 3. Atomic, Verifiable Steps
Make small, discrete modifications that can be independently verified by `agent-testing`.

---

# Standard Maintenance Workflows

## 1. Repairing Severed Progressive Routing
When specialist skills are nested within subdirectories:
1. Verify that the parent directory contains a discoverable `SKILL.md` routing hub.
2. In the parent hub, provide explicit markdown links to each specialist skill (``[Name](subpath/to/SKILL.md)``).
3. Include explicit instructions directing the agent to load the document on-demand using `view_file`.
4. Validate that the relative path resolves cleanly from the parent hub.

## 2. Reconciling Relative Links After Relocation
When moving a document between directories:
1. Recalculate relative link paths from the new directory depth.
2. Ensure references within `references/` use `./` relative to their own location rather than assuming they are at root.
3. Replace hardcoded absolute machine paths (`file:///Users/<name>/...`) with portable relative links (`./references/...`).

## 3. Securing Script Execution & Environment Portability
1. Ensure executable bits are set (`chmod +x <script>`).
2. Eliminate shell syntax traps (e.g. `./~` where `./` disables tilde expansion).
3. Replace hardcoded machine paths with dynamic environment variables (e.g. `$AI_SKILLS_DIR`, `$PROJECT_ROOT`) and validate their existence before invocation.
4. Replace unexecutable template placeholders with valid defaults or interactive verification steps.

## 4. Platform Boundary Decoupling
When a generic skill contains platform-specific instructions (e.g., Jetpack Compose rules in generic testing):
1. Extract the platform rules into a specialized reference under the appropriate domain folder (`android/references/`).
2. Update the domain parent skill to route to the new reference.
3. Leave the generic skill purely platform-agnostic.
