---
name: clinical-session-agent-patterns
description: Domain patterns for AI agents handling clinical, therapy, and patient session documentation, SOAP/DAP notes, non-destructive note synthesis, privacy boundaries, and structured session exports.
license: Apache-2.0
metadata:
  author: Jeffery Forbes
  last-updated: '2026-09-05'
  keywords:
  - Clinical Documentation
  - Therapy Session
  - SOAP Note
  - DAP Note
  - AI Agent
  - Patient Privacy
  - HIPAA
  - Non-Destructive Synthesis
  - Export
---

# Clinical Session AI Agent Patterns

## Overview

AI agents assisting therapists, psychiatrists, and clinical practitioners must operate under strict non-destructive, privacy-conscious, and legally verifiable guidelines.

An AI agent in this domain should **augment** the clinician's workflow, never overwrite raw practitioner observations or diagnose autonomously.

---

## 1. Core Principles

1. **Non-Destructive Augmentation**: The AI summary and extracted insights are stored in companion fields (e.g. `aiReview`, `suggestedInsights`). They must never overwrite or delete the clinician's raw manual notes.
2. **Practitioner Sovereignty**: All AI suggestions require explicit practitioner review, approval, or editing before entering final clinical export records.
3. **Strict Privacy Boundaries (PHI/PII Redaction)**: Strip or tokenize identifiers (patient full name, phone numbers, addresses, SSN/NHS numbers) before transmitting session transcripts to external cloud LLMs.
4. **Structured Clinical Frameworks**: Format clinical summaries using industry standards:
   - **SOAP**: Subjective, Objective, Assessment, Plan.
   - **DAP**: Data, Assessment, Plan.
   - **BIRP**: Behavior, Intervention, Response, Plan.

---

## 2. Clinical Data Schemas

```kotlin
package com.example.app.clinical

import kotlinx.serialization.Serializable
import kotlinx.datetime.Instant

@Serializable
data class ClinicalSession(
    val id: String,
    val patientId: String,
    val timestamp: Instant,
    val durationSeconds: Int,
    val rawTranscription: String,
    val clinicianNotes: String, // Manual notes written by the therapist
    val aiEvaluation: AiSessionEvaluation? = null,
    val status: SessionStatus = SessionStatus.DRAFT
)

@Serializable
data class AiSessionEvaluation(
    val soapNote: SoapNote,
    val keyInsights: List<ClinicalInsight>,
    val riskFlags: List<RiskFlag>,
    val generatedAt: Instant,
    val reviewedByClinician: Boolean = false
)

@Serializable
data class SoapNote(
    val subjective: String, // Patient self-reported feelings, symptoms, experiences
    val objective: String,  // Observable behaviors, affect, speech patterns, appearance
    val assessment: String, // Clinical evaluation of progress, themes, coping mechanisms
    val plan: String        // Homework, next session goals, medication follow-ups
)

@Serializable
data class ClinicalInsight(
    val topic: String,
    val quoteContext: String,
    val therapeuticRelevance: String
)

@Serializable
data class RiskFlag(
    val severity: RiskSeverity, // LOW, MODERATE, CRITICAL
    val observation: String,
    val suggestedAction: String
)
```

---

## 3. Koog AI Agent Sequence for Session Review

When orchestrating through the Koog agent harness, decompose clinical processing into a multi-step declarative pipeline:

```
[Raw Audio Transcription]
          ↓
[1. PII Redaction & De-identification]
          ↓
[2. SOAP Structure Extraction]
          ↓
[3. Longitudinal Insight Comparison] (against previous sessions)
          ↓
[4. Safety & Risk Flag Detection]
          ↓
[Draft Review Presented to Clinician]
```

### Koog Prompt Guidelines:
- Instruct the model: `"You are a clinical documentation assistant assisting a licensed therapist. Do not provide medical diagnoses. Focus on organizing the patient's reported statements into Subjective, the clinician's noted observations into Objective, and thematic summaries into Assessment."`
- Request structured JSON matching `AiSessionEvaluation`.

---

## 4. Export Pipelines (PDF & Excel/CSV)

Therapists frequently export notes for insurance reimbursement (EHR systems) or legal compliance:

1. **PDF Export**:
   - Header: Session Date, Clinician ID, Patient Code (anonymized if sharing externally).
   - Section 1: Final Clinician Approved Notes (SOAP format).
   - Section 2: Session Key Themes & Milestones.
   - Disclaimer: *"Document assisted by AI documentation tooling and verified by licensed practitioner."*
2. **Excel / CSV Export**:
   - Tabular schema: `SessionDate | Duration | PrimaryThemes | PlanSummary | ClinicianSignOff`.

---

## Deep References
Load on-demand using `view_file`:
- **[SOAP & DAP Note Templates](./references/soap-dap-templates.md)**: Structured note templates, clinical fields, and privacy scrubbing protocols.
