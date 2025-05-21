import json

with open('12.json', "r", encoding='utf-8') as file:
    data = json. load(file)

new_product = {
    "name": input("Введите название продукта: "),
    "price": int(input("Введите цену: ")),
    "available": input("В наличии? (да/нет): ").strip().lower() == "да",
    "weight": int(input("Введите вес (граммы): "))
}

data["products"].append(new_product)

with open("products.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("\nОбновленный список продуктов:\n")
for product in data["products"]:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Bec: {product['weight']}")

    if product["available"]:
        print("В наличии!")
    else:
        print("Нет в наличии!")
    print()
    