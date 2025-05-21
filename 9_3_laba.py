import os
from PIL import Image, ImageFilter

out = 'fILT'
os.makedirs(out, exist_ok=True)

for i in range(1, 6):
    img = Image.open(f'{i}.jpg')
    filtered = img.filter(ImageFilter.CONTOUR)
    filtered.save(os.path.join(out, f'f{i}.jpg'))
