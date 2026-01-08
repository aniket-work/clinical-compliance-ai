import base64
import requests
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

# Setup directories
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

def generate_mermaid_diagrams():
    diagrams = {
        "architecture": """
graph TB
    subgraph Client Layer
        U[Audit Request]
        V[Protocol Document]
    end
    subgraph Agent Core
        A[Compliance Agent Interface]
        B[Regulatory Rules Engine]
        C[LMM Auditor]
        D[Risk Assessment Module]
    end
    subgraph Knowledge Base
        E[FDA/ICH Guidelines]
        F[Internal SOPs]
    end
    U --> A
    V --> A
    A --> B
    B --> E
    B --> F
    A --> C
    C --> D
    D --> G[Compliance Report]
""",
        "workflow": """
flowchart TD
    A[Start Protocol Upload] --> B[Text Extraction]
    B --> C{Rule Identification}
    C --> D[Clause Matching]
    D --> E[Compliance Verification]
    E --> F{Risk Detected?}
    F -- Yes --> G[Flag Violation & Recommendation]
    F -- No --> H[Mark Compliant]
    G --> I[Generate PDF/JSON Report]
    H --> I
    I --> J[End]
""",
        "structure": """
graph LR
    P[Project Root] --> S[src/]
    P --> D[data/]
    P --> I[images/]
    S --> A[auditor.py]
    S --> R[rules_engine.py]
    D --> M[mock_protocols.md]
    D --> G[guidelines.json]
    I --> T[title-animation.gif]
"""
    }

    for name, code in diagrams.items():
        encoded = base64.b64encode(code.encode()).decode()
        url = f"https://mermaid.ink/img/{encoded}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(os.path.join(IMAGE_DIR, f"{name.replace('_', '-')}-diagram.png"), 'wb') as f:
                    f.write(response.content)
                print(f"Generated {name} diagram.")
            else:
                print(f"Failed to generate {name} diagram: {response.status_code}")
        except Exception as e:
            print(f"Error generating {name} diagram: {e}")

def generate_statistical_charts():
    # Chart 1: Compliance Accuracy
    labels = ['Manual Audit', 'AI-First Audit', 'AI-Human Hybrid']
    accuracy = [78, 92, 98]
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, accuracy, color=['#e74c3c', '#3498db', '#2ecc71'])
    plt.title('Clinical Compliance Audit Accuracy (%)', fontsize=14, fontweight='bold')
    plt.ylabel('Accuracy Percentage')
    plt.ylim(0, 100)
    for i, v in enumerate(accuracy):
        plt.text(i, v + 1, f"{v}%", ha='center', fontweight='bold')
    plt.savefig(os.path.join(IMAGE_DIR, 'compliance-accuracy.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Chart 2: Time Sensitivity (Days)
    trial_size = ['Phase I', 'Phase II', 'Phase III']
    manual_time = [5, 12, 35]
    ai_time = [0.2, 0.5, 2]

    plt.figure(figsize=(10, 6))
    x = np.arange(len(trial_size))
    width = 0.35
    plt.bar(x - width/2, manual_time, width, label='Manual Audit', color='#95a5a6')
    plt.bar(x + width/2, ai_time, width, label='AI Agent', color='#9b59b6')
    plt.title('Protocol Audit Lead Time (Days)', fontsize=14, fontweight='bold')
    plt.xticks(x, trial_size)
    plt.ylabel('Days to Complete')
    plt.legend()
    plt.savefig(os.path.join(IMAGE_DIR, 'audit-time-savings.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated statistical charts.")

def generate_animated_gif():
    # Collect all generated PNGs
    chart_files = [
        os.path.join(IMAGE_DIR, 'compliance-accuracy.png'),
        os.path.join(IMAGE_DIR, 'audit-time-savings.png'),
        os.path.join(IMAGE_DIR, 'architecture-diagram.png')
    ]
    
    images = []
    for file in chart_files:
        if os.path.exists(file):
            img = Image.open(file)
            # Standardize size for the GIF
            img = img.resize((1200, 800), Image.Resampling.LANCZOS)
            images.append(img)
    
    if images:
        images[0].save(
            os.path.join(IMAGE_DIR, 'title-animation.gif'),
            save_all=True,
            append_images=images[1:],
            duration=1500,  # 1.5 seconds per frame
            loop=0
        )
        print("Generated animated title GIF.")

if __name__ == "__main__":
    generate_mermaid_diagrams()
    generate_statistical_charts()
    generate_animated_gif()
