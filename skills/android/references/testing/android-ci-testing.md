# Android CI & Test Automation Strategy

## Purpose

Architecture, job partitioning, and automation strategies for Android Continuous Integration (CI) pipelines.

---

## 1. CI Pipeline Stages & Job Partitioning

To maintain fast feedback cycles while ensuring quality, divide CI automation into tiered stages:

### Stage 1: Fast PR Checks (Host-Side)
Run on every pull/merge request. Must complete within a few minutes.
- **Build from scratch**: Verify project compiles and dependency graph resolves (`./gradlew assembleDebug`).
- **Static Analysis & Lint**: Style enforcement and static checks (`./gradlew lintDebug detekt ktlintCheck`).
- **Local Host-Side Tests**: Fast JVM unit tests and Robolectric tests (`./gradlew testDebugUnitTest`).

### Stage 2: Instrumented & Regression Checks
Run on PRs modifying core architecture, or on merge to main.
- **Device Provisioning via Gradle Managed Devices (GMD)**: Define emulator targets directly in Gradle (e.g., Pixel 6 API 33) to avoid complex runner emulator shell scripts:
  ```kotlin
  android {
      testOptions {
          managedDevices {
              devices {
                  maybeCreate<com.android.build.api.dsl.ManagedVirtualDevice>("pixel6Api33").apply {
                      device = "Pixel 6"
                      apiLevel = 33
                      systemImageSource = "aosp"
                  }
              }
          }
      }
  }
  ```
  Run with: `./gradlew pixel6Api33Check`.
- **Device Farms**: For wide hardware coverage and physical device matrices, delegate to services such as Firebase Test Lab.

---

## 2. Screenshot Testing in CI

### Handling Cross-Platform Rendering Drift
Different operating systems (macOS developer workstations vs. Linux CI runners) produce minor rasterization differences (subpixel text rendering, anti-aliasing, shadow gradients).
1. **Tolerance Thresholding**: Configure the comparator with a small tolerance (e.g. 0.5% - 1% pixel diff or SSIM structural diff) to avoid false positives.
2. **Server-Side Golden Generation**: If pixel-perfect comparison is required:
   - Run verification on CI.
   - If tests fail, run screenshot recording on CI (`./gradlew recordRoborazziDebug` or equivalent).
   - Have CI commit updated reference images back to the feature branch for PR review and approval.

---

## 3. Performance Benchmarks Automation

- **Physical Devices Required**: Microbenchmark and Macrobenchmark require real physical hardware to provide deterministic, non-throttled timing. Never run benchmark regressions on virtual emulators.
- **Scheduled / Nightly Execution**: Benchmarks take significant time and resources. Run them on a scheduled cadence (e.g. nightly or post-merge), not on every PR.
- **Noise Reduction via Step-Fitting**: Single-build runs fluctuate. Use a rolling window of historical benchmark runs ("step fitting") to detect true regressions rather than temporary system noise.

---

## 4. Test Coverage Regression Checks

- **Separate Coverage Metrics**: Always maintain separate coverage metrics for **Unit Tests** and **Instrumented/UI Tests**.
  - Unit tests verify granular edge cases with high assertion density per line.
  - Instrumented/UI tests traverse deep application code paths with shallow assertion density. Blending them dilutes signal and masks missing unit test coverage.
- **Delta Thresholds**: Configure CI to alert or block if test coverage decreases relative to the target branch.
