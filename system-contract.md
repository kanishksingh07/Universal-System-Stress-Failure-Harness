# 📜 Universal System Contract

> **Status:** FINAL
> **Scope:** Universal System Stress Failure Harness

This document defines the **Non-Negotiable Guarantees** provided by the harness. Any deviation from these rules is considered a critical defect in the harness itself.

---

## 1. The Integrity Contract (Input/Output)

### 1.1 Input Pre-Conditions
The system **MUST** reject execution (ContractViolationError) unless:
* **Sum of Weights:** The weights of all superposition states sum to `1.0` (Tolerance: $\pm 0.01$).
* **Payload Integrity:** Every defined state has a non-empty name and a valid payload dictionary.
* **Configuration:** Both `target_system` and `quantum_settings` are present in the loaded config.

### 1.2 Output Post-Conditions
The system **GUARANTEES** the output artifact (`quantum_metrics.json`):
* **Schema Compliance:** Always contains `shot_id`, `collapsed_state`, `status`, `latency_ms`.
* **Latency Invariant:** $\forall \text{result} : \text{latency\_ms} \ge 0$.
* **Status Invariant:** `status` $\in$ `{"success", "failure"}`.

### 1.3 Failure Handling
* **Graceful Crash:** Internal exceptions in the harness (not the target) triggers `SystemExit(1)` with a stack trace.
* **Metric Boundaries:** A Risk Score $> 1.0$ triggers an immediate `ContractViolationError`.

---

## 2. The Safety Contract (Adaptive Boundaries)

When running in **Adaptive Mode (Layer 3)**, the system enforces strict physics on its own learning:

### 2.1 The Bounded Growth Guarantee
**"No matter how catastrophic the failures, the system will never mutate a test state by more than 10% in a single run."**
* **Invariant:** $|\Delta weight| \le 0.10$ per epoch.
* **Mechanism:** `actual_delta = max(-0.10, min(0.10, raw_delta))`

### 2.2 The Entropy Floor Guarantee
**"The system will never stop testing 'Normal' users completely."**
* **Invariant:** $\forall \text{state} : \text{weight} \ge 0.05$.
* **Mechanism:** Prevents "Mode Collapse" where the system focuses 100% on attacks and forgets baseline functionality.

---

## 3. The Determinism Contract

### 3.1 The Replay Guarantee
**"Given the same Initial State and the same Seed, the system will learn the exact same lessons."**
* **Invariant:** `Hash(Run_A_Output) == Hash(Run_B_Output)` given `Seed_A == Seed_B`.
* **Mechanism:** All probabilistic collapses and weight updates are derived from a seeded PRNG.

### 3.2 The No-Mutation Guarantee
**"History is immutable."**
* The system updates *future* probabilities based on *past* results.
* It **NEVER** modifies logs, metrics, or artifacts from previous epochs.

---

## 4. The Boundary Contract (Negative Space)

What the system **explicitly DOES NOT do**:

| Behavior | Guarantee |
| :--- | :--- |
| **Execution** | The harness NEVER executes payloads. It only delivers them to the Target Endpoint. |
| **Privilege** | The harness NEVER requests `sudo` or Admin privileges. |
| **Persistence** | The harness is stateless between processes. It leaves no daemons or cron jobs. |
| **Network** | The harness ONLY talks to the configured `target_system` URL. No telemetry. |

---

## 5. Verification
To verify these contracts, run:
```bash
python test_drift_safety.py  # Verifies Safety Contracts (Growth, Entropy)
# (Replay verification script pending in misuse-tests/)
```
