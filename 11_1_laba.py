import os
from PIL import Image, ImageFilter
input_folder = 'mumu'

output_folder = input_folder + '+контур'
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        try:
            img = Image.open(file_path)

            filtered = img.filter(ImageFilter.CONTOUR)
            output_path = os.path.join(output_folder, filename)
            filtered.save(output_path)
            print(f'Обработан файл: {filename}')
        except Exception as e:
            print(f'Ошибка при обработке {filename}: {e}')