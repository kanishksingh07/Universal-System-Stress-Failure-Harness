import statistics

class CollapseEngine:
    """
    FORMALIZED Collapse Engine (Task 3 Compliant).
    Enforces strict mathematical bounds on all risk metrics.
    """
    def __init__(self, results):
        self.results = results
        self.total_shots = len(results)
        
        # Invariant Check 1: Data Validity
        if self.total_shots < 0:
            raise ValueError("CRITICAL: Negative shot count detected.")
            
    def calculate_confidence(self) -> float:
        """Returns the probability (0.0 - 1.0) of system success."""
        if self.total_shots == 0: return 0.0
        
        successes = len([r for r in self.results if r['status'] == 'success'])
        confidence = successes / self.total_shots
        
        # Bound Enforcement
        return max(0.0, min(1.0, confidence))

    def calculate_stability_index(self) -> float:
        """Returns Stability (0.0 - 1.0). High Variance = Low Stability."""
        if self.total_shots < 2: return 1.0
        
        latencies = [max(0.0, r['latency_ms']) for r in self.results] # Enforce non-negative time
        avg_latency = statistics.mean(latencies)
        
        if avg_latency == 0: return 1.0
        
        stdev = statistics.stdev(latencies)
        variation_ratio = stdev / avg_latency
        
        stability = 1.0 - variation_ratio
        
        # Bound Enforcement (Strict [0,1] clamping)
        return max(0.0, min(1.0, stability))

    def get_risk_report(self):
        """Collapses data into a Formal Risk Profile."""
        confidence = self.calculate_confidence()
        stability = self.calculate_stability_index()
        
        # Formal Risk Formula
        risk_score = 1.0 - (confidence * stability)
        
        # Final Bound Check (Safety Net)
        risk_score = max(0.0, min(1.0, risk_score))
        
        verdict = "SAFE"
        if risk_score > 0.25: verdict = "CRITICAL FAILURE"
        elif risk_score > 0.10: verdict = "WARNING"

        return {
            "total_shots": self.total_shots,
            "confidence_score": round(confidence, 4), 
            "stability_index": round(stability, 4),   
            "calculated_risk": round(risk_score, 4),  
            "verdict": verdict
        }
