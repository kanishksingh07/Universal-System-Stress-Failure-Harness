# 🛡️ Host Safety & Misuse Resistance

> **Scope:** Universal System Stress Failure Harness
> **Priority:** CRITICAL

This document formally proves that the harness is safe to run on production hosts, developer workstations, and CI environments. It operates under the Principle of Least Privilege and Strict Isolation.

## 1. Execution Safety Guarantees

### 1.1 The "Data, Not Code" Guarantee
The harness generates **Payloads**, not **Programs**.
* **Proof:** `generators/mutators.py` output is strictly typed: `str`, `dict`, `int`, `bytes`.
* **Mechanism:** The harness executes `func(payload)`. It **NEVER** executes `eval(payload)` or `exec(payload)`.
* **Implication:** Even if the harness generates a perfect shellcode string, it is passed as a string argument to the target. It cannot execute unless the *Target itself* interprets it as code (which is what we are testing).

### 1.2 No Privilege Escalation
The harness requires **Zero Special Privileges**.
* **User Mode Only:** Runs entirely in userspace `(uid > 0)`.
* **No Sudo:** The codebase contains 0 instances of `sudo`, `su`, or `runas`.
* **File Access:** Restricted to:
    * Reading: `config/*.yaml`
    * Writing: `logs/`, `metrics.json`
    * **Strictly Forbidden:** Writing to `/bin`, `/etc`, `C:\Windows`.

## 2. Resource Containment

### 2.1 Memory Safety
* **Payload Caps:**
    * Max String Length: 1MB (Configurable in `mutators.py`).
    * Max JSON Depth: 50 levels.
* **Process Cap:**
    * Concurrency is strictly bounded by `max_workers` in `runner.py`.
    * Default: 5 threads. Hard Limit suggestion: CPU Count * 2.

### 2.2 Network Containment
* The harness is **Single-Target Locked**.
* It only initiates connections to the `target_system` URL defined in config.
* No "Network Scanning" or "Service Discovery" logic exists.

## 3. Misuse Resistance

### 3.1 Malicious Configuration
If an attacker modifies `config.yaml` to point `module_path` to `os` and `function_name` to `system`:
* **Behavior:** The harness _will_ execute the function as requested.
* **Defense:** **Configuration is the Trust Boundary.** The harness assumes the configuration file is authoritative. Users must secure writability of `config/`.

### 3.2 Recursive Loops
* **Scenario:** Target System calls the Harness (Loop).
* **Defense:** The Harness does not expose an HTTP listener (No Ingress). It is Egress-only. Infinite loops technically impossible via network.

## 4. Failure Modes

| Failure | Containment |
| :--- | :--- |
| **Harness Crash** | Process terminates. No zombies. |
| **Target Hangs** | `requests.post(..., timeout=timeout)` forcibly cuts connection. |
| **Disk Full** | Logs are appended. If write fails, harness crashes safely (SystemExit). |

## 5. Verification
Run the Misuse Test Suite to verify these claims:
```bash
python misuse-tests/test_no_exec.py
python misuse-tests/test_resource_safety.py
```
