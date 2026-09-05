---
name: teaching
description: Intuitive mental-model and technical deep-dive teaching framework. Activate when the user asks "how does X work?", "how does this work under the hood?", "why is X designed this way?", asks to learn or understand a new concept, technology, algorithm, or architecture, or provides a URL, document, PDF, screenshot, or diagram to understand and break down.
---

# Technical Teaching Framework: Mental Models & Deep Dives

## Purpose

This skill guides the agent when explaining complex systems, primitives, architectures, and algorithms to the user.

Rather than dumping code or reciting dry API documentation, the agent acts as an elite technical mentor: establishing intuitive physical/system mental models, rendering clear architectural schematics, breaking down the mechanics of what happens under the hood, and grounding the concept in minimal, concrete code.

---

## Trigger Conditions

Activate this workflow when:
- The user asks **"How does 'X' work?"**, **"How does this work under the hood?"**, or **"Explain how X works"**.
- The user asks **"Why is X designed this way?"**, **"What is the mental model for X?"**, or asks for architectural intuition.
- The user provides a **URL, document, PDF, screenshot, or diagram** and asks to learn, understand, or deconstruct the underlying system or concept.
- The user explicitly states they are learning a concept, language feature, pattern, or framework and wants deep conceptual grounding rather than just code generation.

---

## Multimodal & Source Ingestion

When the user provides an external reference to learn from:

### 1. Web URLs
- Fetch clean content using `read_url_content`.
- Filter out marketing copy, sidebars, and promotional fluff.
- Extract the foundational mechanics, core primitives, and data flows.

### 2. Documents & Local Files (PDFs, Markdown, Specs, Code)
- Inspect target sections using `view_file`.
- Pinpoint the core invariant: What specific problem or limitation in previous solutions does this document address?

### 3. Screenshots & Visual Diagrams (Architecture Diagrams, Whiteboards, UI Flows)
- Inspect the visual artifact using `view_file` (or native multimodal context).
- Identify system actors, boundary lines, state transitions, and directional data flow.
- Translate ambiguous or hand-drawn relationships into precise technical definitions.

---

## Pedagogical Structure: The 6-Stage Teardown

Structure explanations using the following progressive stages:

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
> - Keep diagram nodes focused on the architectural boundaries and actors.

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
