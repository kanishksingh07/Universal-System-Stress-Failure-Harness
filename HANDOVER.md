# 📂 Universal Stress Harness - Handover

## Overview
This repository contains a config-driven stress testing harness designed to validate API reliability, latency, and failure modes.

## 🚀 How to Run

### 1. Prerequisites
* Python 3.11+
* Install dependencies:
    ```bash
    pip install requests pyyaml flask
    ```

### 2. Configuration
Edit `config/mutation-config.yaml` to change targets.
* **Current Target:** `http://localhost:8080/api/v1/test`
* **Timeout:** 5 seconds

### 3. Execution Steps
**Step 1: Start the Target** (If testing locally)
```bash
python dummy_server.py