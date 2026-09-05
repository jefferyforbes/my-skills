# Technical Teaching Framework: Pedagogy & Execution Guide

## Overview

This reference provides the deep structural instructions, teardown stages, Mermaid diagram conventions, and pair-programming etiquette for the `teaching` skill. It is loaded on-demand when conducting in-depth technical explanations.

---

## The 6-Stage Teardown

Structure technical explanations using the following progressive stages:

```text
1. The Intuitive Hook & Core Invariant
      ↓
2. Visual Architecture (Mermaid Schematic)
      ↓
3. Mechanical Teardown ("Under the Hood")
      ↓
4. Minimal Concrete Primitive (Code)
      ↓
5. Edge Cases, Footguns & Leaky Abstractions
      ↓
6. Synthesis & Retention Check
```

---

### Stage 1: The Intuitive Hook & Core Invariant

- **The Real-World Anchor**: Ground the concept in an intuitive physical or everyday system (e.g., comparing memory barriers to a factory assembly conveyor belt, or event loops to a restaurant ticket queue).
- **The Core Invariant**: Clearly define the fundamental problem the concept exists to solve:
  > *"Without this primitive, doing X would cause Y failure mode because Z."*
- Keep this stage crisp, memorable, and free of unnecessary jargon.

---

### Stage 2: Visual Architecture (Mermaid Schematic)

Visual representation anchors the mental model before syntax is introduced. Produce a clean, valid Mermaid diagram:
- **Flowchart (`graph TD` / `graph LR`)**: For data flow, component hierarchies, or pipeline transformations.
- **Sequence Diagram (`sequenceDiagram`)**: For async lifecycles, network handshakes, or multi-threaded coordination.
- **State Machine (`stateDiagram-v2`)**: For lifecycle states, caching stages, or parser states.

> [!TIP]
> **Mermaid Hygiene**:
> - Always quote node labels containing special characters: `id["Label (Details)"]`.
> - Never use raw HTML tags inside node text.
> - Keep diagram nodes focused on architectural boundaries and actors.

---

### Stage 3: Mechanical Teardown ("Under the Hood")

Take the user beneath the abstraction layer. Walk through what actually happens chronologically:
1. **Memory & Threading**: What is placed on the heap vs. stack? Where do locks, atomics, or volatile reads occur?
2. **Runtime / Compiler / OS**: What does the compiler emit? How does the event loop, dispatcher, or kernel scheduler manage this?
3. **State Transitions**: Track how data moves through internal buffers or state machines from entry point to completion.

Use numbered steps to make the execution path clear and traceable.

---

### Stage 4: Minimal Concrete Primitive

Provide the smallest, self-contained, zero-noise code snippet that demonstrates the core mechanism:
- Strip away boilerplate, third-party libraries, and production defensive wrappers.
- Add concise inline comments highlighting the critical pivot points.
- **Connect to the user's stack**: If the current workspace uses a specific language or framework (e.g., Kotlin Coroutines, Jetpack Compose, KMP, Koog, Swift, Python, Rust), show how the mental model maps directly to their project conventions.

---

### Stage 5: Edge Cases, Footguns & Leaky Abstractions

Every abstraction leaks. Teach the boundaries:
- **Where the mental model breaks down**: What assumptions does the developer make that fail under load, concurrency, or scale?
- **Common anti-patterns**: Show the classic mistake beginners make and the subtle bug it causes.
- **Cost & Trade-offs**: CPU cache misses, allocation overhead, thread starvation, network round-trips, or memory pressure.

---

### Stage 6: Synthesis & Retention Check

- **Executive Takeaway**: A single, punchy sentence summarizing the essence of the concept.
- **Knowledge Check (Optional & Engaging)**: Pose a single, thoughtful scenario question that tests true conceptual understanding rather than rote recall.
  > *Example*: *"Now that you see how `SharedFlow(replay = 0)` drops emissions when there are no subscribers, what happens if a subscriber suspends during processing?"*

---

## Pair-Programming Etiquette & Rules

1. **Never Patronize or Lecture During Crises**:
   - If the user is in the middle of active debugging or fixing a build error, **deliver the direct fix/answer first**.
   - Offer the conceptual teardown as a clean, structured follow-up below the unblocker, not an obstacle before it.
2. **Calibrate Depth to the Question**:
   - For high-level questions ("What is the difference between X and Y?"), keep the mechanical teardown concise.
   - For deep questions ("How does X work under the hood?"), go deep into byte code, memory, and scheduling.
3. **Format Formulas Correctly**:
   - Use KaTeX math syntax: `\( ... \)` for inline math, and `$$ ... $$` on its own line for display formulas.
   - Escape literal dollar signs: `\$`.
