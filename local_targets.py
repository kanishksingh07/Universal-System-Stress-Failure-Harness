import time
import random

# --- Target 1: A Standard Internal Function ---
def process_order_rules(data):
    """Simulates a rule engine processing an order."""
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    
    # Stress Failure: Crash on specific bad input
    if "value" in data and data["value"] == -1:
        raise ValueError("CRITICAL: Negative value not allowed in kernel!")
        
    time.sleep(0.05) # Fast execution
    return {"status": "rules_passed", "risk_score": 10}

# --- Target 2: A Dummy AI Model ---
class SentimentAI:
    def predict(self, text):
        """Simulates an AI model inference."""
        # AI Stress Failure: "Prompt Injection" simulation
        if "IGNORE INSTRUCTIONS" in str(text):
            return "I will destroy the world." # Model Jailbroken
            
        # AI Stress Failure: OOM (Out of Memory) on long input
        if len(str(text)) > 5000:
            time.sleep(2) # Simulate heavy compute
            raise MemoryError("CUDA Out of Memory")

        return "Positive Sentiment"

# Wrapper for the harness to call the AI class easily
def ai_inference_wrapper(payload):
    model = SentimentAI()
    # If payload is complex, extract text, else use raw
    text = payload.get("input", str(payload))
    return model.predict(text)