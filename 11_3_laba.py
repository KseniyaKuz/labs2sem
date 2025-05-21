import csv
filename = 'spisok.csv'
total = 0
print("Нужно купить:")

with open(filename, encoding='cp1251') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row['Продукт']
        quantity = int(row['Количество'])
        price = int(row['Цена'])
        print(f"{product} - {quantity} шт. за {price} руб.")
        total += quantity * price

print(f"Итоговая сумма: {total} руб.")