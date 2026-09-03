---
name: gemini-omni-flash-api
description: Generative video editing, text-to-video, image-referenced video generation, and video transitions using Gemini Omni 1.1 Flash (gemini-omni-1.1-flash) via google-genai SDK.
---

# Gemini Omni 1.1 Flash Video Generation & Editing

## Purpose

Provide operational rules for generating, editing, and extending video content using Gemini Omni 1.1 Flash (`gemini-omni-1.1-flash`).

---

# Core Principles & Rules

1. **Model ID**: Always use `gemini-omni-1.1-flash` via the official `google-genai` Python SDK or `@google/genai` JS SDK.
2. **Video Pre-processing**:
   - High-resolution or long source videos must be stripped/pre-processed using ffmpeg before sending to the model to optimize latency and token cost.
3. **Sound Regeneration**:
   - Strip source audio during turn-by-turn video editing for full sound regeneration.
4. **Structured Task Flow**:
   - Pre-process source media -> Invoke Omni Flash -> Post-process output.

---

# Complete Video Editing & ffmpeg Reference Guide

For step-by-step code samples, ffmpeg preprocessing scripts, turn-by-turn editing flows, and parallel execution pipelines, see [references/omni-flash-guide.md](file:///Users/jefferyforbes/.gemini/config/plugins/gemini-api/skills/gemini-omni-flash-api/references/omni-flash-guide.md).
