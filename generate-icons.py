#!/usr/bin/env python3
"""
Generate Cymatics PWA icons with Chladni pattern visualization.
Requires: pip install Pillow
"""

from PIL import Image, ImageDraw
import math
import os

def create_chladni_pattern(size, freq_mode=3):
    """
    Generate a Chladni pattern image.
    freq_mode: controls pattern complexity (2-5)
    """
    img = Image.new('RGB', (size, size), color='#0d1117')
    draw = ImageDraw.Draw(img, 'RGBA')

    # Draw circle (plate)
    margin = size // 10
    circle_bbox = [margin, margin, size - margin, size - margin]
    draw.ellipse(circle_bbox, outline='#30363d', width=3)

    # Sample points and draw Chladni pattern
    step = max(1, size // 200)
    center_x, center_y = size // 2, size // 2
    radius = (size - 2 * margin) // 2

    for y in range(margin, size - margin, step):
        for x in range(margin, size - margin, step):
            dx, dy = x - center_x, y - center_y
            r = math.sqrt(dx**2 + dy**2)

            if r <= radius:
                # Normalize coordinates
                nx = dx / radius
                ny = dy / radius

                # Calculate Chladni amplitude
                n = freq_mode
                m = freq_mode - 1
                angle = math.atan2(ny, nx)
                amp = math.sin(n * math.pi * r / radius) * math.cos(m * angle)

                # Map amplitude to color intensity
                intensity = int((abs(amp) + 1) * 60)  # 0-120 range
                if amp > 0.2:  # Draw particles at high amplitude zones
                    color = f'rgba(212, 175, 139, {intensity})'
                    draw.point((x, y), fill='#d4af8b')

    return img

def create_solid_icon(size):
    """Create a simple solid icon with Cymatics branding."""
    img = Image.new('RGB', (size, size), color='#0d1117')
    draw = ImageDraw.Draw(img)

    # Draw concentric circles (plate)
    center = size // 2
    for i in range(3, 0, -1):
        r = (center * i) // 4
        draw.ellipse(
            [center - r, center - r, center + r, center + r],
            outline='#c4a882',
            width=max(1, size // 64)
        )

    # Draw some particles
    particle_size = max(2, size // 32)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        px = center + math.cos(rad) * (center // 2)
        py = center + math.sin(rad) * (center // 2)
        draw.ellipse(
            [px - particle_size, py - particle_size, px + particle_size, py + particle_size],
            fill='#d4af8b'
        )

    return img

def create_maskable_icon(size):
    """Create a maskable icon (for adaptive icons on Android)."""
    img = Image.new('RGB', (size, size), color='#0d1117')
    draw = ImageDraw.Draw(img)

    center = size // 2
    radius = int(size * 0.35)

    # Draw main circle with pattern
    draw.ellipse(
        [center - radius, center - radius, center + radius, center + radius],
        fill='#c4a882',
        outline='#0d1117'
    )

    # Draw inner detail
    inner_radius = radius // 2
    draw.ellipse(
        [center - inner_radius, center - inner_radius, center + inner_radius, center + inner_radius],
        fill='#0d1117'
    )

    # Draw particles around circle
    num_particles = 6
    particle_radius = radius + 20
    particle_size = max(2, size // 32)
    for i in range(num_particles):
        angle = (i / num_particles) * 2 * math.pi
        px = center + math.cos(angle) * particle_radius
        py = center + math.sin(angle) * particle_radius
        draw.ellipse(
            [px - particle_size, py - particle_size, px + particle_size, py + particle_size],
            fill='#c4a882'
        )

    return img

def create_screenshot(width=540, height=720):
    """Create a PWA screenshot for the manifest."""
    img = Image.new('RGB', (width, height), color='#0d1117')
    draw = ImageDraw.Draw(img)

    # Simulate app header
    draw.rectangle([0, 0, width, 60], fill='#161b22')
    draw.text((width // 2 - 50, 20), 'Cymatics', fill='#c4a882')

    # Simulate canvas area with Chladni pattern
    canvas_height = height - 200
    center_x, center_y = width // 2, 200 + canvas_height // 2
    radius = min(width, canvas_height) // 2 - 20

    # Draw plate boundary
    draw.ellipse(
        [center_x - radius, center_y - radius, center_x + radius, center_y + radius],
        outline='#30363d',
        width=2
    )

    # Draw some particles
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        px = center_x + math.cos(rad) * (radius * 0.5)
        py = center_y + math.sin(rad) * (radius * 0.5)
        draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill='#d4af8b')

    # Simulate controls at bottom
    draw.rectangle([0, height - 140, width, height], fill='#161b22')
    draw.text((20, height - 120), 'Frequency: 440 Hz', fill='#c9d1d9')
    draw.text((20, height - 80), 'Vibrate  Reset  Presets', fill='#c4a882')

    return img

def main():
    """Generate all icons."""
    os.makedirs('icons', exist_ok=True)

    # Standard icons
    icon_sizes = [192, 512]
    for size in icon_sizes:
        icon = create_solid_icon(size)
        icon.save(f'icons/icon-{size}.png', 'PNG')
        print(f'Generated icons/icon-{size}.png')

    # Maskable icons (for Android adaptive icons)
    for size in icon_sizes:
        icon = create_maskable_icon(size)
        icon.save(f'icons/icon-{size}-maskable.png', 'PNG')
        print(f'Generated icons/icon-{size}-maskable.png')

    # Screenshot
    screenshot = create_screenshot()
    screenshot.save('icons/screenshot-1.png', 'PNG')
    print('Generated icons/screenshot-1.png')

    print('All icons generated successfully!')

if __name__ == '__main__':
    main()
