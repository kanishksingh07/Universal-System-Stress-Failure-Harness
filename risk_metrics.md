# 📉 Quantum Risk Metrics

## Overview
Unlike classical testing, which outputs a binary "Pass/Fail", the Quantum-Adversarial layer outputs a **Risk Distribution**. We measure the system's behavior across multiple probabilistic states to derive these metrics.

## 1. Confidence Score ($\mathcal{C}$)
The probability that the system will handle a superposition of user states without crashing.
* **Formula:** $\mathcal{C} = \frac{N_{success}}{N_{total}}$
* **Interpretation:** A score of 95% means the system fails 1 in 20 times under probabilistic load.

## 2. Stability Index ($\mathcal{S}$)
A measure of latency consistency. A system that averages 200ms but spikes to 5000ms is "Unstable" even if it doesn't crash.
* **Formula:** $\mathcal{S} = 1 - (\frac{\sigma}{\mu})$ 
* *(Where $\sigma$ is standard deviation and $\mu$ is mean latency)*

## 3. Calculated Risk ($\mathcal{R}$)
The unified metric for deployment decisions.
* **Formula:** $\mathcal{R} = 1 - (\mathcal{C} \times \mathcal{S})$
* **Thresholds:**
    * $< 10\%$: Production Ready
    * $> 20\%$: Critical Risk (Do not deploy)