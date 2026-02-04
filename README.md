# ⚛️ Quantum-Adversarial Stress Harness

**A config-driven, probabilistic, and adaptive stress testing system designed to break APIs, Internal Functions, and AI Models under uncertainty.**

## 📖 Overview
This repository contains a tri-layer stress harness that evolves from simple bug hunting to autonomous risk management:

1.  **Layer 1 (Universal Harness):** A high-volume, deterministic stress tester for finding hard crashes and bugs.
2.  **Layer 2 (Quantum-Adversarial):** A probabilistic engine that models "Superposition" (multiple potential input states) and "Collapse" to calculate a system's **Risk Profile**.
3.  **Layer 3 (Adaptive Learning):** An autonomous feedback loop that **learns from failures**, automatically adjusting risk weights to focus on weak points while respecting strict safety boundaries.

It follows a **Zero Code Change** philosophy: switch between testing an API, a local function, or an AI model purely by changing the configuration.

---

## 🚀 Key Features

### 🛡️ Layer 1: Universal Stress (Deterministic)
* **Universal Targets:** Test HTTP APIs or Local Python Functions via dynamic loading.
* **Hostile Mutations:** Automatically generates SQL injection, Deep JSON nesting, Regex Bombs, and Unicode overflows.
* **High Volume:** Generates thousands of test cases using random entropy.

### ⚛️ Layer 2: Quantum-Adversarial (Probabilistic)
* **Superposition Modeling:** Define a "User State" as a weighted probability cloud (e.g., 80% Normal, 15% Malicious).
* **Collapse Engine:** "Measures" the system 100+ times to collapse uncertainty into a single reality.
* **Risk Metrics:** Calculates **Confidence Score** and **Stability Index** (latency variance).

### 🧠 Layer 3: Adaptive Learning (Autonomous)
* **Self-Healing State:** Automatically increases the probability of testing scenarios that cause crashes or latency spikes.
* **Safety Brakes:** Enforces **Max Delta** (velocity limits) and **Entropy Floors** to prevent runaway learning.
* **Explainable AI (XAI):** Logs *why* a weight was changed (e.g., "Failure Detected -> Increased Weight by 0.05").

---

## 📂 Project Structure

```text
stress-harness/
├── config/
│   ├── mutation-config.yaml    # Layer 1 Config
│   └── probability-config.yaml # Layer 2 Config
├── adaptive_layer/             # NEW: Layer 3 Logic
│   ├── learning_engine.py      # The Brain (Update Rules & Safety Brakes)
│   └── __init__.py
├── quantum_layer/              # Layer 2 Logic
│   ├── superposition.py
│   └── collapse_engine.py
├── generators/                 # Mutation payloads
├── logs/                       # Execution logs
├── runner.py                   # Layer 1 Execution
├── superposition_runner.py     # Layer 2 Execution
├── test_drift_safety.py        # Layer 3 Verification
├── measure_risk.py             # Risk Measurement
├── system-contract.md          # 📜 FINAL CONTRACT: System Guarantees
├── behavior-matrix.md          # 🧭 TRUTH TABLE: Deterministic Behavior
├── host-safety.md              # 🛡️ Host Protection Policies
├── failure-containment.md      # 🚒 Blast Radius Control
└── requirements.txt            # Dependencies

## 📜 System Semantics & Guarantees
This system operates under a strict **Universal System Contract**.
* **[System Contract](system-contract.md):** Defines the bounded growth, entropy floors, and immutable history guarantees.
* **[Behavior Matrix](behavior-matrix.md):** The deterministic "Truth Table" of how the system reacts to every signal.
* **[Host Safety](host-safety.md):** Proof that the harness cannot escalate privilege or execute arbitrary code.
🛠️ Installation
Clone the repository:

Bash
git clone [https://github.com/your-username/quantum-stress-harness.git](https://github.com/your-username/quantum-stress-harness.git)
cd quantum-stress-harness
Install Dependencies:

Bash
pip install -r requirements.txt
🏃‍♂️ Usage Guide
Mode A: Classical Stress Testing (Task 1)
Best for finding bugs, crashes, and memory leaks.

Configure: Edit config/mutation-config.yaml.

Run: python runner.py

Analyze: python analyze_metrics.py

Mode B: Quantum-Adversarial Testing (Task 2 & 3)
Best for measuring stability, confidence, and risk under uncertainty.

Configure: Edit config/probability-config.yaml (Set seed: 42 for determinism).

Run: python superposition_runner.py

Generates quantum_metrics.json

Measure: python measure_risk.py

Output:

Plaintext
QUANTUM RISK REPORT (N=100)
✅ System Confidence:   95.0%
⚖️  Stability Index:     76.2%
⚠️  FINAL RISK SCORE:    27.5% (CRITICAL RISK)
Mode C: Adaptive Learning Verification (Task 4)
Best for testing the system's ability to learn from failure without going rogue.

Run Safety Check:

Bash
python test_drift_safety.py
Verify Behavior:

The system simulates a massive failure signal (1000 crashes).

Pass Condition: The weight increases but stops exactly at 0.60 (Saturation Limit) instead of going to 1.0.

Explainability: Check the logs printed to console to see the reasoning behind every weight change.

🛡️ Attack Vectors
The harness supports the following mutation types:

regex_bomb: Triggers catastrophic backtracking.

long_string: 50KB+ payloads to test buffers.

nested_json: Recursive depth > 50.

boundary_int: Edge cases like -1, 0, MAX_INT.

📝 License
This project is open-source. Created for the System Stress & Failure Engineering assignment.
