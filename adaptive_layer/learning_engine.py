import copy

class AdaptiveRiskEngine:
    """
    Day 2 Upgrade: Adds Stability Constraints, Cooldowns, and Explainability.
    """
    def __init__(self, current_states):
        self.states = copy.deepcopy(current_states)
        
        # --- Safety Configuration ---
        self.MAX_DELTA = 0.10          # Max change per step
        self.MIN_WEIGHT = 0.05         # Entropy Floor
        self.MAX_WEIGHT = 0.60         # Saturation Ceiling
        
        self.COOLDOWN_EPOCHS = 3       # Constraint B: Epoch Cooldown
        self.current_epoch = 0
        self.last_update_epoch = -3    # init so first run (0) works
        
        # Learning Rates
        self.LR_FAILURE = 0.05
        self.LR_LATENCY = 0.02
        self.LR_DECAY = 0.01
        
        # Explainability Log
        self.explanation_log = []

    def _normalize_weights(self):
        total = sum(s['weight'] for s in self.states)
        for s in self.states:
            s['weight'] = round(s['weight'] / total, 4)

    def learn_from_epoch(self, results):
        self.explanation_log = [] # Clear logs for this run
        self.current_epoch += 1
        
        # --- Safety Check: Ambiguity (Refusal to Learn) ---
        total_failures = sum(1 for r in results if r['status'] == 'failure')
        failure_rate = total_failures / len(results) if results else 0
        
        if failure_rate > 0.90:
            self.explanation_log.append(f"⛔ REFUSAL: Ambiguous Signal (Failure Rate: {failure_rate:.2%}). Learning Frozen.")
            return self.states

        # --- Safety Check: Cooldown ---
        epochs_since_update = self.current_epoch - self.last_update_epoch
        if epochs_since_update < self.COOLDOWN_EPOCHS:
             self.explanation_log.append(f"⏳ SKIP: Cooldown Active ({epochs_since_update}/{self.COOLDOWN_EPOCHS} epochs).")
             return self.states

        # Only if checks pass, we proceed to update
        self.last_update_epoch = self.current_epoch
        signals = {s['name']: 0.0 for s in self.states}
        
        # 1. Calculate Raw Signals
        for shot in results:
            name = shot['collapsed_state']
            if shot['status'] == "failure":
                signals[name] += self.LR_FAILURE
            elif shot['latency_ms'] > 100:
                signals[name] += self.LR_LATENCY
            else:
                signals[name] -= (self.LR_DECAY / len(results))

        # 2. Apply Updates with KINETIC BRAKES
        for s in self.states:
            name = s['name']
            raw_delta = signals.get(name, 0)
            old_weight = s['weight']
            
            # Brake 1: Clamp Velocity (Max Delta)
            actual_delta = max(-self.MAX_DELTA, min(self.MAX_DELTA, raw_delta))
            
            # Brake 2: Saturation Limits
            proposed_weight = old_weight + actual_delta
            final_weight = max(self.MIN_WEIGHT, min(self.MAX_WEIGHT, proposed_weight))
            
            # Update State
            s['weight'] = final_weight
            
            # Log Explainability
            if abs(final_weight - old_weight) > 0.001:
                reason = "Failure Detected" if raw_delta > 0 else "Success Decay"
                self.explanation_log.append(
                    f"State '{name}': {old_weight:.2f} -> {final_weight:.2f} | Reason: {reason} (Delta: {actual_delta:.4f})"
                )

        # 3. Re-Normalize
        self._normalize_weights()
        
        return self.states

    def get_explanation(self):
        """Returns the 'Why' behind the changes."""
        return "\n".join(self.explanation_log)