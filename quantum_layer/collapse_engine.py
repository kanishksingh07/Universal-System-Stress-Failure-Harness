import statistics

class CollapseEngine:
    """
    Analyzes the 'wave function' of test results to calculate 
    risk metrics and system stability.
    """
    def __init__(self, results):
        self.results = results
        self.total_shots = len(results)

    def calculate_confidence(self):
        """Returns the probability (0.0 - 1.0) that the system succeeds."""
        if self.total_shots == 0: return 0.0
        successes = len([r for r in self.results if r['status'] == 'success'])
        return successes / self.total_shots

    def calculate_stability_index(self):
        """
        Returns a score (0.0 - 1.0) based on latency consistency.
        High Standard Deviation = Low Stability.
        """
        if self.total_shots < 2: return 1.0
        
        latencies = [r['latency_ms'] for r in self.results]
        avg_latency = statistics.mean(latencies)
        stdev = statistics.stdev(latencies)
        
        # Stability Formula: 1.0 - (Variation / Average)
        # If variation is huge, stability drops.
        if avg_latency == 0: return 1.0
        variation_ratio = stdev / avg_latency
        stability = max(0.0, 1.0 - variation_ratio)
        return stability

    def get_risk_report(self):
        """Collapses all data into a final Risk Profile."""
        confidence = self.calculate_confidence()
        stability = self.calculate_stability_index()
        
        # Risk is the inverse of Confidence * Stability
        risk_score = 1.0 - (confidence * stability)
        
        return {
            "total_shots": self.total_shots,
            "confidence_score": round(confidence * 100, 2), # %
            "stability_index": round(stability * 100, 2),   # %
            "calculated_risk": round(risk_score * 100, 2),  # %
            "verdict": "SAFE" if risk_score < 0.2 else "CRITICAL RISK"
        }