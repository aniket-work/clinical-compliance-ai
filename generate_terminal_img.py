from PIL import Image, ImageDraw, ImageFont
import os

def generate_terminal_frames(output_dir="images/terminal-frames"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the progressive text content
    steps = [
        "$ python main.py",
        "$ python main.py\n=== Starting Autonomous Clinical Compliance Audit ===",
        "$ python main.py\n=== Starting Autonomous Clinical Compliance Audit ===\n[ReguBot]: Searching for regulations...",
        "$ python main.py\n=== Starting Autonomous Clinical Compliance Audit ===\n[ReguBot]: Found 4 relevant frameworks.\n[ProtoScan]: Analyzing protocol sections...",
        "$ python main.py\n=== Starting Autonomous Clinical Compliance Audit ===\n[ReguBot]: Found 4 relevant frameworks.\n[ProtoScan]: Audit complete. Scores: [0.90, 0.79, 0.84, 0.77]",
        "$ python main.py\n=== Starting Autonomous Clinical Compliance Audit ===\n[ReguBot]: Found 4 relevant frameworks.\n[ProtoScan]: Audit complete. Scores: [0.90, 0.79, 0.84, 0.77]\n[Syntho]: Synthesizing executive summary...",
        "$ python main.py\n=== Starting Autonomous Clinical Compliance Audit ===\n[ReguBot]: Found 4 relevant frameworks.\n[ProtoScan]: Audit complete.\n[Syntho]: Final Report Status: NEEDS REVIEW",
        "$ python main.py\n=== Starting Autonomous Clinical Compliance Audit ===\n[ReguBot]: Found 4 relevant frameworks.\n[ProtoScan]: Audit complete.\n[Syntho]: Final Report Status: NEEDS REVIEW\n\nGenerating statistics..."
    ]

    # Image properties
    width, height = 800, 400
    background_color = (30, 30, 30)
    text_color = (200, 200, 200)
    title_bar_color = (45, 45, 45)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", 16)
    except:
        font = ImageFont.load_default()

    for i, text in enumerate(steps):
        img = Image.new('RGB', (width, height), color=background_color)
        draw = ImageDraw.Draw(img)
        
        # Title bar
        draw.rectangle([0, 0, width, 30], fill=title_bar_color)
        draw.ellipse([10, 8, 22, 20], fill=(255, 95, 86))
        draw.ellipse([30, 8, 42, 20], fill=(255, 189, 46))
        draw.ellipse([50, 8, 62, 20], fill=(39, 201, 63))
        
        # Draw text
        draw.text((20, 50), text, fill=text_color, font=font)
        
        frame_path = os.path.join(output_dir, f"frame_{i:02d}.png")
        img.save(frame_path)
    
    print(f"Terminal frames generated in {output_dir}")

if __name__ == "__main__":
    generate_terminal_frames()
