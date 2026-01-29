# 🚧 Metric Bounds & Invariants

## 1. Universal Bounds
All metrics must strictly adhere to the closed interval $[0.0, 1.0]$.
* $\forall m \in \{\mathcal{C}, \mathcal{S}, \mathcal{R}\} : 0.0 \le m \le 1.0$

## 2. Invalid States
The system must raise a `ContractViolationError` if:
* $N_{total}$ (Shots) is negative.
* Calculated $\mathcal{R}$ exceeds 1.0 due to floating-point errors.
* Latency values are negative (Time travel is not permitted).

## 3. Risk Thresholds (The "Red Line")
| Metric | Safe Range | Warning Range | Critical Failure |
| :--- | :--- | :--- | :--- |
| **Confidence** | $0.99 - 1.00$ | $0.90 - 0.98$ | $< 0.90$ |
| **Stability** | $0.80 - 1.00$ | $0.60 - 0.79$ | $< 0.60$ |
| **Final Risk** | $0.00 - 0.10$ | $0.11 - 0.25$ | $> 0.25$ |

**Enforcement:**
Any run resulting in **Critical Failure** must exit with a non-zero status code (System exit 1).