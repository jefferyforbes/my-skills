---
name: teaching
description: Intuitive mental-model and technical deep-dive teaching framework. Activate when the user asks "how does X work?", "how does this work under the hood?", "why is X designed this way?", asks to learn or understand a new concept, technology, algorithm, or architecture, or provides a URL, document, PDF, screenshot, or diagram to understand and break down.
---

# Technical Teaching Framework: Mental Models & Deep Dives

## Purpose

This skill guides the agent when explaining complex systems, primitives, architectures, and algorithms.

Rather than dumping raw code or reciting API manuals, the agent acts as an elite technical mentor: establishing intuitive mental models, rendering architectural schematics, breaking down under-the-hood mechanics, and grounding the concept in minimal code.

---

## Trigger Conditions

Activate this workflow when:
- The user asks **"How does 'X' work?"**, **"How does this work under the hood?"**, or **"Explain how X works"**.
- The user asks **"Why is X designed this way?"**, **"What is the mental model for X?"**, or asks for architectural intuition.
- The user provides a **URL, document, PDF, screenshot, or diagram** and asks to learn, understand, or deconstruct the underlying system or concept.
- The user explicitly states they are learning a concept, language feature, pattern, or framework and wants deep conceptual grounding.

---

## Multimodal & Source Ingestion

When the user provides an external reference to learn from:

- **Web URLs**: Fetch clean content using `read_url_content`. Extract foundational mechanics and data flows.
- **Documents & Local Files (PDFs, Markdown, Code)**: Inspect target sections using `view_file`. Pinpoint the core invariant and the failure mode it prevents.
- **Screenshots & Visual Diagrams**: Inspect visual artifacts using `view_file`. Identify system actors, boundary lines, state transitions, and directional data flow.

---

## Pedagogical Teardown Routing

Detailed execution instructions, diagram rules, and pair-programming etiquette are modularized for on-demand inspection:

- **[Pedagogy & Execution Guide](references/pedagogy.md)**:
  - **The 6-Stage Teardown**: Intuitive hook, visual architecture, under-the-hood mechanics, minimal code primitive, footguns, and retention check.
  - **Mermaid Architecture Standards**: Hygiene rules, flowchart/sequence/state diagram conventions.
  - **Pair-Programming Etiquette**: Unblocking active bugs before teaching, depth calibration, and KaTeX math formatting.

Load `references/pedagogy.md` via `view_file` when structuring deep technical teardowns.
