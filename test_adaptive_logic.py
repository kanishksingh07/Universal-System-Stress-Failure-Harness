import json
from adaptive_layer.learning_engine import AdaptiveRiskEngine

def main():
    print("🧠 Testing Adaptive Learning Logic...")

    # 1. Mock Initial State (Normal: 0.8, Attack: 0.2)
    initial_states = [
        {"name": "|Normal_User>", "weight": 0.80, "payload": {}},
        {"name": "|Attack_User>", "weight": 0.20, "payload": {}}
    ]

    # 2. Mock Results (The Attack causes a crash)
    mock_results = [
        {"collapsed_state": "|Attack_User>", "status": "failure", "latency_ms": 50},
        {"collapsed_state": "|Normal_User>", "status": "success", "latency_ms": 20}
    ]

    # 3. Run Learning Engine
    engine = AdaptiveRiskEngine(initial_states)
    new_states = engine.learn_from_epoch(mock_results)

    # 4. Verify Learning
    print("\n--- Learning Outcome ---")
    for s in new_states:
        print(f"State: {s['name']} | Old Weight: {0.8 if 'Normal' in s['name'] else 0.2} -> New Weight: {s['weight']}")

    # Check if Attack weight increased
    attack_weight = next(s['weight'] for s in new_states if "Attack" in s['name'])
    if attack_weight > 0.20:
        print("\n✅ SUCCESS: System 'learned' to fear the Attack state.")
    else:
        print("\n❌ FAILURE: Weights did not update correctly.")

if __name__ == "__main__":
    main()