# 🚒 Failure Containment & Blast Radius Control

> **Goal:** Ensure the harness survives catastrophic target failures and never decompresses hazards into the host environment.

## 1. The Blast Radius
The harness defines a rigid boundary between "The Experiment" and "The Laboratory".
* **Inside the Blast Radius:** Targeted API, Local Function, Testing Thread.
* **Outside the Blast Radius:** Harness Core, File System, OS Resources.

## 2. Containment Strategies

### 2.1 Exception Traps (The Air Gap)
The harness wraps **ALL** target interactions in broad exception handlers.
* **Mechanism:** `try...except Exception` blocks in `runner.py` and `superposition_runner.py`.
* **Behavior:** If a target function throws `MemoryError`, `RecursionError`, or `segfault` (if python catches it), the harness:
    1.  Catches the signal.
    2.  Marks the test case as `status: failure`.
    3.  Records the stack trace in JSON.
    4.  **CONTINUES** to the next test case.
* **Guarantee:** A single bad input cannot crash the entire test campaign.

### 2.2 Timeouts (The Deadman Switch)
Every target interaction is strictly time-boxed.
* **Network Mode:** `requests` checks `timeout=config.timeout_seconds`.
* **Function Mode:** (Future) `signal.alarm` or threaded timeouts (currently reliant on function return, but process limits apply).

### 2.3 Contract Enforcement (The Circuit Breaker)
Before a run begins, `validate_config()` performs a pre-flight check.
* **Triggers:** Sum of probabilities $\ne$ 1.0, Missing keys, Invalid structure.
* **Response:** Immediate `SystemExit(1)`. The flight is grounded before takeoff.

## 3. Post-Failure Cleanup
* **Statelessness:** The harness writes no temp files during execution.
* **Log Integrity:** Logs are appended/overwritten atomically where possible.
* **Artifacts:** Metrics are dumped only after the run completes (or could be streamed). *Current implementation dumps at end.*

## 4. Self-Preservation
If the Harness detects it is destabilizing the host (e.g., Memory Usage > Limit), it effectively has no internal monitoring *yet*, but relies on OS limits and `max_workers` constraints to stay within bounds.

## 5. Manual Emergency Stop
To kill a runaway harness:
* **Linux/Mac:** `Ctrl+C` (KeyboardInterrupt is handled gracefully).
* **Kill Command:** `pkill -f runner.py` (Safe, as no state is persisted other than logs).
