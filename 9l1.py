from PIL import Image
image = Image.open("1.jpg")
image.show()
print("Формат изображения:", image.format)
print("Размер изображения:", image.size)
print("Цветовая модель:", image.mode)
