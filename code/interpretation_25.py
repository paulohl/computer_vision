from PIL import Image, ImageDraw, ImageFont
import cairosvg
import io
import os

# Define SVGs for outline and filled variants
outline_svg = """
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">
  <circle cx="100" cy="100" r="95" fill="none" stroke="#00b8d9" stroke-width="8"/>
  <text x="50%" y="55%" text-anchor="middle" font-family="serif" font-size="64" fill="#e6c84f" dominant-baseline="middle">
    XYZ
  </text>
</svg>
"""

filled_svg = """
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">
  <circle cx="100" cy="100" r="95" fill="#00b8d9"/>
  <text x="50%" y="55%" text-anchor="middle" font-family="serif" font-size="64" fill="#e6c84f" dominant-baseline="middle">
    XYZ
  </text>
</svg>
"""

# Convert SVG to PNG bytes using cairosvg
outline_png_bytes = cairosvg.svg2png(bytestring=outline_svg.encode('utf-8'))
filled_png_bytes = cairosvg.svg2png(bytestring=filled_svg.encode('utf-8'))

# Function to resize and save multiple favicon sizes
sizes = [16, 32, 64, 128, 256]
output_files = []

def save_resized_png(base_png_bytes, prefix):
    base_img = Image.open(io.BytesIO(base_png_bytes)).convert("RGBA")
    for size in sizes:
        resized_img = base_img.resize((size, size), Image.LANCZOS)
        filename = f"/mnt/data/{prefix}_{size}x{size}.png"
        resized_img.save(filename, format="PNG")
        output_files.append(filename)

# Save favicon sets for outline and filled variants
save_resized_png(outline_png_bytes, "favicon_outline")
save_resized_png(filled_png_bytes, "favicon_filled")

output_files
