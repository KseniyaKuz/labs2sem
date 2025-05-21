from PIL import Image
import matplotlib.pyplot as plt

image_path = "9_1.jpg"

try:
    img = Image.open(image_path)
except FileNotFoundError:
    print("Ошибка: файл не найден!")
    exit()

plt.imshow(img)
plt.axis('off')
plt.title("Ваше изображение")
plt.show()


width, height = img.size
image_format = img.format
color_mode = img.mode


print("\nИнформация о изображении:")
print(f"- Размер: {width}x{height} пикселей")
print(f"- Формат: {image_format}")
print(f"- Цветовая модель: {color_mode}")
