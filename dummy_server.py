from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

@app.route('/api/v1/test', methods=['POST'])
def test_endpoint():
    # Simulate Latency (Day 4 Requirement)
    delay = random.uniform(0.1, 2.0) # Wait between 0.1s and 2s
    time.sleep(delay)

    # Simulate Random Crashes (Day 1 Strategy)
    if random.random() < 0.2: # 20% chance of total crash
        return "Internal Server Error", 500

    # Simulate logic handling
    data = request.json
    if not data:
        return "Bad Request: No Data", 400
    
    # Day 5 Defense: Check for "Long String" attack
    if len(str(data)) > 10000:
        return "Payload Too Large", 413

    return jsonify({"status": "received", "processing_time": delay}), 200

if __name__ == '__main__':
    print("⚠️  DUMMY TARGET LIVE ON PORT 8080 ⚠️")
    app.run(port=8080)