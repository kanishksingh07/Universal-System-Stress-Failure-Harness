import json
from adaptive_layer.learning_engine import AdaptiveRiskEngine

def main():
    print("🛡️ Testing Extended Safety Checks...")

    # --- Setup ---
    initial_states = [
        {"name": "|State_A>", "weight": 0.50},
        {"name": "|State_B>", "weight": 0.50}
    ]
    engine = AdaptiveRiskEngine(initial_states)
    
    # --- TEST 1: Ambiguity / Refusal to Learn ---
    print("\n[TEST 1] Ambiguity Check (Global Outage)")
    # 100% Failure Rate
    ambiguous_results = [{"collapsed_state": "|State_A>", "status": "failure", "latency_ms": 50}] * 10
    
    engine.learn_from_epoch(ambiguous_results)
    explanation = engine.get_explanation()
    print(f"Log: {explanation}")
    
    if "⛔ REFUSAL" in explanation and "Ambiguous" in explanation:
        print("✅ PASS: System refused to learn from ambiguous signal.")
    else:
        print("❌ FAIL: System attempted to learn from noise.")

    # --- TEST 2: Cooldown Logic ---
    print("\n[TEST 2] Cooldown Cycles")
    
    # Epoch 1 (Valid Update - after init)
    # Note: init last_update=-3, current=0. 
    # Call 1 -> current=1. Diff = 1 - (-3) = 4 >= 3. OK.
    valid_results = [{"collapsed_state": "|State_A>", "status": "failure", "latency_ms": 50}, 
                     {"collapsed_state": "|State_B>", "status": "success", "latency_ms": 20}] # 50% fail rate, OK
    
    print("Epoch 1 (Expected: Update):")
    engine.learn_from_epoch(valid_results)
    print(engine.get_explanation())

    # Epoch 2 (Rapid Fire - Should Skip)
    # Call 2 -> current=2. Last update=1. Diff = 1 < 3. SKIP.
    print("Epoch 2 (Expected: Skip):")
    engine.learn_from_epoch(valid_results)
    print(engine.get_explanation())
    
    if "⏳ SKIP" in engine.get_explanation():
         print("✅ PASS: Cooldown enforced.")
    else:
         print("❌ FAIL: Cooldown ignored.")

    # Epoch 3 (Still Skip)
    # Call 3 -> current=3. Last update=1. Diff = 2 < 3. SKIP.
    engine.learn_from_epoch(valid_results)
    
    # Epoch 4 (Ready again)
    # Call 4 -> current=4. Last update=1. Diff = 3 >= 3. OK.
    print("Epoch 4 (Expected: Update):")
    engine.learn_from_epoch(valid_results)
    if "State" in engine.get_explanation(): # Standard update log contains "State..."
        print("✅ PASS: System recovered after cooldown.")
    else:
        print("❌ FAIL: System failed to resume learning.")

if __name__ == "__main__":
    main()
