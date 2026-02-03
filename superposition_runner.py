import yaml
import time
import json
import sys
import importlib
import random
from quantum_layer.superposition import SuperposedInput

# --- Helper: Dynamic Function Loader ---
def get_local_function(module_name, func_name):
    """Dynamically imports a function from a local Python file."""
    sys.path.append(".") # Ensure local path is visible
    module = importlib.import_module(module_name)
    return getattr(module, func_name)

# --- Day 3: Contract Validator ---
def validate_config(config):
    """
    Enforces Strict System Contracts defined in system-contracts.md.
    Prevents invalid runs before they start.
    """
    print("🛡️  Validating System Contracts...")
    
    # Contract 1: Configuration Structure
    if 'superposition_states' not in config:
        raise ValueError("CONTRACT VIOLATION: Missing 'superposition_states' in config.")
    
    if 'quantum_settings' not in config:
        raise ValueError("CONTRACT VIOLATION: Missing 'quantum_settings' in config.")

    # Contract 2: Weight Summation (Must be ~1.0)
    # We use a small epsilon (0.01) to account for floating point math
    total_weight = sum(s.get('weight', 0) for s in config['superposition_states'])
    if not (0.99 <= total_weight <= 1.01):
        raise ValueError(f"CONTRACT VIOLATION: Total weight is {total_weight}. Must sum to 1.0")

    # Contract 3: State Integrity
    for state in config['superposition_states']:
        if 'payload' not in state or 'name' not in state:
            raise ValueError(f"CONTRACT VIOLATION: Invalid state definition: {state}")
            
    print("✅ Contracts Verified. System is stable.")

def main():
    # 1. Load Configuration
    print("⚛️  Initializing Quantum-Adversarial Layer...")
    try:
        with open("config/probability-config.yaml", "r") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("❌ Error: config/probability-config.yaml not found!")
        return

    # 2. Enforce Contracts (Day 3 Requirement)
    try:
        validate_config(config)
    except ValueError as e:
        print(f"\n⛔ FATAL ERROR: {e}")
        sys.exit(1) # Hard Crash on Contract Violation

    # 3. Enforce Determinism (Day 2 Requirement)
    # We set the seed globally for the 'random' library.
    seed = config['quantum_settings'].get('seed', None)
    if seed is not None:
        print(f"🔒 DETERMINISM ENFORCED: SeedingPRNG with [{seed}]")
        random.seed(seed)
    else:
        print("⚠️  WARNING: Running in Non-Deterministic Mode (No Seed)")

    # 4. Build the Superposition Object
    q_input = SuperposedInput()
    print("   ... Loading States into Superposition:")
    
    for state in config['superposition_states']:
        print(f"      - Adding State {state['name']} (Weight: {state['weight']})")
        q_input.add_state(state['payload'], state['weight'], state['name'])

    # 5. Prepare Target
    target = config['target_system']
    func = get_local_function(target['module_path'], target['function_name'])
    total_shots = config['quantum_settings']['shots']
    results = []

    print(f"\n🚀 Running {total_shots} Measurement Shots...\n")

    # 6. The Measurement Loop
    for i in range(total_shots):
        # A. Collapse
        # Because we set random.seed(), this choice is now pre-determined.
        collapsed_state = q_input.collapse()
        
        # B. Execute
        start_time = time.time()
        status = "success"
        output = None
        
        try:
            output = func(collapsed_state['payload'])
        except Exception as e:
            status = "failure"
            output = str(e)
            
        latency = (time.time() - start_time) * 1000

        # C. Record
        results.append({
            "shot_id": i + 1,
            "collapsed_state": collapsed_state['name'],
            "status": status,
            "latency_ms": latency,
            "error_msg": output if status == "failure" else None
        })

    # 7. Save Results
    output_file = "quantum_metrics.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"✅ Run Complete. Measurements saved to {output_file}")

if __name__ == "__main__":
    main()