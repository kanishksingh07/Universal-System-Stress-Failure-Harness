Markdown

# ⚛️ Quantum-Adversarial Stress Harness

**A config-driven, probabilistic stress testing system designed to break APIs, Internal Functions, and AI Models under uncertainty.**

## 📖 Overview
This repository contains a dual-layer stress harness:
1.  **Layer 1 (Universal Harness):** A high-volume, deterministic stress tester for finding hard crashes and bugs.
2.  **Layer 2 (Quantum-Adversarial):** A probabilistic engine that models "Superposition" (multiple potential input states) and "Collapse" (measurement) to calculate a system's **Risk Profile** and **Stability Index**.

It follows a **Zero Code Change** philosophy: switch between testing an API, a local function, or an AI model purely by changing the configuration.

---

## 🚀 Key Features

### 🛡️ Layer 1: Universal Stress (Deterministic)
* **Universal Targets:** Test HTTP APIs or Local Python Functions via dynamic loading.
* **Hostile Mutations:** Automatically generates SQL injection, Deep JSON nesting, Regex Bombs, and Unicode overflows.
* **High Volume:** Generates thousands of test cases using random entropy.
* **Concurrency:** Parallel execution for high-throughput stress.

### ⚛️ Layer 2: Quantum-Adversarial (Probabilistic)
* **Superposition Modeling:** Define a "User State" as a weighted probability cloud (e.g., 80% Normal, 15% Malicious, 5% Edge Case).
* **Collapse Engine:** "Measures" the system 100+ times to collapse uncertainty into a single reality.
* **Risk Metrics:** Calculates **Confidence Score** and **Stability Index** (latency variance) instead of binary Pass/Fail.

---

## 📂 Project Structure

```text
stress-harness/
├── config/
│   ├── mutation-config.yaml    # Layer 1 Config (Deterministic)
│   └── probability-config.yaml # Layer 2 Config (Quantum/Probabilistic)
├── generators/                 # Mutation logic (bit flips, regex bombs)
├── quantum_layer/              # NEW: Superposition & Collapse logic
│   ├── superposition.py
│   └── collapse_engine.py
├── logs/                       # Execution logs
├── runner.py                   # Layer 1 Execution Engine
├── superposition_runner.py     # Layer 2 Execution Engine
├── analyze_metrics.py          # Layer 1 Analytics
├── measure_risk.py             # Layer 2 Risk Measurement
├── local_targets.py            # Dummy targets (Rule Engine & AI Model)
├── final-risk-report.md        # Task 1 Report
├── quantum-war-report.md       # Task 2 Report
└── requirements.txt            # Dependencies
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

Run:

Bash

python runner.py
Analyze:

Bash

python analyze_metrics.py
Mode B: Quantum-Adversarial Testing (Task 2)
Best for measuring stability, confidence, and risk under uncertainty.

Configure: Edit config/probability-config.yaml to define states and weights.

Run (Superposition Engine):

Bash

python superposition_runner.py
Generates quantum_metrics.json

Measure (Collapse Engine):

Bash

python measure_risk.py
Output:

Plaintext

QUANTUM RISK REPORT (N=100)
✅ System Confidence:   95.0%
⚖️  Stability Index:     76.2%
⚠️  FINAL RISK SCORE:    27.5% (CRITICAL RISK)
🛡️ Attack Vectors
The harness supports the following mutation types:

regex_bomb: Triggers catastrophic backtracking in regex engines.

long_string: 50KB+ payloads to test buffer handling.

nested_json: Recursive depth > 50 to stack-overflow parsers.

boundary_int: Edge cases like -1, 0, MAX_INT.

malformed_schema: Structurally valid JSON that violates business logic.

📝 License
This project is open-source. Created for the System Stress & Failure Engineering assignment.
