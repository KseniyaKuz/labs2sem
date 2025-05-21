import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('watermark', exist_ok=True)

wm = Image.new('RGBA', (150, 55))
draw = ImageDraw.Draw(wm)
font = ImageFont.truetype('arial.ttf', 80)
draw.text((30, 30), "АИП", fill=(255, 255, 255, 200), font=font)

for i in range(1, 6):
    img = Image.open(f'{i}.jpg').convert('RGBA')
    x = img.width - wm.width - 15
    y = img.height - wm.height - 15
    img.paste(wm, (x, y), wm)
    img.convert('RGB').save(f'watermark/wm{i}.jpg')
