# 📉 Failure Taxonomy

## Overview
This document defines the classification of system failures used by the Universal Stress Harness. [cite_start]Our core philosophy is that **silent failures are unacceptable**[cite: 6].

## 1. Classification of Failures

### 🔴 Critical Failures (Forbidden)
These indicate a breakdown in the system's reliability or availability.
* **Hard Crash:** The process terminates unexpectedly (e.g., Python `SystemExit`, Segmentation Fault).
* **HTTP 500/502/503:** The server failed to handle the request gracefully.
* **Uncaught Exception:** Internal stack traces leaked to the user (e.g., `ValueError` bubbling up).
* **Silent Failure:** The system returns `200 OK` but performs the wrong action or drops data.

### 🟠 Performance Failures (Degradation)
* **Timeout:** Response time exceeds the configured threshold (Default: 5s).
* **Latency Spike:** Average response time deviates >300% from baseline.
* **Resource Exhaustion:** System runs out of Memory (OOM) or CPU during stress.

### 🟢 Expected Rejections (Valid)
These are "good" failures where the system correctly identifies hostile input.
* **HTTP 400 Bad Request:** Correct rejection of malformed JSON.
* **HTTP 413 Payload Too Large:** Correct rejection of "Long String" attacks.
* **Validation Error:** Returns a structured error message explaining why input was rejected.