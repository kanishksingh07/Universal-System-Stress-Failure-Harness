# 🚦 Signal Boundaries & Limits

## 1. Learning Signals (Triggers)
The system adapts based on **Negative Reinforcement Signals**:
* **Hard Failure:** HTTP 500 / Exception. (Strong Signal: Risk $\uparrow \uparrow$)
* **Instability:** Latency > $2\sigma$ (Standard Deviation). (Weak Signal: Risk $\uparrow$)
* **Success:** HTTP 200. (Decay Signal: Risk $\downarrow$)

## 2. Safety Boundaries (The Red Lines)
To prevent "Runaway Learning" (where one state consumes 100% probability), we enforce:
* **Saturation Limit:** No weight can exceed $0.60$ (60%).
* **Minimum Floor:** No weight can drop below $0.05$ (5%).
* **Max Delta:** A weight cannot change by more than $\pm 0.10$ in a single step.

## 3. Determinism Contract
Given Initial State $S_0$ and Seed $K$, the sequence of updates $S_0 \rightarrow S_1 \rightarrow S_2$ must be mathematically identical on every replay.

jhkjhkjh