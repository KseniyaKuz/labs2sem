from PIL import Image, ImageOps

image = Image.open("2.jpg")

small = image.resize((image.width // 3, image.height // 3))
small.save('2small.jpg')
hor = ImageOps.mirror(image)
hor.save('2horizont.jpg')
ver = ImageOps.flip(image)
ver.save('2verti.jpg')