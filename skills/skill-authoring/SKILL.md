---
name: skill-authoring
description: Create, extract, or refactor composable Antigravity skills from URLs, markdown files, specifications, or repeated workflows while enforcing context budgets and progressive disclosure.
---

# Skill Authoring & Synthesis

## Purpose

This skill guides the creation, extraction, and refactoring of composable agent skills that minimize context cost while preserving deep operational capability.

Use this skill when asked to:
- **"Turn this URL / markdown / document into a skill."**
- **"Create a new skill for X."**
- Refactor or decompose an existing monolithic skill.

---

## The Core Triad of Our Skills

Every skill created, cultivated, or refactored must strictly adhere to three foundational principles:

```text
┌─────────────────────────────────────────────────────────────┐
│                 THE CORE TRIAD OF OUR SKILLS                │
├──────────────────────────────┬──────────────────────────────┤
│ 1. Well-Connected            │ Explicit routing table,      │
│    (Zero Dead Ends)          │ bidirectional parent-child   │
│                              │ links, reachable in harness. │
├──────────────────────────────┼──────────────────────────────┤
│ 2. Thorough                  │ Deep domain knowledge, edge  │
│    (No Shallow Checklists)   │ cases, and real recipes in   │
│                              │ references/ (never lost).    │
├──────────────────────────────┼──────────────────────────────┤
│ 3. Precise                   │ Root router <600 words,      │
│    (Context Economical)      │ zero fluff, actionable rules,│
│                              │ exact verification steps.    │
└──────────────────────────────┴──────────────────────────────┘
```

---

## The Router Hub & References Architecture

> **Keep operational rules and triggers in the root `SKILL.md`; defer deep knowledge, component catalogs, and multi-line examples to `references/`.**

```text
skills/<skill-name>/
├── SKILL.md            <-- Root router: purpose, triggers, decision rules, verification (<600 words)
├── references/         <-- On-demand deep documentation (loaded via view_file when needed)
│   ├── api-guide.md
│   └── recipes.md
└── scripts/            <-- Executable automation or regression scripts (optional)
```

---

## Antigravity Discovery Contract

1. **Top-Level Discovery**:
   - Antigravity discovers active skills at exactly `~/.gemini/config/skills/<skill-name>/SKILL.md` (depth 1).
   - Only place skills at top level if they represent distinct, independently discoverable capabilities.
2. **Context Budget Ceiling**:
   - The root `SKILL.md` must stay under **600 words** (strictly under 1,000 words).
   - A skill is a capability routing tool, not an encyclopedia.

---

## Workflow for Authoring a Skill

### 1. Ingestion & Analysis
- **From URL**: Fetch content using `read_url_content`. Strip promotional fluff, navigation bars, and marketing copy.
- **From Local Spec / Markdown**: Inspect sections using `view_file`.
- Pinpoint:
  - *What exact capability does this provide?*
  - *What triggers its activation?*
  - *What tools does it require?*

### 2. Separation of Concerns (Router Hub + References)
- **Root `SKILL.md` (Precise & Well-Connected)**:
  - YAML frontmatter: `name` (kebab-case) and `description` (concise trigger criteria).
  - Clear purpose statement.
  - Activation trigger checklist.
  - Core behavioral constraints and decision rules.
  - Explicit routing table to references (`references/<topic>.md`).
  - Verification checklist.
- **`references/` Directory (Thorough)**:
  - Full API endpoint tables, schema mappings, extensive code templates, and migration walkthroughs.

---

## References & Authoring Templates

Load on-demand via `view_file`:
- **[Skill Authoring Templates & Schemas](./references/skill-templates.md)**: Standard markdown scaffolds for root routers, references, and tool definitions.

---

## Verification & Change Gate Checklist

Before considering any newly authored skill complete:
- [ ] **Well-Connected**: Relative markdown links resolve cleanly (`[Title](./references/guide.md)`).
- [ ] **Precise**: Root `SKILL.md` is strictly within the context budget (`wc -w SKILL.md` < 600).
- [ ] **Thorough**: Complex concepts have dedicated reference files under `references/`.
- [ ] **Portable**: No machine-specific hardcoded absolute paths (`/Users/...`).
- [ ] **Executable**: Referenced scripts have executable permissions (`chmod +x`).
- [ ] **Change Gate**: Pass regression suite: `python3 ~/.gemini/config/skills/maintenance/scripts/run_regression.py`.
- [ ] **Sync**: Offer to synchronize to external backup via `update-ai-data`.
