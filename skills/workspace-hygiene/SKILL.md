---
name: workspace-hygiene
description: Maintains workspace hygiene by removing temporary agent artifacts from .agent/tmp/ while preserving durable context in skills, context, and memory.
---

# Agent Workspace Cleanup Skill

This skill defines mandatory repository hygiene protocols for agents. It establishes procedures for tearing down ephemeral task artifacts while preserving durable context and maintaining repository integrity.

---

## 1. Agent Workspace Structure & Lifecycle

The `.agent/` directory is partitioned into temporary and durable workspaces:

| Directory | Type | Purpose | Lifecycle Policy |
| :--- | :--- | :--- | :--- |
| `.agent/tmp/` | Ephemeral | Scratchpad for temporary files, logs, tool intermediates, and scratch scripts | **Purge** after each task |
| `.agent/context/` | Durable | Project architecture notes, domain knowledge, and shared context | **Preserve** across tasks |
| `.agent/memory/` | Durable | Persistent session state, agent learnings, and history | **Preserve** across tasks |
| `.agent/skills/` | Durable | Reusable procedural skills, runbooks, and automation scripts | **Preserve** across tasks |

---

## 2. Mandatory Cleanup Rules

### Rule 1: Empty the Temporary Directory (`.agent/tmp/`)
- Upon task completion, all transient files, intermediate outputs, scratch scripts, and temporary caches in `.agent/tmp/` MUST be removed.
- The `.keep` file (`.agent/tmp/.keep`) MUST be preserved to maintain directory tracking in git.

```bash
# Clean all temporary files while keeping the root .keep intact
find .agent/tmp -mindepth 1 ! -path '.agent/tmp/.keep' -delete
```

### Rule 2: Preserve Durable Context
- NEVER delete or overwrite files in `.agent/context/`, `.agent/memory/`, or `.agent/skills/` during cleanup routines.
- Any valuable insights, updated project documentation, or shared patterns must be persisted into `.agent/context/` or `.agent/memory/` before tearing down the temporary workspace.
- Ensure all `.keep` placeholder files (`.agent/context/.keep`, `.agent/memory/.keep`, `.agent/tmp/.keep`) remain in place.

### Rule 3: Maintain Repository Hygiene & Prevent Leaking Artifacts
- Ensure the repository is left in a clean, intentional state without committing temporary agent artifacts.
- Check `git status` prior to completing any task to confirm no untracked scratch files, ad-hoc logs, or temporary caches exist outside `.agent/tmp/` or are staged for commit.
- Untracked artifacts generated during testing or execution outside `.agent/` must be cleaned up immediately.

---

## 3. Post-Task Cleanup Protocol

Follow this checklist at the conclusion of every engineering task:

1. **Persist Learnings & Context**:
   - Move any durable notes or architectural decisions to `.agent/context/`.
   - Update agent memory in `.agent/memory/` if long-term state tracking is required.

2. **Purge Temporary Files**:
   - Run the cleanup command to empty `.agent/tmp/` without deleting `.agent/tmp/.keep`.

3. **Verify Repository Cleanliness**:
   - Run `git status` to verify no untracked or unwanted files remain in the working tree.
   - Confirm that only intended code and configuration modifications are present.

