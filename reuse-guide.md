# ♻️ Reuse & Configuration Guide

## Philosophy
This harness follows the **Zero Code Change** principle. [cite_start]You can switch between testing a web API, a local function, or an AI model entirely through configuration[cite: 59].

## Configuration Reference (`config/mutation-config.yaml`)

To switch targets, modify the `target_system` block:

### Mode 1: HTTP API
Use this for REST endpoints.
```yaml
target_system:
  type: "api"
  url: "http://localhost:8080/api/v1/test"
  method: "POST"
  timeout_seconds: 5