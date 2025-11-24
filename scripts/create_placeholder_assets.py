#!/usr/bin/env python3
"""Create placeholder PNG assets for Microsoft Store submission.

These are minimal valid PNGs that allow the workflow to build.
Replace with professional assets before final submission.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_icon(size, filename, text):
    """Create a simple placeholder icon."""
    # Create image with gradient background
    img = Image.new('RGBA', size, (70, 130, 180, 255))  # Steel blue
    draw = ImageDraw.Draw(img)

    # Draw a simple camera icon representation
    # Draw rectangle for camera body
    margin = size[0] // 6
    draw.rectangle(
        [margin, margin, size[0]-margin, size[1]-margin],
        fill=(255, 255, 255, 255),
        outline=(50, 50, 50, 255),
        width=max(1, size[0] // 44)
    )

    # Draw circle for lens
    center = (size[0] // 2, size[1] // 2)
    radius = size[0] // 4
    draw.ellipse(
        [center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius],
        fill=(70, 130, 180, 255),
        outline=(50, 50, 50, 255),
        width=max(1, size[0] // 44)
    )

    # Draw small circle in lens
    small_radius = radius // 3
    draw.ellipse(
        [center[0]-small_radius, center[1]-small_radius,
         center[0]+small_radius, center[1]+small_radius],
        fill=(255, 255, 255, 200)
    )

    # Save
    img.save(filename, 'PNG')
    print(f"Created: {filename} ({size[0]}x{size[1]})")

def create_splash_screen(filename):
    """Create splash screen."""
    size = (620, 300)
    img = Image.new('RGBA', size, (70, 130, 180, 255))
    draw = ImageDraw.Draw(img)

    # Draw camera icon in center
    center = (size[0] // 2, size[1] // 2)

    # Camera body
    cam_width = 120
    cam_height = 90
    draw.rectangle(
        [center[0]-cam_width//2, center[1]-cam_height//2,
         center[0]+cam_width//2, center[1]+cam_height//2],
        fill=(255, 255, 255, 255),
        outline=(50, 50, 50, 255),
        width=3
    )

    # Lens
    radius = 35
    draw.ellipse(
        [center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius],
        fill=(70, 130, 180, 255),
        outline=(50, 50, 50, 255),
        width=3
    )

    # Small reflection
    small_radius = 12
    draw.ellipse(
        [center[0]-small_radius, center[1]-small_radius,
         center[0]+small_radius, center[1]+small_radius],
        fill=(255, 255, 255, 200)
    )

    # Try to add text (will use default font if custom not available)
    try:
        # Try to use a nicer font if available
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
    except:
        # Fall back to default font
        font = ImageFont.load_default()

    # Draw text
    text = "Camera Reactions"
    # Get text size (different method for PIL versions)
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except:
        text_width, text_height = draw.textsize(text, font=font)

    text_position = (center[0] - text_width // 2, center[1] + cam_height//2 + 30)
    draw.text(text_position, text, fill=(255, 255, 255, 255), font=font)

    img.save(filename, 'PNG')
    print(f"Created: {filename} ({size[0]}x{size[1]})")

def main():
    """Create all placeholder assets."""
    base_dir = "assets/store"
    os.makedirs(base_dir, exist_ok=True)

    print("Creating placeholder Microsoft Store assets...")
    print("(Replace with professional designs before final submission)\n")

    # Create all required assets
    create_placeholder_icon((44, 44), f"{base_dir}/Square44x44Logo.png", "44")
    create_placeholder_icon((150, 150), f"{base_dir}/Square150x150Logo.png", "150")
    create_placeholder_icon((310, 150), f"{base_dir}/Wide310x150Logo.png", "310")
    create_placeholder_icon((50, 50), f"{base_dir}/StoreLogo.png", "50")
    create_splash_screen(f"{base_dir}/SplashScreen.png")

    print("\n✓ All placeholder assets created successfully!")
    print(f"✓ Location: {base_dir}/")
    print("\nThese are simple placeholders for testing.")
    print("For production, create professional assets using:")
    print("  - Figma (https://figma.com)")
    print("  - Canva (https://canva.com)")
    print("  - Or hire on Fiverr ($5-20)")

if __name__ == "__main__":
    main()
