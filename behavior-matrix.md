# 🧭 System Behavior Matrix

> **Status:** FINAL
> **Scope:** Universal System Stress Failure Harness

This matrix defines the **Deterministic Behavior** of the system under specific conditions. This acts as the "Truth Table" for the harness.

## 1. Safety & Stability (Layer 3)

| Condition | Trigger Value | Guaranteed Behavior | Rationale |
| :--- | :--- | :--- | :--- |
| **Ambiguous Failure** | Failure Rate > 90% | **REFUSAL TO LEARN** | If everything fails, the signal is noise. We freeze state to prevent learning bad habits. |
| **Rapid Updates** | Epochs since update < 3 | **COOLDOWN SKIP** | Prevents oscillating feedback loops (Control Theory: Damping). |
| **Runaway Growth** | Delta > 0.10 | **VELOCITY CLAMP** (`0.10`) | Limits the "Learn Rate" to prevent sudden state shocks. |
| **Mode Collapse** | Weight < 0.05 | **ENTROPY FLOOR** (`0.05`) | Ensures we never stop testing baseline/safe users. |
| **Saturation** | Weight > 0.60 | **SATURATION CEILING** (`0.60`) | Prevents one vector from dominating the entire test strategy. |

## 2. Integrity & Error Handling (Layer 1 & 2)

| Condition | Context | Guaranteed Behavior |
| :--- | :--- | :--- |
| **Invalid Config** | Missing `quantum_settings` | **CRASH** (`SystemExit 1`) |
| **Network Timeout** | Connection to Target | **Log Failure** (don't crash harness) |
| **Risk Overflow** | Risk Score > 1.0 | **ContractViolationError** |
| **Weight Sum Mismatch** | $\Sigma \ne 1.0 \pm 0.01$ | **ContractViolationError** |

## 3. Operational Logic

| Input State | Action | Outcome |
| :--- | :--- | :--- |
| **High Latency** | Avg Latency > 100ms | **Increase Risk Weight** (Logic: System is struggling, push harder) |
| **Zero Failures** | Clean Run | **Decay Risk Weight** (Logic: System is stable, look elsewhere) |
| **Manual Override** | `freeze_learning: true` | **No Weight Updates** |

---

## 4. Verification Check
To validate this matrix against the code:
1. **Ambiguity Check:** `test_safety_checks.py`
2. **Growth Check:** `test_drift_safety.py`
3. **Integrity Check:** `system-contract.md` verification.
