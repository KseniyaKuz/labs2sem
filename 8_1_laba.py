country_capital = {
    "Россия": "Москва",
    "Германия": "Берлин",
    "Франция": "Париж",
    "Италия": "Рим",
    "Япония": "Токио",
    "Китай": "Пекин",
    "Бразилия": "Бразилиа",
    "Канада": "Оттава"
}
print("a) Все страны и их столицы:")
for country, capital in country_capital.items():
    print(f"{country}: {capital}")

x_country = "Канада"
print(f"\nb) Столица страны {x_country}: {country_capital.get(x_country, 'Страна не найдена')}")

print("\nc) Словарь, отсортированный по названиям стран:")
for country in sorted(country_capital.keys()):
    print(f"{country}: {country_capital[country]}")