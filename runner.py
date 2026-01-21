import requests
import yaml
import time
import json
import concurrent.futures
import importlib
import sys
from generators.mutators import PayloadGenerator

# Ensure current directory is in path so we can import local_targets.py
sys.path.append(".")

# Load Config
with open("config/mutation-config.yaml", "r") as f:
    config = yaml.safe_load(f)

LOG_FILE = "logs/execution.log"
METRICS_FILE = "metrics.json"
results = []

# --- Dynamic Function Loader (Universal Support) ---
def get_local_function(module_name, func_name):
    module = importlib.import_module(module_name)
    return getattr(module, func_name)

def run_test_case(payload, mutation_type):
    target = config['target_system']
    mode = target.get('type', 'api') # Default to API
    timeout = target['timeout_seconds']
    
    start_time = time.time()
    result = {
        "mutation": mutation_type,
        "timestamp": start_time,
        "mode": mode,
        "status": "unknown",
        "latency_ms": 0,
        "response": None
    }

    try:
        # --- MODE A: HTTP API ---
        if mode == 'api':
            response = requests.post(target['url'], json=payload, timeout=timeout)
            result["status"] = "success" if response.status_code < 500 else "failure"
            result["response"] = str(response.status_code)

        # --- MODE B: Local Function / AI Model ---
        elif mode == 'function':
            # 1. Dynamically load the python code
            func = get_local_function(target['module_path'], target['function_name'])
            
            # 2. Execute with payload
            # (We measure execution time to simulate latency tracking)
            output = func(payload)
            result["status"] = "success"
            result["response"] = str(output)[:100] # Truncate long AI outputs to keep logs clean

    except Exception as e:
        # Catch Python Crashes (TypeError, ValueError, MemoryError, ConnectionError)
        result["status"] = "crash_or_network_error"
        result["error"] = str(e)
        
    # Measure Latency
    result["latency_ms"] = (time.time() - start_time) * 1000
    return result

def main():
    # 1. Generate Specific Mutations (The "Smart" Tests)
    mutations = [
        (PayloadGenerator.generate_long_string(), "long_string"),
        (PayloadGenerator.generate_unicode(), "unicode"),
        (PayloadGenerator.generate_nested_json(), "nested_json"),
        (PayloadGenerator.generate_regex_bomb(), "regex_bomb"),
        (PayloadGenerator.generate_malformed_schema(), "malformed_schema")
    ]
    
    # Add Boundary Values
    for val in PayloadGenerator.generate_boundary_ints():
        mutations.append(({"value": val}, "boundary_int"))

    # 2. Generate Random Entropy (The "Volume" Tests)
    # This logic satisfies the "Thousands of test cases" requirement
    target_count = config['test_settings']['total_requests']
    current_count = len(mutations)
    
    if current_count < target_count:
        print(f"Generating {target_count - current_count} random test cases to reach target...")
        for _ in range(target_count - current_count):
            mutations.append((PayloadGenerator.generate_random_entropy(), "random_entropy"))

    # 3. Execution Phase
    t_type = config['target_system'].get('type', 'api')
    print(f"Starting Universal Stress Test via [{t_type}] mode...")
    print(f"Total Cases: {len(mutations)}")

    concurrency = config['test_settings']['concurrency']
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(run_test_case, m[0], m[1]) for m in mutations]
        
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    # 4. Save Metrics
    with open(METRICS_FILE, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"Test Complete. Metrics saved to {METRICS_FILE}")

if __name__ == "__main__":
    main()