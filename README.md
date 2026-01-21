# 🛡️ Universal System Stress & Failure Harness

A **config-driven, reusable system stress and failure testing harness** designed to intentionally break systems and surface crashes, latency spikes, forbidden failures, and nondeterministic behavior.

This project focuses on **robustness testing**, not just correctness — answering the question:

> *How does a system behave when users don’t behave nicely?*

---

## 📖 Overview

The Universal System Stress & Failure Harness is built to test **input-driven systems** such as:

- HTTP APIs
- Internal Python functions / rule engines
- AI & ML inference logic (extensible)

Unlike traditional load-testing tools that focus only on traffic volume, this harness generates **hostile and adversarial inputs** and measures how systems fail under stress.

The harness follows a **zero code change philosophy** — systems are tested by changing configuration only.

---

## 🚀 Key Features

- 🔧 **Hybrid Target Support**
  - HTTP APIs
  - Local Python functions
  - Extensible for AI models

- 🧬 **Input Mutation Engine**
  - Empty inputs
  - Extremely long payloads
  - Unicode & malformed data
  - Random entropy & boundary values

- 🧠 **Failure Taxonomy Driven**
  - Expected vs forbidden failures
  - Crash and exception detection
  - Silent failure identification

- 📊 **Observability & Metrics**
  - Latency measurement
  - Failure frequency
  - Run-level traceability (`run_id`)
  - Machine-readable JSON reports

- ♻️ **Fully Config-Driven**
  - No hardcoded targets
  - No code changes per system
  - Reusable across environments

---

## 📂 Project Structure

```text
stress_harness/
├── adapters/            # API, Function, AI adapters
├── core/                # Runner, metrics, failure detection
├── generators/          # Input mutation engine
├── config/              # YAML-based configuration
├── reports/             # Machine-readable output (metrics.json)
├── failure-taxonomy.md  # Defined failure classes & severity
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
````

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kanishksingh07/Universal-System-Stress-Failure-Harness.git
cd Universal-System-Stress-Failure-Harness
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

**Dependencies**

* `requests`
* `pyyaml`

---

## ⚙️ Configuration

All behavior is controlled via `config/harness.yaml`.

### 🔹 Test an HTTP API

```yaml
target:
  type: api
  url: http://localhost:8000/test
  timeout_ms: 2000

execution:
  total_tests: 50

mutations:
  - empty
  - long
  - unicode
  - random
```

### 🔹 Test a Local Python Function

```yaml
target:
  type: function
  module: sample_target
  function: test_function
  timeout_ms: 2000

mutations:
  - empty
  - long
  - unicode
  - random
```

Switching target types requires **no code changes**.

---

## 🏃 Usage

Run the harness from the project root:

```bash
python -m core.runner
```

This will:

1. Generate hostile inputs
2. Execute them against the target
3. Measure latency & failures
4. Write results to `reports/metrics.json`

---

## 📊 Output Example

```json
{
  "run_id": "2026-01-22T10:41:12Z",
  "mutation": "unicode",
  "status": "error",
  "failure_type": "FORBIDDEN_FAILURE",
  "latency": 0.134
}
```

All outputs are **machine-readable** and suitable for dashboards or further analysis.

---

## 🧪 Failure Taxonomy

Failure classes and severity levels are defined in:

```
failure-taxonomy.md
```

The taxonomy distinguishes:

* ✅ Expected failures (safe rejection)
* ❌ Forbidden failures (crashes, hangs, silent corruption)

---

## 🎯 Intended Use Cases

* API robustness testing
* Rule engine validation
* AI inference edge-case testing
* Demo & prototype hardening
* Internal tool stress testing

---

## 📝 License

This project is open-source and intended for educational, testing, and system hardening purposes.

Use it to break systems — and then fix them.

````

---

## ✅ `requirements.txt` (commit this too)

```text
requests
pyyaml
````

---


