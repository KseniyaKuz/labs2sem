from PIL import Image, ImageDraw, ImageFont

name = input("Введите имя: ").strip()

image = Image.open('4.jpg').convert('RGBA')
area = (100, 150, image.width - 100, image.height - 50)
pimage = image.crop(area)

draw = ImageDraw.Draw(pimage)

try:
    font = ImageFont.truetype("arialbd.ttf", 70)
except:
    font = ImageFont.truetype("arial.ttf", 70)
    print("шрифт не найден")

text = f"{name}, поздравляю!"
text_width = draw.textlength(text, font=font)
x = (pimage.width - text_width) // 2
y = pimage.height - 100

draw.text((x, y), text, font=font, fill="pink", stroke_width=2, stroke_fill="black")

pimage.save('new_4.png', 'PNG')