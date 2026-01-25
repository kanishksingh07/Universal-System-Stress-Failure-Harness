import yaml
import time
import json
import sys
import importlib
from quantum_layer.superposition import SuperposedInput

# --- Helper: Dynamic Function Loader (Reused from Task 1) ---
def get_local_function(module_name, func_name):
    sys.path.append(".") # Ensure local path is visible
    module = importlib.import_module(module_name)
    return getattr(module, func_name)

def main():
    # 1. Load Configuration
    print("⚛️  Initializing Quantum-Adversarial Layer...")
    with open("config/probability-config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # 2. Build the Superposition Object
    q_input = SuperposedInput()
    print("   ... Loading States into Superposition:")
    
    for state in config['superposition_states']:
        print(f"      - Adding State {state['name']} (Weight: {state['weight']})")
        q_input.add_state(state['payload'], state['weight'], state['name'])

    # 3. Prepare Target
    target = config['target_system']
    func = get_local_function(target['module_path'], target['function_name'])
    total_shots = config['quantum_settings']['shots']
    results = []

    print(f"\n🚀 Running {total_shots} Measurement Shots...\n")

    # 4. The Measurement Loop (Running the probabilistic batch)
    for i in range(total_shots):
        # A. Collapse the Superposition
        collapsed_state = q_input.collapse()
        
        # B. Execute the Reality
        start_time = time.time()
        status = "success"
        output = None
        
        try:
            output = func(collapsed_state['payload'])
        except Exception as e:
            status = "failure"
            output = str(e)
            
        latency = (time.time() - start_time) * 1000

        # C. Record the Observation
        results.append({
            "shot_id": i + 1,
            "collapsed_state": collapsed_state['name'], # Crucial: What state did it collapse to?
            "status": status,
            "latency_ms": latency,
            "error_msg": output if status == "failure" else None
        })

    # 5. Save Results
    output_file = "quantum_metrics.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"✅ Run Complete. Measurements saved to {output_file}")

if __name__ == "__main__":
    main()