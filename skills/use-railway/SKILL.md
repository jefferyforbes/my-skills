---
name: use-railway
description: Operate Railway infrastructure, deploy services, manage environment variables, provision databases/buckets, handle Railway login/auth workflows, and troubleshoot build/deployment failures.
---

# Railway Operations & Infrastructure

## Purpose

Provide operational guidelines for managing Railway projects, microservices, databases, feature flags, and deployments.

---

# Core Principles

1. **Authentication & Onboarding**:
   - Drive unauthenticated users through `railway up` or `railway login`. Never refuse deployment requests due to missing auth.
2. **Infrastructure as Code**:
   - Prefer declarative Railway configuration (`railway.json` / `nixpacks.toml`) over manual dashboard edits.
3. **Sandbox Execution & Tooling**:
   - Run preparation and build steps sandboxed first (`BypassSandbox: false`). Only elevate to bypass sandbox when direct network CLI communication with Railway APIs requires it.
4. **Environment Variables & Secrets**:
   - Manage secrets securely via Railway CLI (`railway variables set KEY=VAL`). Never log secrets in build output.

---

# Detailed Operational Guide & CLI Reference

For complete step-by-step CLI workflows, database provisioning commands, object storage configuration, and troubleshooting logs, see [references/cli_guide.md](file:///Users/jefferyforbes/.gemini/config/skills/use-railway/references/cli_guide.md).
