# ⚛️ Quantum-to-System Mapping

## 1. Introduction
Traditional testing is deterministic: `Input A -> Output B`. Real-world systems, however, exist in states of uncertainty (network flakes, race conditions). This framework maps quantum mechanical principles to software stress testing to better model this entropy.

## 2. Conceptual Mapping

### A. Superposition → Multi-State Inputs
* **Quantum Concept:** A qubit exists in a state $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$, representing a probability of being 0 or 1 simultaneously until measured.
* **System Equivalent:** A "Test State" is not a single JSON payload but a probabilistic definition of multiple potential payloads (e.g., "Valid User" AND "Malicious SQL Injection" simultaneously).
* **Implementation:** The harness will accept a `SuperposedPayload` object containing multiple potential mutations and their associated probability weights ($\alpha, \beta$).

### B. Probability Amplitudes → Execution Weights
* **Quantum Concept:** The probability of collapsing to state $|0\rangle$ is $|\alpha|^2$.
* **System Equivalent:** We assign configuration weights to distinct user behaviors.
    * $|\text{Normal}\rangle$: 0.8 weight (High probability)
    * $|\text{Attack}\rangle$: 0.2 weight (Low probability)
* **Implementation:** The runner uses a weighted random choice algorithm to "collapse" the superposed input into an actual HTTP request at the moment of execution.

### C. Measurement & Collapse → Risk Distribution
* **Quantum Concept:** Measuring a quantum system collapses the superposition into a single eigenstate.
* **System Equivalent:** Executing the request "collapses" the uncertainty into a concrete result (200 OK or 500 Error).
* **Implementation:** Instead of a binary "Pass/Fail" for a single run, we perform $N$ measurements (shots) to build a probability distribution of stability.
    * *Result:* "System has 95% Confidence of Stability."

## 3. Why Classical Testing Fails
Classical testing assumes the system is static. It checks `if x then y`. It fails to catch "Heisenbugs"—errors that only occur under specific, probabilistic conditions (like race conditions that happen 1% of the time). This quantum-inspired approach explicitly models that 1% probability.