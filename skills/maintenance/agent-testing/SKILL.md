---
name: agent-testing
description: Scenario and regression testing tool for proving proposed agent system changes. Validates discoverability, routing integrity, link resolution, execution safety, and platform boundary isolation.
---

# Agent Testing & Regression Proving

## Purpose

`agent-testing` is the verification and regression layer of the **Formal Maintenance Change Gate**:

$$\\text{agent-audit (findings)} \\longrightarrow \\text{agent-testing (baseline)} \\longrightarrow \\text{modify} \\longrightarrow \\text{agent-testing (regression test)} \\longrightarrow \\text{adopt}$$

Its primary role is to **prove that proposed system modifications solve identified problems without causing behavioral or architectural regressions**.

Maintenance skills must never modify foundational instructions or workflows without first establishing a baseline test and subsequently passing regression validation.

---

# Initial Concrete Regression Suite

The test suite is seeded directly from the system audit findings:

```text
agent-testing
├── discovery
│   └── nested_capability_is_reachable
├── routing
│   └── engineering_routes_to_all_specialists
├── references
│   └── all_internal_links_resolve
├── execution
│   └── referenced_scripts_are_executable
├── boundaries
│   └── generic_engineering_contains_no_android_specific_rules
└── regression
    ├── nested_skill_discovery
    ├── broken_relative_links
    ├── absolute_machine_paths
    └── executable_placeholder_commands
```

---

## 1. Discovery Suite: `nested_capability_is_reachable`

### Assertion:
Every nested workflow or reference must be reachable via a chain of valid markdown links originating from an independently discoverable top-level skill (`skills/<name>/SKILL.md`).

### Test Procedure:
1. Inventory all top-level discoverable roots (depth 1 under `skills/`).
2. Crawl outgoing markdown links recursively.
3. Assert that 100% of internal `.md` documents are present in the reachable set.
4. Flag any orphaned documents that cannot be reached by an agent starting from a discoverable root.

---

## 2. Routing Suite: `engineering_routes_to_all_specialists`

### Assertion:
The root `engineering/SKILL.md` routing hub must contain explicit, resolvable links and `view_file` instructions for all 12 specialist engineering workflows:
- Planning: `requirements-analysis`, `implementation-plan`, `architecture`
- Execution: `code-context`, `refactoring`, `code-path-cleanup`
- Validation: `testing`, `code-review`, `security`
- Operations: `debugging`, `observability`, `workspace-hygiene`

### Test Procedure:
Verify that each specialist relative path resolves to a valid `SKILL.md` file on disk.

---

## 3. References Suite: `all_internal_links_resolve`

### Assertion:
All internal markdown links (``[text](path/to/doc.md)``) must resolve to existing files on disk. Zero dead links are permitted.

### Test Procedure:
Execute an automated link crawler across all markdown files. Verify that 100% of relative target paths exist.

---

## 4. Execution Suite: `referenced_scripts_are_executable`

### Assertion:
Every script referenced in execution steps of any skill must:
1. Exist on disk.
2. Have executable permissions (`chmod +x`).
3. Pass language-specific syntax validation (`py_compile` for Python, `bash -n` for Bash, `swiftc` for Swift).
4. Contain no unexpanded placeholder commands (e.g. `<configured-script>` or `<path-to-repo>`).

---

## 5. Boundaries Suite: `generic_engineering_contains_no_android_specific_rules`

### Assertion:
Generic engineering skills (`engineering/validation/testing`, `engineering/validation/code-review`) must remain language- and platform-agnostic. 
Platform-specific frameworks (Jetpack Compose, Android Lifecycle, Coroutines, Swift SPM) must reside within their respective domain folders (`android/`, `xcode-project-setup/`) rather than polluting generic engineering context.

---

## 6. Regression Suite: Known Regressions

- **`nested_skill_discovery`**: Proves that no skill expects Antigravity to perform recursive automatic discovery.
- **`broken_relative_links`**: Proves that moving a file within subdirectories updates relative link depth.
- **`absolute_machine_paths`**: Proves that skills use portable relative paths or environment variables rather than hardcoded `/Users/<username>/...` paths.
- **`executable_placeholder_commands`**: Proves that sample commands provided to agents are either fully executable or explicitly marked as templates requiring input.

---

# Proving Workflow

When a change is proposed by `agent-audit`:
1. **Run Baseline**: Execute the relevant test suite against the current state. Record existing passes and failures.
2. **Apply Modification**: Let `skill-maintenance` or `skill-optimization` apply the minimal correct change.
3. **Run Regression**: Execute the entire test suite against the modified state.
4. **Evaluate Gate**:
   - Passed if all previously passing tests still pass AND the target defect is resolved.
   - Rejected if any new failure or regression is introduced.
