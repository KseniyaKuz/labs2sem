bukva_cenost = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10
}

slovo = input("Введите слово: ").upper()

stoimost = 0
for bukva in slovo:
    if bukva in bukva_cenost:
        stoimost += bukva_cenost[bukva]
    else:
        print(f"Буква '{bukva}' не учтена в правилах. Считаем как 0 очков.")

print(f"Слово '{slovo}' стоит {stoimost} очков.")