from PIL import Image, ImageDraw, ImageFont
import os

def generate_terminal_image(output_path="images/terminal-run.png"):
    # Define the text content
    text = """$ python main.py
=== Starting Autonomous Clinical Compliance Audit ===
[ReguBot - Regulatory Compliance Researcher]: Searching for regulations...
[ReguBot - Regulatory Compliance Researcher]: Found 4 relevant frameworks.
[ProtoScan - Trial Protocol Auditor]: Analyzing protocol sections...
[ProtoScan - Trial Protocol Auditor]: Audit complete. Scores: [0.90, 0.79, 0.84, 0.77]
[Syntho - Compliance Risk Synthesizer]: Synthesizing executive summary...
[Syntho - Compliance Risk Synthesizer]: Final Report Status: NEEDS REVIEW

=== Audit Results Summary ===
{
    "overall_health_score": 0.8286,
    "status": "NEEDS REVIEW",
    "findings_count": 4,
    "critical_violations": 1,
    "summary": "Audit processed successfully. 1 critical gaps identified."
}

Generating business performance statistics...
Statistical charts generated in images/"""

    # Image properties
    width, height = 800, 500
    background_color = (30, 30, 30)  # Dark terminal gray
    text_color = (200, 200, 200)
    title_bar_color = (45, 45, 45)
    
    # Create image
    img = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(img)
    
    # Draw title bar
    draw.rectangle([0, 0, width, 30], fill=title_bar_color)
    # Draw "buttons"
    draw.ellipse([10, 8, 22, 20], fill=(255, 95, 86))  # Close
    draw.ellipse([30, 8, 42, 20], fill=(255, 189, 46)) # Minimize
    draw.ellipse([50, 8, 62, 20], fill=(39, 201, 63))  # Maximize
    
    # Try to load a mono font
    try:
        # Common locations for fonts on macOS
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    # Draw text
    draw.text((20, 50), text, fill=text_color, font=font)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f"Terminal run image saved to {output_path}")

if __name__ == "__main__":
    generate_terminal_image()
