import urllib.request
from PIL import Image
import io

def generate_ascii(image, width=92):
    # Resize
    aspect_ratio = image.height / image.width
    # Terminal characters are typically 2:1 height:width, so adjust aspect ratio
    new_height = int(width * aspect_ratio * 0.5)
    img = image.resize((width, new_height))
    
    # Convert to grayscale
    img = img.convert('L')
    
    # ASCII chars from dark to light
    chars = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]
    
    pixels = img.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += chars[pixel * len(chars) // 256]
        
    return [ascii_str[i:i+width] for i in range(0, len(ascii_str), width)]

# Fetch avatar
url = "https://github.com/daivik-debuger.png"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    img_data = response.read()

image = Image.open(io.BytesIO(img_data))
ascii_lines = generate_ascii(image, width=92)

# Ensure we only have around 49 lines (the original has 49 lines, from y=79.98 to y=442.27, step is ~7.5)
# Actually let's just find all <tspan x="30" in the file and replace them one by one.
import re

for filename in ['dark.svg', 'light.svg']:
    with open(filename, 'r') as f:
        content = f.read()
        
    # Find all tspans with x="30"
    pattern = r'<tspan x="30"[^>]*>.*?</tspan>'
    matches = re.finditer(pattern, content)
    
    new_content = content
    for i, match in enumerate(matches):
        if i < len(ascii_lines):
            # preserve the starting part, just replace the inner text
            original = match.group(0)
            prefix = original[:original.find('>')+1]
            suffix = '</tspan>'
            new_tspan = prefix + ascii_lines[i] + suffix
            new_content = new_content.replace(original, new_tspan, 1)
        else:
            # If there are more tspans than ascii lines, replace with spaces
            original = match.group(0)
            prefix = original[:original.find('>')+1]
            suffix = '</tspan>'
            new_tspan = prefix + (" " * 92) + suffix
            new_content = new_content.replace(original, new_tspan, 1)
            
    with open(filename, 'w') as f:
        f.write(new_content)

print("Replaced ASCII art successfully!")
