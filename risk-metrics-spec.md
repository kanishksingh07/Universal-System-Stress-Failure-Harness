# 📏 Formal Risk Metric Specification

## 1. System Confidence ($\mathcal{C}$)
**Definition:** The statistical probability that a single request, selected from the superposition state, will execute successfully without a system crash (HTTP 500) or unhandled exception.

* **Type:** Float (Precision: 4 decimal places)
* **Formula:** $$\mathcal{C} = \frac{N_{success}}{N_{total}}$$
* **Dependencies:** Requires $N_{total} > 0$. If $N_{total} = 0$, $\mathcal{C}$ is undefined (Implementation: defaults to 0.0).

## 2. Stability Index ($\mathcal{S}$)
**Definition:** A normalized measure of latency consistency. It quantifies the system's resistance to "jitter" or performance degradation under probabilistic load.

* **Type:** Float (Precision: 4 decimal places)
* **Formula:**
    $$\mathcal{S} = \max\left(0.0, 1.0 - \frac{\sigma}{\mu}\right)$$
    * Where $\sigma$ is the standard deviation of latency.
    * Where $\mu$ is the mean latency.
* **Edge Case:** If $\mu = 0$, $\mathcal{S} = 1.0$ (Instant response implies perfect stability).

## 3. Final Risk Score ($\mathcal{R}$)
**Definition:** The aggregated probability of critical failure or unacceptable instability in a production environment.

* **Type:** Float (Precision: 4 decimal places)
* **Formula:**
    $$\mathcal{R} = 1.0 - (\mathcal{C} \times \mathcal{S})$$
* **Interpretation:** A score of $0.0$ implies perfect reliability. A score of $1.0$ implies total system failure.