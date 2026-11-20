#!/usr/bin/env python3
"""GTA6 clipper thumbnail"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 720
img = Image.new('RGB', (W, H), '#0a0a14')
draw = ImageDraw.Draw(img)

# Background gradient
for y in range(H):
    r = int(15 + (y/H) * 40)
    g = int(5 + (y/H) * 15)
    b = int(25 + (y/H) * 50)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Video frames collage
frames = [
    (50, 80, 370, 280),   # top left
    (440, 80, 370, 280),  # top right
    (50, 380, 370, 280),  # bottom left
    (440, 380, 370, 280), # bottom right
]
colors = ['#ff2e6e', '#ff6b35', '#9b59b6', '#00ccff']
for i, (fx, fy, fw, fh) in enumerate(frames):
    # Frame with neon border
    draw.rectangle([fx, fy, fx+fw, fy+fh], fill='#111122', outline=colors[i], width=3)
    # Film sprocket holes
    for sy in range(fy + 15, fy + fh, 30):
        draw.rectangle([fx - 6, sy, fx - 4, sy + 12], fill='#333')
        draw.rectangle([fx + fw + 4, sy, fx + fw + 6, sy + 12], fill='#333')
    # Scene number
    draw.text((fx + 15, fy + 15), f"SCENE {i+1}", fill=colors[i], font=None)

# Center overlay
draw.rectangle([W//2 - 200, H//2 - 100, W//2 + 200, H//2 + 100], fill='#000000cc', outline='#ff2e6e', width=2)

try:
    font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
except:
    font_big = ImageFont.load_default()
    font_sm = ImageFont.load_default()

draw.text((W//2 - 180, H//2 - 75), "GTA VI", fill='#ff2e6e', font=font_big)
draw.text((W//2 - 180, H//2 - 15), "CLIPPER", fill='white', font=font_big)
draw.text((W//2 - 180, H//2 + 40), "yt-dlp + ffmpeg", fill='#00ccff', font=font_sm)
draw.text((W//2 - 180, H//2 + 68), "Auto-clip · Vertical · Overlay", fill='#888', font=font_sm)

# Bottom text
draw.text((50, H-50), "make.fun/gta6-clipper-01", fill='#444', font=font_sm)

# Decorative scan lines
for y in range(0, H, 4):
    draw.line([(0, y), (W, y)], fill='#00000022')

os.makedirs("/output", exist_ok=True)
img.save("/output/gta6-clipper-thumb.png", "PNG")
print("gta6-clipper-thumb.png generated")