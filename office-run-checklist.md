# 📋 Office Validation Checklist

To validate this system, follow these exact steps:

## Phase 1: Determinism Check
1. [ ] Open `config/probability-config.yaml`.
2. [ ] Ensure `seed: 42` is set.
3. [ ] Run `python superposition_runner.py`.
4. [ ] Rename `quantum_metrics.json` to `reference.json`.
5. [ ] Run `python superposition_runner.py` again.
6. [ ] **Pass Condition:** The "collapsed_state" order in `quantum_metrics.json` matches `reference.json` exactly.

## Phase 2: Contract Check
1. [ ] Open `config/probability-config.yaml`.
2. [ ] Change the weight of `|Normal_User>` to `0.0` (Total sum becomes 0.2).
3. [ ] Run `python superposition_runner.py`.
4. [ ] **Pass Condition:** System crashes immediately with `FATAL ERROR: CONTRACT VIOLATION`.
5. [ ] **Revert:** Change weight back to `0.8` before proceeding.

## Phase 3: Risk Measurement
1. [ ] Run `python measure_risk.py`.
2. [ ] **Pass Condition:** Output shows a "Formal Risk Score" between 0.0 and 1.0.