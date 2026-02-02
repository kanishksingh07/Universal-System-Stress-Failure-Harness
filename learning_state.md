# 🧠 Learning State Definition

## 1. The "Brain" of the System
The system's "State" is defined not by neural weights, but by the **Probabilistic Weights** of the Superposition model.
* **State Vector ($S$):** A list of weights $\{\omega_1, \omega_2, ..., \omega_n\}$ corresponding to each test payload (e.g., Normal, SQL, Boundary).
* **Invariant:** $\sum \omega_i = 1.0$.

## 2. Learning vs. Prediction
* **Prediction (ML):** Guessing what *might* happen based on past data.
* **Learning (Control):** Adjusting $\omega_i$ based on *observed* data.
    * If `|SQL_Injector>` crashes the system, its "Risk Importance" ($\omega_{sql}$) increases.
    * This forces the Superposition Engine to select it more frequently in the next epoch.

## 3. The Update Cycle
1.  **Execute:** Run Batch $N$ with weights $S_t$.
2.  **Observe:** Collect metrics (Success, Failure, Latency).
3.  **Learn:** Apply update rules to generate $S_{t+1}$.
4.  **Repeat.**