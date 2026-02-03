# 📜 System Contracts & Guarantees

## 1. Input Contract (Pre-Conditions)
The system rejects execution unless:
* **Sum of Weights:** The weights of all superposition states must sum to approximately 1.0 (tolerance $\pm 0.01$).
* **Payload Integrity:** Every state must have a non-empty name and a valid payload dictionary.
* **Configuration:** `target_system` and `quantum_settings` must be present.

## 2. Output Contract (Post-Conditions)
The system guarantees:
* **Schema Compliance:** The `quantum_metrics.json` will always contain: `shot_id`, `collapsed_state`, `status`, `latency_ms`.
* **Latency Invariant:** $\forall \text{result} : \text{latency\_ms} \ge 0$.
* **Status Invariant:** `status` is strictly an element of `{"success", "failure"}`.

## 3. Failure Contract (Silent Failure Impossible)
* **Crash Handling:** Any internal exception in the runner logic (not the target) must trigger a `SystemExit(1)` and print a stack trace.
* **Metric Boundaries:** If `collapse_engine` produces a Risk Score $> 1.0$, the system must raise `ContractViolationError`.