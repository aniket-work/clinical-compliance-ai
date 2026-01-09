from PIL import Image, ImageDraw, ImageFont
import os
import time

def generate_realistic_terminal_frames(output_dir="images/terminal-frames"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Clean previous frames
    for f in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, f))

    # Configuration
    width, height = 800, 450
    bg_color = (30, 30, 30)
    text_color = (200, 200, 200)
    cursor_color = (200, 200, 200)
    title_bar_color = (45, 45, 45)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", 18)
    except:
        font = ImageFont.load_default()

    # The script of what happens in the terminal
    # Tuples of (text_to_add, delay_after_line, is_typing_effect)
    sequence = [
        ("$ python main.py", 0.5, True), # Typing command
        ("\n=== Starting Autonomous Clinical Compliance Audit ===", 0.3, False),
        ("\n[ReguBot]: Initializing knowledge base...", 0.2, False),
        ("\n[ReguBot]: Searching FDA/EMA databases...", 0.4, False),
        ("\n[ReguBot]: Found 4 relevant regulatory frameworks.", 0.2, False),
        ("\n[ProtoScan]: Loading protocol documents...", 0.2, False),
        ("\n[ProtoScan]: Analyzing Section 4.1 against 21 CFR 50...", 0.3, False),
        ("\n[ProtoScan]: Analyzing Section 5.3 against GCP-R2...", 0.3, False),
        ("\n[ProtoScan]: Audit complete. 4 Findings logged.", 0.2, False),
        ("\n[Syntho]: Aggregating risk factors...", 0.2, False),
        ("\n[Syntho]: Synthesizing executive summary...", 0.4, False),
        ("\n\n=== Audit Results Summary ===", 0.1, False),
        ("\n{", 0.1, False),
        ('\n    "overall_health_score": 0.82,', 0.1, False),
        ('\n    "status": "NEEDS REVIEW",', 0.1, False),
        ('\n    "critical_violations": 1', 0.1, False),
        ("\n}", 0.1, False),
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
        
        # Cursor
        if show_cursor:
            # Simple cursor approximation: get size of text
            # This is tricky with multiline. For simplicity in this PoC, 
            # we'll just put the cursor at end of last line or approximate.
            # Using getbbox is better but complex. 
            # We will use a blinking underscore at the end of the text string visually
            pass # Cursor drawing logic can be complex for multiline wrapped text with Pillow
                 # Instead, we append a block char to text if cursor is needed
        
        frame_path = os.path.join(output_dir, f"frame_{frame_count:03d}.png")
        img.save(frame_path)
        frame_count += 1

    # Generate frames
    for content, delay, is_typing in sequence:
        if is_typing:
            # Type out character by character
            chars = content if not content.startswith("\n") else content[1:] # Handle newline prefix logic manually
            prefix = current_text + ("\n" if content.startswith("\n") else "")
            
            for char in chars:
                current_text = prefix + char
                prefix = current_text
                # Save frame with cursor
                save_frame(current_text + "█", show_cursor=True)
                # Skip some frames for speed if needed, but 1 frame per char is okay for 10-15fps
        else:
            # Line appears at once
            current_text += content
            save_frame(current_text, show_cursor=False)
            
            # "Wait" frames (copies of current state)
            # Assuming 10 fps, 0.1s delay = 1 frame
            frames_to_hold = int(delay * 10)
            for _ in range(frames_to_hold):
                save_frame(current_text + (" █" if frame_count % 6 < 3 else ""), show_cursor=True) # Blinking cursor effect

    print(f"Generated {frame_count} frames in {output_dir}")

if __name__ == "__main__":
    generate_realistic_terminal_frames()
