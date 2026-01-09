"""
generate_assets.py - Asset generation for the Clinical Trial project.
Handles Mermaid diagram conversion and GIF creation.
"""
import base64
import requests
import os
from PIL import Image

def generate_mermaid_diagrams():
    diagrams = {
        "title-diagram": """
graph TD
    subgraph Regulatory Intelligence
        R1[FDA 21 CFR]
        R2[EMA GCP]
        R3[GDPR Health]
    end
    subgraph Multi-Agent Engine
        A1[Regulatory Researcher]
        A2[Protocol Analyzer]
        A3[Compliance Synthesizer]
    end
    Trial[Protocol Document] --> A2
    R1 & R2 & R3 --> A1
    A1 -->|Knowledge| A2
    A2 -->|Findings| A3
    A3 --> Report[Compliance Audit Report]
    
    style A1 fill:#e1f5fe,stroke:#01579b
    style A2 fill:#e1f5fe,stroke:#01579b
    style A3 fill:#e1f5fe,stroke:#01579b
    style Report fill:#c8e6c9,stroke:#2e7d32
""",
        "architecture-flow": """
sequenceDiagram
    participant P as Protocol
    participant R as Researcher
    participant A as Analyzer
    participant S as Synthesizer
    
    P->>A: Submit Document
    R->>A: Regulatory Context
    A->>A: Pattern Match
    A->>S: Raw Findings
    S->>S: Risk Scoring
    S->>P: Final Audit
"""
    }

    os.makedirs("images", exist_ok=True)
    for name, code in diagrams.items():
        print(f"Generating {name}...")
        encoded = base64.b64encode(code.encode()).decode()
        url = f"https://mermaid.ink/img/{encoded}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"images/{name}.png", 'wb') as f:
                    f.write(response.content)
                print(f"Saved images/{name}.png")
            else:
                print(f"Error generating {name}: {response.status_code}")
        except Exception as e:
            print(f"Exception for {name}: {e}")

def create_animated_title():
    print("Creating comprehensive animated title GIF...")
    frames = []
    
    # 1. Add Terminal frames (Realistic Typing)
    terminal_dir = "images/terminal-frames"
    if os.path.exists(terminal_dir):
        frame_files = sorted([f for f in os.listdir(terminal_dir) if f.endswith(".png")])
        for f in frame_files:
            img = Image.open(os.path.join(terminal_dir, f))
            frames.append(img.convert("RGB"))

    # 2. Add Statistical Chart frames
    charts = ["compliance-health.png", "risk-correlation.png", "latency-stats.png"]
    for chart in charts:
        path = os.path.join("images", chart)
        if os.path.exists(path):
            img = Image.open(path).resize((800, 450)) # Ensure consistent size (Height changed to 450 to match terminal)
            # Add chart frame multiple times to stay on screen longer
            for _ in range(20): # 20 frames * 100ms = 2 seconds per chart
                frames.append(img.convert("RGB"))
    
    if frames:
        print(f"Total frames gathered: {len(frames)}")
        # Verify first frame is terminal
        print(f"First frame mode: {frames[0].mode}, Size: {frames[0].size}")
        
        frames[0].save(
            "images/title-animation-v2.gif",
            save_all=True,
            append_images=frames[1:],
            duration=100, # 100ms
            loop=0
        )
        print("Saved images/title-animation-v2.gif")
    else:
        print("No frames found for GIF creation.")

if __name__ == "__main__":
    generate_mermaid_diagrams()
    # Note: create_animated_title() should be called AFTER running main.py to ensure charts exist
    create_animated_title()
