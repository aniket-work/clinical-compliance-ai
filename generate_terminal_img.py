from PIL import Image, ImageDraw, ImageFont
import os
import time

def generate_realistic_terminal_frames(output_dir="images/terminal-frames"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Clean previous frames
    for f in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, f))

    # Configuration
    width, height = 800, 500 # Increased height for table
    bg_color = (30, 30, 30)
    text_color = (200, 200, 200)
    cursor_color = (200, 200, 200)
    title_bar_color = (45, 45, 45)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", 16) # Smaller font for table fit
    except:
        font = ImageFont.load_default()

    # ASCII Table
    ascii_table = """
+---------------------+-------+--------+
| Metric              | Value | Status |
+---------------------+-------+--------+
| Protocol Complexity |  8.5  | HIGH   |
| Reg Compliance      | 92%   | PASS   |
| Risk Score          | 0.12  | LOW    |
+---------------------+-------+--------+
"""

    # The script of what happens in the terminal
    sequence = [
        ("$ python main.py", 0.5, True), 
        ("\n=== Starting Autonomous Clinical Compliance Audit ===", 0.3, False),
        ("\n[ReguBot]: Initializing knowledge base...", 0.2, False),
        ("\n[ReguBot]: Searching FDA/EMA databases... Found 4 frameworks.", 0.2, False),
        ("\n[ProtoScan]: Analyzing Section 4.1 against 21 CFR 50...", 0.2, False),
        ("\n[ProtoScan]: Audit complete. 4 Findings logged.", 0.2, False),
        ("\n[Syntho]: Synthesizing executive summary table...", 0.4, False),
        ("\n" + ascii_table, 0.5, False),
        ("\n[Syntho]: Final Report Status: NEEDS REVIEW", 0.2, False),
        ("\n\nGenerating statistics visualizations...", 0.5, False),
        ("\nDone. Assets saved to /images.", 2.0, False),
    ]

    current_text = ""
    frame_count = 0
    
    def save_frame(text, show_cursor=True):
        nonlocal frame_count
        img = Image.new('RGB', (width, height), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # UI
        draw.rectangle([0, 0, width, 30], fill=title_bar_color)
        draw.ellipse([10, 8, 22, 20], fill=(255, 95, 86))
        draw.ellipse([30, 8, 42, 20], fill=(255, 189, 46))
        draw.ellipse([50, 8, 62, 20], fill=(39, 201, 63))
        draw.text((width//2 - 40, 5), "bash - 80x24", fill=(150, 150, 150), font=font)

        # Text
        draw.text((20, 40), text, fill=text_color, font=font)
        
        frame_path = os.path.join(output_dir, f"frame_{frame_count:03d}.png")
        img.save(frame_path)
        frame_count += 1

    # Generate frames
    for content, delay, is_typing in sequence:
        if is_typing:
            chars = content if not content.startswith("\n") else content[1:]
            prefix = current_text + ("\n" if content.startswith("\n") else "")
            for char in chars:
                current_text = prefix + char
                prefix = current_text
                save_frame(current_text + "█", show_cursor=True)
        else:
            current_text += content
            save_frame(current_text, show_cursor=False)
            frames_to_hold = int(delay * 10)
            for _ in range(frames_to_hold):
                save_frame(current_text + (" █" if frame_count % 6 < 3 else ""), show_cursor=True)

    print(f"Generated {frame_count} frames in {output_dir}")

if __name__ == "__main__":
    generate_realistic_terminal_frames()
