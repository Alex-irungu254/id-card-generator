from PIL import Image, ImageDraw, ImageFont
import os

# Create template image (ID card size: 450x300)
template = Image.new('RGB', (450, 300), color='white')
draw = ImageDraw.Draw(template)

# Add border
draw.rectangle([(5, 5), (445, 295)], outline='black', width=2)

# Add header
draw.rectangle([(10, 10), (440, 50)], fill='#0066cc', outline='black', width=1)
draw.text((200, 25), "ID CARD", fill='white', font=None)

# Add lines for content (placeholder areas)
draw.text((20, 80), "Name:", fill='black')
draw.line([(80, 90), (420, 90)], fill='gray', width=1)

draw.text((20, 130), "DOB:", fill='black')
draw.line([(80, 140), (420, 140)], fill='gray', width=1)

draw.text((20, 180), "ID Number:", fill='black')
draw.line([(120, 190), (420, 190)], fill='gray', width=1)

# Add photo placeholder
draw.rectangle([(20, 210), (150, 285)], fill='#e0e0e0', outline='black', width=1)
draw.text((50, 240), "Photo", fill='gray')

# Save template
template_dir = os.path.join('media', 'templates')
os.makedirs(template_dir, exist_ok=True)
template.save(os.path.join(template_dir, 'template.jpeg'))
print("Template image created successfully at media/templates/template.jpeg")
