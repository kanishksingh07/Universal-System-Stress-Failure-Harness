# 🔁 Replay Guarantees

## 1. The Contract
The system guarantees **Bitwise Identity** on replay.
* **Input:** `probability-config.yaml` (including `seed`).
* **Output:** `quantum_metrics.json`.

## 2. Verification Protocol
To verify compliance:
1.  Run the system with Seed `42`. Save output as `run_A.json`.
2.  Run the system with Seed `42`. Save output as `run_B.json`.
3.  **Assertion:** `Hash(run_A) == Hash(run_B)`.

## 3. Violation
Any deviation in the output stream (even a single different "Collapse" choice) constitutes a critical system failure.