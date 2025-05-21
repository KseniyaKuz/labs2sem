import os
from PIL import Image

folder = 'mumu'
allowed_exts = ('.jpg', '.jpeg', '.png')
for filename in os.listdir(folder):
    if filename.lower().endswith(allowed_exts):
        file_path = os.path.join(folder, filename)
        try:
            image = Image.open(file_path)
            print(f"Файл: {filename}")
            print("  Формат изображения:", image.format)
            print("  Размер изображения:", image.size)
            print("  Цветовая модель:", image.mode)
        except Exception as e:
            print(f"Ошибка при обработке {filename}: {e}")
    else:
        print(f"Пропущен файл (не изображение): {filename}")