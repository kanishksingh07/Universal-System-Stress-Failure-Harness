import json
from adaptive_layer.learning_engine import AdaptiveRiskEngine

def main():
    print("⚓ Testing Stability & Drift Safety...")

    # 1. Setup State
    initial_states = [
        {"name": "|Normal_User>", "weight": 0.50, "payload": {}},
        {"name": "|Weak_Point>", "weight": 0.50, "payload": {}}
    ]

    # 2. Simulate CATASTROPHIC FAILURE (1000 crashes)
    # Theoretically, this should push weight to 100%, but our Brakes should stop it.
    mock_results = [{"collapsed_state": "|Weak_Point>", "status": "failure", "latency_ms": 50}] * 1000

    # 3. Run Engine
    engine = AdaptiveRiskEngine(initial_states)
    new_states = engine.learn_from_epoch(mock_results)

    # 4. Check Results
    weak_point = next(s for s in new_states if "Weak_Point" in s['name'])
    print(f"\nResult Weight: {weak_point['weight']}")
    
    # 5. The Audit
    print("\n--- Explainability Log ---")
    print(engine.get_explanation())

    # Verification Logic
    if weak_point['weight'] <= 0.60:
        print("\n✅ SUCCESS: Safety Brakes engaged. Weight capped at 0.60 despite massive failure signal.")
    else:
        print(f"\n❌ FAILURE: Runaway learning detected! Weight {weak_point['weight']} exceeded limit.")

if __name__ == "__main__":
    main()