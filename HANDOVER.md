# 📦 Universal Stress Harness - Final Handover

> **Version:** 1.0.0 (Release Candidate)
> **Integrity:** Verified
> **Safety:** Enforced

## 📖 Overview
This repository delivers a **Universal System Stress Failure Harness**, a tri-layer testing engine designed to break APIs, Functions, and Models under controlled uncertainty.

## 🚀 Quick Start
### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Choose Your Mode
| Mode | Purpose | Command | Config |
| :--- | :--- | :--- | :--- |
| **Layer 1** | **Stress & Fuzzing** (Find bugs) | `python runner.py` | `config/mutation-config.yaml` |
| **Layer 2** | **Risk Profiling** (Measure Stability) | `python superposition_runner.py` | `config/probability-config.yaml` |
| **Layer 3** | **Adaptive Learning** (Auto-tuning) | *(Integrated in Layer 2 runner if adaptive flag set)* | `config/probability-config.yaml` |

## 🛠️ Configuration
The system is **100% Config-Driven**. No code changes required to switch targets.

### Target: HTTP API
```yaml
target_system:
  type: api
  url: "http://localhost:8080/v1/analyze"
  timeout_seconds: 2
```

### Target: Local Python Function
```yaml
target_system:
  type: function
  module_path: "local_targets"
  function_name: "dummy_risk_engine"
```

## 📂 Key Deliverables
* **[System Contract](system-contract.md):** The non-negotiable guarantees.
* **[Behavior Matrix](behavior-matrix.md):** The deterministic behavior guide.
* **[Host Safety](host-safety.md):** Security and isolation proofs.
* **[Failure Containment](failure-containment.md):** Blast radius documentation.

## ✅ Verification
To verify the system integrity before deployment:
```bash
python test_drift_safety.py         # Verify Safety Brakes
python misuse-tests/test_no_exec.py # Verify Host Safety
```