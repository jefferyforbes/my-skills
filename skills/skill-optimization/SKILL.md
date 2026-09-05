---
name: skill-optimization
description: Context budgeting, progressive disclosure optimization, and reference extraction tool. Measures actual inference cost vs total repository knowledge and compresses prompt footprints without capability degradation.
---

# Skill Optimization & Context Budgeting

## Purpose

`skill-optimization` is the efficiency and compression arm of the **Formal Maintenance Change Gate**:

$$\\text{agent-audit} \\longrightarrow \\text{agent-testing (baseline)} \\longrightarrow \\mathbf{skill-optimization} \\longrightarrow \\text{agent-testing (regression)} \\longrightarrow \\text{adopt}$$

Its primary goal is to **maximize agent capability per token of context**, ensuring that the agent has access to comprehensive knowledge without bloating inference prompts.

---

# The Context Optimization Metric

The core metric governing skill optimization is:

$$\\text{Total Knowledge} \\neq \\text{Inference Cost}$$

$$\\text{Actual Cost} = \\text{Base Instructions} + \\text{Mounted Skill Metadata} + \\text{Selected Router} + \\text{Loaded References}$$

### Key Insights:
1. **Repository Size $\\neq$ Prompt Load**: A 50,000-word domain documentation library (such as Android Wear Compose samples or Railway infrastructure guides) has **zero prompt cost** until a task specifically calls for that domain.
2. **Root Routers Must Be Lean**: The root `SKILL.md` file mounted into the agent prompt or selected during task initiation must remain concise (~300–700 words), containing only:
   - What the domain handles.
   - Core behavioral rules and constraints.
   - A clear routing table pointing to specialist references.
3. **Deep Material Belongs in `references/`**: Lengthy API guides, component galleries, recipes, edge-case checklists, and multi-line code samples must reside in unmounted `references/` files loaded via `view_file` only when needed.

---

# Progressive Disclosure Extraction Workflow

When a skill exceeds acceptable context budgets (>1,000 words in its root `SKILL.md`):

```text
Heavy Monolithic SKILL.md (>1,500 words)
                 │
                 ▼
        [Extract & Split]
                 │
  ┌──────────────┴──────────────┐
  ▼                             ▼
Concise SKILL.md           references/
(~400–600 words)           (deep guides, samples, recipes)
- Purpose                  - API catalogs
- Triggers                 - Component samples
- Core rules               - Migration walkthroughs
- Routing table            - Edge-case catalogs
```

### Extraction Checklist:
1. **Identify Bulky Sections**: Search for long code examples, repetitive parameter tables, and framework migration guides.
2. **Move to `references/`**: Create descriptive markdown files under `references/<topic>.md`.
3. **Add On-Demand Link in Router**: In the parent `SKILL.md`, link to ``[Topic Guide](references/topic.md)`` with explicit trigger conditions.
4. **Preserve Specialized Rules**: Ensure behavioral constraints and validation steps remain in the active operational path.
5. **Verify via `agent-testing`**: Confirm all newly extracted reference links resolve and that the prompt context size is successfully reduced.
