"""
utils.py - Visualization and data helper for the Clinical Trial project.
Generates statistical charts for business analysis.
"""
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_compliance_stats(output_dir="images"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Chart 1: Compliance Scores over Time
    trials = ["Trial A", "Trial B", "Trial C", "Trial D", "Trial E"]
    scores = [0.92, 0.85, 0.78, 0.95, 0.88]
    
    plt.figure(figsize=(10, 6))
    plt.bar(trials, scores, color=['#4CAF50', '#FFC107', '#F44336', '#4CAF50', '#2196F3'])
    plt.axhline(y=0.85, color='gray', linestyle='--', label='Compliance Threshold')
    plt.title("Clinical Trial Compliance Health Scores", fontsize=14)
    plt.ylabel("Score (0-1.0)")
    plt.ylim(0, 1.1)
    plt.legend()
    plt.savefig(os.path.join(output_dir, "compliance-health.png"), dpi=300)
    plt.close()

    # Chart 2: Risk Correlation (Complexity vs Gaps)
    complexity = np.random.uniform(1, 10, 20)
    gaps = complexity * 0.5 + np.random.normal(0, 1, 20)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(complexity, gaps, color='#E91E63', alpha=0.6)
    plt.title("Protocol Complexity vs. Regulatory Gaps", fontsize=14)
    plt.xlabel("Protocol Complexity Index")
    plt.ylabel("Detected Gaps")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig(os.path.join(output_dir, "risk-correlation.png"), dpi=300)
    plt.close()

    # Chart 3: Response Time Distribution
    times = np.random.normal(5, 1.5, 100)
    plt.figure(figsize=(10, 6))
    plt.hist(times, bins=15, color='#00BCD4', edgecolor='white')
    plt.title("Agent Synthesis Latency Distribution", fontsize=14)
    plt.xlabel("Wait Time (seconds)")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(output_dir, "latency-stats.png"), dpi=300)
    plt.close()
    
    print(f"Statistical charts generated in {output_dir}")

if __name__ == "__main__":
    generate_compliance_stats()
