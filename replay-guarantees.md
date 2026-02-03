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

## 4. Example: Before vs After Learning
The following JSON snippet demonstrates how the system's internal state evolves deterministically after observing a failure in the SQL injection vector.

**Epoch T (Baseline):**
```json
{
  "states": [
    { "name": "|Normal_User>", "weight": 0.80 },
    { "name": "|SQL_Injector>", "weight": 0.20 }
  ]
}
```

*Event: `|SQL_Injector>` triggers a crash (Latency: 0ms).*

**Epoch T+1 (Refined Risk):**
```json
{
  "states": [
    { "name": "|Normal_User>", "weight": 0.70 }, 
    { "name": "|SQL_Injector>", "weight": 0.30 }
  ]
}
```
*Note: The weight increased by exactly 0.10 (Constraint A max velocity), shifting probability mass from the safe state to the risky state.*