from PIL import Image

image = Image.open("kartinka.jpg")
area = (200, 200, image.width - 200, image.height - 200)
pimage = image.crop(area)
pimage.save('new_kartinka.jpg')