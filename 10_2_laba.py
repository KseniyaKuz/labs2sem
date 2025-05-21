from PIL import Image


postcards = {
    "день рождения": "dr.jpg",
    "новый год": "ng.jpg",
    "1 мая": "may.jpg"
}


holiday = input("К какому празднику вам нужна открытка? ").lower()


if holiday in postcards:
    image = Image.open(postcards[holiday])
else:
    print("Открытка к этому празднику не найдена.")