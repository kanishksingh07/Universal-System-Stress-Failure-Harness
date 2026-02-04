# 🔌 Integration Readiness Guide

> **Audience:** DevOps, SRE, and CI/CD Engineers
> **Purpose:** "Zero Configuration Surprise" deployment.

## 1. Embeddability
This harness is designed to be embedded as a **Git Submodule** or **Sidecar Container**.

### Recommended Structure
```text
/your-service-repo
  /tests
    /stress-harness (submodule)
      /config (override these!)
      /logs (mount execution volume here)
```

## 2. CI/CD Pipeline Integration

### The "Gatekeeper" Pattern
Run the harness as a blocking stage in your pipeline.
```yaml
# Example GitLab CI / GitHub Actions step
stress-test:
  stage: verify
  script:
    - pip install -r tests/stress-harness/requirements.txt
    - python tests/stress-harness/superposition_runner.py
  artifacts:
    reports:
      junit: tests/stress-harness/metrics.json 
```

### Exit Codes
The harness adheres to standard UNIX exit codes:
* **0 (OK):** Test suite completed successfully.
* **1 (Error):** Contract Violation or Harness Internal Error.
* **Note:** A high failure rate in the *Target* does NOT cause the harness to exit with 1. It exits with 0 (since it successfully measured the failures). Check `quantum_metrics.json` for pass/fail logic.

## 3. Production Readiness Checklist
- [ ] **Config Override:** Ensure `config/*.yaml` points to STAGING, not PRODUCTION.
- [ ] **Resource Limits:** Set `max_workers` based on the CI runner's CPU.
- [ ] **Artifacts:** Ensure `logs/` directory is writable and persisted.
- [ ] **Dependencies:** Vendor `requirements.txt` if air-gapped.

## 4. Determinism
To run in **Regression Mode** (exact same test vector every time):
* Set `quantum_settings.seed: <INTEGER>` in `probability-config.yaml`.
* This guarantees identical input generation for debugging.
