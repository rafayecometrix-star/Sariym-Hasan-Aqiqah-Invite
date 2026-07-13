import re
import os

html_path = "aqiqah-invitation-sariym-hasan trial 1.html"
images_dir = "images"

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Find all base64 image strings
base64_pattern = re.compile(r'data:image\/(jpeg|png|gif|webp);base64,([A-Za-z0-9+/=\s]+)')
matches = list(base64_pattern.finditer(html))

image_names = ['hero-bg', 'gallery-1', 'gallery-2']
replacements = []

for i, match in enumerate(matches):
    ext = 'jpg' if match.group(1) == 'jpeg' else match.group(1)
    base64_data = re.sub(r'\s+', '', match.group(2))
    
    name = imageNames = image_names[i] if i < len(image_names) else f'image-{i}'
    filename = f"{name}.{ext}"
    filepath = os.path.join(images_dir, filename)
    
    # Write image file
    import base64
    try:
        with open(filepath, "wb") as img_file:
            img_file.write(base64.b64decode(base64_data))
        print(f"Saved: {filename}")
        replacements.append((match.group(0), f"images/{filename}"))
    except Exception as e:
        print(f"Error decoding image {i}: {e}")

# Apply replacements
for original, replacement in replacements:
    html = html.replace(original, replacement)

# Write updated HTML back
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
