import os
from datetime import date, timedelta
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont


def _safe_font(name, size):
    try:
        return ImageFont.truetype(name, size)
    except Exception:
        return ImageFont.load_default()


def _draw_hatch(draw, width, height):
    for y in range(0, height, 112):
        draw.line([(0, y), (width, y + 120)], fill='#f1e9e0', width=1)
        draw.line([(0, y + 6), (width, y + 126)], fill='#f9f4ef', width=1)


def generate_id_card(data):
    width, height = 1000, 620
    base = Image.new('RGB', (width, height), '#f7f1eb')
    draw = ImageDraw.Draw(base)

    _draw_hatch(draw, width, height)

    # Light background patterns
    # for i in range(0, width, 240):
    #     draw.ellipse([(i - 140, 40), (i + 280, 340)], outline='#f4e4d6', width=2)

    # Header bars
    draw.rectangle([(0, 0), (width, 120)], fill='#004d6d')
    draw.rectangle([(0, 120), (width, 180)], fill='#f7efe5')

    # White panel behind personal info for text contrast
    draw.rectangle([(320, 200), (720, 560)], fill='#ffffff')
    draw.rectangle([(320, 200), (720, 560)], outline='#d1d5db', width=1)

    logo_font = _safe_font('ariali.ttf', 90)
    title_font = _safe_font('arialbd.ttf', 44)
    label_font = _safe_font('arial.ttf', 18)
    value_font = _safe_font('arialbd.ttf', 34)
    small_font = _safe_font('arial.ttf', 15)
    signature_font = _safe_font('ariali.ttf', 28)
    state_font = _safe_font('arialbd.ttf', 58)

    # State name and license title
    draw.text((50, 30), 'Florida', fill='white', font=logo_font)
    draw.text((50, 95), 'DRIVER LICENSE', fill='black', font=title_font)
    draw.text((720, 35), 'USA', fill='white', font=_safe_font('arialbd.ttf', 24))
    draw.text((720, 70), 'DHSMV', fill='white', font=label_font)

    # License number and class badge
    draw.text((650, 125), f'ID#: {data.id_number}', fill='#ffcc00', font=value_font)
    draw.rectangle([(820, 130), (930, 170)], outline='white', width=3)
    draw.text((835, 135), 'CLASS', fill='white', font=_safe_font('arial.ttf', 16))
    draw.text((840, 155), 'D', fill='white', font=_safe_font('arialbd.ttf', 24))

    # Photo panel
    photo_box = (50, 220, 330, 520)
    draw.rectangle(photo_box, fill="#4a1ba0", outline='#1b5f7a', width=5)
    draw.rectangle([(photo_box[0] + 8, photo_box[1] + 8), (photo_box[2] - 8, photo_box[3] - 8)], outline='#95b9d9', width=2)

    photo = Image.open(data.photo.path).convert('RGB')
    photo = photo.resize((photo_box[2] - photo_box[0] - 16, photo_box[3] - photo_box[1] - 16), Image.BILINEAR)
    base.paste(photo, (photo_box[0] + 8, photo_box[1] + 8))
    draw.text((photo_box[0] + 12, photo_box[3] + 14), 'PHOTO', fill='#1b5f7a', font=label_font)

    # Hologram circle and FL mark
    seal_center = (910, 275)
    draw.ellipse([(seal_center[0] - 55, seal_center[1] - 55), (seal_center[0] + 55, seal_center[1] + 55)], outline='#f9d9b7', width=4)
    draw.text((seal_center[0] - 18, seal_center[1] - 12), 'FL', fill='#1b5f7a', font=_safe_font('arialbd.ttf', 28))
    draw.text((seal_center[0] - 30, seal_center[1] + 20), 'USA', fill='#1b5f7a', font=_safe_font('arial.ttf', 14))

    # Personal info fields
    left = 380
    top = 220
    spacing = 55

    def field(row, label, value):
        y = top + row * spacing
        draw.text((left, y), label, fill="#4c68aa", font=label_font)
        draw.text((left, y + 26), value, fill="#121416", font=value_font)

    field(0, 'NAME', data.name.upper())
    field(1, 'DOB', data.dob.strftime('%m/%d/%Y'))
    field(2, 'DL NO.', data.id_number)
    field(3, 'CLASS', 'D')
    field(4, 'ENDORSE', 'NONE')
    field(5, 'RESTR', 'B')

    issue_date = date.today()
    try:
        expiry_date = issue_date.replace(year=issue_date.year + 6)
    except ValueError:
        expiry_date = issue_date + timedelta(days=6 * 365)

    draw.text((left, top + 6 * spacing), 'ISSUE', fill='#0f172a', font=label_font)
    draw.text((left, top + 6 * spacing + 26), issue_date.strftime('%m/%d/%Y'), fill='#07101b', font=value_font)
    draw.text((left + 260, top + 6 * spacing), 'EXP', fill='#0f172a', font=label_font)
    draw.text((left + 260, top + 6 * spacing + 26), expiry_date.strftime('%m/%d/%Y'), fill='#07101b', font=value_font)

    # Subtext and sample lines
    draw.text((50, 540), 'SAMPLE - NOT A REAL LICENSE', fill='#8b1f1f', font=small_font)
    draw.text((50, 560), 'DO NOT ALTER OR FORGE LICENSE', fill='#3a3f4d', font=small_font)

    # Signature line
    sig_y = 520
    draw.line([(380, sig_y), (680, sig_y)], fill='#0f3d52', width=2)
    draw.text((382, sig_y + 6), data.name.split()[0] if data.name else 'SIGNATURE', fill='#0f3d52', font=signature_font)

    # Barcode-like block
    barcode_top = 480
    bar_left = 700
    for x in range(bar_left, width - 30, 24):
        thickness = 4 if (x // 24) % 5 != 0 else 10
        draw.line([(x, barcode_top), (x, barcode_top + 80)], fill='#2b3f52', width=thickness)

    draw.text((bar_left, barcode_top + 88), 'F L O R I D A', fill='#3a4b5a', font=small_font)

    output_dir = os.path.join(settings.MEDIA_ROOT, 'generated')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f'{data.id_number}.jpg')
    base.save(output_path, 'JPEG', quality=90)

    data.generated_card = f'generated/{data.id_number}.jpg'
    data.save()