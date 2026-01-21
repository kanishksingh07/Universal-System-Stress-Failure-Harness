import json
import statistics

def analyze_results():
    with open("metrics.json", "r") as f:
        data = json.load(f)

    total = len(data)
    if total == 0:
        print("No data found.")
        return

    # 1. Filter results
    successes = [d for d in data if d['status'] == 'success']
    failures = [d for d in data if d['status'] == 'failure'] # HTTP 500s
    crashes = [d for d in data if d['status'] == 'crash_or_network_error']
    timeouts = [d for d in data if d['status'] == 'timeout']

    # 2. Calculate Latency Metrics (Day 4 Requirement)
    latencies = [d['latency_ms'] for d in data]
    avg_latency = statistics.mean(latencies) if latencies else 0
    max_latency = max(latencies) if latencies else 0

    # 3. Print the "War Report" Summary
    print("-" * 30)
    print(f"TEST RUN SUMMARY (Total: {total})")
    print("-" * 30)
    print(f"✅ Success (Handled Safely): {len(successes)}")
    print(f"❌ Application Failures (500s): {len(failures)}")
    print(f"⚠️  Timeouts: {len(timeouts)}")
    print(f"🔥 Critical Crashes: {len(crashes)}")
    print("-" * 30)
    print(f"⏱️  Avg Latency: {avg_latency:.2f}ms")
    print(f"⏱️  Max Latency: {max_latency:.2f}ms")
    print("-" * 30)

    # 4. List specific errors for debugging
    if crashes:
        print("\nCRASH DETAILS:")
        for c in crashes:
            print(f" - {c['mutation']}: {c.get('error', 'Unknown Error')}")

if __name__ == "__main__":
    analyze_results()