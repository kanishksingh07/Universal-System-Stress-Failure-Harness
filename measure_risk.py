import json
from quantum_layer.collapse_engine import CollapseEngine

def main():
    print("⚛️  Collapsing Wave Function into Risk Metrics...\n")
    
    # 1. Load the raw probability data
    try:
        with open("quantum_metrics.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ Error: Run superposition_runner.py first!")
        return

    # 2. Initialize Engine
    engine = CollapseEngine(data)
    
    # 3. Collapse & Report
    report = engine.get_risk_report()
    
    print("-" * 40)
    print(f"QUANTUM RISK REPORT (N={report['total_shots']})")
    print("-" * 40)
    print(f"✅ System Confidence:   {report['confidence_score']}%")
    print(f"⚖️  Stability Index:     {report['stability_index']}%")
    print("-" * 40)
    print(f"⚠️  FINAL RISK SCORE:    {report['calculated_risk']}%")
    print(f"📝 Verdict:             {report['verdict']}")
    print("-" * 40)

if __name__ == "__main__":
    main()