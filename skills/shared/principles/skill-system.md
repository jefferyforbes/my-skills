# Skill System Architecture

The agent skill system is intentionally layered.

```text
Root AGENTS.md
│
├── Global operating principles
│
└── skills/
    │
    ├── shared/
    │   └── reusable cross-domain principles (internal progressive disclosure)
    │
    ├── engineering/
    │   ├── planning/
    │   ├── execution/
    │   ├── validation/
    │   └── operations/
    │
    ├── android/
    │   └── Android-specific guidance
    │
    ├── koog-agent-framework/
    │   └── Koog-specific guidance
    │
    ├── maintenance/
    │   ├── agent-audit/
    │   ├── agent-testing/
    │   ├── skill-maintenance/
    │   └── skill-optimization/
    │
    └── infrastructure / product-specific skills
```

---

## Host Harness Discovery Contract

> **A file is not a skill merely because it is named `SKILL.md`. A capability is discoverable only when supported by the host harness. Nested workflows that are not independently discoverable must be explicitly reachable through a discoverable parent skill. Never assume recursive skill discovery.**

To preserve portability across host harnesses (Antigravity, Relay, Hermes), distinguish:

```text
Discoverable Skill (mounted in host harness `<skills>`)
      ↓
Routed Workflow (progressive disclosure via parent router)
      ↓
Reference (on-demand deep documentation / code samples)
```

Never treat everything ending in `SKILL.md` as an equivalent top-level skill.

---

## Context Cost Principle

The primary context optimization metric is:

$$\\text{Total Knowledge} \\neq \\text{Inference Cost}$$

$$\\text{Actual Cost} = \\text{Base Instructions} + \\text{Mounted Skill Metadata} + \\text{Selected Router} + \\text{Loaded References}$$

A large domain repository (e.g. 46k words of Android documentation or 26k words of Railway operations) is architecturally sound and context-efficient if the root router is concise (~500 words) and selectively loads specific reference files on-demand.

Do not aggressively delete or shrink valuable domain references merely because the total repository token count is high. Optimize context cost through progressive extraction, not capability deletion.

---

## Ownership Layers

### 1. Root AGENTS.md
Owns universal agent behaviour:
- understand before acting;
- evidence over assumptions;
- planning;
- scope;
- verification;
- failure recovery;
- communication;
- completion.

### 2. Parent Skills (Discoverable)
Own domain-wide workflows, decision routing, and progressive disclosure entry points (e.g., `engineering`, `android`, `maintenance`).

### 3. Specialist Skills (Routed Workflows)
Own task-specific procedures and checklists reached via discoverable parent routers (e.g., `engineering/planning/implementation-plan`).

### 4. References (On-Demand Knowledge)
Own deep documentation, component catalogs, recipes, and sample implementations loaded only when required by specific tasks.

---

## Design Rule

Do not solve context duplication by deleting capability.

Instead prefer:

```text
Global principle
      +
Specialised extension
      +
On-demand reference
```

This preserves capability while minimising unnecessary inference tokens.
