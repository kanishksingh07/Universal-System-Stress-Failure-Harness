# ⚓ Stability & Drift Constraints

## 1. The Drift Problem
"Drift" occurs when an adaptive system over-optimizes for recent data, forgetting historical context. To prevent this, we enforce strict kinetic limits on how fast the Probability Wavefunction can change.

## 2. Safety Constraints
* **Constraint A (Max Velocity):** $\Delta \omega \le 0.10$. A weight cannot change by more than 10% in a single epoch, regardless of failure severity.
* **Constraint B (Cooldown):** Learning updates can only trigger once every $N$ epochs (Epoch Cooldown).
* **Constraint C (Entropy Floor):** The system must maintain at least 5% probability for *all* states to preventing "Mode Collapse" (where it stops testing normal scenarios entirely).

## 3. The "Panic" Circuit
12. If the total change in system state ($\sum |\Delta \omega_i|$) exceeds $0.25$ in one step, the system must trigger a `SafetyReset` and revert to the baseline configuration.

## 4. Refusal to Learn (Constraint D)
The system is explicitly designed to **reject** updates in specific dangerous scenarios:
*   **Scenario:** If the feedback signal is "ambiguous" (e.g., Target returns 500 Internal Error for *every* request, making it impossible to distinguish attack success from system outage).
*   **Action:** The Learning Layer freezes. $S_{t+1} = S_t$.
*   **Reasoning:** Learning from noise creates drift. If we cannot correlate input to output with >90% confidence, we do not update the model.