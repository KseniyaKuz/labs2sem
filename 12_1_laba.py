import json

with open('12.json', encoding='utf-8') as file:
    data = json. load(file)

for product in data["products"]:
    name = product['name']
    price = product['price']
    weight = product ['weight']
    available = product ['available']

    print(f"Название: {name}")
    print(f"Цена: {price}")
    print(f"Bec: {weight}")

    if available:
        print("В наличии!")
    else:
        print("Нет в наличии!")

    print() 